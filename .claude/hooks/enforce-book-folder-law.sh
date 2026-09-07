#!/bin/bash
# ============================================================================
# PreToolUse guard enforcing the BOOK FOLDER LAW for this repo:
#
#   Every book lives in its OWN folder under books/, and that folder is created
#   by tools/new-book.sh (or tools/new-series.sh). Nothing else.
#
#   - Book artifacts (STATE.yaml, foundation.md, outline.md, voice-dna.md,
#     character-bible.md, ENTITY_STATE.yaml, premise.md, manuscript chapters)
#     may ONLY be written inside books/<slug>/ or books/<series>/<book>/.
#   - A new book folder may NOT be hand-rolled with mkdir/cp — it is scaffolded
#     by tools/new-book.sh, so every book starts from the same complete skeleton
#     (STATE.yaml, the three mechanical gates, delivery/ebook.yaml, research/…).
#
# Enabled/disabled by BOOK_FOLDER_LAW in .claude/pipeline.conf (default: enforced).
# The decision itself lives in book_folder_law.py next to this file; this wrapper
# only reads the switch and passes the tool-call JSON through on stdin.
#
# Blocks by exiting 2 with an explanation on stderr, which Claude Code feeds back
# to the model instead of running the call. FAIL-OPEN on anything unexpected.
# ============================================================================
set -uo pipefail

BOOK_FOLDER_LAW="enforced"
REPO="${CLAUDE_PROJECT_DIR:-$PWD}"
CONF="$REPO/.claude/pipeline.conf"
if [ -f "$CONF" ]; then
  # shellcheck disable=SC1090
  source "$CONF"
fi
[ "${BOOK_FOLDER_LAW:-enforced}" = "enforced" ] || exit 0

GUARD="$(dirname "${BASH_SOURCE[0]}")/book_folder_law.py"
[ -f "$GUARD" ] || exit 0          # guard missing — allow rather than block blindly

CLAUDE_PROJECT_DIR="$REPO" python3 "$GUARD"
rc=$?

# 2 = the law was broken and the guard explained why on stderr. Anything else
# (including the guard itself failing) allows the call through.
[ "$rc" -eq 2 ] && exit 2
exit 0
