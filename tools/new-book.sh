#!/usr/bin/env bash
# ============================================================================
# new-book.sh — scaffold a new book FOLDER inside this monorepo (books/<slug>/)
# from books/_template/. No new repo, no GitHub step — everything lives on `main`.
#
# Usage:
#   bash tools/new-book.sh <slug> "<Book Title>" [--series <series-slug> [--position N]]
#
# Examples:
#   bash tools/new-book.sh the-glass-road "The Glass Road"
#   bash tools/new-book.sh emberfall-book-2 "A Vault of Ash" --series emberfall --position 2
#
# With --series the book is created at books/<series-slug>/<slug>/ instead, and its
# STATE.yaml gets a filled-in `series:` block (bible + previous book) so the pipeline
# carries canon forward. See docs/SERIES.md.
#
# Run from the repo root.
# ============================================================================
set -euo pipefail

SLUG=""; TITLE=""; SERIES=""; POSITION=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --series)   SERIES="${2:-}"; shift 2 ;;
    --position) POSITION="${2:-}"; shift 2 ;;
    -h|--help)  sed -n '2,18p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *)
      if [[ -z "$SLUG" ]]; then SLUG="$1"
      elif [[ -z "$TITLE" ]]; then TITLE="$1"
      else echo "error: unexpected argument '$1'" >&2; exit 1; fi
      shift ;;
  esac
done

if [[ -z "$SLUG" || -z "$TITLE" ]]; then
  echo 'usage: bash tools/new-book.sh <slug> "<Book Title>" [--series <series-slug> [--position N]]' >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TPL="$ROOT/books/_template"
TODAY="$(date +%Y-%m-%d)"

if [[ -n "$SERIES" ]]; then
  SERIES_DIR="$ROOT/books/$SERIES"
  [[ -d "$SERIES_DIR" ]] || {
    echo "error: series folder books/$SERIES does not exist." >&2
    echo "       create it first: bash tools/new-series.sh $SERIES \"<Series Name>\"" >&2
    exit 1; }
  DEST="$SERIES_DIR/$SLUG"
  REL="books/$SERIES/$SLUG"
else
  DEST="$ROOT/books/$SLUG"
  REL="books/$SLUG"
fi

[[ -d "$TPL" ]] || { echo "error: template not found at $TPL" >&2; exit 1; }
[[ -e "$DEST" ]] && { echo "error: $DEST already exists" >&2; exit 1; }

# Full working structure for a book project.
mkdir -p "$DEST"/{research,manuscript/chapters,evaluations/continuity,feedback,delivery/editorial,delivery/production,voice-bank/samples,tools}

# Seed from the template.
[[ -f "$TPL/STATE.yaml" ]]            && cp "$TPL/STATE.yaml" "$DEST/STATE.yaml"
[[ -f "$TPL/CLAUDE.md" ]]             && cp "$TPL/CLAUDE.md"  "$DEST/CLAUDE.md"
[[ -f "$TPL/character-bible.md" ]]    && cp "$TPL/character-bible.md" "$DEST/character-bible.md"
[[ -f "$TPL/tools/style_check.py" ]]  && cp "$TPL/tools/style_check.py"  "$DEST/tools/style_check.py"
[[ -f "$TPL/tools/grammar_check.py" ]]&& cp "$TPL/tools/grammar_check.py" "$DEST/tools/grammar_check.py"
[[ -f "$TPL/tools/voice_wear_check.py" ]]&& cp "$TPL/tools/voice_wear_check.py" "$DEST/tools/voice_wear_check.py"
[[ -f "$TPL/delivery/ebook.yaml" ]]     && cp "$TPL/delivery/ebook.yaml" "$DEST/delivery/ebook.yaml"

# Fill placeholders.
sed -i "s|<BOOK TITLE>|$TITLE|g; s|<YYYY-MM-DD>|$TODAY|g; s|books/<slug>|$REL|g" \
  "$DEST/STATE.yaml" "$DEST/CLAUDE.md" "$DEST/character-bible.md" 2>/dev/null || true

# Series wiring: uncomment and fill the series: block in STATE.yaml.
if [[ -n "$SERIES" ]]; then
  SERIES_NAME="$(sed -n 's|^# ||p' "$ROOT/books/$SERIES/README.md" 2>/dev/null | head -1)"
  SERIES_NAME="${SERIES_NAME:-$SERIES}"
  POSITION="${POSITION:-0}"

  # The previous book is the sibling folder at position N-1, if we can find one.
  PREV=""
  if [[ "$POSITION" =~ ^[0-9]+$ ]] && [[ "$POSITION" -gt 1 ]]; then
    while IFS= read -r cand; do
      [[ -f "$cand/STATE.yaml" ]] || continue
      p="$(grep -E '^\s+position:' "$cand/STATE.yaml" 2>/dev/null | head -1 | grep -oE '[0-9]+' || true)"
      [[ "$p" == "$((POSITION - 1))" ]] && PREV="../$(basename "$cand")"
    done < <(find "$ROOT/books/$SERIES" -mindepth 1 -maxdepth 1 -type d)
  fi

  python3 - "$DEST/STATE.yaml" "$SERIES_NAME" "$POSITION" "$PREV" <<'PY'
import sys
path, name, position, prev = sys.argv[1:5]
s = open(path).read()
block = f'''series:
  name: "{name}"
  position: {position}
  bible: "../SERIES-BIBLE.md"        # canon shared by every book in the series
  previous_book: "{prev}"{"" if prev else "    # set once an earlier book exists"}
  carry_forward: [character-bible.md, ENTITY_STATE.yaml, voice-dna.md]
'''
marker = '# SERIES — delete this block for a standalone book. See docs/SERIES.md.\n'
start = s.find(marker)
if start != -1:
    end = s.find('\ndecisions:', start)
    s = s[:start] + '# SERIES — this book is part of a series. See docs/SERIES.md.\n' + block + '\n' + s[end + 1:]
else:
    s = s.rstrip() + '\n\n' + block
open(path, 'w').write(s)
PY
fi

cat > "$DEST/feedback/progress.md" <<EOF
# Progress — $TITLE

Scaffolded $TODAY by tools/new-book.sh into $REL/.

## Next steps
1. Stage source material into research/ (draft + any roadmap/bible).
2. Fill STATE.yaml (premise, genre, comps, canon, guardrails, open decisions).
3. Edit tools/style_check.py ALLOWLIST with this book's deliberate motifs.
4. Architect pass — foundation.md + outline.md + voice-dna.md + character-bible.md.
   The architect SELECTS a macro-structure per book (Section 0.5); it will NOT
   default to 3-act/20-chapters.
5. Run the chapter loop in order; commit per chapter.

## Resume point
Nothing drafted yet.
EOF

if [[ -n "$SERIES" ]]; then
  cat >> "$DEST/feedback/progress.md" <<EOF

## Series
Part of "$SERIES_NAME" (position ${POSITION}). Read \`books/$SERIES/SERIES-BIBLE.md\` before
the architect runs, and run the carry-over checklist at the bottom of it (character bible,
ENTITY_STATE, naming registry). Add this book to the series README table.
EOF
fi

echo "Created $REL/ (\"$TITLE\"). Next: stage source material, fill STATE.yaml, run the architect."
[[ -n "$SERIES" ]] && echo "Series wiring written to $REL/STATE.yaml — now do the carry-over checklist in books/$SERIES/SERIES-BIBLE.md."
echo "Then commit:  git add $REL && git commit -m \"Scaffold $TITLE\""
