# CLAUDE.md — <BOOK TITLE>

Per-book playbook. A fresh Claude Code session should read this first, then continue.
(This is a copy of the template — fill in the `<…>` placeholders for this book, and delete
whatever does not apply.)

## What this is
A book project in this monorepo, built with the shared book pipeline. Pick the run mode
and delete the other line:

- **Genesis from idea** — no existing draft; the architect builds foundation + outline +
  voice-dna + character-bible from the premise/source notes, then the chapter loop writes.
- **Revise / expand an existing draft** — source prose is staged in `research/`; the chapter
  loop REVISES it to the roadmap beats instead of inventing from scratch.

Repo workflow: see the root `CLAUDE.md`. By default this repo works only on `main` and
commits straight to it — a fork can change that (`docs/WORKFLOW-AND-HOOKS.md`).

Git identity (so commits are attributed consistently):
```
git config user.email noreply@anthropic.com
git config user.name Claude
```

## The pipeline (shared — nothing to install)
The 12 `book-*` agents, `/gemini-second-opinion` + `/grok-second-opinion`, and APODICTIC live
in the **repo root** `.claude/` + `tools/` and load automatically each session. This book uses
them directly — nothing to clone or copy in. Improvements go to the **root**, per the repo
UPDATE RULE; the only per-book pipeline file is this book's `tools/style_check.py` ALLOWLIST.

Full reference: `docs/PIPELINE.md`. Character bible: `docs/CHARACTER-BIBLE.md`.

## Project layout (`books/<slug>/`)
```
books/<slug>/
├── STATE.yaml                 # READ FIRST — state, word/style gates, canon, open decisions
├── premise.md                 # forged premise (genesis runs)
├── foundation.md              # characters, theme-as-question, anchors, opening strategy
├── outline.md                 # macro-structure + per-chapter plan
├── voice-dna.md               # global voice, differentiation matrix, anti-pattern budget
├── character-bible.md         # cast VOICE/distinctness — ADD every new named character (tic budget)
├── ENTITY_STATE.yaml          # entity-tracker's structured canon (facts, timeline, who-knows-what)
├── research/                  # staged source: original draft, story/series bible, roadmap
├── manuscript/chapters/       # chapter-1.md ... chapter-N.md (the book)
├── evaluations/               # per-chapter eval reports + continuity/ audits
├── feedback/progress.md       # exact resume point
├── delivery/                  # editorial package + production files
└── tools/style_check.py       # style gate (edit ALLOWLIST for this book's motifs)
```
If this book is part of a series, it sits under `books/<series-slug>/<book-slug>/` and also
answers to the series bible — see `docs/SERIES.md`.

## How to continue
1. `cd books/<slug>` and read `STATE.yaml` and `feedback/progress.md`.
2. `ls manuscript/chapters/` and `git log --oneline` to find the last finalized chapter.
3. Produce the next chapter IN ORDER. On a revise run, locate its material in `research/`
   and REVISE/EXPAND to the roadmap beats — do not invent from scratch. Match the locked
   Ch.1 voice if one exists. Run each chapter through: write → dialogue-polish → hook-craft
   → disruptor → evaluate → quality gate.
4. Commit per chapter: `git add -A && git commit -m "genesis: finalize chapter N"`.

## Quality gates (all must pass before a chapter is "done")
- **Genesis Floor ≥ 8.5** (book-evaluator); below → book-editor polish loop (max 5).
- **Style check** — `python3 tools/style_check.py` clean: simile ≤4/1k, em-dash ≤~10/1k,
  no NEW cross-chapter repeated phrase (add deliberate motifs to ALLOWLIST), tics under ceiling.
- **Grammar check** — `python3 tools/grammar_check.py` clean (tier 1 gates: doubled words,
  space-before-punctuation, a/an mismatch).
- **Motif cap (author standing rule)** — no signature narrative tic-phrase may recur more than
  **3 times across the whole book**. ALLOWLIST is a *capped* registry, not an exemption:
  declaring a motif does NOT license unlimited use. Entries are `"phrase"` (cap 3) or
  `("phrase", N)` to raise the cap for a genuinely load-bearing image (keep overrides rare/small).
  The gate FAILS if any motif exceeds its cap.
- **Tic budget** — `character-bible.md` §TIC BUDGET holds: ≤2–3 tic-bearing characters in the
  whole book, no two characters sharing a device.

## Word floor
Finished book ≥ `manuscript_min_words` (see STATE.yaml). Verify:
`wc -w manuscript/chapters/chapter-*.md`. If short, expand the thinnest chapters.
There is deliberately NO per-chapter floor — chapter lengths vary widely by design.

## Canon guardrails (settled author decisions — never violate)
- <fill in this book's settled spellings, names, world rules, locked chapters, etc.>

## Open author decisions (ask, don't invent)
- <fill in>

## Status (update as you go)
- ⚠️ TEMPLATE DEFAULT — freshly scaffolded, no source staged yet. **Update this AND
  `STATE.yaml`'s `phase.status` the moment source lands or the architect runs.** A status
  line that still says "TEMPLATE DEFAULT" is stale by definition — verify against the actual
  files (`research/`, `foundation.md`/`outline.md`, `feedback/progress.md`) rather than
  trusting it.
