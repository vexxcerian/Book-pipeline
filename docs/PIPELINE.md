# The pipeline

The reference: every agent, every phase, every file, and why the design is shaped this
way. Read [GETTING-STARTED.md](GETTING-STARTED.md) first if you just want to run it.

## The shape of it

The pipeline is **12 sub-agents**, each with one job, coordinated either by you or by the
`book-orchestrator`. They communicate through **files on disk**, never through a shared
conversation. That is the load-bearing design decision: a book is far longer than any
context window, so the manuscript's state lives in `STATE.yaml`, `ENTITY_STATE.yaml`,
`character-bible.md` and `feedback/progress.md`, and any session — days later, on any
model — can resume from them.

The agents live in `.claude/agents/`. Improve them **there**, at the repo root, and every
book inherits the improvement. That is the repo's UPDATE RULE.

## The 12 agents

| Agent | Job | Reads | Writes |
|---|---|---|---|
| `book-researcher` | Market research, comp titles, gaps, reader personas | STATE.yaml | `research/market-research.md`, `research/bestseller-dna.md`, `reader-personas.md` |
| `book-architect` | Premise forge, foundation, outline, voice DNA, character bible | research, STATE.yaml | `premise.md`, `foundation.md`, `outline.md`, `voice-dna.md`, `character-bible.md`, `voice-bank/` |
| `entity-tracker` | The structured canon: who/what/where/when, who knows what | outline, chapters | `ENTITY_STATE.yaml`, `evaluations/entity-changelog.md` |
| `continuity-guardian` | Audits continuity; **flags, never fixes** | everything | `evaluations/continuity/*.md` |
| `book-writer` | Writes one chapter | outline, voice-dna, character-bible, entity state, previous chapter | `manuscript/chapters/chapter-N.md` + report |
| `dialogue-polish` | Dialogue-only surgery; cover-the-name test | chapter, voice cards | edits chapter in place |
| `hook-craft` | The first and last 3–5 sentences | chapter, outline | edits chapter in place |
| `book-disruptor` | Anti-AI disruption; simile surgery | chapter, anti-pattern budget | edits chapter in place |
| `book-evaluator` | Genesis Score, CVI, reader simulation, 20-pattern scan | chapter + all specs | `evaluations/eval-chapter-N.md` |
| `book-editor` | Targeted revision against named findings | evaluation findings | edits chapter in place |
| `book-packager` | Editorial package + production prep | manuscript, foundation | `delivery/` |
| `book-orchestrator` | Runs all of the above; never writes prose | everything | `STATE.yaml` |

## The phases

```
PHASE 1     RESEARCH + READER PERSONAS      book-researcher
PHASE 1.5   PREMISE FORGE                   book-architect (forge mode)
PHASE 2     FOUNDATION + OUTLINE            book-architect
PHASE 2.5   VOICE DNA + CHARACTER BIBLE     book-architect (voice mode)
   >>> CHECKPOINT 1 — you approve the foundation <<<
PHASE 2.7   ENTITY BUILD                    entity-tracker (BUILD)
PHASE 2.8   CONTINUITY (outline)            continuity-guardian (OUTLINE AUDIT)
PHASE 3     THE CHAPTER LOOP                steps A–G, sequential, per chapter
PHASE 4     FULL-MANUSCRIPT EVALUATION      book-evaluator
PHASE 5     REVISION                        book-editor
PHASE 5.5   ENTITY UPDATE                   entity-tracker (UPDATE)
PHASE 5.6   CONTINUITY (full manuscript)    continuity-guardian (MANUSCRIPT AUDIT)
   >>> CHECKPOINT 2 — you approve the manuscript <<<
PHASE 6     DELIVERY                        book-packager
   >>> CHECKPOINT 3 — editorial package ready <<<
```

### Phase 1.5 — the premise forge, and why it exists

The raw idea is a **seed, not a contract**. The forge generates five variants, each built
on a different irony engine, scores all of them on six dimensions (hook, irony engine,
native escalation, the central question, market-gap fit, retellability), and the winner
needs a **floor** of 8.0.

Skipping this caps Originality at whatever the seed was worth, and no amount of downstream
polish recovers it — a chapter gate cannot fix a premise. The rule that keeps it honest is
**elevate, don't replace**: your idea must stay recognizable inside the winning premise.
Variant 1 is always your raw idea, scored honestly, so you can see what the forge actually
bought you.

### Phase 2 — macro-structure selection (the anti-uniformity rule)

Before outlining, the architect **chooses** a macro-structure for this specific premise
from a menu: three-act (with jittered turning points), four-act / kishōtenketsu, five-act,
two-part diptych, in-media-res + unspooling, mosaic/braided, slow-burn + short explosive
finale, circular/frame.

This exists because **structural uniformity is the loudest machine-made tell**: every book
landing at ~20 chapters of ~5,000 words in three visible acts with turning points on the
exact quarter-marks. Three specific rules enforce the escape:

- **Jitter the turning points.** Never 25/50/75. Uneven act lengths on purpose.
- **Never compute `word_target ÷ per_chapter_floor`.** That division *is* the mechanism
  behind the 20-chapter monoculture. Chapter count falls out of the beats; lengths vary
  widely (~1,500–7,000 words), including at least one very short punch chapter.
- **Budget to the book total.** Sum the varied chapter targets; the sum must clear
  `manuscript_target_words` with a 5–10% margin. Variance redistributes words — it never
  excuses a short book.

Hence there is deliberately **no per-chapter word floor** anywhere in this pipeline. Only
the book total is gated.

### Phase 3 — the chapter loop

Per chapter, in order:

**A. Write** (`book-writer`) → **B. Dialogue polish** → **C. Hook craft** → **D. Disruption**
→ **D.5 Entity update** (every 3–5 chapters) → **E. Mechanical preprocess** (bash: em-dash
counts, Pattern #11 greps, adverb density, repeated sentence openers) → **F. Evaluate** →
**G. Quality gate**.

**The loop is strictly sequential, and this is not an optimization you should undo.**
Chapter N+1's writer reads the *finalized* chapter N. But N keeps being mutated by steps
B, C, D and possibly G after it is first written. Start N+1 early and it builds on a
version of N that no longer exists — that is the race that quietly corrupts continuity
thirty chapters later.

**The gate (step G):**
- **Hard floor** (genre-adjusted): literary 7.5, commercial 7.0, thriller 7.0, memoir 7.5,
  prescriptive NF 7.0. Below this the chapter is broken and never ships.
- **Pass** = Genesis **Floor ≥ 8.5 AND Casual Reader ≥ 8.5**. Nothing else is a pass.
- Between the two: the polish loop. `book-editor` targets only the 1–2 dimensions holding
  the floor down, quoting the evaluator's "PATH TO 8.5" and the "Strengths to PRESERVE"
  list, then re-evaluate. Max 5 cycles, then escalate and re-attack in Phase 5.

## The files, and what each is for

```
books/<slug>/
├── STATE.yaml            # the resume point. Genre, gates, canon, scores, phase, decisions.
├── premise.md            # the forge's variants + the winner, with scores
├── foundation.md         # characters (with chaos), theme-as-question, anchors, opening strategy
├── outline.md            # macro-structure block + per-chapter beats
├── voice-dna.md          # global voice, differentiation matrix, anti-pattern budget
├── character-bible.md    # per-character voice cards + the TIC BUDGET  → CHARACTER-BIBLE.md
├── ENTITY_STATE.yaml     # structured canon: facts, timeline, who-knows-what-when
├── reader-personas.md    # primary (drives writing), hostile (drives evaluation), stretch
├── voice-bank/           # benchmark prose samples this book is aiming at
├── research/             # market research, bestseller DNA, staged source material
├── manuscript/chapters/  # chapter-N.md — the book
├── evaluations/          # per-chapter evals, disruption/dialogue/hook reports, continuity/
├── feedback/progress.md  # the human-readable resume point
├── delivery/             # editorial package + production files
└── tools/                # this book's style_check.py + grammar_check.py (ALLOWLIST is per-book)
```

**`STATE.yaml` and `ENTITY_STATE.yaml` do different jobs and are not interchangeable.**
STATE is the *project*: phase, gates, scores, settled decisions. ENTITY_STATE is the
*story world*: every character, location, object, timeline entry and world rule, plus
`learned_chapter` on each piece of knowledge so information-flow violations (a character
knowing something before they were told) are detectable. `character-bible.md` is the third
leg: not facts, but **voice**.

## Two design rules worth keeping

**The guardian flags; it never fixes.** `continuity-guardian` reports with severity
(CRITICAL / WARNING / NOTE) and stops. Fixes go through `book-editor`. Separating
detection from repair keeps the auditor from quietly rewriting the thing it is auditing —
and lets it distinguish an ERROR from an INTENT (an unreliable narrator and a planted
re-read reward both look like contradictions).

**The evaluator never scores its own prose.** It evaluates chapters it did not write, and
the anti-inflation protocol assumes 0.5–1.0 of self-bias by default: no score may jump
more than +0.5 per revision cycle, every score needs a cited passage as evidence, and a
floor above 8.0 without extraordinary evidence is to be challenged. A system grading its
own output is at maximum bias; these rules are the counterweight.

## Version note

This is **Book Genesis V4**. Calibration tags inside the agents (`V3.1`–`V3.7`) are
generations that have been folded into V4 — they are current rules, not legacy. Don't
"upgrade" or strip them.

The pipeline is adapted from the open-source
[Best Seller Studio](https://github.com/felipelobomotta-blip/best-seller-studio) agents,
substantially extended here: the premise forge, macro-structure selection, the character
bible and tic budget, motif caps, the mechanical gates, series support, and the print /
IngramSpark path.
