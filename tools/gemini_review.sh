#!/bin/bash
# gemini_review.sh — a cross-model SECOND OPINION on a manuscript chapter, from
# Google's Gemini, tuned for FICTION (not code review).
#
# Sends a chapter's prose to Gemini with a veteran-YA-fantasy-editor prompt and
# returns a craft critique (voice, pacing, emotional truth, YA tone, continuity,
# what is not working). Same cross-model value as the off-the-shelf "Gemini peer
# review" plugins, but pointed at prose instead of git diffs.
#
# Auth: reads GEMINI_API_KEY. Looks for it in the environment, else sources
# ~/.gemini_env (mode 600, kept OUTSIDE the repo so it is never committed).
#
# The editor persona and the book briefing are DERIVED from the book the chapter
# lives in (tools/review_context.py reads the nearest STATE.yaml, or a hand-written
# <book>/review-context.md). Override with REVIEW_CONTEXT="..." for a one-off.
#
# Usage:
#   bash tools/gemini_review.sh <chapter.md> [extra focus notes...]
# Example:
#   bash tools/gemini_review.sh books/your-book/manuscript/chapters/chapter-18.md
set -euo pipefail

CHAPTER="${1:?usage: gemini_review.sh <chapter.md> [focus notes]}"
shift || true
FOCUS="${*:-}"
[ -f "$CHAPTER" ] || { echo "No such file: $CHAPTER" >&2; exit 1; }

# Load the key (env first, then the out-of-repo file).
if [ -z "${GEMINI_API_KEY:-}" ] && [ -f "$HOME/.gemini_env" ]; then
  # shellcheck disable=SC1090
  source "$HOME/.gemini_env"
fi
[ -n "${GEMINI_API_KEY:-}" ] || { echo "GEMINI_API_KEY not set (add it to the environment or ~/.gemini_env)." >&2; exit 1; }
command -v gemini >/dev/null || { echo "gemini CLI not installed (npm i -g @google/gemini-cli)." >&2; exit 1; }
export GEMINI_CLI_TRUST_WORKSPACE=true

PROMPT_FILE=$(mktemp)
trap 'rm -f "$PROMPT_FILE"' EXIT
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# A context-helper failure must never kill the review — fall back to a generic brief.
PERSONA="$(python3 "$SCRIPT_DIR/review_context.py" "$CHAPTER" --what persona 2>/dev/null || true)"
CONTEXT="$(python3 "$SCRIPT_DIR/review_context.py" "$CHAPTER" --what context 2>/dev/null || true)"
[ -n "$PERSONA" ] || PERSONA="You are a veteran acquiring editor of commercial fiction. You are giving a candid, specific SECOND OPINION on a single chapter of a draft novel, independent of the author's own pipeline. Flattery is worthless."
[ -n "$CONTEXT" ] || CONTEXT="(No book metadata found; judge the chapter on its own terms.)"

{
  echo "$PERSONA"
  echo
  echo "Book context:"
  echo "$CONTEXT"
  echo
  echo "Critique THIS CHAPTER on, in order of importance:"
  echo "1. What is genuinely NOT WORKING (the most important section — be blunt, rank the problems)."
  echo "2. Prose & VOICE: sentence rhythm, over-writing/over-narration, any line that rings false or purple."
  echo "3. PACING & tension: where it drags, where it rushes, whether the chapter earns its length."
  echo "4. EMOTIONAL truth: does the feeling land or is it asserted; is restraint maintained or undercut."
  echo "5. REGISTER: does it hold the tone/age-band the book context above describes, or drift out of it."
  echo "6. Anything that reads as AI-generated / formulaic, and any continuity or logic snags you notice."
  echo "End with the 3 highest-leverage fixes, concrete. Do NOT rewrite the chapter. Respond in prose/markdown only; do not attempt to use any tools or read any files."
  [ -n "$FOCUS" ] && { echo; echo "ALSO specifically address: $FOCUS"; }
  echo
  echo "===== CHAPTER TEXT BEGINS ====="
  cat "$CHAPTER"
  echo "===== CHAPTER TEXT ENDS ====="
} > "$PROMPT_FILE"

# Prefer pro (if the project has quota), fall back to flash automatically.
for MODEL in gemini-2.5-pro gemini-2.5-flash; do
  OUT=$(gemini -m "$MODEL" --skip-trust "$(cat "$PROMPT_FILE")" 2>/tmp/gemini_err.$$ || true)
  if echo "$OUT" | grep -qiE "exhausted your daily quota|quota exceeded|RESOURCE_EXHAUSTED|429"; then
    continue
  fi
  if [ -n "$OUT" ]; then
    echo "## Gemini second opinion ($MODEL) — $(basename "$CHAPTER")"
    echo
    echo "$OUT" | grep -viE "256-color support|^Warning: "
    rm -f /tmp/gemini_err.$$
    exit 0
  fi
done
echo "Gemini returned no usable output (all models quota-blocked?). Last stderr:" >&2
cat /tmp/gemini_err.$$ >&2 2>/dev/null || true
rm -f /tmp/gemini_err.$$
exit 1
