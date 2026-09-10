# Dialogue Pass — Chapter 10: Compliance

Scope: dialogue only. **Nine edits, all inside quoted speech.** No narration paragraph was
touched — verified mechanically, not by eye: every line of the file that does not contain a
`“` is **byte-identical before and after** (`diff` of the non-quoted lines returns nothing),
and `style_check.py` reports the narration block unchanged at 108 sentences · median 18.5 ·
`>=40w` 20.4% · `<=6w` 28.7%. No idea, beat, plot point or outcome changed. The mandated first
line (the meeting time) and last line (the barometric figures) are untouched. Question marks:
**5 before, 5 after — none removed.**

`git diff --stat`: **1 file changed, 9 insertions(+), 9 deletions(-)**.

**REVEAL verified byte-for-byte.** Both instances of Dessen's two-sentence finding are
character-identical to each other *and* to their pre-pass state (string comparison, not
inspection): `2 instances | identical: True | unchanged from before: True`.

---

## 1. COVER-THE-NAME TEST

**Method as Ch.9.** Every quoted turn and every italic interface turn stripped of tag, beat,
paragraph and turn-order, read cold **against the whole twenty-voice cast**. **DISTINCT** =
lands on exactly one character on first read. **WEAK** = lands only once turn-taking is
restored. **INDISTINCT** = lands on nobody, *or on the wrong character because it is wearing
somebody else's device.*

**92 attributable turns** (87 quoted + 5 italic interface), against `style_check.py`'s 210 →
207 dialogue lines (its splitter counts sentences, not turns; turns are the only unit the test
runs in).

| | DISTINCT | WEAK | INDISTINCT | Strict | Tolerant |
|---|---|---|---|---|---|
| **Before** | 46 | 30 | **16** | **50.0 %** | 82.6 % |
| **After** | 47 | 32 | **13** | **51.1 %** | **85.9 %** |

Per character, after:

| Character | Turns | Distinct | Weak | Indistinct |
|---|---|---|---|---|
| Dessen | 40 | 24 | 13 | 3 |
| Vexx | 25 | 4 | 12 | 9 |
| Jameson | 22 | 16 | 5 | 1 |
| Rx | 5 | 4 | 1 | 0 |

**Read the rate against the form.** This is a 4,000-word interrogation. **All 13 remaining
INDISTINCT turns are three words or fewer** and sit in the question-and-answer spine —
Vexx's four bare *"No."*s, *"Yes."*, *"I did."*, *"Go on."*, *"I will,"*; Dessen's
*"Inconclusive."*, *"That's it,"*, *"It is,"*; Jameson's *"All of it."* Lengthening them to
make them identifiable in isolation would be writing to the metric and would destroy the
airlessness the chapter exists for. They are not defects and were left. **Every INDISTINCT
that was a *misassignment* — a turn landing on the wrong character because it wore that
character's device — is fixed.** There were three (two to Zeus, one to Dessen); there are now
none.

Vexx's low strict rate is a property of the scene, not of his voice: he is under caution and
answers in one and two words for two thirds of the chapter. His four DISTINCT turns are the
four times he is allowed a sentence, and all four are unmistakably his.

---

## 2. THE GATE CONDITION — MY INDEPENDENT VERDICT

**It holds. I concur with the writer, and I did not take his word for it.**

I read all 22 Jameson turns twice: once as the scene means them, once in the voice of a man
who watched Rx die at close range, wrote the report that buried it, and has come to a
compliance room to find out how close an investigator has got to the Corwin material. A line
fails if the second reading yields *extra* meaning — if it is cleverer for the reader than for
the character, or if it could be replayed later by Vexx and heard differently.

**Nothing fails.** Six lines I tested hardest, and why each survives:

**(1) *"I know who you are. I've read your file. I've read your finding."*** — the closest
call in the chapter, and the one I nearly cut. Cold, it is the classic intimidation opener,
and it is said to the officer investigating the evidence of his own crime. It survives on
three grounds. It gains **nothing** from the murder — it is about her personnel record, not
about Corwin, and knowing he is the killer adds no second layer to it. It is his established
Ch.2 move, warmly meant there (*"I've read your file. All of it"*), so its recurrence
characterises consistency rather than menace. And it is capped one clause later by *"I came
from the other end of the building without a coat"* — a man volunteering that he is wet,
unprepared and undignified, which is the opposite of a man running a play. It stands
unapologised-for inside the eight seconds; that is designed rudeness, not a threat.

**(2) *"…every board that ever opens him reads it first, and not a single one of them ever
finds out it was written by somebody who has never in her life had to decide anything in under
a minute."*** — the most resonant line in the chapter for a reader who knows, because
Jameson's own crime is a written report nobody ever questioned. Tested and cleared: he is not
saying it about himself, he does not know it applies to himself, and **Vexx hears a defence.**
This is dramatic irony supplied entirely from Ch.2's narration, which is precisely what the
outline asks for. It also carries his Ch.24 grievance (boards, timetables) forward without
naming it.

**(3) *"…he drew it in person, off the counter, himself, which isn't in your finding and
should be, because that was the last place a third party could have got into the chain, and he
shut that door too."*** — the line a man protecting himself would most want on the record
(no witnesses in the chain). It survives because he supplies it **against Vexx**, unprompted,
to strengthen the case he is about to demolish, and immediately calls it *"worse."* A man
managing this room does not hand the prosecutor her missing paragraph. This is the strongest
single proof in the chapter that he is not managing anyone.

**(4) *"You'd have signed the truth. That's the trouble with an honest man in a compliance
room — he's the only person in it who can be talked out of his own position."*** — the
second-hardest. It is, read one way, Jameson describing his own method to its subject. It
survives because it is an **observation, not a warning** — he does not say *be careful who
talks to you*, does not name a future, does not leave anything for Vexx to act on. It is
fondness, and it is also simply true, and the sentence means exactly the same thing at both
levels. Nothing is hidden in it.

**(5) *"That woman is going to run this directorate in nine years, and I have made an enemy of
her in a store cupboard."*** — available as *a killer worrying about the investigator who
might one day look at him.* Survives on the joke: the scale is vanity, the setting is a store
cupboard, and the anxiety is about his own standing thirty seconds after saving a man's
career. Read as a man who knows, it would be a strangely trivial thing to say.

**(6) *"Don't thank me. I read a disposition line. That isn't a favor, it's Thursday."*** —
modesty, meant, and it is true. Kept (see §4 for the one device question attached to it).

**He is never told anything he does not already have**, he wins on a public document any
competent officer could have found, and **he is not given an exit line** — he leaves
mid-sentence about his father's barometer and the doors take the rest of it. I found no
knowing pause, no aside, no conditional, no sentence Vexx could replay.

**One gate improvement made, not merely confirmed.** *"Which is not weather. That's a front.
It'll be in off the water by tonight."* is the one line I judged actively unsafe — not as a
threat, but because the bible requires the barometer to **never become a metaphor**, and *"that
isn't weather, that's a front coming"* is exactly the shape a reader converts into
foreshadowing. It is now *"That much in two days is a front,"* which is pure hobbyist
rate-of-fall shop-talk with no metaphorical lift, and which additionally plants the coda's
*"you don't read the number, you read how long it took to get there."*

---

## 3. §STANDING OFFENCES — CHECKED BY NAME, FIRST, BEFORE ANY OTHER READ

Searched in quoted dialogue, in the italic interface register, **and in narration and reported
speech** — the Ch.9 recurrence hid inside a run of reported questions.

| # | The rule | Verdict |
|---|---|---|
| **1** | **Zeus never asks why** | **CLEAR.** Zeus does not appear, is not named, and is not reported anywhere in Ch.10 (`grep -i zeus` → 0). The only `why` in the chapter is **Rx's** (*"Why?"*, line 318), which is legal. No why-in-other-clothes in narration either: I re-read every reported question in the chapter (*"the first thing any competent officer asks is where it has been"* — a where; *"Against which reference."* — a which; *"Do you know anybody in operational support"* — a who) and none asks for the reason behind a stated reason. |
| **2** | **Aglaope does not use Zeus's *"That's not X. That's Y"*** | **CLEAR as to Aglaope** — she does not appear. **But the device itself is FOUND, twice, on new mouths** — see §4. The bible's rule is *"no NEW character may be given this shape,"* and Jameson had been given it three times. Two removed. |
| **3** | **Only Spector counts ALOUD** (the *N-of-the-M* construction included) | **FOUND AGAIN. Third consecutive chapter.** Jameson: *"Compliance has produced four findings in this building this year. **Three of them** were about parking."* M, then N-of-M, spoken, performed at a room — the identical shape caught on Gaia in Ch.8 and Zeus in Ch.9. **Fixed** (J3). One secondary count-echo also removed (J4). |
| **4** | **Rx's too-quick denial is capped (5/5 spent)** | **CLEAR.** Zero instances in Ch.10 — `grep` of the phrase family across the whole manuscript returns Ch.1 ×1, Ch.3 ×3, Ch.9 ×1 (Rx) and Ch.8 ×1 (Gaia, a concession, not a denial). The cap is untouched by this chapter and Ch.13's break is unaffected. Rx's *"It isn't. Being used."*-adjacent moment belongs to **Vexx**, and the 195-word narration sentence before it makes it slow, which is the inverse of the device. |
| **5** | **The tidying gesture (squaring to an edge, the quarter-turn)** | **CLEAR. Zero instances in Ch.10.** Grepped the whole manuscript for `squar/quarter-turn/straighten/tidy/lined up/aligned`: Ch.10 returns nothing. The nearest approach is Jameson *"pulling one out, turning it"* — a man turning a chair in order to sit in it, in a sentence that explicitly denies fuss (*"doing none of the small business a man does to make a point of arriving late"*). Not the gesture. **The new character did not pick it up.** |
| **6** | **Hands flat on a surface is Ch.1's gesture** | **CLEAR. Zero instances in Ch.10.** Grepped `hands flat / flat on the / palms flat / both hands on`: Ch.10 returns nothing. The nearest approach is *"He set his hands on the arms of the chair"* — chair arms, not a surface, and not flat. **The new character did not pick it up.** Vexx's *"His hand was on the edge of the table. He took it off."* is the **table-edge** substitute the Ch.9 pass introduced for exactly this reason, correctly reused. |

**Recommendation for `character-bible.md` (not actioned — one-file constraint):** offence #3
has now recurred in **three consecutive chapters** (Ch.8 Gaia · Ch.9 Zeus/Vexx · Ch.10
Jameson). Every dispatch should carry the counting rule in the same explicit form the Ch.9
report asked for on Zeus.

---

## 4. DEVICE-BLEED AUDIT — every speaker × every reserved device

Four speakers against the full one-device map, **including the routes nobody predicted** — the
brief is right that the predicted pairs held again and the bleed went elsewhere. `—` = the
device does not appear. **HIT** = fixed below.

| Reserved device (owner) | JAMESON | DESSEN | VEXX | RX |
|---|---|---|---|---|
| Counting **ALOUD** / N-of-M / sequence (**Spector**) | **HIT → J3** (four findings / three of them), **HIT → J4** (twice / both times). Residuals cleared below | near-miss cleared below (*twice a year … both times*) | clean — no spoken count | cleared below (*ninety words a minute*, *twenty-two minutes*) |
| The private, silent tally (**Vexx/Rx**) | — | — | **his own** — the closing beat is memorisation, silent, said to nobody. Canon-clean | — |
| Compulsive narration / never letting a silence stand (**Echo**) | **examined hard, cleared** — the aneroid run-on is framed as filling a silence, but ten lines earlier he **lets a silence stand at length, deliberately** (*"he waited a good deal longer than the silence could comfortably carry"*). The chapter shows him doing the opposite first, on the page. Echo's is a compulsion; this is one man covering for another man's failure | clean — she lets every silence stand | clean | clean — he goes almost entirely quiet from the moment Jameson enters |
| Naming/labelling, then using the name as agreed (**Echo**) | *"a solitude problem"* — coined once, not reused. Cleared | — | — | — |
| Too-quick denial / reflex deflection (**Rx**) | clean | clean | *"It isn't. Being used."* — cleared: the 195-word sentence before it is the delay, and the device is **speed** | **not used** ✓ (cap untouched) |
| Body-check question before content (**Bastion**) | clean — and note the inverse is load-bearing: in the corridor he **notices** Vexx is in difficulty and asks nothing | clean — *"The water's been standing since yesterday. I'd have it anyway"* is a fact about the water | — | — |
| Restate-then-disagree; *"No."* as a sentence (**Paladin**) | **the closest structural neighbour, and cleanly separated on the page.** *"Then let me put your case, because I don't think you've put it hard enough"* restates her position and then defeats it — but Paladin restates **accurately**, Jameson restates **better than you did**, and this chapter announces the difference in the line itself. Cleared, and it is the best demonstration of the split in the book | clean | four bare *"No."* — under caution, answers, no restatement. Cleared (same finding as Ch.9) | — |
| Correcting the terms of a question (**Vexx**, capped 5) | *"Then what you have is a solitude problem"* supplies a word she **never used**; Vexx corrects a word he **was handed**. Cleared, near-neighbour logged | clean | **his own — 0 spent in Ch.10.** Book total stays **2 / 5** | — |
| Pre-empt the objection and improve it (**Jameson**) | **his own**, twice (the steelman; the disposition line) | clean — *"you're entitled to hear the finding"* is entitlement-reading, not improvement | — | — |
| **"That's not X. That's Y"** / corrective two-beat reframe (**Zeus**) | **HIT → J5** (*"So it isn't a custody problem. It's a solitude problem."* — negates **her** term). **HIT → J7** (*"Which is not weather. That's a front."*). One retained — see below | **present and PROTECTED** — *"You didn't destroy it. You did something narrower."* and *"Not because it's contaminated — because…"* are quoted as canon in her ANCHORED note. Logged, not touched | clean | clean |
| Withhold until useful / answer late (**Hollow**) | clean — he withholds nothing | clean | — | *"He'll have gone by now … answering something Vexx had not asked him"* — **examined hard, cleared.** Hollow's device is answering **forty minutes late**; Rx's is **immediate** anticipation of his brother's unspoken question, which is his own card (monitoring Vexx constantly). Opposite timing, opposite content. Logged for a future pass because the *narration's wording* sits close to Hollow's card |
| Fact-then-silence, no modals (**Voss**) | clean — he explains constantly | near-neighbour, cleared: Voss gives a fact and stops; Dessen gives a fact and **writes down what you do with it**, which the chapter dramatises continuously | clean | — |
| **Same question three times, one word changed** (**Dessen**) | **HIT → J6.** *"What did the board rule."* / *"What did the board rule about the material."* — a re-issue with a qualifier added, getting a different answer: her technique, run **on her, in her only chapter.** **HIT → J2:** *"Say the rest of it."* / *"Say the rest of the sentence."* — the same demand with one term swapped, twelve lines before she does it herself | **her own** — and **D1** removes a second anaphoric pair from her mouth to protect it (see §5) | clean | clean |
| Involuntary self-echo (**Merrick**) | *"No." / "No, that was contemptible."* — emphasis, and the hinge of the chapter. Cleared | *"Every last one of these dies at the tail. Every single one."* — emphatic requantification, not an echo of her own last three words. Cleared, watched | clean | clean |
| Naming what she noticed, unasked (**Aglaope**) | clean — and pointedly so: in the corridor he notices and **says nothing** | *"The water's been standing since yesterday"* — she names a fact about the room, never about him. Cleared | — | — |
| Fact → ask → clock; *"your call"* (**Gaia**) | clean — **he never puts a clock on anything**, never asks for a decision, never leaves a door open | *"You'll get a property return notice inside a fortnight. Answer it the same day."* — fact + instruction + clock, but **no ask and no decision demanded.** Cleared, near-neighbour logged | — | — |
| Trade vocabulary for ethics (**Goliath**) | *"it's a paragraph, a signature, a line in the quarterly"* — clerical, his band. Clean | clean | clean | clean |
| The pause before agreement (**Requiem**) | *"Thank you. I would."* / *"Good."* — both immediate. Clean | *"Yes. That's better than I had it."* — she pauses **before**, and the narration measures it as a working silence with the heating cycling; but she is checking a document, not withholding assent. Cleared | — | — |
| The singing image (**Requiem**) | — | — | — | — |
| Grammar correction (**Corwin**) | *"Not the clause number. The words."* is a specification of **which text to read**, not a correctness rebuke. Clean | clean | clean | — |
| Self-interrupting over-explanation (**Reyes**) | the aneroid speech is cut off **by the elevator doors**, not by himself, and he does not run out. Cleared | clean | *"My brother's—"* is a sentence that **stops**, not a self-interruption that redirects. Cleared | — |
| Interviewing the people assessing him (**Ives**) | he asks Dessen a run of questions but is not under assessment. Clean | — | — | — |
| Standing whenever anyone enters (**Beck**) | he **does not sit** on entering and sits only when invited — his own card (*he stands when an operator enters*), not Beck's compulsion. Clean | clean | clean | — |
| **The why-question** (**Zeus never**) | asks no why | asks no why | asks no why | *"Why?"* ×1 — legal |

### The one instance of Zeus's shape I kept, and why

**Jameson: *"Don't thank me. I read a disposition line. That isn't a favor, it's Thursday."***
By the strict surface test this is the form — it negates Vexx's term and substitutes another.
I kept it, and the distinction is real: **Zeus's device supplies the *true* category**
(*"That's not caution. That's a man rationing himself"*); Jameson supplies an **absurd** one in
order to refuse credit. That is deflation, not correction — a different rhetorical act aimed at
a different target (himself). After J5 and J7 it is the **only** true instance in his mouth,
which puts a non-owner at one where the Ch.9 pass allowed the owner two. Two weaker instructions
survive — *"Not the clause number. The words."* and *"Not the summary — the disposition."* —
and I cleared both deliberately: they negate one of **Jameson's own** alternatives to specify
what he wants read, they are not reframes of anybody's position, and the pair is a deliberate
rhyme that pays off on the disposition line, which wins the scene.

### Residuals examined and cleared, with reasoning

- **Triadic lists are not counting.** Rx's *"first light, last light, the state of the water and
  a fishing advisory"*; Jameson's *"a paragraph, a signature, a line in the quarterly"*;
  Dessen's *"No extension. No note to the lock. No line anywhere…"*. Applied literally,
  *"cataloguing"* would make the book unwritable. The bible's operative narrowing is the one I
  used throughout: **Spector's device is counting performed as competence, for a room** — an
  unnecessary count that goes right. None of these carries a number, and none is performed.
- **Dessen's *"The board sits twice a year. I've been told both times…"*** — the same M/all-of-M
  shape as J4, and I removed **Jameson's** rather than hers, because hers is load-bearing (she
  applied twice and was refused twice with the same sentence) and is the closing beat of her own
  thread. With his gone, the construction appears once in the chapter, in the mouth it belongs
  to. **This was also a shared-reach hit** — *twice … both times*, two characters, one chapter —
  and it is now resolved in one edit.
- **Rx's *"about ninety words a minute … twenty-two minutes."*** Two measurements of another
  person's hand, not a tally of anything, no N-of-M. Cleared (I concur with the writer).
- **Rx's *"A board is three people, a table you can't reach across, and a stenographer who hates
  you personally."*** A rule-of-three joke-definition; the three items are not three of a kind
  and no count is performed. Cleared.
- **Jameson's precise numbers** (*nine points*, *nine years*, *six hours*, *four months*, *forty
  times a week*, *All four things*) are explicitly licensed by his card (*"concrete nouns and
  precise numbers"*). What is **not** licensed is enumerating a set and then counting a subset
  of it, which is what J3 removed. *"I'm sorry. All four things."* is a summation of his own
  enumerated apology, not a performance — and it is the line that makes the apology refuse to
  soften. Kept.
- **Jameson's *"I've read your file"* recurring from Ch.2.** Kept and judged **good**: the same
  man doing the same thing, which the chapter is already calling back to explicitly (*"the same
  as it had been in a briefing room two levels below anything with a name on the door"*). Vexx
  also uses it in Ch.2, so it is ONI register rather than a reserved device.
- **Dessen's *"I want to be sure you understand what the finding is about."*** Logged as a
  low-grade cross-chapter neighbour of Jameson's Ch.2 *"I want you to understand what that
  means"* — different construction, he does not use it in this chapter, and her ANCHORED note
  canonises the beat. Cleared, not spent on.

---

## 5. GESTURE BLEED — what characters DO

Grepped the whole manuscript for the chapter's physical verbs (`set · put · turn · tap · fold ·
rub · cap · press · hand · thumb · click · underline · draw · pull · push`) and counted per
character. **Ch.10 is clean, and it is the cleanest chapter in the book on this axis.**

| Business | Instances in Ch.10 | Characters | Book-wide |
|---|---|---|---|
| The pen — capping, clicking, the sound, the speed | 19 | **Dessen only** | Ch.10 only, in this form |
| *turned a leaf* | 2 | **Dessen only** | Ch.10 only |
| The cap — turned over, on the knee, in both hands | 6 | **Jameson only** | Ch.10 only (`grep "his cap"` → chapter-10 exclusively) |
| The table **edge** | 1 | **Vexx only** | the Ch.9 substitute for offence #6, correctly reused |
| Squaring / quarter-turn (offence #5) | **0** | — | Ch.2 ×1 (author, Zeus) · Ch.6 ×3 · Ch.8 ×2 |
| Hands flat on a surface (offence #6) | **0** | — | Ch.1 ×1 (author) · Ch.6 · Ch.7 (load-bearing) |

Two characters own two large, distinct, uncontaminated physical vocabularies for four thousand
words in one room. **The new character picked up neither over-spent gesture.**

**One item logged, not fixed.** *"He set the pad down on the table without looking at where it
landed"* (Jameson, Ch.10) shares six words with *"set the pad down on the wood face-down"*
(Voss, Ch.6). One instance each, two characters, well under the three-character threshold, and
the gestures mean **opposite** things — Voss's is her registered controlled face-down return,
Jameson's is a man who has never had to keep track of his own props. Recorded so the next pass
does not find it as new; a third user would make it bleed.

---

## 6. EVERY LINE CHANGED (9 edits)

### Jameson — device bleed

**J1 — Zeus's *"All right."*, verbatim.** (line 302)
> “It'll keep,” Vexx said. / **“All right.”**
> → “It'll keep,” Vexx said. / **“As you like.”**

`All right` as a **bare standalone turn** belongs to Zeus in this book — Ch.4:83, Ch.8:312,
Ch.9:88 — and Ch.9's narration explicitly measures it as **his** (*"the flattest three
syllables in the room"*). Reusing it, unlabelled, on the other measured senior voice, at the
chapter's emotional peak, is the exact shape the brief warns about: correctly separated axes
sharing a surface. The replacement had to be inert, warm, immediate, in-register, and — per
the paragraph that follows it — must **not** leave a door open. I rejected *"Of course."*
specifically because Vexx (Ch.6:210) and Aglaope (Ch.9:196) already hold it as a bare turn and
a third user would make it nobody's; I rejected *"Then it'll keep"* and *"Take your time"*
because both lean forward, which the next sentence forbids and the gate dislikes. *"As you
like"* is a grant, it costs him nothing (his card), and it closes the subject completely.

**J2 — Dessen's device: the demand re-issued with one term swapped.** (lines 154, 158)
> **“Say the rest of it.”** … “I came from the other end of the building without a coat. **Say the rest of the sentence.**”
> → **“Finish the sentence.”** … “I came from the other end of the building without a coat. **Read me the end of it.**”

Two faults in one exchange. (a) *"Say the rest of it."* is **verbatim Aglaope**, Ch.9:192 —
consecutive chapters, a whole five-word turn, one bare imperative each. (b) The two demands
together are the same command with one noun changed, which is **Dessen's registered technique**,
performed at her, twelve lines before she is characterised by it. The replacements are two
structurally different demands, and the second lands his real method (*make the record speak*)
alongside *"Read me the schedule"* and *"Read the disposition line"* — three imperatives that
now read as one consistent habit rather than an accident.

**J3 — STANDING OFFENCE #3: the spoken N-of-M.** (line 162)
> “**Compliance has produced four findings in this building this year. Three of them were about parking.**”
> → “**The last finding Compliance produced in this building was about parking.**”

M, then N-of-M, spoken, performed at a room: Spector's construction, caught for the third
chapter running. Everything the beat needs survives — the contempt, the invented fact, and his
own retraction of it (*"The thing about the parking, I don't know to be true"*), which reads
identically against a single claim. It is also **shorter**, which is right inside eight seconds,
and a single specific slur is more contemptuous than a statistic.

**J4 — the count-echo, and a shared reach with Dessen.** (line 174)
> “I have relied on it **twice this year, both times to my advantage, neither time with a note of thanks to anybody.**”
> → “I have relied on it **twice this year, to my advantage, and thanked nobody for it.**”

*Twice → both times → neither time* is a count restated twice, which is the drumbeat Z02
removed from Zeus in Ch.9. It was also the same construction Dessen uses ninety-odd lines later
(*"twice a year … both times"*) — two characters reaching the same unusual figure in one
chapter. Fixing his leaves the shape once, in the right mouth. **The outcome-grading the writer
identified as one of the chapter's three reader-supplied chills is fully preserved** —
*"to my advantage"* survives, and *"thanked nobody for it"* is a harder self-accusation than
the original's three-clause hedge.

**J5 — Zeus's corrective two-beat, on Dessen's own term.** (line 204)
> **“So it isn't a custody problem,” Jameson said. “It's a solitude problem. You're saying** he was alone in it start to finish…”
> → **“Then what you have is a solitude problem,” Jameson said. “You're saying** he was alone in it start to finish…”

The strongest bleed in the chapter: it negates the other character's stated term and substitutes
the correct one, which is the definition of the device the bible reserves to Zeus and forbids
to new characters. Cold-read, the original assigns to Zeus. The rewrite is the same act
performed on **Jameson's** axis — he does not correct her word, he **supplies one she never
had**, which is what her reply has always said he did: *"That's better than I had it."* The
coinage *"solitude problem"* is preserved intact; *"chain of custody"* is in the reader's ear
from the finding, from Rx, and from Jameson's own preceding speech, so nothing is lost.

**J6 — Dessen's device again, in her own scene.** (line 212)
> “**What did the board rule about the material.**”
> → “**On the material.**”

The same question re-issued with a qualifier added, producing a different answer: her technique
exactly, run on her 130 lines after she runs it on Vexx. A technique a second character performs
in the same scene stops belonging to the first. The bare narrowing is terser, more senior, does
her no damage, and *"Nothing in the room for a second"* and her answer both land unchanged.

**J7 — Zeus's two-beat, and the barometer tipping into metaphor.** (line 240)
> “Pressure's fallen nine points since Tuesday,” he said. “**Which is not weather. That's a front.** It'll be in off the water by tonight.”
> → “Pressure's fallen nine points since Tuesday,” he said. “**That much in two days is a front.** It'll be in off the water by tonight.”

Two reasons, and the second is the more important. It is the third instance of the reserved
two-beat in Jameson's mouth. And *"that isn't weather, that's a front"* is the exact phrasing a
reader converts into foreshadowing, which the bible forbids absolutely (*the barometer must
never become a metaphor*). The replacement is a hobbyist's rate-of-fall rule — nine points in
two days, Tuesday to Thursday, consistent with *"it's Thursday"* — with no metaphorical lift at
all, and it quietly plants the coda's *"you don't read the number, you read how long it took to
get there."* The beat is unchanged: he says it, Dessen turns a leaf and goes on writing.

### Dessen — protecting her own technique

**D1 — a second anaphoric question-pair in the same scene.** (line 106)
> “—the fourteen days,” Dessen said. “Do you dispute the period.” / “No.” / “**Do you dispute that it ran out.**” / “No.”
> → “—the fourteen days,” Dessen said. “Do you dispute the period.” / “No.” / “**Or that it ran out.**” / “No.”

Her ANCHORED note is explicit that the triple **fires once and only once**, *"because a
technique used twice in one scene reads as a quirk"* — and forty lines after it, the surface
form was back: *"Do you dispute X." / "Do you dispute Y."* It is not the technique (the two
questions have different content and both answers are the same, so nothing is diagnostic), but
it is the technique's **sound**, and the sound is what a reader hears. Continuing the sentence
instead of re-opening it is tighter, is exactly how a compliance officer adds the second half
after the first answer, and leaves the triple as the only repetition in her chapter.

---

## 7. THE FOUR JUDGEMENTS THE BRIEF ASKED FOR

### (a) Dessen is not a stooge and not a bully. Her case is correct.

**Confirmed, and I found nothing to fix.** She reads him his entitlement before asking a single
question; declines to chase the clerk *because the clerk is not her question* (which keeps her
honest rather than lenient, and keeps Voss un-endangered); tells him to drink the standing
water; thanks him for the retraction and **puts the retraction on the page in his favour**;
exercises discretion not to send him to a board; concedes to Jameson **on the merits, in her own
time, after checking the document herself**; and the finding **stands**, because it is right.
She never says *"I think"* — verified line by line; the only *"I don't think"* in the chapter is
Jameson's.

Her case is correct on both halves, and the second half is what saves the chapter from being a
paperwork argument: the plate is not contaminated, it is **unvouchable**, and *"You made it
useless to him"* is a moral finding, not a procedural one. The one structure I tested as a risk
was lecture-mode at line 134 — it survives, because the content is **new to Vexx**, it is the
chapter's value shift, Vexx's *"Go on."* motivates it, and it is broken twice (the turned leaf,
the heating going off). It is a compliance officer doing her job, not a mouthpiece.

Her own life is on the page and belongs to nobody else: the pen that dies at the tail and the
one human flare of irritation about it, the strap set for somebody else's shoulder, and the
transfer — raised unprompted, answered *"No,"* dropped, and never picked up by anyone.

### (b) The triple question — verified, with one honest discrepancy

> Q1 *"What was the material **required** for."* → **“Secondary examination.”**
> Q2 *"What was the material **used** for."* → **“I looked at it again … under a better light …”**
> Q3 *"What **is** the material **being used** for."* → **“It isn't. Being used.”**

**Q1 → Q2 is exactly one word.** **Q2 → Q3 is one *tense shift* realised in two tokens**
(`was … used` → `is … being used`). Dessen's card says *"one word changed"*; her ANCHORED note,
written after the chapter, says *"one verb changed each time"*. **I resolved in favour of the
anchored canon and did not change it**, and I think that is right: the only one-token
alternative is *"What is the material used for,"* which collapses the diagnostic — a bare
present is answerable with Q2's answer, and it is the **progressive** that forces the present
moment and leaves Vexx nothing. Flagged so the card and the note can be reconciled in the
bible; the prose should win, as it did over the counting rule.

**The three answers really differ, and the difference is diagnostic of *him*, not of her
method.** A1 is the form's own words — he hands back institutional boilerplate, which is
withholding. A2 is true, volunteered, and **over-detailed** (the field lamp, the kitchen table,
the lamp brought down close) — a man relieved to be asked something he can answer honestly. A3
is true and conceals everything. Read in sequence they show the reader the exact shape of the
man: **he tells the truth expansively in the middle register and hides at both ends**, and
Dessen writes all three down *"each under the last, drawing no line between them,"* which is her
declining to editorialise about precisely the thing she has just proved. It fires once and is
not repeated (see D1).

### (c) Vexx degrades in the right way — withholding vs fabricating

**Confirmed, and the chapter finds the difference exactly where it should.** The withheld
clerk's name comes out *"level, easy, **a shade ahead of the question**"* and costs him nothing.
The fabricated extension arrives *"before he had decided anything,"* and the failure is the
right one — **not nerves, but the absence of detail**: he can see the reference format (*a
letter, four figures, a stroke, the year*), he can see the box it goes in, and he cannot put
anything inside the box. That is precisely what a man who has never fabricated cannot do at
speed. The retraction is then flat, exact and self-analytic — *"I said that because you asked me
a question I had no answer to, and it seemed better to have one"* — which is his card under
maximum load (*he goes flat, and reports facts in sequence like a log entry*), not a confession.
Nothing here needed changing.

His term-correction device is **not deployed at all** in Ch.10. Book total remains **2 / 5**.

### (d) The apology is better than the anger, and it is not a management move

**Confirmed on two tests.**

*Test one — does he gain?* He apologises **before he has an argument** and before he is invited
to sit; he gains nothing he could not have taken by rank. And thirty seconds later, in the
corridor, he says he has **made an enemy of her** — his own read is that it cost him. A
management move whose author believes it failed is not a management move.

*Test two — does it volunteer a harm the other party has not raised?* Yes, and this is decisive.
His fourth item is that he has **damaged her authority in front of an operator under her
questioning** — a cost to *her* that she has not mentioned, that Vexx has not noticed, and that
he did not need to name. And he refuses the one thing every managed apology requires, an offer:
*"I'd like to say I'll repair it. I can't — there isn't a mechanism."*

It is specific (four named offences, in order), it grades itself (*"The first part was temper.
The second part I chose"* — his outcome-worldview turned on himself), it names the ugly thing
plainly (*contemptible*, *trivial*, *temper*) with **no register-softener anywhere** — no
*unfortunate*, no *regrettable*, per his card — and it asks for nothing. The anger, by contrast,
is generalised, contains an invented fact, and is a **bad draft of the argument he then makes
properly**. The apology is better than the anger. Untouched by this pass except J3 and J4, both
of which make it harder rather than softer.

He does not raise his voice anywhere in the chapter. Card intact.

---

## 8. IS JAMESON DISTINCT FROM ZEUS?

**Yes — after this pass, plainly. Before it, not plainly enough, and this was the chapter's
largest defect after the counting offence.**

Jameson carries ~40 spoken sentences here against a handful in Ch.2, and under that load he was
drifting onto the other measured, controlled, senior voice by **three separate routes**, none
of which the Cover-the-Name Test could see, because every one of those lines read as vividly
*somebody's*:

1. **Zeus's corrective two-beat reframe**, three times (J5, J7, and the retained deflation).
2. **Zeus's bare *"All right."***, verbatim, in the same accepting function (J1).
3. Plus **Dessen's** re-issued question, twice (J2, J6) — bleed onto the *other* methodical
   questioner in the room.

With five of those removed, the split is clean and it is now visible in the text rather than
only on the matrix:

| | **Zeus** | **Jameson** |
|---|---|---|
| What he does to your position | **negates your term and supplies the true one** — *"That's not caution. That's a man rationing himself"* | **supplies a term you never had** — *"Then what you have is a solitude problem"* |
| What he tells you | what you are **doing** | what you are **thinking**, and then agrees with it |
| Questions | never repeats one; asks in a deliberately wrong order; **never asks why** | asks documents, not people — *read me the schedule*, *read the disposition line* |
| Wants | **nothing.** Never puts a clock on anything, never leaves a door open | wants the **outcome**, and says so |
| Numbers | clinical inventory, and Ch.9 removed one of his | precise, hobbyist, and landing on nobody |
| Warmth | withheld deliberately; never comforts | continuous, sincere, and free — every concession costs him nothing |
| Silence | comfortable in it, lets it run all morning | **lets one run**, then spends it on a barometer |

The corridor coda is now the proof: Zeus, given a man failing to finish a sentence about his
brother, would have named what the man was protecting. Jameson notices, says nothing, waits
past comfort, grants it, and then fills the silence with his father's aneroid. **They cannot be
confused across those eight lines.** He is also distinct from Dessen (she repeats, he narrows
once and moves) and from Voss (she stops, he explains).

---

## 9. PAIRS I STILL JUDGE TOO CLOSE

1. **Dessen and Zeus, on *"That's not X. That's Y."*** Her two instances — *"You didn't destroy
   it. You did something narrower."* and *"Not because it's contaminated — because there's no
   longer anyone who can say it isn't."* — are **quoted as canon** in her ANCHORED note and I
   did not touch them. They are the moral centre of her case. But they mean the device now
   stands in three mouths across the book (Zeus, Corwin's grandfathered four, Dessen), and Zeus
   is the owner. **Recommendation:** if Dessen ever returns, she loses it; and no further
   character acquires it. Recorded so the next pass does not find it as new.
2. **Jameson and Paladin, restate-then-defeat.** Structurally identical, separated only by
   *"better than you would."* This chapter separates them beautifully because Jameson announces
   the difference out loud. **They must never share a scene without that announcement** — put it
   in any dispatch that puts Jameson in a room with Paladin.
3. **Rx and Hollow, answering the unasked question.** Cleared on timing (immediate vs forty
   minutes late) and content, but the *narration's* wording at line 278 — *"answering something
   Vexx had not asked him"* — is Hollow's card almost verbatim. Not a defect today; a defect the
   day Hollow does it on the page in the same words.
4. **Dessen and Gaia, on the closing clock.** *"Answer it the same day"* is fact + clock without
   the ask. One instance; a second would be Gaia's shape.
5. **Jameson and Voss, *set the pad down on the* ___.** Gesture, one instance each, opposite
   meanings. See §5.

---

## 10. GATES

All three clean. **Chapters 1–9 untouched and byte-identical** (`style_check.py` reports every
Ch.1–9 figure unchanged). Ch.10 shows **no new flag** — the same two breath ceilings that were
there before this pass, both of them the writer's declared long-mode over-reach and **explicitly
not mine to fix**.

| metric | limit | before | after |
|---|---|---|---|
| words (tokenizer) | — | 4,646 | **4,626** |
| `and` /1k | ceiling 24.0 | 17.4 | **17.7** |
| em-dash /1k | 8.5 – 12.0 | 10.8 | **10.8** (50 → 50, none added or removed) |
| comparison (simile) /1k | floor 2.0 | 2.2 | **2.2** |
| comma /1k | floor 58.0 | 63.7 | **64.0** |
| adverb /1k | ceiling 20.0 | 4.7 | **4.8** |
| `, which` narration /1k | ceiling 1.0 | 0.4 | **0.4** |
| question marks /1k | author 1.0–3.0 | 1.1 (5) | **1.1 (5 — none removed)** |
| narration sentences | — | 108 | **108** (byte-identical) |
| narration median | ceiling 18.0 | 18.5 ⚠ | **18.5** ⚠ *(pre-existing, not mine)* |
| narration `>=40w` | ceiling 16.5% | 20.4% ⚠ | **20.4%** ⚠ *(pre-existing, not mine)* |
| narration `<=6w` | ceiling 30.0% | 28.7% | **28.7%** |
| dialogue lines | — | 210 | **207** |
| semicolons | 0 | 0 | **0** |
| straight quotes / apostrophes | 0 | 0 | **0** |
| British spellings (incl. `-ise`/`-isation`) | 0 | 0 | **0** |
| repeated-phrase gate | no new | clean | **clean** |
| motif cap | ≤3 book-wide | clean | **clean** |

`style_check.py` → 2 issues, **the same two, unchanged** · `grammar_check.py` → **clean**
(0 errors, 3 long-sentence notes, the same three) · `voice_wear_check.py` → **clean — no
retired phrases, no device over cap**. `git diff --stat`: **1 file changed**.

---

## 11. FOR THE ORCHESTRATOR

1. **STANDING OFFENCE #3 has now recurred in three consecutive chapters** (Ch.8 Gaia · Ch.9
   Zeus/Vexx · Ch.10 Jameson) and has escaped onto a **principal**. Every dispatch should carry
   the counting rule explicitly, in the form the Ch.9 report asked for on Zeus.
2. **Add to §STANDING OFFENCES: *"That's not X. That's Y" is bleeding to new characters.*** It
   was Aglaope's recurrence in Ch.8 and Ch.9; in Ch.10 it arrived on **Jameson ×3 and Dessen
   ×2** with nobody named on any watch-list. Two of Jameson's are removed; Dessen's are canon.
   This device is now the book's most mobile.
3. **Reconcile Dessen's card with her ANCHORED note** on the triple: the card says *"one word
   changed"*, the note says *"one verb changed each time"*, and the prose does the latter. The
   prose should win, as it did over the counting carve-out.
4. **`character-bible.md` should record *"All right."* as Zeus's bare turn** — Ch.9's narration
   already treats it as measurable and his, and it walked onto Jameson unnoticed. Likewise
   *"Say the rest of it."* is now spent (Aglaope, Ch.9).
5. **The two breath ceilings on Ch.10 are still open** and are owned by a later pass. This pass
   deliberately did not lengthen or delete any narration sentence; the narration block is
   byte-identical, so that pass starts from exactly the numbers the writer reported.
6. **Rx's *"Fine."* cap remains 5/5 spent** and Ch.13's break still needs the author decision
   raised in the Ch.9 report. Ch.10 spends none of it.
