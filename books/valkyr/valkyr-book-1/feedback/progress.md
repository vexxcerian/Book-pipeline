# Progress — Valkyr: Book One

Scaffolded 2026-09-07 by `tools/new-book.sh` into `books/valkyr/valkyr-book-1/`.

## Where this stands

**Ch.1–6 in the manuscript. Ch.6 is the first chapter to PASS the 8.5 quality gate.**
Ch.1 is the author's, untouched and locked. Ch.2–5 are his prose with a targeted editor pass.
Ch.6 is the first pipeline-written chapter: Genesis floor **8.5**, average **8.79** — it matches
the locked benchmark's floor. All three mechanical gates pass on all six.

⚠️ **Ch.2–5 were revised AFTER they were scored**, so their recorded floors describe the
pre-revision text. Re-run `book-evaluator` on them if a current number matters.

| Artifact | State |
|---|---|
| `foundation.md` | ✅ 12,110w — characters, theme-as-question, anchors, motifs, opening strategy |
| `outline.md` | ✅ 19,665w — macro-structure + all 26 chapters |
| `voice-dna.md` | ✅ 4,228w — voice reverse-engineered from the author's own prose |
| `character-bible.md` | ✅ 8,357w — 22 entries, §TIC BUDGET, cover-the-name test run in-file |
| `voice-bank/` | ✅ README + 13 samples (4 breaking, 2 irrelevant-thought, 5 verbatim author prose) |
| `manuscript/chapters/` | ✅ Ch.1–6, **~20,200 words**, italics + 23 scene breaks restored from the PDF |
| style / grammar / voice-wear | ✅ all three clean, calibrated to the author's measured voice |
| `feedback/pov-map.txt` | ✅ single POV, Vexx, Ch.1–6 |
| `ENTITY_STATE.yaml` | ✅ 20 characters, 64 knowledge entries, evidence chain-of-custody |
| Genesis scores | Ch.1 **8.5** (prose 9.0, locked) · **Ch.6 8.5 / 8.79 PASS** · Ch.2–5 stale |
| `evaluations/` | ✅ per-chapter evals + `ch1-5-summary.md` — read the summary first |

## The structure, in one paragraph

**Four-movement kishōtenketsu**, not three acts, as four titled Parts — INTEGRATION (Ch.1–2) /
ASSESSMENT (Ch.3–13) / RECLAMATION (Ch.14–19) / DISPOSITION (Ch.20–26), turning at 8 / 48 /
72%. Chosen because Book One's ending is a locked **non**-climax and kishōtenketsu is the one
common structure whose fourth movement is reconciliation rather than resolution. The author's
Act Three is **split, not altered** — the *ten* sits inside it. **Σ = 95,829 words**
(14,630 drafted + 81,200 new), chapters 1,400–6,800 (4.9× spread). Full reasoning is in the
`## Macro-Structure` block at the top of `outline.md` — read it before questioning the shape.

## What was decided on 2026-09-07 (all reversible — say so and it changes)

1. **AI-speech formatting: the author's convention, recovered not guessed.** The italics were
   pulled back out of the PDF's *font layer* (`DejaVuSerif-Italic`), so Rx and the AIs speak in
   unquoted italics exactly as written, and voices in the room keep their quotes. 233 italic
   runs restored. Paragraph breaks were rebuilt at the same time — the earlier staging copy had
   merged Rx's dialogue into the narration around it.
2. **The gates were calibrated to the author, not the author to the gates.** The strict
   ceilings exist to catch a *machine's* tells; several were firing on ordinary human phrasing.
   `tools/style_check.py` now has `AUTHOR_DRAFTED`/`AUTHOR_CEILINGS` and
   `tools/voice_wear_check.py` has `RETIRED_EXEMPTIONS` — **Ch.1–5 measured, Ch.6–26 stay
   strict.** Not one word of the author's prose was edited to pass a gate.
3. **`drafted_words` = 14,630**, by `wc -w`, the same tool the floor gate uses.

## The 2026-09-08 revision pass (evaluate, then edit)

`book-evaluator` scored all five; `book-editor` revised **Ch.2–5 only**. Ch.1 untouched.

- **Ch.2** — Zeus's recruitment dramatized (~600w). He had *no dialogue in his own
  recruitment* despite carrying Ch.3's interrogation and Ch.4's de-escalation. His line
  *"You don't need me for the ending. You need me for the twenty minutes before it, while
  it's still possible for it not to be one"* is a deliberate plant that Ch.4 now cashes.
  Gaia and Paladin each get one dramatized beat.
- **Ch.4** — the Reyes de-escalation dramatized (~360w). 700 words of moral crisis with a
  live kill authorization had been resolving in one summary sentence. It now gets worse
  before it breaks, and Reyes never touches his weapon.
- **Ch.3** — Paladin's two feed-lines (*"Our target?"* / *"Which tells us what?"*) replaced
  with lines that come from his creed rather than the scene's need for exposition.
- **Across Ch.2–5** — three told-emotion sentences staged instead of reported; the "filed it
  away" stacks unstacked (9 uses → 4); all four closers differentiated so no two consecutive
  chapters share a shape or a verb, and every closer sits inside Vexx's perception.

## The Ch.6 build, and what it taught the pipeline

Ch.6 ran the full loop — write → dialogue-polish → hook-craft → disruptor → evaluate — and
surfaced four pipeline defects, all now fixed at the root:

1. **`style_check.py` had a latent `NameError`** that could only fire on a non-author chapter.
   `doctor.sh` now RUNS each book's gates instead of only parsing them.
2. **`book-architect` audited opening diversity but not endings**, which is why Ch.2–5 had all
   drifted onto one closing figure. It now carries an ending-diversity check, and `hook-craft`
   a PULL SEQUENCING section.
3. **`book-disruptor` wrote its backup into `manuscript/chapters/`**, where the gates glob it
   as a real chapter and fail the chapter against its own backup. Backups now go to
   `evaluations/`.
4. **The style gate had ceilings but no FLOORS** — so a pipeline chapter could pass by writing
   *calmer* than the author. That was the real seam (below).

**THE SEAM — the finding that matters most for Ch.7–26.** The evaluator could not find the
pipeline's known fingerprint (analytical simile, competence cascade, emotional temperature) —
none of it fires. But four rhythm metrics put Ch.6 outside the author's entire range in the
same direction: **the author interrupts himself with em-dashed appositives; the pipeline
chained clauses on `and`.** No sentence was wrong; twenty chapters of it would be a second
author. `style_check.py` now gates em-dash/comma FLOORS and `and`/vague-pronoun ceilings, and
reports rhythm per chapter. Ch.6 was recalibrated back into band (em-dash 4.7 → 9.5/1k,
`and` 40.4 → 23.7/1k) **without changing one idea, image, beat or line of dialogue.**

## Resume point

1. **The chapter loop from Ch.7:** write → dialogue-polish → hook-craft → disruptor →
   evaluate → quality gate. Commit per chapter.
2. **Watch the rhythm numbers** `style_check.py` now prints. They are the early warning.
3. Optional: the Ch.5 ending review, and the FOLLOW-UP items in `STATE.yaml` (the Aglaope
   metacognition line, Ch.2's chaos density). None block drafting.

## Worth the author's eye

- **Ch.5's ending was rewritten, and this is the one to look at first.** The old close —
  *"Richard Jameson slept, as he had for four years… He was wrong. He simply didn't know it
  yet."* — asserted a fact Vexx cannot know, breaking the POV lock, and was the fourth
  consecutive chapter to end on the same zoom-out figure. It now ends on the dog tag: *"He
  could still find the serial with his thumb. A number that belonged to nobody. He put it
  back before it got light."* The old lines are recoverable from git at `1c53c57`.

- **Ch.2 is the densest chapter in the book** — simile 7.0/1k and em-dash 11.1/1k, both the
  highest of the five. It passes because the ceilings are set to the author's own range, but
  if any chapter would benefit from a trim, it is this one.
- **Ch.2, "never once"** — `"a man who had never once in his career been kept waiting"`. On the
  pipeline's retired list as a model crutch; kept because here it is doing real
  characterisation work. Declared explicitly in `RETIRED_EXEMPTIONS`, not silently excused.
- **"the first time since"** is allowlisted at a cap of 4 (its current count). Vexx dates
  everything from a grief landmark — the gray room, the empty casket, a folder full of nothing.
  Deliberate, and now capped so Ch.6–26 cannot help themselves to more of it.

## Things not to re-litigate

These are settled and the reasoning is written down; changing one means changing the outline.

- The kishōtenketsu structure and the four Part titles (`outline.md` §Macro-Structure).
- **The second cell** — the *ten*. Vexx's cell assesses; another disposes. Built from the
  locked "no contact between cells" rule; it is what retroactively converts the drafted
  Ch.3–5 from spent beats into evidence, and it is why Ch.1–5 do not need rewriting.
- **Ives dies** (cleared Ch.13, dead Ch.14) and **Reyes lives** (canon) — Reyes surviving is
  what makes the pattern legible.
- Stage-3 unlock lands in **Ch.13**. The "man I suspect is the man I report to" turn is
  **Ch.21**. The ending runs **Ch.24 → Ch.26**.
- **Jameson has no verbal tic, deliberately.** A catchphrase would make him legible, and a
  scene where the reader can see he is the villain is a failed scene.
- The donor-stock plant is **one Spector line in Ch.18**, marked `CUTTABLE-PLANT` inline.
  Nothing in Ch.19–26 depends on it.

## Known risks

- **`research/original-draft.md` is SUPERSEDED** — it is the staging copy, has no italics, and
  has coarser paragraph breaks. The live text is `manuscript/chapters/`. Edit the manuscript.
  The unmodified source is preserved at `research/valkyr-source.pdf`; check it before assuming
  anything about formatting.
- **The manuscript was machine-reconstructed from the PDF's LAYOUT**, not from a text
  heuristic. The PDF encodes three distinct vertical gaps — ~5 line wrap, ~14 paragraph break,
  ~43 scene break — and a font name per character, so paragraphs, scene breaks and italics are
  all read off the geometry rather than inferred. The word stream was verified token-for-token
  identical to the raw extraction. The one remaining guess is at page turns, where there is no
  gap to measure and a right-margin test decides whether a paragraph continues (~30 places in
  the book). A human proofread against `research/valkyr-source.pdf` is still worth one pass.
- Comp titles in `STATE.yaml` are provisional; `book-researcher` has not run on this book.
- **Word counts: always use `wc -w`.** Python's `.split()` counts a standalone " — " as a word
  and `wc` does not, so on this em-dash-heavy prose the two differ by ~150 words over five
  chapters. The floor gate and `doctor.sh` both use `wc -w`; quote that figure and no other.
