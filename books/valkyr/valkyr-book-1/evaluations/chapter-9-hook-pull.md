# Chapter 9 — Hook & Pull Pass (0200)

Both chapter ends were treated as fixed and were not touched. The mandated opening (an
unattributed line of dialogue three words in — *"Did Paladin ever get the fourth string."*)
and the mandated closing move (Vexx involuntarily executing the method he refused, stopping
partway, then the cup upside down on the rack) are byte-identical to what came out of the
dialogue pass. The work was the chapter's single internal join, the pull, and the two
scene endings.

**Changes: 1 sentence.** Everything else was audited and left. `git diff --stat`:
**1 file changed, 2 insertions(+), 2 deletions(-)** — the prose line, plus the stale
word count in the scene-budget comment.

---

## 1. The opening and the two scene endings

| # | Position | Text as it now stands | Type | Governing verb / shape | Changed |
|---|---|---|---|---|---|
| — | **Chapter opening** | *"Did Paladin ever get the fourth string."* / *Vexx answered before he had worked out who was asking, which is what two hours in a chair will do to a man.* | IN MEDIAS RES (voice-carried) | **answered** — unattributed speech, no speaker, no room; duration supplied before setting is | no (FIXED) |
| 1 | **Scene 1 end** — the annex | *Everything in that room drives you up the wall.* / *The card taped to the terminal is wrong about paging. It's been wrong four years. Somebody laminated it.* | QUESTION PLANT | **laminated** — a comic deflection ending on a dead flat past participle; the plant is what Rx is *not* saying | no |
| 2 | **Scene 2 end** — the mess (= chapter close) | *He had got that far before he stopped.* … *Vexx put his cup upside down on the rack, the way you leave a thing for whoever comes in after you, turned the strip light off over the servery, and went up.* | DECISION POINT (inverted) | **stopped**, then **put / turned off / went up** — three ordinary transitive acts after the one act he refused to complete | no (FIXED) |

**On the scene-1 pull.** Rx's two blocks are the only thing between the offer and the white
space, and they are doing more than they look. Vexx opens with *"You've been quiet since I
sat down."* Rx answers *"Fine"* — the one denial in his budget — and then talks for two
sentences about a man's handwriting and a laminated card. He was in the room for all of it:
the office at Kell, the eleven people, *"Less, if he has children,"* the refusal. He says
nothing about any of it, and nobody makes him. The pull across the break is not information;
it is the second person in the room having heard the same offer and choosing furniture
instead. That is a question plant of exactly the register the outline wants, and it is
unimprovable from where I sit, because every word of it is dialogue.

---

## 2. The one change

**Line 44 — the narratorial flash-forward. Cut.**

Before:
> At two in the morning, in a cold room, with a screen open in front of him, answering them
> cost nothing at all — and he did not work out until a great deal later what the order of
> them had been for.

After:
> At two in the morning, in a cold room, with a screen open in front of him, answering them
> cost nothing at all.

Twenty-five words removed, nothing added. Four faults, one cut:

1. **It is the plot hook.** The brief's own description of the thing to look for —
   *a hinted consequence, a "he would think about that later", a foreshadow* — is this
   clause almost verbatim. It converts the chapter's moral pull (a method exists and Vexx
   cannot un-know it) into an informational one (the questions had a hidden order, and you
   will be told what it was). Nothing else in the chapter promises the reader a return.
   It was the only one.
2. **It steps outside the chapter's now, which is the POV fault this book has already
   paid for.** *"He did not work out until a great deal later"* is the narrator standing
   downstream of Vexx and reporting back — the same figure as Ch.5's cut close
   (*"He was wrong. He simply didn't know it yet."*) and a cousin of Ch.2's dramatic irony,
   which is permanently spent. It survived here because it is mid-chapter rather than at an
   ending, which is exactly why it needed finding.
3. **It makes Zeus sinister**, against the outline's first writer warning. Four ordinary
   questions — a col, an acoustics story, who won an argument, whether a man ever owned a
   dog — become a sequence with a concealed purpose the moment the narrator says they had
   an order. Zeus running a technique on Vexx is true and is the subtext; the narrator
   *confirming* it turns the most considerate character in the chapter into an operator with
   a plan. The scene already carries it without help: he has been there for two hours, he
   has not asked anything, and he has not left.
4. **It pre-empts the shareable moment.** *The interrogator who never asks why* only works
   if the reader notices the absence themselves. A line that says *these questions were
   for something* does the noticing for them, on the page, six lines before Zeus
   demonstrates it.

**Considered and rejected: keeping the observation without the flash-forward.** Two variants
were tested — *"…cost nothing at all, which was the whole of what they were for"* and
*"…cost nothing at all. Not one of them was a question about the terminal."* The first is
the same narrator being knowing in a shorter coat. The second is a new idea, which this pass
is not allowed to add. The bare cut is the only version that removes the promise without
replacing it with a different one.

**Metric handling.** The cut takes one sentence out of the `>=40w` bucket (15 → 14 of 96)
and removes one em-dash and one *and*. Measured immediately after the edit, not at the end:
every figure still clears, and the narration median is untouched at 14.5 because the
shortened sentence (23w) never crossed it. Full table in §6.

---

## 3. The single scene break, and the slow-reading design

Ch.8 had eight internal joins across 5,717 words. Ch.9 has **one**, and the outline forbids
a transition scene through it. What actually carries the reader across the white space is
not momentum — the chapter has deliberately spent its momentum by then — it is three
continuities, all of them physical:

- **The cup.** It is the chapter's through-object and it crosses the break in the reader's
  hand. Zeus's cup with a skin over it (*"a cup he was not going to drink"*) → Aglaope with
  *"a pad and no cup"* → the inch left in the urn → *he turned his cup on the table* →
  *taking both cups* → **the cup upside down on the rack**, which is the last image in the
  chapter. The break lands in the middle of that chain, not across a gap in it.
- **The hour.** Scene 1 is timestamped four separate ways (*ten past one*, *two in the
  morning*, *a hundred and four minutes*, the badge log). Aglaope's second line
  (*"It's been off since one"*) and her *"since half past two"* pick the clock straight back
  up, and the close names *four in the morning*. The reader never has to work out how long
  the white space was.
- **The direction of travel.** *"He was still sitting when Vexx went out"* → *"You came up
  from the annex."* Four flat words, second line of the new scene, and the join is closed by
  a character rather than by the narrator. This is the correct move for a chapter that is
  not allowed a transition scene.

**Reading speed: deceleration audited, and left alone everywhere.** The slow beats were
checked one by one for whether they are designed or slack:

| Beat | Verdict |
|---|---|
| The annex paragraph (line 16) arriving *after* five lines of unplaced dialogue | Designed — the setting is withheld, then supplied cold, and it carries institutional neglect (*costed twice and run neither time*; a laminated card *for the benefit of nobody*) rather than scenery. Left. |
| The heater, twice, in two different rooms (lines 56, 238) plus *"Nothing after that but the heater and the pen"* | Designed rhyme, not drift — the same silence-marker in both two-handers is what makes them one night in one building. The second does more than the first: it *measures* the silence, and it is the beat that buries Aglaope's line about Rx. Left. |
| The lights going out on their timer and neither man moving (line 92) | Designed — the only stage business between the offer and the refusal. Left. |
| Seven beats of cooling after the moral peak (the cup half-turn, *"I'd have been sorry"*, row four, Sedge, the thank-you, the badge log, the departure) | Designed, and it is the chapter's argument: the offer is made and then two men go on being decent to each other. Compressing any of it would be the pass "fixing the quiet." Left. |
| *"The moment went past the both of them and out the other side"* (line 100) | The one line I would question on craft grounds — it is a third statement of a fact already carried by *"he left it where it was"* and *"Zeus went on turning the cup."* **Declined:** it is not a transition, not a pull, not a POV breach and not a plot hook, so it is outside this pass's remit, and the outline mandates the beat. Flagged for the disruptor, not actioned. |

**No pace was injected anywhere.** The one edit *removes* a forward-leaning clause; it does
not add a forward-leaning anything.

---

## 4. Required confirmations

**No line converts the moral pull into a plot hook. CONFIRMED after the cut.** The whole
chapter was scanned for narratorial promises (`later`, `afterward`, `by the time`,
`did not know`, `would come to`). Four hits before the edit; one was the clause now cut, and
the other three are all inside dialogue and all inside the speaker's present:

- Zeus, line 62: *"He's the only kind who doesn't report the conversation afterward."*
  Method, not promise.
- Zeus, line 66: *"a shut door frightens a man into remembering the day afterward."*
  Method, not promise.
- Zeus, line 138: *"I'd rather have said it than found out later that I hadn't."*
  A man explaining why he spoke, in the past-conditional. Not a foreshadow.

Two further candidates were examined and cleared as in-scene motive rather than narratorial
plant: *"He wrote the sort out on the back of his hand with the stylus, in case it was worth
something in the morning"* (Vexx's intention, and it goes nowhere in this chapter), and
Zeus's badge-log warning, *"That goes up on Monday with the water and the lights"* — which
does open toward Ch.10, but is mandated by the outline's own progressive structure, is
spoken by a character, and sits 55 lines from the last page rather than on it. **The last
page of the chapter contains no promise of any kind:** the closing paragraph reasons out a
method and then stops, and nothing tells the reader what it is for.

**Both scene endings sit inside Vexx's perception. CONFIRMED.**

- **Scene 1** ends on the interface channel. Rx's lines are heard by Vexx, in Vexx's head,
  in the register the two-register convention reserves for exactly that. No breach possible.
  The one thing examined: Rx claiming two hours of observation of a man Vexx spent the night
  facing away from. Cleared — Vexx walks the length of the room past him, reads the grid at
  close range twice (*"That's ink."*, *"You've got the same man in two places"*), and
  *"driving me up the wall for two hours"* is a complaint about persistence, not a claim of
  continuous line of sight. It is also dialogue and out of this pass's reach.
- **Scene 2** ends on Vexx's own reasoning and Vexx's own hands. Nothing in the last
  paragraph is perceived by anyone else.
- **Examined and cleared: line 140**, the last narration of the annex —
  *"He was still sitting when Vexx went out — four bays lit, five dark, a cup he was not
  going to drink, a puzzle he could not finish and would not start again."* Two of the four
  items are statements about Zeus's future, which is why it was tested. It holds: the whole
  sentence is anchored to the instant of *"when Vexx went out,"* the bay count is what a man
  sees from a door, and both predictions are licensed by Zeus's own on-page words
  (*"If I start it again I lose Tuesday and Wednesday"*; the cup has had a skin on it since
  before Vexx arrived and was never drunk). It is Vexx's read of a man he has just spent two
  hours with, not the camera staying behind after he leaves. **Recorded here so the next
  pass does not rediscover it as new.**

**The shareable moment is landing, in three places, and is not buried.** *The interrogator
who never asks why* is carried by:

1. **Line 18, plainly** — *"Zeus had not asked what he was doing — had not asked anything at
   all — and had not left."* Paragraph-final, 19 words, no gloss. This is the sentence a
   reader quotes.
2. **Lines 32–50, by demonstration** — seven questions on seven subjects, none of them a
   why, and then Zeus tells Vexx what Vexx is doing without ever having been told.
3. **Lines 124–126, crystallized** — *"Why."* / *"Ask a different question."* The one *why*
   in the chapter is Vexx's, and Zeus refuses it about his own life. That is the technique
   turned inward, and it is the last exchange before Vexx stands up.

The cut at line 44 **strengthens** this rather than weakening it: it removes the only line
that told the reader in advance that the questions were a technique. The moment now belongs
to the reader who notices, which is the only way a moment about an absence can work.

---

## 5. Considered and declined

- **Sharpening lines 8–16 after the fixed opening** (permitted by the brief). Declined.
  *"which is what two hours in a chair will do to a man"* is the aphoristic register the
  book opens every chapter in, and it does the one job the withheld setting cannot: it puts
  a duration under the reader before it puts a room. Every trim tested lost the duration.
- **Reordering or trimming the annex establishing paragraph** so the reader reaches Zeus
  faster. Declined — this is the exact shape of "fixing the quiet," and the paragraph is not
  scenery: it is the costed-twice ducting and the laminated card, i.e. the institution
  neglecting things, which is what the chapter is about.
- **Two room-inventory sentences either side of the break** (line 140's *four bays lit, five
  dark, a cup…* and line 152's *the urn off and one strip light… a pad and no cup*).
  A genuine syntactic near-rhyme, and the *cup / no cup* pairing was tested as accidental.
  Judged designed and load-bearing: the cup chain is the chapter's only physical continuity
  across the break, and five italic lines sit between the two sentences on the page. Left.
- **Giving scene 1 a harder last beat than a laminated card.** Declined twice over: the lines
  are dialogue, and the deflation *is* the pull. A compressed ending here would be the
  chapter announcing that something significant just happened, which is the one thing the
  outline forbids (*theme stated nowhere*).
- **Pull sequencing.** Ch.7 and Ch.8 both closed on a document; Ch.9's last page carries no
  paper, and the ninth closing shape is unrepeated. Ch.8's internal endings ran heavily to
  QUESTION PLANT; Ch.9's two are QUESTION PLANT then DECISION POINT, so the chapter does not
  close on the type it opens its second half with. No three-in-a-row anywhere. No action.

---

## 6. Gates — after the pass

All three clean, whole manuscript. Chapters 1–8 untouched and byte-identical.

| metric | limit | before | after |
|---|---|---|---|
| words | — | 3,416 | **3,397** |
| `and` /1k | ceiling 24.0 | 22.0 | **21.8** |
| em-dash /1k | 8.5 – 12.0 | 10.0 | **9.7** |
| comparison /1k | **floor 2.0** | 2.6 | **2.6** |
| comma /1k | floor 58.0 | 61.8 | **62.1** |
| adverb /1k | ceiling 20 | 2.9 | **2.9** |
| narration sentences | — | 96 | **96** |
| narration median | floor 13 | 14.5 | **14.5** |
| narration `>=40w` | floor 11.5% | 15.6% | **14.6%** |
| narration `<=6w` | ceiling 33% | 21.9% | **21.9%** |
| dialogue lines | — | 161 | **161** |
| semicolons | 0 | 0 | **0** |
| straight quotes / apostrophes | 0 | 0 | **0** |
| British spellings (incl. `-ise`/`-isation`) | 0 | 0 | **0** |

`style_check.py` **clean** · `grammar_check.py` **clean** (0 errors, 3 long-sentence notes,
the same three as before) · `voice_wear_check.py` **clean — no retired phrases, no device
over cap**.

No comparison was touched: the chapter carries 9 of them against a floor of 2.0/1k, which is
8 at this word count, so the margin is a single sentence. Any future pass cutting narration
here must count comparisons first.

---

## 7. For the orchestrator

1. **The flash-forward is a repeat offence, not a one-off.** Ch.2's dramatic irony, Ch.5's
   cut close, and now Ch.9 line 44 — three chapters where the narrator stepped downstream of
   Vexx and reported back. Twice it was caught at a chapter ending; this time it had moved to
   the middle, where the closer inventory does not look. **Recommend the check be phrased as
   "no narration anywhere may know something Vexx does not yet know," not "no chapter may end
   outside Vexx."** That is a root-level `book-writer.md` / `hook-craft` edit under the
   UPDATE RULE, not a per-book note.
2. **Line 100, *"The moment went past the both of them and out the other side,"*** is the
   chapter's one gloss-on-a-beat-already-rendered. Outside this pass's remit. Give it to the
   disruptor.
3. **Ch.9's inventory entries stand unchanged.** Opening move: *a line of dialogue with no
   attribution and no setting, three words in*. Closing move: *the POV character
   involuntarily begins executing the method he refused, stops partway, and does something
   ordinary and courteous on top of it*. Ch.10 still needs the tenth distinct shape, and it
   may not be a document.
