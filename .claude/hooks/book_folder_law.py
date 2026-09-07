#!/usr/bin/env python3
"""Decide whether a tool call violates the BOOK FOLDER LAW.

Reads the PreToolUse JSON on stdin. Exits 2 (with an explanation on stderr) to
block the call, 0 to allow it. Driven by .claude/hooks/enforce-book-folder-law.sh,
which owns the on/off switch in .claude/pipeline.conf.

The law, in one line: every book lives in its own folder under books/, and that
folder is created by tools/new-book.sh — never by hand.

FAIL-OPEN by construction: every unexpected condition allows the call. A guard
that bricks a writing session is worse than a guard that misses one case.
"""

import json
import os
import re
import sys

# Files that only ever belong to a single book.
ARTIFACTS = {
    "STATE.yaml",
    "ENTITY_STATE.yaml",
    "foundation.md",
    "outline.md",
    "voice-dna.md",
    "character-bible.md",
    "premise.md",
}
CHAPTER_RE = re.compile(r"^chapter-\d+[a-z]?\.md$", re.I)

# Shared-pipeline areas. The template lives here, and so do the docs that
# *describe* these artifacts. Never book content, so never the law's business.
EXEMPT_PREFIXES = (
    ".claude/",
    "docs/",
    "tools/",
    "books/_template/",
    "books/_series-template/",
    "books/_assets/",
)

WRITING_TOOLS = ("Write", "Edit", "MultiEdit", "NotebookEdit")

HOW_TO = """   Every book lives in its OWN folder, and that folder is scaffolded by the tool:
       bash tools/new-book.sh <slug> "<Book Title>"
       bash tools/new-book.sh <slug> "<Book Title>" --series <series-slug> --position N
   (a brand-new series starts with: bash tools/new-series.sh <series-slug> "<Series Name>")
   Then write every book artifact INSIDE books/<slug>/ (or books/<series>/<book>/).
   The shared pipeline (.claude/, tools/, docs/) is never a place to keep book content.
"""


def block(reason, path=None):
    where = "\n   Offending path: %s" % path if path else ""
    sys.stderr.write(
        "⚖️ BOOK FOLDER LAW (Book-pipeline): %s%s\n%s" % (reason, where, HOW_TO)
    )
    sys.exit(2)


def relative(repo, path):
    """Repo-relative POSIX path, or None if it is outside the repo."""
    if not path:
        return None
    absolute = path if os.path.isabs(path) else os.path.join(repo, path)
    absolute = os.path.realpath(os.path.normpath(absolute))
    if absolute == repo:
        return ""
    if not absolute.startswith(repo + os.sep):
        return None  # outside the repo — not ours to police
    return absolute[len(repo) + 1:].replace(os.sep, "/")


def exempt(rel):
    return any(rel.startswith(prefix) for prefix in EXEMPT_PREFIXES)


def is_artifact(rel):
    base = rel.rsplit("/", 1)[-1]
    return (
        base in ARTIFACTS
        or bool(CHAPTER_RE.match(base))
        or "/manuscript/chapters/" in "/" + rel
    )


def in_book_folder(rel):
    """books/<slug>/… or books/<series>/<book>/… — at least one level below books/."""
    parts = rel.split("/")
    return len(parts) >= 3 and parts[0] == "books" and not parts[1].startswith("_")


def book_root(rel):
    """The book (or series) folder a books/… path belongs to, if any."""
    parts = rel.split("/")
    if len(parts) < 2 or parts[0] != "books":
        return None
    return "books/" + parts[1]


def check_write(repo, tool_input):
    rel = relative(repo, tool_input.get("file_path") or tool_input.get("notebook_path"))
    if not rel or exempt(rel):
        return
    if is_artifact(rel) and not in_book_folder(rel):
        block("a book artifact may only be written inside a book folder under books/.", rel)


PATH_CHARS = r"[A-Za-z0-9_./~$@:{}-]+"


def creation_targets(command):
    """Paths a shell command would CREATE or overwrite.

    Deliberately narrow: a redirect target, an argument to touch/tee, and the
    destination of cp/mv/install. Everything else a command merely mentions —
    what it reads, greps, counts or deletes — is none of the law's business.
    """
    targets = []

    # foo > path, foo >> path
    targets += re.findall(r">>?\s*(" + PATH_CHARS + ")", command)

    # touch a b c   |   tee -a path
    for segment in re.split(r"[;&|]+", command):
        words = segment.split()
        for i, word in enumerate(words):
            if os.path.basename(word) in ("touch", "tee"):
                targets += [w for w in words[i + 1:] if not w.startswith("-")]
                break

    # cp/mv/install src… dest  — the destination is the last non-flag argument
    for segment in re.split(r"[;&|]+", command):
        words = segment.split()
        for i, word in enumerate(words):
            if os.path.basename(word) in ("cp", "mv", "install"):
                args = [w for w in words[i + 1:] if not w.startswith("-")]
                if len(args) >= 2:
                    targets.append(args[-1])
                break

    return targets


def check_bash(repo, tool_input):
    command = (tool_input.get("command") or "").replace("\n", " ")
    if not command.strip():
        return

    # The sanctioned scaffolders are always allowed — they ARE the law.
    if re.search(r"tools/new-(book|series)\.sh", command):
        return

    tokens = re.findall(r"[A-Za-z0-9_./~$@:{}-]+", command)

    # 1) Creating a NEW book folder by hand (mkdir / cp -r / rsync / install into books/…).
    #    `mv` is deliberately absent: renaming an already-scaffolded book folder moves a
    #    complete skeleton, which is exactly what the law wants to preserve.
    if re.search(r"\b(mkdir|cp|rsync|install)\b", command):
        for token in tokens:
            if not (token.startswith("books/") or "/books/" in token):
                continue
            rel = relative(repo, token)
            if rel is None or not rel.startswith("books/"):
                continue
            root = book_root(rel)
            if (
                root
                and not root.rsplit("/", 1)[-1].startswith("_")
                and not os.path.isdir(os.path.join(repo, root))
            ):
                block(
                    "creating a book folder by hand is forbidden — scaffold it with the "
                    "tool so every book starts from the same complete, checked skeleton.",
                    rel,
                )

    # 2) CREATING a book artifact somewhere that is not a book folder.
    #    Only creation targets count — reading, grepping or removing a stray file must
    #    stay possible, not least because removing it is the fix.
    #    Skipped when the command changes directory: a token then resolves against a
    #    cwd this guard cannot know, and a false block is worse than a missed one.
    #    The Write/Edit check above is the load-bearing one.
    if re.search(r"(^|[;&|]\s*)cd\s", command):
        return
    for target in creation_targets(command):
        rel = relative(repo, target)
        if not rel or exempt(rel):
            continue
        if is_artifact(rel) and not in_book_folder(rel):
            block(
                "a book artifact may only be created inside a book folder under books/.",
                rel,
            )


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return  # unreadable payload — allow

    repo = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
    tool = data.get("tool_name") or ""
    tool_input = data.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        return

    if tool in WRITING_TOOLS:
        check_write(repo, tool_input)
    elif tool == "Bash":
        check_bash(repo, tool_input)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        pass  # fail open — never let a guard bug stop the work
    sys.exit(0)
