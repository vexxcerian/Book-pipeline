#!/usr/bin/env bash
# ============================================================================
# new-series.sh — scaffold a SERIES folder inside this monorepo.
#
# A series is a folder under books/ that holds several book folders plus the
# canon they share (SERIES-BIBLE.md) and any production tooling used by all of
# them. Each book inside is a normal book project using the shared root pipeline.
#
# Usage:
#   bash tools/new-series.sh <series-slug> "<Series Name>" [first-book-slug "First Book Title"]
#
# Examples:
#   bash tools/new-series.sh emberfall "The Emberfall Cycle"
#   bash tools/new-series.sh emberfall "The Emberfall Cycle" emberfall-book-1 "A Crown of Cinders"
#
# Run from the repo root. See docs/SERIES.md for the full workflow.
# ============================================================================
set -euo pipefail

SLUG="${1:-}"; NAME="${2:-}"; BOOK_SLUG="${3:-}"; BOOK_TITLE="${4:-}"
if [[ -z "$SLUG" || -z "$NAME" ]]; then
  echo 'usage: bash tools/new-series.sh <series-slug> "<Series Name>" [first-book-slug "First Book Title"]' >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TPL="$ROOT/books/_series-template"
DEST="$ROOT/books/$SLUG"

[[ -d "$TPL" ]] || { echo "error: series template not found at $TPL" >&2; exit 1; }
[[ -e "$DEST" ]] && { echo "error: $DEST already exists" >&2; exit 1; }

mkdir -p "$DEST"
cp "$TPL/SERIES-BIBLE.md" "$DEST/SERIES-BIBLE.md"
cp "$TPL/README.md"       "$DEST/README.md"
sed -i "s|<SERIES NAME>|$NAME|g" "$DEST/SERIES-BIBLE.md" "$DEST/README.md"

echo "Created books/$SLUG/ (\"$NAME\") with SERIES-BIBLE.md + README.md."

if [[ -n "$BOOK_SLUG" && -n "$BOOK_TITLE" ]]; then
  bash "$ROOT/tools/new-book.sh" "$BOOK_SLUG" "$BOOK_TITLE" --series "$SLUG" --position 1
else
  echo
  echo "Next: add the first book —"
  echo "  bash tools/new-book.sh <book-slug> \"<Book Title>\" --series $SLUG --position 1"
fi

echo
echo "Then: fill SERIES-BIBLE.md (world rules, cast, arc, naming registry) BEFORE the architect"
echo "runs on book one — the bible is what every later book is held to."
