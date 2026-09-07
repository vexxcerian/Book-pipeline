#!/bin/bash
# SessionStart hook for the Books pipeline.
#
# Idempotent and non-interactive. Runs in every environment:
#   1. Enforces WORKFLOW_LAW (default: main-only) — see .claude/pipeline.conf.
#   2. Deploys the 12 book-* agents to ~/.claude/agents from THIS repo, so they are
#      available whether or not the session was started inside the repo.
#   3. Verifies both agent locations and reports anything missing.
# Remote (web) sessions additionally install the build toolchain, set the default model,
# and install the Gemini CLI when a key is present — a fresh container needs those; a
# local machine gets told what is missing instead of having pip and apt run on it.
#
# Everything it does is configurable in .claude/pipeline.conf — a fork that wants a
# branch/PR workflow sets WORKFLOW_LAW="off" there and this hook stops policing git.
set -euo pipefail

# Runs in EVERY environment. What it does depends on where it is:
#   everywhere  — enforce the workflow law, deploy the agents, verify.
#   remote only — install system/Python dependencies and set the default model. A fresh
#                 container needs them; someone's laptop does not want a hook silently
#                 running pip and apt, so locally we report what is missing instead.
REMOTE=0
[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] && REMOTE=1

REPO="${CLAUDE_PROJECT_DIR:-$PWD}"

# ---------------------------------------------------------------------------
# 0) Load repo config (with defaults, so a missing file is never fatal).
# ---------------------------------------------------------------------------
WORKFLOW_LAW="main-only"
AGENT_SOURCE="repo"
PIPELINE_MODEL="claude-opus-4-8"
PIPELINE_MAXTURNS="120"
INSTALL_GLOBAL_AGENTS="auto"
if [ -f "$REPO/.claude/pipeline.conf" ]; then
  # shellcheck disable=SC1091
  source "$REPO/.claude/pipeline.conf"
fi

# ============================================================================
# 1) ⚖️ WORKFLOW LAW — main ONLY (when enabled). No branches, no PRs.
# If this session starts on any branch other than main, switch to main and DELETE
# the stray branch. Uncommitted work is carried across via a stash pop so nothing
# in the working tree is lost.
# ============================================================================
if [ "$WORKFLOW_LAW" = "main-only" ] && git -C "$REPO" rev-parse --git-dir >/dev/null 2>&1; then
  CUR="$(git -C "$REPO" rev-parse --abbrev-ref HEAD 2>/dev/null || echo)"
  if [ -n "$CUR" ] && [ "$CUR" != "main" ] && [ "$CUR" != "HEAD" ]; then
    echo "⚖️  WORKFLOW LAW: session started on '$CUR' — switching to main and deleting the branch."
    if git -C "$REPO" stash push -u -m "law-autostash" >/dev/null 2>&1; then STASHED=1; else STASHED=0; fi
    git -C "$REPO" fetch origin main >/dev/null 2>&1 || true
    if git -C "$REPO" show-ref --verify --quiet refs/heads/main; then
      git -C "$REPO" checkout main >/dev/null 2>&1 || true
    else
      git -C "$REPO" checkout -B main origin/main >/dev/null 2>&1 || true
    fi
    [ "$STASHED" = "1" ] && git -C "$REPO" stash pop >/dev/null 2>&1 || true
    git -C "$REPO" branch -D "$CUR" >/dev/null 2>&1 || true
    echo "   Now on main; stray branch '$CUR' deleted (uncommitted work carried over)."
  fi
fi

AGENTS_DIR="$HOME/.claude/agents"
REPO_AGENTS="$REPO/.claude/agents"
mkdir -p "$AGENTS_DIR"

# ---------------------------------------------------------------------------
# 2) Default model for sub-agent dispatches. Without this, general-purpose agents
#    default to a smaller model than the pipeline is written for.
# ---------------------------------------------------------------------------
if [ "$REMOTE" = "1" ] && [ -n "${CLAUDE_ENV_FILE:-}" ] && [ -n "$PIPELINE_MODEL" ]; then
  echo "export ANTHROPIC_MODEL=$PIPELINE_MODEL" >> "$CLAUDE_ENV_FILE"
  echo "Set ANTHROPIC_MODEL=$PIPELINE_MODEL for this session."
fi

# ---------------------------------------------------------------------------
# 3) Manuscript-build toolchain. The PDF pipeline needs these in every fresh container.
# ---------------------------------------------------------------------------
if [ "$REMOTE" = "1" ]; then
if ! python3 -c 'import reportlab' >/dev/null 2>&1; then
  echo "Installing Python build deps (reportlab, pillow)..."
  pip install --quiet reportlab pillow >/dev/null 2>&1 \
    && echo "reportlab/pillow installed." \
    || echo "warn: pip install reportlab/pillow failed; build_pdf.py may not run." >&2
fi
if ! command -v gs >/dev/null 2>&1; then
  echo "Installing ghostscript (for PDF/X-1a CMYK conversion)..."
  { apt-get install -y ghostscript >/dev/null 2>&1 || sudo apt-get install -y ghostscript >/dev/null 2>&1; } \
    && echo "ghostscript installed ($(gs --version 2>/dev/null))." \
    || echo "warn: ghostscript install failed; make_pdfx.sh (PDF/X-1a) will be unavailable." >&2
fi

# grammar_check.py tier-2 (tense/agreement/dangling modifiers via LanguageTool).
# Tier 1 is dependency-free and always gates; tier 2 is the optional --languagetool layer.
# The ~250MB LanguageTool engine downloads lazily on first use (NOT here — keeps startup fast).
if ! python3 -c 'import language_tool_python' >/dev/null 2>&1; then
  echo "Installing language-tool-python (grammar_check.py tier-2; engine downloads on first use)..."
  pip install --quiet language-tool-python >/dev/null 2>&1 \
    && echo "language-tool-python installed." \
    || echo "warn: language-tool-python install failed; grammar_check.py --languagetool unavailable (tier 1 still gates)." >&2
fi
else
  # Local: never install anything behind the user's back — just say what is missing.
  MISSING=""
  python3 -c 'import yaml'      >/dev/null 2>&1 || MISSING="$MISSING pyyaml"
  python3 -c 'import reportlab' >/dev/null 2>&1 || MISSING="$MISSING reportlab"
  command -v gs >/dev/null 2>&1                 || MISSING="$MISSING ghostscript"
  [ -n "$MISSING" ] && echo "Book pipeline: missing$MISSING — run 'bash tools/install.sh' (ghostscript is only needed for print builds)."
fi

# ---------------------------------------------------------------------------
# 4) Install the 12 book-* agents into ~/.claude/agents.
#
#    DEFAULT (AGENT_SOURCE=repo): copy this repo's own committed agents. The repo
#    copies are the source of truth — they carry every improvement made under the
#    UPDATE RULE, and a fork stays self-contained with no network dependency.
#
#    AGENT_SOURCE=upstream: refetch the original Best Seller Studio project and
#    rebuild the four skill-based roles from it. This OVERWRITES the local copies
#    and drops this repo's improvements — only for deliberately tracking upstream.
# ---------------------------------------------------------------------------
EXPECTED=(book-orchestrator book-researcher book-architect book-writer \
  book-evaluator book-editor book-disruptor book-packager \
  entity-tracker continuity-guardian dialogue-polish hook-craft)

install_from_repo () {
  local n=0
  for a in "${EXPECTED[@]}"; do
    if [ -f "$REPO_AGENTS/$a.md" ]; then
      cp "$REPO_AGENTS/$a.md" "$AGENTS_DIR/$a.md"
      n=$((n + 1))
    fi
  done
  echo "Installed $n agent(s) into $AGENTS_DIR from the repo's .claude/agents/."
  [ "$n" -gt 0 ]
}

install_from_upstream () {
  # NOTE: do NOT use `git clone` here — the web environment's git proxy limits clones
  # to this repo (403). Fetch the tarball over HTTPS instead. Upstream default branch
  # is `master`.
  local url="https://codeload.github.com/felipelobomotta-blip/best-seller-studio/tar.gz/refs/heads/master"
  local dir="/tmp/bss"
  local ready=false

  if [ -f "$dir/agents/book-writer.md" ]; then
    ready=true
    echo "Upstream BSS already present at $dir, skipping download."
  else
    for attempt in 1 2 3; do
      rm -rf "$dir"; mkdir -p "$dir"
      if curl -sSL --cacert /root/.ccr/ca-bundle.crt -o /tmp/bss.tar.gz "$url" 2>/dev/null \
         && tar xzf /tmp/bss.tar.gz -C "$dir" --strip-components=1 2>/dev/null \
         && [ -f "$dir/agents/book-writer.md" ]; then
        ready=true; echo "Upstream BSS downloaded (attempt $attempt)."; break
      fi
      echo "warn: BSS download attempt $attempt failed; retrying..." >&2
      sleep $((attempt * 2))
    done
  fi
  [ "$ready" = true ] || { echo "ERROR: could not fetch upstream BSS." >&2; return 1; }

  cp "$dir"/agents/*.md "$AGENTS_DIR"/

  # The four skill-based roles need agent frontmatter wrapped around the SKILL.md body.
  make_agent () {
    local name="$1" src="$2" desc="$3"
    [ -f "$src" ] || { echo "warn: missing $src, skipping $name" >&2; return 0; }
    {
      printf -- '---\n'
      printf 'name: %s\n' "$name"
      printf 'description: %s\n' "$desc"
      printf 'tools: Read, Write, Edit, Grep, Glob, Bash\n'
      printf 'model: opus\n'
      printf 'maxTurns: %s\n' "$PIPELINE_MAXTURNS"
      printf -- '---\n\n'
      awk 'NR==1&&$0=="---"{f=1;next} f&&$0=="---"{f=0;next} !f{print}' "$src"
    } > "$AGENTS_DIR/$name.md"
  }
  make_agent entity-tracker "$dir/skills/optional/entity-tracker/SKILL.md" \
    "Builds and maintains ENTITY_STATE.yaml — the persistent structured database of every character, location, object, organization, timeline entry, and world rule in the manuscript. Operates in BUILD mode (initial extraction) and UPDATE mode (incremental tracking)."
  make_agent continuity-guardian "$dir/skills/optional/continuity-guardian/SKILL.md" \
    "Cross-manuscript consistency auditor. Runs after every 3-5 chapter batch and after full completion. Catches continuity errors, information-flow violations, timeline contradictions, and orphaned plot threads."
  make_agent dialogue-polish "$dir/skills/deprecated/dialogue-polish/SKILL.md" \
    "Dedicated dialogue editing pass — ensures distinct character voices, subtext, natural rhythm, and correct dialogue-to-prose ratio. Runs AFTER the writer and BEFORE hook-craft/disruptor."
  make_agent hook-craft "$dir/skills/deprecated/hook-craft/SKILL.md" \
    "Specializes in chapter openings (hooks) and endings (pulls). Every chapter must start with a reason to keep reading and end with a reason to turn the page."
}

if [ "$INSTALL_GLOBAL_AGENTS" = "off" ]; then
  echo "Agent deploy to $AGENTS_DIR skipped (INSTALL_GLOBAL_AGENTS=off); the repo's"
  echo "  .claude/agents/ is still loaded for this project."
elif [ "$AGENT_SOURCE" = "upstream" ]; then
  install_from_upstream || install_from_repo || true
else
  install_from_repo || {
    echo "warn: repo .claude/agents/ has no agents; falling back to upstream fetch." >&2
    install_from_upstream || true
  }
fi

# Normalize maxTurns across ALL installed agents (upstream ships 40, which truncates
# a full chapter write-plus-gate-loop before it can finish).
for f in "$AGENTS_DIR"/*.md; do
  [ -e "$f" ] || continue
  if grep -qiE '^maxTurns:' "$f"; then
    sed -i -E "s/^maxTurns: *[0-9]+/maxTurns: $PIPELINE_MAXTURNS/I" "$f"
  fi
done

# ---------------------------------------------------------------------------
# 5) Verify. Two locations matter for different reasons:
#    - ~/.claude/agents  : what a local session reads.
#    - repo .claude/agents/ : the ONLY thing dispatchable by name in web sessions,
#      because the Agent registry is built from the clone BEFORE this hook runs.
#      This step only REPORTS on the repo copies — it must never overwrite them, or
#      every session would start with a dirty working tree.
# ---------------------------------------------------------------------------
missing=(); for a in "${EXPECTED[@]}"; do [ -f "$AGENTS_DIR/$a.md" ] || missing+=("$a"); done
echo "Book pipeline agents in $AGENTS_DIR (maxTurns normalized to $PIPELINE_MAXTURNS):"
ls "$AGENTS_DIR"
if [ "${#missing[@]}" -eq 0 ]; then
  echo "OK: all ${#EXPECTED[@]} agent files present in $AGENTS_DIR."
else
  echo "ERROR: ${#missing[@]} sub-agent file(s) MISSING from $AGENTS_DIR: ${missing[*]}" >&2
fi

repo_missing=(); for a in "${EXPECTED[@]}"; do [ -f "$REPO_AGENTS/$a.md" ] || repo_missing+=("$a"); done
if [ "${#repo_missing[@]}" -eq 0 ]; then
  echo "OK: all ${#EXPECTED[@]} agents committed in repo .claude/agents/ — dispatchable by name."
else
  echo "WARN: repo .claude/agents/ is missing ${#repo_missing[@]} agent(s): ${repo_missing[*]}" >&2
  echo "      -> commit them to .claude/agents/ so they dispatch by name in web sessions." >&2
fi

# ---------------------------------------------------------------------------
# 6) Cross-model second-opinion tooling (Gemini). Only sets up when a key is available.
# ---------------------------------------------------------------------------
if [ "$REMOTE" = "1" ] && { [ -n "${GEMINI_API_KEY:-}" ] || [ -f "$HOME/.gemini_env" ]; }; then
  if ! command -v gemini >/dev/null 2>&1; then
    echo "Installing Gemini CLI for second-opinion reviews..."
    npm install -g @google/gemini-cli >/dev/null 2>&1 \
      && echo "Gemini CLI installed." \
      || echo "warn: Gemini CLI install failed; /gemini-second-opinion unavailable." >&2
  fi
fi
