# Chapters 6, 7 and 10 — voice-match pass

Date: 2026-10-11. Three separate jobs, three different envelopes, one method:
**add the plain spoken connective adverb back into narration, and convert `and`-chains into
the author's own interruptions.** No beat, scene, structure, outcome, number or season
changed in any of the three. No sentence was split, added or removed anywhere.

Method is the one worked out on Ch.9 (`chapter-9-voice-match-pass.md`) and repeated on Ch.8.
All numbers are `tools/style_check.py`'s own tokenizer, **narration register**.

`style_check.py` now prints **no VOICE-MATCH line anywhere in the book** and closes with
`RESULT: clean.` `grammar_check.py` 0 errors book-wide. `voice_wear_check.py` clean.

---

## Summary — before / after

| metric | Ch.6 before | Ch.6 after | Ch.7 before | Ch.7 after | Ch.10 before | Ch.10 after | wall |
|---|---|---|---|---|---|---|---|
| **narration adverbs** | **2.7 (7)** | **12.4 (32)** | **3.2 (3)** | **13.8 (13)** | **3.3 (8)** | **12.3 (30)** | floor 10.5 · ceiling 17.0 |
| **narration `and`** | **20.7 (53)** | **18.9 (49)** | **20.4 (19)** | **19.1 (18)** | 18.6 (45) | **18.5 (45)** | author band 18.2–19.5 |
| narration median | 14.5 | 15.0 | 11 | 11 | 17.0 | 17.0 | floor 14.0 · ceiling 18.0 |
| narration ≥40w | 13.2% (18/136) | 13.2% (18/136) | 12.3% | 12.3% | 14.7% (17/116) | 14.7% (17/116) | floor 13.0 · ceiling 16.5 |
| narration ≤6w | 25.0% | 25.0% | 33.3% | 33.3% | 27.6% | 27.6% | ceiling 30.0 |
| em-dash | 47 (10.8) | 48 (10.9) | 15 (9.9) | 15 (9.8) | 48 (10.4) | 48 (10.4) | floor 8.5 · ceiling 12.0 |
| simile | 9 (2.06) | 9 (2.05) | 4 (2.64) | 4 (2.62) | 10 (2.17) | 10 (2.16) | floor 2.0 · ceiling 5.0 |
| flat-man | 1 | 1 | 0 | 0 | 1 | 1 | ceiling 3 |
| comma | 59.7 | 59.2 | 69.9 | 69.5 | 62.5 | 62.4 | floor 58.0 |
| gloss `, which` | 0.8 | 0.8 | 0.0 | 0.0 | 0.0 | 0.0 | ceiling 1.0 |

Ch.7's breath row is PUNCH-exempt and was not touched; it is reported to show it did not move.
Ch.6's and Ch.10's breath rows are **byte-identical in sentence count** — the whole repair
was done at zero sentence cost, which is what the two long-sentence floors required.

### The arithmetic that set the sizes

- **Ch.6's ≥40w sits 0.2 points above its floor** (18 of 136 = 13.24% against 13.0), so
  splitting was unavailable: one split of a long sentence gives 17/137 = 12.41%, a breach.
  Every adverb went *inside* an existing sentence. Four ≥40w sentences near the boundary
  (L44 41w, L132 41w, L216 40w, L260 41w) were checked and **lost no words**.
- **Ch.6's `and` could lose at most 5.** 53 → 49 lands at 18.95; a sixth removal would have
  given 47/2586 = 18.18, *under* the author's 18.2 lower wall. Four were taken.
- **Ch.7's `and` could lose exactly one.** 19 → 18 lands at 19.13. A second gives
  17/941 = 18.07, a breach of the lower wall. One was taken and no more.
- **Ch.10 needed adverbs only.** Its 45 `and`s were already inside the band, so none was
  touched — but adding narration words lowers the rate, so the budget was capped: 45 `and`
  stays ≥18.2 only while narration ≤2,472 words. 22 adverbs took it to 2,438 (18.46), with
  34 words of headroom still in hand. **This is the Ch.11 failure mode** (21.6 → 19.0 → 18.2
  → 17.96 across three individually-correct passes) and it was sized against, not stumbled on.
- **Ch.10's ≥40w had only 2 sentences of ceiling room** (17 of 116 = 14.66%, ceiling 16.5% =
  19 sentences). The four narration sentences in the 36–39 band were identified first; the two
  that received an adverb (L40 38→39w, L140 36→37w) **stayed under 40**, so the count held at 17.

### Register check

Of the 57 adverbs added, **46 instances use a lemma measured in the author's own Ch.1–5
narration** — `easily, entirely, exactly, actually, finally, fully, barely, simply,
deliberately, plainly, properly, carefully, slowly, clearly, certainly, completely,
considerably, genuinely, immediately, personally, strictly, usually, directly, absolutely,
really`. Of the remaining 11 instances, **8 use a lemma named in the brief's own target
palette** (`steadily, evidently, honestly, slightly, squarely`) and the last 3
(`precisely` ×1, `noticeably` ×2, `naturally` ×1 — 4 instances) are the same family as his
`unmistakably / recognizably / imperceptibly / apparently`: plain, non-manner, inferential.
All of them sit in observation or inference passages, which is where he banks them.
**Not one went into a dialogue tag.** Every tag in all three chapters is still a bare `said`.
None is a manner adverb propping up a verb that should have carried the weight.

---

## CHAPTER SIX — 25 adverbs, 4 conjunctions recast

### The 25 adverbs, in order of appearance

| # | adverb | ¶ / line | the sentence |
|---|---|---|---|
| 1 | **entirely** | L8 | "which was *entirely* true, and which was not the reason" *(also AND-fix 1)* |
| 2 | **steadily** | L10 | "a woman worked *steadily* through a bag of dried fruit" |
| 3 | **evidently** | L12 | "the duty officer who countersigned it, *evidently* without reading past the dates" |
| 4 | **honestly** | L12 | "He had *honestly* expected that to be the difficult part" |
| 5 | **precisely** | L24 | "true, in *precisely* the sense that everything Vexx had put on paper that month was true" |
| 6 | **fully** | L24 | "Vexx *fully* intended to do it." |
| 7 | **exactly** | L24 | "hear which parts came out *exactly* the same" |
| 8 | **entirely** | L26 | "then stopped thinking about it *entirely*" |
| 9 | **plainly** | L28 | "was *plainly* a converted agricultural station" |
| 10 | **barely** | L32 | "apologized twice for a wait of *barely* four minutes" |
| 11 | **genuinely** | L34 | "It was *genuinely* good coffee" |
| 12 | **properly** | L44 | "so she could see the picture *properly*" |
| 13 | **actually** | L44 | "none of them was *actually* listening to it" |
| 14 | **properly** | L48 | "Vexx had not *properly* registered how much of the man had been gone" |
| 15 | **evidently** | L48 | "The place had *evidently* taken clippers to his hair" |
| 16 | **immediately** | L64 | "opened it *immediately* when he said yes" |
| 17 | **personally** | L64 | "she would *personally* fight the first man who came here trying to change it" |
| 18 | **exactly** | L92 | "not *exactly* embarrassment about the grammar, but embarrassment about the reflex" |
| 19 | **directly** | L96 | "walking *directly* behind Paladin" |
| 20 | **simply** | L98 | "and he had *simply* let it go past him" |
| 21 | **carefully** | L126 | "trying it *carefully* in one place, then in another" |
| 22 | **fully** | L168 | "the answer was out of her, before he had *fully* got to the question" |
| 23 | **exactly** | L180 | "He knew *exactly* what that was worth, on the way out of his mouth." |
| 24 | **deliberately** | L196 | "a thing left behind — planted *deliberately*, dropped as theatre, meant to be found" |
| 25 | **slowly** | L200 | "the gardener straightened up *slowly*, put a hand in the small of his back" |

Pre-existing in narration: `properly` (L32), `faintly` (L200), `badly`/`mostly` (L216),
`kindly` (L254), `barely` (L260), `actually` (L264). Total 32.

### The 4 narration `and`s removed — and how

**None by deleting the conjunction.** §THE SEAM.

| # | line | before → after | device |
|---|---|---|---|
| 1 | L8 | "which was not the reason, **and** passed the pad back" → "…**then** passed the pad back" | sequence adverb |
| 2 | L78 | "since the second change, **and** it had not come out." → "since the second change **—** it had not come out." | em-dashed appositive *(+1 em-dash)* |
| 3 | L168 | "with everything else on the trolley — **and** carried on doing" → "— **then** carried on doing" | the existing em-dash carries it; sequence adverb |
| 4 | L180 | "He said it anyway, **and** Corwin thanked him for it, and neither man…" → "He said it anyway, Corwin thanked him for it, and neither man…" | asyndeton — the three beats now arrive as one list, which is the beat |

Fixes 2 and 4 each shed one word; both sentences are 16–21 words, so no ≥40w sentence
lost anything and the long-sentence count held at 18.

### Not touched in Ch.6 — verified intact

- **Corwin.** Every line of his dialogue is byte-identical. He is still lucid, sympathetic
  and grateful; the account he hands back ("They explained it to me. I think I had it
  backwards.") is unaltered, as is the grammar correction (*"Were."*) and the beat after it.
  The only adverb anywhere near it is `exactly` at L92, which is Vexx *reading a face* and
  hedges his reading — it does not name a feeling.
- **The *eleven hundred* motif.** 3 instances in Ch.6, unchanged, and no fourth added.
  **L36 and L132 — the two motif sentences — received no edit of any kind** and are
  byte-identical. Book-wide count unmoved (Ch.6 ×3, Ch.10 ×2 = 5, at cap).
- **Voss's scene.** Still summary narration, her dialogue still unquoted italics. Not one
  character of the coda between L230 and L258 was altered except the `exactly` at L180 and
  the two pre-existing adverbs.
- **Every number and interval.** "eleven weeks", "nine weeks", "eight weeks", "ninety
  seconds", "four minutes", "eleven days", "twenty years", "four years", "three visitors a
  month", "two years", "a second and a half" — all unaltered. Ch.7 and Ch.8 measure from
  Ch.6's interval and it has not moved.
- **The flat beats.** "His hands were flat on the table, and they were not doing anything."
  / "He might have been reading out a manifest." / "Vexx put his cup down on the table." /
  "Nobody tidies in a firefight." / "It had come off a man who went back for it and missed."
  / "Rx did not say anything." / "He signed it. He should have stopped there." — all
  untouched. So is the closing polysyndeton ("came on time and it was clean and there were
  seats on it"), which is doing the flatness and was *not* counted toward the `and` repair.
- Flat-man held at 1 (L64), simile at 9, both registers unchanged, zero straight quotes.

---

## CHAPTER SEVEN — 10 adverbs, 1 conjunction recast

⚠️ **Ch.7 is a declared PUNCH chapter.** Median 11 and 33.3% short sentences are the design.
Nothing was lengthened, joined or split, and the breath row is identical before and after.

⚠️ **No adverb went inside a document block.** The cold-open ISSUE RECORD, the KIA log, the
second issue record and the closing furniture listings are untouched — a requisition form
does not contain the word *honestly*. All ten are in plain narration paragraphs. (They would
not have counted anyway: `split_registers()` reads a wholly-italic paragraph as the
non-narrator register, which is the two-register convention working.)

| # | adverb | line | the sentence |
|---|---|---|---|
| 1 | **really** | L14 | "The table in his kitchen was not *really* a kitchen table — a folding utility trestle…" |
| 2 | **completely** | L22 | "three *completely* separate veterans' associations, none of which spoke to the others" |
| 3 | **noticeably** | L48 | "the D had worn *noticeably* shallower than the rest of it" |
| 4 | **actually** | L62 | "then would not *actually* take the one on the tag" |
| 5 | **squarely** | L78 | "Vexx put his thumb *squarely* on the serial." |
| 6 | **exactly** | L108 | "Vexx put the two of them *exactly* one under the other on the pad" |
| 7 | **entirely** | L140 | "had stopped feeling it *entirely*, like a watch he had stopped taking off" |
| 8 | **finally** | L148 | "the thing on that table had *finally* acquired a shape" |
| 9 | **deliberately** | L154 | "the four sellers on the whole index who *deliberately* photograph a table from the one angle that hides the underside of it" |
| 10 | **usually** | L154 | "You can *usually* see it coming in the photographs" |

Pre-existing in narration: `badly` (L124), `reasonably`/`mostly` (L154). Total 13.

### The 1 narration `and` removed

| line | before → after | device |
|---|---|---|
| L30 | "Vexx turned the tag over on the laminate, **and** turned it back." → "Vexx turned the tag over on the laminate, turned it back." | asyndeton |

**A second removal was arithmetically unavailable.** 17 of 941 = 18.07/1k, under the author's
18.2 lower wall. One is the whole budget and it was spent on the cleanest candidate — a flat
two-beat gesture that reads better unchained.

### Not touched in Ch.7 — verified intact

- **The dog tag, `HOLST, D.` (4 occurrences), the issue-date-read-twice beat (L110/L114 —
  byte-identical), and "Eleven months after the file closed." (L116 — byte-identical).**
  The chapter's whole point is untouched.
- **The furniture listings at the close** (L156–L160) are unaltered and still pay nothing off.
- "since the summer", "two months ago", "seven years and four months", "nineteen", "line
  forty-one of sixty", "line seven of twenty-two", "thirty-one percent", "the fourth letter
  of a surname they shared", "nine civilian archives" — every number and season unchanged.
- "The barracks roof had been concrete." / "It took nineteen." / "He cleared the field." /
  "The eggs were fine and he put them in the sink." / "He got up." — untouched. The last one
  keeps its `and`, which is doing flat work and was not a candidate.
- "There was a bicycle chained to the rail outside the apartment across the landing." —
  untouched. Pure texture, no thematic function, and that is exactly why it stays.
- Register boundaries unmoved: nothing converted in either direction, 0 straight quotes.

---

## CHAPTER TEN — 22 adverbs, ZERO conjunctions touched

**Ch.10's `and` was already correct and nothing was done to it.** 45 raw occurrences before,
45 after. The rate moved 18.63 → 18.46 purely because 22 words entered the narration
denominator, and the budget was sized so it could not cross 18.2 (the ceiling on added
narration words was 56; 22 were spent).

| # | adverb | line | the sentence |
|---|---|---|---|
| 1 | **easily** | L8 | "leaving a lip you could *easily* catch a toe on" |
| 2 | **naturally** | L8 | "He had *naturally* assumed Merrick." |
| 3 | **strictly** | L16 | "converted by somebody working *strictly* to a budget that ran to a table, four chairs, the paint" |
| 4 | **plainly** | L16 | "then cut open again later with a knife, *plainly* by somebody in a hurry" |
| 5 | **slightly** | L40 | "no question asked twice over in a *slightly* different tone" |
| 6 | **completely** | L40 | "a data chip burned *completely* past recovery" |
| 7 | **honestly** | L58 | "and there is *honestly* no strain in that at all" |
| 8 | **certainly** | L62 | "The water in the jug had *certainly* been there since before the room was booked" |
| 9 | **clearly** | L74 | "Vexx heard the change *clearly*, could not, sitting there, work out what it bought her." |
| 10 | **finally** | L76 | "and when it *finally* stopped she read back what she had put down" |
| 11 | **entirely** | L82 | "any other answer had to be built *entirely* out of nothing, on the spot" |
| 12 | **squarely** | L90 | "the first answer, the second, the third, each *squarely* under the last" |
| 13 | **noticeably** | L126 | "the sound of it was *noticeably* different, wetter" |
| 14 | **considerably** | L140 | "a man who had needed air *considerably* more than he had needed the paintwork" |
| 15 | **properly** | L166 | "without having *properly* worked out what he intended to do with the rest of the movement" |
| 16 | **simply** | L168 | "taking the power off it rather than *simply* switching it" |
| 17 | **exactly** | L172 | "the hand holding it had stayed *exactly* where it was on the page" |
| 18 | **slowly** | L220 | "Then she read it again, *slowly*, with her lips moving and her pen not going" |
| 19 | **carefully** | L226 | "she went back *carefully* through her own pad, then through the notebook" |
| 20 | **absolutely** | L248 | "looking down a corridor with *absolutely* nothing in it" |
| 21 | **exactly** | L270 | "true, useless, *exactly* the sort of remark he would have been annoyed to be handed himself" |
| 22 | **usually** | L276 | "The elevator at the north end *usually* takes its time" |

Pre-existing in narration: `simply` (L18), `exactly` (L34), `evidently` (L98), `properly`
(L140), `evidently` (L176), `comfortably` (L298), `quickly`/`correctly` (L322). Total 30.

### The two Ch.10-specific gates, checked adverb by adverb

**(a) Zero flash-forwards, zero retrospective-narrator intrusions — still zero.**
An adverb that marks narratorial hindsight is one of those, so every candidate of that class
was rejected. `immediately` was considered at L74 ("could not, sitting there, immediately
work out what it bought her") and **cut**, because *immediately* implies he worked it out
later and that is a hindsight marker. All 22 that survive are observations, perceptions or
inferences **available to Vexx in the room at that moment**:
`easily / plainly / strictly / certainly / clearly / noticeably / considerably / squarely /
slightly / completely / absolutely / exactly` are things he can see or hear;
`naturally / honestly / properly / entirely` are his own state and reasoning at the time;
`finally / slowly / carefully` are Dessen observed in real time; `usually` is habitual
present-tense knowledge, and sits in a sentence that was *already* in that tense
("The elevator at the north end takes its time"). Nothing new is known that Vexx does not know.

**(b) The Jameson gate.** **No line of Jameson's dialogue was touched, at all.** Two adverbs
land in narration near him: `simply` (L168, inside the existing machine simile describing how
his temper stopped — mechanism, not menace) and `usually` (L276, the elevator). Neither gives
him a second meaning, and neither is available to him as one. His apology (L170–L178), the
eight seconds (L164), and the paragraph where he waits and does not ask again (L298) are
byte-identical. **The temptation to put `personally` into L140** ("He had gone down to that
counter on a Thursday afternoon") **was identified and refused** — it would have pre-empted
Jameson's own reveal 60 lines later ("he drew it in person, off the counter, himself").

**(c) Dessen stays correct.** Her six adverbs (`finally, squarely, slowly, carefully,
noticeably, exactly`) all make her *more* precise and more competent. She is neither stooge
nor bully; nothing softens or sharpens her, and her finding is unaltered in both readings
(L32 and L254 are byte-identical to each other and to their previous state).

### Not touched in Ch.10 — verified intact

- **The four interval statements**, all unchanged: *since the autumn* (L134 and L224),
  *two days before he signed* (L224), *had not seen on it before* (L168 — the L168 edit is
  inside the simile clause only and ends 30 words before it).
- **The anchor** (L182, the pen writing the apology at the speed of the insult) — not one
  character altered.
- **The *eleven hundred* paragraph (L98)** — skipped entirely. It carries 2 of the motif's
  5 book-wide uses, "eight weeks earlier", and the misfiling that is the book's subject in
  miniature. It received nothing, including an adverb.
- Every number and season: "Eleven forty, room 2-14", "twenty past ten", "a fortnight",
  "re-floored in the summer", "thirty years", "fourteen days", "ninety words a minute",
  "twenty-two minutes", "Twenty years", "eight seconds", "nine points since Tuesday",
  "forty times a week", "nine years", "Four years", "at fourteen", "half a mile east",
  "Thursday afternoon" vs "Tuesday afternoon" — all unaltered.
- **The flat beats:** "He sat." / "The heating went off." / "The door opened." / "She read
  them." / "Dessen was writing." / "Nothing in the room for a second." / "Dessen wrote it
  down." / "Nothing came." / "It went on for about eight seconds." / "He went out, left the
  door standing open, and somebody had to get up to shut it. It was Vexx." / "The elevator
  came. He got into it, still talking, and the doors took the rest of the sentence." — all
  untouched.
- "in the voice of a woman filing something" (L272) is the chapter's one flat-man and was
  deliberately left alone; the count held at 1 against a ceiling of 3.
- "boxes still taped shut in the corner of the front room" (L82) and "in a briefing room two
  levels below anything with a name on the door" (L290) are the two flagged informational
  repeats and were not edited, so no new pair was created and none was broken.

---

## For the next pass

- **Ch.6 has 0.2 points of long-sentence room and 0.5 of median room.** Unchanged by this
  pass. Any future pass that adds or splits a narration sentence in Ch.6 breaks the 13.0%
  floor. Lengthen or join only.
- **Ch.6's simile is 9 at 2.048/1k against a 2.0 floor** — the thinnest margin in the three.
  Adding another ~100 words of prose to Ch.6 without adding a simile breaches it.
  Removing one simile breaches it immediately.
- **Ch.6's `and` is 49 at 18.95/1k.** Exactly one further removal is affordable (48 → 18.57);
  a second is not.
- **Ch.7's `and` is 18 at 19.13/1k and is now at its removal floor.** Not one more.
  Its em-dash is 9.83/1k with ~3 units of headroom if `and` ever needs to move again —
  but it does not.
- **Ch.10's `and` is 45 raw at 18.46/1k, with 34 narration words of headroom** before the
  author's 18.2 lower wall. ⚠️ **Any future pass that adds prose to Ch.10 must re-check this
  and add a conjunction back if it crosses.** This is the Ch.11 failure mode and the gate
  does not enforce this wall.
- **Ch.10's ≥40w has 2 sentences of ceiling room** (17 of 116, ceiling 19). The three
  narration sentences still sitting at 38–39 words (L40 now 39, L150 36, L290 39) are the
  ones to watch — a single added word in L40 or L290 costs a long-sentence slot.
- Question marks are 0.9 / 0.7 / 1.1 per 1k across the three, against the author's 1.0–3.0.
  Reported, not gated, and out of scope here — Ch.7's unpunctuated-question device is doing
  it deliberately. Worth a human eye, not a fix.
