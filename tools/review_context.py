#!/usr/bin/env python3
"""
review_context.py — build the book-specific context block that the cross-model
second-opinion scripts (gemini_review.sh / grok_review.sh) prepend to a chapter.

Why this exists: the review prompts used to hardcode one specific book's series
context and editor persona, which quietly gave every other book the wrong editor
and the wrong expectations. Now the context is DERIVED from the book the chapter
lives in.

Resolution order (first hit wins):
  1. $REVIEW_CONTEXT            — explicit override in the environment.
  2. <book>/review-context.md   — hand-written per-book briefing (recommended for
                                  a book with settled canon; keep it under ~200 words).
  3. <book>/STATE.yaml          — derived: title, genre/subgenre, premise, comps,
                                  series name + position, register/voice note.
  4. Nothing                    — a generic "unnamed draft novel" line.

The book folder is found by walking UP from the chapter file to the nearest
directory containing STATE.yaml (so it works for books/<slug>/ and for a series
entry at books/<series>/<book>/ alike).

Usage:
    python3 tools/review_context.py <chapter.md> [--what persona|context]
      --what context  (default) prints the context block
      --what persona  prints the one-line editor persona
"""
import argparse
import os
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - yaml ships with the environment
    yaml = None


def find_book_dir(chapter_path):
    d = os.path.dirname(os.path.abspath(chapter_path))
    while True:
        if os.path.isfile(os.path.join(d, "STATE.yaml")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def load_state(book_dir):
    if not book_dir or yaml is None:
        return {}
    path = os.path.join(book_dir, "STATE.yaml")
    try:
        with open(path) as fh:
            data = yaml.safe_load(fh)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def persona(state):
    """The editor we ask the other model to be — derived from genre, not assumed."""
    proj = state.get("project") or {}
    genre = (proj.get("genre") or "").strip()
    sub = (proj.get("subgenre") or "").strip()
    comps = proj.get("comp_titles") or []
    comps = [str(c) for c in comps if str(c).strip()][:3]

    if sub and genre:
        band = f"{sub} ({genre})"
    else:
        band = sub or genre or "commercial fiction"

    line = f"You are a veteran acquiring editor of {band}."
    if comps:
        line += " Books you have edited sit alongside: " + ", ".join(comps) + "."
    line += (
        " You are giving a candid, specific SECOND OPINION on a single chapter of a draft"
        " novel, independent of the author's own pipeline. Flattery is worthless."
    )
    return line


def context(state, book_dir):
    """The book-specific briefing: what this draft is trying to be."""
    proj = state.get("project") or {}
    bits = []

    title = (proj.get("title") or "").strip()
    series = state.get("series") or {}
    if isinstance(series, dict) and (series.get("name") or "").strip():
        pos = series.get("position")
        pos_txt = f", book {pos}" if pos else ""
        bits.append(f"Book: '{title or 'untitled'}' — {series['name']}{pos_txt}.")
    elif title:
        bits.append(f"Book: '{title}' (standalone).")

    genre = (proj.get("genre") or "").strip()
    sub = (proj.get("subgenre") or "").strip()
    if genre or sub:
        bits.append("Genre: " + " / ".join(x for x in (genre, sub) if x) + ".")

    premise = (proj.get("premise") or "").strip()
    if premise and not premise.startswith("<"):
        bits.append(f"Premise: {premise}")

    comps = [str(c) for c in (proj.get("comp_titles") or []) if str(c).strip()]
    if comps:
        bits.append("Comps: " + ", ".join(comps[:5]) + ".")

    # Canon guardrails are the most useful thing to hand an outside reader: they stop
    # it from "fixing" settled author decisions.
    rails = [
        str(g) for g in (state.get("guardrails") or [])
        if str(g).strip() and not str(g).startswith("<")
        and not str(g).lower().startswith(("genesis floor", "style gate", "word floor"))
    ]
    if rails:
        bits.append("Settled canon/guardrails (do NOT propose undoing these): " + " ".join(rails[:4]))

    if not bits:
        return "This is a chapter from an unnamed draft novel; judge it on its own terms."
    return "\n".join(bits)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("--what", choices=["context", "persona"], default="context")
    args = ap.parse_args()

    override = os.environ.get("REVIEW_CONTEXT", "").strip()
    book_dir = find_book_dir(args.chapter)
    state = load_state(book_dir)

    if args.what == "persona":
        print(persona(state))
        return

    if override:
        print(override)
        return

    if book_dir:
        brief = os.path.join(book_dir, "review-context.md")
        if os.path.isfile(brief):
            with open(brief) as fh:
                text = fh.read().strip()
            if text:
                print(text)
                return

    print(context(state, book_dir))


if __name__ == "__main__":
    sys.exit(main())
