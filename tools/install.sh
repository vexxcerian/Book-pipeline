#!/usr/bin/env bash
# ============================================================================
# install.sh — one-command setup for the Books pipeline on a LOCAL machine.
#
#   bash tools/install.sh
#
# The SessionStart hook only runs in Claude Code on the web; this is its local
# equivalent. It installs the Python dependencies, checks for Ghostscript, and
# copies the 12 book-* agents into ~/.claude/agents so they are dispatchable in
# local sessions.
#
# Idempotent. Safe to re-run after pulling pipeline changes.
# ============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENTS_DIR="$HOME/.claude/agents"

# Config (same file the hooks read).
PIPELINE_MAXTURNS="120"
[ -f "$ROOT/.claude/pipeline.conf" ] && source "$ROOT/.claude/pipeline.conf"

echo "Installing the Books pipeline from $ROOT"
echo

# ---------------------------------------------------------------------------
# 1) Python dependencies
# ---------------------------------------------------------------------------
echo "[1/3] Python dependencies"
if python3 -c 'import yaml, reportlab, PIL' 2>/dev/null; then
  echo "      already present (pyyaml, reportlab, pillow)"
else
  pip install --quiet -r "$ROOT/requirements.txt" 2>/dev/null \
    && echo "      installed from requirements.txt" \
    || echo "      warn: pip install failed — try: pip install -r requirements.txt" >&2
fi

# ---------------------------------------------------------------------------
# 2) Ghostscript (only needed for print PDF builds)
# ---------------------------------------------------------------------------
echo "[2/3] Ghostscript (print builds)"
if command -v gs >/dev/null 2>&1; then
  echo "      found: $(gs --version)"
else
  echo "      NOT found. Needed only for IngramSpark print files (tools/make_noicc.sh)."
  echo "      Install with:  apt-get install ghostscript   |   brew install ghostscript"
fi

# ---------------------------------------------------------------------------
# 3) Agents
# ---------------------------------------------------------------------------
echo "[3/3] Book pipeline agents -> $AGENTS_DIR"
mkdir -p "$AGENTS_DIR"
n=0
for f in "$ROOT"/.claude/agents/*.md; do
  [ -e "$f" ] || continue
  cp "$f" "$AGENTS_DIR/$(basename "$f")"
  n=$((n + 1))
done
for f in "$AGENTS_DIR"/*.md; do
  [ -e "$f" ] || continue
  grep -qiE '^maxTurns:' "$f" && sed -i.bak -E "s/^maxTurns: *[0-9]+/maxTurns: $PIPELINE_MAXTURNS/I" "$f" && rm -f "$f.bak"
done
echo "      installed $n agents (maxTurns normalized to $PIPELINE_MAXTURNS)"

echo
echo "Done. Verify with:  bash tools/doctor.sh"
echo "Start a book with:  bash tools/new-book.sh <slug> \"<Title>\""
