# Continuity Audit — Valkyr: Book One, Chapters 1–8

**Date:** 2026-09-09
**Scope:** full manuscript as it stands — `chapter-1.md` … `chapter-8.md`, 27,815 words
**Audited against:** `../../../SERIES-BIBLE.md` (outranks all), `../../CLAUDE.md`, `outline.md`,
`character-bible.md`, `foundation.md`, `ENTITY_STATE.yaml`
**Method:** all eight chapters read in full and in order; databases cross-checked in both
directions (manuscript → YAML and YAML → manuscript); five standard audits plus the four
special tests the brief specifies (four-year fix, Ch.8 deployment count, Ch.8 information
routing, memory-ladder integrity).

> **Note on file churn during the audit.** `chapter-2.md` and `chapter-7.md` were edited on
> disk by other agents while this pass was running. Both were re-read at their current state
> and the findings below reflect that state. The Ch.2 change removed the last surviving
> "four-month" line; the Ch.7 change was revision 4 (evaluator F2/F3). Nothing in this report
> reverses either.

**Totals:** 1 BREAKS THE BOOK · 13 needs a fix · 14 worth a look · 9 deliberate-and-fine

---

## 0. VERDICT ON THE FOUR SPECIFIC TESTS

### 0.1 The four-year fix — **TOOK, EVERYWHERE. Verified clean.**

`grep` across all eight chapters returns **zero** instances of "four months", "four-month", or
any residue of the old span. The chain is coherent end to end:

| Chapter | Line | Status |
|---|---|---|
| Ch.1 | "For four years after that, he did what people do." | ✔ |
| Ch.1 | "The second knock came four years to the day." | ✔ |
| Ch.1 | "the first order Rx had given him in four years" | ✔ |
| Ch.1 | "sitting in that gray room four years into mourning" | ✔ |
| Ch.1 | "*I've been retired for four years.*" | ✔ |
| Ch.2 | "four years turning over an empty casket in his mind" | ✔ |
| Ch.2 | "no **four-year** gap of grief first" | ✔ (this was the last hold-out; now correct) |
| Ch.2 | Zeus: "How long have you been out?" / "Four years." | ✔ |
| Ch.2 | "a gray room four years into a grief he hadn't known how to carry alone" | ✔ |
| Ch.3 | "muscle memory outlasting four years of retirement" | ✔ |

**The consequences that follow from the gap also hold, and they were the real risk:**

- **How long Rx's AI waited.** Ch.1: "leaving him there, alone, the way he'd apparently
  already been sitting for **years**". Ch.1: "*We attempted integration with three other
  candidates before we located you.*" Three failed integration attempts is a four-year-shaped
  process, not a four-month one. ✔
- **How long the retirement ran.** Ch.6: "He had spent **four years** learning to leave no
  shape behind him anywhere." Ch.8: "somewhere in the middle of **the four years he did not
  talk about**." Both written after the fix and both correct. ✔
- **Jameson's consolidation.** Ch.2 gives him "a program he'd built his entire career on top of
  a lie about" — four years of building, not four months. ✔

**Two dead lines cited by `ENTITY_STATE.yaml` CF-01 as still-conflicting no longer exist in
the manuscript** — `ch-03` "a door that had been closed for four years had just shifted" and
`ch-05` "Richard Jameson slept, as he had for four years…". The second of those was a
**Jameson-POV sentence**; it has been removed from Ch.5 and the POV lock is now intact for the
whole drafted book. Recorded here so nobody restores either line from the YAML.

**One residual wobble, in locked Ch.1, report-only:** see §1, C-01.

### 0.2 Ch.8 deployment count — **the outline is wrong, the prose is safe.**

Ch.8 is the cell's **fifth** deployment at the earliest, not its fourth.

| | |
|---|---|
| Ch.3 | "*First deployment as a full cell*" → **#1** |
| — | second deployment never depicted or dated |
| Ch.4 | "The friction with Paladin came on the cell's **third deployment**, six weeks later" → **#3** |
| Ch.5 | "a simple monitoring assignment", falls after Reyes → **#4** |
| Ch.8 | "a corridor argument **seven weeks earlier**" pins it after Ch.5 → **#5 or later** |

`outline.md` §Chapter 8 Premise says *"The cell's **fourth** deployment"* — and contradicts
itself four lines down in its own beat 5: *"Paladin holds the line for the third time in
**five** missions."* Five is the correct arithmetic and it is what the drafted chapter
executes ("It was the third time Paladin had said no in a room like that" — Ch.2 recruitment,
Ch.4 Reyes, Ch.8 Merrick).

**Ch.8 never numbers the deployment on the page, so no chapter file needs editing.** Fix the
outline's Premise line. Logged as `CF-07`.

### 0.3 Ch.8's information-flow test — **PASSES. This is the cleanest thing in the book.**

Spector's observation reaches Vexx exactly once, secondhand, through Goliath, in a corridor,
and the routing is airtight in both directions.

**Nothing earlier tells him.** Everything Vexx knew about Rx's malfunction before Ch.8 came
either from Rx directly (Ch.1 half-syllable catch; Ch.3 treeline; Ch.4 "the shape of a
refusal", and Rx *naming* Jameson's name as one of the two triggers) or from Vexx's own
observation (Ch.2 Rx's silence; Ch.4 "a private tally of which kind of quiet"). **No character
outside Vexx has previously noticed anything about Rx on the page.** Spector's report is
therefore the first *external corroboration* in the manuscript — new in kind, not a repeat.

**Nothing later assumes more.** Goliath gives two of three words ("'Unstable.' And
'refused.'"), asks *"Do you want the third one, when he gives it to me?"*, and Vexx does not
answer — "and waited, and went on waiting, past the point where a man expects an answer and
some distance past the point after that." The third word is withheld and nothing in the
remaining text reaches for it.

**The one thing that slightly softens it** is in Ch.5, not Ch.8 — see §3, W-03. Recorded in
`ENTITY_STATE.yaml` as `secrets.rx-runs-hot-on-certain-words` with an explicit constraint that
no later chapter may assume Vexx holds word three.

### 0.4 Memory-unlock ladder — **stage 3 is unspent and unduplicated. Verified.**

Ch.6, 7 and 8 spend no stage. Nothing legible surfaces to Rx; no new fact reaches Vexx from
inside Rx; **Jameson is not present in person in any of the three chapters.** Stage 1
(Ch.3 treeline) and stage 2 (Ch.4 "the shape of a refusal") remain the only unlocks on the
page and neither is re-run.

**Two standing cautions, both recorded in the YAML ladder block:**

1. **Ch.7's confabulation is a new class of malfunction the ladder does not describe.** Rx
   produces a false shared childhood memory — *"It rained on that roof every night the summer
   we were fifteen, tin roof, the second barracks"* — breaks off mid-simile, covers with
   *"Queue's moved"*, and the narration corrects him in one flat line: **"The barracks roof had
   been concrete."** It is the best beat in the chapter and it should stay. But confabulating a
   memory *adjacent* to the sealed one is the closest this book has come to a rampancy tell,
   and series canon forbids that reading absolutely. It must be framed as suppression bleeding
   sideways — **never** as decay over time, and never quantified. See §3, W-04.
2. **"Jameson present in person" is no longer a novel trigger.** He has been in a room with
   Vexx and Rx twice on the page (Ch.2 first meeting, Ch.3 mission brief) and Rx produced only
   silence and a hitch. `outline.md` §Chapter 13 already escalates correctly — *his actual
   voice, close, on an open channel, giving a live coordinating instruction*. **Do not weaken
   that to mere proximity.** See §4, D-02.

---

## 1. FINDINGS IN CHAPTER 1 — LOCKED. REPORT ONLY. NO EDIT PROPOSED.

### C-01 · worth a look · Vexx's age arithmetic
- **Ch.1:** "Twenty-six years of his life had a shape, and the shape had just been surgically
  removed" — against, in the same chapter, "Vexx had spent **thirty years** learning to read
  people under pressure", and "the reflex to laugh… out of **thirty years** of habit."
- **Corroborated outside Ch.1 on the "thirty" side:** Ch.3 "thirty years of training had taught
  him"; Ch.8 "He had been in three of them in **thirty years**."
- **Why it matters:** inducted at six, thirty years of service, four years retired makes him
  ~40; "twenty-six years" makes him ~36. The book never states an age, so no reader will
  arithmetic it out — but Ch.8 has now joined the "thirty" side, which makes "twenty-six" the
  lone outlier.
- **No edit.** Chapter 1 is the voice benchmark and this is invisible at reading speed. Logged
  in `ENTITY_STATE.yaml` as an existing unresolved conflict on `vexxcerian.physical.age`.
  **Constraint for Ch.9–26: never state a number.**

### C-02 · deliberate-and-fine · the mess hall at 1100
- **Ch.1:** "the particular clatter of a mess hall at 1100".
- **Ch.6:** "the clatter of a mess hall at eleven hundred came up on him whole, like a door
  pushed open on it" — and then Ch.6 *develops* it: "The light in the mess hall had been wrong
  for eleven hundred… he had been calling it eleven hundred to himself for something over
  twenty years."
- This is the single best callback in the pipeline chapters. Two of three uses spent.
  **Action: confirm it is in `tools/style_check.py` ALLOWLIST as a capped motif so the third
  use is deliberate and the fourth is blocked.**

### C-03 · deliberate-and-fine · "an outline with nothing in it"
Ch.1 ("what was left was an outline with nothing in it") → Ch.2 ("the first night since the
empty casket that he'd gone to sleep without the apartment feeling like an outline with
nothing in it"). Two of three. Same ALLOWLIST action.

### C-04 · deliberate-and-fine · "Took you long enough"
Rx's first words in Ch.1; Corwin's first words in Ch.3. Deliberate and load-bearing — Corwin
saying it is what tells Vexx he has been waiting for Valkyr. Two of three. Do not spend a third.

### C-05 · deliberate-and-fine · Corwin knows the word "Valkyr"
Ch.3 flags its own gap — "None of them had used that word *anywhere* he could plausibly have
heard it" — and never closes it. Ch.6 then pointedly leaves it shut: "it occurred to Vexx that
nine weeks ago, this man had known the word Valkyr, had used it out loud in a clearing, that
neither of them had said it once today." **Deliberate. Do not resolve casually.**

---

## 2. FINDINGS IN CHAPTERS 2–5 — THE AUTHOR'S PROSE. MINIMAL PROPOSALS ONLY.

### A-01 · **needs a fix** · Ch.4's internal date is off by six weeks
- **Ch.4, opening:** "Vexx learned it **three weeks after the jungle**, in a debrief…"
- **Ch.4, three scenes later:** "The friction with Paladin came on the cell's third deployment,
  **six weeks later**" → the Reyes mission sits at jungle + ~9 weeks.
- **Ch.4, that same night:** Rx's voice is "threaded with an unsteadiness Vexx had only heard
  once before, **in a jungle clearing three weeks earlier**."
- **Why it is a contradiction:** the jungle clearing is nine weeks earlier by the chapter's own
  arithmetic, not three. The "three weeks" is a fossil from before the "six weeks later" scene
  break was placed.
- **Proposed fix — one word, in Ch.4:** *"in a jungle clearing **two months** earlier"*.
  ("Two months" reads more naturally in this voice than "nine weeks", and does not compete with
  Ch.6's nine-weeks motif.)
- **What is at stake if left:** a careful reader who is tracking the Rx thread — which is
  exactly the reader this book is built for — is counting these intervals, because the
  intervals are the evidence. Getting one wrong in the chapter where Vexx first asks *"Do you
  remember anything at all about how you actually died?"* undercuts the one thing that
  chapter is doing.
- **Cascade:** none. Nothing downstream keys off "three weeks earlier".

### A-02 · **needs a fix** · Ch.2 dates the Phantom slip twice, differently
- **Ch.2:** "He was right, though it took longer than an hour — **three weeks**, in fact, most
  of them spent on a training range…"
- **Ch.2, sixteen lines later, inside that same scene:** "the way he seemed to pick up on most
  things about his operator faster than made strict logical sense for **six weeks** of
  acquaintance."
- **Why it is a contradiction:** Goliath's pairing happens "three days later" than his
  interview, and the range scene is three weeks after the pairing. Six weeks is not available.
- **Proposed fix — one word, in Ch.2:** *"for **three weeks** of acquaintance"*.
- **What is at stake:** small. But the sentence's whole rhetorical move is *the interval is too
  short for this intimacy*, and the interval it names is double the real one, which weakens the
  point it is making. Already logged in `ENTITY_STATE.yaml` timeline note for Ch.2.

### A-03 · worth a look · Ch.5's "that autumn"
- **Ch.2** sets the roster-building in autumn ("Like so much else that autumn"). The first
  deployment is ~6 weeks after that. **Ch.5** falls ~10 weeks after the jungle and still says
  "the way he'd learned to do more and more often **that autumn**" — which by the book's own
  clock is deep winter. Ch.6, written later, correctly has an orchard "pruned back hard for
  winter."
- **Proposed fix if touched at all:** *"that first winter"*. **Recommendation: leave it.** It is
  the author's cadence, the season is nowhere load-bearing in Ch.5, and Ch.6 quietly overrides
  it two chapters later. Flagged so the copyeditor has the choice rather than discovering it.

### A-04 · worth a look · Ch.2's roster arithmetic
"**Six pairings** into a roster he'd built with his own hands instead of one handed to him" —
he built five; his own was handed to him, which is the whole point of the sentence's second
half. Voss commissions "Five operators, five AI." Already open in `ENTITY_STATE.yaml` as
`CF-06`. **Minimal fix: "Five pairings into a roster…"** Low stakes; author's call.

### A-05 · worth a look · Ch.2's Phantom scene is dramatised, then disclaimed
The Goliath/Spector Phantom exchange runs on full quotation-mark dialogue for fourteen lines —
and then: "Vexx, watching from the observation deck above the range, **didn't hear the exchange
in full** — only saw Goliath go quiet…" The POV repair is welded onto the end of Goliath's
dialogue paragraph.
- **Assessment: deliberate and inherited.** SERIES-BIBLE requires this beat in Book One Ch.2,
  delivered as a slip rather than from a record, and the disclaimer sentence is the author
  patching it himself. **No fix proposed.**
- **This is also my single best candidate for a page-turn reconstruction artifact in Ch.1–5**
  (see §5) — the disclaimer reads like it wants to be its own paragraph. Flagged, not fixed.

### A-06 · worth a look · Ch.5 lets Echo speak privately into Vexx's ear
"Echo, quiet through the whole exchange, offered a small, approving hum in Vexx's ear that
mirrored, almost exactly, the sound Rx had made weeks earlier." Every other AI–operator
exchange in the book routes through the AI's own operator's interface ("*Spector said, through
Goliath's interface*", "*Bastion said, through Paladin's interface*").
- **Why it matters:** it establishes that any AI can address any operator directly, which makes
  the reader ask, in Ch.8, why Spector did not simply tell Vexx himself. **Ch.8 answers it
  well** — "That isn't what he did. He came to me" frames it as Spector's *choice*, not a
  limitation — so this is not a contradiction, only a softening.
- **No fix proposed.** Recorded in the YAML so the mechanic is not later declared impossible.

---

## 3. FINDINGS IN CHAPTERS 6–8 — PIPELINE-WRITTEN. PROPOSE FREELY.

> ⚠️ **Ch.8 sits on four mechanical floors and ceilings simultaneously (word target, style
> gate, motif cap, tic budget). Every proposal below is word-count-neutral or negative and is
> written to be applied as a single dispatched pass, not piecemeal.**

### 🔴 B-01 · **BREAKS THE BOOK** · The manuscript is written in two different Englishes

This is the largest mechanical defect in the book and no per-chapter gate can see it.

| | Ch.1 | Ch.2 | Ch.3 | Ch.4 | Ch.5 | Ch.6 | Ch.7 | Ch.8 |
|---|---|---|---|---|---|---|---|---|
| **US forms** | 20 | 17 | 11 | 9 | 7 | 2 | 1 | 3* |
| **British forms** | 0 | 0 | 0 | 0 | 0 | **15** | **4** | **15** |

\* Ch.8's three "meter" hits are the multimeter instrument and are correct in either dialect.

Chapters 1–5 are **100% US and contain zero British forms**. Chapters 6–8 carry **34** British
forms — `armour`, `colour`, `grey`, `metre`/`metres`, `apologise`/`apologised`,
`authorisation`, `recognise`, `humour`, `per cent`.

**The two that are worse than a style inconsistency:**

1. **Ch.6:** *"He was in soft clothes, **grey**, the kind a person could sleep in."*
   Chapter 1 uses **"gray"** six times, and "the gray room" is the book's founding image —
   locked, hand-finished, the voice benchmark. Ch.6 spells it the other way, on Corwin, in the
   chapter that is a deliberate mirror of the gray room.
2. **Ch.6:** *"Cooperative with **programme** throughout."*
   The SERIES-BIBLE naming registry makes **"the program"** canonical. Ch.6 and Ch.7 use
   "program" correctly elsewhere; this one institutional quotation drifts.

- **Proposed fix — in Ch.6, Ch.7 and Ch.8, none of which is locked:** convert all 34 British
  forms to US. **Chapter 1 is locked and is therefore the standard; the pipeline chapters
  convert to it, never the reverse.** Word-count-neutral.
- **Cascade / prevention (this is the important half):**
  - Add an **orthography line to `books/valkyr/valkyr-book-1/CLAUDE.md`** under *Canon
    guardrails*: *"US spelling throughout, set by locked Ch.1. `gray`, not `grey`. `the
    program`, never `programme`."*
  - Add a British-forms check to `books/valkyr/valkyr-book-1/tools/style_check.py` so
    Ch.9–26 cannot repeat it. **This is a per-book gate, so it stays in the book folder** —
    if the check logic itself proves generally useful, promote the *mechanism* to
    `books/_template/` per the repo UPDATE RULE, leaving the word list per-book.
- Logged as `CF-14`.

---

### N-01 · **needs a fix** · Ch.8's failed stack breaks POV *and* miscounts the cell

Two defects in one paragraph, and one edit fixes both.

> "…and it put **four of them stacked** in a service corridor two metres wide with the far end
> of it dark, and it put nobody at all on the second door."
> […] "The kid came through it… before **Paladin's weapon came up**. It did not come all the way
> up… **Goliath had a fistful of the fleece**, had put him against the wall with a forearm…"
> […] "**Vexx came in through the near door.** The thermos was on the floor…"
> […] Zeus "**had come in behind Vexx**"

**(a) POV.** The contact is narrated with close visual detail — the boy's walk, the weapon
coming up and stopping, the forearm going on and coming off — from a vantage *inside* the
two-metre corridor. Then "Vexx came in through the near door" places him *outside* it for the
whole thing. This is the same class of break as the "for the entire time they were in the
building" line already caught and fixed in this chapter.

**(b) Arithmetic.** The cell is six. Gaia is at the far corner. Vexx comes in after. Zeus comes
in behind Vexx. That leaves **Goliath, Paladin and Aglaope — three**, not four.

- **Proposed fix, in Ch.8:** put Vexx in the stack. Then Gaia (corner) + Vexx, Goliath, Paladin
  and Aglaope stacked = **four**, and Zeus is the one still outside. Change
  *"Vexx came in through the near door"* → *"Vexx got past Goliath to the step"* (or similar
  in-corridor movement), and *"He had come in behind Vexx"* → *"He had come in behind them."*
  Word-count-neutral; two touches.
- **Why this fix and not the other:** the alternative (change "four" to "three" and keep Vexx
  outside) leaves the POV break standing and is the worse of the two.
- **Cascade:** check that nothing else in the scene depends on Vexx arriving late. It does not —
  the line *"That was mine," Vexx said, on the net, to all of them*, works better with him in
  the corridor, not worse.
- Logged as `CF-10`.

### N-02 · **needs a fix** · Ch.8's assessment scene breaks the POV it just declared

The chapter sets its own rule, precisely, and then breaks it twice:

> "Vexx stood **outside the door where he could hear it, which is not the same as being in the
> room** — which Merrick knew and did not mind."

and honours it beautifully once — *"Vexx, outside the door, **heard the chair**."* Then:

1. **"Merrick opened his mouth."** — a purely visual beat from inside a room Vexx cannot see
   into.
2. **"Zeus did not stop him. He did not say a name, he did not clear his throat, he did not do
   the thing an ordinary man would have done, which is to look at the door."** — Vexx cannot
   observe Zeus *not looking at a door*.

- **Proposed fix, in Ch.8:**
  1. *"Merrick opened his mouth."* → *"Nothing came back."* — keeps the beat, converts it to
     something audible through a door, and is arguably a better sentence.
  2. Cut the clause *"he did not do the thing an ordinary man would have done, which is to look
     at the door"*. The two preceding negatives ("did not say a name", "did not clear his
     throat") are both **audible** and already carry the point. Net −18 words, which helps
     against the 6,200 target.
- **Cascade:** none. The kitchen-table scene later gives Vexx Zeus's account in full, so nothing
  is lost.

### N-03 · **needs a fix** · Ch.8 counts eleven people on the apron, and there are not eleven

> Gaia: *"Garrison eleven, ten of them accounted for in the block, one unaccounted."* → the
> garrison is **eleven including Merrick**.
> Then: *"He shook **ten** hands."* → correct: ten remain once Merrick is on the ramp.
> Then, four lines later: *"He told the station commander that the bund needed doing before
> spring… The station commander said he would — **then went inside and did not come out
> again**."* → nine remain outside.
> Then: *"with a hand on the frame and his back to the plateau and **eleven people on the apron
> behind him** watching him go."*

Eleven is wrong on every reading — ten with the commander, nine without him, fifteen if you
count the cell.

- **Proposed fix, in Ch.8:** de-number rather than re-count, because the number is doing
  rhythm rather than information: *"…and his back to the plateau and the whole of the station
  on the apron behind him watching him go"* — or simply *"and the station behind him watching
  him go."*
- **Cascade:** Paladin's "eleven people in it" (the garrison) and Gaia's "Ten of the eleven have
  noticed" are both correct and must not be touched.
- Logged as `CF-09`.

### N-04 · **needs a fix** · Ch.6 lands on top of Ch.4 instead of after Ch.5

Ch.6 dates itself at **jungle + 9 weeks**, three times, and it is the chapter's central image:

> "He was in a jungle **nine weeks earlier**, at two in the morning…"
> "**Nine weeks** he had been on the other side of that sentence…"
> "it occurred to Vexx that **nine weeks ago**, this man had known the word Valkyr…"
> plus: Corwin is "**six weeks** into a rehabilitation track" after a debrief at jungle + 3 weeks.

But Ch.4 puts the Reyes mission at **jungle + ~9 weeks** ("three weeks after the jungle" → two
days → "six weeks later"), and Ch.5 falls *after* Reyes. So a Ch.6 at + 9 weeks arrives at or
before Ch.5, not after it. Ch.6's own arithmetic is internally flawless; the collision is
between chapters.

- **Proposed fix — in Ch.6, because Ch.4 and Ch.5 are the author's prose and Ch.6 is not:**
  "nine weeks" → **"eleven weeks"** (three instances) and "six weeks into a rehabilitation
  track" → **"eight weeks"**. Word-count-neutral.
- **Cascade — checked, and it holds.** Ch.7's "two months ago" (measured from the Ch.4 kitchen
  table) and Ch.8's "seven weeks earlier" (measured from the Ch.5 corridor) both survive the
  change without adjustment; the resulting chronology still puts Ch.8 in deep winter with
  February ahead of it, which is what Merrick's dialogue needs.
- Logged as `CF-08`.

### N-05 · **needs a fix** · Ch.6 quotes a clinical file Vexx has never seen

Mid-scene, unattributed, in the document italics the book uses elsewhere:

> *Subject's account of the deployment now aligns with the operational record. Persecutory
> ideation not reported this cycle; insight assessed as much improved.*
> *Cooperative with programme throughout. Recommend continuation of track; review at ninety
> days.*

Ch.7 and Ch.8 use the same device correctly — the requisition and the flag summary are both
things Vexx is demonstrably reading on a pad. **Here he is sitting in a day room with a coffee,
and Corwin's clinical progress note is not a document he has, or would have.** POV break, and
the only one in Ch.6.

- **Proposed fix, in Ch.6 — one of two, dispatcher's choice:**
  1. **Ground it.** Move the two lines into the pre-visit material: Vexx read the resident
     summary attached to his visitor authorisation on the transit out. Two lines earlier in the
     chapter, one clause of setup. *(Cheapest, keeps the device.)*
  2. **Cut it.** The passage is doing work Corwin's own speech already does better —
     *"They explained it to me. I think I had it backwards"* — and the institutional voice is
     already in the room in the clinician's *"It's in review."* Net −35 words.
- **Recommendation: option 2.** The chapter's power is that the institution never has to speak
  for itself.

### N-06 · **needs a fix** · Ch.6 spends Merrick's reserved device on Corwin, two chapters early

`character-bible.md` §TIC BUDGET, one-device-per-character map:

> | Involuntary self-echo — repeating his own last three words *(not a technique; a symptom)* | **MERRICK** |

Ch.8 executes it as the chapter's declared anchor: *"Round the changeover."* / *"In the
folder."* / *"It does."* / *"Before dark."* / *"Sorry, Tomas."*

But Ch.6 already gave it to Corwin:

> "**He was tidying.** That's how I said it to myself for eleven days, in those words, over and
> over. **He was tidying.**"

and, softer, *"It's the honest answer. Neither do I."* echoing his own line two beats up.

- **Why this is worse than a budget breach.** Ch.6's whole anchor is *Corwin is lucid and well*,
  and Ch.8's whole function is *Merrick genuinely is coming apart, and this is what that sounds
  like*. Handing Corwin the diagnostic tell first blurs both. A reader who meets the device on
  Corwin in Ch.6 has been taught to read it as a mannerism by the time it matters in Ch.8.
- **What is NOT the same device and must be kept:** Corwin echoing **the clinician** — *"It's in
  review," Corwin said. To Vexx. Nodding.* That is a man repeating the institution back, which
  is the best line in Ch.6 and belongs to nobody else.
- **Proposed fix, in Ch.6:** de-duplicate the *self*-echo. *"…in those words, over and over."*
  and stop — let the paragraph end there, and let the second "He was tidying" be Vexx's
  narration two paragraphs later ("**He was tidying.** Nobody tidies in a firefight."), where it
  is already doing better work as Vexx's own turn. Net −4 words.
- **Related, same chapter, same shape:** Ch.6 has Corwin correct his own slip ("There was six of
  you." / "**Were.**") and Ch.8 has Merrick correct his own slip ("He got the cook's name wrong
  and corrected it himself"). Two adjacent chapters, same structural move, different men.
  Corwin's is the reserved grammar device and is correct; **Merrick's is the one to consider
  dropping** if the pair reads as a rhyme — it is one clause in a list of five.

### N-07 · **needs a fix** · "the whole of it" has become a narrator tic across three chapters

Ten instances across the manuscript, six of them in Ch.8:

| Chapter | Line | Voice |
|---|---|---|
| Ch.4 | "That was the whole of it, in the end — a Spartan screaming himself hoarse…" | narrator |
| Ch.6 | "That was the whole of her surprise." | narrator |
| Ch.6 | "…the whole of it looking like somebody's farm." | narrator |
| Ch.7 | "*That's the whole of it. It isn't evidence of anything.*" | Rx |
| Ch.8 | "That was the whole of it. There had been four more lines under it…" | narrator |
| Ch.8 | "That was the whole of it — three seconds, no discussion…" | narrator |
| Ch.8 | "That is the whole account of it." | narrator |
| Ch.8 | "You can have the whole of it." | Zeus |
| Ch.8 | "You asked me for the whole of it and then you said no." | Zeus |
| Ch.8 | "…and that was the whole of it." | narrator |

**Four narrator uses in one chapter.** Per-chapter gates cannot see this because the ALLOWLIST
has no entry for it and no single chapter looks unreasonable in isolation. The motif cap is
**three across the whole book**.

- **Proposed fix, in Ch.8:** keep **one** narrator use — *"That is the whole account of it"*,
  after the stack, which is the one that earns it — and recast the other three. Keep **both** of
  Zeus's; they are a deliberate pair inside one exchange, forty words apart, and they are the
  argument.
  - "That was the whole of it. There had been four more lines under it in the packet…" →
    *"That was all of it. There had been four more lines…"*
  - "That was the whole of it — three seconds, no discussion, no reason given" →
    *"Three seconds. No discussion, no reason given:"*
  - "…and that was the whole of it." (Goliath leaving) → *"…and that was that."* or cut.
- **Then:** add `"the whole of it"` to `tools/style_check.py` ALLOWLIST as a **capped** entry at
  3, so Ch.9–26 cannot quietly reload it.

### N-08 · **needs a fix** · A single hand-gesture is now shared by four characters

Squaring or quarter-turning an object on a table — an intimate, specific, *characterising*
gesture — is currently being performed by everyone:

| | |
|---|---|
| Ch.2 | Zeus: "He pushed his chair back under the table, a small tidy careful movement, and **squared it**." |
| Ch.5 | Vexx: "He **turned her cold cup a quarter turn** on the table and left it where it was." |
| Ch.6 | Corwin: "He **turned the mug a little on the table, squared it to the edge.**" |
| Ch.6 | Corwin: "He **squared the mug again**. For the first time his hands did something." |
| Ch.6 | Voss: "She **squared the folder** of authorisations on the counter…" |
| Ch.8 | Aglaope: "She **turned the cup a quarter-turn**." |
| Ch.8 | Aglaope: "…put something on the desk beside the pad, **squared it to the edge** with two fingers…" |

Corwin's is *earned and load-bearing* — his hands not doing anything is the first thing Vexx
registers about him, and the mug is how the chapter measures him. **It should be his alone.**

- **Proposed fix, in Ch.8 (both instances):**
  - Aglaope's cup: *"She turned the cup a quarter-turn"* → *"She put the cup down without
    drinking from it."* (She has already been established, two lines up, as holding a cup she
    has not drunk from — this closes it instead of repeating a gesture.)
  - Aglaope's notebook: *"squared it to the edge with two fingers"* → *"set it down square, with
    two fingers, and took them off it."*
- **Leave Ch.5 and Ch.6 alone.** Ch.5 is the author's; Ch.6's is the owner. Voss's folder
  (Ch.6) is a different verb-object and can stay.

### N-09 · **needs a fix** · An identical physical beat two chapters apart

- **Ch.6:** "…and the gardener straightened up, **put a hand in the small of his back**."
- **Ch.8:** "'The shed's fine,' Goliath said, and stood, **put his hand in the small of his
  back**."

Same six-word phrase, both pipeline chapters, and in Ch.8 it lands on a principal.

- **Proposed fix, in Ch.8:** *"…and stood, and took a moment about standing."* Both are men
  being older than the work; the Ch.6 gardener is the one that should keep the phrase, because
  he is scenery and Goliath is not.

### N-10 · **needs a fix (author/architect decision)** · Ch.7 gives Rx Spector's reserved device

`character-bible.md` one-device map: *"Counting · sequence · countdown · numbering · tallying ·
rating · pricing · cataloguing"* → **SPECTOR, and nobody else.**

Ch.7 hands Rx a sustained numeric register inside 1,500 words: *"Line forty-one of sixty"* ·
*"Nine minutes in a queue"* · *"thirty-one per cent complete"* · *"I've given it five years
four times to cover the twenty I want"* · *"It took nineteen"* · *"Line seven of twenty-two. I
can't see the other twenty-one from here"* · and the tally, *"You're seventeen of thirty on the
moving plates this month. I keep it. Nobody's asked me to keep it. I don't know what I keep it
for."* Meanwhile Ch.8 gives Spector his own count — *"One, two, three, four — four drums, four
seals, four intact."*

**And the outline is on Rx's side of the argument:** `outline:ch-08` and `outline:ch-13` both
schedule *"Rx's marksmanship tally"* as Rx's character-chaos beat, which the bible's map
forbids. So this is a settled-decision gap, not a drafting slip.

- **Recommendation — resolve it in the docs, not by gutting Ch.7.** The tally is the best line
  in Ch.7 and `outline:ch-13` has it deployed mid-collapse as "the most frightening thing in the
  book." Renarrow Spector's device in `character-bible.md` to **SEQUENCE** (*set-charge-clear*,
  ordered enumeration of a procedure) and cede **tallying / keeping a count of a person** to
  **RX**, where it means something entirely different and darker. Then thin Ch.7's incidental
  numbers by two or three so the tally lands alone.
- **This is an edit to `character-bible.md` (per-book) and `outline.md`.** No series-level
  change.
- Logged as `CF-11`.

### N-11 · **needs a fix** · Ch.6's recovery-element day count contradicts Ch.3

- **Ch.3 (author):** Gaia, at the burned camp — *"Recovery unit went in **eleven days ago**."*
  Corwin has been dark eleven days.
- **Ch.6 (pipeline):** Corwin's corrected account — *"The recovery element came in on **day
  three**… I went into the trees and I stayed out of their way for **eight days** while they
  looked for me."* (3 + 8 = 11, internally clean, but it puts the recovery element on the ground
  eight days ago, not eleven.)
- **Proposed fix, in Ch.6, because Ch.3 is the author's:** *"came in on day three"* → *"came in
  on the first day"*, and *"eight days"* → *"ten days"*. Gaia's "eleven days" then reads as
  ordinary field rounding rather than a flat contradiction, and Corwin's "drinking off leaves
  for the first two of them" still works.
- **Cascade:** nothing else keys off either number.

---

## 4. FINDINGS IN `ENTITY_STATE.yaml`, `SERIES-BIBLE.md`, `outline.md` AND `CLAUDE.md`

### D-01 · **needs a fix** · `outline.md` Ch.8 Premise: "fourth deployment" → **fifth**
Full reasoning in §0.2. The outline contradicts itself in the same entry ("third time in five
missions" is correct). **No manuscript change.** `CF-07`.

### D-02 · **needs a fix (guardrail, not a defect)** · Protect the stage-3 trigger
Jameson has now stood in a room with Vexx and Rx twice on the page without a stage-3 event.
`outline:ch-13` already specifies the right escalation — **his voice, close, on an open channel,
giving a live coordinating instruction** — and its writer-warning (a) is correct as written.
**Action:** add one line to the Ch.13 entry making explicit that *mere proximity has already
been spent twice in Ch.2 and Ch.3 and is not by itself the trigger*, so a later drafting pass
cannot soften it back to "Jameson is present."

### D-03 · **needs a fix** · `SERIES-BIBLE.md` is stale in three places
1. **The books table** still reads *"In progress — **5 chapters** drafted, architect pass done."*
   → eight.
2. **"Introduced by the Book One outline, not yet on the page"** still lists **Merrick** (Ch.8)
   and **Holst, D.** (Ch.7) and **RECLAMATION** (Ch.7). All three are now on the page and
   therefore series canon. Per the bible's own instruction — *"they become series canon the
   moment their chapter is drafted"* — they should move into the cast/state tables with their
   Book One end-state: **Merrick — alive, removed from field, medical track, escort of two, not
   restrained; the baseline case, and NOT a conspiracy victim.**
3. **The naming registry needs new rows** for entities Ch.6–8 created:
   `Deric A. Holst | Holst, D.; Holst | Derek, Deryk, Holtz, Holste` · `Tomas | — | Thomas,
   Tomás` · `Ivo` · `Hallam` · `Kettle` (the ridge Echo names) · `Hallow's Bottom`.

### D-04 · **needs a fix** · `SERIES-BIBLE.md` registry vs Ch.7 on Holst's first name
The planning constraint said *"never given a first name."* Ch.7 gives him one, off an archive
line — **STAFF SERGEANT DERIC A. HOLST, 11TH SHOCK TROOPS BATTALION** — and the constraint
should yield: the full name is what makes the entry read as a scanned record rather than a
prop, and *"Somebody had written **photo?** in pencil in the margin"* depends on it being a
real person's file. **The prose is right.** `CF-13`.

### D-05 · **needs a fix** · The book's `CLAUDE.md` Status block is stale and now actively wrong
> "**Nothing has passed the pipeline's gates yet.** `manuscript/chapters/` is still empty; the
> author's five chapters live in `research/original-draft.md` and have not been promoted."

Eight chapters are in `manuscript/chapters/`. A fresh session reads this file first and will be
misdirected by it. **Also add there:** the US-spelling rule from B-01, and a note that Ch.6–8
are pipeline-written and freely editable while Ch.2–5 are the author's and Ch.1 is locked.

### D-06 · deliberate-and-fine · RECLAMATION planted correctly
`outline:ch-07` writer_constraint: *"must NOT be glossed on first appearance. No character
notices it in Ch.7; no narration underlines it."* Ch.7 delivers *"ROUTING: MD 4, SUB.
RECLAMATION"* inside a materiel footer and **nobody remarks on it.** Exactly right. Verified and
recorded.

---

## 5. THE PAGE-TURN RECONSTRUCTION QUESTION (Ch.1–5)

Mechanically, Ch.1–5 are **clean**: across all five chapters there is **not one paragraph that
begins with a lower-case letter** and **not one that ends without terminal punctuation** —
which is what a mis-joined or mis-split page-turn usually leaves behind. Whatever the
right-margin test decided, it did not leave visible scars.

**One semantic candidate,** offered as the place to look first if the author ever revisits the
reconstruction:

- **Ch.2**, the close of the Phantom scene. "'Yeah,' Goliath said. He didn't sound entirely
  convinced it was coincidence. Vexx, watching from the observation deck above the range,
  didn't hear the exchange in full — only saw Goliath go quiet in a way that didn't suit him,
  and Spector's readouts hold unusually steady beside him, like an AI being very careful not to
  say more than he already had."
  Goliath's dialogue tag and a full POV pull-back to a different vantage sit in one paragraph.
  **If a break was dropped anywhere in Ch.2, it is before "Vexx, watching…".** Flagged, not
  fixed — Ch.2 is the author's and this is a judgement call, not an error.

---

## 6. ORPHANED THREADS AT THE END OF CH.8

### Deliberate long-arc plants — leave them open

| Thread | Opened | Planned payoff |
|---|---|---|
| RECLAMATION (the routing tag) | Ch.7, unglossed | `outline:ch-15`; series-canon |
| Voss's motive | Ch.2, Ch.4, Ch.6 | `outline:ch-19`; series-canon ("unexplained") |
| Phantom / Goliath's homeworld | Ch.2 | series-canon; suspicion only, never confirmed |
| The half-melted data chip | Ch.4 | unread and unreadable by design |
| Corwin's AI's name | Ch.6, actively refused | withheld by design — *"I'm not putting it in a room where it counts as a symptom"* |
| Tomas | Ch.8 | `outline:ch-08` requires he stay unidentifiable |
| Vexx's four typed letters of a shared surname | Ch.7 | Rx's *"I didn't see that"* is the payoff, and it is enough |
| The visitor-log signature | Ch.6 | `outline:ch-10`, Internal Compliance |
| How Corwin knew the word "Valkyr" | Ch.3, self-flagged | see C-05 |

### Genuine loose ends — decide now, not at Ch.20

**O-01 · needs a fix · Merrick's notebook has nowhere to go.**
Aglaope recovers it from behind the fuse box, squares it on Vexx's desk, and leaves. **Vexx
never opens it, and `outline.md` §Chapter 9 does not mention it** — Ch.9 is the archive at 0200
and the Zeus offer. This is a Chekhov object handed to the POV character in the last 200 words
of a chapter with no scheduled consumer. Either Ch.9 opens it in its first page, or the outline
needs to say which chapter does. **Do not let it drift past Ch.10.**

**O-02 · needs a fix · Corwin's letters.**
Vexx says *"I'll ask"*, knows what it is worth on the way out of his mouth, and says the debt
out loud to a stranger at a transit shelter — *"I don't know whether it went"*. Emotionally
that closes; practically it is a promise to a man in an institution, and the book has not
touched it in two chapters. `foundation.md` and `character-bible.md` both say the daughter is
*"the only thing Corwin ever asks for… and it is never granted"* — which makes never granting
it correct, but **only if the failure is dramatised at least once more.** Assign it a chapter.

**O-03 · worth a look · The third word Spector gave Goliath.**
Deliberate and excellent — but it is a live offer left on the table (*"Do you want the third
one, when he gives it to me?"*) and the outline does not say who picks it up. Nominate a
chapter.

**O-04 · worth a look · The archive subscription that lapses at the end of the month.**
Ch.7 plants a clock — *"that archive runs on a subscription that lapses at the end of the
month, which is a thing I've decided to tell you now rather than at the end of the month."*
That is a promise of pressure. If nothing uses it, cut the clause; if something does, it should
be within two or three chapters.

**O-05 · worth a look · Paladin's right hand.**
Introduced in Ch.8 by Bastion, worse on Tuesday, never referenced again. Fine as texture; a
loose end if it was meant as more.

---

## 7. CROSS-CHAPTER REPETITION THE PER-CHAPTER GATES CANNOT SEE

Consolidated; the fixes are in §3.

| # | Pattern | Chapters | Verdict |
|---|---|---|---|
| 1 | Orthography: two Englishes | 1–5 vs 6–8 | **BREAKS THE BOOK** — B-01 |
| 2 | "the whole of it" ×10 (4 narrator uses in Ch.8) | 4, 6, 7, 8 | needs a fix — N-07 |
| 3 | Squaring / quarter-turning an object on a table, ×7, four characters | 2, 5, 6, 8 | needs a fix — N-08 |
| 4 | "put a hand in the small of his back" | 6, 8 | needs a fix — N-09 |
| 5 | Involuntary self-echo of one's own last words | 6 (Corwin), 8 (Merrick) | needs a fix — N-06 |
| 6 | A man correcting his own slip, unprompted | 6 (Corwin), 8 (Merrick) | worth a look — N-06 note |
| 7 | Counting/tallying as an AI device | 7 (Rx), 8 (Spector) | needs a fix — N-10 |
| 8 | Coffee as an institutional index | 6 (the good pot), 8 (the feud, the urn) | **deliberate-and-fine** — `outline:ch-18` is titled "The Coffee Pot". Register it in the ALLOWLIST so it is capped rather than accidental. |
| 9 | The mess hall at 1100 / "an outline with nothing in it" / "Took you long enough" | 1→6, 1→2, 1→3 | **deliberate-and-fine** — 2 of 3 each. ALLOWLIST them. |

**W-10 · worth a look · The involuntary sensory-memory intrusion is a new device with no budget.**
Ch.6 (the mess hall at eleven hundred), Ch.7 (orange drink powder in a plastic cup; a radio in
the next bay), Ch.8 (boot polish, the tin with the yellow lid; a tin of fudge with a lighthouse
on the lid). **Three chapters, five instances, ~2 per chapter, and the device does not exist
anywhere in Ch.1–5.** It is very good, it is doing real work — it is Vexx's version of what Rx
cannot do — and it is completely unregistered in `voice-dna.md` or `character-bible.md`.
**At 2 per chapter it will run to ~40 instances by Ch.26.** Register it and cap it (a
suggestion: no more than one per chapter after Ch.10, and none at all in the chapters where Rx
is leaking, so the two never compete).

---

## 8. OTHER FINDINGS — WORTH A LOOK

**W-04 · Ch.7's confabulation and the rampancy guardrail.** Covered in §0.4. Keep the beat;
never quantify it; never let a later chapter frame it as progressive decay. Recorded in the
YAML ladder block as a standing caution.

**W-05 · Rx's signature tic has gone missing.** `character-bible.md` gives Rx exactly one
device — **the too-quick denial**, *"Fine." / "I'm fine, Vexx."* — and requires that it
**BREAK in Ch.13 and never be smooth again.** It appears in Ch.1, Ch.2, Ch.3 and Ch.4, and then
**not once in Ch.6, Ch.7 or Ch.8.** For a break to land in Ch.13, the reader needs it fresh.
**Action:** get one clean, unremarkable use into Ch.9–12. Ch.9 or Ch.12 is the natural place.

**W-06 · Hollow has not spoken since Chapter 2.** Zeus's AI speaks once, at the pairing, and
has been silent for six chapters — including Ch.8's kitchen-table round, where Vexx polls Zeus,
Gaia, Aglaope, Goliath and **Bastion**, and Hollow says nothing. The character-bible device
assigned to Hollow is *"withholding until useful / answering forty minutes late"*, so the
silence is arguably in character — **but six chapters is past the point where a reader stops
noticing and starts forgetting he exists.** Give him one late answer before Ch.13.

**W-07 · Ch.8 and February.** Merrick refers *forward* to February twice ("that means lifting
plate in February"; "how many hours of dark there were at that latitude in February"), which
places the chapter in January — but the chapter's other anchors (jungle + ~17 weeks after the
N-04 correction, "the sixteenth's the changeover") push it to the edge of February. Not wrong;
just tight. **If N-04 is applied, re-read those two lines once to confirm February still reads
as ahead of him.**

**W-08 · The data chip has fallen out of the evidence inventory.** Ch.7's stocktake of Vexx's
exposure names *"an armour fragment… a tag with a dead man's name stamped on it… a search
history across nine civilian archives"* — and omits the half-melted data chip, which is one of
the three fragments and is in the same drawer. Possibly deliberate (it is inert). Flagged so it
is not quietly lost before it pays off. `CF-12`.

**W-09 · "It's been the water since August."** Goliath's line puts him in the building in
August; Ch.2 sets roster-building in autumn. It works — Goliath is the *first* pairing and
precedes the six weeks of roster-building — but it is the tightest join in the book's clock.
Leave it; noted so nobody moves Ch.2's autumn earlier.

**W-12 · Month names on the page.** The guardrail is *"no hard in-universe calendar **date**"*.
Ch.6 and Ch.8 use April, spring, summer, August, October, winter, February, and *"the
sixteenth's the changeover."* **Assessment: compliant.** No year is pinned, nothing is anchored
to a Halo-canon event, and the months are how station life is measured. *"The sixteenth"* is
the closest approach and is still a rota date, not a calendar date. **No action — recorded so
the next auditor does not re-open it.**

**W-13 · Jameson.** He does not appear in Ch.6, 7 or 8 at all — not in person, not by voice,
and his name is not spoken. The last on-page Jameson is Ch.4's signed commendation
(*"Cell showed excellent judgment and restraint. Well done."*). **The institutional/never
cartoonish guardrail is intact and untested across the pipeline chapters.** `outline:ch-10` is
where it gets its real test.

**W-14 · The book still ends on suspicion.** At the end of Ch.8, Vexx has an anomaly he can
date (Holst's tag reissued eleven months after his file closed), a reinterpretation of how it
reached the ground, and no link whatever to Rx or Jameson — and Rx says so out loud:
*"That's the whole of it. It isn't evidence of anything."* **No revelation has leaked forward.**
Verified.

---

## 9. WHAT I CHANGED IN `ENTITY_STATE.yaml`

The file was at `mode: BUILD`, `chapters_tracked: [1,2,3,4,5]`. I ran an UPDATE pass over it.
**It re-parses cleanly under `yaml.safe_load`.** A pre-edit copy is in the session scratchpad.
Counts moved from 20→29 characters, 9→12 locations, 13→20 objects, 3→4 secrets, 5→8 timeline
entries, 6→14 conflicts.

**Principle applied:** only entries where the manuscript is unambiguous were written as facts.
**Everything this audit judged to be a defect in the prose was recorded under `conflicts` and
deliberately NOT written into the entity facts** — so the file does not launder an error into
canon.

### Metadata
- `chapters_tracked` → `[1,2,3,4,5,6,7,8]`; `chapters_planned_not_tracked` → `[9…26]`.
- `mode` → `UPDATE`; `last_updated` → `2026-09-09`; `last_updated_by` → continuity-guardian,
  with an `update_note` pointing at this report.
- `open_conflicts` 6 → **11**; `needs_review` 3 → **2** (`characters.corwin` cleared).

### Characters added (9)
`merrick` (full block — physical, traits including the reserved self-echo device, the Ivo/Tomas
split, the eleven-month watch, the book, October, relationships, location log, knowledge, and
the arc note that he is **not** a conspiracy victim) · `tomas` (with an explicit
*do-not-resolve-him-casually* arc note) · `ivo` · `hallam` (with a note that both of his two
uses are spent) · `relay-station-commander` (including the `R/H — MERRICK` board error that
causes the failed stack) · `relay-hall-boy` · `rehab-clinician` · `corwins-daughter`
(**promoted from `planned`**) · `deric-holst` (**promoted from `planned`**, with all six archive
facts and the `photo?` pencil marginalia).

### Characters updated with Ch.6–8 material (8)
`vexxcerian` — a `ch6_8_additions` block with a three-chapter location log, **nine new
knowledge acquisitions** each with method and source, and — most importantly — an explicit
**`knowledge_NOT_gained`** list: the third word, the contents of Merrick's notebook, and who
filed the third concern. That list is the guardrail for Ch.9+.
`rx` — seven Ch.6–8 behaviours (the total silence at the rehab track; ticking "researcher"; the
tin-roof confabulation and the flat correction; the double pre-emption; the tally; "I didn't see
that"; his deliberate plot-uselessness in Ch.8), plus a `note` that no stage is spent and a
`signature_tic_status` field recording that the too-quick denial is absent from Ch.6–8 (W-05).
`goliath` · `spector` · `paladin` (with a `count_note` verifying the "third time" against Ch.2
and Ch.4) · `aglaope` · `voss` · `corwin` (a full `ch6_additions` block: the restored weight,
the grammar reflex on the page, the recantation recorded verbatim with
`holds_it_sincerely: true` **and** `vexx_does_not_believe_it: ch-06:p120` side by side, the
daughter, the refused AI name, and the one detail he disowns).

### Locations added (4)
`rehabilitation-station` (nine facts; transit distance; the note that its decency is the point
and must never be made sinister) · `relay-station-plateau` (seven facts including the relay
hall's two-door geometry, which is what the failed stack turns on) · `kettle-ridge` (with a
note that Echo naming it is the correct device owner) · `hallows-bottom`.

### Objects
**Added 8:** `merricks-notebook` (three-stage chain of custody, and an `unresolved` field saying
plainly that Vexx does not open it — see O-01) · `holst-issue-record` · `corwins-letters` (with a
`debt` field) · `corwins-ai-casing` (with the withheld-name constraint) ·
`the-visitor-log-signature` · `paladins-instrument-file` · `rxs-marksmanship-tally` (cross-linked
to `CF-11`) · `the-relay-hall-chain` (with a note that the maker's stamp is a deflection, not a
clue, so no later skill turns it into one).
**Rewritten 3:** `dented-dog-tag` — its three `planned_developments` marked `NOT ON THE PAGE` are
now `developments` marked `ON THE PAGE`, with a new `reinterpretation` block (before: planted as
theatre → after: dropped by a man who came back for it and missed) and an explicit
`still_not_proven` quoting Rx. `corwins-fragments` — stage 6 of the chain of custody added
(the Ch.7 trestle), quoting Vexx's own inventory and flagging that the data chip is missing from
it. `half-melted-data-chip` — cross-linked to `CF-12`.

### Secrets
- `rx-was-murdered` — added `state_at_end_of_ch8`: harder in substance, unchanged in kind;
  nobody new told; Rx still unconnected.
- **New: `rx-runs-hot-on-certain-words`** — the Ch.8 information-flow anchor. Records the full
  routing (Spector → Goliath → Vexx, once, in a corridor), that Spector chose *not* to use
  maintenance telemetry and *not* to go to Vexx directly, that Goliath holds two of three words
  and Vexx holds two of three, and a hard constraint that **no later chapter may assume Vexx
  holds the third**. Seven other characters explicitly recorded as `level: none`.

### Memory-unlock ladder
Four Ch.6–8 precursors appended to `stage_3.precursors_already_on_the_page`, plus a new
`ch6_8_audit_2026_09_09` field stating that stages 1 and 2 are not duplicated, stage 3 is
unclaimed, and carrying the two standing cautions from §0.4 in full.

### `planned` block
`holst-d`, `merrick`, `corwins-daughter` and `the-rehabilitation-facility` removed and replaced
with promotion comments pointing at their new homes. `reclamation` gained a `status_2026_09_09`
field recording that it is now planted on the page, unglossed, and still unsolved.

### Conflicts
- **`CF-04` closed** (`status: RESOLVED`) — Ch.6 delivers Corwin's grammar-correction device
  *and* retro-installs the missing Ch.3 anchor as a memory (*"There were fewer of them than the
  report says. Not less."* — the character-bible's exact sample line, placed in the jungle on
  Paladin's back and explicitly never written down) *and* delivers the daughter. **No prose
  change needed.** This was the second-largest open conflict in the file and Ch.6 solved it
  without being asked to.
- **Eight new conflicts opened**, each with canonical value, quoted counter-evidence, source
  refs and a recommended fix: `CF-07` deployment count · `CF-08` Ch.6 timeline squeeze ·
  `CF-09` apron head-count · `CF-10` Ch.8 POV + stack arithmetic · `CF-11` Rx/Spector counting
  device · `CF-12` the data chip · `CF-13` Holst's first name · `CF-14` orthography.
- `CF-01`'s stale conflict entries were **left in place** (they are `status: RESOLVED` at the
  parent level) but note that the two prose lines they quote — including a **Jameson-POV
  sentence in Ch.5** — no longer exist in the manuscript. Flagged in §0.1 so nobody restores
  them from the file.

**What I did NOT change:** no chapter file was touched, `CF-03`, `CF-05` and `CF-06` were left
open as author decisions, and no defect this audit found was written into the entity facts.

---

## 10. RECOMMENDED DISPATCH ORDER

1. **B-01** (orthography, Ch.6–8) — mechanical, largest, and cheapest to do first before other
   edits multiply the affected lines.
2. **N-01 + N-02 + N-03** (Ch.8 POV, stack arithmetic, apron count) — **one pass, one agent.**
   All three are inside two scenes and Ch.8's floors and ceilings mean it should be opened once.
   Net word change ≈ −25, which helps against the 6,200 target.
3. **N-04 + N-05 + N-06 + N-11** (Ch.6: timeline, the clinical note, Corwin's self-echo, the
   day count) — one pass. Net ≈ −40.
4. **A-01 + A-02** (Ch.2 and Ch.4, one word each) — author's prose; confirm before applying.
5. **N-07 + N-08 + N-09** (cross-chapter repetition, mostly Ch.8) — with the ALLOWLIST additions
   in the same commit, or they will come back.
6. **D-01 + D-02 + D-03 + D-04 + D-05** (docs) — no manuscript risk; do them while the chapter
   edits are in flight.
7. **N-10** and **O-01/O-02** — author/architect decisions. Ask; do not invent.

**Re-run this audit after step 3.** N-01 and N-04 both move things other chapters measure from,
and a post-revision pass over Ch.4–8 is cheap insurance.
