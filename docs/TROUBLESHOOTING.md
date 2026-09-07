# Troubleshooting

The failures you will actually hit, and what they mean.

**Start here:** `bash tools/doctor.sh` checks the environment, the pipeline files and every
book folder, and names what's missing. `bash tools/doctor.sh books/<slug>` checks one book.

## Agents

**"Cannot resolve subagent_type" / the agent isn't found.**
In web sessions only agents **committed** to `.claude/agents/` are dispatchable by name —
the registry is built from the clone before hooks run. Commit the agent file; it becomes
available next session. In the meantime, run a general-purpose agent and tell it to read
`.claude/agents/<name>.md` and follow it.

**I edited an agent and nothing changed.**
Same cause. Agent edits take effect in the **next** session. This is also why the pipeline
lives in the repo rather than only in `~/.claude/agents`.

**An agent stops mid-chapter, leaving half a revision.**
`maxTurns` too low. Upstream agents ship with 40; a full chapter write-plus-gate-loop needs
more. `PIPELINE_MAXTURNS` in `.claude/pipeline.conf` defaults to 120 and the SessionStart
hook normalizes every installed agent to it.

**Sub-agents feel dumber than the main session.**
They defaulted to a smaller model. The hook sets `ANTHROPIC_MODEL` from `PIPELINE_MODEL`;
if you're running locally without the hook, set it yourself.

**The orchestrator asks what to do next instead of just doing it.**
It is specified to be autonomous between the three checkpoints. If it's deliberating, it's
usually missing an input it needs — most often a `STATE.yaml` that's still full of template
placeholders. Fill in genre, premise and word floor, then re-dispatch.

## State and continuity

**The architect built the wrong book.**
Check `STATE.yaml` first. A file still reading `TEMPLATE DEFAULT`, or with the wrong genre,
sends every downstream agent off confidently in the wrong direction — genre drives
genre-adjusted thresholds in the evaluator, the anti-pattern budget, hook floors and the
CVI weighting.

**A character knows something they shouldn't.**
An information-flow violation. `ENTITY_STATE.yaml` records `learned_chapter` + source on
each piece of knowledge; run `entity-tracker` UPDATE then `continuity-guardian`. If the
entity state is stale (it's updated every 3–5 chapters, not every chapter), that gap is
usually where the error hid.

**Continuity contradictions after a revision pass.**
Revisions mutate finalized chapters, so run `entity-tracker` UPDATE after Phase 5 — that's
what Phase 5.5 is for. Skipping it leaves the canon describing a version of the book that
no longer exists.

**The guardian flagged something that's deliberate.**
It distinguishes ERROR from INTENT, but not perfectly — an unreliable narrator and a
planted re-read reward both look like contradictions. Record the intent in `STATE.yaml`
`guardrails` so it stops recurring as a finding.

## Quality gates

**A chapter won't reach 8.5 after several cycles.**
Expected in part: the anti-inflation rule caps improvement at +0.5 per cycle, so 7.5 → 8.5
is a minimum of two cycles. If it's stuck after five, the evaluation is telling you the
problem isn't at chapter level — a chapter can't fix a premise or an outline. Escalate it,
keep going, and re-attack in Phase 5.

**Scores jumped from 7.0 to 9.0 in one pass.**
That's inflation, and it violates the +0.5 rule. Challenge it: ask for the cited passage
evidence per dimension and re-evaluate.

**style_check.py fails on a phrase I use on purpose.**
Add it to the ALLOWLIST in that book's `tools/style_check.py` — but note the **motif cap**:
allowlisting exempts a phrase from the generic repeat check while still holding it to 3
uses per book. If you genuinely need more for one load-bearing image, use
`("phrase", N)` — sparingly. If several motifs need raising, the prose has a tic problem,
not a configuration problem.

**Every chapter trips the same tic words.**
That's voice wear. Run `python3 books/<slug>/tools/voice_wear_check.py` (shipped with every
new book) and check the retired/at-risk list in `character-bible.md`. See the Amelia Lesson
in [CHARACTER-BIBLE.md](CHARACTER-BIBLE.md).

**grammar_check.py --languagetool is slow or fails.**
Tier 2 needs Java and a ~250MB engine that downloads on first use. Tier 1 gates without it
and is dependency-free — tier 2 is an assist, never an authority, since it false-positives
on fiction dialogue.

## Second opinions

**Gemini: quota exhausted.**
The script tries `gemini-2.5-pro` then falls back to `gemini-2.5-flash`. If both are
blocked it exits with the stderr — wait, or use Grok.

**Grok: `permission-denied`.**
An xAI key with no team credits. The tool is correct; the account is unfunded. Buy credits
at console.x.ai.

**A key isn't found.**
`GEMINI_API_KEY` / `XAI_API_KEY` from the environment, or `~/.gemini_env` / `~/.grok_env`
(mode 600, outside the repo). Never commit them — `.gitignore` covers the usual filenames,
but the safe location is outside the repo entirely.

**The review reads as though it's for a different book.**
Check what `tools/review_context.py` derives: `python3 tools/review_context.py <chapter>`.
It reads the nearest `STATE.yaml`, so a placeholder-filled one produces a vague briefing.
Write `books/<slug>/review-context.md` for a hand-tuned one.

## Git and the environment

**"Creating a branch is forbidden" when I wanted a branch.**
The workflow law is on. Set `WORKFLOW_LAW="off"` in `.claude/pipeline.conf` — see
[WORKFLOW-AND-HOOKS.md](WORKFLOW-AND-HOOKS.md). Note the guard also fires when a *command
string* merely contains a blocked pattern, which occasionally catches an innocent echo.

**My session started on a branch and the branch disappeared.**
That's the SessionStart hook enforcing the law. Uncommitted work is carried across via
stash, so the working tree survives; the branch pointer doesn't.

**Branch deletion returns 403 from the web environment.**
The git proxy blocks it. Delete branches via the GitHub website (repo → Branches → trash
icon) or a local terminal.

**`git clone` of another repo fails with 403.**
The web environment's git proxy limits clones to the session's repos. Fetch a tarball over
HTTPS instead (that's why the upstream agent fetch uses `curl`, not `git clone`).

**"No space left on device" with low disk usage reported.**
The writable allowance is per-session, so `df` misleads. Delete build artifacts, caches and
stale clones — deletes still succeed while writes fail.

**Ghostscript missing / `build_pdf.py` won't run.**
The SessionStart hook installs `reportlab`, `pillow` and Ghostscript, but only in the
remote environment. Locally run `bash tools/install.sh`, then install Ghostscript itself
(`apt-get install ghostscript` / `brew install ghostscript`) — it isn't pip-installable.
`bash tools/doctor.sh` tells you which of these are missing.

## Publishing

**IngramSpark rejected the upload for image resolution.**
Probably *too high*, not too low — their preflight objects to both. `make_noicc.sh`
downsamples to 300 ppi. See [PUBLISHING.md](PUBLISHING.md).

**"PDF CONTAINS ICC COLOR PROFILES."**
Non-blocking warning. Files built with `make_noicc.sh` are profile-free; if it still
appears, proceed and order a printed proof to confirm the interior prints solid black.

**Em dashes and curly quotes won't copy out of the print PDF.**
Known and accepted: the Ghostscript pass drops the ToUnicode mapping. Printing is
unaffected. Use the RGB build from `delivery/` if you need extractable text.

**The eBook format blocks submission while I'm on the print tab.**
"Preview my book" validates all formats. Fill in the eBook format (EPUB — a PDF is
rejected there) before previewing.

**`make_epub.py` says "missing required config".**
The book has no `delivery/ebook.yaml`, or it lacks a required key (title, author, ebook
ISBN, cover). Start from `books/_template/delivery/ebook.yaml`; new books get a copy
automatically. Paths in it are relative to the book folder.

**The EPUB built but has 0 chapters.**
The assembled manuscript isn't using `CHAPTER ONE` headings — that's the format
`assemble_manuscript.py` produces and what the parser looks for.

**`collect_completed.py --check` exits 1.**
`completed-books/` is stale against the current builds. Re-run without `--check`. Never
hand-edit that folder — it's generated precisely so staleness is detectable.
