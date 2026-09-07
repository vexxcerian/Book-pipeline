#!/bin/bash
# ============================================================================
# Environment setup script for the Books pipeline (Claude Code on the web).
#
# Paste this into your Environment's "setup script" field in the web UI. It runs
# once per session, BEFORE the session starts, and installs the toolchain the
# pipeline's build and gate scripts need.
#
# It deliberately does NOT install the agents. The 12 book-* agents live in this
# repo at .claude/agents/ and are loaded from the clone directly — that is also
# the only place they can be dispatched by name from, because the agent registry
# is built before any hook runs. .claude/hooks/session-start.sh handles the rest.
#
# Idempotent and non-interactive. Safe to run every session.
# ============================================================================
set -euo pipefail

# Only meaningful in the remote (web) environment. Locally, run tools/install.sh.
[ "${CLAUDE_CODE_REMOTE:-}" != "true" ] && exit 0

# 1) Default all sub-agent dispatches to Opus. Without this they fall back to a
#    smaller model than the pipeline is written for.
[ -n "${CLAUDE_ENV_FILE:-}" ] && echo 'export ANTHROPIC_MODEL=claude-opus-4-8' >> "$CLAUDE_ENV_FILE"

# 2) Python build/gate dependencies.
#    pyyaml       — tools/review_context.py, tools/doctor.sh
#    reportlab    — build_pdf.py (print interiors)
#    pillow       — cover compositing / image handling
#    language-tool-python — grammar_check.py tier 2 (engine downloads on first use)
python3 -c 'import yaml'                 2>/dev/null || pip install --quiet pyyaml || true
python3 -c 'import reportlab'            2>/dev/null || pip install --quiet reportlab pillow || true
python3 -c 'import language_tool_python' 2>/dev/null || pip install --quiet language-tool-python || true

# 3) Ghostscript — the grayscale/CMYK no-ICC conversion for IngramSpark uploads.
command -v gs >/dev/null 2>&1 \
  || { apt-get install -y ghostscript || sudo apt-get install -y ghostscript; } 2>/dev/null \
  || true

echo "Books pipeline environment ready (agents load from the repo's .claude/agents/)."

# ---------------------------------------------------------------------------
# OPTIONAL — your own account-wide instructions.
#
# This script runs for every repo in the environment, so it is a convenient place
# to install a personal ~/.claude/CLAUDE.md. Nothing of the sort ships here: what
# belongs in your global instructions is yours, and a repo that installs its
# author's personal standing instructions into everyone else's account is a bug.
#
# To use it, uncomment and put your own text in:
#
# mkdir -p "$HOME/.claude"
# cat > "$HOME/.claude/CLAUDE.md" <<'EOF'
# <your own account-wide instructions>
# EOF
# ---------------------------------------------------------------------------
