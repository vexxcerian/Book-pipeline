#!/bin/bash
# ============================================================================
# ACCOUNT-WIDE book-pipeline installer for Claude Code on the web.
#
# Paste this into your Environment's "setup script" (web UI: environment
# settings). It runs at the start of EVERY session, for EVERY repo, and installs
# YOUR customized pipeline (from the knightdx91-alt/book-pipeline repo) into
# ~/.claude/ — so any new book repo works with zero per-repo copying, and every
# tweak you push to book-pipeline propagates everywhere automatically.
#
# Idempotent + non-interactive. Safe to run every session.
# ============================================================================
set -euo pipefail
[ "${CLAUDE_CODE_REMOTE:-}" != "true" ] && exit 0

CFG="$HOME/.book-pipeline-src"

# 1) Default all sub-agents to Opus.
[ -n "${CLAUDE_ENV_FILE:-}" ] && echo 'export ANTHROPIC_MODEL=claude-opus-4-8' >> "$CLAUDE_ENV_FILE"

# 2) Build toolchain (PDF/style/grammar gates).
python3 -c 'import reportlab' 2>/dev/null || pip install --quiet reportlab pillow || true
command -v gs >/dev/null 2>&1 || { apt-get install -y ghostscript || sudo apt-get install -y ghostscript; } 2>/dev/null || true
python3 -c 'import language_tool_python' 2>/dev/null || pip install --quiet language-tool-python || true

# 3) Pull the canonical, CUSTOMIZED pipeline from book-pipeline (your source of truth).
#    book-pipeline must be in this session's repo scope so the git proxy allows it.
if [ -d "$CFG/.git" ]; then
  git -C "$CFG" fetch --depth 1 origin main 2>/dev/null && git -C "$CFG" reset --hard origin/main 2>/dev/null || true
else
  rm -rf "$CFG"
  git clone --depth 1 https://github.com/knightdx91-alt/book-pipeline "$CFG" 2>/dev/null || true
fi

# 4) Install YOUR customized agents/commands/settings/apodictic into ~/.claude.
if [ -d "$CFG/.claude" ]; then
  mkdir -p "$HOME/.claude/agents" "$HOME/.claude/commands"
  cp -f "$CFG/.claude/agents/"*.md   "$HOME/.claude/agents/"   2>/dev/null || true
  cp -f "$CFG/.claude/commands/"*.md "$HOME/.claude/commands/" 2>/dev/null || true
  # APODICTIC plugin, enabled at user level.
  if [ -d "$CFG/tools/apodictic" ]; then
    rm -rf "$HOME/.claude/apodictic"; cp -R "$CFG/tools/apodictic" "$HOME/.claude/apodictic"
    python3 - <<'PY'
import json, os
p = os.path.expanduser("~/.claude/settings.json"); s = {}
if os.path.exists(p):
    try: s = json.load(open(p))
    except Exception: s = {}
s.setdefault("extraKnownMarketplaces", {})["apodictic"] = {
    "source": {"source": "directory", "path": os.path.expanduser("~/.claude/apodictic")}}
s.setdefault("enabledPlugins", {})["apodictic@apodictic"] = True
json.dump(s, open(p, "w"), indent=2)
PY
  fi
  # Expose the repo generator + folder scaffolder on PATH for convenience.
  mkdir -p "$HOME/.local/bin"
  [ -f "$CFG/new_book_repo.sh" ] && install -m 0755 "$CFG/new_book_repo.sh" "$HOME/.local/bin/new-book-repo" 2>/dev/null || true
  case ":$PATH:" in *":$HOME/.local/bin:"*) : ;; *) [ -n "${CLAUDE_ENV_FILE:-}" ] && echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE" ;; esac
  echo "book-pipeline installed: $(ls "$HOME/.claude/agents" | wc -l) agents, $(ls "$HOME/.claude/commands" 2>/dev/null | wc -l) commands. New book repo: 'new-book-repo <slug> \"<Title>\"'."
else
  echo "warn: book-pipeline clone unavailable — ensure the repo is in this environment's scope." >&2
fi
