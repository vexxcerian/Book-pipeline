#!/usr/bin/env bash
# ============================================================================
# doctor.sh — preflight check for the Books pipeline.
#
#   bash tools/doctor.sh                 # check the environment + every book
#   bash tools/doctor.sh books/your-book # check the environment + one book
#
# Tells you whether this checkout is ready to write a book, and what is missing
# if it isn't. Exits non-zero if anything REQUIRED is missing (optional pieces
# are reported as warnings).
# ============================================================================
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-}"
FAIL=0
WARN=0

ok ()   { printf '  \033[32mok\033[0m    %s\n' "$1"; }
bad ()  { printf '  \033[31mFAIL\033[0m  %s\n' "$1"; FAIL=$((FAIL+1)); }
warn () { printf '  \033[33mwarn\033[0m  %s\n' "$1"; WARN=$((WARN+1)); }

echo "Books pipeline doctor — $ROOT"
echo
echo "Environment"

# --- Python + modules -------------------------------------------------------
if command -v python3 >/dev/null 2>&1; then ok "python3 $(python3 -V 2>&1 | awk '{print $2}')"
else bad "python3 not found"; fi

python3 -c 'import yaml' 2>/dev/null \
  && ok "pyyaml (STATE.yaml parsing, review context)" \
  || bad "pyyaml missing — pip install -r requirements.txt"

python3 -c 'import reportlab' 2>/dev/null \
  && ok "reportlab (print PDF builds)" \
  || warn "reportlab missing — only needed for print builds"

python3 -c 'import PIL' 2>/dev/null \
  && ok "pillow (cover/image handling)" \
  || warn "pillow missing — only needed for cover work"

python3 -c 'import language_tool_python' 2>/dev/null \
  && ok "language-tool-python (grammar tier 2)" \
  || warn "language-tool-python missing — grammar_check.py tier 1 still gates"

command -v gs >/dev/null 2>&1 \
  && ok "ghostscript $(gs --version 2>/dev/null) (no-ICC print conversion)" \
  || warn "ghostscript missing — needed only for IngramSpark print files"

# --- Pipeline files ---------------------------------------------------------
echo
echo "Pipeline"

EXPECTED=(book-orchestrator book-researcher book-architect book-writer \
  book-evaluator book-editor book-disruptor book-packager \
  entity-tracker continuity-guardian dialogue-polish hook-craft)
missing=()
for a in "${EXPECTED[@]}"; do
  [ -f "$ROOT/.claude/agents/$a.md" ] || missing+=("$a")
done
if [ "${#missing[@]}" -eq 0 ]; then
  ok "all 12 agents committed in .claude/agents/ (dispatchable by name)"
else
  bad "missing agent(s) in .claude/agents/: ${missing[*]}"
fi

hm=0
for a in "${EXPECTED[@]}"; do [ -f "$HOME/.claude/agents/$a.md" ] || hm=$((hm+1)); done
if [ "$hm" -eq 0 ]; then ok "all 12 agents installed in ~/.claude/agents/"
else warn "$hm agent(s) not in ~/.claude/agents — run: bash tools/install.sh"; fi

if [ -f "$ROOT/.claude/pipeline.conf" ]; then
  # shellcheck disable=SC1091
  source "$ROOT/.claude/pipeline.conf"
  ok "pipeline.conf (WORKFLOW_LAW=${WORKFLOW_LAW:-unset}, AGENT_SOURCE=${AGENT_SOURCE:-unset})"
else
  warn "no .claude/pipeline.conf — hooks will use built-in defaults"
fi

for h in session-start.sh enforce-main-law.sh; do
  if [ -f "$ROOT/.claude/hooks/$h" ]; then
    bash -n "$ROOT/.claude/hooks/$h" 2>/dev/null && ok "hook $h (syntax ok)" || bad "hook $h has a syntax error"
  else
    warn "hook $h missing"
  fi
done

for t in new-book.sh new-series.sh review_context.py make_noicc.sh collect_completed.py make_epub.py; do
  [ -f "$ROOT/tools/$t" ] && ok "tools/$t" || warn "tools/$t missing"
done

[ -d "$ROOT/books/_template" ] && ok "books/_template/" || bad "books/_template/ missing — new-book.sh cannot scaffold"
[ -d "$ROOT/books/_series-template" ] && ok "books/_series-template/" || warn "books/_series-template/ missing — new-series.sh cannot scaffold"

# --- API keys (optional) ----------------------------------------------------
echo
echo "Cross-model second opinions (optional)"
{ [ -n "${GEMINI_API_KEY:-}" ] || [ -f "$HOME/.gemini_env" ]; } \
  && ok "Gemini key present" || warn "no Gemini key (env or ~/.gemini_env) — /gemini-second-opinion unavailable"
{ [ -n "${XAI_API_KEY:-}" ] || [ -f "$HOME/.grok_env" ]; } \
  && ok "xAI key present" || warn "no xAI key (env or ~/.grok_env) — /grok-second-opinion unavailable"

# --- Books ------------------------------------------------------------------
check_book () {
  local d="$1" name; name="${d#$ROOT/}"
  echo
  echo "Book: $name"

  [ -f "$d/STATE.yaml" ] || { bad "no STATE.yaml — not a book folder"; return; }

  local out
  out="$(python3 - "$d/STATE.yaml" "$name" <<'PY'
import sys, os
try:
    import yaml
except ImportError:
    sys.exit(0)
path, name = sys.argv[1], sys.argv[2]
G = "\033[32mok\033[0m   "; W = "\033[33mwarn\033[0m "; B = "\033[31mFAIL\033[0m "
try:
    st = yaml.safe_load(open(path)) or {}
except Exception as e:
    print(f"  {B} STATE.yaml does not parse: {e}"); sys.exit(1)

proj = st.get("project") or {}
issues = 0

status = str(((st.get("phase") or {}).get("status")) or "")
if "TEMPLATE DEFAULT" in status:
    print(f"  {W} phase.status is still TEMPLATE DEFAULT — stale by definition")
else:
    print(f"  {G} phase.status set")

for key in ("title", "genre", "premise"):
    v = str(proj.get(key) or "")
    if not v or v.startswith("<"):
        print(f"  {W} project.{key} is a placeholder — genre drives every genre-adjusted gate")
        issues += 1
if not issues:
    print(f"  {G} project title/genre/premise filled in")

wf = st.get("word_floor") or {}
if wf.get("manuscript_min_words"):
    print(f"  {G} word floor: {wf['manuscript_min_words']:,} words")
else:
    print(f"  {W} no word_floor.manuscript_min_words")

ser = st.get("series") or {}
if isinstance(ser, dict) and ser.get("name"):
    bible = os.path.join(os.path.dirname(path), ser.get("bible") or "")
    if ser.get("bible") and os.path.isfile(bible):
        print(f"  {G} series: {ser['name']} #{ser.get('position','?')} (bible found)")
    else:
        print(f"  {B} series block names a bible that does not exist: {ser.get('bible')}")
        sys.exit(1)
PY
)"

  local rc=$?
  printf '%s\n' "$out"
  [ "$rc" -ne 0 ] && FAIL=$((FAIL+1))
  WARN=$((WARN + $(printf '%s' "$out" | grep -c 'warn' || true)))

  [ -f "$d/character-bible.md" ] \
    && ok "character-bible.md present" \
    || warn "no character-bible.md — required architect deliverable (docs/CHARACTER-BIBLE.md)"

  for f in tools/style_check.py tools/grammar_check.py tools/voice_wear_check.py; do
    [ -f "$d/$f" ] && ok "$f" || warn "$f missing — copy it from books/_template/"
  done

  local n; n=$(ls "$d"/manuscript/chapters/chapter-*.md 2>/dev/null | wc -l | tr -d ' ')
  if [ "$n" -gt 0 ]; then
    local w; w=$(cat "$d"/manuscript/chapters/chapter-*.md 2>/dev/null | wc -w | tr -d ' ')
    ok "$n chapter(s), $w words"
  else
    ok "no chapters drafted yet"
  fi
}

if [ -n "$TARGET" ]; then
  check_book "$(cd "$TARGET" && pwd)"
else
  while IFS= read -r d; do
    case "$(basename "$d")" in _template|_series-template|_assets) continue ;; esac
    [ -f "$d/STATE.yaml" ] && check_book "$d"
  done < <(find "$ROOT/books" -mindepth 1 -maxdepth 2 -type d | sort)
fi

echo
if [ "$FAIL" -gt 0 ]; then
  echo "$FAIL problem(s), $WARN warning(s)."
  exit 1
fi
echo "All required checks passed ($WARN warning(s))."
