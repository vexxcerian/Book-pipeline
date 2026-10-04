# Continuity Audit — Valkyr: Book One, Chapters 1–11

**Date:** 2026-10-03
**Scope:** full manuscript as it stands — `chapter-1.md` … `chapter-11.md`, **38,398 words** (`wc -w`)
**Audited against:** `../../../SERIES-BIBLE.md` (outranks all), `../../CLAUDE.md`,
`outline.md`, `character-bible.md` (§STANDING OFFENCES, §THE ONE CARVE-OUT),
`foundation.md`, `ENTITY_STATE.yaml`, `feedback/progress.md`, `tools/style_check.py`
**Supersedes nothing in:** `evaluations/continuity/ch1-8-audit.md` — that report's closed
findings are not re-reported here; everything it left open was re-checked and the status of
each is in §1.

**Totals:** 0 BREAKS THE BOOK · 11 needs a fix · 14 worth a look · 12 deliberate-and-fine

**Chapter status, applied throughout:**

| Chapters | Standing | What this report does |
|---|---|---|
| **Ch.1** | author's, **LOCKED** | report only, never a proposed edit |
| **Ch.2–5** | author's prose, light editor pass | propose minimally, say what is at stake |
| **Ch.6–11** | pipeline-written | propose freely |
| **Ch.11** | pipeline, **PRE-POLISH** (no dialogue pass, no hook pass, no disruptor, no eval, no writer report) | judged as a first draft |
| docs | `ENTITY_STATE.yaml`, `outline.md`, `SERIES-BIBLE.md`, `CLAUDE.md`, `character-bible.md`, `tools/style_check.py` | fixed here or proposed there, never in the prose |

> **⚙️ MECHANICAL HEADROOM — read before dispatching any prose fix.** Measured with the gate's
> own tokenizer, 2026-10-03:
>
> | Ch | em-dash /1k (ceiling 12.0) | narration median (floor 14.0 / ceiling 18.0) | headroom |
> |---|---|---|---|
> | 6 | 10.8 | 14.5 | em-dash: ~5. **median: 0.5 above the floor — do not shorten.** |
> | 7 | 9.9 | 11 `[PUNCH — exempt]` | free |
> | 8 | **11.8** | 14.0 | **em-dash: ~1. Do not add one.** median at floor — do not shorten. |
> | 9 | 9.8 | 14 | em-dash ~7. **median at the floor — do not shorten.** |
> | 10 | 10.5 | 17 | em-dash ~6; median has 1.0 of room up and 3.0 down |
> | 11 | **11.5** | **18 — EXACTLY ON THE CEILING** | **em-dash: ~1. Do NOT lengthen a narration sentence.** |
>
> Consequence, stated once: **in Ch.11, add only SHORT sentences and no em-dashes.** A short
> addition moves the median *down*, which is safe. In Ch.8 and Ch.11 an added em-dash breaches
> the gate on its own. Every fix proposed below names the metric it moves.

---

## 0. VERDICT ON THE TWELVE SPECIFIC TESTS

### 0.1 Timeline, built from the text — **it holds, with four dates wrong in Ch.10 and one leftover in Ch.6.**

The chronology below is reconstructed from the prose only, anchored on *jungle = t0* (Ch.3).
Nothing in the manuscript, `STATE.yaml` or `outline.md` declares a total elapsed span, so this
table is now the book's clock. It is also in `ENTITY_STATE.yaml` as `timeline[9..11]`.

| Point | Anchor in the text | t (jungle = 0) | Absolute (derived) |
|---|---|---|---|
| Rx's death | Ch.1 | t − ~4y 4m | — |
| The gray room | Ch.1, "four years to the day" | t − ~13 wks | ~July |
| Jameson's office | Ch.2, "three weeks into his own re-entry" | t − ~10 wks | ~late July |
| Goliath paired | Ch.2, +2 wks +4 days +3 days | t − ~7 wks | ~August ✔ ("It's been the water since August") |
| Phantom slip | Ch.2, "three weeks" after the pairing | t − ~4 wks | ~September |
| Roster complete | Ch.2, "the following six weeks" | t − ~3 days | ~October ✔ ("that autumn") |
| **Ch.3 — deployment #1** | "First deployment as a full cell" | **t + 0** | ~October |
| Ch.4 debrief | "three weeks after the jungle" | t + 3 wks | ~November |
| **The release** | Ch.4, "two days later" | **t + 3.5 wks** | ~November |
| **Ch.4 — deployment #3 (Reyes)** | "six weeks later" | **t + 9 wks** | ~December |
| **Ch.5 — deployment #4** | after Reyes; "two nights later" | **t + ~10 wks** | ~late December |
| Ch.6 | "eleven weeks earlier"; Corwin "eight weeks into" rehab | t + 11 wks | ~early January |
| Ch.7 | "two months ago" (the Ch.4 table) | t + ~12 wks | ~January |
| **Ch.8 — deployment #5** | "a corridor argument seven weeks earlier" (Ch.5) | **t + 17 wks** | ~February |
| Ch.9 | days after Ch.8; Thu–Sun (puzzle Tue/Wed → log goes up Monday) | t + ~17–18 wks | ~February |
| Ch.10 | "a fortnight after a transport had gone out" | t + 19 wks | ~late February |
| Ch.11 | after Ch.10, **interval unstated**; boot propped "a week" | t + ~20 wks | ~March |

**Where it breaks:** five interval statements contradict the table they sit in — one leftover
in Ch.6 (**N-01**) and four in Ch.10 (**N-02**, **N-03**, **N-04**). All five are pipeline text.
Two more are the author's and are older than the previous audit (**A-01**, **A-02**, both still
unfixed).

**Ch.9's internal clock — rebuilt, and it now closes. Verified minute by minute.**

| Time | Event | Source |
|---|---|---|
| 01:10 | Vexx enters the records annex; Zeus is already there | ch-09 ¶18 |
| ~02:10 | "Vexx had said good evening, then nothing else for an hour" | ¶18 |
| 02:10 → 02:40 | "Zeus asked four more over the next half hour" | ¶44 |
| 02:40 | Zeus: "you've been typing an hour and a half" — 01:10 + 1h30 ✔ | ¶50 |
| 02:54 | "a hundred and four minutes at two in the morning" — 01:10 + 104 ✔ | ¶134 |
| 02:30 | Aglaope in the mess "since half past two"; urn off "since one" ✔ | ¶158, ¶218 |
| ~02:55 | Vexx reaches the mess | — |
| 04:00 | "The mess at four in the morning" ✔ | ¶248 |

**No gap, no overlap, no double-counted interval.** This is the cleanest internal clock in the
manuscript. One season wobble inside it — see **W-04** ("at Christmas").

### 0.2 Deployment count — **consistent, and Ch.11 does not re-number anything. Verified clean.**

`CF-07` is **closed**: `outline.md` §Chapter 8 Premise now reads *"The cell's **fifth**
deployment"*, matching its own beat 5 (*"the third time in five missions"*) and the prose.

Ch.11's references are all unnumbered and all correct:

- *"**At the relay hall**, I stood at that corner with a full view of a wall"* — Ch.8, ¶200
  verbatim (*"from the corner, forty metres away, where she had been standing the entire time
  with a full view of a wall"*). ✔
- *"You've had something since before **the jungle**"* — Ch.3. ✔
- *"You pulled our files again after **the jungle**"* — Ch.3. ✔
- *"**One of the jobs we've run** wasn't the job we were briefed"* — deliberately unspecified, no
  ordinal. ✔

**Nothing in Ch.11 numbers a deployment.** The count is safe in the prose and now correct in the
outline. One note under **W-05** on which job Vexx means.

### 0.3 Information flow — **the test passes on all three limbs, but the brief's premise is wrong.**

> ⚠️ **"Ch.11 is the first time Vexx tells another human being anything" is FALSE, and the
> chapter that disproves it is the author's.** Ch.5, ¶65: *"'I think someone in this program
> killed my brother,' he said, quiet, the words strange and heavy in his own mouth, **the first
> time he'd said any version of it out loud to another living person**."* He names Jameson (or
> rather Aglaope does, and he does not deny it), and he gives her more than Gaia gets in Ch.11.
>
> **Ch.11's actual first is narrower, and better:** the first time Vexx hands anyone an
> **operational claim about a mission the cell ran**. Ch.5 is a theory about his brother; Ch.11
> is an allegation about work they did together. Keep the two straight in future briefs. The
> distinction is recorded in `ENTITY_STATE.yaml` at `characters.aglaope.arc_notes_ch9`.

**(a) Nothing earlier already told Gaia, or anyone else, what Ch.11 gives her.** Checked
chapter by chapter:

| Who | Holds what, at the end of Ch.11 | How |
|---|---|---|
| **Aglaope** | the suspicion *in outline*, Jameson's name, since Ch.5. **Not the evidence** | Vexx told her (Ch.5) |
| **Gaia** | since Ch.5, *"I suspect something"* + the promise *"you'll be the first to hear it"*. Since Ch.11, **one sentence** | Vexx told her |
| **Zeus** | that Vexx is working something off-book, at 02:00, in an open index, with the door shut | **inferred, never told.** He did not report it |
| **Goliath** | two of Spector's three words; that Rx runs hot | Spector told him (Ch.8) |
| **Dessen** | that Vexx took the material and kept it, and lied once about an extension | documentary + Vexx |
| **Jameson** | **NEW IN CH.10:** that Vexx took the Corwin material out of a lock, kept it in a residence under a lamp, never returned it | he read Dessen's finding |
| **Paladin, Hollow, Bastion, Spector, Echo, Requiem, Voss** | nothing of the Rx thread | — |

**Ch.5's prior disclosure does not undercut Ch.11.** Ch.11 explicitly cashes the Ch.5 promise on
the page — *"You told me I'd be first." / "I did."* — which is the single best cross-chapter
callback in the manuscript and it is pipeline prose reaching correctly back into the author's.

**(b) Nothing in Ch.11 leaks more than the one sentence.** Verified exhaustively. Vexx gives
exactly one declarative and three refusals:

> *"One of the jobs we've run," Vexx said, "wasn't the job we were briefed."*
> *"Which one." / "No." — "Who briefed it." / "No." — "Have you got paper." / "Nothing I can give
> you." / "That's a no." / "That's a no."*

No name, no chapter, no object, no date, no paper. His **silence** also leaks nothing, because
Gaia's closing guess is itself unspecified (*"If it turns out to be what I think it is"*). The
narration's one disclosure — *"the reason for it not on her roster, not on anybody's roster these
four years"* — goes to the **reader**, not to Gaia, and it is the correct way to do it.

**(c) Gaia's mind-reading is 70 % right and 30 % wrong, and Vexx does not correct it.**
The chapter marks the split itself, in one clause: *"she had **the machine of it exactly right,
the reason for it wrong**, the reason for it not on her roster, not on anybody's roster these
four years."*

| | What she says | Verdict |
|---|---|---|
| **THE 70 % — the machine** | he has had something since before the jungle; he decided not to bring it to them, and *"you didn't decide it once, you've decided it every week since"*; *"You worked out what each of us would cost you. In your head, in order"*; *"You pulled our files again after the jungle"* | **right** |
| **THE 30 % — the reason** | *"It isn't that you think we'd sell you. It's that you want us able to stand in front of a woman with a notebook, say we didn't know, be telling the truth when we say it."* And: *"the only reason to [pull the files] is to find out which of us goes to command first."* | **wrong** |

**The 30 % is the motive, twice over:** she reads it as protecting the cell's deniability, and
reads the file-pull as command-succession triage. The real reason is **Rx** — *"not on anybody's
roster these four years"* — and she cannot see it because Rx is not a person on a roster.
Note the sharpness of the irony: she guesses *"a woman with a notebook"* without knowing that
Vexx sat in front of exactly that woman a fortnight earlier. That is reader-side and excellent.

**Vexx does not correct it.** *"he kept it where it was, and let her keep the rest."* ✔ And
`outline:ch-11` writer-warning (b) holds: he is not tempted, he is *relieved* — *"he had been
carrying it for weeks, cut down and cut down again, the size of a thing you could hand across a
corridor. Until it was out of him he had not understood what he had been trimming it for."* ✔

### 0.4 The drawer — **inventory consistent at every mention. CF-12 is closed. The move is not narrated.**

| Chapter | Named contents | Location |
|---|---|---|
| Ch.4 ¶23 | scorched armor plating fragment · half-melted data chip · dented dog tag | kitchen table, then "a drawer in his apartment" |
| Ch.5 ¶97 | "a dog tag, a data chip, a name" | "the drawer beside his bed" |
| Ch.7 ¶14, ¶78, ¶148 | the tag (on the trestle); "an armor fragment… a tag… a search history" | the apartment; drawer referenced as past |
| Ch.10 ¶82, ¶134, ¶256 | the plate "with the modification on the underside"; "the tag with the dent in one corner… among a watch strap, a cufflink, a torch he never used" | **"a drawer beside a bed in an apartment", "half a mile east"** |
| Ch.11 ¶206 | **"the tag… Then the scorched fragment of plating, the half-melted chip"** | **"the trauma pack in the bottom of his locker"** |

**Three items in, three items out. Nothing is in two places at any point. `CF-12` / W-08 from the
previous audit is CLOSED** — Ch.11's coda restores the data chip to the inventory by name after
Ch.7 omitted it. Recorded in the YAML at `objects.half-melted-data-chip.cf_12_closed_2026_10_03`.

**What does not hold is the geography, and it is the chapter's own anchor beat.** See **N-05**.

### 0.5 POV integrity — **Ch.9, Ch.10 and Ch.11 are CLEAN on both new rules. Ch.6 and Ch.8 are not.**

Swept Ch.9–11 for (a) narration knowing what Vexx does not yet know, and (b) narrator vouching.

**Rule (a) — flash-forwards: ZERO in Ch.9, Ch.10 and Ch.11.** Every `would` in the three chapters
is conditional, habitual-past, or Vexx's own projection:

- Ch.9 ¶76 *"anything he **would have** called a decision"* — conditional ✔
- Ch.9 ¶232 *"a thing she **would not be able** to put down again"* — Vexx's projection ✔
- Ch.10 ¶256 *"where it **would still be** tonight"* — Vexx's knowledge of where he left it. The
  closest line in the three chapters, and still inside his head ✔
- Ch.10 ¶322 *"a man who **would be** pleased with him"* — past habitual, at fourteen ✔
- Ch.11 ¶114 *"nowhere she **would rather** spend it"* — conditional ✔

**The Ch.10 measurement is confirmed: zero flash-forwards, and the gate condition is why.** None
of the three named tells (*he would understand later*, *he did not know it yet*, *it would be some
time before*) appears anywhere in Ch.6–11.

**Rule (b) — vouching: ZERO in Ch.9–11.** Two candidates, both permissible: Ch.9 ¶128 *"because
it was true, and no arrangement of the sentence made it less true"* (Vexx certifying his **own**
thanks — close third permits a POV character to know his own sincerity), and Ch.10 ¶256 above.

**Ch.6 and Ch.8 predate the rule and fail it. See N-08.** Ch.6 ¶32 contains the brief's own named
example verbatim.

**And the rule as written cannot apply to Ch.1–5.** See **D-04** — this needs scoping in the docs
before a later pass tries to "fix" locked prose.

### 0.6 The Ch.10 gate condition — **PASSES, and nothing in Ch.11 retroactively converts a line.**

*No Jameson line may be readable as a threat, a double meaning or a warning **where the second
meaning is available to him**.* Every Jameson line in Ch.10 was tested. All second meanings are
reader-side. The three closest, recorded so no later pass strengthens them:

1. *"Then what you have is a solitude problem. You're saying he was alone in it start to finish,
   with nothing in the file that could have stopped him."* — **the closest line in the chapter.**
   It is true of Vexx's investigation as well as of his paperwork. But Jameson is arguing
   procedure, against his own side's interest, and cannot know there is an investigation. The
   second meaning is not available to him. **Holds.**
2. *"That's the trouble with an honest man in a compliance room — he's the only person in it who
   can be talked out of his own position."* — he has just talked Dessen out of hers; the reader
   hears *I can talk you out of yours*. Reader-side. **Holds.**
3. The barometer — *"It'll be in off the water by tonight."* A storm as a figure for what is
   coming is entirely the reader's. **Holds.**

**Ch.11 converts nothing.** Verified by grep: **Ch.11 does not mention Jameson, Dessen, the
finding, Compliance or the property return at all.** There is one reader-side rhyme worth
recording and protecting — Jameson's *"a man who did the only honest thing available to him **in
a corridor** at the end of a very bad month"* pre-echoes a chapter in which Vexx does the only
honest thing available to him in a corridor. That rhyme is free and should be kept. **The small
problem inside it is that "in a corridor" has no referent — see W-06.**

**The institutional/never-cartoonish lock:** this is the strongest execution of it in the book.
Eight seconds of disproportionate, ugly temper, then an apology itemised into four parts, one of
which is *"The first part was temper. The second part I chose"* and another of which is the
procedural harm he cannot repair because *"there isn't a mechanism."* The scene makes him **more**
likeable, which is exactly the trap the guardrail asks for. **No action. Recorded as verified.**

### 0.7 The memory-unlock ladder — **no stage fired in Ch.9, 10 or 11. This is the important finding of the pass.**

**Jameson is physically present in Ch.10, at length, speaking loudly, at close range, in the same
room as Vexx and Rx — and Rx produces silence and nothing else.** Nothing legible surfaces. No
fragment of the refusal, no treeline, no audio artifact, no new fact. That is the **Ch.2 response
with no escalation**, which is the correct call and holds the lock. `ENTITY_STATE.yaml`
`memory_unlock_ladder.stage_3` now records it.

Two things it changes, and one is urgent:

1. **Mere proximity has now been spent THREE times** (Ch.2 ¶5, Ch.3 ¶5, Ch.10) — and Ch.10
   additionally spends *"his actual voice, close, at length, in the same room."* What is left as
   **novel** for Ch.13 is therefore only: **(a) an open channel rather than a room, (b) a live
   coordinating instruction rather than conversation, (c) in contact.** `outline:ch-13` beat 2
   specifies exactly those three. **It must not be softened by one word.** See **D-02**.
2. **Rx's reaction in Ch.10 is NOT a stage and must not later be recategorised as one.** It is
   silence, it is precedented twice, and the narration frames it as scoped to the scene — he
   speaks normally again in the corridor coda (*"It's been on the met page every day for four
   years…"*). Recorded.

**And the signature tic is back.** `W-05` from the previous audit is **CLOSED**: Ch.9 ¶144 gives
one clean, smooth, unremarkable firing — *"You've been quiet since I sat down." / "**Fine**, Rx
said. Then, at his ordinary speed: 'He's left-handed. Did you know that.'"* — the first since
Ch.4, which is exactly what the Ch.13 break needs in order to land. This was the previous
audit's most important open action and it was executed.

### 0.8 Rx's silence — **tracked, consistent, and thinning. Not forgotten; one silence is unmarked.**

Mentions of "Rx" per chapter, measured:

| Ch | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | **11** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| count | 23 | 16 | 9 | 9 | 5 | 2 | 11 | 4 | 2 | 4 | **0** |

**Ch.11 does not contain the string "Rx" anywhere.** The silence is nevertheless *registered* —
the coda is *"**You've gone quiet,** he said. / Nothing came back. The cursor on the pad by the
bed went on doing what it did."* So it is deliberate, not forgotten.

Each silence is marked on the page except one:

- **Ch.6** — marked: *"Rx did not say anything. He had not said anything since the corridor. Vexx sat with that."* ✔
- **Ch.10** — marked: *"and had said almost nothing since the audit-room door opened."* ✔
- **Ch.11** — marked in the coda, but **not in the 2,000-word corridor scene.** See **W-07**.
- **Ch.8 after ¶73 — NOT MARKED, and it is the worst of the four.** Goliath says *"Your Rx runs
  hot"* with Rx in Vexx's ear. Rx says nothing, in Ch.8 or in any chapter since, and Vexx has
  never raised it with him. See **W-07**.

**Also silent, and nobody has noticed:** **Hollow** and **Requiem** have not spoken since Ch.2 —
**nine chapters.** Hollow's device is *withholding until useful*, so his is arguable. Requiem
belongs to Aglaope, who carries two whole two-handers (Ch.5, Ch.9) with her AI mute. See **W-12**.

### 0.9 Canon guardrails — **all four intact.**

| Guardrail | Verdict |
|---|---|
| **No rampancy clock, in any form** | ✔ **Clean.** No timer, no fragmentation vocabulary, no "how long does he have", no decay-over-time framing anywhere in Ch.9–11. The one standing caution is still Ch.7's confabulated tin roof and nothing has made it worse. |
| **No hard in-universe calendar date** | ✔ **Compliant.** Ch.9–11 use days of the week (Tuesday, Wednesday, Thursday, Monday), seasons, "the new year" and "the sixteenth" (a rota date). No year is pinned, nothing is anchored to a Halo-canon event. **One borderline: Ch.9's *"still be out of tune at Christmas"* — see W-04.** |
| **Jameson institutional, never cartoonish** | ✔ **Passed its hardest test.** See §0.6. |
| **Book One ends on suspicion, not revelation** | ✔ **Verified, and it got stronger.** Vexx learns **no new fact** about Rx's death in Ch.9, 10 or 11. What changed is exposure and method, not evidence: Zeus has inferred that he is working something; Compliance has found against him permanently and the plate *"cannot now be put in front of anybody"*; Jameson knows he kept the material and intervened to save him; Gaia holds one unactionable sentence. Nothing has leaked forward. |

### 0.10 Entity consistency — **one genuine name collision; the boot's owner stays clean.**

New names in Ch.9–11: **Dessen** (registry ✔, spelling ✔), **Mr. Beattie**, **Curran**,
**Ansel / Anseth**, plus places **Sedge**, **Kell**, **Ridgeway**, and **"the Gullet"**.
Registry names checked across all 11 chapters: Vexxcerian/Vexx, Rx, Richard Jameson, Valkyr, the
Choosing, Goliath/Spector, Gaia/Echo, Paladin/Bastion, Zeus/Hollow, Aglaope/Requiem, Phantom,
Corwin, Reyes, Voss, Merrick, Holst — **zero variant spellings, zero drift.** Ranks, roles and
operator/AI pairings are consistent throughout.

**One collision: HALLAM is two different people. See N-07.**

**The boot's owner — verified never identified.** Ch.11 ¶50 *"It hasn't got an owner."* Goliath
narrows the *motive* (*"A boot at the bottom is what you use when you want to come through it
fast and not stop"*) and not the person. Vexx removes the boot and is still holding it at the end
of the chapter. **Nothing later identifies them.** Recorded as a hard constraint at
`characters.the-boots-owner`. The possible resonance with Ch.7's cold open (*ITEM: BOOT, COLD
WEATHER, PAIR. LINE 41 OF 60* / Rx: *"Those are boots"*) is left unglossed in both places, which
is correct — **do not connect them on the page.**

### 0.11 Orphaned threads — **Merrick's notebook landed and is closed. Six others are open and two are rotting.**

**O-01, Merrick's notebook — CLOSED, and closed well.** `outline:ch-09` beat 8 was added and
Ch.9 ¶48 delivers it:

> *"Merrick's notebook lay by his elbow, the rubber band round it slack now, like elastic out of
> a cuff. Bus bars. Runoff figures for four quarters, the wet months underlined twice. The
> Thursdays, every Thursday, three years of them — depot, no answer — depot, no answer — depot,
> called back, will send a man. Vexx had read it twice on the transport, once in his quarters,
> had brought it down with him tonight, had not opened it."*

**It contains nothing, and the nothing is the payoff.** Verified that nothing in Ch.10 or Ch.11
makes it matter. **Constraint recorded: the object must never later acquire a secret.**

The open ones are consolidated at **D-05** and in `ENTITY_STATE.yaml` `CF-24`.

### 0.12 Cross-chapter repetition — **three new findings, and §STANDING OFFENCE #7 is unbroken in Ch.9–10 but clean in Ch.11.**

| §SO | Rule | Ch.9–11 contribution | Verdict |
|---|---|---|---|
| **#5** | the tidying gesture is not everyone's | **Ch.9 adds 3** (Zeus ×2, Vexx ×1) | **N-10** — but ownership is arguably restored |
| **#6** | hands flat on a surface is Ch.1's gesture | **Ch.9–11 add 0** | ✔ clean |
| **#7** | generic-person manner attribution | **Ch.9 = 3, Ch.10 = 4, Ch.11 = 0** | **W-09** — Ch.11 is the first pipeline chapter since Ch.7 at zero |
| **#3** | only Spector counts aloud | Ch.11 Gaia (*"One laugh. Never two. I was in there five months"*) | **W-10** — fourth consecutive chapter, watch not finding |
| **#1** | Zeus never asks why | **repaired in Ch.9**, and Ch.9 goes further — Vexx asks *"Why."* and Zeus answers *"Ask a different question."* | ✔ closed |
| **#2** | Aglaope does not use Zeus's reframe | repaired; no clean instance in Ch.9 | ✔ closed |
| — | **NEW: device bleed onto Gaia in Ch.11** | Zeus's reframe in the chapter's first line; Vexx's term-correction ×2 | **N-09** |
| — | **NEW: the "eleven hundred" motif is at 5 against a cap of 3** | Ch.10 adds 2 | **N-06** |
| — | **NEW: a verbatim two-sentence structure duplicated Ch.6 → Ch.11** | | **N-11** |
| — | **NEW: "X with nothing in it" has become the narrator's emptiness formula** | Ch.10 adds 3, Ch.11 adds 2 | **W-08** |
| — | **NEW: "A pause with [X] in it", one per chapter, Ch.7–10** | | **W-08** |
| — | **NEW: Ch.11's opening and closing moves both duplicate earlier chapters** | | **N-12** |
| — | the involuntary sensory-memory intrusion (W-10, prev. audit) | Ch.9 ×2, Ch.10 ×2, Ch.11 ×1 | **W-11** — now 5 chapters, ~10 instances, still unregistered |

---

## 1. STATUS OF EVERYTHING THE PREVIOUS AUDIT LEFT OPEN

Re-checked against the files as they now stand. **Not re-reported below except where noted.**

| ID | Finding | Status now |
|---|---|---|
| **B-01** | two Englishes | **95 % applied; 4 survivors, and the gate cannot see them → N-13** |
| A-01 | Ch.4's "jungle clearing three weeks earlier" | **STILL OPEN** — unfixed. See **A-01** below |
| A-02 | Ch.2's "six weeks of acquaintance" | **STILL OPEN** — unfixed. See **A-02** below |
| A-03 | Ch.5's "that autumn" | still open; **recommendation stands: leave it** |
| A-04 | Ch.2's "six pairings" | still open; author's call (`CF-06`) |
| A-05 | Ch.2's Phantom scene disclaimed | unchanged; **no fix proposed**, still the best page-turn candidate |
| A-06 | Ch.5 lets Echo speak into Vexx's ear | unchanged — **and Ch.11 quietly repairs the mechanic:** Echo arrives *"on the net"*, a shared channel, not privately. Recorded. |
| N-01 | Ch.8 failed stack: POV + headcount | **FIXED.** Verified: "Vexx came in through the near door" gone; Zeus "had come in behind **them**"; four stacked = Vexx, Goliath, Paladin, Aglaope. `CF-10` closed |
| N-02 | Ch.8 assessment-scene POV | **FIXED.** "Merrick opened his mouth" gone; the "look at the door" clause cut |
| N-03 | Ch.8 "eleven people on the apron" | **STILL OPEN** (`CF-09`). See **N-14** |
| N-04 | Ch.6 lands on top of Ch.4 | **MOSTLY FIXED** — 3 of 4 instances converted; **one leftover → N-01** |
| N-05 | Ch.6 quotes a clinical file Vexx has not seen | **STILL OPEN.** See **W-13** |
| N-06 | Ch.6 spends Merrick's self-echo on Corwin | **DECLINED, with reasons, and the decision is recorded in progress.md.** Not re-opened |
| N-07 | "the whole of it" ×10 | **PARTIALLY APPLIED** — Ch.8 down from 6 to 3; **book-wide still 7 and the ALLOWLIST entry was never added → N-06** |
| N-08 | the tidying gesture across 4 characters | **STILL OPEN** in Ch.6 and Ch.8; **Ch.9 added 3 more → N-10** |
| N-09 | "put a hand in the small of his back" ×2 | **STILL OPEN** — both instances present |
| N-10 | Rx/Spector counting device | **RESOLVED IN THE DOCS**, correctly — the bible now narrows Spector to the *spoken* count and cedes the private tally. §THE ONE CARVE-OUT is the best piece of canon maintenance in the project |
| N-11 | Ch.6's recovery-element day count vs Ch.3 | **STILL OPEN** — "day three" + "eight days" unchanged against Ch.3's "eleven days ago" |
| D-01 | outline Ch.8 "fourth deployment" | **FIXED** → "fifth". `CF-07` closed |
| D-02 | protect the stage-3 trigger | **NOT APPLIED, and now more urgent.** See **D-02** |
| D-03 | SERIES-BIBLE stale in three places | **NOT APPLIED.** See **D-03** |
| D-04 | Holst's first name | **RESOLVED** in `character-bible.md`; `CF-13` closed |
| D-05 | the book's CLAUDE.md Status block | **NOT APPLIED.** See **D-04** |
| O-01 | Merrick's notebook | **CLOSED by Ch.9.** §0.11 |
| O-02…O-05 | letters, third word, subscription, Paladin's hand | **ALL STILL OPEN.** See **D-05** |
| W-04 | the Ch.7 confabulation | caution holds; nothing made it worse ✔ |
| W-05 | Rx's signature tic missing | **CLOSED by Ch.9.** §0.7 |
| W-06 | Hollow silent since Ch.2 | **WORSE** — nine chapters, and **Requiem too.** See **W-12** |
| W-07 | Ch.8 and February | holds; February still reads as ahead of Merrick, just |
| W-08 | the data chip out of inventory | **CLOSED by Ch.11.** `CF-12` closed. §0.4 |
| W-09 | "the water since August" | **spent a second time, verbatim, by a different character → W-08** |
| W-10 | the sensory-memory intrusion has no budget | **WORSE** — now 5 chapters. See **W-11** |
| W-12 | month names on the page | ruling holds; **one new borderline → W-04** |
| W-13 | Jameson absent from Ch.6–8 | **superseded** — he is in Ch.10 in person and the lock held. §0.6 |
| W-14 | the book still ends on suspicion | **re-verified at Ch.11.** §0.9 |
| C-01…C-05 | Ch.1 findings | all unchanged. **C-01 note: Ch.10 adds a fourth "thirty" datapoint** (*"withholding for thirty years"*, *"a life he had left thirty years ago"*), making Ch.1's "twenty-six years" four-to-one the outlier. Still **no edit** — Ch.1 is locked. Constraint for Ch.12–26: **never state a number.** |
| C-02/C-03/C-04 | motif ALLOWLIST additions | **NOT APPLIED** — the ALLOWLIST still holds only `an outline with nothing in it` (3) and `the first time since` (4). This is why **N-06** happened |

---

## 2. FINDINGS IN CHAPTER 1 — LOCKED. REPORT ONLY. NO EDIT PROPOSED.

**Nothing new.** C-01 through C-05 stand as written in the previous audit, with the one
strengthening note on C-01 above.

One structural observation, report-only, because it has consequences for a **doc** rather than
for the chapter: **locked Ch.1 is built on the construction the new POV rule forbids.** *"The
memory was there, **Vexx would learn much later**, sealed beneath something baked into the
transfer process itself"*; *"a sound Vexx **would come to associate, for the rest of his life**,
with the moment everything changed"*; *"something that **would take years**, and a man named
Richard Jameson, and a truth neither of them could see coming, to finally surface."* These are
the author's deliberate retrospective frame and they are the chapter's engine. **The rule needs
scoping, not the prose. See D-04.**

---

## 3. FINDINGS IN CHAPTERS 2–5 — THE AUTHOR'S PROSE. MINIMAL PROPOSALS ONLY.

### A-01 · **needs a fix** · Ch.4's "three weeks earlier" — *still unfixed, and Ch.4 now contradicts itself twice*

- **Ch.4 ¶115:** *"threaded with an unsteadiness Vexx had only heard once before, **in a jungle
  clearing three weeks earlier**."*
- By the chapter's own arithmetic (¶3 "three weeks after the jungle" → ¶21 "two days later" →
  ¶41 "six weeks later") that clearing is **nine weeks** earlier, not three.
- **New corroboration from inside the same chapter:** ¶127 dates Jameson's office as *"**months**
  earlier"*. So Ch.4 itself already uses the longer scale for the other anchor.
- **Proposed fix — one word, in Ch.4:** *"in a jungle clearing **two months** earlier."*
- **What is at stake:** the intervals *are* the evidence, and this is the chapter where Vexx
  first asks *"Do you remember anything at all about how you actually died?"* The reader this
  book is built for is counting.
- **Gated metrics:** word-count +1, em-dash-neutral, no sentence-length change. Ch.4 is an
  author chapter on `AUTHOR_CEILINGS`; no metric moves materially.
- **Cascade:** none.

### A-02 · **needs a fix** · Ch.2 dates the Phantom slip twice, differently — *still unfixed*

- **Ch.2 ¶89:** *"three weeks, in fact, most of them spent on a training range…"*
- **Ch.2 ¶101, sixteen lines later, inside that same scene:** *"faster than made strict logical
  sense for **six weeks** of acquaintance."*
- **Proposed fix — one word, in Ch.2:** *"for **three weeks** of acquaintance."*
- **What is at stake:** the sentence's whole move is *the interval is too short for this
  intimacy*, and it names double the real interval, which blunts the point it is making.
- **Gated metrics:** zero movement. Ch.2 is the densest chapter in the book (simile 7.0/1k,
  em-dash 11.1/1k) and this touches neither.

### A-03 · **worth a look** · Ch.3's "three weeks earlier" is the same fossil as A-01 — *new finding*

- **Ch.3 ¶93:** Rx's too-quick denial is *"the same reflex as the transport bay, the same reflex
  as **Jameson's office three weeks earlier**."*
- Ch.2's own arithmetic puts Jameson's office at **~10 weeks** before the first deployment
  (3 weeks re-entry → +2 weeks → +4 days → +3 days → +6 weeks → +3 days). And **Ch.4 ¶127 says
  "months earlier"** about the same meeting.
- **So Ch.3 is the outlier and Ch.4 is right** — and the error is the same shape as A-01: a
  "three weeks" that was correct before the roster-building scene break was placed.
- **Proposed fix if touched — one word, in Ch.3:** *"the same reflex as Jameson's office **two
  months** earlier"*, or simply delete *"three weeks earlier"* and leave *"Jameson's office"*
  (−3 words, and arguably better rhythm).
- **Recommendation: fix it with A-01, or leave both.** Fixing one and not the other is the worst
  of the three options, because it makes the surviving one the only wrong number in the book.
- **Gated metrics:** neutral either way.

### A-04 · **deliberate-and-fine** · Ch.5 is the book's first disclosure, and Ch.11 reaches back to it correctly

Recorded because a brief got it wrong and the next one might: **Ch.5 ¶65 is the first time Vexx
tells a human being**, it is the author's prose, and Ch.11 cashes its promise verbatim
(*"You told me I'd be first." / "I did."*). Do not let a later pass "move" the first disclosure
to Ch.11 in order to make the brief true. **No edit.** See §0.3.

### A-05 — A-06 · carried forward unchanged

A-05 (Ch.2's disclaimed Phantom scene) and A-06 (Ch.5's Echo in Vexx's ear) stand as previously
written. **No new proposals.** A-06 is softened further by Ch.11 putting Echo on the shared net,
which is the right mechanic; recorded in the YAML.

---

## 4. FINDINGS IN CHAPTERS 6–11 — PIPELINE-WRITTEN. PROPOSE FREELY.

### N-01 · **needs a fix** · Ch.6 contradicts itself about the jungle, two paragraphs apart

The CF-08 repair converted three "nine weeks" and **missed the fourth**, because it is the only
one not followed by *earlier* or *ago*.

> **Ch.6 ¶96:** *"He was in a jungle **eleven weeks earlier**, at two in the morning…"*
> **Ch.6 ¶98:** *"**Nine weeks** he had been on the other side of that sentence — it had been
> sitting in his own ears the whole time…"*

Same fact, same sentence of Corwin's, two paragraphs apart. Corroborated against ¶24 ("eight
weeks into a rehabilitation track") and ¶216 ("eleven weeks ago"), both of which were converted.

- **Proposed fix, in Ch.6:** *"**Eleven weeks** he had been on the other side of that sentence."*
- **Gated metrics:** word-count-neutral, em-dash-neutral, no sentence-boundary change. Ch.6 has
  headroom on em-dash (10.8/12.0) and its narration median (14.5) must not be *shortened* — this
  edit does not touch it.
- **Cascade:** none. `CF-15`.

### N-02 · **needs a fix** · Ch.10 says the material has been out of lock for "the better part of a year". It has been ~3.5 months.

> **Ch.10 ¶134, Dessen:** *"the answer is a kitchen table, in a residence, under a lamp, alone,
> **for the better part of a year**."*
> **Ch.10 ¶224, Jameson:** *"You can find him for a property return that's overdue **since the
> summer** — you should, because it is."*

The release is Ch.4's, at jungle + ~3.5 weeks (~November by the derived calendar). Ch.10 is
jungle + 19 weeks (~late February). **That is fifteen and a half weeks, not a year**, and it is
not "since the summer" — the summer is when the cell was *formed*.

- **Why it matters more than an arithmetic slip:** both lines sit inside the chapter's two best
  speeches, and both are doing *rhetorical magnitude*. A reader tracking the intervals — the
  reader this book is for — hears Dessen inflate by 3× in the one scene whose whole subject is
  that the record is exact.
- **Proposed fix, in Ch.10, two words:**
  - *"alone, **since the autumn**"* (Dessen)
  - *"overdue **since the autumn**"* (Jameson)
  Season names are compliant with the no-calendar-date guardrail per the standing W-12 ruling; a
  **year** would not be.
- **Gated metrics:** Dessen's is −2 words, Jameson's is 0. No em-dash movement (Ch.10: 10.5/12.0).
  Narration median 17 is untouched — both edits are inside dialogue.
- **Cascade:** none. `CF-16`.

### N-03 · **needs a fix** · Ch.10 says the board's disposition came three weeks before the release. Ch.4 says two days.

> **Ch.10 ¶224, Jameson:** *"**Three weeks before he signed anything.** The chain of custody
> you're describing was ended in writing by a review board on a Tuesday afternoon."*

Ch.4 ¶5 is the debrief where the ruling is delivered; Ch.4 ¶21 is *"two days later"*. Three weeks
before the signature puts the board's ruling at the jungle itself, which is not available.

- **Proposed fix, in Ch.10:** *"**Two days** before he signed anything."*
- **This fix makes the speech better.** "Two days" turns the line from a span into an indictment
  of the board's haste, which is precisely what Jameson is arguing.
- **Gated metrics:** word-count-neutral. Dialogue only. `CF-17`.

### N-04 · **needs a fix** · Ch.10 says Vexx has known Jameson two years. It is about seven months.

> **Ch.10 ¶168:** *"and something went across his face **Vexx had not seen on it in two years**."*

Ch.2 ¶5 puts their first meeting three weeks into re-entry; the roster takes ~9 weeks; Ch.3 is
the first deployment; Ch.10 is jungle + 19 weeks. **~7 months.**

- **This is NOT the same claim as Ch.2 ¶225** (*"He would spend the better part of two years
  finding out how much of that hope had been earned"*), which is the retrospective narrator's
  vantage over the whole arc and is correct. Do not "fix" that one.
- **Also cross-check:** Ch.8 ¶66 says the cell's cohesion arrived *"somewhere in the first year"*,
  which is incompatible with Vexx having served under Jameson two years.
- **Proposed fix, in Ch.10, pick one:**
  1. *"something went across his face Vexx had not seen on it before."* (−3 words)
  2. *"…had not seen on it in the seven months he had known him."* (+5 words)
  **Recommend (1).** It is stronger — the point is that the expression is new, not that it is rare.
- **Gated metrics:** (1) is −3 words and shortens one narration sentence. Ch.10's median is 17
  against a floor of 14.0, so there is room; it is the only chapter of the six with slack in both
  directions. Em-dash-neutral. `CF-18`.

### N-05 · **needs a fix** · Ch.11's coda moves the evidence between two buildings without saying so, and the cover story has a hole

Three problems in one 200-word coda, and it is the chapter's declared anchor beat.

**(a) The objects teleport.** Ch.10 ¶256 is explicit: the tag is *"lying in a drawer beside his
bed… **half a mile east of the chair he was sitting in**"*, in *"an apartment with boxes still
taped shut in the corner of the front room"* (¶82). Ch.11 ¶206 puts all three into *"the trauma
pack in the bottom of his **locker**"*, in *"a dead little room with a bed in it and a locker in
it"*, with *"the walk to the **supply cage** for a fresh tab"* — unambiguously on the station.
**The fetch is never narrated, and the coda reads as though the objects were already to hand**
(*"he had chosen the pack before he had crossed the room"*).

**(b) The cover story contradicts the pack.** *"The trauma pack… was **sealed, dated**"* — and the
prepared lie is *"that he had used the pack on the Kettle job, **drawn a new one at the cage**."*
What is actually in the locker is the **same pack with a fresh tab**. A date stamp defeats a
new-pack story on first inspection. **The chapter's last beat depends on the lie sounding like
the truth**, so this inverts the ending.

**(c) The promise made two weeks earlier is broken and nobody notices.** Ch.10 ¶232: *"You'll get
a property return notice inside a fortnight. Answer it the same day." / "I will," Vexx said. /
"People say that."* **Ch.11 is Vexx concealing that exact property.** Whether the notice has
already arrived — which depends on the unstated Ch.10→Ch.11 interval — changes the act from
pre-emption to active breach. Dessen's *"People say that"* is a loaded gun and Ch.11 fires it
without looking at it.

- **Proposed fixes, in Ch.11, cheapest first:**
  1. **(b), word-neutral and the best value:** change the cover story to something the pack can
     support — *"the answer was that he had broken the seal on the Kettle job and re-tabbed it at
     the cage"* — which is also *true*, which makes the final beat land harder.
     Alternatively just cut *", dated"*: −2 words, no other movement.
  2. **(a), one short sentence:** place the fetch. e.g. *"He had brought them in on the transit
     that morning."* **Must be SHORT and must contain no em-dash** — Ch.11's narration median is
     **exactly 18.0 against a ceiling of 18.0**, so a short sentence moves the median *down*
     (safe; floor is 14.0) and a long one or an added em-dash breaches a gate on its own
     (em-dash 11.5/1k, ~1 of headroom).
  3. **(c), two words:** date Ch.11 against the notice. *"The notice had not come yet."* Short,
     metric-safe, and it converts the coda from an oversight into the deliberate act the outline
     asks for.
- **Cascade:** none backwards. Forwards: if (c) is answered "the notice has come", `outline:ch-12`
  onward inherits an active breach and the property return becomes a live thread needing a
  consumer. **Ask before choosing.** `CF-19`.

### N-06 · **needs a fix** · The "eleven hundred" motif is at **five uses against a cap of three**, and Ch.10 re-runs Ch.6's development almost verbatim

Measured instances, book-wide:

| Chapter | Instances | Line |
|---|---|---|
| Ch.1 ¶19 | 1 | *"the particular clatter of a mess hall at 1100"* |
| Ch.6 ¶36 | 1 | *"the clatter of a mess hall at eleven hundred came up on him whole"* |
| Ch.6 ¶132 | 2 | *"The light in the mess hall had been wrong for eleven hundred… he had been calling it eleven hundred to himself for something over twenty years"* |
| **Ch.10 ¶98** | **2** | *"He had been putting that at eleven hundred for as long as he had been telling it to himself. It was not eleven hundred."* |

**Five, against the hard cap of three across the whole book.** Worse: Ch.10's is a near-restatement
of Ch.6's own development (*"he had been calling it eleven hundred to himself for something over
twenty years"* → *"He had been putting that at eleven hundred for as long as he had been telling
it to himself"*). The previous audit called this *"the single best callback in the pipeline
chapters"*, counted it at two of three, and recommended ALLOWLIST registration. **The ALLOWLIST
entry was never added, so nothing stopped Ch.10 spending two more.**

Same root cause, same chapter, for **"the whole of it"**: book-wide 7 uses (Ch.4, Ch.6, Ch.7 Rx,
Ch.8 ×3 incl. *"the whole account of it"*, and Zeus's deliberate pair). N-07 from the previous
audit took Ch.8 from 6 to 3 but **the ALLOWLIST entry was never added either.**

- **Proposed fix, in Ch.10 — recast ¶98's two instances to one, or to zero.** Ch.6 is the owner;
  it has the light, the twenty years and the door-pushed-open image. Ch.10's version adds one new
  idea only — *"everything after it in that day sat in the wrong order too"* — and that idea
  survives without the phrase: *"He had been putting that sitting at the wrong hour for as long as
  he had been telling it to himself. It was the late sitting."*
- **ALLOWLIST additions, in `tools/style_check.py`, in the same commit or they will come back:**
  `("eleven hundred", 3)` · `("the whole of it", 3)` · `("took you long enough", 2)` ·
  `("the clatter of a mess hall", 2)`. The MOTIF CAP section currently reports
  *"all motifs within cap (clean)"* on a book with a 5-instance motif, because the registry has
  only two entries. **Per the root CLAUDE.md PROPAGATION RULE**, the same caps are stated in
  `character-bible.md` §CAPPED and in `voice-dna.md`; check all three.
- **Gated metrics:** the Ch.10 recast is approximately word-neutral; it is narration, so keep the
  replacement sentences at or above 17 words or accept the median falling (floor 14.0, current 17
  — safe). Em-dash-neutral.

### N-07 · **needs a fix** · "Hallam" is two different people

> **Ch.8 ¶76–78:** *"'Eight minutes,' **the crew chief** called back. / Gaia stood, put a hand on
> the rail, said, '**Thanks, Hallam**,' by name, every time, to a man Vexx had not known had a
> name."* — and again at ¶378, to a different crew, to nobody who could hear her.
> **Ch.9 ¶32–36:** *"'Do you know the cook's name,' Zeus said. / '**Hallam**.' / '**Hallam's the
> day shift.** The one who does the night urn is a Mr. Beattie.'"*

Ch.9 does **not** frame this as Vexx getting the name wrong — **Zeus confirms it**, which makes
Hallam the home station's day-shift cook as well as a dropship crew chief.
`ENTITY_STATE.yaml` records Hallam as the crew chief with the explicit note *"Do not spend a
third"*; Ch.9 spent a third, on a different man.

- **Proposed fix, in Ch.9, because Ch.8 is earlier and the name does more work there** (*"to a man
  Vexx had not known had a name"* is the whole point of it):
  1. **Rename the cook.** One word, twice. The beat is untouched — it is still that Vexx does not
     know the name of the man who makes his coffee.
  2. **Or make it Vexx's error, which is sharper:** *"'Hallam.' / '**Hallam flies.** The cook's a
     Mr. Beattie.'"* — Vexx reaches for the one service name he happens to know and gets it
     wrong, which is a better version of the same humiliation. **+0 words.**
  **Recommend (2).**
- **Gated metrics:** both are word-neutral, dialogue-only, em-dash-neutral. Ch.9's narration
  median is **at its floor (14 vs 14.0)** — neither option touches narration.
- **Also:** neither **Hallam** nor **Beattie** is in the SERIES-BIBLE naming registry. See D-03.
  `CF-20`.

### N-08 · **needs a fix** · Ch.6 and Ch.8 vouch, and the brief's own named example is on the page in Ch.6

The rule — *the narrator does not vouch; if a sentence would survive being spoken aloud by an
advocate, it is vouching* — postdates both chapters, so this is not a regression. It is an
unswept chapter.

**Ch.6, four instances:**

| ¶ | Line | Why it vouches |
|---|---|---|
| 32 | *"A woman at the desk apologized twice for a wait of four minutes — **she meant it both times** —"* | **the brief's exact named tell.** An advocate would say this |
| 170 | *"There was no unkindness in it anywhere. **She was not lying.** Vexx understood that this was not the first time she had said it"* | a flat narratorial certification of a third party's honesty |
| 74 | *"A small laugh. **It was a real one. There was nothing broken anywhere in it.**"* | a verdict on a laugh, not an observation of one |
| 70 | *"'I am better.' **There was nothing underneath it.**"* | same shape |

**Ch.8, two instances, both softer because Vexx is present:**

| ¶ | Line |
|---|---|
| 244 | *"**he told it well**, Zeus laughed once, and **it was a real one**"* — and Vexx is **outside a closed door** for this, so "he told it well" is a verdict on something he cannot assess |
| 368 | *"**The medical crew were decent about it.**"* — borderline; he is watching, and "decent" can be read as his |

- **Proposed fixes:**
  - **Ch.6 ¶32:** cut *"— she meant it both times —"*. **−5 words.** The apology-twice-for-four-
    minutes already carries it, and the sentence reads faster without. ⚠️ **This removes two
    em-dashes from Ch.6 (10.8 → ~10.4/1k) and shortens a long narration sentence. Ch.6's
    narration median is 14.5 against a floor of 14.0 and its ≥40w share is 13.2% against a floor
    of 11.5% — this sentence is one of the long ones. Check both after the cut.**
  - **Ch.6 ¶170:** *"She was not lying."* → *"She had not had to think about it."* Observable,
    same meaning, word-neutral, median-neutral.
  - **Ch.6 ¶74 and ¶70:** convert to what Vexx hears. *"It was a real one"* → *"It went all the
    way through."* / *"There was nothing underneath it"* → leave; it is the shortest and the most
    defensible of the four.
  - **Ch.8 ¶244:** *"he told it well"* → *"he got to the end of it without stopping."* Audible
    through a door. ⚠️ **Ch.8 has ~1 em-dash of headroom (11.8/12.0) and sits at its narration
    median floor (14.0) and its ≥40w floor (13.6% vs 11.5%). Add no em-dash and shorten nothing
    long.**
  - **Ch.8 ¶368:** leave it. Vexx is watching and the judgement is his.
- **Recommend dispatching Ch.6's four as one pass with N-01 and W-13**, since Ch.6 should be
  opened once and re-measured once.

### N-09 · **needs a fix** · Ch.11 gives Gaia two other characters' devices, one of them in its first line

Ch.11 has not had its dialogue pass, and this is exactly what `dialogue-polish`'s Device Bleed
Scan exists to catch. Flagged here so the brief carries it.

**Zeus's reframe, on Gaia, as the chapter's opening line** — `character-bible.md` logged-bleed
note: *"no NEW character may be given this shape"*:

> *"—**it isn't a door now, it's a hole**," Gaia said. "A door does something. **That's a hole with
> a hinge on it.**"*

**Vexx's capped term-correction, on Gaia, twice** (owner: VEXX, cap 5, 2 spent in the author's
chapters):

> ¶20: *"**I don't need to hear the stair. I hear the stair.**"*
> ¶90–94: *"I've got the door shut." / "That's what you asked for." / "**It's what I said.**"*

**Her own device does land** — *"What you do with the rest of it is your call"* (¶192) is
fact → ask → clock with *your call* as the weapon, exactly as mapped. **She is not under-served;
she is over-served with other people's.**

- **Proposed fix, in Ch.11, at dialogue-polish:** recast the three. The first line is the one that
  matters most — it is the chapter's opening move and it currently belongs to Zeus. A version in
  her own register: *"—there's no door there now. There's a hole with a hinge on it."* (drops the
  *isn't/is* pivot, keeps the image, keeps the rhythm).
- **Gated metrics:** dialogue-only, so Ch.11's narration median (18.0, at ceiling) is untouched.
  **Do not introduce an em-dash** — the leading em-dash in ¶6 is already counted and Ch.11 has
  ~1 of headroom. `CF-21`.

### N-10 · **needs a fix (judgement call)** · §STANDING OFFENCE #5: Ch.9 adds three more tidying gestures

The bible records *"Ch.6 ×4, Ch.8 ×2, Ch.9 ×2… Ch.9's Aglaope instance is fixed"*. Measured now,
Ch.9 carries **three** of the core gesture, not two:

| ¶ | Who | Line |
|---|---|---|
| 94 | **Zeus** | *"reached over and **turned the cup a half-turn** on the table"* |
| 100 | **Zeus** | *"Zeus went on **turning the cup**."* |
| 226 | **Vexx** | *"He **turned his cup** on the table."* |

Full book census: Ch.2 Zeus (the author's one use) · Ch.5 Vexx · Ch.6 Corwin ×2, Voss ×2 ·
Ch.7 Vexx (the pad) · Ch.8 Aglaope ×2 · **Ch.9 ×3** · Ch.10 Dessen (capped pen, turned leaf).
**Ch.11 adds zero.** ✔

- **The judgement call, and it cuts both ways:** Ch.9 returns the gesture to **Zeus**, who is the
  author's original and only owner. That is arguably a *repair*, not a bleed — and Vexx's ¶226
  use deliberately rhymes Ch.5's (*"He turned her cold cup a quarter turn"*), in a scene that is
  the Ch.5 confession scene replayed with the roles reversed. **If both are deliberate, say so
  and register them**; if not, cut Ch.9 ¶100 (*"Zeus went on turning the cup"* → *"Zeus did not
  look up"*), which is the one instance doing no work.
- **The excess is still in Ch.6 and Ch.8**, unfixed from the previous audit, and that is where a
  cut costs nothing.
- **Gated metrics:** Ch.9 ¶100 is narration; Ch.9's median is **at its floor (14 vs 14.0)** —
  a same-length replacement only. Em-dash-neutral.

### N-11 · **needs a fix** · A verbatim two-sentence structure, duplicated Ch.6 → Ch.11, in the same dramatic position

> **Ch.6 ¶252–254:** *"Vexx waited for the rest of it. / **There was no rest of it.** **She went**
> back to her authorisations…"* — Voss
> **Ch.11 ¶198–200:** *"Vexx waited for the rest of it. / **There was no rest of it.** **She went**
> up the stair…"* — Gaia

**Identical two sentences, identical paragraphing, identical third beat ("She went…"), both on a
woman withholding, both near the end of the chapter.** This is the exact class of defect no
per-chapter gate can see — and the REPEATED PHRASES gate reports *"none distinctive (gate clean)"*
on it, because its function-word filter eats *"the rest of it"*. **A real blind spot in the gate.**

The wider frame is also over-spent: **"the rest of it" × 11 across the book** (Ch.1, Ch.2, Ch.4,
Ch.6 ×2, Ch.7 ×3, Ch.9 ×2, Ch.11 ×2), including *"Say the rest of it"* in Ch.7 and *"Say the rest
of it. You had a rest of it"* in Ch.9.

- **Proposed fix, in Ch.11, because Ch.6's is earlier and Voss's is the better one** (hers is the
  chapter's dismissal; Gaia's is a door closing on an anecdote): recast Ch.11 ¶198–200. Gaia has
  just told a story about a man who laughed once a night; the shape the moment wants is the
  silence, not the formula. e.g. *"Vexx waited. / She did not add anything to it. She went up the
  stair, and the slack closer landed twice behind her — dry, clean, in a corridor with nothing in
  it."*
- ⚠️ **Gated metrics, Ch.11:** this is narration. The proposed version replaces a 6-word sentence
  and a 6-word sentence with a 3-word and a 6-word — **it pushes the ≤6w share up (currently
  21.6%, ceiling 33.0%: safe) and the median down from 18.0 (ceiling 18.0, floor 14.0: safe, and
  in fact helpful)**. Em-dash count unchanged. **This is the one Ch.11 edit that is free in every
  direction.**
- **Also:** add `("the rest of it", 4)` to the ALLOWLIST and fix the gate's filter so a repeated
  5-word *structure* made of common words is still reported. See N-13.

### N-12 · **needs a fix** · Ch.11's opening AND closing moves each duplicate an earlier chapter, against an inventory that forbids repeats

`feedback/progress.md` maintains an **OPENINGS** and a **CLOSERS** inventory precisely because
Ch.2–5 all drifted onto one closing figure. Ch.11 is not in either table yet, and when it is
entered, both cells collide.

**The opening is Ch.8's device, almost line for line:**

> **Ch.8 ¶6:** *"**—because the water's wrong**," Goliath said. "**It isn't the grounds.** Every
> one of you goes straight to the grounds."*
> **Ch.11 ¶6:** *"**—it isn't a door now, it's a hole**," Gaia said. "A door does something.
> That's a hole with a hinge on it."*

Em-dash-initial dialogue fragment · mid-argument · attributed to a cell member · about a mundane
piece of station infrastructure · with an *"it isn't X"* in the second clause · opening the
chapter cold. The inventory lists Ch.8's as *"mid-transit, mid-argument, no scene-setting"* — the
same entry describes Ch.11 exactly.

**The closer is Ch.6's device:**

> **Ch.6 ¶268:** *"'I don't know whether it went,' Vexx said, **out loud**, to a stranger who had
> asked him about a train."* — inventory: *"a misdirected answer to a stranger"*
> **Ch.11 ¶212–214:** *"he said it once, **out loud**, in the room, to hear what the room did with
> it. / The room did nothing with it…"*

Both end on **Vexx saying a prepared sentence out loud into a space that is not listening.** They
are not identical — Ch.6's is misdirection to a person, Ch.11's is a lie rehearsed to an empty
room — but they share the verb, the adverb, the mechanism and the function, and one is five
chapters after the other.

- **Proposed fix, in Ch.11, at hook-craft (which has not run yet — this is the cheapest moment in
  the book to fix it):**
  - **The opening:** keep the mid-argument cold start, drop the em-dash-initial fragment and the
    *"it isn't X"*. Enter on Gaia's *position* instead of her sentence — she is the only character
    in the book whose body is a device (weight on the foot nearest the stair). **Bonus: removing
    the leading em-dash buys back Ch.11's one unit of em-dash headroom.**
  - **The closer:** Ch.11's eleventh distinct closing shape is available cheaply, because the
    coda already contains one — *the room answering*. End on the room, not on the saying:
    *"The room did nothing with it. It went a pace, stopped, dry, no carry…"* and cut the
    *"he said it once, out loud, in the room"* framing to a clause.
- ⚠️ **Gated metrics:** cutting the framing clause shortens a narration sentence (median 18.0 →
  lower: **safe**, floor 14.0). Dropping the leading em-dash: 11.5 → ~11.0/1k, **which is the
  single most useful mechanical move available in Ch.11.**
- **Then enter Ch.11 in both inventories in `feedback/progress.md`.** They are the only defence
  against this class of drift and the file is one chapter behind.

### N-13 · **needs a fix** · The dialect gate reports CLEAN on four surviving British forms, because its own word list does not contain them

`CF-14` is 30-of-34 applied and `DIALECT = "us"` was added to `tools/style_check.py`. *"grey"* →
*"gray"* and *"programme"* → *"program"* both verified fixed in Ch.6. **Four survivors:**

| Where | Form | Why the gate missed it |
|---|---|---|
| Ch.6 ¶96 | **kilometre** | not in `_UK_US` (Ch.4 ¶85 correctly uses *kilometer*) |
| Ch.7 ¶52 | **per cent** | **two words** — the gate tokenizes on `[A-Za-z]+` and cannot see it |
| Ch.8 ¶52 | **humour** | not in `_UK_US` |
| Ch.8 ¶54 | **humoured** | not in `_UK_US` |

**The gate printing "clean" is worse than it printing a number**, because it carries the authority
of having checked.

- **Prose fix:** `kilometre` → `kilometer` (Ch.6) · `per cent` → `percent` (Ch.7) ·
  `humour`/`humoured` → `humor`/`humored` (Ch.8). ⚠️ **All four are word-neutral and
  em-dash-neutral; `per cent` → `percent` reduces Ch.7's word count by 1, and Ch.7 is the
  `PUNCH_CHAPTERS` exemption so no breath metric applies.**
- **Gate fix, `tools/style_check.py` `_UK_US`:** add `humour/humours/humoured/humourless`,
  `kilometre/kilometres`, and a two-token rule for `per cent`. **Per the root CLAUDE.md
  PROPAGATION RULE: this is a mechanism improvement, not a book's motif list, so if it is worth
  keeping it belongs in `books/_template/tools/style_check.py` too** — the word list is generic
  English, not Valkyr-specific.
- **Not a dialect hit, author's call:** Ch.11 ¶22, Echo — *"I want it **minuted**"*. A British
  institutional idiom rather than a spelling. It is in character for Echo (naming and minuting
  are both his), and it is the only Briticism of register in a US-spelled book. Flagged, not
  proposed.

### N-14 · **needs a fix** · Ch.8's apron head-count is still eleven, and it is still wrong on every reading

Unchanged from the previous audit (`CF-09`). Ch.8 ¶374: *"and eleven people on the apron behind
him watching him go."* Garrison is eleven **including Merrick**; he is on the ramp; the station
commander *"went inside and did not come out again"* four lines earlier. Ten, nine, or fifteen —
never eleven.

- **Proposed fix, in Ch.8 — de-number rather than re-count**, because the number is doing rhythm:
  *"and the whole of the station on the apron behind him watching him go."*
  ⚠️ **"the whole of" is at cap** (see N-06) — so use *"and the station behind him watching him
  go"* instead. **−4 words, em-dash-neutral.**
- **Must not be touched:** Paladin's *"eleven people in it"* (¶306) and Gaia's *"Ten of the eleven
  have noticed"* (¶322) are both correct.
- ⚠️ Ch.8 has ~1 em-dash of headroom and sits on two breath floors. **Dispatch this with the
  Ch.8 half of N-08 as a single pass and re-measure once.**

---

## 5. WORTH A LOOK

**W-01 · Ch.11's distance from Ch.10 is unstated, and it is the one interval that carries weight.**
Ch.10 ends with a fortnight clock running. Ch.11's only bounds are Goliath's *"what everybody in
this corridor has been asked for a week"* and Gaia's *"the night before last"* / *"yesterday"*.
Four words would settle it, and **N-05(c)** is the place to put them.

**W-02 · Ch.10's "He'll have gone by now" is placed where it will be misread.**
Ch.10 ¶278: *"**He'll have gone by now**, Rx had said on the stairs, answering something Vexx had
not asked him, and had said almost nothing since the audit-room door opened."* The stairwell is
¶8, on the way *to* the meeting, where "he" can only be **Merrick** (*"He had assumed Merrick"*).
But the sentence sits in the corridor coda where Jameson is standing at the elevator, so the
default reading is Jameson — and *that* reading is impossible, because on the stairs Rx does not
know Jameson is in the building. **Propose, in Ch.10:** *"Rx had said on the stairs, about
Merrick, answering something…"* (+2 words, em-dash-neutral, inside an existing sentence).

**W-03 · Ch.6's "day three" + "eight days" still contradicts Ch.3's "eleven days ago."**
N-11 from the previous audit, unfixed. Ch.3 (author) has Gaia say *"Recovery unit went in eleven
days ago"*; Ch.6 (pipeline) has Corwin say *"The recovery element came in on **day three**… I
stayed out of their way for **eight days**."* Internally clean, externally eleven-vs-eight.
**Fix in Ch.6, because Ch.3 is the author's:** *"came in on the first day"* / *"**ten** days"*.
Word-neutral.

**W-04 · Ch.9's "at Christmas" is both a season wobble and the manuscript's closest approach to a calendar.**
Ch.9 ¶14, Zeus: *"that instrument will still be out of tune **at Christmas**."* The joke only
works if Christmas is weeks away; the book's own clock puts Ch.9 in **February**, which makes it
reach eleven months forward. And Christmas pins a specific calendar in a universe where the
guardrail says *no hard in-universe calendar date*. The standing W-12 ruling permits months and
seasons; a named festival is a step past that. **One word, in Ch.9:** *"at the changeover"* (which
Ch.8 has already established as a station unit of time) or *"in the spring"*. Word-neutral,
dialogue-only.

**W-05 · Which job does Vexx mean, and can the reader get there?**
*"One of the jobs we've run wasn't the job we were briefed."* The only inference the evidence
supports is the **Ch.3 jungle deployment**: briefed as find-and-assess, with a Choosing
authorisation live, on the one surviving witness to an ambush whose armour carried a dead man's
reissued tag. That chain *is* available to a careful reader. But it is four steps long and the
sentence is deliberately bare, and a reader who assembles the wrong job (Reyes, or Merrick) will
mis-read Ch.12 onward. **No prose change proposed** — the bareness is the point, and
`outline:ch-11` beat 4 asks for exactly this. **Recorded so the outline for Ch.12+ can confirm
which job Vexx means, in the plan if not on the page.**

**W-06 · Ch.10's "in a corridor" has no referent.**
Jameson ¶162: *"a man who did the only honest thing available to him **in a corridor** at the end
of a very bad month."* Ch.10 itself says where it happened: *"He had gone down to **that counter**
on a Thursday afternoon with an authorization on a pad"* (¶140). **Propose, in Ch.10:** *"at a
counter at the end of a very bad month"* — word-neutral, and sharper, because Jameson is quoting
the record. ⚠️ **It also removes the reader-side rhyme with Ch.11's corridor scene noted in §0.6.
Dispatcher's choice; the rhyme is worth more than the precision if the author likes it.**

**W-07 · Rx's two unmarked absences.**
(a) **Ch.8 ¶422:** Goliath says *"Your Rx runs hot"* with Rx in Vexx's ear, and Rx says nothing —
in Ch.8 or in any chapter since — and the narration never registers the non-reaction. The Ch.6,
Ch.10 and Ch.11 silences are all marked; this one is the loudest and is not. **One clause in Ch.9
or Ch.10 closes it**, and it is good material: *Rx had not mentioned it. Not once, in a fortnight.*
(b) **Ch.11's corridor scene** has Echo arrive uninvited on the net and Rx stay silent through
2,000 words including the disclosure, with no acknowledgement until the coda. The coda does the
work, and this is defensible — but it is 2,000 words of the chapter where Rx has the most at
stake. ⚠️ **If anything is added to Ch.11 narration it must be SHORT and em-dash-free.**
`CF-23`.

**W-08 · Two new narrator formulas that no per-chapter gate can see.**
(a) **"X with nothing in it"** — Ch.1 and Ch.2 carry the registered motif (*"an outline with
nothing in it"*, 2 of 3). Ch.10 adds **three** (*"a corridor with nothing in it"*, *"a box with
nothing in it"*, *"A pause with nothing in it"*) and Ch.11 adds **two** (*"a room with nothing in
it"*, *"a corridor with nothing in it"*). Seven total, and the frame is now the narrator's default
for emptiness, which dilutes the one that is load-bearing. Ch.10's *"a box with nothing in it"* is
a deliberate and excellent echo of Ch.1's empty casket — **keep that one and thin the others.**
(b) **"A pause with [X] in it"** — exactly one per chapter, Ch.7 (*nothing wrong*), Ch.8 (*no
weight*), Ch.9 (*a pen moving*), Ch.10 (*nothing*). Four chapters, one formula, invisible to every
gate because the filler word changes each time. **Cap it at 3 and spend the third deliberately.**
(c) Minor: *"bark of a laugh"* Ch.2 and Ch.11; *"It was a real one"* Ch.6 and Ch.8 (and both are
in N-08 anyway).

**W-09 · §STANDING OFFENCE #7 has still not been recast, and the plateau is now five chapters long.**
Measured: Ch.6 = 3, Ch.7 = 0, Ch.8 = 5, Ch.9 = **3**, Ch.10 = **4**, Ch.11 = **0**. The bible's
human flag is ≥3 per chapter, so Ch.9 and Ch.10 are both over it and **neither has been recast.**
Ch.9: *"like a man giving directions to a road he drives every week"* · *"like a man reporting a
fault on a vehicle he means to go on driving"* · *"like a man signing something on his knee"*.
Ch.10: *"like a woman reading out a train time"* · *"like a man reporting a figure off a gauge"* ·
*"in the voice of a woman filing something"* · *"like a man carrying something wet"*.
**Ch.11 at zero is the good news and the proof it is reducible** — the first pipeline chapter since
Ch.7 to come in clean. ⚠️ **Recast, do not cut: the bible warns that cutting breaches the 2.0
comparison floor.** Ch.9's comparison rate is 2.7/1k and Ch.10's is 2.2/1k against a floor of 2.0,
so **Ch.10 can afford to lose at most one.**

**W-10 · §STANDING OFFENCE #3 fires for the fourth consecutive chapter.**
Ch.11 ¶196, Gaia: *"a man through mine who laughed once a night, about eleven. **One laugh. Never
two.** I was in there five months."* Ch.8 Gaia, Ch.9 Zeus, Ch.10 Jameson, Ch.11 Gaia — and the
bible's own note is the right one: *it is never the same character twice, so auditing "is this in
character?" will never catch it.* This instance is the weakest of the four (it is a detail in a
personal anecdote, not a count performed for a room) so it is a **watch, not a finding** — but
four chapters running is what the bible asked to be told about.

**W-11 · The involuntary sensory-memory intrusion is now five chapters old and still unregistered.**
Ch.6 ×1, Ch.7 ×2, Ch.8 ×2, Ch.9 ×2 (the Ridgeway gate dog; the `SOLID ASH` listing callback),
Ch.10 ×2 (the mess hall at the wrong hour; the shirt collar neither twin learned to fold),
Ch.11 ×1 (the dispenser out of its middle selection). **~10 instances, ~2 per chapter, and the
device exists nowhere in `voice-dna.md` or `character-bible.md`.** At this rate it reaches ~30 by
Ch.26. It is one of the best things the pipeline has invented — it is Vexx's version of what Rx
cannot do — which is exactly why it needs a cap rather than a cut. **Suggested:** register it;
no more than one per chapter after Ch.12; **none at all in the chapters where Rx is leaking**, so
the two never compete. Ch.13 is the first such chapter.

**W-12 · Requiem and Hollow have been silent for nine chapters.**
Neither has spoken since the Ch.2 pairings. Hollow's device is *withholding until useful /
answering forty minutes late*, so his silence is arguable — but **nine chapters is past the point
where a reader stops noticing and starts forgetting he exists**, and Ch.8's kitchen-table round
polls five operators and **Bastion** while Hollow says nothing. Requiem is worse: she belongs to
**Aglaope**, who carries two full two-handers (Ch.5, Ch.9) with her AI mute, and whose Ch.5 scene
*quotes Requiem's creed out of Aglaope's mouth* rather than letting Requiem say it. `outline:ch-16`
has Requiem's one planned beat (objecting to her own operator) ten chapters away. **Give each one
line before Ch.13.** `CF-24`.

**W-13 · Ch.6 still quotes a clinical file Vexx has never seen.**
N-05 from the previous audit, unfixed. Ch.6 ¶122–124, unattributed, mid-scene, in the document
italics: *"Subject's account of the deployment now aligns with the operational record…
Cooperative with program throughout."* Vexx is sitting in a day room with a coffee; Corwin's
clinical progress note is not a document he has. **The previous audit's option 2 (cut, −35 words)
remains the recommendation** — the chapter's power is that the institution never speaks for
itself, and Corwin's own *"They explained it to me. I think I had it backwards"* does the work
better. ⚠️ **A 35-word cut from Ch.6 will move its ≥40w share (13.2% against a floor of 11.5%) —
the two italic lines are long. Re-measure; if it drops below the floor, use option 1 (ground it in
the pre-visit material) instead.**

**W-14 · Merrick's notebook is inside Vexx's jacket while Compliance finds against him for exactly this.**
Ch.9 ¶128: *"put the notebook inside his jacket."* It is station property from an assessment,
never returned, never logged — and **the very next chapter** opens with Internal Compliance
finding against him for taking assessment material out of a locked room and not bringing it back.
**No chapter notices.** This is a free, already-paid-for irony sitting one clause away, and it is
the single best unclaimed beat the audit found. **Propose, in Ch.10, inside an existing sentence:**
when Dessen asks what the material was, Vexx is aware of a soft-cornered notebook against his
ribs. ⚠️ **Ch.10 is the only chapter with slack in both breath directions; a short clause is
safe.** `CF-23`.

---

## 6. DELIBERATE-AND-FINE — verified, recorded, do not re-open

1. **Ch.9's internal clock.** Closes to the minute. §0.1.
2. **The Ch.10 gate condition.** Holds; Ch.11 converts nothing. §0.6.
3. **Jameson's eight seconds and the four-part apology.** The strongest execution of the
   institutional lock in the book. §0.6.
4. **Rx's Ch.10 silence.** The Ch.2 response with no escalation. Correct. §0.7.
5. **The signature tic reloaded in Ch.9.** Closes W-05. §0.7.
6. **Ch.11 cashes Ch.5's promise verbatim** — *"You told me I'd be first." / "I did."* The best
   cross-chapter callback in the manuscript.
7. **Echo's two devices both land in Ch.11, and one is subverted.** *"Is this the Gullet?"* +
   *"Nobody had ever agreed to call the corridor the Gullet"* is naming-then-using-the-name
   exactly as mapped; and *"Echo. Off." / "Off, Echo said, and was."* is the one AI in the book
   whose device is *never letting a silence stand* being switched off mid-sentence and obeying.
   **Note the unremarked beat underneath it:** Vexx silences **Gaia's** AI in the middle of an
   argument about Vexx managing Gaia, and nobody mentions it. If that is deliberate it is one of
   the best things in the chapter. **Register it either way.**
8. **Merrick's notebook contains nothing, and the nothing is the payoff.** §0.11.
9. **The boot's owner is never identified, and the Ch.7 boot requisition is left unconnected.**
   §0.10.
10. **Ch.11's coda withholds the self-hatred `outline:ch-11` beat 6 asks for**, and renders the
    *speed* instead (*"None of that took any thinking at all, and he had chosen the pack before he
    had crossed the room"*). That is the right call for this book's zero-emotional-temperature
    register. **Do not add the feeling back.**
11. **RECLAMATION is still unglossed and unremarked** (1 of 9 spent, Ch.7). ✔
12. **"Vexx does not do the small kind thing."** He says *"I'll ask"* about Corwin's letter in
    Ch.6 and has not; Aglaope asks him to *"Tell Paladin about the peg"* in Ch.9 and he has not,
    two chapters on. Zeus predicts the pattern in the book's own words — *"He won't offer, though.
    He'll wait to be asked, Paladin won't ask, and that instrument will still be out of tune at
    Christmas."* **This is almost certainly deliberate and it is nowhere registered as a pattern.
    Register it in `foundation.md` or `character-bible.md`, and then the two unkept promises stop
    looking like two orphans.** (Which is also half of D-05's answer.)

---

## 7. FINDINGS IN THE DOCS — fix there, not in the prose

### D-01 · **needs a fix** · `feedback/progress.md` is one chapter behind, and both inventories are the defence against N-12

> *"**Ch.1–10 in the manuscript, 35,593 words of prose.**"*

It is **Ch.1–11, 38,398 words** (`wc -w`). Also required:
- Enter **Ch.11** in the **OPENINGS** table and the **CLOSERS** table — and when you do, N-12
  becomes visible without my having to find it, which is the point of those tables.
- Add Ch.11's measured numbers to **§4 the live measured items**: narration `and` 21.1/1k (above
  the author's 18.19–18.90 band, and a reversal of Ch.10's 18.39), generic-person manner
  attribution **0**, narration median **18.0 — exactly on the ceiling**.
- Update the resume point: Ch.11's loop (dialogue-polish → hook-craft → disruptor → evaluate →
  8.5 gate) is still outstanding, and **N-09 and N-12 should be carried into its dialogue-polish
  and hook-craft briefs**, because both are cheapest there.

### D-02 · **needs a fix, and it is now the most load-bearing doc item in the book** · Protect the stage-3 trigger

D-02 from the previous audit was **never applied**, and Ch.10 has made it worse: **proximity to
Jameson has now been spent three times, and Ch.10 additionally spent his voice, close, at length,
in the same room.** What is left as novel for Ch.13 is **only** the open channel, the live
coordinating instruction, and being in contact.

`outline:ch-13` beat 2 specifies exactly those three and its writer warnings (a)–(e) **still do
not say that proximity is spent.** A later drafting pass reading only the warnings could soften
beat 2 back to "Jameson is present" without knowing it had already been cashed.

- **Action:** add one line to the Ch.13 entry's writer warnings. **And then, per the root
  CLAUDE.md PROPAGATION RULE, check the same statement in all four places it lives:**
  `outline.md` §Chapter 13 · `character-bible.md` RX entry · `voice-dna.md` ·
  `ENTITY_STATE.yaml` `memory_unlock_ladder.stage_3` (**done in this pass**).

### D-03 · **needs a fix** · `SERIES-BIBLE.md` is stale in four places now

Unapplied from the previous audit, plus two new:

1. **The books table, line 34:** *"In progress — **5 chapters** drafted, architect pass done"* →
   **eleven chapters drafted, Ch.6–10 through the 8.5 gate, Ch.11 pre-polish.**
2. **"Introduced by the Book One outline, not yet on the page"** still lists **Merrick** (Ch.8)
   and now **Dessen** (Ch.10). Per the bible's own instruction, both became series canon the
   moment their chapter was drafted. Move them into the cast/state tables:
   - **Merrick** — alive, removed from field, medical track, escort of two, not restrained; the
     baseline case, **not** a conspiracy victim.
   - **Dessen** — alive, Internal Compliance; her finding stands unamended and her recommendation
     fell away; **pressure from the system, deliberately not from Jameson** (verified honoured);
     and her unattainable transfer is a plant with no consumer (see D-05).
3. **Gaia's `Knows` cell** currently reads *"That Vexx suspects something and promised to tell her
   first."* After Ch.11 she also holds **one operational claim** — that one of the cell's jobs was
   not the job they were briefed, with no names and no evidence — **and has closed her own account
   of it** (*"That was your one"*). The promise is cashed on the page. Update the cell; the `State`
   cell (*friction suspended, not resolved*) is correct and verified.
4. **The naming registry needs rows** for everything Ch.6–11 created and the previous audit's list
   was never added: `Deric A. Holst` · `Tomas` · `Ivo` · `Hallam` · `Kettle` · `Hallow's Bottom` ·
   and now **`Beattie`** · **`Curran`** · **`Ansel`** · **`Anseth`** · **`Sedge`** · **`Kell`** ·
   **`Ridgeway`**.
   ⚠️ **`Ansel` and `Anseth` must be registered as two separate names whose near-identity is the
   point** — Aglaope's whole argument against alphabetising depends on them being nine pages
   apart. A later "spelling consistency" pass would destroy the beat by collapsing them.

### D-04 · **needs a fix** · The book's `CLAUDE.md` is still wrong, and the POV rule needs scoping before it damages locked prose

1. **The Status block is still the stale one** the previous audit flagged: *"Nothing has passed
   the pipeline's gates yet. `manuscript/chapters/` is still empty."* Eleven chapters are in it
   and five have passed the gate. **A fresh session reads this file first.**
2. **Add the orthography line** (B-01's prevention half, never added): *"US spelling throughout,
   set by locked Ch.1. `gray`, not `grey`. `the program`, never `programme`."*
3. **Add the chapter-standing table** (locked / author's / pipeline / pre-polish).
4. **SCOPE THE POV RULE.** *"No narration anywhere may know something Vexx does not yet know"* is
   correct for Ch.6–26 and **cannot** apply to Ch.1–5. Locked Ch.1 is built on the construction
   (*"the memory was there, Vexx would learn much later"*, *"a sound Vexx would come to associate,
   for the rest of his life"*, *"something that would take years… to finally surface"*), and Ch.2's
   hinge sentence is one (*"He had no way of knowing, sitting in that chair, that the man across
   the table had watched his brother die at close range and personally written the report that
   buried it"*). **As written, the rule instructs a future pass to edit the voice benchmark.**
   State the scope: **the dramatised-present chapters, Ch.6–26.** Same for *the narrator does not
   vouch*. ⚠️ **PROPAGATION RULE: the same two rules will be quoted in `voice-dna.md` §4/§6 and in
   whichever agent brief last carried them. Grep before committing.**
5. **Record `character-bible.md` §CAPPED's own gap:** the retrospective-narrator cap is *"≤2 per
   chapter"* and Ch.1 is *"locked and exempt"* — which is right, and is exactly the scoping
   sentence item 4 needs. Reuse the wording.

### D-05 · **needs a fix (decisions, not defects)** · Seven open threads, and two of them are clocks

None of these is a contradiction. All are cheaper to decide now than at Ch.20. Full detail at
`ENTITY_STATE.yaml` `CF-24`.

| Thread | Opened | Status | Why it needs a decision now |
|---|---|---|---|
| **Corwin's letters** (O-02) | Ch.6 ¶178 | **untouched in Ch.7–11, and a grep of `outline.md` for "letter" returns NO scheduled chapter at all** | `foundation.md` and `character-bible.md` both require the ask never to be granted. That is only dramatic if the failure is dramatised at least once more. **Assign a chapter.** (Consider pairing with the "Vexx does not do the small kind thing" pattern — §6.12 — which would resolve both at once.) |
| **The archive subscription** (O-04) | Ch.7 ¶134 | **ROTTING.** By the book's own clock the month has ended. **Ch.9 returns to an archive terminal and does not mention it.** | A clock that passes unremarked teaches the reader that this book's clocks are decoration. **Fire it or cut the clause.** |
| **The annex badge log** | Ch.9 ¶134 | **ROTTING.** `outline:ch-10` claims Ch.10 *"builds on Ch.9's archive access"* and **Ch.10's prose never mentions the annex, the badge or the 104 minutes.** | The misdirection is good — the summons is about Corwin, not the annex — but the plant needs one acknowledgement or it reads as forgotten. **Cheapest fix: three words in Ch.10 ¶8, inside the existing sentence.** *"He had assumed Merrick. Not the annex, then."* |
| **The third word** (O-03) | Ch.8 ¶440 | live offer, unanswered, no outline consumer | Goliath asked a direct question and is still waiting. **Nominate a chapter.** |
| **Dessen's transfer** | Ch.10 ¶264–272 | planted, no consumer | A board that sits twice a year and has twice refused her. Either `outline:ch-22` ("The Clerk") claims it or cut it to one line. |
| **"Tell Paladin about the peg"** | Ch.9 ¶240 | unexecuted two chapters on | Almost certainly the deliberate pattern in §6.12. **Register the pattern and it stops being an orphan.** |
| **Paladin's right hand** (O-05) | Ch.8 ¶36 | never referenced as an injury again | Ch.9 is adjacent but makes his hand trouble about a tuning peg, which is a different thing. Fine as texture; a loose end if it was meant as more. |

**Deliberate long-arc plants — leave open, all verified still open and unspoilt:** RECLAMATION
(Ch.7, `outline:ch-15`) · Voss's motive (`outline:ch-19`) · Phantom / Goliath's homeworld ·
the half-melted chip (unreadable by design) · Corwin's AI's name (actively refused) · Tomas ·
Vexx's four typed letters of a shared surname · the visitor-log signature · how Corwin knew the
word "Valkyr" (self-flagged in Ch.3, pointedly left shut in Ch.6) · **the boot's owner** (new) ·
**Ansel/Anseth** (new, and must never be "corrected").

### D-06 · **needs a fix** · The outline's Ch.10 beat 7 carries the vouching phrase the prose correctly avoided

`outline:ch-10` beat 7 ends: *"and then lets it go, **because that is what a decent man does**."*
That is the brief's own named vouching tell, sitting in the plan. **The prose did not take the
bait** — Ch.10 ¶298 renders it entirely observably (*"He did none of the small courteous things
people do to let a man off… nothing on his own but the ordinary concern of somebody who has
noticed that the person in front of him is having difficulty"*), which is why §0.5 reports Ch.10
clean. **Amend the outline line so a later revision pass cannot reinstate it.**

### D-07 · **needs a fix** · The REPEATED PHRASES gate has a blind spot that let N-11 through

`tools/style_check.py` reports *"none distinctive (gate clean)"* on a manuscript containing
**"Vexx waited for the rest of it. / There was no rest of it."** verbatim in two chapters,
because its content-rich filter discards n-grams made of function words. It also reports *"all
motifs within cap (clean)"* on a 5-instance motif (N-06) because the registry has two entries.
**Both are honest gaps, not bugs — but a gate that prints "clean" on these two is actively
misleading.** Minimum: report discarded-as-generic repeats that occur in **different chapters**
separately from within-chapter ones, as the informational list already half does. **Per the
PROPAGATION RULE, the filter is mechanism and belongs in `books/_template/` if it is changed.**

---

## 8. WHAT I CHANGED IN `ENTITY_STATE.yaml`

**The file was at `chapters_tracked: [1..8]`, `open_conflicts: 11`, 29 characters / 12 locations /
20 objects / 8 timeline entries / 14 conflicts.** It is now at **[1..11]**, `open_conflicts: 18`,
**34 / 16 / 27 / 11 / 25**. **It re-parses cleanly under `yaml.safe_load`** (verified after every
edit). A pre-edit copy is at
`/tmp/claude-0/-home-user/4fce6c78-e88e-5692-aee2-8b94c6a653f4/scratchpad/ENTITY_STATE.pre-ch1-11-audit.yaml`.

**Principle applied, same as the 2026-09-09 pass:** only entries where the manuscript is
unambiguous were written as **facts**. **Every defect this audit found was recorded under
`conflicts` and deliberately NOT written into the entity facts**, so the file does not launder an
error into canon. Everything sourced to Ch.11 carries `draft_status: "ch-11 pre-polish"`.

### Metadata
- `chapters_tracked` → `[1…11]`; `chapters_planned_not_tracked` → `[12…26]`.
- `last_updated` → `2026-10-03`; `last_updated_by`, `update_note` pointing at this report.
- `open_conflicts` 11 → **18**, with the open/resolved split written out inline.
- New `draft_status_note` recording that Ch.11 is pre-polish and that anything sourced to it may
  move.

### Two **stale entries in the file itself**, corrected
This matters more than the additions, because both were actively wrong:
1. **`timeline[chapter 1]`** still described the **pre-fix "four months"** text — *"four months of
   grief → 'the second knock came four months to the day'"* — and its note still quoted *"I've
   been retired for a year"*. Neither line exists in the manuscript. Rewritten to describe the
   text as it stands, with an explicit **"CF-01 IS CLOSED AND THE PROSE NOW MATCHES"** and a
   do-not-restore warning naming the two dead lines (one of which was a **Jameson-POV sentence in
   Ch.5**).
2. **`timeline[chapter 6]`** still described the **pre-fix "nine weeks / six weeks"** text.
   Rewritten, with the one surviving leftover named and cross-linked to `CF-15`.

### Timeline
Three new entries, **9, 10 and 11**, each with the derived clock, the season evidence, and the
conflicts. Ch.9's carries the **verified minute-by-minute reconciliation** from §0.1. Ch.8's note
updated to record `CF-07` closed.

### Characters — 5 added, 6 updated
**Added:** `dessen` (full block — physical, her reserved three-question device with the three
quoted forms, behaviours, relationships, knowledge, `does_not_know`, outcome, the unconsumed
transfer plant, and a flag that she should be promoted in the SERIES-BIBLE) · `beattie` ·
`curran` · `ansel-and-anseth` (**with a hard instruction that the near-identical spellings are
load-bearing and must never be normalised**) · `the-boots-owner` (**with the never-identify
constraint and a do-not-connect note about Ch.7's boot requisition**).

**Updated:** `vexxcerian` (a `ch9_11_additions` block: three-chapter location log, **thirteen new
knowledge acquisitions** each with method and source, an explicit **`knowledge_NOT_gained`** list
of five items as the guardrail for Ch.12+, and eleven behaviours) · `rx` (a `ch9_11_additions`
block: the tic landing, the Ch.10 silence scoped to Jameson's presence, the Ch.11 absence, a
`does_not_know_or_does_not_say` entry on the unanswered "Your Rx runs hot", and a measured
**`silence_log_2026_10_03`** with per-chapter counts) · `richard-jameson` (a `ch10_additions`
block: thirteen behaviours, what he gained, what he still does not know — **CF-03 is NOT closed by
Ch.10** — and a **`gate_condition_verified_2026_10_03`** field recording the three closest lines
so no later pass strengthens them) · `gaia` (a `ch9_11_additions` block, and a structured
**`her_reading_of_vexx`** with `right_70_percent` / `wrong_30_percent` / `vexx_does_not_correct_it`
written out, plus the SERIES-BIBLE update required and the CF-21 bleed) · `zeus` (a `ch9_additions`
block: the Sedge/Kell back-history now on the page, seven behaviours, and a
**`level_of_knowledge`** field recording that he has **inferred, not been told** — which is the
distinction every later chapter has to respect) · `aglaope` (a `ch9_additions` block: the list,
the eleven years, Ansel/Anseth, Curran, the CF-25 ambiguity, and the note that **Ch.5 not Ch.11 is
the first disclosure**) · `hallam` (the CF-20 collision, in full).

### Locations — 4 added
`home-station-operations-block` (**nine facts building the interior geography Ch.9–11 created** —
the records annex, the badge log, room 2-14, the north-end corridor and its fire door, the Gullet
corridor's acoustics, the mess, the dispenser, the quarters and the supply cage — plus the
half-a-mile-east distance to the apartment and the CF-22 fire-door question) · `sedge` · `kell`
(with a pointer to `outline:ch-22` as the scheduled consumer) · `ridgeway`.

### Objects — 7 added, 2 rewritten
**Added:** `the-trauma-pack` (**two-stage chain of custody, the cover story verbatim, and all
three CF-19 unresolved items**) · `the-propped-boot` · `dessens-notebook` · `aglaopes-list` (four
facts and a *do not let a later chapter have her take the advice* note) · `zeuss-logic-grid` ·
`the-annex-badge-log` (**status `chekhov_open` — PLANTED CLOCK, NOT YET FIRED**) ·
`the-property-return-notice` (**status `chekhov_open` — A LIVE CLOCK AS OF CH.11**).

**Rewritten:** `merricks-notebook` — `status: chekhov_open` → **resolved as a deliberate dead
object**, with its contents quoted, a fourth chain-of-custody stage, and the new `unresolved`
field recording that it is in Vexx's jacket while Compliance finds against him for exactly that
(`CF-23`). `half-melted-data-chip` — **`CF-12` closed by Ch.11**, `last_mentioned` moved from
`ch-05:p37` to `ch-11:p206`.

### Secrets
`rx-was-murdered` gained **`state_at_end_of_ch11`**: a five-point account of what changed in
Ch.9–11 (Zeus's inference; Compliance's permanent finding; **Jameson now knowing Vexx kept the
material**; Gaia's one sentence; the evidence moving) and the explicit verification that **no new
fact about Rx's death reached Vexx, and nothing has leaked forward**.

### Memory-unlock ladder
Three Ch.9–11 precursors appended to `stage_3.precursors_added_2026_10_03`, plus a new
**`ch9_11_audit_2026_10_03`** field stating that no stage is spent, that **Jameson was physically
present in Ch.10 and produced only silence**, that **proximity is now spent three times**, and
enumerating the three things that remain novel for Ch.13 — with the note that **D-02 was never
applied** and which four files the statement lives in.

### `planned` block
`dessen` removed and replaced with a promotion comment pointing at `characters.dessen` and at the
SERIES-BIBLE table she should move out of.

### `notes`
New **`notes.pov_integrity_2026_10_03`** block: the two rules stated, the Ch.9–11 sweep result
(clean, with the two permissible candidates named), the Ch.6/Ch.8 failures listed line by line,
and **`rule_a_and_the_author`** — the finding that the rule as written cannot apply to Ch.1–5 and
must be scoped in `CLAUDE.md` and `voice-dna.md` before a pass tries to edit locked prose.

### Conflicts — CF-15 … CF-25 opened; CF-07, CF-10, CF-12 closed; CF-14 statused
| ID | Subject | Severity |
|---|---|---|
| **CF-15** | Ch.6's surviving "Nine weeks" | structural |
| **CF-16** | Ch.10: "better part of a year" / "since the summer" | plot-load-bearing |
| **CF-17** | Ch.10: "Three weeks before he signed anything" | minor |
| **CF-18** | Ch.10: "in two years" | minor |
| **CF-19** | Ch.11's coda — the move, the date stamp, the broken promise | plot-load-bearing |
| **CF-20** | Hallam is two people | structural |
| **CF-21** | Ch.11 device bleed onto Gaia; Ch.9's "at Christmas" | canon-mechanism |
| **CF-22** | one fire door or two | minor |
| **CF-23** | three unsourced/unmarked beats (Gaia's file-pull; Rx's unanswered silence; the notebook irony) | canon-mechanism |
| **CF-24** | eight orphaned threads, consolidated | structural |
| **CF-25** | "Have you told anybody but him" / "No" | minor |

**Closed:** `CF-07` (outline fixed) · `CF-10` (Ch.8 POV + stack arithmetic verified fixed, **plus
the Ch.9–11 POV sweep result recorded on it**) · `CF-12` (chip restored by Ch.11).
**Statused, still open:** `CF-08` (partially applied → CF-15) · `CF-14` (**30 of 34 applied; the
four survivors named and the reason the gate missed each one**).

**What I did NOT change:** no chapter file was touched — `ls -la manuscript/chapters/` confirms
every mtime predates this session. `CF-03`, `CF-05`, `CF-06`, `CF-09`, `CF-11` left open as author
decisions or as previously-recorded prose defects. No defect this audit found was written into the
entity facts. **Nothing was committed.**

---

## 9. RECOMMENDED DISPATCH ORDER

1. **N-13** (four British forms + the `_UK_US` gate fix) — mechanical, trivially safe, and it
   stops the gate lying. Do it before any other prose edit so later diffs are clean.
2. **Ch.11's polish loop, with N-09 and N-12 written into the briefs.** `dialogue-polish` gets
   N-09 (Gaia's three borrowed devices); `hook-craft` gets N-12 (the opening and the closer, both
   duplicating earlier chapters). **This is the single highest-value item in the report**, because
   Ch.11 has not been polished and both findings are free to fix *now* and expensive later.
   ⚠️ Carry the headroom table into both briefs: **median exactly 18.0 at the ceiling, ~1 em-dash
   of headroom.** Dropping the leading em-dash in ¶6 buys the chapter its only slack.
3. **N-05 + N-11 + W-07(b)** (Ch.11's coda and the duplicated two-sentence structure) — **one
   pass, same agent, after the dialogue pass**, because they are inside the same 400 words.
   N-11's recast is the only Ch.11 edit that is free in every metric direction. **Ask the author
   about N-05(c) first** — whether the property return notice has arrived changes Ch.12 onward.
4. **N-02 + N-03 + N-04 + W-02 + W-06 + W-14 + D-05's badge-log clause** — **one pass, Ch.10.**
   Four date corrections, two referent clarifications, and one three-word plant payoff. Ch.10 is
   the only chapter of the six with slack in both breath directions, so it can absorb a single
   pass comfortably. Net ≈ −10 words.
5. **N-01 + N-08(Ch.6) + W-03 + W-13** — **one pass, Ch.6.** The "Nine weeks" leftover, the four
   vouching sentences, the recovery-element day count, and the clinical note.
   ⚠️ **Ch.6 sits 0.5 above its narration median floor and 1.7 above its ≥40w floor, and three of
   these edits shorten long narration sentences. Re-measure after, and be prepared to use W-13's
   option 1 instead of option 2 if the ≥40w share drops.**
6. **N-07** (Hallam, Ch.9) + **W-04** (Christmas, Ch.9) + **N-10** (Ch.9's third cup-turn, if the
   author agrees it is not deliberate) — one pass, dialogue-only where possible, because **Ch.9's
   narration median is at its floor.**
7. **N-14 + N-08(Ch.8)** — **one pass, Ch.8, and open it once.** Ch.8 has ~1 em-dash of headroom
   and sits on two breath floors simultaneously. Net ≈ −8 words, which is the right direction.
8. **A-01 + A-03 + A-02** (Ch.4, Ch.3, Ch.2 — one word each) — the author's prose. **Confirm
   before applying, and apply A-01 and A-03 together or not at all.**
9. **N-06** (the "eleven hundred" recast in Ch.10 **plus** the four ALLOWLIST additions, in the
   same commit, or it comes back) — and **D-07**'s gate-filter fix alongside it.
10. **The docs: D-01, D-02, D-03, D-04, D-06.** No manuscript risk; do them while the chapter
    edits are in flight. **D-02 and D-04 are the two that would cause real damage if a later pass
    read the stale version.** Per the root CLAUDE.md PROPAGATION RULE, each of these touches a
    number or a rule that lives in three or four files — **grep before committing, and say in the
    commit message which files you checked.**
11. **D-05, W-11, W-12, and §6.12** — decisions, not defects. **Ask the author; do not invent.**
    §6.12 (registering "Vexx does not do the small kind thing" as a pattern) resolves two of
    D-05's seven rows at a stroke and costs nothing but a paragraph in `foundation.md`.

**Re-run this audit after step 5.** N-01 and the Ch.6 pass move an interval that Ch.7 and Ch.8
measure from, and a post-revision pass over Ch.6–8 is cheap insurance. **Re-run the entity tracker
after Ch.11's loop completes**, because every `ch-11`-sourced entry in the YAML is marked
`draft_status: "ch-11 pre-polish"` and may move.
