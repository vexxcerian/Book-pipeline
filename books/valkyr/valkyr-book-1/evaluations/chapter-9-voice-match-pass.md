# Chapter 9 — voice-match pass (Revision 5)

Date: 2026-10-08. Surgical pass only: no beat, scene, structure or outcome changed.
Three breaches closed — the narration **adverb floor**, the narration **`and` ceiling**
(§THE SEAM) and the cross-chapter repeat **`"that had nothing to do with"`**.

All numbers below are `tools/style_check.py`'s own tokenizer, narration register.

| metric | before | after | wall |
|---|---|---|---|
| **narration adverbs** | **0.6/1k (1)** | **13.0/1k (23)** | floor 10.5 · ceiling 17.0 ✅ |
| **narration `and`** | **24.3/1k (43)** | **18.6/1k (33)** | ceiling 19.5 ✅ *(author 18.2–18.9)* |
| narration median | 14 | 14 | floor 14.0 ✅ *(unchanged — no sentence added or split)* |
| narration ≥40w | 14.0% (13/93) | 14.0% (13/93) | floor 13.0 · ceiling 16.5 ✅ |
| narration ≤6w | 19.4% | 19.4% | ceiling 30.0 ✅ |
| em-dash | 33 (9.8/1k) | 36 (10.7/1k) | floor 8.5 · ceiling 12.0 ✅ *(3 of 7 units spent)* |
| simile | 2.7/1k | 2.7/1k | floor 2.0 ✅ *(none lost)* |
| flat-man | 3 | 3 | ceiling 3 ✅ *(none added)* |
| comma | 60.2/1k | 61.8/1k | floor 58.0 ✅ |
| `, which` gloss | 0.6/1k (1) | 0.6/1k (1) | ceiling 1.0 ✅ |
| whole-chapter `and` | 22.4/1k | 19.3/1k | ceiling 24.0 ✅ |
| `the way` | 3 | 3 | ceiling 5 ✅ |
| semicolons / straight quotes / dialect | 0 / 0 / none | 0 / 0 / none | ✅ |

`style_check.py` now prints **no VOICE-MATCH line for Ch.9** (book total 12 → 10 issues).
`grammar_check.py` clean (0 errors). `voice_wear_check.py` clean.

---

## The 22 adverbs added, in order of appearance

**Zero went into a dialogue tag.** Every tag in the chapter is still a bare `said`.
All 22 are in narration; none is a manner adverb propping up a weak verb.

| # | adverb | where (¶ / line) | the sentence |
|---|---|---|---|
| 1 | **properly** | ¶1 / L8 | "Vexx answered before he had *properly* worked out who was asking" |
| 2 | **easily** | annex / L16 | "— *easily* the coldest room in the building" |
| 3 | **slightly** | annex / L16 | "The lights came on in banks of two, *slightly* late, as a man walked the length of it" |
| 4 | **steadily** | annex / L16 | "like off a cellar wall, working *steadily* into a man's back inside the hour" *(also AND-fix 1)* |
| 5 | **completely** | Zeus at the table / L18 | "a cup at his elbow with a skin gone *completely* over the top of it" |
| 6 | **entirely** | the grid / L20 | "It was worked *entirely* in pen." |
| 7 | **actually** | the four questions / L44 | "where she *actually* learned the acoustics thing" |
| 8 | **lawfully** | the index / L46 | "no arrangement of words that would *lawfully* put them on a screen" *(was the adjective "no lawful arrangement" — converted, no word added)* |
| 9 | **finally** | the index / L46 | "until the third time, when he *finally* understood the set was being sorted" *(also AND-fix 4)* |
| 10 | **carefully** | the index / L46 | "He wrote the sort out *carefully* on the back of his hand" |
| 11 | **necessarily** | the index / L46 | "Somewhere under all of it, *necessarily*, was a routing office" *(also AND-fix 5)* |
| 12 | **honestly** | the refusal / L76 | "ahead of anything he would *honestly* have called a decision" |
| 13 | **deliberately** | the table edge / L90 | "did not come back — then *deliberately* let go of it" — and the next sentence is the control failing, which is why it is there |
| 14 | **actually** | the cup / L94 | "without having *actually* written a thing with it" |
| 15 | **exactly** | the unsaid thing / L100 | "he could see the shape of it *exactly*" |
| 16 | **finally** | the chair / L114 | "Vexx turned his chair round, *finally*, to face into the room." |
| 17 | **squarely** | the chair / L114 | "The chair had been pointed *squarely* at the terminal all night." |
| 18 | **exactly** | the list / L162 | "he knew *exactly* what it was without being told" |
| 19 | **separately** | the Ridgeway dog / L220 | "every man on the gate fed it, *separately*, not one of them admitting to it" *(also AND-fix 9)* |
| 20 | **considerably** | the four sentences / L232 | "She waited *considerably* longer than the answer needed." |
| 21 | **normally** | the Kell reasoning / L244 | "would *normally* go through a base accommodation office" |
| 22 | **plainly** | the Kell reasoning / L244 | "by asking him *plainly* about his summer" |

Pre-existing: **slowly** (L234, "She nodded, slowly"). Total 23.

**Register check.** Every one of the 22 is a plain spoken connective or a hedge, and 14 of
the 22 lemmas are in the author's own Ch.1–5 narration (`properly, easily, slightly,
completely, entirely, actually, finally, carefully, honestly, deliberately, exactly,
considerably, plainly, slowly`). The eight not literally in his five chapters —
`steadily, lawfully, necessarily, squarely, separately, normally` — are all from the same
family (plain, non-manner, inferential) and sit in the inferential/speculative passages,
which is exactly where he banks them. Ch.11's closed version of this breach is the
register model.

## The 10 narration `and`s removed — and how

**Never by deleting the conjunction.** §THE SEAM. Six are em-dashed or comma-set
appositives, three are asyndeton, one is a participial recast.

| # | ¶ / line | before → after | device |
|---|---|---|---|
| 1 | L16 | "…cellar wall, **and it was** into a man's back…" → "…cellar wall, **working steadily into** a man's back…" | participle |
| 2 | L16 | "a materiel index on it, **and** a laminated card…" → "a materiel index on it, a laminated card…" | asyndeton — the paragraph is already a catalogue of fragments ("Nine bays of shelving, of which four held anything.") |
| 3 | L46 | "as a run of serials **and had it come back** with…" → "as a run of serials **—** it came back with…" | em-dash *(+1)* |
| 4 | L46 | "in a different order, **and** he took it…" → "in a different order **—** he finally took it…" | em-dash *(+1)* |
| 5 | L46 | "a duty roster under that — **and** people on the roster" → "…under that — people on the roster" | existing em-dash carries the appositive |
| 6 | L128 | "with the side of his thumb, **and said**, "Thank you"" → "…with the side of his thumb, said, "Thank you"" | asyndeton — the thank-you now arrives as one more item in the list, which is the beat |
| 7 | L152 | "burning over the servery, **and** Aglaope was at…" → "burning over the servery **—** Aglaope was at…" | em-dash *(+1)* |
| 8 | L184 | "with nothing behind it, **and** went back to the pad" → "…with nothing behind it, **then** went back to the pad" | sequence adverb |
| 9 | L220 | "every man on the gate fed it, **and not one of them would admit to it**" → "…fed it, separately, not one of them **admitting** to it" | participle + comma-set adverb |
| 10 | L232 | "four sentences ready **and they were all true**, and every one…" → "four sentences ready, **all of them true**, and every one…" | appositive |

**No sentence was split and no sentence was added.** That was deliberate: splitting would
have been *safe* for Ch.9's median (which sits on its 14.0 floor, so raising it is the safe
direction), but every split raises the narration sentence count and **13 of 93 ≥40-word
sentences is only 1.0 point above a 13.0% floor** — seven added sentences would have taken
it to 13.0% exactly and any split of a ≥40w sentence would have cut the numerator too
(12/94 = 12.8%, a floor breach). Appositive and asyndeton move `and` at zero sentence cost.
Both metrics therefore read *identical* before and after.

Four ≥40w sentences shed a word in the `and` repair and were checked individually: L46
"Twice it returned…" 42 → 42 (the adverb replaced the conjunction), L128 "Vexx sat with
that a while…" 47 → 46, L152 "The mess had the urn off…" 41 → **40** (still counted),
L232 "He had four sentences ready…" 57 → 56. None fell below 40.

## The cross-chapter repeat

`"that had nothing to do with"` was in Zeus's offer speech (L62) — the only instance in
Ch.9, and in dialogue, which is why dialogue was touched here and nowhere else.

> "— and both of them have done it before, for reasons that had nothing to do with you or
> with me."
> → "— and both of them have done it before, for reasons **of their own that had no bearing
> on** you or on me."

"No bearing on" is institutional-precise, which is Zeus's register, and the following two
sentences ("A man wanting his own service record because the pension office lost it. That
kind of thing.") still gloss it exactly as before. The gate now reports the phrase at
**×3 [3, 8, 11]** — Ch.9 is out, Ch.3 is the author's, so only two pipeline instances
remain and the FLAG has one recast left in it. `voice_wear_check` agrees: "had nothing to
do with — in 3 ch".

**No new repeat was created.** The two-chapter pair list is still exactly 42 entries, with
the same contents.

## Not touched — verified intact after the pass

- **Zeus's three turns.** No question added anywhere; he still never asks why. "Ask a
  different question." is unaltered.
- **Aglaope's casualty-list scene.** `Ansel` / `Anseth` both present and distinct (L208,
  L212). The hour and forty minutes and the nine pages are unaltered. No edit of any kind
  landed between L152 and L212 except the one `exactly` at L162 and the `then` at L184.
- **"Have you told anybody but him," she said. / "No."** — byte-identical.
- **Merrick's notebook beat (L48).** Untouched entirely — bus bars, runoff figures, the
  three years of *depot, no answer*. It acquired nothing, including an adverb.
- **Rx's "Fine" (L144).** Untouched.
- **The clock.** 01:10 ("ten past one"), the hour of silence, the four questions, the
  104-minute badge log, Aglaope "since half past two", close at four — all unaltered.
- **POV.** Every adverb added is an observation or an inference available to Vexx in the
  room (`evidently`-class hedges deliberately preferred in the speculative paragraphs:
  `necessarily`, `normally`, `honestly`). Nothing new is known that Vexx does not know.
- **The two registers.** No quotation mark became an italic or vice versa. Zero straight
  quotes, zero semicolons, zero British forms.
- **Both retrospective-narrator intrusions** and the flat-man count (3, at ceiling) are
  unchanged — no construction of either kind was added.

## For the next pass

- **Ch.9's median is still exactly 14 against a 14.0 floor.** It was 14 before this pass
  and no edit moved it, but the headroom is still zero: **any pass that adds a short
  narration sentence to Ch.9 breaks the floor.** Lengthen or join; do not add.
- **≥40w is 14.0% against a 13.0% floor** — about seven added narration sentences of
  room, and splitting any of the thirteen long ones costs double.
- **Em-dash is 10.7/1k with 4 units of headroom left** (36 of ~40). Spend them on `and`
  if Ch.9 is ever re-measured over.
- **Flat-man is at the ceiling (3).** Any new "like a man…" / "in the voice of a…" in Ch.9
  is an immediate breach.
- Question marks remain **0.0/1k** against the author's 1.0–3.0. Reported, not gated, and
  out of scope for this pass — but Ch.9 is the chapter that produced the note, and the
  unpunctuated-question device is doing it deliberately here. Worth a human eye, not a fix.
