#!/usr/bin/env bash
# ============================================================================
# new_book_repo.sh — generate a COMPLETE, standalone book REPO (not just a
# folder), fully wired with the pipeline, ready to push to GitHub on `main`.
#
# Usage:
#   bash new_book_repo.sh <slug> "<Book Title>" [git-remote-url]
#
# Examples:
#   bash new_book_repo.sh the-glass-road "The Glass Road"
#   bash new_book_repo.sh the-glass-road "The Glass Road" https://github.com/knightdx91-alt/the-glass-road
#
# What it does:
#   1. Creates ./<slug>/ as a fresh git repo on `main`.
#   2. Seeds the pipeline from book-pipeline (agents/commands/apodictic into
#      .claude/ + tools/), so the repo is self-contained.
#   3. Writes the root CLAUDE.md (workflow Law + pipeline source-of-truth + update rule).
#   4. Scaffolds book/genesis/<slug>/ from the template (STATE/CLAUDE/style_check).
#   5. Commits everything.
#   6. If a remote URL is given AND the empty repo already exists on GitHub, pushes.
#      Otherwise prints the exact create-repo + push steps (GitHub repo creation
#      cannot be automated from inside a Claude session — 403).
# ============================================================================
set -euo pipefail

SLUG="${1:-}"; TITLE="${2:-}"; REMOTE="${3:-}"
if [[ -z "$SLUG" || -z "$TITLE" ]]; then
  echo "usage: bash new_book_repo.sh <slug> \"<Book Title>\" [git-remote-url]" >&2; exit 1
fi
TODAY="$(date +%Y-%m-%d)"
DEST="$(pwd)/$SLUG"
[[ -e "$DEST" ]] && { echo "error: $DEST already exists" >&2; exit 1; }

# --- Locate the pipeline source (book-pipeline) ---
CFG="$HOME/.book-pipeline-src"
if [[ -d "$CFG/.git" ]]; then
  git -C "$CFG" fetch --depth 1 origin main >/dev/null 2>&1 && git -C "$CFG" reset --hard origin/main >/dev/null 2>&1 || true
else
  git clone --depth 1 https://github.com/knightdx91-alt/book-pipeline "$CFG" >/dev/null 2>&1 \
    || { echo "error: cannot reach book-pipeline; add it to this environment's repo scope." >&2; exit 1; }
fi

# --- 1. Fresh repo on main ---
mkdir -p "$DEST"; cd "$DEST"
git init -q; git checkout -B main >/dev/null 2>&1
git config user.email noreply@anthropic.com; git config user.name Claude

# --- 2. Seed the pipeline (self-contained) ---
cp -R "$CFG/.claude" "$DEST/.claude"
mkdir -p "$DEST/tools"; cp -R "$CFG/tools/apodictic" "$DEST/tools/apodictic"

# --- 3. Root CLAUDE.md ---
cat > "$DEST/CLAUDE.md" <<EOF
# CLAUDE.md — $TITLE

Guidance for Claude Code working in this repository. **Read this first, every session.**

## ⚖️ WORKFLOW LAW — READ EVERY SESSION (non-negotiable)

**We work ONLY on \`main\`. ALWAYS. This is Law.** No other branch, ever. No PRs (not
even drafts). Everything commits and pushes straight to \`main\`. If a session starts on
some other branch (e.g. \`claude/...\`), push your work to \`main\` directly. The only
exception is when the author (Terry) explicitly says otherwise for a task.

Git identity: \`git config user.email noreply@anthropic.com && git config user.name Claude\`

## What this repo is

Working repo for the book **$TITLE**. The active pipeline project lives at
\`book/genesis/$SLUG/\` — read its own \`STATE.yaml\` and \`feedback/progress.md\` first.

## 🔧 Pipeline source of truth — book-pipeline (READ + OBEY THE UPDATE RULE)

The book-writing pipeline (the \`book-*\` agents, \`/gemini\` + \`/grok\` commands, APODICTIC)
is shared from **knightdx91-alt/book-pipeline**, installed into \`~/.claude/\` each session by
the environment setup script (a self-contained copy also lives in this repo's \`.claude/\`).
It is the ONE place the pipeline is edited.

**UPDATE RULE:** anytime you make the pipeline better — a new agent/tool, a tweak to an
agent/command/gate, or a better entry to a shared list (anti-AI pattern, craft-mistake
rule, structural-variety option) — commit it to **book-pipeline** and push, so every book
inherits it. Do NOT strand improvements in one book. (Per-book style_check ALLOWLISTs are
the exception — those stay here, seeded from the template.)
EOF

# --- 4. Scaffold the book project from the template ---
TPL="$CFG/book/genesis/_template"
BOOK="$DEST/book/genesis/$SLUG"
mkdir -p "$BOOK"/{research,manuscript/chapters,evaluations/continuity,feedback,delivery/editorial,delivery/production,voice-bank/samples,tools}
if [[ -d "$TPL" ]]; then
  [[ -f "$TPL/STATE.yaml" ]]           && cp "$TPL/STATE.yaml" "$BOOK/STATE.yaml"
  [[ -f "$TPL/CLAUDE.md" ]]            && cp "$TPL/CLAUDE.md" "$BOOK/CLAUDE.md"
  [[ -f "$TPL/tools/style_check.py" ]] && cp "$TPL/tools/style_check.py" "$BOOK/tools/style_check.py"
  sed -i "s|<BOOK TITLE>|$TITLE|g; s|<YYYY-MM-DD>|$TODAY|g" "$BOOK/STATE.yaml" "$BOOK/CLAUDE.md" 2>/dev/null || true
else
  echo "note: _template not found in book-pipeline; created empty project structure." >&2
fi
cat > "$BOOK/feedback/progress.md" <<EOF
# Progress — $TITLE

Scaffolded $TODAY by new_book_repo.sh.

## Next steps
1. Stage source material into research/ (draft + any roadmap/bible).
2. Fill STATE.yaml (premise, genre, comps, canon, guardrails, open decisions).
3. Edit tools/style_check.py ALLOWLIST with this book's deliberate motifs.
4. Architect pass — foundation.md + outline.md. NOTE: the architect now SELECTS a
   macro-structure per book (Section 0.5) — it will NOT default to 3-act/20-chapters.
5. Run the chapter loop in order; commit per chapter.

## Resume point
Nothing drafted yet.
EOF

# --- 5. Commit ---
git add -A
git commit -q -m "Scaffold $TITLE: standalone book repo on main + full pipeline

Self-contained repo (workflow Law, pipeline .claude/ + apodictic, templated
book/genesis/$SLUG/ project). Ready for source material + architect pass."

echo "Created repo: $DEST (branch main, $(git rev-list --count HEAD) commit)."

# --- 6. Push (only if the empty GitHub repo already exists) ---
if [[ -n "$REMOTE" ]]; then
  git remote add origin "$REMOTE"
  if git push -u origin main 2>/dev/null; then
    echo "Pushed to $REMOTE (main)."
  else
    echo ""
    echo "Push failed — the GitHub repo probably doesn't exist yet (creation can't be"
    echo "automated from a Claude session). Do this:"
    echo "  1. Create an EMPTY repo on GitHub named '$SLUG' (no README)."
    echo "  2. Then run:  git -C \"$DEST\" push -u origin main"
  fi
else
  echo ""
  echo "Next: create an EMPTY GitHub repo named '$SLUG', then:"
  echo "  git -C \"$DEST\" remote add origin https://github.com/knightdx91-alt/$SLUG"
  echo "  git -C \"$DEST\" push -u origin main"
fi
