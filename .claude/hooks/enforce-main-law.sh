#!/bin/bash
# ============================================================================
# PreToolUse guard enforcing WORKFLOW LAW for the Books repo:
#   - No creating new branches (main ONLY).
#   - No pull requests (commit + push straight to main).
# Enabled/disabled by WORKFLOW_LAW in .claude/pipeline.conf (default: main-only).
# Blocks the offending tool call by exiting 2 with an explanation on stderr,
# which Claude Code feeds back to the model instead of running the command.
# Reads the tool-call JSON on stdin.
# ============================================================================
set -euo pipefail
INPUT="$(cat)"

# Repo config decides whether the law is enforced at all. A fork that wants a normal
# branch/PR workflow sets WORKFLOW_LAW="off" in .claude/pipeline.conf.
WORKFLOW_LAW="main-only"
CONF="${CLAUDE_PROJECT_DIR:-$PWD}/.claude/pipeline.conf"
if [ -f "$CONF" ]; then
  # shellcheck disable=SC1090
  source "$CONF"
fi
[ "$WORKFLOW_LAW" = "main-only" ] || exit 0

block () {
  echo "⚖️ WORKFLOW LAW (Books repo): $1 We work ONLY on main — no new branches, no PRs. Commit and push straight to main." >&2
  exit 2
}

TOOL="$(printf '%s' "$INPUT" | python3 -c 'import sys,json; print(json.load(sys.stdin).get("tool_name",""))' 2>/dev/null || echo)"

# Block PR-related MCP tools outright.
case "$TOOL" in
  *create_pull_request*|*enable_pr_auto_merge*|*create_and_submit_pull_request*)
    block "opening/auto-merging pull requests is forbidden." ;;
esac

# For Bash calls, inspect the command string.
CMD="$(printf '%s' "$INPUT" | python3 -c 'import sys,json; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null || echo)"
[ -z "$CMD" ] && exit 0
norm="$(printf '%s' "$CMD" | tr '\n' ' ')"

# Branch creation
echo "$norm" | grep -qE 'git[[:space:]]+checkout[[:space:]]+-[bB]([[:space:]]|$)'  && block "creating a branch via 'git checkout -b' is forbidden."
echo "$norm" | grep -qE 'git[[:space:]]+switch[[:space:]]+-[cC]([[:space:]]|$)'    && block "creating a branch via 'git switch -c' is forbidden."
# 'git branch <name>' (a bare name, not an option/flag) creates a branch
echo "$norm" | grep -qE 'git[[:space:]]+branch[[:space:]]+[A-Za-z0-9]' && block "creating a branch via 'git branch <name>' is forbidden."
# Pull requests via gh CLI
echo "$norm" | grep -qE '\bgh[[:space:]]+pr[[:space:]]+create\b' && block "opening pull requests is forbidden."

exit 0
