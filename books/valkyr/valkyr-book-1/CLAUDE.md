# CLAUDE.md — Valkyr: Book One

Per-book playbook. A fresh Claude Code session should read this first, then `STATE.yaml`,
then `feedback/progress.md`.

## What this is

Book One of the **Valkyr** series — military SF / black-ops conspiracy, set in the Halo
universe at the UNSC-ONI black-ops tier.

**Run mode: revise / expand an existing draft.** The author's own prose for Chapters 1–5
(~14,600 words) is staged at `research/original-draft.md`. The chapter loop REVISES and
CONTINUES it against the roadmap; it does not invent from scratch. **Chapter 1 is LOCKED** —
it is the hand-finished voice benchmark. Match it; never rewrite it.

**Premise.** A retired Spartan is handed back the only piece of his dead twin that survived —
his mind, running as an AI — and rebuilds the black program that killed him, under the command
of the man who pulled the trigger.

**Series canon lives one level up:** `../SERIES-BIBLE.md`. It **outranks this file and
`STATE.yaml`** on anything shared. Everything marked `(locked)` there is a settled author
decision: execute it, never re-litigate it.

Repo workflow: see the root `CLAUDE.md` — including the **BOOK FOLDER LAW** (every book in its
own folder, scaffolded by `tools/new-book.sh`, enforced by a hook).

## The pipeline (shared — nothing to install)

The 12 `book-*` agents, `/gemini-second-opinion` + `/grok-second-opinion`, and APODICTIC live
in the **repo root** `.claude/` + `tools/` and load automatically each session. This book uses
them directly — nothing to clone or copy in. Improvements go to the **root**, per the repo
UPDATE RULE; the only per-book pipeline file is this book's `tools/style_check.py` ALLOWLIST.

Full reference: `docs/PIPELINE.md`. Character bible: `docs/CHARACTER-BIBLE.md`.
Series workflow: `docs/SERIES.md`.

## Project layout (`books/valkyr/valkyr-book-1/`)

```
books/valkyr/
├── SERIES-BIBLE.md            # LOCKED shared canon — read before anything else
└── valkyr-book-1/
    ├── STATE.yaml             # READ FIRST — state, word/style gates, canon, open decisions
    ├── foundation.md          # characters, theme-as-question, anchors, opening strategy
    ├── outline.md             # macro-structure + per-chapter plan
    ├── voice-dna.md           # global voice, differentiation matrix, anti-pattern budget
    ├── character-bible.md     # cast VOICE/distinctness — ADD every new named character (tic budget)
    ├── ENTITY_STATE.yaml      # entity-tracker's structured canon (facts, timeline, who-knows-what)
    ├── research/              # original-draft.md (Ch.1–5), author-act-outline.md, valkyr-source.pdf
    ├── manuscript/chapters/   # chapter-1.md … chapter-N.md (the book)
    ├── evaluations/           # per-chapter eval reports + continuity/ audits
    ├── feedback/progress.md   # exact resume point
    ├── delivery/              # editorial package + production files
    └── tools/style_check.py   # style gate (edit ALLOWLIST for this book's motifs)
```

## How to continue

1. Read `STATE.yaml` and `feedback/progress.md`, then `../SERIES-BIBLE.md`.
2. `ls manuscript/chapters/` and `git log --oneline` to find the last finalized chapter.
3. Produce the next chapter IN ORDER. Locate its material in `research/original-draft.md`
   (Ch.1–5) or `outline.md` (Ch.6+), REVISE/EXPAND to the roadmap beats, and match the locked
   Ch.1 voice. Run each chapter through: write → dialogue-polish → hook-craft → disruptor →
   evaluate → quality gate.
4. Commit per chapter: `git add -A && git commit -m "genesis: finalize chapter N"`.

## Quality gates (all must pass before a chapter is "done")

- **Genesis Floor ≥ 8.5** (book-evaluator); below → book-editor polish loop (max 5).
- **Style check** — `python3 tools/style_check.py` clean: simile ≤4/1k, em-dash ≤~10/1k,
  no NEW cross-chapter repeated phrase (add deliberate motifs to ALLOWLIST), tics under ceiling.
- **Grammar check** — `python3 tools/grammar_check.py` clean (tier 1 gates).
- **Motif cap** — no signature narrative tic-phrase may recur more than **3 times across the
  whole book**. The ALLOWLIST is a *capped* registry, not an exemption.
- **Tic budget** — `character-bible.md` §TIC BUDGET holds: ≤2–3 tic-bearing characters in the
  whole book, no two sharing a device.

⚠️ **Watch the em-dash gate on the drafted chapters.** The author's own prose leans hard on
the em-dash. That is the voice and it is not a defect — but the mechanical gate will flag it,
so when Ch.1–5 are promoted into `manuscript/`, expect the style check to fire and treat it as
a calibration question for the ALLOWLIST/threshold rather than as licence to sand the voice
flat. Ch.1 is locked either way.

## Word floor

Finished book ≥ 85,000 words (`manuscript_min_words`); the outline budgets to 90,000. Verify:
`wc -w manuscript/chapters/chapter-*.md`. The five drafted chapters contribute ~14,600 of
those. No per-chapter floor — lengths vary widely by design, and the draft's own chapters
already run 1,914–4,000 words.

## Canon guardrails (settled — never violate)

- **POV is Vexx, close third, for the whole book. No Jameson POV, no Rx POV.** The reader only
  ever knows Rx through a processed voice and what Vexx infers from it.
- **Book One ends on SUSPICION, not revelation** — Vexx choosing to keep investigating in
  secret rather than act. The full memory unlock (stage 4) and the Jameson confrontation belong
  to Book Two and may not be reached here.
- **The memory-unlock ladder is four stages, series-level. Stages 1 and 2 are already spent**
  in the drafted Ch.3 (the treeline flash) and Ch.4 ("the shape of a refusal"). Book One's one
  remaining unlock beat is **stage 3** — proximity-triggered by Jameson present in person.
  Do not invent intermediate stages; do not reach stage 4.
- **Jameson is institutional, never cartoonish.** Warm, credible, genuinely persuasive. A scene
  where the reader can see he is the villain is a failed scene — his danger is that the reader
  likes him.
- **No rampancy clock**, in any form, as a source of tension. Rx's instability is memory
  suppression, trauma and moral weight only.
- **No hard in-universe calendar date** on the page. Era: early-to-mid Human-Covenant War, four
  years after Rx's death.
- **Spelling and naming:** obey the registry in `../SERIES-BIBLE.md` exactly (Vexxcerian/Vexx,
  Rx, Jameson, Spector, Aglaope, the Choosing, SPARTAN-II…).

## Open author decisions (ask, don't invent)

Full list in `STATE.yaml` under `open_author_decisions`. The ones that bite soonest:

- **Rights posture** — Halo fan fiction, or an original property to be filed off later? This
  decides the entire delivery path. It does **not** block drafting, but do not start any
  packaging or publishing work until it is answered.
- **The real title.** "Valkyr: Book One" is a placeholder.
- **How much do the drafted Ch.2–5 get touched?** Ch.1 is locked. Recommended: evaluate-only,
  and polish just what a gate flags.
- Whether the shared AI donor-stock twist is planted late in Book One or held for Book Two.
  It is designed to be cuttable — one line.

## Status (update as you go)

- **2026-09-07** — Folder scaffolded via `tools/new-book.sh`. Author's PDF staged into
  `research/`; series canon transcribed to `../SERIES-BIBLE.md`; `STATE.yaml` filled.
  Architect pass run — see `outline.md`, `foundation.md`, `voice-dna.md`, `character-bible.md`
  and `feedback/progress.md` for the current resume point.
- **Nothing has passed the pipeline's gates yet.** `manuscript/chapters/` is still empty; the
  author's five chapters live in `research/original-draft.md` and have not been promoted.
