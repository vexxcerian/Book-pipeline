# Glossary

The pipeline's working vocabulary, in one place.

**Amelia Lesson** — the named precedent for tic calcification: a counting device and the
phrase "never once" hardened into a tic and then bled across the cast until everyone sounded
alike, requiring a manuscript-wide de-tic. Why the tic budget and the retired-phrase list
exist. See [CHARACTER-BIBLE.md](CHARACTER-BIBLE.md).

**Anti-pattern budget** — genre-adjusted density ceilings (per 1,000 words) for explanatory
similes, adverbs in dialogue tags, "as if" constructions, metacognitive narration and
emotional temperature reports. The writer aims under it; the disruptor cuts down to it.
Lives in `voice-dna.md`.

**Anti-inflation protocol** — the rules stopping the system from grading its own homework
generously: max +0.5 per revision cycle, cited evidence per score, challenge any floor above
8.0, assume 0.5–1.0 of self-bias.

**Character chaos** — the deliberate irrationality that makes a character read as a person:
an irrelevant thought, a visible cognitive distortion, an unprompted memory, a failure of
emotional management. Literary fiction and memoir cap at 7.5 on Characters without it.

**Chapter loop** — steps A–G run per chapter, strictly sequential: write → dialogue-polish
→ hook-craft → disruption → (entity update) → mechanical preprocess → evaluate → gate.

**Cover-the-name test** — delete every speaker tag and name from a page of dialogue; can a
reader still tell who's speaking? The operational test for cast distinctness.

**CVI (Commercial Viability Index)** — co-equal with the Genesis Score, measuring what
craft quality doesn't predict. **CVI-Launch** = first-year sales potential (commercial
pacing, Tomorrow Test, casual-reader verdict, shareability, concept pitch, human closeness).
**CVI-Legacy** = 20-year potential (originality, theme depth, cultural vocabulary,
re-readability).

**Cultural vocabulary** — words or concepts a book puts into common usage ("Big Brother",
"fear is the mind-killer"). A CVI-Legacy input.

**Device (voice)** — a *class* of verbal habit: counting, listing, pricing, rating,
cataloguing are one device in different coats. At most one character per device.

**Discovery Test** — chapter 1 only: BUY / MAYBE / PUT BACK after three pages in a shop.

**Disruption** — the anti-AI pass that deliberately roughens prose: 2–4 operations on a
strong chapter, up to 6–8 on a weak one, with simile surgery (Pattern #11) as priority one.

**Emotional anchor** — a concrete image carrying a chapter's feeling, planned in the
outline. Deliberately **not** an intensity number: "a 7/10 of grief" is unwritable; "the
unopened second toothbrush" is not.

**Emotional residue** — what the final chapter must leave behind. Resonance, never a
cliffhanger. Tested by the Residue Test.

**Engagement type** — how a book holds readers: empathy, fascination, self-insertion,
intellectual stimulation, or aspiration/identity. Ranked primary/secondary/tertiary; real
bestsellers run two or three at once. A book low on empathy but high on fascination isn't
failing, it's using a different engine.

**Entity state** (`ENTITY_STATE.yaml`) — the structured canon: characters, locations,
objects, timeline, plot threads, world rules, and every piece of knowledge tagged with
`learned_chapter` + source so information-flow violations are detectable.

**Genesis Floor / Average** — the floor is the lowest of the seven dimensions and **is** the
score for gating purposes; the average is recorded but never gates.

**Genesis Score** — the 7-dimension craft assessment: originality, theme, characters, prose
& voice, pacing & coherence, emotion, plus a configurable seventh set per book.

**Hard floor** — the genre-adjusted score below which a chapter is broken and never ships
(literary 7.5, commercial 7.0, thriller 7.0, memoir 7.5, prescriptive NF 7.0). Distinct from
the 8.5 excellence target, which is the only pass.

**Hook / pull** — a chapter's opening (reason to keep reading) and ending (reason to turn
the page). `hook-craft` rewrites only the first and last 3–5 sentences.

**Information flow** — the rule that no character knows a thing before they were told it on
the page. The most common continuity failure in a long manuscript, and the reason entity
state tracks knowledge with a chapter number.

**Irony engine** — the structural tension that generates a premise's conflict natively,
rather than having conflict applied to it. The premise forge scores variants on whether they
have one.

**Macro-structure** — the book's overall shape, selected per premise from a menu (three-act
with jittered turns, kishōtenketsu, five-act, diptych, in-media-res, mosaic, slow-burn +
short finale, circular). Recorded in a `## Macro-Structure` block at the top of `outline.md`.

**Motif cap** — no signature phrase may recur more than 3 times in a whole book. The
ALLOWLIST is a *capped registry*, not an exemption.

**Pattern #11 (Explanatory Extension)** — observations that explain themselves; similes
extended to unpack their own comparison. The most reliable AI fingerprint in prose. Write
similes raw.

**Premise forge** — Phase 1.5: five variants on different irony engines, scored on six
dimensions, winner needs floor ≥ 8.0. Elevates the seed without replacing it — your idea
must stay recognizable in the winner.

**Quality gate** — the per-chapter pass condition: Genesis Floor ≥ 8.5 **and** Casual Reader
≥ 8.5.

**Reader personas** — primary (drives the writing), hostile (drives the evaluation), stretch
(the adjacent audience). Built from real comp-title reviews, not invented.

**Re-read architecture** — planted details that gain meaning on a second reading. A
CVI-Legacy input, and the reason the continuity guardian must distinguish intent from error.

**Shareability** — quote ("this line"), plot ("you won't believe what happens") and
emotional ("this destroyed me"). Scored with a max-weighted formula so a book strong in one
channel isn't penalized for being weak in the others.

**Structural variety rule** — books must not all converge on ~20 chapters of ~5,000 words in
three visible acts with quarter-mark turning points. Chapter count and length emerge from
the beats; the book *total* is the only word gate.

**Theme as question** — a book asks; it never answers. The architect writes the theme as an
interrogative and the ending refuses to resolve it into a moral.

**Tic budget** — at most 2–3 characters in a whole book may lead with a verbal tic, each
earned; no two characters share a device; no signature repeats across your other books.

**Tomorrow Test** — what concrete anchors does a reader still remember tomorrow? Counts both
image and quote anchors; a CVI-Launch input.

**UPDATE RULE** — pipeline improvements are made once, at the repo root (`.claude/` +
`tools/`), so every book inherits them. The one exception is each book's `style_check.py`
ALLOWLIST, which is book-specific by design.

**Voice bank** — benchmark prose samples the book is aiming at, in three registers:
controlled, breaking, and irrelevant-thought.

**Voice DNA** — the prescriptive, executable voice spec: global narration, the
differentiation matrix, the anti-pattern budget, benchmark samples, and voice-under-pressure
(how the prose breaks under emotional overload).

**Voice under pressure** — how narration changes when a character is overwhelmed. Specified
up front, because a voice that stays composed through catastrophe is one of the clearest
tells that nobody was actually feeling it.

**Workflow law** — this repo's default git rule: `main` only, no branches, no PRs, enforced
by hooks. Configurable via `.claude/pipeline.conf`.
