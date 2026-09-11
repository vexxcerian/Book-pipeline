# Progress — Valkyr: Book One

Scaffolded 2026-09-07 by `tools/new-book.sh` into `books/valkyr/valkyr-book-1/`.

## Where this stands

**Ch.1–10 in the manuscript, 35,593 words of prose. Ch.6 through Ch.10 have ALL PASSED the
8.5 gate** — five consecutive pipeline chapters. All three mechanical gates clean on all ten.

Ch.1 is the author's, untouched and locked. Ch.2–5 are his prose with a targeted editor pass.
Ch.6 (8.5/8.79), Ch.7 (8.5/8.79, **Prose 9.0**) and Ch.8 (8.5/8.79, **Prose 9.0 sustained
over 5,600 words**) are pipeline-written and through the gate.

⚠️ **Ch.2–5 were revised AFTER they were scored**, so their recorded floors describe the
pre-revision text. Re-run `book-evaluator` on them if a current number matters.

| Artifact | State |
|---|---|
| `foundation.md` | ✅ 12,110w — characters, theme-as-question, anchors, motifs, opening strategy |
| `outline.md` | ✅ macro-structure + all 26 chapters |
| `voice-dna.md` | ✅ voice reverse-engineered from the author's own prose; device-bleed watch-list corrected from what actually happened |
| `character-bible.md` | ✅ 22+ entries, §TIC BUDGET, §THE ONE CARVE-OUT (the counting device) |
| `voice-bank/` | ✅ README + 13 samples (4 breaking, 2 irrelevant-thought, 5 verbatim author prose) |
| `manuscript/chapters/` | ✅ Ch.1–10, **35,593 words**, italics + 23 scene breaks restored from the PDF |
| style / grammar / voice-wear | ✅ clean on all nine, calibrated to the author's measured voice |
| `feedback/pov-map.txt` | ✅ single POV, Vexx, Ch.1–10 |
| `ENTITY_STATE.yaml` | ✅ audited Ch.1–8; 9 characters, 4 locations, 8 objects added; CF-04 and CF-13 closed |
| Genesis scores | Ch.1 **8.5** (prose 9.0, locked) · Ch.6/7/8 **8.5 / 8.79** · Ch.9 **8.5 / 8.71** · Ch.10 **8.5 / 8.64 PASS** · Ch.2–5 stale |
| `evaluations/` | ✅ per-chapter evals, pass reports, `continuity/ch1-8-audit.md` |

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

## The Ch.7–8 build, and the three layers of THE SEAM

Ch.7 ("Issue Date", 1,535w, declared punch chapter) passed at **8.5 / 8.79** and reached
**Prose 9.0**, the locked Ch.1's number. Ch.8 ("Merrick", 5,717w, the book's one long
immersive mission chapter) is drafted and mechanically clean.

Between them they took the pipeline's fingerprint apart into three layers, and each layer
was found *after* the one above it was closed:

1. **Punctuation — closed.** The em-dash/`and` calibration from Ch.6 holds. Ch.7 drafted at
   `and` 35.9/1k and was converted to 15.0 before the file was finalised.
2. **Connective habit — still recurring, now caught at draft time.** Ch.8 drafted at **45.5
   `and`/1k**, the worst in the book, on a brief that carried the warning in writing. Three
   chapters running. It is no longer treated as something a writer can be told out of: the
   root `book-writer.md` now carries a **60%-of-draft self-check** rather than a brief-time
   warning, and it worked on its first outing — Ch.8's final 898 words came in at 20.0/1k.
   The repair took **111 conjunctions** out of Ch.8, none of them from a spoken line.
3. **Breath — gated, after two wrong implementations.** See below.

### The breath gate, and why the obvious version of it was wrong

The Ch.7 evaluator found that Ch.6 and Ch.7 were shorter-breathed than every author chapter
and recommended gating sentence length. Measured **across the whole chapter** the finding
looked enormous — Ch.6 and Ch.8 at medians of 8 and 7 against an author minimum of 10.

It was almost entirely **dialogue share**. Everyone's dialogue is short, this author's
included: his runs to a median of 6–10 words and puts up to 47% of its lines at six words or
fewer. Ch.8 carries 201 spoken lines to 149 of narration, more than any chapter in the
drafted five. **A gate on the un-split number would have told a writer to lengthen people's
speech** — which would have flattened the twelve-voice ensemble that is Ch.8's whole texture.

Split the registers and what survives is small, specific, and points in **opposite
directions**: Ch.6 hit the median but under-reached on the long accumulating sentence (≥40w
9.3% against his 11.5% floor); Ch.8 over-reached on that same metric (18.8%) and sat a point
light on the median. That is not one habit.

`style_check.py` now gates **narration only** — median ≥13.0, ≥40w ≥11.5%, ≤6w ≤33.0% — all
calibrated with the gate's own tokenizer against the author's own narration. All five author
chapters pass every threshold. The **dialogue:narration ratio is reported and deliberately
not gated**: the author himself swings 0.44:1 to 1.16:1, so there is no band to defend.
`PUNCH_CHAPTERS = {7}` is the one exemption and it was earned in the outline before the
chapter was written.

Ch.6 was repaired with four joins (≥40w 9.3% → 12.4%) using punctuation and conjunction only.
Its `and` count went **down** in the process.

⚠️ **Ch.8 now has no slack in any direction:** `and` 23.3 against a 24.0 ceiling, em-dash
11.7 against 12.0, `the way` at exactly 5 of 5, narration median exactly 13.0 against a floor
of 13, ≥40w 11.7% against a floor of 11.5%. Any later pass that shortens anything in Ch.8
breaks a floor. Brief accordingly.

### Two defects no gate could see, found by reading a diff

- **Straight quotes.** The author's chapters are 100% typographic (reconstructed from his
  PDF). Every pipeline chapter arrived mixed — Ch.6 was *mostly straight*, 193 straight
  double quotes to 90 typographic. Ch.8's closing line, which must be character-identical to
  the sentence it quotes from the top of the chapter, differed by one apostrophe. 370
  characters converted across Ch.6–8; now gated.
- **Semicolons.** The author uses **zero** across all five of his chapters. Two of the three
  found in pipeline prose were *correct* — they sit inside a quoted psych report, and
  institutional prose uses semicolons. The check exempts whole-italic paragraphs (this book's
  convention for quoted documents) and **reports the exemption** rather than dropping it
  silently. Ch.6 prints `2 semicolon(s) exempted inside quoted documents` and passes honestly.

## The 2026-09-09 full read-through and audit — what a whole-manuscript pass found

Every pass before this was per-chapter. The first cross-manuscript audit, plus a full human
read of all eight chapters, found things no per-chapter gate can see **because within any one
chapter the usage is perfectly consistent.**

**1. The book was being written in two different Englishes.** Ch.1–5: 82 US spellings, zero
British. Ch.6–8: 31 British forms — including `"soft clothes, grey"` against the locked Ch.1's
**gray room**, used six times and the book's founding image, and `"Cooperative with programme
throughout"` against a registry that says *the program*. Converted, and **gated**:
`style_check.py` now takes `DIALECT = "us"` and fails any chapter carrying the other dialect.

**2. The pipeline had over-corrected past the author into plainness.** The analytical simile
is the model's #1 fingerprint, so the disruptor cuts them and voice-dna bans *as if* — and the
result sailed past "not machine-made" into **plainer than the author has ever written**: he
runs 2.1–4.4 figurative comparisons per 1k, Ch.6/7/8 came in at 0.9, 1.3 and **0.4**. Ch.8 used
one comparison per 2,800 words; his plainest chapter uses one per 480. Seventeen **bare**
comparisons restored; a **floor** added at 2.0. *A ceiling with no floor only ever catches the
overshoot in one direction.*

**3. A POV break that was also a headcount error.** Ch.8's failed stack narrated a contact in
close visual detail from inside a corridor, then had *"Vexx came in through the near door"* —
and "four of them stacked" left three once Gaia was held at the corner and Zeus "had come in
behind Vexx". One change fixed both: Vexx is in the stack. Both breath floors went **up**.

**4. Two things declined, with reasons.** The audit read Ch.6's *"He was tidying"* as spending
Merrick's reserved self-echo early — it is not the same device; Corwin is quoting a mantra he
knows he repeated. And a `somebody`/`nobody` ceiling of 3.0 was recommended for the third
chapter running; **the author himself runs 4.2–6.3**, so that threshold would push the prose
away from his voice. Recorded so it stops being re-proposed.

### Two bugs in the gate itself, both found by an agent being honest

- **The rounding bug.** `per1k()` rounded and the comparisons ran on the rounded value, so
  every threshold had half a step of slop **in both directions, always favouring the chapter
  under test**: a true 1.9934/1k displayed 2.0 and passed a floor of 2.0. Found because the
  editor volunteered that a pass was marginal instead of reporting a green number. Comparisons
  now run on the exact rate; only the display rounds.
- **The simile metric was counting the wrong word.** *"I like him already"*, *"cells like
  this"*, *"They like him"* — the verb and the bare preposition. It was tracking how much
  dialogue a chapter had. Nearly became the fifth threshold in that file calibrated against
  the wrong measurement. Corrected — and the finding got *stronger*.

### Canon corrections — a rule contradicting the prose it was written to protect

**The counting device.** The bible reserved counting/tallying to Spector alone and named the
violation: *"if Vexx starts tallying anything, that is device bleed."* The author's own Ch.4
does exactly that (*"keeping a private tally of which was which"*), and the same file's Rx
entry assumed it three lines below the ban. Narrowed: **Spector owns the SPOKEN count**
(craft, performed for a room); **the private, unspoken tally is Vexx's and Rx's.** A tally said
aloud to another character has crossed over. See `character-bible.md` §THE ONE CARVE-OUT.

**The device-bleed watch-list was aimed at the wrong characters.** voice-dna predicted Zeus or
Gaia, and Spector's counting onto Bastion. Those routes stayed clean and the watched pairs
held. The bleed went where nobody was looking: Goliath took Vexx's term-correction shape *and*
spoke Spector's countdown verbatim; Gaia applied Spector's *N-of-the-M* construction to
people's interior states; Paladin spoke Rx's capped denial; **Zeus asked *why***, which he does
nowhere else in the book, and took six edits in one chapter. **The lesson is not a better list
of pairs — a predicted watch-list makes you blind to the routes it does not name.** And every
one of those lines passed the Cover-the-Name Test, because that test measures whether a line is
*distinctive* and never *whose it is*. `dialogue-polish` now runs a separate Device Bleed Scan.

**CF-13 — Holst's first name.** The plan said *never given a first name*; Ch.7 prints
*STAFF SERGEANT DERIC A. HOLST* off an archive line with *photo?* in pencil in the margin. The
prose is right and the constraint yielded — a name recovered off a scanned record is what makes
it read as a document rather than a prop. Narrowed to: **full name only inside quoted document
text; narration says HOLST, D.** He still never appears, never speaks, is never described.

## The two inventories — check every new chapter against BOTH

Chapters 2–5 all drifted onto one closing figure because nothing was tracking the sequence.
`book-architect` and `hook-craft` now carry the rules; these are the running tallies.

**CLOSERS — nine chapters, nine shapes. No repeats, and Ch.2's is spent.**

| Ch | Closing move |
|---|---|
| 2 | dramatic irony — **SPENT, do not reuse in this book** |
| 3 | a scene beat with another character |
| 4 | an interior equation |
| 5 | a physical object handled in the dark |
| 6 | a misdirected answer to a stranger |
| 7 | the narration stops and hands the reader an unglossed found document |
| 8 | the narrator re-reads a document **while writing its fourth instance himself** |
| 9 | the POV character **involuntarily begins executing the method he refused**, stops partway, and does something ordinary and courteous on top of it |
| 10 | an unremarked act of **preparation for the antagonist** — memorising something to have it ready for him next time |

Ch.7 and Ch.8 both ended on a document — two running was the limit, and Ch.9 cleared it with
no paper on the last page, as the outline required.

**OPENINGS — the drift warning is cleared and stays cleared.**

| Ch | Opening move |
|---|---|
| 2–5 | a retrospective framing statement — four in a row |
| 6 | a physical object in near-real-time (the visitor form) |
| 7 | a raw administrative document (the boots requisition) |
| 8 | mid-transit, mid-argument, no scene-setting |
| 9 | a line of dialogue with no attribution and no setting, three words in |
| 10 | **the meeting time** — a summons, flat, no explanation |

## Resume point

1. **Ch.11's loop:** dialogue-polish → hook-craft → disruptor → evaluate → 8.5 gate.
2. **Then Ch.12.** Eleventh/twelfth distinct closing shapes — check the inventory first.
3. **Run `continuity-guardian` after Ch.12** — the last full audit was Ch.1–8.
4. **The live measured items, each with its definition** (a metric name is not a definition):
   - **Narration `and`** (`\band\b` per 1k, narration only): author **18.19–18.90**, a
     0.7-point band. Pipeline 20.68 → 20.39 → 22.07 → 24.35 → **18.39**. Ch.10 reversed the
     rise from a draft. **Not gated** — retrofit is blocked on Ch.9 by the long-sentence floor,
     and a gate that can only stay red erodes. Carried in the writer brief, where it has now
     worked twice.
   - **Generic-person manner attribution** (*"like a man reporting a figure off a gauge"*):
     author max **1 per chapter**; pipeline 3 · 0 · 5 · 3 · 4. **Plateaued, not rising, which
     is worse** — every other fingerprint here was caught by its slope. §STANDING OFFENCE #7.
   - **Numeric density** — ⚠️ **two incompatible definitions exist in this project's own
     committed files.** Digits-plus-spelled-out gives the author 4.8–14.0; the Ch.9 eval's
     regex gives 11.7–23.4. A threshold of 16.0 is right under the first and puts the **locked
     Ch.1 in breach by 7.8 points** under the second. Always state which.
5. Optional: the Ch.5 ending review and the `STATE.yaml` FOLLOW-UP items. None block drafting.

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

- **The comparison gate has a known gap.** `the way X does Y` is one of the author's comparison
  forms (*"the way weather fills a sky"*) and is **not counted**, because the same construction
  is separately capped as a pipeline fingerprint and counting it twice would have the gate
  arguing with itself. The measure is consistent rather than complete — it reads the author and
  the pipeline through the same narrow window. Closing it means re-deriving the comparison
  floor and the `theway` ceiling from the author together.
- **Three comparisons added in the 2026-09-09 repair were flagged by the editor itself as
  possibly added rather than found** — Ch.6 *"like a man checking a table for dust"* (it
  supplies a motive for a gesture that may be better unmotivated), Ch.8 *"holding it like a hot
  water bottle"*, Ch.8 *"like a switch wired to nothing"* (named as chosen for quota reasons).
  Left in; worth the author's eye. Details in `evaluations/ch6-8-comparison-repair.md`.
- **Ch.8 has very little slack.** It sits near several limits at once; brief any future pass on
  it accordingly, and re-measure after every edit.

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
