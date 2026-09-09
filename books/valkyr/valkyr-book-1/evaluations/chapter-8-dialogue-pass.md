# Dialogue Pass — Chapter 8: Merrick

Scope: dialogue only. No narration paragraph was touched (verified: narration sentence
count, median, `>=40w` and `<=6w` are byte-identical or better after the pass — see METRICS).
No idea, beat, plot point or outcome changed. The protected final 898 words (from *"The
breach bag was still against the relay hall wall"*) were left entirely alone; the one
cover-the-name failure that block contained was resolved by editing its *counterpart* earlier
in the chapter instead (see V07).

---

## 1. COVER-THE-NAME TEST

Method: every quoted turn plus every unquoted interface turn was stripped of attribution,
tag, beat and paragraph context, and read cold in sequence. A turn scores **DISTINCT** if it
lands on exactly one character on first read; **WEAK** if it lands only once the surrounding
turn-taking is restored; **INDISTINCT** if it lands on nobody, or on the *wrong* character
because it is wearing another character's device.

**Turns counted: 131** (125 speech-bearing paragraphs + 6 interface turns — Rx ×5, Echo ×1).

| | DISTINCT | WEAK | INDISTINCT | Strict hit rate | Tolerant hit rate |
|---|---|---|---|---|---|
| **Before** | 82 | 34 | **15** | **62.6 %** | 88.5 % |
| **After**  | 95 | 35 | **1**  | **72.5 %** | **99.2 %** |

Per character, after the pass:

| Character | Turns | Distinct | Weak | Indistinct | Note |
|---|---|---|---|---|---|
| Merrick | 17 | 17 | 0 | 0 | self-echo carries every turn |
| Zeus | 16 | 14 | 2 | 0 | six turns rebuilt — see V04–V10 |
| Goliath | 24 | 19 | 5 | 0 | two device bleeds removed |
| Paladin | 14 | 11 | 3 | 0 | "It's fine." removed from his mouth |
| Gaia | 12 | 9 | 3 | 0 | separated from Aglaope — V16 |
| Vexx | 17 | 10 | 7 | 0 | procedural short turns ("Copy", "Social") |
| Aglaope | 3 | 3 | 0 | 0 | "That's not X" bleed removed |
| Bastion | 7 | 6 | 1 | 0 | |
| Spector | 4 | 4 | 0 | 0 | |
| Echo | 1 | 1 | 0 | 0 | |
| Rx | 5 | 5 | 0 | 0 | |
| Voss | 0 (reported speech only) | — | — | — | summary register, correct |
| unassigned / role | 11 | — | 11 | 1 | crew chief, the kid, the bay chorus |

**The one remaining INDISTINCT:** the unattributed *"It's the same water it was last month."*
in the opening bay chorus. Left deliberately — it is ambient crew noise before the cell has
been sorted for the reader, and the reply pattern hands it to Gaia four lines later. Flagged,
not fixed.

---

## 2. EVERY LINE CHANGED (18 edits, all inside quoted dialogue)

### Device-bleed removals (the tic budget)

**V01 — PALADIN.** *Rx's one capped device, spoken by another character.*
> "It's fine." → **"It's working."**
> (and BASTION's reply) "It was fine on Tuesday." → **"It was working on Tuesday."**

Rx's tic is the too-quick denial and the literal phrase is capped at 5 with 3 spent. Paladin
producing *"It's fine."* verbatim in answer to a body-check is the exact collision
`character-bible.md` warns about, and cold-read the line assigns to Rx. *"It's working"* is
also better Paladin: he reports function and position, not condition.

**V02 — GOLIATH.** *Spector's countdown, verbatim from Spector's own sample line.*
> "Taking it as it is. Three. Two. Set—" → **"Taking it as it is. Round the frame, then in. Set—"**

Counting, numbering and sequence belong to Spector alone. Replacing the count with the craft
problem is Goliath's axis, and it strengthens the failed stack: he *calls* the frame, and the
frame still costs them the half-second the narration goes on to describe.

**V03 — GOLIATH.** *Echoing Merrick's own phrase, inside Merrick's scene.*
> "Lifting plate in February," → **"That's a job for two,"**

Merrick's involuntary self-echo must not have a companion. Goliath picking up his phrase put a
second repetition figure in the same six lines. The replacement is trade-practical (Goliath's
register) and it makes Merrick's *"I'll be lifting plate in February"* mean *alone*, which is
the assessment's finding arriving early and unremarked. Also clears the
`voice_wear_check` self-repeat flag on "lifting plate in february" (3× → 2×).

**V04 — ZEUS.** *He never asks the obvious question, and he does not use question marks.*
> "What was the name?" → **"Which shift is he on,"**

Zeus steps past the slip and asks a small operational question that assumes Ivo exists — so
the correction has to come out of Merrick's own mouth (*"There's an Ivo on the north shift.
Was."*). Wrong-order questioning, which is his whole method.

**V05 — ZEUS.** *He never asks why, in the entire book.*
> "Why not." → **"Then I'm wrong."**

A hard card violation, and the fix is better: conceding to draw the man out is kindness used
as technique, which is what the outline says this scene is. Merrick's answer already begins
*"Because…"*, so nothing downstream moves.

**V06 — ZEUS.** *He never repeats anything — the absolute split against Dessen.*
> "That isn't what I asked, and I'll ask it again in a minute anyway, so take your time with it."
> → **"That isn't what I asked, and I'm in no hurry, so take your time with it."**

The original had Zeus announce that he would repeat a question, in the chapter where a
repetition-bearing character is on the page. The replacement keeps the relentlessness (he
will sit there) without putting him on Dessen's axis.

**V07 — ZEUS.** *Exact-line duplicate with Vexx, later in the chapter.*
> "Which two." → **"Who else can go to it,"**

Vexx says *"Which two."* to Goliath in the corridor scene — inside the protected block, and
his line is the better-earned of the two. Changing Zeus's instead removes the duplicate, and
his new line motivates the full watch rotation that Merrick then produces.

**V08 — ZEUS.** *Second echo of Merrick's words in one scene.*
> "In the book." → **"Where."**

One instance of Zeus holding the man's unfinished sentence open is technique
(*"It isn't fair to."* — kept, and it is the best line in the scene). Two makes it a habit and
starts competing with the symptom.

**V09 — ZEUS.** *Rx's witness-request shape, flagged as WATCH for Ch.8+.*
> "I want that said out loud, because it will not survive into the file:"
> → **"It will not survive into the file, so it gets said here:"**

*"I want that on the record" / "I want that understood"* is Rx's Ch.7 structure and the bible
says catch any recurrence at dialogue-polish. Recast as a flat impersonal reframe, which is
colder and more Zeus — and colder is what separates him from Paladin two lines later.

**V10 — ZEUS.** *Goliath's axis: trade vocabulary applied to moral positions.*
> "Those are two different transactions and you're owed both."
> → **"Those are two different things and you're owed both."**

**V11 — AGLAOPE.** *The logged "That's not X. That's Y" bleed — owner: Zeus.*
> "He's been waiting for somebody to come. That's not the same as knowing why."
> → **"He's been waiting for somebody to come. He doesn't know what for."**

Aglaope is named in the bible as one of the characters the shape had already spread to. The
replacement is plainer and shorter, which is her card (fewer words than anyone else in the
cell).

**V12 — BASTION.** *The same reframe shape, and a false lead.*
> "Sit down. Not because you're hurt. Because you're going to be dizzy in about forty seconds…"
> → **"Sit down. You're not hurt. You're going to be dizzy in about forty seconds…"**

Bastion leads with the body fact rather than a corrective structure that belongs to Zeus.

**V13 — SPECTOR.** *Shortest sentences of any voice; no filler.*
> "…a spanner on the floor that shouldn't be on the floor and that's the whole of my complaint."
> → **"…a spanner on the floor that shouldn't be on the floor. That's my whole complaint."**

**V14 — SPECTOR.** *A second device on a character already capped at one.*
> "…to be able to say the shed is fine. Say the shed is fine." → **"…to be able to say the shed is fine. Say it."**

Spector holds the count. Giving him self-repetition as well, in the chapter where
self-repetition is a medical symptom, muddies both.

### On-device correction

**V15 — MERRICK.** *Put the echo on its stated shape (his own last three words).*
> "It's all in the folder," → **"In the folder,"**

The other seven echoes are two- or three-word tails. This one repeated a whole six-word
sentence, which reads as a man re-issuing information rather than a man's mouth doing
something without him. Now 8 of 8 are the same shape.

### Voice separation (the pair the brief named)

**V16 — GAIA.** *Separated from Aglaope: Gaia states facts about the world, Aglaope states facts about you.*
> "The others won't, because they like him — and I mean that they like him, not that they're covering."
> → **"The others won't. They like him. Nobody's covering."**

The original had Gaia interpreting people's motives across an em-dashed appositive — Aglaope's
axis in Aglaope's syntax, twelve lines before Aglaope speaks. Three clipped facts is Gaia's
card (fastest speaker, no adjectives), and the em-dash comes back into the budget.

*(V01 counts as two line changes, V16 as one. Total lines touched: 18.)*

### Tag / beat work
- Tags replaced with beats: **0.** Every beat in this chapter is inside a narration paragraph
  and the rhythm gates have no slack. The existing beat:tag balance is already good — the
  chapter runs almost no bare "said" without either a beat or a deliberate silence.
- Tags removed: **0.**
- Adverbs in dialogue tags: **0** before, **0** after.
- One typographic repair inside a changed tag: `"…is he on." Zeus said` → `"…is he on," Zeus said`.

---

## 3. MERRICK'S REPETITION — COUNT

**8 canonical self-echoes** (his own last two or three words, after he has said them):

| # | Line | Echo |
|---|---|---|
| 1 | plant house, first meeting | "Round the changeover." |
| 2 | after Goliath's "Happens" | "It does." |
| 3 | the folder | "In the folder," *(was "It's all in the folder," — V15)* |
| 4 | the assessment, the book | "Written down." |
| 5 | after the search fails | "Before dark," |
| 6 | the ramp, to Paladin | "Before dark." |
| 7 | the ramp, to the crew | "About all this." |
| 8 | the head of the ramp | "Sorry, Tomas." |

Plus **1 forward stammer** — *"He rotated out. He rotated out at the start of the winter…"* —
which is the same symptom arriving mid-flow rather than as a tail. Kept: deterioration should
not be metronomic.

**Distribution:** 4 in the plant house / assessment (over ~1,600 words), then 4 clustered in
the extraction (over ~300 words). The acceleration is the chapter's argument and it is not
overdone at this density; the second cluster is the anchor the outline asks for.

**Never commented on.** After V03 and V08 no character picks up, mirrors or completes any of
Merrick's repetitions, and the narrator names the behaviour nowhere. The one place the
narration comes close — *"The second time was quieter than the first… as though the sentence
had finished the first time"* — describes the sound without diagnosing it, and it is the
reader's first encounter with the symptom, so it earns its place. **Flagged, not changed:**
that sentence also carries the chapter's only *"as though"*, which voice-dna treats as
effectively banned (budget ≈1 per 6,000 words — it is exactly at budget, but it is narration
and outside this pass).

---

## 4. ZEUS'S ASSESSMENT — THE CENTRE

Surface: sleep, a bus bar, a chief with a story about a fan belt. Real: a man being weighed.

Nothing in the scene now states what is happening. The three lines that came closest have
been rebuilt: V05 removed the one direct *why*, V06 removed Zeus announcing his own
procedure, V08 removed the second echo. What remains carrying the subtext is entirely
behavioural — Zeus conceding expertise (*"Then I'm wrong."*), Zeus refusing to look at the
door, Zeus getting down on the plate steel to look under a bench for a book he already knows
is not there, and Zeus not once saying it does not matter. The kindness is the technique and
the technique is never named.

**Cover-the-name on the assessment scene: PASS, 26/26.** Zeus and Merrick cannot swap a single
line — Zeus never repeats and never asks why; Merrick cannot stop repeating and answers a
different question than the one asked.

---

## 5. PALADIN'S OBJECTION

Unchanged, and it should be. It is preceded by his own ground —
*"He's stood a watch for eleven months. In a place with no relief and no cover and eleven
people in it."* — which is his card exactly (positions, and who is covering them, never a
number used as a tally). The refusal then runs his structure with no deviation: restate the
opponent's case intact, concede each part out loud, then **"No."**

The one change in his vicinity is V09, which pulled Zeus's reply *away* from advocacy and into
flat institutional reframe. Before the pass, Zeus's *"I want that said out loud"* and
Paladin's defence of Merrick were arguing on the same axis and could be swapped. They cannot
now: Zeus reports what will not survive the file; Paladin argues about a man.

---

## 6. PAIRS STILL TOO CLOSE

1. **Goliath ↔ Paladin, in the coffee/instrument volley** (*"Bar three." / "Bar three." / "It's
   a different bar three." / "It is not a different bar three."*). Assignable only from the
   turn-taking — the joke *requires* the identical line, so this is a WEAK I would not fix, but
   it is the chapter's largest block of interchangeable dialogue and a reader skimming will not
   hold the speakers apart. **Recommend to the Writer, not to this pass.**
2. **Vexx's procedural monosyllables** (*"Social." / "Copy." / "Take it as it is." / "It's going
   on it."*). Seven WEAK turns. Correct for a commander on the net, and gating them would push
   his dialogue away from the author's own practice. No action.
3. **Bastion ↔ Spector, one word.** Bastion's *"Then it costs you nothing to humour me"* and
   Spector's *"Twenty-two minutes is what it costs"* both reach for cost. Bastion's is idiom,
   Spector's is literal valuation, and they are fifty lines and two scenes apart. Left alone;
   logged because six AIs sharing a service cadence is the book's largest convergence risk and
   this is the only place in Ch.8 where two of them touch the same vocabulary.

**Judged resolved:** Zeus/Paladin (V09 + V10, plus V05/V06 pulling Zeus off Dessen's axis) and
Gaia/Aglaope (V11 + V16).

---

## 7. NOT DONE — flagged for the Writer / chaos-engine

- **Rx's marksmanship tally is missing.** `outline.md` Ch.8 lists it under *Character chaos*
  ("Rx's marksmanship tally, deployed at maximally wrong moments (Ch.8, 13, 26)") and
  `character-bible.md` repeats it. There is no instance in the chapter. Adding one is a beat,
  not a dialogue repair, and it would cost words the rhythm gates have no room for. Either the
  chaos-engine places it or the outline entry moves to Ch.13/26.
- **The chapter's dominant dialogue figure is the two-speaker echo** — *"Bar three"*,
  *"Somebody dropped/left a spanner"*, *"Taking it as it is"*, *"the shed is fine"*, *"It isn't
  fair to."*, *"All right"*. This pass removed three of them (V03, V08, V14) to protect Merrick's
  symptom. What remains is deliberate and works, but it is at its ceiling: one more added
  anywhere in the chapter and the symptom starts reading as house style.

---

## 8. METRICS AFTER THE PASS

`python3 tools/style_check.py` · `grammar_check.py` · `voice_wear_check.py` — **all three clean.**
`git diff --stat`: **1 file changed.** Chapters 1–7 byte-identical and their style-check output
unchanged.

| Metric | Ceiling / floor | Before | After | Direction |
|---|---|---|---|---|
| `and` per 1k | ceiling **24.0** | 23.3 | **23.0** | −0.3 (headroom gained) |
| em-dash per 1k | ceiling **12.0** / floor 8.5 | 11.7 (67) | **11.6 (66)** | −1 dash, still mid-range |
| `the way` | ceiling **5** | 5 | **5** | untouched — all five are in narration |
| comma per 1k | floor 58.0 | 72.1 | **72.3** | fine |
| somebody/nobody per 1k | ceiling 6.5 | 5.1 | **5.3** | fine |
| simile per 1k | ceiling 5.0 | 1.4 | **1.2** | fine |
| adverb per 1k | ceiling 20.0 | 4.0 | **4.0** | unchanged |
| narration sentences | — | 213 | **213** | **unchanged** |
| narration median | floor **13.0** | 13 | **13** | **unchanged** |
| narration ≥40w | floor **11.5 %** | 11.7 % | **11.7 %** | **unchanged** |
| narration ≤6w | ceiling 33.0 % | 31.0 % | **31.5 %** | +0.5 (one dialogue-adjacent sentence) |
| semicolons | 0 | 0 | **0** | |
| straight quotes / apostrophes | 0 | 0 | **0** (the single `'` is in the pre-existing editorial comment, exempt) | |
| dialogue lines : narration | reported | 224 (1.05:1) | 226 (1.06:1) | |
| words | — | 5,717 | **5,697** (file 5,794 with comments) | −20 |

Every narration figure that was at a limit is at the same value it was before the pass, because
no narration paragraph was edited. The chapter's closing line
*"Concern raised by subject's own section on three separate occasions, the most recent in
writing."* is verified **character-identical** to its first appearance at the top.

Not committed.
