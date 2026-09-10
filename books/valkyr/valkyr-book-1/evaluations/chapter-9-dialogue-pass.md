# Dialogue Pass — Chapter 9: 0200

Scope: dialogue only. Ten edits, all inside speech (nine inside quoted/italic dialogue, one
inside a summary-register report of Zeus's questions — flagged as Z01 and justified there).
No narration paragraph was rewritten: narration sentence count (96), median (14.5), `>=40w`
(15.6%) and `<=6w` (21.9%) are **byte-identical before and after**. No idea, beat, plot point
or outcome changed. The mandated first line (*"Did Paladin ever get the fourth string."*) and
the mandated last (the cup upside down on the rack) were not touched.

`git diff --stat`: **1 file changed, 10 insertions(+), 10 deletions(-)**.

---

## 1. COVER-THE-NAME TEST

**Method.** Every quoted turn and every italic interface turn was stripped of tag, beat,
paragraph and turn-order and read cold **against the whole twenty-voice cast**, not against
the four in this chapter. A turn scores **DISTINCT** if it lands on exactly one character on
first read; **WEAK** if it lands only once turn-taking is restored; **INDISTINCT** if it lands
on nobody, or on the *wrong* character because it is wearing somebody else's device.

**Units.** 112 attributable turns (107 quoted segments + 5 italic interface segments),
carrying **178 spoken sentences**. `style_check.py` counts the same material as **161 dialogue
lines** — its splitter joins tag-split speeches; the numbers below are per-turn, which is the
only unit the test can actually be run in.

| | DISTINCT | WEAK | INDISTINCT | Strict | Tolerant |
|---|---|---|---|---|---|
| **Before** | 62 | 46 | **4** | **55.4 %** | 96.4 % |
| **After** | 66 | 45 | **1** | **58.9 %** | **99.1 %** |

Per character, after the pass:

| Character | Turns | Sentences | Distinct | Weak | Indistinct |
|---|---|---|---|---|---|
| Zeus | 43 | 81 | 28 | 15 | 0 |
| Vexx | 36 | 45 | 15 | 20 | 1 |
| Aglaope | 30 | 45 | 20 | 10 | 0 |
| Rx | 3 | 7 | 3 | 0 | 0 |

**Read the strict rate against the chapter's form, not against Ch.8's 72.5 %.** Ch.9 is two
two-handers. In a two-hander, alternation alone assigns every turn, so the chapter is *written*
to afford one-word turns — *"Hallam." / "I did." / "Of course." / "There." / "A full stop."*
Thirty-one of the 45 remaining WEAK turns are four words or shorter. Lengthening them to make
them identifiable in isolation would be writing to the metric and would wreck the one thing
the chapter is for. They are not defects and were left.

**The one remaining INDISTINCT.** Vexx's *"I know."* (line 136), which cold-reads exactly as
Zeus's *"I know."* ninety lines earlier. **Left deliberately** — it exists so Zeus can answer
*"I know you know. I'd rather have said it than found out later that I hadn't,"* which is the
most considerate line in the chapter and the seed of the Ch.10 badge log. Fixing the collision
destroys the reply. Flagged, not fixed.

---

## 2. EVERY LINE CHANGED (10 edits)

### Device-bleed removals

**Z01 — ZEUS.** *A why-question wearing different clothes.* (line 44, summary register)
> …whether Gaia had ever said where she learned the acoustics thing, **what the argument about the coffee bracket had actually been about**, whether Vexx had ever in his life owned a dog.
> → …whether Gaia had ever said where she learned the acoustics thing, **who had won the argument about the coffee bracket**, whether Vexx had ever in his life owned a dog.

The word *why* appears once in Ch.9 and it is Vexx's. This was the semantic one. *"What the
argument had **actually** been about"* asks for the real reason behind a stated reason — that
is *why*, and *"actually"* is the tell. It also broke its own frame: the sentence that carries
it promises four questions *"none of them needing more than a word back,"* and this one cannot
be answered in a word. *"Who had won"* answers in a name, is a person-question rather than a
reason-question (his axis), and is cheaper still, which strengthens the run.

**This is the one edit inside narration.** It is reported speech — the content of Zeus's
questions, carried in this book's summary register per the two-register convention — and it is
the chapter's single most load-bearing constraint. Sentence count unchanged, sentence still
`>=40w`, all narration metrics identical after.

**Z02 — ZEUS.** *Spector's N-of-the-M construction, spoken aloud.* (line 62)
> "Eleven people. Two of them sign retention exceptions, **which means two of them can** pull a whole record, print it, walk out of the building with it inside a coat—"
> → "Eleven people. Two of them sign retention exceptions, **which means they can** pull a whole record, print it, walk out of the building with it inside a coat—"

The bible narrows the counting rule to: *a spoken count belongs to Spector; a silent tally is
Vexx's and Rx's.* The bleed here is not the numbers — it is the **restatement**, M then N-of-M
then N-of-M again, which is the drumbeat of *four drums, four seals, four intact*, and which is
the exact shape the Ch.6–8 audit caught on Gaia. Cold-read, *"Eleven people. Two of them sign
retention exceptions, which means two of them can…"* assigns to Spector. Killing the second
*two of them* leaves the office facts fully intact — eleven people, two signatories, both of
them already dirty — and removes the performance. This was the chapter's only INDISTINCT
outside Aglaope, and it is now DISTINCT.

*Note the writer already caught the same construction in the closing Kell paragraph
(*"four of the five things a man would need"* → *"most of what a man would need"*) and missed
this one, which is the louder of the two because it is spoken.*

**A01 — AGLAOPE.** *Zeus's registered "That's not X. That's Y," in her mouth, for the second
time in the book.* (line 224)
> "You're carrying it in from somewhere else tonight. **It's not Merrick. Merrick's in you, but it isn't Merrick.**"
> → "You're carrying it in from somewhere else tonight. **Merrick's in you. He isn't this.**"

`character-bible.md` logs this device as **ZEUS's**, logs that it had already spread to
Aglaope once, and logs that the Ch.8 pass removed it from her. It came straight back. The
first sentence is her device untouched (naming what she noticed, unasked). The rewrite keeps
the negation and **removes the substitution** — Zeus negates and then supplies the correct
term; Aglaope negates and leaves the real thing unnamed, which is her evasion axis and which
keeps the subtext under. It also drops *Merrick* from three occurrences to two: three
repetitions of a name in one line, in a chapter following the chapter whose owner-of-record
device is involuntary self-echo, was its own small hazard. Shorter is her card
(*"fewer words than anyone else in the cell"*).

**A02 — AGLAOPE.** *The tail of Zeus's Ch.4 line, verbatim in shape.* (line 240)
> "He's been holding his hand wrong on purpose for a fortnight, **to fix a thing that isn't his fault.**"
> → "He's been holding his hand wrong on purpose for a fortnight, **to fix something the peg's doing.**"

Ch.4, line 47, **Zeus**: *"That's a man looking for someone to blame for something that isn't
their fault."* That clause is the tail of his bible sample line, and this is her exit line —
the last thing she says in the chapter. Cross-chapter shared reach, and on the strongest
possible position. The replacement is concrete and mechanical (her band: plain, small, no
abstraction), the self-blame is already carried by *"He thinks it's him,"* and it makes her
instruction actionable, which is why she is giving it to Vexx at all. Bonus: it closes the
chapter's frame on the peg, which is where the unattributed first line opened it.

**V03 — VEXX.** *The chapter's last N-of-the-M.* (line 198)
> "…a full stop — so you're not **reading two hundred entries to find four**."
> → "…a full stop — so you're not **reading the list end to end to find four**."

Same rule as Z02. Vexx's manifest reflex is legitimately his and the outline requires it to
escalate, but *"two hundred entries to find four"* is a ratio performed aloud and it was the
one phrase in his scene-two run that cold-reads off him. *"End to end"* is procedure, which is
his axis, and the meaning is identical.

### Voice-consistency repairs

**Z04 / Z05 — ZEUS.** *A dialect marker he does not carry.* (lines 14, 58)
> "**He'll not** offer, though." → "**He won't** offer, though."
> "**You'll not** get the rest of it that way." → "**You won't** get the rest of it that way."

`X'll not` occurs **twice in the manuscript and both are Zeus in Ch.9**. Across his lines in
Ch.4 and Ch.8 he uses standard contractions throughout (*didn't*, *I'm not going to*, *It will
not survive*). His band is *"ONI intelligence, clinical, unhurried"* — a Northern contraction
is off-card, and on a whole-book cold read it points **away** from him rather than toward him.
Two instances is also already at the skill's dialect ceiling for a marker that earns nothing.

**Z03 — ZEUS.** *Numeric self-echo.* (line 72)
> "He'll be at that same desk **in eleven years**, perfectly all right."
> → "He'll be at that same desk **for the rest of his service**, perfectly all right."

*Eleven people* nine lines earlier, from the same mouth, in the same speech-block; and
Aglaope's *"I've been doing it for eleven years"* is the load-bearing eleven in this chapter
and should own it alone. Institutional register, same meaning (nothing ever happens to him),
and it takes one more number out of a speaker who is carrying nineteen of them.

**V01 — VEXX.** *Continuity, and a device-adjacent prompt.* (line 142)
> *You've been quiet since **he** sat down.* → *You've been quiet since **I** sat down.*

Two problems, one fix. (a) **Continuity:** Zeus never sits down on the page — *"He had been
there when Vexx came in at ten past one."* The only man who sits down in that room is Vexx.
(b) **Device adjacency:** as a third-person condition-observation it read toward Bastion's
body-check-before-content, which is the shape a prompt-for-a-denial naturally falls into.
Timed off his own arrival it becomes Vexx's log-entry habit, and it is better craft: Vexx
times it to himself, and **Rx's answer is the thing that reveals it was about Zeus.**

**V02 — VEXX.** *US spelling.* (line 182)
> "**Alphabetise** it," → "**Alphabetize** it,"

`DIALECT = "us"` and the author's five chapters carry 82 US forms and zero British. The gate
did not catch it because `alphabetise` is not in `style_check.py`'s `_UK_US` map — the map is
deliberately short. **Recommendation (not actioned — one-file constraint):** add
`alphabetise/alphabetised/alphabetisation` to the map in `books/_template/tools/style_check.py`
so every book inherits it, per the root UPDATE RULE.

---

## 3. DEVICE-BLEED AUDIT — every speaker against every reserved device

Four speakers × the full one-device map, including the routes expected to be clean. `—` = the
device does not appear in the chapter at all. **HIT** = fixed above.

| Reserved device (owner) | ZEUS | VEXX | AGLAOPE | RX |
|---|---|---|---|---|
| Counting **aloud** / sequence / N-of-M (**Spector**) | **HIT → Z02**; residual examined below | **HIT → V03**; rest cleared below | examined, cleared below | — |
| The private, silent tally (**Vexx/Rx**) | — | none spoken — canon-clean | — | — |
| Compulsive narration, never letting a silence stand (**Echo**) | clean — the chapter's silences stand (*"Nothing after that but the heater and the pen"*) | clean | clean | examined: his two blocks arrive **after** two hours of silence, i.e. the inverse of Echo's compulsion. Clean |
| Naming/labelling, then using the name as agreed (**Echo**) | — | — | — | — |
| Too-quick denial / reflex deflection (**Rx**) | examined: *"All right."* ×2 is acceptance, and it is **slow**. Clean | clean — Vexx never says *Fine* | clean | **his own**, once ✓ |
| Body-check question before content (**Bastion**) | clean — he never once asks after Vexx's condition | **near-miss → V01**; now timed, not diagnostic | clean — she reads *weight*, not bodies | — |
| Restate-then-disagree; *"No."* as a sentence (**Paladin**) | clean | examined: three bare *"No."* — Paladin's device is the **restatement** before the refusal, and Vexx restates nothing; the outline mandates *"Vexx refuses. Clean. Immediate."* Cleared | examined: *"That's an argument for me checking"* is a riposte inside his frame, not a restatement of his position. Cleared, see §5 | — |
| Correcting the terms of a question (**Vexx**, capped 5) | examined: *"Hallam's the day shift…"* corrects a **fact**, and the two-beat corrective form is Zeus's own registered device. Cleared | **his own** — 2 clear deployments (*"It's an open index"*, *"Chronological."*), **0 capped phrasings spent**, book total stays 2/5 | — | — |
| Pre-empt the objection and improve it (**Jameson**) | examined: *"That's not caution. That's a man rationing himself"* names what Vexx is **doing**, not what he is thinking. That is precisely the documented Zeus/Jameson split. Cleared | — | — | — |
| Reframing / *"That's not X. That's Y"* (**Zeus**) | **his own**, twice (*caution/rationing*, *water/grounds*). At the ceiling — see §5 | clean — no negation-plus-substitution anywhere | **HIT → A01**, and **HIT → A02** | — |
| Withhold until useful / answer late (**Hollow**) | examined: *"Ask a different question"* is a refusal, not a deferral. Clean | — | — | — |
| Fact-then-silence, no modals (**Voss**) | clean — modals throughout | clean | near-neighbour by construction, but she supplies *reasons* (Voss never does). Clean | — |
| Same question three times, one word changed (**Dessen**) | clean — **seven questions, seven different subjects, zero repeats**, verified line by line | clean | clean | — |
| Involuntary self-echo (**Merrick**) | nearest approach in the chapter: *"It's the water"* → *"It's been the water since August."* A **return to a topic** across an interruption, not an immediate echo of his own last words, and it is doing character work. Cleared, watched | clean | see §5 — her scene is built on echoing **him**, not herself | *"wrong about paging… wrong four years"* — one word, cleared |
| Naming what she noticed, unasked (**Aglaope**) | **closest live pair in the chapter** — see §6 | clean | **her own** ✓ | — |
| Fact → ask → clock; *"your call"* (**Gaia**) | **clean, and it is what keeps him non-sinister**: he never puts a clock on the offer, never says *think about it*, never leaves a door open | clean | clean — the predicted Gaia/Aglaope collision did not happen | — |
| Trade vocabulary for ethics (**Goliath**) | one marginal: *"a man rationing himself."* Quartermaster-adjacent, but it is about self-restraint rather than craft-honesty, and it is also plain ONI. Cleared, logged | clean — his register is clerical/data (*field*, *sub-sort*, *manifest*), not trade | clean | — |
| The pause before agreement (**Requiem**) | — | — | examined: *"That's what I'll do"* is **immediate**, and the narration says so. Clean | — |
| The singing image (**Requiem**) | — | — | — | — |
| Grammar correction (**Corwin**) | *"Hallam's the day shift"* is fact, not grammar. Clean | *"Chronological."* is **vocabulary**, which is his; Corwin's is **grammar**. Cleared, near-neighbour logged | *"That's what in order means"* is semantic rebuke, not correctness-for-its-own-sake. Cleared | — |
| Self-interrupting over-explanation (**Reyes**) | clean — he never breaks off | the one broken-off line (*"or it'll take you—"*) is **interrupted by Aglaope**, not self-interrupted. Cleared | — | — |
| Interviewing the people assessing him (**Ives**) | examined — he asks a run of questions but is not under assessment. Clean | — | — | — |
| Standing whenever anyone enters (**Beck**) | clean — and note the inverse is on the page: he does not stand, and does not get up when the lights go out | — | she stands **to leave**, carrying cups. Clean | — |
| **The why-question** (**nobody; Zeus never**) | **HIT → Z01.** Now clean — see §4 | asks *"Why."* once, legally; he is not Zeus, and Zeus's refusal to answer it is the point | *"What happens to him if…"* — what, not why. Clean | clean |

### Residuals examined and cleared, with reasoning

- **Zeus's *"Seven interviews… it used all seven… Same seven interviews."*** Three repetitions
  of one number. Examined hard as Spector's shape and cleared: Spector's count is *competence
  performed for a room*; this is **rhetorical repetition of a grievance**, the number is the
  wound, and it terminates in *"I read it four times to see whether there were two
  documents,"* which is not a count but a man checking his own sanity. It is also the only
  place Zeus's own life is on the page.
- **Aglaope's *"Two hundred and nine. I thought it was two hundred and eleven."*** A spoken
  number, and the narrowed rule says spoken counts are Spector's. Cleared: it is a single
  cardinality, it is **reported as an error**, it is her chaos marker, and it is the outline's
  mandated beat. Spector's device is a sequence that goes right, performed; hers is a count
  that went wrong, admitted at four in the morning. They are not the same device.
- **Vexx's scene-two numbers** (*two hundred and nine entries*, *Four hundred*, *second column,
  then again at the bottom*, *sub-sort by year*). Cleared after V03: what remains is
  database-design register, which is his band, and the escalation is the outline's
  *"correction reflex"* chaos marker running past the point where he should have stopped.
- **Vexx adopting Zeus's phrase** — *"How long does it take. Finding out what a man's
  protecting."* Cleared and **protected**: it is Vexx quoting Zeus, once, and it is the
  chapter's thesis arriving in the wrong mouth. The closing paragraph does the same thing
  silently. That is the trap closing, not a device changing hands.

---

## 4. CONFIRMATIONS REQUIRED BY THE BRIEF

**Zeus never asks why. CONFIRMED.** `why` occurs exactly once in Chapter 9 (line 124) and it
is **Vexx's**. Every one of Zeus's seven questions was re-read as a possible why in different
clothes: *the cook's name* (who), *what did you tell the station commander about the bund*
(what-was-said), *did he do it* (yes/no), *col or ridge* (which), *where Gaia learned the
acoustics thing* (where, and about a third party), *who won the coffee-bracket argument* (who
— **was** a why, fixed at Z01), *whether Vexx ever owned a dog* (yes/no). Nothing remains. He
also never asks Vexx what he is looking for, or what the record is, or what he intends to do
with it — the three obvious questions the scene invites, all absent, which is what makes the
technique visible on a second read.

**Zeus is never sinister. CONFIRMED, and audited on four separate failure modes.**
*Menace:* nothing conditional-threatening; the only warning he gives is the badge log, framed
as housekeeping (*"That goes up on Monday with the water and the lights"*) and immediately
followed by *"I'd rather have said it than found out later that I hadn't."*
*Relish:* the offer contains no intensifier and no evaluative adjective; the worst sentence in
the chapter, *"Less, if he has children,"* is four words and carries no adverb.
*Salesmanship:* audited against Gaia's fact→ask→clock, which is the register a pitch lives in
— **he never puts a clock on it, never asks for a decision, never restates after the refusal,
and never leaves a door open.** He is the only character in the chapter who wants nothing.
*Instruction as superiority:* the two *"that's the part people get wrong"* framings were
examined; they are craft-correction aimed at an imagined third party, not at Vexx.
Z03 additionally removes one of his numbers, which lowers the clinical-inventory tone of the
one speech that could tip.

**Nobody reacts to Aglaope's line about Rx. CONFIRMED.** Lines 236–242: she says it; the next
paragraph is the heater under the servery coming on and stopping; her next words are *"Tell
Paladin about the peg."* No character responds, no narration flags it, no interiority
registers it, and the line is never referred to again in the chapter. She exits on a guitar
peg. Untouched by this pass except for the peg line's tail (A02), which is **after** the drop
and only makes the exit more ordinary.

**Rx's *"Fine."* is clean, single, and unremarked. CONFIRMED — with a cap warning.** One
occurrence, no second denial anywhere, no character notices, and the only narration attached is
*"Then, at his ordinary speed"* — which is the minimum signal that makes the speed legible and
which uses none of the at-risk *"too quick"* wording. Untouched.

> ⚠️ **The literal phrase is now AT CAP, and the writer report has the count wrong.** It logs
> Ch.9's as *"the 3rd literal use."* Actual manuscript count of Rx's literal *Fine / I'm fine*:
> Ch.1 ×1, Ch.3 ×3 (lines 13 and 93), Ch.9 ×1 = **5 of 5**. Ch.13's break therefore has **no
> literal use left in the budget**. Either the cap is raised by the author for the break
> specifically — which is defensible, since the break is the whole reason the cap exists — or
> Ch.13 must break the *behaviour* without the words. **This needs an author decision before
> Ch.13 is dispatched.** (Separately: Ch.8 line 118 gives **Gaia** *"Fine. Kettle."* — a
> concession, not a denial, so it does not spend Rx's cap, but it is the phrase in another
> mouth and is logged here.)

**Vexx's correction reflex bounces off Zeus. CONFIRMED, and it reads as Vexx's.** *"It's an
open index — auditors use it."* Zeus does not argue and does not counter-correct; he says
*"All right"* — which the narration calls *"the flattest three syllables in the room"* — and
then **adopts Vexx's own word and finishes the sentence with it**: *"Then you're reading an
open index at two in the morning with the door shut."* That is Zeus's registered reframe
(editing the premise) operating on Vexx's registered correction (editing the word), which is
exactly the split the differentiation matrix draws between them. The device is Vexx's, it
fires, it fails, and **neither of the two capped phrasings is spent** — the book-wide count
stays at 2 of 5.

**Counting, under the narrowed rule.** After Z02 and V03 there is **no N-of-M construction
spoken aloud by anyone in the chapter**, and no silent tally is ever said out loud.

---

## 5. STRUCTURES EXAMINED AND DELIBERATELY LEFT

These are not defects today. They are the things that become defects if they recur.

1. **Aglaope's echo-figure — five instances in one scene.** *"That's an argument for
   alphabetical." / "It's an argument for me checking."* · *"Four hundred."* · *"A full
   stop."* · *"Without reading them properly."* · *"That's what in order means."* She refuses
   Vexx's optimisation almost entirely by holding his own words up to the light. **Kept:** it
   is a rule-of-three comic escalation that terminates on *"There,"* it is *listening* rather
   than a speech habit, it is scene-local, and it is the mechanism by which the funny thing
   becomes the unbearable thing — which is the outline's stated requirement for beat 6.
   **But she is not a tic-bearer and the roster is full at three.** If the figure appears again
   when her list returns in **Ch.16 or Ch.23**, it stops being a scene structure and becomes an
   unlicensed fourth device. Flag it in those dispatches.
2. **Zeus's *"That's not X. That's Y"* twice in one chapter** (*caution/rationing*,
   *water/grounds*). It is his own device, so not bleed, and the pairing is deliberate — the
   coffee gets the same grammar as the atrocity, which is the chapter's whole argument about
   his voice. **Two is the ceiling.** A third in one chapter would calcify it.
3. **Zeus's *"All right."* ×2.** Cannot be changed: the narration measures the first one
   (*"the flattest three syllables in the room"*). The second, alone, after *"Don't,"* is the
   moment he stops, and it lands because the first one did not stop him. Book total 4.
4. **Vexx's three bare *"No."***. Two are the mandated refusal, one is an answer to Aglaope.
   Paladin's device is the restatement, not the word; cleared. Watch the density if a later
   chapter puts Vexx and Paladin in the same refusal.
5. **Aglaope's Curran speech — the chapter's thinnest veil.** *"If he's on it, then what I do
   is sit with people. And if he isn't, then what I do is something else."* This is the closest
   any line comes to surfacing the real conversation. **Kept**, because (a) it is the outline's
   beat, (b) she says it entirely as a **clerical question about a row on a list**, which is
   displacement rather than statement, and (c) *"something else"* is never named — she supplies
   the terms of the fear and refuses the word for it. Remove it and the scene has no reason to
   exist. It is, however, the line an evaluator will reach for.

---

## 6. PAIRS I STILL JUDGE TOO CLOSE

**Zeus and Aglaope — the unasked observation of Vexx's movement.** This is the real one, and
it is not on anyone's watch-list.

> **Zeus:** *"You came down here with a notebook you haven't opened, and you've been typing two
> hours in a room where there's one terminal and it does one thing."*
> **Aglaope:** *"You came up from the annex."*

Same chapter, same target, same opening — *"You came [direction]…"* — one at the top of each
scene, each telling Vexx what he has just done before he offers it. On the axes they are
genuinely separate: **Zeus reads activity and intent, Aglaope reads weight**, and their second
sentences prove it (his is an inventory of what Vexx did; hers, later, is *"You're carrying
it in from somewhere else tonight"*). But the **surface form is identical**, and the surface
form is what a reader hears. This is exactly the shape of every bleed the Ch.6–8 audit caught:
two axes that are correctly separated on paper, sharing a sentence opening on the page.

**Not fixed, because both fixes are worse.** Hers is four flat words and cannot be improved.
His must end on the terminal, because *"It's an open index"* answers the terminal — reversing
his clauses would land the speech on the notebook, which is the one object in the chapter that
must never be commented on. Recorded here so the next pass does not discover it as new.

Secondary, much weaker:
- **Vexx and Corwin** — vocabulary-correction vs grammar-correction. They never share a scene
  in Ch.9 and the matrix separates them. No action.
- **Vexx and Rx across the interface** — *"driving me up the wall"* / *"drives you up the
  wall."* One brotherly uptake, four lines apart. Left: it is how Vexx accepts a deflection
  without acknowledging it, which is required (nobody may notice the *"Fine."*).

---

## 7. GATES

All three clean, whole manuscript. Chapters 1–8 untouched and byte-identical.

| metric | limit | before | after |
|---|---|---|---|
| words | — | 3,421 | 3,416 |
| `and` /1k | ceiling 24.0 | 21.9 | **22.0** |
| em-dash /1k | 8.5 – 12.0 | 9.9 | **10.0** |
| comparison /1k | floor 2.0 | 2.6 | **2.6** |
| comma /1k | floor 58.0 | 62.0 | **61.8** |
| adverb /1k | ceiling 20 | 3.2 | **2.9** |
| narration sentences | — | 96 | **96** |
| narration median | floor 13 | 14.5 | **14.5** |
| narration `>=40w` | floor 11.5% | 15.6% | **15.6%** |
| narration `<=6w` | ceiling 33% | 21.9% | **21.9%** |
| dialogue lines | — | 161 | **161** |
| semicolons | 0 | 0 | **0** |
| straight quotes / apostrophes | 0 | 0 | **0** |
| British spellings | 0 | 1 (`alphabetise`, ungated) | **0** |

`style_check.py` **clean** · `grammar_check.py` **clean** (0 errors, 3 long-sentence notes,
same three as before) · `voice_wear_check.py` **clean — no retired phrases, no device over
cap**. `git diff --stat`: one file.

---

## 8. FOR THE ORCHESTRATOR

1. **Rx's *"Fine."* cap is spent at 5/5 and Ch.13 has to break it.** Author decision needed
   before Ch.13 is dispatched. This is the highest-priority item in this report.
2. **Aglaope's echo-figure must not recur in Ch.16 or Ch.23.** Put it in those dispatches.
3. **Zeus/Aglaope share the *"You came…"* opening.** Not fixable here; give one of them a
   different way in the next time they both open on Vexx.
4. **`alphabetise` slipped a gate.** Add the `-ise` forms to `books/_template/tools/style_check.py`
   at the root, per the UPDATE RULE. Not done here — the one-file constraint.
5. **Zeus is the character this book's bleed keeps landing on**, now for the second chapter
   running (six edits in Ch.8, five here). Every dispatch that puts him on the page should
   carry the never-asks-why line and the counting rule explicitly.
