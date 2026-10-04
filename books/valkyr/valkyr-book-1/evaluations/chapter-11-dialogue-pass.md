# Dialogue Pass — Chapter 11: The Door

**First polish pass of any kind on this chapter.** Scope: dialogue only. **Seven edits, every
one inside quoted speech.**

**Mechanically verified, not eyeballed.** Every line of the file that does not contain a `“` is
**byte-identical before and after** (diff of the non-quoted lines returns nothing). Lines
changed: `6, 20, 62, 94, 152, 196` plus the header comment. `style_check.py` reports the
narration block **completely unchanged** — 37 sentences · median **18.0** · `>=40w` **16.2 %** ·
`<=6w` **21.6 %** · narration adverb **8.4/1k** · narration `and` **21.6/1k** · flat-man **1**.

**Em-dashes: 25 before, 25 after.** None added, none removed. **Question marks: 4 before,
4 after.**

No idea, beat, plot point or outcome changed. The reveal sentence (¶166), the *"That was your
one"* accounting (¶188–192), the laugh (¶140), the *"Dead"* beat (¶132) and the coda are
untouched.

---

## 0. THE DISPATCH, ANSWERED FIRST

The brief sent me after three borrowed devices on Gaia (continuity finding **N-09** /
`ENTITY_STATE.yaml` **CF-21**). **I found six, in five lines**, and fixed all six. The three the
audit did not have are marked ⚠️**NEW**.

| # | ¶ | Device | Rightful owner | Status |
|---|---|---|---|---|
| D1 | 6 | *"it isn't a door now, it's a hole"* **+** *"That's a hole with a hinge on it"* — the pivot **and** the `That's Y` half, two surface forms of the same device in one line | **ZEUS** (logged-bleed note: *no NEW character may be given this shape*) | **recast** |
| D2 | 20 | *"I don't need to hear the stair. I hear the stair."* | **VEXX** (capped 5, 2 spent) | **recast** |
| D3 | 62 | ⚠️**NEW** *"I'm **not asking** you to own it… **We're asking** whether…"* — negate-the-term-then-substitute, plus **Paladin's** *"we"* for *"I"* | **VEXX** + **PALADIN** | **recast** |
| D4 | 94 | *"That's what you asked for." / "**It's what I said.**"* | **VEXX** | **recast** |
| D5 | 152 | ⚠️**NEW** *"**It isn't that** you think we'd sell you. **It's that** you want us…"* — the full Zeus two-beat, inside the mind-reading speech | **ZEUS** | **recast** |
| D6 | 196 | ⚠️**NEW** *"**One laugh. Never two.**"* — a quantity stated, then the higher quantity negated: Spector's exact clipped numeric two-beat (*"Three. Two. Set. Clear."* / *"four drums, four seals, four intact"*), spoken, performed at a person | **SPECTOR** — **§STANDING OFFENCE #3, fourth consecutive chapter, same character as Ch.8** | **recast** |

**The brief's framing was right and it is worth restating.** Gaia's own device lands correctly
and untouched at ¶192 (*"What you do with the rest of it is your call"* — fact → ask → clock,
*your call* as the weapon). She was carrying **six of other people's** on top of it. She is not
under-served.

---

## 1. EVERY LINE CHANGED

### D1 — ¶6, the opening line. Zeus's reframe, ×2 surface forms.

```
BEFORE  “—it isn’t a door now, it’s a hole,” Gaia said. “A door does something.
         That’s a hole with a hinge on it.”

AFTER   “—it’s a hole with a hinge on it,” Gaia said. “A door does something.
         This one stands open and I lose the stair.”
```
The audit's suggested version was *"—there's no door there now. There's a hole with a hinge on
it."* I went further, and the reason matters: that version still runs **negation → substitution**
in two adjacent sentences, which is the shape, and it also left the third sentence (*"That's a
hole with a hinge on it"*) as a redundant second firing. Putting the image **first**, as a flat
assertion, dissolves the pivot entirely — there is nothing being corrected. The third sentence
then becomes free, and I spent it on **Gaia's own axis**: the operational loss (*"I lose the
stair"*), which is acoustics-and-exits, first person, no adjective, and which plants the stair
so that ¶16's *"I can't hear the stair through that"* and ¶200's closer both land as payoffs
rather than as new information.

Image kept. Rhythm kept (three beats, same count). 22 words → 23. **Em-dash count unchanged.**

### D2 — ¶20. Vexx's capped term-correction (1 of 3).

```
BEFORE  “I don’t need to hear the stair. I hear the stair.” She said it flatly, …
AFTER   “I hear it whether I’m listening or not.” She said it flatly, …
```
Vexx asks *"And you need to hear the stair."* The original edits his word (*need* → *hear*),
which is his device, verbatim in form. Gaia does not edit words; she states the fact that makes
the framing irrelevant and does not look back to see whether it landed — which is exactly what
the untouched beat after it already says she is doing. The involuntariness the original carried
(*it is not a need, it is a condition*) is now carried by *"whether I'm listening or not"*,
which is a self-report rather than a correction.

### D3 — ¶62. ⚠️NEW. Vexx's term-correction + Paladin's *"we"*.

```
BEFORE  “I’m not asking you to own it,” Gaia said. “We’re asking whether you’ve
         seen a man put it there.”
AFTER   “You don’t have to own it,” Gaia said. “Have you seen a man put it there.”
```
The audit missed this one and it is the purest instance in the chapter: *"I'm not X-ing. We're
Y-ing"*, the documented form of Vexx's device (*"I'm not angry. I'm careful."*) with the verb in
the slot instead of the adjective. Two defects fixed in one recast:

1. The negate-then-substitute frame is gone. *"You don't have to own it"* grants him something;
   nothing is substituted for it.
2. The indirect question becomes **direct, and loses its question mark** — which is *this
   chapter's own established Gaia form* (¶170 *"Which one."*, ¶174 *"Who briefed it."*, ¶178
   *"Have you got paper."*). Four of her questions now share one punctuation signature instead
   of three.
3. **Bonus:** *"We're asking"* was also **Paladin's** marker (*"we" where everyone else says
   "I"*) on a character whose card has her trusting nobody. Gone.

Question-mark count unchanged (the original was indirect and carried none).

### D4 — ¶94. Vexx's capped term-correction (2 of 3).

```
BEFORE  “I’ve got the door shut.” / “That’s what you asked for.” / “It’s what I said.”
AFTER   “I’ve got the door shut.” / “That’s what you asked for.” / “And nothing else.”
```
*asked* → *said* is a one-word vocabulary edit of his sentence: Vexx's device, and the second
firing of it inside seventy lines. *"And nothing else."* keeps the meaning (she has the door and
not the thing she came for) and routes it through her own register — flat, clipped, additive —
and it hands straight into *"Say it's a bad door"* without the beat of argument the correction
was spending.

### D5 — ¶152. ⚠️NEW. Zeus's two-beat, inside the mind-reading speech.

```
BEFORE  It isn’t that you think we’d sell you. It’s that you want us able to stand in
         front of a woman with a notebook, …
AFTER   You don’t think we’d sell you. You want us able to stand in front of a woman
         with a notebook, …
```
This is the full *"That's not X. That's Y"* in its *it-isn't-that / it's-that* clothing, and it
sat in the chapter's single most important speech. Recast as **two flat declaratives with the
same subject**, which is faster — and she is the fastest speaker in the cast — and which makes
it an item on her diagnosis list rather than a correction of a position nobody stated.

**The 70/30 is intact and I checked it specifically.** She is no more right and no less certain
than she was: the machine stays exactly right (he has had something since before the jungle; he
re-decides it weekly; he wants the cell deniable; he ranked them), the motive stays exactly
wrong, and the narration at ¶156 that adjudicates it is byte-identical. If anything the
declarative pair reads *more* certain, which is the correct direction.

### D6 — ¶196. ⚠️NEW. §STANDING OFFENCE #3 — Spector's spoken count.

```
BEFORE  “…who laughed once a night, about eleven. One laugh. Never two. I was in
         there five months.”
AFTER   “…who laughed once a night, about eleven. Then nothing off him until the next
         night. I was in there five months.”
```
**This is the find I would most want escalated.** It is not "a bit countish" — it is the
construction, in its signature shape: a quantity stated, then the next quantity up negated,
in two clipped sentences, spoken aloud at another character. Compare the owner's own line:
*"Three. Two. Set. Clear."* / *"four drums, four seals, four intact."*

The offence row is right that auditing *"is this in character?"* will never catch it. **It was
in character.** *"One laugh. Never two."* is a wonderful line for Gaia; the whole point is that
the construction lands in whoever is talking. And it landed on **Gaia, who was the Ch.8
offender for the same device** — so this is both the fourth consecutive chapter and the first
repeat offender.

The content is canon and stays (*"a stranger's laugh through a wall at nineteen"* is her
registered chaos marker). The dread was in the count; it is now in the **wait**, which is her
own axis — she is an acoustics specialist and what she is describing is five months of
listening to a wall for the next one. *"off him"* is her operational shorthand.

### D7 — the header comment
`Word count: 2,214` → `2,170` (style_check's tokenizer), with the revision named.

---

## 2. §STANDING OFFENCES — CHECKED BY NAME, FIRST, BEFORE ANY OTHER READ

Searched in quoted dialogue, in the italic interface register, **and in narration and reported
speech** — Ch.9's recurrence hid inside a run of reported questions.

| # | The rule | Verdict |
|---|---|---|
| **1** | **Zeus never asks why** | **CLEAR.** `grep -i zeus` → 0. Zeus does not appear, is not named, is not reported. The chapter's only *why* is **Gaia's** bare *"Why?"* (¶74), which is legal (precedent: Rx's *"Why?"* in Ch.10). I also re-read every reported question in the narration — there are none; this chapter reports no speech at all outside its two registers. |
| **2** | **No NEW character gets *"That's not X. That's Y"*** | ⚠️ **FOUND, TWICE, BOTH ON GAIA — the chapter's opening line and the climax of its biggest speech.** Fixed: **D1**, **D5**. Both are now zero. |
| **3** | **Only Spector counts ALOUD** (incl. *N-of-the-M*) | ⚠️ **FOUND AGAIN. FOURTH CONSECUTIVE CHAPTER** (Ch.8 Gaia · Ch.9 Zeus/Vexx · Ch.10 Jameson · **Ch.11 Gaia**), and the **first repeat offender**. *"One laugh. Never two."* Fixed: **D6**. Residuals audited and cleared in §4. |
| **4** | **Rx's too-quick denial is capped (5/5 smooth spent)** | **CLEAR.** `grep -n "\*Fine\*\|\*I'm fine"` across the manuscript is unchanged by this pass. Rx has **one turn** in Ch.11 and he does not speak in it: Vexx's *"You've gone quiet"* (¶208) gets **nothing back**, and the cursor goes on. A silence is not a denial; the cap is untouched and Ch.13's mandated break is unaffected. |
| **5** | **The tidying gesture is not everyone's** (squaring to an edge, the quarter-turn) | **CLEAR as to the gesture**, and I confirm the audit's *"Ch.11 adds zero"*. **One word-level collision the audit's grep could not have caught, examined and cleared:** ¶206, *"the tab struck on **square**"*. It matches `squar` but it is not the gesture — it is a man applying a tamper seal straight so that it looks untouched, inside a concealment procedure. Functional, not a fidget, and it carries the opposite meaning (hiding, not fussing). **Recorded so the next pass does not find it as new.** |
| **6** | **Hands flat on a surface is Ch.1's gesture** | **CLEAR. Zero.** Grepped `hands flat / flat on the / palms flat / both hands on`: Ch.11 returns nothing. |
| **7** | **Generic-person manner attribution (flat-man, ceiling 3)** | **CLEAR at 1** — inside the author's own measured range (0 · 2 · 1 · 0 · 0), unchanged by this pass. The single instance is ¶42's *"like a boot that has done a great deal of standing"*, which is an **object**, not a generic person, and is the chapter's anchor image. Not touched. |

---

## 3. THE REPEAT-OFFENCE LOG — Ch.10's fixes, searched for by name in Ch.11

Per the skill's §1.2c. Every violation the Ch.10 pass fixed, looked for **specifically**, by
character and by construction.

| Ch.10 fix | Ch.11 verdict |
|---|---|
| **J3** — the spoken *N-of-M* (*"four findings… three of them"*) | **FOUND AGAIN in a different coat** — not *N*-of-*M* this time but the clipped count-and-negate (**D6**). The row is right that the *shape* varies and the *habit* does not. |
| **J5 / J7** — *"That's not X. That's Y"* on a new mouth | **FOUND AGAIN, twice** (**D1**, **D5**). Removed from Jameson in Ch.10; arrived on Gaia in Ch.11, one chapter later. |
| **J2 / J6** — Dessen's re-issued question on another mouth | **CLEAR.** Gaia's ¶170/174/178 are **three different questions** (*which / who / whether-you-have*), not one question re-issued with a word changed. Checked against her ¶44/46/48 exchange too — *"Whose is it?" / "Nobody's." / "Somebody's."* is a disputed fact, not a re-issue. |
| **J4** — the secondary count-echo (*"twice… both times"*) | **CLEAR.** No M-then-all-of-M anywhere in the chapter. |
| **D1** — the anaphoric pair protecting Dessen's triple | **CLEAR of her technique.** Ch.11 has two anaphoric pairs/triples (¶154 *"Nobody asked you to, nobody told you to"*; ¶192 *"not in a corridor, not on a net, not after…"*) — neither is a question, neither re-issues anything, and both are ordinary emphatic parallelism. Cleared on the Ch.10 precedent. |
| Vexx's term-correction cap (2/5 spent, 0 spent in Ch.10) | **FOUND AGAIN, three times — and in somebody else's mouth** (**D2**, **D3**, **D4**). See §5 for the cap arithmetic. |

**Recommendation for `character-bible.md`:** offence #3 should now be recorded as having a
**repeat offender** (Gaia, Ch.8 and Ch.11), and offence #2's note should be extended from
*"Ch.8, and again Ch.9"* to include **Ch.10 (Jameson ×2) and Ch.11 (Gaia ×2)** — four
consecutive chapters, four different mouths, which is the same profile as #3 and argues for
promoting it to the same standing. Not actioned here (one-file edit scope).

---

## 4. DEVICE-BLEED AUDIT — every speaker × every reserved device

Four speakers (Gaia, Vexx, Goliath, Echo) against the **full** one-device map, not the predicted
pairs. `—` = device absent. **HIT** = fixed above.

| Reserved device (owner) | GAIA | VEXX | GOLIATH | ECHO |
|---|---|---|---|---|
| Counting **ALOUD** / N-of-M / sequence (**Spector**) | **HIT → D6.** Four residuals cleared below | clean — no spoken count | clean | clean |
| The private, silent tally (**Vexx / Rx**) | **near-miss, kept deliberately** — ¶152 *"You worked out what each of us would cost you. In your head, in order."* She is not counting; she is **naming his device back at him**, and it is his. See the note below | **his own** — and the coda is it: the inventory moved into the trauma pack, silent, counted for nobody | — | — |
| Compulsive narration / never letting a silence stand (**Echo**) | clean — she is the opposite, and the chapter says so (¶198–200, a silence she refuses to fill) | clean — ¶150, ¶190 he lets two silences stand | clean | **his own**, and correctly: ¶22 arrives mid-thought, in a run-on, and is shut off |
| Naming/labelling, then using the name as agreed (**Echo**) | *"your one"* (¶188) reused once at ¶192 — **examined, cleared**: *one* is a quantity used as emphasis inside a single breath, not a coined name for a thing. *"the Gullet"* is Echo's and the narration polices it (¶28) | — | — | **his own** — *the Gullet*, ¶22, and ¶28 is the device's own punchline |
| Too-quick denial / reflex deflection (**Rx**) | clean | clean — his refusals (¶172, ¶176) are **slow and repeated**, the inverse | clean — ¶56's *"No."* is examined below | clean |
| Body-check question before content (**Bastion**) | clean | clean | clean | clean |
| Restate-then-disagree; *"No."* as a sentence (**Paladin**) | **HIT → D3** (the *"we"*). No restatement anywhere | four bare *"No."* / *"That's a no."* — cleared on the Ch.9 and Ch.10 precedent: answers under pressure, no restatement | ¶56 *"No,"* — **cleared, and it is the inverse of Paladin's.** Paladin restates your position and *then* refuses. Goliath refuses **before the question exists**, which is his all-or-nothing on people, and the next two lines make the joke of it (*"You don't know what I was going to ask you." / "I know what everybody in this corridor has been asked for a week."*) | — |
| Correcting the terms of a question (**Vexx**, capped) | **HIT ×3 → D2, D3, D4** | **his own — 0 spent in Ch.11.** See §5 | clean — checked against the Amelia note's *"Goliath picked up Vexx's term-correction shape, twice"*. ¶64's *"isn't doing it for air"* is cleared below | — |
| Pre-empt the objection and improve it (**Jameson**) | clean | clean | clean | — |
| **"That's not X. That's Y"** / corrective reframe (**Zeus**) | **HIT ×2 → D1, D5.** One retained — see below | clean | **cleared** — ¶64 *"Whoever's doing it isn't doing it for air. You want air, you use a chair… A boot at the bottom is what you use when you want to come through it fast and not stop."* The substitute arrives **three sentences later, through method**, not in the next clause, and the reasoning is craft-first: this is his own device (trade vocabulary applied to a motive) and the best cover-the-name line in the chapter | — |
| Withhold until useful / answer late (**Hollow**) | clean | **cleared** — he withholds continuously, but Hollow's device is **answering forty minutes late with no preamble**; Vexx answers **immediately and in the negative**, twice. Opposite timing | clean | — |
| Fact-then-silence, no modals (**Voss**) | **cleared, and the contrast is the point** — Gaia gives a fact and then **demands a decision inside a window** (¶82, ¶106, ¶192). Her modals are everywhere | clean — *"It shouldn't be propped"* (¶72) is a modal Voss would not use | clean | — |
| Same question three times, one word changed (**Dessen**) | **cleared** — see §3 | clean | clean | — |
| Involuntary self-echo (**Merrick**) | clean | **cleared** — ¶184 *"That's a no."* repeats **her** three words, not his own. A confirmation, and the chapter's dryest beat | clean | — |
| Naming what she noticed, unasked (**Aglaope**) | **cleared, and this is the tightest pair in the chapter.** Her card's split holds exactly: Aglaope states facts **about you**, Gaia states facts **about the world**. Every observation Gaia makes here is about a *room* — until ¶152, which is about **him** — and ¶152 is explicitly framed as a **theory she is advancing** (*"Here's what I think"*), not a thing noticed. Aglaope never prefaces. The frame is what keeps them apart and it is already on the page | — | — | — |
| Fact → ask → clock; *"your call"* (**Gaia**) | **her own**, and it lands four times (¶82, ¶106, ¶116, ¶192). ¶192 is the mapped form verbatim and is untouched | clean | clean | — |
| Trade vocabulary for ethics (**Goliath**) | **near-neighbour, logged, not actioned** — ¶152's *"what each of us would **cost** you"* / *"I'd **put money** on"* is commercial idiom applied to loyalty. Goliath's band is **trade craft** (ordnance, structures, load-bearing walls), not money, and the cost-accounting register here belongs to the institution she is describing. Cleared | clean | **his own**, ¶64 and ¶68 (*"Coffee's an insult"* — a moral verdict in trade vocabulary, and his registered coffee feud) | — |
| The pause before agreement (**Requiem**) | clean — she never pauses | clean | clean | — |
| Grammar correction (**Corwin**) | clean | clean | clean | clean |
| Self-interrupting over-explanation (**Reyes**) | ¶124 *"Doesn't that—"* is **interrupted by Vexx**, not by herself. Cleared | ¶96 and ¶100 are **cut off by her**. Cleared | clean | ¶22 is **shut off by Vexx**. Cleared | 
| Interviewing the people assessing him (**Ives**) | clean | clean | clean | clean |
| Standing when anyone enters (**Beck**) | clean | clean | clean | — |
| **The why-question** (**Zeus never**) | *"Why?"* ×1 — **legal**, she is not Zeus | asks no why | asks no why | asks no why |

### The one Zeus-shaped line I kept, and why

**Gaia, ¶110: *"I don't want the door shut because you've ordered it." / "I want it shut because
it's a bad door."***

By the strict surface test this negates and substitutes. I kept it, deliberately, and the
distinction is real: **Zeus's device re-categorises a thing** (*"That's not caution. That's a man
rationing himself"*) — it tells you what something **is**. ¶110 states **two of her own
preferences**, in parallel, with the same subject and the same object; nothing is being
re-labelled and no position of his is being corrected. It is also the thesis of the chapter in
two sentences, and the line the whole argument has been walking toward since ¶72.

With D1 and D5 removed, this is the **only** negate-then-state construction left in her mouth —
which puts a non-owner at one, where the Ch.10 pass allowed a non-owner one and the owner two.

### The private tally, and why ¶152 stays

**§THE ONE CARVE-OUT** warns: *"If a tally is ever said aloud to another character, it has
crossed over."* ¶152's *"You worked out what each of us would cost you. In your head, in order.
I'd put money on where I came."* is the closest thing in the chapter and I examined it hard.

It stays, for three reasons. **(a) She is not keeping the tally — she is accusing him of keeping
one**, and the tally she describes is *"in your head"*, which is the device's definition
(*counted for nobody, never spoken, and its whole meaning is that the man keeping it will not
admit he is keeping it*). The carve-out protects Vexx's private count; this line is the only
moment in the book where another character tells him it exists. **(b) There is no number in it,
and nothing is performed** — the operative narrowing is *counting performed as competence, for a
room*, and this is an ordinal accusation with no numeral. **(c) It is the 70/30 beat**, and the
brief's instruction is explicit: do not make her more right or less certain. Removing it would
remove the half she has right.

**Logged** so a later pass does not re-find it as new.

### Counting residuals examined and cleared

- **¶32** *"I shut it the night before last, and it was open again before breakfast, and I shut
  it yesterday, and there it is."* — a sequence of occasions with **no number and no M**. Per
  the Ch.10 precedent on triads. Her clock, her device.
- **¶106** *"four minutes ago"* and **¶196** *"about eleven"*, *"five months"*, **¶164** *"for a
  year"* — **clocks and durations**, explicitly licensed by her card (*fact → ask → clock*) and
  cleared on the Ch.10 precedent for Rx's *"ninety words a minute"* / *"twenty-two minutes"*.
- **¶16** *"the pad in here, the deck, the water, a mess hall full of people"* and **¶192**
  *"not in a corridor, not on a net, not after…"* — unnumbered lists. Applied literally,
  *cataloguing* would make the book unwritable.
- **¶154** *"All of us"* / *"which of us goes to command first"* — a set and an ordinal, no count
  performed.
- **¶166** *"One of the jobs we've run"* — an indefinite partitive with **no M stated**. Not the
  *N-of-the-M* construction, and it is the chapter's reveal sentence. Untouched.
- **¶196** *"laughed once a night"* — a frequency. Unavoidable English.

### Shared reach

No unusual word is reached for by two characters in this chapter. The nearest approach is the
word **door**, which belongs to everybody by design. *"the boot comes back"* is said by Gaia
(¶82, ¶86) and then by Vexx (¶84) — deliberate, it is the argument being handed back and forth,
and it is three lines apart.

---

## 5. VEXX'S CAP — the arithmetic this pass changes

| | Before | After |
|---|---|---|
| Book total, Vexx's term-correction | **2 / 5** (both in the author's chapters) | **2 / 5** |
| Firings in Ch.11 | **3 — all of them in GAIA's mouth** | **0** |

A capped device spent by a character who does not own it is the worst case available: it burns
the cap **and** blurs the owner. All three are gone and **nothing was charged to the cap** —
Ch.11 spends zero, and the ceiling is intact for the chapters that need it.

**One near-miss, logged and not counted.** ¶46–48, *"Nobody's." / "Somebody's."* Vexx negates her
possessive and substitutes another. I am not counting it as a firing: the device is *editing the
vocabulary of a question*, and this edits a **claim of fact**, not a word — he is disagreeing
with her, not correcting her. Recorded so the next pass has the reasoning rather than the
question.

---

## 6. GESTURE BLEED — what characters DO

Grepped the **whole manuscript** for this chapter's physical business, by verb, and counted per
character.

| Business | Ch.11 | Characters in Ch.11 | Book-wide census | Verdict |
|---|---|---|---|---|
| Head over / tilted | 1 (¶130, Gaia, *"the way she did on a ridgeline"*) | **Gaia only** | Ch.11 ×1. Ch.10's only neighbour is an explicit **negation** (*"He did not tilt his head"*) | **CLEAR — one character, and the one other appearance in the book is the gesture being withheld.** Hers, tied to her recon work. Keep |
| Arms crossed / back to the wall / shoulder off the wall | 3 (¶10, ¶16, ¶82) | **Gaia only** | her card: *"arms crossed, chair angled toward the door"* | **CLEAR and load-bearing.** ¶82's *"took her shoulder off the wall, finally, one step, which from her was a shout"* is the best use of it in the book |
| Weight on the foot nearest the stair | 1 (¶10) | **Gaia only** | Ch.11 only | **CLEAR.** The one character in the book whose body is a device |
| Squaring / quarter-turn (**offence #5**) | **0** (one word-level collision at ¶206, cleared in §2) | — | Ch.2 ×1 (author, Zeus) · Ch.5 · Ch.6 ×4 · Ch.8 ×2 · Ch.9 ×3 | **CLEAR.** Ch.11 adds nothing to the ten-instance excess |
| Hands flat on a surface (**offence #6**) | **0** | — | Ch.1 ×1 (author) · Ch.6 · Ch.7 | **CLEAR** |
| *put a hand in the small of his back* (old N-09) | **0** | — | Ch.6 (gardener) · Ch.8 (Goliath) | **CLEAR** — Ch.11 did not make it a third |

### ⚠️ One gesture-bleed finding, LOGGED AND NOT FIXED — and it is for the next pass to decide

**¶186: *"She stood there **turning it over** in front of him without hurrying."***

Book-wide census of *turning it over* as the **deliberation** verb:

| Chapter | Who |
|---|---|
| Ch.1 ¶35 | **Vexx** (*"replay… turning it over and over"*) — author |
| Ch.2 ¶141 | **Vexx** — author |
| Ch.2 ¶253 | **Vexx** (*"**the way he turned over everything eventually**"*) — author, and this is the line that **registers it as his**, by name |
| Ch.4 ¶11 | **Vexx** — author |
| Ch.4 ¶33 | **Vexx** — author |
| **Ch.11 ¶186** | **GAIA** — pipeline |

**Five instances, all the author's, all on Vexx, with his own prose explicitly naming it as his
characteristic habit — and Ch.11 hands it to Gaia.** This is the exact profile of the tidying
gesture at instance two, before it reached five characters.

**Why I did not fix it:** (a) it is **narration**, and this brief puts narration out of my lane
for good metric reasons; (b) it is **two characters**, below the skill's three-character
threshold; (c) it is genuinely load-bearing where it sits — the clause after it (*"he watched
her find the edges of it, find how small it was, not say so"*) is built on the object-handling
conceit and would have to go with it.

**My recommendation, for whoever owns narration next:** register it in `character-bible.md` as
**Vexx's**, so that a third user is caught. If it is to be recast, it is cheap and
metric-neutral — the sentence is ~30 words and a two-word swap moves neither the median nor the
`>=40w` share, and there is no em-dash in the clause being changed. **Do not let a third
character have it.**

---

## 7. COVER-THE-NAME TEST

**Method as Ch.9/Ch.10.** Every quoted turn and every italic interface turn stripped of tag,
beat, paragraph and turn-order, read cold **against the whole twenty-voice cast**.
**DISTINCT** = lands on exactly one character on first read. **WEAK** = lands only once
turn-taking is restored. **INDISTINCT** = lands on nobody, **or on the wrong character because
it is wearing somebody else's device.**

**82 attributable turns** (80 quoted + 2 italic interface), against style_check's 131 dialogue
lines (its splitter counts sentences; turns are the only unit the test runs in).

| | DISTINCT | WEAK | INDISTINCT | Strict | Tolerant |
|---|---|---|---|---|---|
| **Before** | 37 | 41 | **4** | 45.1 % | 95.1 % |
| **After** | **41** | 41 | **0** | **50.0 %** | **100 %** |

| Character | Turns | Distinct | Weak | Indistinct (after) |
|---|---|---|---|---|
| **Gaia** | 38 | 26 | 12 | 0 |
| **Vexx** | 38 | 11 | 27 | 0 |
| **Goliath** | 3 | 3 | 0 | 0 |
| **Echo** | 3 | 2 | 1 | 0 |

**Read the WEAK column before reading the DISTINCT one.** 41 WEAK is high and it is **correct**
for this chapter. Ch.11 is a two-hander in stichomythia: twenty-two of its turns are five words
or fewer (*"Yes." / "For days." / "Yes." / "So." / "No." / "That's a no."*), and a two-word turn
cannot carry a voice signature — it carries the *rhythm*, which is the chapter's whole method,
and the outline asked for an argument that *"goes on about four exchanges too long."* Trying to
make *"Yes."* distinctive would destroy the scene. I made no attempt.

**The thing to take from this table is the INDISTINCT column, which went 4 → 0.** All four were
INDISTINCT **because they landed on the wrong character** — three on Vexx, one on Zeus — while
reading perfectly well in the moment.

### ⚠️ And the finding the table cannot show

**Two of the six bleeds scored DISTINCT before the fix.** ¶152 and ¶196 are long, vivid,
unmistakably-Gaia turns with somebody else's device **buried inside them** — the Zeus pivot in
the middle of her speech, the Spector count in the middle of her anecdote. The test scored both
as clean, correctly, because **the test measures whether a line is distinctive and never whose
it is.** The voice-dna note on the Amelia Lesson says exactly this and it is right: on this
chapter, **the separate device-bleed scan found 50 % more defects than the Cover-the-Name Test
did**, and the two it found alone were the two in the chapter's most important speeches.

### Goliath — the brief asked me to verify the rest of him. Verified.

Three turns, three DISTINCT, and he is the cleanest voice in the chapter.

- **¶56 *"No,"*** — cleared above. Pre-emptive refusal, the inverse of Paladin's.
- **¶60 *"I know what everybody in this corridor has been asked for a week." / "Not mine."***
  — *"Not mine"* is ownership, which is his axis (*the job, and whether it was done honestly*),
  and the untouched beat between them (*"pulled a face at it that had nothing to do with either
  of them, or with the door, and was entirely about the cup"*) is his registered coffee feud
  doing real work.
- **¶64** — his best line in the book and the only line in the chapter that **advances the plot
  through craft**. Trade reasoning (how you would actually prop a door, and why) applied to a
  motive, arriving at *"you want to come through it fast and not stop."* No rule mentioned
  anywhere, which is the Goliath/Paladin split holding.
- **¶68 *"Coffee's an insult," to nobody*** — a moral verdict in trade vocabulary, delivered to
  no one, and he leaves. His marker schedule lists Ch.9/18/25; this is a one-line echo and I
  judge it correct rather than over-spent (the feud is funnier for being continuous).

**One note for the record:** he never asks his *one question and waits*, which is his
syntax fingerprint. In a three-turn appearance that is right — the wait belongs to Ch.8's
*"Do you want the third one, when he gives it to me?"* and spending it here would cheapen it.
**Nothing added.** His silence after ¶64 (*"Neither of them had anything to say to that, and
Goliath did not appear to have expected any"*) is the same behaviour from the other end.

### Echo — untouched, as instructed. Verified correct.

¶22 arrives **mid-thought** (*"arriving on the net mid-thought, as he arrived everywhere"*), in
one unbroken run-on, in the present tense, **names** the corridor, is **shut off** rather than
finishing, and ¶28 is the device's punchline (*"Nobody had ever agreed to call the corridor the
Gullet"*). **minuted** is left exactly as it stands: naming and minuting are both his, it is
deliberate British institutional idiom, and `style_check.py`'s dialect gate does not see it
because it is not in the `-ise`/`-our` families — so it is not at risk from the gate either.
¶26's *"Off, Echo said, and was"* is the best joke in the chapter and it depends on him being
the character who cannot stop talking.

---

## 8. SUBTEXT, EXPOSITION, NATURAL SPEECH — audited, nothing to do

**Subtext.** `outline.md` Ch.11 beat 2 defines it: *"escalation into something that is obviously
not about the door and that nobody names."* The chapter executes this and **nobody names it** —
not once. Surface topic: a fire door. Real topic: whether Vexx trusts the people he commands.
The techniques are already there and already the right ones: **displacement** (¶72–86, the whole
argument conducted about a regulation), **over-specificity** (¶116, *"Whose boot is it, though.
Genuinely."* arriving immediately after the real subject surfaces), **contradiction** (¶126, he
says *"It does, yes"* and then goes and removes the boot, doing the thing rather than saying the
sentence), and **silence** (¶150 and ¶190, two unanswered beats where the gap is the dialogue).
**Zero `FLAT_DIALOGUE` flags.** No subtext was added — per rule 7, the defined layer gets
texture, not a new layer, and this one did not need texture.

**Exposition.** Zero dumps. No *as-you-know-Bob* is available — the door is **never explained**,
by design (outline: *"The door is never explained"*), and neither is the relay hall, the jungle,
or the job. Two long turns examined for lecture mode and both cleared: **¶64** (Goliath) is
four sentences of deduction that is **new to both other characters** and changes the scene;
**¶152** (Gaia) is seven sentences of accusation, motivated entirely by her own grievance, and is
the chapter's turn. Neither is information delivered for the reader.

**Natural speech.** Already at the ceiling and I added nothing. Present before this pass and
preserved: **interruptions** ×3 (¶96, ¶100, ¶124, all em-dash-at-break — and note I could not
have added one even if it needed it), **backchanneling** ×6 (*"Yes." / "Yes." / "So." / "It does,
yes"*), **false start** ×1 (¶24 *"Echo. Off."*), **repetition under pressure** (¶134–136
*"That's good." / "That's very good."*, ¶182–184 *"That's a no." / "That's a no."*), and the
**refused response** ×2 (¶150, ¶190).

**Tags.** Audited, nothing to change. 17 attributions, **all of them `said`** — zero creative
speech verbs, zero adverbs in tags (the §4 zero-tolerance row), zero non-speech-act verbs. Six
carry character-revealing beats rather than plain attribution (*"to his back"*, *"to nobody"*,
*"with an enormous satisfaction she made no attempt to cover"*, *"without heat, which was
worse"*, *"She said it flatly, without any interest in whether it landed"*, *"because he did not
answer questions any other way"*). That is already the beats-over-tags ratio the skill asks for,
and in a chapter this dialogue-dense the plain `said` is doing necessary invisible work.
**Nothing replaced, nothing removed.**

---

## 9. GATES — `python3 tools/style_check.py`, run from the book folder

```
Ch11  2170 words | simile 2.3/1k | adverb 5.5/1k | em-dash 25 (11.5/1k)
      rhythm: and 22.1/1k | comma 72.8/1k | somebody/nobody 5.1/1k
      breath (narration): 37 sentences | median 18 | >=40w 16.2% | <=6w 21.6% | dialogue lines 131 (3.54:1) | dialogue and 22.5/1k | gloss 0.0/1k | question marks 1.8/1k | adverb 8.4/1k | and 21.6/1k | flat-man 1
   VOICE-MATCH: ADVERB narration 8.4/1k < 10.5 (voice-match FLOOR); AND narration 21.6/1k > 19.5 (voice-match CEILING — §THE SEAM)
```

### The three numbers the brief asked me to speak to explicitly

| | Before | After | Moved? |
|---|---|---|---|
| **em-dash count** | 25 | **25** | **No. Not one added or removed.** |
| **em-dash /1k** | 11.49 | **11.55** | +0.06, from the chapter being 6 words shorter. **Headroom: 1.04 em-dashes** (ceiling 12.0 allows 26.0), against 1.11 before. Net cost **0.07 of one em-dash** |
| **narration median** | 18.0 | **18.0** | **No.** Narration block byte-identical |
| **narration `>=40w`** | 16.2 % | **16.2 %** | **No.** |
| **narration `<=6w`** | 21.6 % | 21.6 % | No |
| **narration adverb** | 8.4/1k | 8.4/1k | No — the floor breach is **unchanged and still open** |
| **narration `and`** | 21.6/1k | 21.6/1k | No — the ceiling breach is **unchanged and still open**, as instructed |
| **flat-man** | 1 | 1 | No |
| **question marks** | 4 (1.8/1k) | **4 (1.8/1k)** | **No.** None removed |
| word count | 2,176 | 2,170 | −6 |

**Dialect: 0, confirmed.** `style_check.py` emits no `DIALECT` line for any chapter in the
manuscript, Ch.11 included — the gate is clean book-wide and this pass introduced no
non-US spelling. (`minuted` is deliberately kept and is invisible to the detector, which matches
only the `-ise`/`-our`/`-re` families.)

**`grammar_check.py`: clean.** **`voice_wear_check.py`: clean — no retired phrases, no device
over cap.** **Repeated-phrases gate: clean. Motif cap: clean.** The book-level count is
unchanged at 12 flagged issues — **this pass introduced none and closed none**, which is the
correct outcome for a dialogue-only pass.

### The two live Ch.11 breaches are both NARRATION and both still open

They were open before I started and they are not mine to close — `and` 21.6 against a 19.5
ceiling and adverbs 8.4 against a 10.5 floor. The brief is explicit that the `and` fix belongs
to a later pass and that the two interact. **Recorded here so the next agent does not read
"dialogue pass complete" as "metrics clear."**

---

## 10. HANDOFF TO `hook-craft` — what I changed at ¶6, precisely

You own whether that line opens the chapter. I owned whose device it was. **Build on this; do
not undo it.**

**The line now reads:**
```
“—it’s a hole with a hinge on it,” Gaia said. “A door does something.
 This one stands open and I lose the stair.”
```

1. **I removed the *"it isn't X"* clause outright** — one of the five elements your N-12
   duplication-of-Ch.8 finding is built on. Ch.8 ¶6 is *"—because the water's wrong," Goliath
   said. "**It isn't the grounds.**"*; Ch.11 no longer rhymes with it on that element. **Four
   elements of the five remain** for you: em-dash-initial fragment · mid-argument · cell member ·
   mundane station infrastructure.
2. **I did not touch the em-dash-initial framing**, per the brief, and I invested nothing in it.
   The opening quotation mark, the leading em-dash and the `Gaia said` tag are all still there
   and all still yours to remove. **If you drop the leading em-dash you buy back a full unit of
   em-dash headroom** (25 → 24, i.e. 11.1/1k), which the chapter could use.
3. **The content is now load-bearing in three places and is cheap to relocate.** If you enter on
   Gaia's *position* instead of her sentence (the audit's suggestion — weight on the foot nearest
   the stair, which is already at ¶10), the three beats of this line can move downstream intact:
   the **image** (*a hole with a hinge on it*), the **functional declarative** (*A door does
   something*), and the **operational loss** (*I lose the stair*). Only the third is new from me,
   and it now plants the stair for ¶16 and ¶200 — **keep it somewhere in the first twenty lines**
   or those two payoffs arrive cold.
4. **Do not reintroduce a negate-then-substitute construction anywhere in Gaia's mouth.** That
   is the whole point of D1 and D5, and the opening is where it will be most tempting, because
   the shape is a very good way to open a chapter. It belongs to Zeus.
5. **One em-dash of headroom, total.** 25 of 26. If you add one anywhere, you must remove one.
6. **The closer (¶212–214) is untouched** and is entirely yours — it is narration, so it was out
   of my lane, and your N-12 fix (end on the room, cut the *"he said it once, out loud, in the
   room"* framing) does not collide with anything I did.

---

## 11. FOR THE ORCHESTRATOR

1. ⚠️ **§STANDING OFFENCE #3 has now recurred in FOUR consecutive chapters, and Ch.11 is the
   first repeat offender** (Ch.8 Gaia · Ch.9 Zeus/Vexx · Ch.10 Jameson · **Ch.11 Gaia again**).
   The offence row's own thesis is confirmed a fourth time: it landed in a *different*
   construction (count-then-negate rather than N-of-M) on a *returning* mouth, and it was
   invisible to the Cover-the-Name Test. **Every dialogue dispatch must keep carrying the rule
   in the explicit form the Ch.9 report asked for.**
2. ⚠️ **Promote offence #2 to the same standing.** *"That's not X. That's Y"* has now gone
   **Ch.8 → Ch.9 → Ch.10 (Jameson ×2) → Ch.11 (Gaia ×2)** — four consecutive chapters, four
   mouths, nobody on a watch-list. The bible still records it as *"Ch.8, and again Ch.9"* with a
   logged-bleed note. The note's rule (*no NEW character may be given this shape*) is being
   broken every chapter by a different new character, which is the #3 profile exactly.
3. **`character-bible.md` edits recommended** (not actioned — one-file scope): record Gaia as a
   **repeat offender** on #3; extend #2's "Broken in" column to Ch.10 and Ch.11; add
   ***"turning it over" = Vexx's deliberation verb*** to the one-device map (5 author instances,
   named as his in his own prose at Ch.2 ¶253, now 1 pipeline instance on Gaia — see §6);
   record ***"the tab struck on square"* examined and cleared** under #5 so it is not re-found.
4. **Vexx's term-correction cap stands at 2/5 and Ch.11 spends none.** Three firings were
   removed from the wrong mouth. The cap was never charged.
5. **`ENTITY_STATE.yaml` CF-21 / N-09 can be closed** — with the note that it was **three
   findings and the chapter had six**.
6. **Ch.11's two open style breaches are narration** (`and` 21.6 > 19.5; adverbs 8.4 < 10.5) and
   remain for the pass that owns them. The adverb floor is the one worth real attention: 8.4 is
   the **highest** narration-adverb figure of any pipeline chapter in the book and it is still
   below the floor, which says the problem is systemic rather than local to Ch.11.
7. **N-11 (the *"Vexx waited for the rest of it / There was no rest of it"* structure duplicated
   from Ch.6) is narration and I did not touch it.** For the record, Ch.11's dialogue contributes
   **one** instance of *"the rest of it"* — ¶192's *"What you do with the rest of it is your
   call"*, which is Gaia's mapped device and must not be recast. The other two (¶192's *"coming
   back for the rest"*, ¶198's) are the ones available to a later pass.

---

## 12. COVER-THE-NAME TEST: FINAL

| Conversation | Verdict |
|---|---|
| **¶6–20, the acoustics complaint** (Gaia/Vexx) | **PASS.** Was the chapter's weakest stretch and carried two bleeds; Gaia now owns every turn in it on her own axis |
| **¶22–28, Echo on the net** | **PASS.** The single most identifiable voice in the chapter, untouched |
| **¶30–50, the boot** (Gaia/Vexx) | **PASS**, with the WEAK caveat above — the short-turn volley is rhythm by design |
| **¶54–70, Goliath** | **PASS, strongest in the chapter.** Three turns, three distinct, zero bleed |
| **¶72–112, the regulation** (Gaia/Vexx) | **PASS.** One bleed removed (¶94); ¶110's negate-then-state retained and reasoned |
| **¶116–140, the laugh** | **PASS.** ¶138 (*"I'm standing here holding a boot"*) is Vexx's registered flat-physical-fact break and is the best cover-the-name line he has in the chapter |
| **¶144–162, the turn** | **PASS.** One bleed removed from inside ¶152; the 70/30 verified intact |
| **¶166–192, the smallest true thing** | **PASS.** Gaia's three no-question-mark questions now rhyme with ¶62's; ¶192 is her mapped device verbatim |
| **¶196–202, the laugh through the wall** | **PASS.** One bleed removed (¶196); the chaos marker and the *"It's a bad door"* payoff untouched |
| **¶208, the coda** (Vexx → Rx, italic) | **PASS.** Private channel, correct register, and the silence that answers it leaves Rx's cap untouched |

**10 conversations, 10 PASS, 0 INDISTINCT lines remaining.**

**Remaining concern, one, and it is not a defect:** 41 of 82 turns are WEAK, and that is the
right answer for a stichomythic two-hander. Any future pass tempted to "fix" the WEAK column by
making *"Yes."* and *"So."* distinctive will destroy the scene the outline asked for. **Recorded
here so that temptation arrives pre-answered.**
