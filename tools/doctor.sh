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

for h in session-start.sh enforce-main-law.sh enforce-book-folder-law.sh; do
  if [ -f "$ROOT/.claude/hooks/$h" ]; then
    bash -n "$ROOT/.claude/hooks/$h" 2>/dev/null && ok "hook $h (syntax ok)" || bad "hook $h has a syntax error"
  else
    warn "hook $h missing"
  fi
done

for t in new-book.sh new-series.sh review_context.py make_noicc.sh collect_completed.py make_epub.py; do
  [ -f "$ROOT/tools/$t" ] && ok "tools/$t" || warn "tools/$t missing"
done

# Every Python tool must at least compile, or it fails at the worst moment.
badpy=""
for f in "$ROOT"/tools/*.py "$ROOT"/books/_template/tools/*.py "$ROOT"/.claude/hooks/*.py; do
  [ -e "$f" ] || continue
  python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" "$f" 2>/dev/null \
    || badpy="$badpy $(basename "$f")"
done
[ -z "$badpy" ] && ok "all Python tools parse" || bad "Python syntax errors in:$badpy"

# settings.json is what registers the hooks and the apodictic plugin.
if [ -f "$ROOT/.claude/settings.json" ]; then
  python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$ROOT/.claude/settings.json" 2>/dev/null \
    && ok ".claude/settings.json parses (hooks + plugin registered)" \
    || bad ".claude/settings.json is not valid JSON — hooks will not run"
else
  bad ".claude/settings.json missing — hooks will not run"
fi

# The agents must be well-formed, and every name the orchestrator dispatches must exist.
python3 - "$ROOT" <<'PY'
import os, re, sys, glob
root = sys.argv[1]
G = "  \033[32mok\033[0m    "; B = "  \033[31mFAIL\033[0m  "
names, problems = set(), []
for f in sorted(glob.glob(os.path.join(root, ".claude/agents/*.md"))):
    base = os.path.basename(f)[:-3]
    txt = open(f).read()
    if not txt.startswith("---"):
        problems.append(f"{base}: no frontmatter"); continue
    fm = txt.split("---", 2)[1]
    kv = dict(re.findall(r"^([A-Za-z_]+):\s*(.*)$", fm, re.M))
    names.add(kv.get("name", ""))
    if not kv.get("description"): problems.append(f"{base}: no description (it will not be selectable)")
    if kv.get("name") != base:    problems.append(f"{base}: name is '{kv.get('name')}' but must match the filename")
orch = os.path.join(root, ".claude/agents/book-orchestrator.md")
if os.path.isfile(orch):
    for d in sorted(set(re.findall(r"Dispatch:\s*`?([a-z][a-z-]+)`?", open(orch).read()))):
        if d == "agent-name":      # the doc's own placeholder in the how-to-dispatch example
            continue
        if d not in names:
            problems.append(f"orchestrator dispatches '{d}' but no such agent exists")
if problems:
    for p in problems: print(B + p)
    sys.exit(1)
print(G + f"{len(names)} agents well-formed; every orchestrator dispatch resolves")
PY
[ $? -ne 0 ] && FAIL=$((FAIL+1))

[ -d "$ROOT/books/_template" ] && ok "books/_template/" || bad "books/_template/ missing — new-book.sh cannot scaffold"
[ -d "$ROOT/books/_series-template" ] && ok "books/_series-template/" || warn "books/_series-template/ missing — new-series.sh cannot scaffold"

# --- Book folder law --------------------------------------------------------
# One book, one folder. Every book artifact must live inside books/<slug>/ (or
# books/<series>/<book>/). Anything loose is a book that was started the wrong way.
echo
echo "Book folder law"

if [ -f "$ROOT/.claude/hooks/book_folder_law.py" ] && [ -f "$ROOT/.claude/hooks/enforce-book-folder-law.sh" ]; then
  ok "guard present (enforce-book-folder-law.sh + book_folder_law.py)"
else
  bad "book folder law guard missing — new books can be scaffolded anywhere"
fi

if grep -q 'enforce-book-folder-law\.sh' "$ROOT/.claude/settings.json" 2>/dev/null; then
  ok "guard registered as a PreToolUse hook in settings.json"
else
  bad "guard not registered in .claude/settings.json — it will never run"
fi

case "${BOOK_FOLDER_LAW:-enforced}" in
  enforced) ok "BOOK_FOLDER_LAW=enforced" ;;
  off)      warn "BOOK_FOLDER_LAW=off — the law is documented but not enforced" ;;
  *)        warn "BOOK_FOLDER_LAW='${BOOK_FOLDER_LAW}' is not a known value (enforced|off)" ;;
esac

strays=""
while IFS= read -r f; do
  rel="${f#"$ROOT"/}"
  case "$rel" in
    .git/*|.claude/*|docs/*|tools/*|books/_template/*|books/_series-template/*|books/_assets/*) continue ;;
    books/*/*) continue ;;   # books/<slug>/… — exactly where a book belongs
  esac
  strays="$strays $rel"
done < <(find "$ROOT" -name .git -prune -o -type f \( \
    -name STATE.yaml -o -name ENTITY_STATE.yaml -o -name foundation.md -o \
    -name outline.md -o -name voice-dna.md -o -name character-bible.md -o \
    -name premise.md -o -name 'chapter-*.md' \) -print 2>/dev/null)

if [ -z "$strays" ]; then
  ok "no book artifacts outside a book folder"
else
  bad "book artifact(s) outside books/<slug>/ —$strays"
  printf '        move each into its own book folder: bash tools/new-book.sh <slug> "<Title>"\n'
fi

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

  # Scaffolded by new-book.sh? These come free from the template; missing them means
  # the folder was hand-made, and a gate that cannot run is a gate that never fails.
  for f in tools/style_check.py tools/grammar_check.py tools/voice_wear_check.py delivery/ebook.yaml; do
    [ -f "$d/$f" ] && ok "$f" || warn "$f missing — folder not scaffolded from books/_template/ (see the BOOK FOLDER LAW)"
  done

  # The gates must RUN, not merely parse. A per-book gate is edited by hand (ALLOWLIST,
  # ceilings), and a config name that is referenced but never defined is a NameError that
  # only fires on the chapter it applies to — long after the edit, and silently until then.
  # Exit 1 here means "the gate flagged something", which is the gate working; a traceback
  # means the gate itself is broken, which is the gate not existing.
  for g in style_check grammar_check voice_wear_check; do
    [ -f "$d/tools/$g.py" ] || continue
    local out; out="$(cd "$d" && python3 "tools/$g.py" 2>&1)"
    if printf '%s' "$out" | grep -q 'Traceback (most recent call last)'; then
      bad "tools/$g.py CRASHES — $(printf '%s' "$out" | tail -1)"
    fi
  done

  local n; n=$(ls "$d"/manuscript/chapters/chapter-*.md 2>/dev/null | wc -l | tr -d ' ')
  if [ "$n" -gt 0 ]; then
    # Strip <!-- editorial comments --> before counting. Scene budgets and revision
    # notes live in the chapter files and are NOT prose; counting them inflates the
    # manuscript against its own word floor, by ~40 words per chapter and rising.
    local w; w=$(cat "$d"/manuscript/chapters/chapter-*.md 2>/dev/null \
        | perl -0777 -pe 's/<!--.*?-->//gs' | wc -w | tr -d ' ')
    ok "$n chapter(s), $w words of prose"
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
