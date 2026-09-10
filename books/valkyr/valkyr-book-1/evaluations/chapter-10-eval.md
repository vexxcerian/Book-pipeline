# Evaluation: Chapter 10 — Compliance
**Evaluator:** book-evaluator | **Date:** 2026-09-10
**Scope:** 4,588 words (`style_check.py` tokenizer, comments stripped) / 2,392 narration-paragraph words / 2,196 dialogue-paragraph words. One room, five internal breaks, corridor coda, close.
**Dimension 7:** Momentum / Series Engine (carried from Ch.6–9).
**Anti-AI posture:** FULLY LIVE. Genre band: Commercial Fiction (settled Ch.6–8). Devoted Reader ACTIVE (SFF).
**Benchmarks:** Ch.1 (LOCKED) 8.5 / Prose 9.0 / Avg 8.71 · Ch.6 8.5/8.79 · Ch.7 8.5/8.79 · Ch.8 8.5/8.79 · Ch.9 (rev.4) 8.5/8.71.
**Two-register dialogue convention:** verified correct throughout. **CLOSED IN WRITING AT CH.8. NOT RE-OPENED. NOT A FINDING.**
**All measurements below were recomputed by me** on `style_check.py`'s own `words()`, `sentences()` and `split_registers()`, with all ten chapters measured in the same run by the same instrument. Where I use a definition of my own I state it in full.

---

## HEADLINE

**CVI-Launch:** 9.0 | **CVI-Legacy (chapter proxy):** 6.6 | **Genesis Floor:** 8.5 | **Genesis Average:** 8.64
**Engagement Type:** Fascination (primary — a man the reader knows is a murderer being decent for four thousand words, and being unable to look away) · Empathy (secondary — Dessen, and Vexx's involuntary gratitude) · Intellectual (tertiary — the chain-of-custody argument, which the reader must actually follow).
**Verdict: PASS.** Floor 8.5 · Casual Reader 8.5.

**Divergence Alert — YES, and in the direction that matters.** CVI-Launch 9.0 against Genesis Floor 8.5 is a 0.5 gap, and CVI-Launch against CVI-Legacy is a 2.4 gap. This is a chapter whose commercial charge (the shareable moment is one sentence and it is devastating) substantially exceeds its legacy inputs (no cultural vocabulary, chapter-level identity effect near zero). That is the correct profile for chapter 10 of 26 and needs no action.

**Gate-condition verdict, stated first because it is what the chapter must be judged on: IT HOLDS.** I audited all 23 Jameson turns myself, twice each, and I did not take three prior passes' word for it. Details in §2, including the one place I disagree with how the test is worded.

---

## THE FINDING OF THIS EVALUATION, STATED FIRST

**§THE FLAT-MAN — the pipeline has found one construction that satisfies the book's hardest rule, and it has been running it at ~6× the author for four chapters at a stable rate no gate measures.**

The rule is `voice-dna.md` §1.4: *"Never reports an emotional temperature. Zero instances in 14,776 words."* Ch.10 obeys it perfectly — **zero emotion words in 4,588 words** (no *felt*, *feeling*, *anger*, *afraid*, *relief*, *grateful*, *fear*; `grep` returns nothing). But there is a cost, and it is countable.

The construction is **GENERIC-PERSON MANNER ATTRIBUTION**: characterising how someone speaks or moves by comparing them to an unnamed generic person *performing an ordinary occupational action*.

> *"in the voice of a woman filing something"* · *"like a man reporting a figure off a gauge"* · *"like a woman reading out a train time"* · *"like a man carrying something wet"*

```
metric:             narration comparisons of the form
                      {like | the way | in the voice of | with the …of}
                      + {a|an|some} + {man|woman|men|women|somebody|someone|person|people}
                      + an ACTION (gerund / finite verb / "about to V" / "at the N").
                    Whole-chapter text; per 1,000 words on style_check.py's words().
author benchmark:   Ch.1  0 / 3,861 = 0.00   Ch.2  0 / 4,821 = 0.00
                    Ch.3  2 / 3,000 = 0.67   Ch.4  0 / 2,378 = 0.00
                    Ch.5  0 / 1,886 = 0.00
                    range 0.00–0.67/1k · pooled 2 / 15,946 = 0.13/1k · max COUNT 2
pipeline history:   Ch.6 3 (0.69) · Ch.7 0 (0.00) · Ch.8 5 (0.88) · Ch.9 3 (0.89)
this chapter:       4 / 4,588 = 0.87/1k
proposed threshold: REPORTED COUNT, human flag at >= 3 per chapter.
                    benchmark PASSES — the author's per-chapter maximum is 2, one
                    instance of headroom. Ch.6/8/9/10 flag; Ch.7 does not.
                    NOT a per-1k ceiling: counts run 0–5 and a density gate on numbers
                    that small is the same instability STANDING OFFENCE #3 already
                    refused to gate for. A ceiling at his 0.67 would sit below three
                    pipeline chapters by less than one instance.
```

Two things make this worth more than the count.

**1. The shape differs, not just the frequency.** The author's two instances attribute an *inner posture* — *"the way a man says a thing hoping to be corrected out of it"* (Ch.3), *"with the particular unease of a man witnessing a skill he'd been right to be cautious about"* (Ch.3). The pipeline's fifteen attribute *occupational flatness*: checking a table for dust, reading out a train time, reporting a figure off a gauge, signing something on his knee, asking about the weather, filing something, at the end of a shift, giving directions to a road he drives every week. **The author uses the construction to name what a man is feeling without naming it. The pipeline uses it to certify that a man is feeling nothing.** It is the default solution to the voice's central prohibition — a device that exists to pass the anti-pattern budget.

**2. It has plateaued, not risen.** 0.69 → 0.00 → 0.88 → 0.89 → 0.87. Every previous cross-chapter finding this project has made (the `, which` gloss, narration `and`) was a *rising* line that a gate caught and reversed. This one is flat, in band with itself, and invisible: it fires no style-check metric, it is worded differently every time, it never repeats a phrase, and `voice_wear_check.py` catches only its shadow (`[Vexx] self-repeat: "voice of a woman" — in 3 ch, 4x total`, buried in a clean run). **A habit that does not rise is not a drift the pipeline will notice; it is a house style the pipeline has already adopted.**

**In Ch.10 it does specific damage**, and this is the chapter's top revision finding (F2). Two of the four are the same sentence in different coats, 80 lines apart, on the chapter's two guest characters:

> l.144 — *"She said this **without any softening on it whatsoever**, **like a woman reading out a train time**."* (Dessen)
> l.224 — *"Jameson said it **with no lift on it whatsoever**, **like a man reporting a figure off a gauge**."* (Jameson)

Same frame, same vehicle class, same intensifier — and **`whatsoever` occurs 0 times in Chapters 1–9 and twice in Ch.10.** At the two moments the chapter most needs Dessen and Jameson to be different sizes, the narration renders them with the identical instrument. This is STANDING OFFENCE #3's diagnosis exactly — *"a NARRATOR-level habit that lands in whoever happens to be speaking, so auditing 'is this in character?' will never catch it"* — in a new coat, and all four passes cleared it because each line is in character.

**Second finding, related and smaller: §THE VOUCH-BY-NEGATION.** The disruptor was right that narrator vouching is the adjacent failure to menace, and right to cut *"the way a decent man does."* It cut the verdict and left six instances that do the same work in behaviour-clothes:

| # | Line | Subject |
|---|---|---|
| 1 | *"not making a point of it, not the small held pause of a person who means you to wait, simply finishing a line"* | Dessen |
| 2 | *"There was none of the small theater Vexx had been braced for — no folder pushed across the table, no pause held for effect, no question asked twice over…"* | Dessen |
| 3 | *"doing none of the small business a man does to make a point of arriving late"* | Jameson |
| 4 | *"He did none of the small courteous things people do to let a man off"* | Jameson |
| 5 | *"nothing on his own but the ordinary concern of somebody who has noticed that the person in front of him is having difficulty"* | Jameson |
| 6 | *"He did not ask again. He did not tilt his head, or say* are you sure*, or leave a door propped open in his voice…"* | Jameson |

```
metric:             narration clauses that DENY a performative or insincere behaviour and
                    attribute the denied behaviour to a generic third party, or deny
                    "performance" outright — thereby certifying the described character
                    as unperforming. Narration only; quoted spans and italic runs stripped
                    wherever they occur. Regex sweep, then every hit hand-read (the regex
                    over-collects: positive attributions like Ch.1's "the deliberate
                    caution of a man who…" are NOT this and were discarded).
author benchmark:   Ch.1 0 · Ch.2 2 · Ch.3 0 · Ch.4 0 · Ch.5 0
                    = 2 in 10,144 narration words (0.20/1k). Per-chapter max 2 (0.70/1k).
                    His two: "grave without performance, warm without excess" (Jameson,
                    Ch.2) and "none of the small props men bring into a room where they
                    expect to be weighed" (Zeus, Ch.2).
pipeline history:   Ch.6 0 · Ch.7 0 · Ch.8 0 · Ch.9 0
this chapter:       6 in 2,339 narration words = 2.57/1k
proposed threshold: REPORTED COUNT, human flag at >= 3 per chapter.
                    benchmark PASSES — his maximum is 2, one instance of headroom.
                    Again NOT a density gate: 0–6 instances is too few to be stable.
```

**And the polarity is inverted.** One of the author's two is undercut in the next breath — Ch.4: *"found nothing but the same practiced warmth Jameson had shown him from their very first meeting. He wanted, badly, for that to be reassuring. It wasn't, quite."* His certification of Jameson comes with a counterweight *in the same paragraph*. Ch.10's six have none. The chapter whose entire design is *"the reader supplies the chill; the scene supplies none"* tells the reader six times that these two people are not performing — and *decent* is the one word in this book a reader most needs to arrive at unassisted.

Both findings share the shape every previous evaluation has found and it is now four for four: **the pipeline generalises a distinctive requirement into house style, one register below where the watch-list looks.** Ch.8 found it in clause-joining, Ch.9 in subordination and punctuation, Ch.10 in *comparison vehicles* and *negative-space characterisation*. The watch-lists guard vocabulary, gesture wording and character devices. The drift keeps happening in grammar and in figure.

---

## §THE DEFINITION HAZARD — a live, preventable eleven-point failure sitting in this project's own documents right now

The brief asks me to measure numeric density and say whether it is gateable. In doing so I found that **"numeric density" currently means two incompatible things in two committed pipeline documents, and shipping one document's number with the other document's regex would put the locked Ch.1 in breach by 7.8 points.** This is the exact failure the standing rule exists to prevent, and it is currently latent, not hypothetical.

```
metric:            "numeric density /1k" — TWO DEFINITIONS IN CIRCULATION UNDER ONE NAME.
  Def A  (chapter-9-eval §10 P3): digits + spelled cardinals + ordinals
         + once/twice/half/quarter/dozen.
  Def C  (chapter-10 writer brief): digits + spelled cardinals ONLY.

author benchmark:  Def A   Ch.1 23.83 · Ch.2 23.02 · Ch.3 19.67 · Ch.4 18.92 · Ch.5 12.73
                           → range 12.73–23.83, max 23.83  (LOCKED Ch.1 is the maximum)
                   Def C   Ch.1 13.99 · Ch.2 13.90 · Ch.3 12.67 · Ch.4  9.25 · Ch.5  4.77
                           → range  4.77–13.99, max 13.99  (LOCKED Ch.1 is the maximum)

this chapter:      Def A   22.89/1k  → INSIDE the author's range (below his maximum)
                   Def C   15.04/1k  → 1.07x his maximum
                   (the writer reports 14.3 on Def C; the 0.7 gap is tokenizer/comment
                    handling, not disagreement. Both numbers say the same thing.)

proposed threshold: Def C, ceiling 16.0 — benchmark PASSES (author max 13.99, headroom 2.0)
                    Def A, ceiling 26.0 — benchmark PASSES (author max 23.83, headroom 2.2)

                    ⚠ DO NOT SHIP 16.0 WITH DEF A. The locked Ch.1 measures 23.83 and
                    would be in breach by 7.8 points, and every chapter of this book would
                    then be "repaired" toward a voice the author does not have. The Ch.9
                    evaluation quoted the author's maximum as 23.4 (Def A); the Ch.10
                    writer brief quoted it as 14.0 (Def C); a future implementer reading
                    both files will take the ceiling from one and the regex from the other.
                    Write the DEFINITION into the gate file beside the NUMBER.
```

**Answer to the question actually asked: yes, it is gateable, on Def C at 16.0, firing from Ch.11 with Ch.6–10 recorded pre-gate** (the simile-floor precedent), **and it still needs the declared-exemption mechanism the Ch.9 evaluation asked for** — Ch.7 (47.4 on Def C) is a records search and Ch.9 (34.0) counts the dead. A flat ceiling would be wrong for both.

**And the Ch.9 evaluation's parting warning can be closed.** Its last line was *"the number that should worry the orchestrator most is numeric density at 1.79× the author's maximum, in the fourth consecutive chapter above the flag."* Measured on **its own definition (Def A)**, Ch.10 posts **22.89 against the author's 12.73–23.83 — inside his range for the first time in five pipeline chapters.** Trajectory on Def A: 24.93 → 56.65 → 31.05 → 41.73 → **22.89.** The warning is answered. On Def C it sits 1.07× his maximum, which is a rounding error, not a divergence.

---

## §THE SEAM — measured, and a correction to the brief I was given

The brief states: *"Ch.10 is the first chapter to draft in band without a repair loop: narration `and` 17.7/1k against the author's 18.2–18.9 band."*

**That comparison is wrong, and acting on it would have sent an editor the wrong way.** 17.7/1k is the **whole-chapter** figure; 18.2–18.9 is the **narration** band. Comparing them makes Ch.10 look 0.5 points *under* the author's floor, and the obvious repair — adding conjunctions — would have pushed a compliant chapter out of band. This is precisely the error mode the Ch.9 evaluation retracted itself for (*"whole chapter instead of narration"*). Measured like for like, on the gate's own splitter:

| `and` /1k | Ch.1 | Ch.2 | Ch.3 | Ch.4 | Ch.5 | **Author** | Ch.6 | Ch.7 | Ch.8 | Ch.9 | **Ch.10** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Narration** | 18.43 | 18.29 | 18.90 | 18.19 | 18.81 | **18.19–18.90** | 20.68 | 20.39 | 22.07 | 24.35 ✗ | **18.39 ✓** |
| **Dialogue** | 27.17 | 17.09 | 13.89 | 20.41 | 11.42 | **11.42–27.17** | 27.09 | 10.24 | 25.06 | 20.14 | **16.85 ✓** |
| **Register sum** | 45.60 | 35.38 | 32.79 | 38.60 | 30.23 | **30.23–45.60** | 47.77 ✗ | 30.63 | 47.13 ✗ | 44.49 | **35.24 ✓** |
| **Whole chapter** | 19.68 | 17.84 | 17.33 | 18.92 | 15.38 | **15.38–19.68** | 23.33 ✗ | 16.47 | 23.16 ✗ | 22.35 ✗ | **17.65 ✓** |

**No scar. All four readings pass, and the narration figure does not merely re-enter the band — it lands on the author's own median.** His five chapters: 18.19, 18.29, 18.43, 18.81, 18.90. Ch.10: **18.39.** The pipeline's monotonic four-chapter rise (20.68 → 20.39 → 22.07 → 24.35) is reversed, and it is reversed to the centre rather than to an edge, which is what a voice match looks like as opposed to a metric hit.

The writer's own note is the reason and deserves to be recorded as pipeline knowledge: *"The conversion pass overshot to 16.9 — under the author's own minimum — and I put four `and`s back deliberately."* **The band has a floor and the floor did work.** A writer chasing a ceiling alone would have landed at 16.9 and written calmer than this author, which is the fault the em-dash floor was added to catch and which the Ch.9 evaluation predicted would recur.

---

## §THE QUESTION MARK — the pressure device is legible again, and the mechanism is better than the count

Ch.9 posted zero question marks in 3,355 words. Ch.10 posts **5 in 4,588 = 1.09/1k**, against the author's **1.04–3.00**. Inside the band, at the bottom of it.

The count is the least interesting part. What matters is whether the *unpunctuated* form reads as technique again, and it does — because the punctuation tracks **whether the speaker is on the record**, and it tracks it consistently enough that a re-reader can use it.

| Marked (5) | Unmarked (~12) |
|---|---|
| *Am I allowed a representative?* (Vexx, private channel) | *"Did anybody in the chain of that transaction work outside your cell."* |
| *"Do you want to sit down?"* (Dessen, off the record, to Jameson) | *"What was the material required for."* / *"used for."* / *"is being used for."* |
| *"All of it?"* (Dessen, surprised, unprocedural) | *"Do you dispute the period."* / *"Or that it ran out."* |
| *Can you get it?* (Vexx, private channel) | *"Against which reference."* / *"Where would I find it,"* |
| *Why?* (Rx, private channel) | *"Do you know what that word does."* / *"What did the board rule."* |

Dessen asks *"Do you dispute the period."* unmarked and *"Do you want to sit down?"* marked — same speaker, same syntax, eight scene-lines apart. The difference is that the first goes in the book and the second goes in the margin. Jameson's *"All of it."* (instruction, flat) answers Dessen's *"All of it?"* (surprise, marked) in a three-word exchange that teaches the reader the whole system in one beat. **That is the device working, not merely present.** The writer restored five marks and got a legible convention back for zero words.

**One note for the root, no gate proposed:** `style_check.py` already reports `question marks X/1k` and explicitly declines to gate it. That is correct and should stay correct — a floor would be gameable by punctuating the wrong questions. But the Ch.10 writer report is right that the number belongs in the **Writer brief** alongside the two ungated targets, because this drift is invisible at draft time (the first Ch.10 draft had zero in 4,646 words and the writer caught it himself). Surfacing it upstream is free.

---

## §THE GATE CONDITION — my own independent audit

I read all 23 Jameson turns twice: once as the scene means them, once in the voice of a man who watched Rx die at close range, wrote the report that buried it, and has come to a compliance room to find out how close an investigator has got to the Corwin material.

**Verdict: IT HOLDS. Concurring with three prior passes, on my own reading, and I tested lines they did not name.**

**But first — the test as the brief words it is wrong, and if applied literally it would delete the chapter's best effects.** The brief says: *"If a line survives the second reading with extra meaning, it fails."* Under that wording, this line fails:

> *"…every board that ever opens him reads it first, and not a single one of them ever finds out it was written by somebody who has never in her life had to decide anything in under a minute."*

It yields enormous extra meaning to a reader who knows Jameson's own crime is a written report nobody ever questioned. But `character-bible.md` says the opposite thing and says it better: *"All the irony in this book belongs to the reader's later knowledge, never to his performance."* **The operative test is not whether extra meaning exists; it is whether the extra meaning belongs to the character or to the reader.** Sharpened, for the root:

> A Jameson line fails if the second meaning is **available to Jameson** — if he could be saying it on purpose, if it names a future, if it leaves Vexx something to act on, or if Vexx could replay it later and hear a different sentence. It passes if the second meaning exists **only in the reader's hands**, assembled from knowledge Jameson does not have.

Under that test, every line passes. The six I tested hardest, three of which the prior passes did not name:

**(1) The steelman — *"he drew it in person, off the counter, himself, which isn't in your finding and should be, because that was the last place a third party could have got into the chain, and he shut that door too."*** The most available second layer in the chapter: a murderer establishing on the record that his investigator acted alone, uncorroborated. It survives, and it is the chapter's strongest proof of innocence-of-intent — **the extra meaning is worse for Jameson, not better.** A man managing this room does not hand the prosecutor her missing paragraph, and he calls it *"worse"* one clause later. Passes.

**(2) *"That's the trouble with an honest man in a compliance room — he's the only person in it who can be talked out of his own position."*** Second-hardest, and the prior passes cleared it as "fondness, and also simply true." I agree, and I want the reason on the page: **the sentence means exactly the same thing at both levels.** It is not a warning (no future named), not an offer, and Vexx cannot replay it as directed at anything but the audit. It is also a man describing his own method to its subject without knowing he is — which is the reader's, not his.

**(3) *"I know who you are. I've read your file. I've read your finding."*** Cold, the classic intimidation opener. It is addressed to **Dessen**, not Vexx, so there is nothing for Vexx to replay; it is his established warm Ch.2 move; and it is capped one clause later by a man volunteering that he is wet and coatless, which is nobody's play. Passes.

**(4) *"Do you know what that word does. Not to a career — to a file. It sits in the second field for the rest of a man's service."*** Not previously named, and I flag it — **not as a gate failure but as a canon cost.** See F3: this is Ch.19's concept (*"They don't kill you. They file you."*) on the page nine chapters early, in a more articulate mouth. It clears the gate (no knowledge, no warning, about careers rather than lives, and it is dialogue rather than the narration `voice-dna.md` §4 actually bans) and it narrows Corwin's gap.

**(5) *"That woman is going to run this directorate in nine years, and I have made an enemy of her in a store cupboard."*** Available as a killer worrying about a future investigator. Survives on scale: it is vanity, in a store cupboard, thirty seconds after saving a man's career. A man who knew would find this a strangely trivial thing to be worrying about.

**(6) The aneroid speech.** No exit line, verified — he leaves mid-clause (*"everything off the—"*) and the doors take the rest. Not a beat of the barometer is metaphorical; the dialogue pass's replacement of *"Which is not weather. That's a front"* with *"That much in two days is a front"* was the right call and I would have made the same one, because the earlier version is the shape a reader converts into foreshadowing regardless of intent.

**He is never told anything he does not already have.** He arrives having read the file, wins on a public disposition line any competent officer could have found, and gains nothing from the room. Independently verified: zero flash-forward constructions anywhere in the chapter (`would later` / `would learn` / `would come to` / `did not yet know` / `had no way of knowing` / `it would be some time before` — **zero hits in 4,588 words**), and **zero retrospective-narrator intrusions** against a budget of ≤2.

**That last number is the gate condition working structurally, and it deserves credit.** `voice-dna.md` §1.2(a) calls the retrospective narrator *"the book's defining move."* Ch.10 uses it not once — because any retrospective intrusion in this chapter would be the narrator knowing something about Jameson, which is the one thing forbidden. The chapter's signature-voice absence is the design, not a deficiency, and no future editor should "restore" it here.

**Fourth failure mode — narrator vouching: PARTIALLY PRESENT.** See §THE VOUCH-BY-NEGATION above and F1. The disruptor was right about the failure mode and cut the right line; six instances of the same work survive in behaviour-clothes, four of them on Jameson, and the polarity has no counterweight where the author's does. This is the chapter's top revision finding. It is **not** a gate failure — nothing certifies him as *safe*, only as *unperforming* — but it spends some of the reader's discovery.

---

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|---|---|---|---|
| **Originality** | **8.5** | Two moves I cannot name a precedent for. **(a) A rescue the reader does not want.** The genre-standard internal-affairs beat is doubly subverted exactly as the outline promises: the investigator is right, the finding **stands** (*"The finding stands. It's correct, I'm not amending it. The recommendation falls away"*), and the villain intervenes on the hero's side, sincerely — so the scene's tension resolves into gratitude, which is a far worse thing to be holding. **(b) The closing beat**, the tenth distinct closing shape in ten chapters: a man taking barometric figures and putting them *"into the place built into him at fourteen for holding things he would have to say back quickly, correctly, under pressure, to a man who would be pleased with him"* — memorising small talk to please his brother's murderer, unnarrated, in an empty corridor. Last verb: *learned them.* | Not 9.0: the components (compliance audit, senior officer intervenes, protagonist indebted) are individually familiar; the originality is entirely in arrangement and emotional target, which is execution-level and correctly scores here. |
| **Theme** | **9.0** | *"Theme: strong, inverted"* — and stated nowhere; verified, no line in 4,588 words asks or answers *what a man is willing to become*. It is asked of **both** men in one room and answered in opposite directions. Of Jameson, by conduct alone: eight seconds of ugly anger, then *"The first part was temper. The second part I chose."* Of Vexx, by Dessen, in a line that does not know what it is asking: **"You didn't destroy it. You did something narrower. You made it useless to him."** Organic texture confirmed — the shirt collar, the dying pen bought by the gross, the fishing advisory nobody has ever needed, the tray gone brown at the rim, the strap set for somebody else's shoulder. | — |
| **Characters** | **8.5** | **Chaos 4/4, INHABITED, none narrated as chaos.** Irrelevant thought: *"There is a way of folding a shirt so the collar never creases, and neither of them had ever learned it"* — two sentences, no justification, cut across mid-word by Dessen's next line. Unprompted memory, 2nd appearance and mutated: the mess hall, and he is no longer sure it was 1100 — *"in which case everything after it in that day sat in the wrong order too."* Cognitive distortion: *"He had been careful. He had been careful the entire time."* Failed management: *"came half out of the chair without having worked out what he intended to do with the rest of the movement."* **Voice under pressure DEMONSTRATED** — flat mode at the corridor (*"He had his mouth open. He shut it. Then he did it again."*), plus present-tense leakage twice. **Dessen is a genuinely new person with a life the protagonist does not touch**: the dying pen, the strap, and a transfer she raises unprompted, is answered *"No,"* and nobody picks up. **Jameson has his own chaos, not about Vexx** — the store-cupboard vanity, the barometer landing on nobody twice. | Not 9.0: **the certification cluster** (§THE VOUCH-BY-NEGATION, 6 instances, 4 on Jameson) is the narration doing character work the characters should do; and the twin *whatsoever* similes (F2) render the two guest characters with the identical instrument 80 lines apart. Also: by design, the protagonist is the least characterised person in his own chapter for two thirds of it. |
| **Prose & Voice** | **8.5** | **Stopping sentence, cited:** *"She wrote down the apology at the same speed she had written down the insult, in the same hand, without hurrying, without any change at all in the sound of the pen — the only thing in that room, from first to last, that treated the two of them as the same size."* Fifteen citable underlines; runners: *"The pen made a sound in the quiet room like a fingernail going down a seam."* · *"Not because it's contaminated — because there's no longer anyone who can say it isn't."* · *"They broke it. He inherited it."* · *"He went out, left the door standing open, and somebody had to get up to shut it. It was Vexx."* · *"a case with a strap, the strap set for somebody else's shoulder, never since changed."* **Declared ugly sentence present:** *"The water in the jug had been there since before the room was booked and he drank two glasses of it."* Every band clean and mid-range, not edge-hit (see §THE SEAM). | Not 9.0: **F2** (the twin flat-professional simile with a novel intensifier used twice in a book that had never used it once) and **F1** (six sincerity certifications against an author maximum of two). Both are sentences an editor circles. Not 8.0: the stopping sentence is real, cited, and carries the chapter's thesis with **zero intensity words in it**. |
| **Pacing & Coherence** | **8.5** | **Value shift is double and in opposite directions** — situationally positive (recommendation falls, command retained), morally negative (he learns what the breach cost Corwin, is caught fabricating inside a minute, and ends the chapter rehearsing weather for his brother's killer). Reading speed genuinely designed and independently visible: the audit's narration median walks *down* 21 → 23 → 14 → 18.5 → **7.0**, and §5 — *"You didn't destroy it. You did something narrower"* — is the only section in the chapter with no long sentence in it at all. The gear change lands **at the door**: *"The door opened."* (3w) → 14w / 36w / 5w / 6w → seven consecutive sub-nine-word turns. Full stop at the corridor, where the longest sentence in the coda is the one describing a man **waiting**. No internal contradiction found: the heating functions as a clock (up / off / on-ran-off) and never disagrees with itself; 1140 summons at 1020, *"about an hour,"* Rx's twenty-two minutes at the triple — all consistent. | Not 9.0: one genuine skim window — the dismantling (l.200–232), ~500 words in which the reader must follow a legal argument about disposition lines, remits and schedules to get the win. And a close that deliberately refuses an information hook (correct artistically; measurable commercially). |
| **Emotion** | **9.0** | **Anchor lands and there are three of them.** (1) The pen writing the apology at the speed of the insult. (2) *"the tag with the dent in one corner, the serial that came back as nothing at all, lying in a drawer beside his bed among a watch strap, a cufflink, a torch he never used, half a mile east of the chair he was sitting in, where it would still be tonight."* (3) The barometer close. **Emotional surprise executed as a leak, not a description** — the disruptor's two words: *"It'll keep," Vexx said. "Thank you."* No narration, no reflection, nobody remarks on it, twelve lines after Jameson said *"Don't thank me."* **Earned rather than asserted**: it arrives in the physical location Ch.2 established (*"There it was, under the breastbone, the same as it had been in a briefing room two levels below anything with a name on the door"*) and Ch.2 supplies the mechanism (four years hungry for anyone who'd say his brother's name right). **Body rebel ×3.** **Technique variety: 5** (physical sensation · displacement onto objects · failed control · wrong emotion in the right place · silence). **Zero emotion words in 4,588 words.** | Not 9.5: the Ch.2 callback does a little of the reader's remembering for them (F4 — *"the first time a man he had never met said his brother's name out loud and got the weight of it right"*), and l.298 tells the reader what is on Jameson's face rather than what it is doing. |
| **Momentum / Series Engine** | **8.5** | Five forward loads, and one of them is a dated clock: *"You'll get a property return notice inside a fortnight. Answer it the same day." / "I will," Vexx said. / **"People say that."**"* — a two-word prediction of failure, followed sixteen lines later by the reader being shown the object she does not know about, sitting in a drawer. That is the best momentum device in the chapter. Also: Vexx now consciously owes Jameson; **Rx goes near-silent from the moment Jameson enters and Vexx does not flag it**; Dessen's refused transfer is a Book-Two asset; the barometer is a Ch.12/Ch.24 plant. **No unlock fires** — verified. Jameson is present in person and stage 3 is intact for Ch.13. | Not 9.0, two reasons, both specific. (a) **Placement**: the live obligation is delivered at the 85% mark and the final 650 words renew nothing — the last page is a mood-load, not an obligation-load. That is the right artistic choice and a measurable momentum cost, and it is recorded here **so the editor does not chase it** (see F5). (b) **F3** — Ch.19's concept is pre-figured. |
| **FLOOR** | **8.5** | | |
| **AVERAGE** | **8.64** | | |

**Trajectory: Ch.1 8.5/8.71 (locked) → Ch.6 8.5/8.79 → Ch.7 8.5/8.79 → Ch.8 8.5/8.79 → Ch.9 rev.4 8.5/8.71 → Ch.10 8.5/8.64.**

Floor/average gap **0.14** — the tightest in the manuscript. No single-dimension bottleneck; the chapter is flat at 8.5–9.0 with nothing sagging and nothing spiking. The average is the lowest of the passing chapters by 0.15, and it is the arithmetic of a chapter that is very good at five things and excellent at two, rather than a chapter with a hole.

**I interrogated whether I am scoring low to look independent.** The test I applied: would I have scored Ch.9 higher for the same profile? Ch.9's revised card is 8.5 / 9.0 / 8.5 / 8.5 / 8.5 / 9.0 / **9.0** = 8.71. Mine is identical except Momentum. So the entire delta is one dimension, and I have published two named reasons for it (placement arithmetic and F3), either of which the orchestrator can overrule. If Momentum goes to 9.0 the average is 8.71 and the chapter is level with Ch.1 and Ch.9. **I would not fight hard for 8.5 over 9.0 on Momentum. I would fight hard for every other number on this card.**

---

## CVI-Launch Breakdown

| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | **7.0/10** | 4,588 words, second-longest chapter in the book, single room, near-real-time procedure. Chapter-end is a mood-load. Curiosity gap present and sharp (*"People say that."*) but placed at 85%. A non-reader would need to want the people. |
| Tomorrow Test | **3 anchors (IMAGE ×3)** → 9 | The pen writing the apology at the speed of the insult · the dog tag in the drawer half a mile east of the chair · a man learning a week of barometric pressure in an empty corridor. (A fourth — the strap set for somebody else's shoulder — is a lovely detail but not one a reader names the next morning.) |
| Casual Reader | **8.5/10** | See report. Exactly on the gate; 8.0 is defensible. |
| Shareability (quote / plot / emotional) | **4 / 4 / 4** → MAX 8 ×0.6 + AVG 8 ×0.4 = **8.0** | Quote: *"That isn't a favor, it's Thursday."* / *"The first part was temper. The second part I chose."* / *"They broke it. He inherited it."* / *"People say that."* Plot: *the man he suspects of killing his brother saves his career.* Emotional: *he memorises the weather so he'll have something to say to his brother's killer.* |
| Concept Pitch | **yes** → 10 | Unchanged and strong. |
| Human Closeness | **yes** → 10 | Three people in one small room for 4,000 words, and the intimacy IS the subject. |

**CVI-Launch = 1.4 + 1.8 + 1.7 + 1.6 + 1.0 + 1.0 = 8.5, +0.5 (anchor exists) = 9.0.**

**CVI-Legacy (chapter proxy, default weights — engagement is Fascination-primary, not Aspiration):** Originality 8.5 (.30) + Theme 9.0 (.25) + Cultural Vocabulary 2 (.20) + Re-readability 7 (.15) + Identity Effect 3 (.10) = **6.6.** Re-readability is the strong input and it is genuinely 7: **this chapter is a different chapter on a second reading**, because every warm thing Jameson does becomes something else, and none of it changes a word.

---

## Anti-AI Scan (20 patterns + 1 project-local) — density on 4,588 words

| # | Pattern | Verdict | Density | Citation / reasoning |
|---|---|---|---|---|
| 1 | Forced symmetry | **FOUND — deliberate, half weight** | 1 frame, 0.22/1k | The fire-door lip where the money ran out, opening and closing. Kept: he walks it at the top carrying a rehearsed answer to a question nobody asks him, and stands in it at the end rehearsing an answer nobody has asked for at all, on purpose, for the man who killed his brother. Same image, opposite meaning. |
| 2 | Empty poetic vocabulary | **CLEAR** | 0 | Ten comparisons, every vehicle physical or domestic. No abstraction anywhere. |
| 3 | Automatic rule of three | **CLEAR** | 5.67/1k (proxy) | **Author range 4.56–6.00; Ch.10 is inside it.** See §RETRACTION 1 — this closes a Ch.9 hypothesis. The triads that stand out (*"armor plating…, a data chip burned past recovery, a dog tag"*) are `voice-dna.md` §1.3(3), the author's own catalogue-in-place-of-a-feeling, reprising Ch.1 exactly. |
| 4 | Excessive em-dashes | **CLEAR** | 48 = 10.46/1k | Author 9.0–11.8. It is the voice. |
| 5 | Empty metaphors | **CLEAR** | 0 | Zero explanatory extensions on any of the ten similes; the disruptor cut the one that had a tail (*the shopping list*). |
| 6 | Dramatic "And" openings | **FOUND — minor, half weight** | 2 = 0.44/1k | *"And his body knew the difference…"* · *"And I came in over the top of a sentence you were entitled to finish."* Author uses it (Ch.1 ×2, Ch.2 ×1). |
| 7 | Pseudo-philosophical closings | **CLEAR** | 0 | Every scene-end is flat: *"Nobody wanted it." · "The heating went off." · "Dessen wrote it down." · "It was Vexx."* The chapter closes on *"and learned them."* |
| 8 | Excessive parallelism | **FOUND — moderate, full weight** | 3 = 0.65/1k | *"He did not sit. He did not say excuse me."* / *"He did not ask again. He did not tilt his head…"* — the same anaphoric frame bookending Jameson's presence, plus *"He raised it. He countersigned it."* Folded into F1: the first two are also certifications. |
| 9 | Overly smooth transitions | **CLEAR** | 0 | Every break is a hard cut. The mess hall opens cold with no bridge; *"The door opened."* |
| 10 | Described emotions | **CLEAR** | **0 emotion words in 4,588** | No *felt / feeling / anger / afraid / relief / grateful / fear / sad / guilt*. `grep` returns nothing. Exceptional. |
| 11 | **Explanatory Extension** | **CLEAR** — arithmetic below | broad 1.09/1k · narration gloss 0.38/1k | Both readings pass, one of them below the author's *minimum*. See the boxed arithmetic. |
| 12 | Binary negation opener | **FOUND — minor, half weight** | 1 = 0.22/1k | l.18, in appositive form with a positive resolution: *"not making a point of it, not the small held pause of a person who means you to wait, simply finishing a line."* The author's nearest (Ch.2, *"no data pad, no file, none of the small props"*) has no positive third beat. Same sentence as F1 instance 1. |
| 13 | Precision Flex | **FOUND — moderate, full weight** | Def C 15.04/1k vs author max 13.99 | 1.07× his maximum. Substantially character-licensed (Jameson's card: *"concrete nouns and precise numbers"*) and structurally licensed (a compliance audit). See §THE DEFINITION HAZARD. |
| 14 | Emotional control demonstration | **FOUND — minor, half weight** | 1 = 0.22/1k | *"His hand was on the edge of the table. He took it off."* — notice → manage → continue. It is immediately followed by a confession, so the management fails in the same breath. Everywhere else the pattern is **inverted**: he comes half out of the chair, his mouth opens and shuts twice, and the thank-you leaks out through the gap the deflection left. |
| 15 | Authoritative description | **CLEAR — actively inverted** | 0 | The room is described with holes in it: *"where somebody had run out of it, or run out of the money for it"* · *"cut open again later with a knife, by somebody in a hurry."* And the chapter's centre is an epistemic failure: *"It was not eleven hundred. It might have been the late sitting."* This is the opposite of the pattern and it is a strength. |
| 16 | Philosophical asides | **FOUND — minor, half weight** | 2 in narration = 0.44/1k | *"there is no strain in that at all"* (gnomic present tense) and *"which does nothing to an elevator anywhere in the galaxy"* (wit, and shareable). The aphoristic lines in **dialogue** are character-licensed and not counted (Jameson's card licenses stating things better than you would; Rx's joke-definition of a board is his register). |
| 17 | Clean dialogue | **CLEAR** | 7 breaks | Genuinely messy: *"—the fourteen days,"* cuts across the shirt-folding mid-thought · *"And you are—"* · *"…his fitness to hold—"* / **The door opened.** · *"Sir—" / "Richard."* · *"My brother's—"* · the elevator doors taking the aneroid sentence · *"It isn't," he said. "Being used."* Plus Dessen answering a question nobody asked (*"The water's been standing since yesterday"*) and raising her own transfer, which nobody picks up. |
| 18 | Thematic echo chamber | **CLEAR** | — | Substantial non-thematic texture: the shirt collar, the pens bought by the gross, the fishing advisory, the tray gone brown at the rim, the strap. |
| 19 | Graduated reveal | **CLEAR** | — | Single-scene near-real-time held for 4,000 words in one room; structurally unlike Ch.9's two-location night mosaic. Tenth distinct closing shape in ten chapters. |
| 20 | Emotional temperature report | **CLEAR** | 0 | See #10. |
| **21** | **Generic-person manner attribution** *(project-local — proposed addition)* | **FOUND — moderate, full weight** | 4 = 0.87/1k vs author max 0.67 | §THE FLAT-MAN. Two of the four are twins 80 lines apart. **This is the pattern the 20 do not have a slot for and it is this pipeline's most durable fingerprint on this book.** |

**8 patterns found (5 minor / half weight), 13 clear. Commercial Fiction band: 0–8 = CLEAN.** Ch.10 sits at the top of clean. No over-correction flag (not 0/20).

### ⚠️ Pattern #11 — the arithmetic in full, all three readings, and which I applied

```
READING (A) — V3.4 as written, Commercial Fiction: >6 instances OR >0.8/1k
  instrument: `the way X` + `, which` + `as if/as though`, whole text
  Ch.10 count 5   (threshold >6)   -> not breached
  Ch.10 density 1.09/1k            -> BREACHED
  Chapter is 4,588 words, ABOVE the 2,500-word carve-out, so both thresholds apply
  and the density reading would cap Prose at 7.5.
  BUT it breaches for ALL FIVE author chapters: Ch.1 1.30 · Ch.2 2.08 · Ch.3 2.35 ·
  Ch.4 2.11 · Ch.5 3.19 — including the LOCKED Ch.1, which it fails HARDER than
  it fails Ch.10 (1.30 vs 1.09).
  A threshold that fails the benchmark is measuring the language, not the pipeline.
  >>> NOT APPLIED. This is the third consecutive evaluation to publish this and decline it.

READING (B) — author-benchmarked, broad definition
  Author 1.30–3.19/1k  ·  Ch.10 1.09/1k
  >>> PASS. BELOW THE AUTHOR'S MINIMUM. The lowest broad-#11 figure in the manuscript,
      author chapters included. Composition: theway 0 / `, which` 5 / as-if 0.

READING (C) — author-benchmarked, NARROW (the `, which` gloss in narration)
  Two splitters, both reported, because they disagree by one instance:
    paragraph-based (the gate's own):  author 0.00–0.99/1k  ·  Ch.10 0.00/1k -> PASS
    span-based (quoted + italic runs stripped WHEREVER they occur):
                                       author 0.00–0.92/1k  ·  Ch.10 0.38/1k -> PASS
  >>> PASS on both. The single narration gloss is the elevator joke.
```

**All coherent readings agree: no cap. And a definitional note for the root, benchmarked as required.** The gate's paragraph-based splitter classifies a whole paragraph as dialogue if it *opens* with a quotation mark, so narrator prose embedded after a spoken line is invisible to `which_gloss_per1k`. Ch.10 scores a perfect 0.00 while containing a narrator gloss (*"Jameson pressed the call plate a second time, which does nothing to an elevator anywhere in the galaxy"*).

```
metric:            `, which` per 1,000 NARRATION words, narration defined by SPAN
                   (strip quoted spans and italic runs wherever they occur) rather than
                   by paragraph-opening character.
author benchmark:  Ch.1 0.00 · Ch.2 0.28 · Ch.3 0.00 · Ch.4 0.58 · Ch.5 0.92 → max 0.92
this chapter:      1 / 2,646 = 0.38/1k
proposed threshold: KEEP the existing 1.0. benchmark PASSES (his max 0.92, headroom 0.08 —
                   marginally safer than the current paragraph-based 0.99/1.0).
                   Change the DEFINITION, not the number. This is a strict improvement:
                   it closes a channel that currently reads 0.00 and it loosens nothing.
```

**Reported and NOT a finding, with the arithmetic shown so the next pass does not re-derive it:** Ch.10's **whole-text** `, which` is 5 = 1.09/1k against the author's whole-text 0.00–0.53 — 2.1× his maximum. **Four of the five are in Jameson's mouth**, whose card licenses exactly this register (*pre-empts your objection and states it better than you would*). Gating a character's licensed device is the error `style_check.py`'s own calibration comments warn about three times. **Report the whole-text figure; do not gate it.**

---

## Character Chaos Check — Vexx (primary)

- **Irrelevant thought:** **PRESENT** — the shirt collar, two sentences, connected to nothing, cut across mid-word by Dessen's next line.
- **Cognitive distortion:** **PRESENT** — retrospective determinism: *"He had gone down to that counter on a Thursday afternoon… He had read the second field of the form, and had read it properly, and had signed underneath it. He had been careful. He had been careful the entire time."*
- **Unprompted memory:** **PRESENT**, second appearance and **mutated** — the mess hall, and the doubt has escalated from Ch.6 (the light was wrong) to the whole day (*"everything after it in that day sat in the wrong order too"*). Deliberately avoids Ch.1/Ch.6 wording.
- **Failed emotional management:** **PRESENT ×3** — half out of the chair; the mouth opening and shutting twice; *"It came out of him with more in it than he had meant to put there."*
- **Voice under pressure:** **DEMONSTRATED.** Flat mode at the corridor (*"He had his mouth open. He shut it. Then he did it again."*), the unfinished sentence rendered as an absence (*"Three words, and then whatever came after them did not arrive"*), and present-tense leakage twice.

**4/4, inhabited.** Nothing is narrated *as* chaos anywhere.

## Secondary Character Chaos

- **DESSEN** — **has her own life, three times, none of it about Vexx.** The pen that dies at the tail mid-interview and the small human annoyance about it (*"They're bought by the gross"*); the case with *"a strap set for somebody else's shoulder, never since changed"*; and the transfer she raises unprompted at the end, is answered *"No,"* and which nobody in the room picks up. She is **not** a stooge and **not** a bully: her case is correct, she declines to chase the clerk because *"the clerk isn't my question,"* she concedes only after checking it herself (*"That's better than I had it"*), and **her finding stands** — only the recommendation falls.
- **JAMESON** — the barometer twice, both landing on nobody (Dessen turns a leaf; the doors take the second one); the eight seconds; the apology; and his own vanity thirty seconds after saving a man's career (*"That woman is going to run this directorate in nine years, and I have made an enemy of her in a store cupboard"*).
- **RX** — present, useful, **no unlock fires**, capped denial **not used** (verified: zero instances of the phrase family in Ch.10; all five smooth firings remain spent and Ch.13 is safe).

No secondary functions only as a protagonist tool. No cap.

**One item cleared that a future editor must not "fix."** l.278: *"Rx had said on the stairs, answering something Vexx had not asked him, and had said almost nothing since the audit-room door opened."* Rx does speak inside the audit (l.92, ~65 words). *"Almost nothing"* carries it for the book's most talkative presence. More importantly, **the vagueness is load-bearing**: the plant means *since Jameson came in* (Rx is silent from l.146 to l.278, without exception), and writing that would make Vexx notice something suspicious, which the outline forbids in terms. **The imprecision is the design. Do not sharpen it.**

---

## Device Bleed — audited independently, every speaker against every reserved device

I ran §STANDING OFFENCES by name first, in narration and reported speech as well as quoted lines, and I re-ran the one-device map myself rather than reading the dialogue pass's table.

| # | Rule | My verdict |
|---|---|---|
| 1 | Zeus never asks why | **CLEAR.** Zeus absent, unnamed, unreported (`grep -i zeus` → 0). The only *why* in the chapter is Rx's, which is legal. |
| 2 | Aglaope does not use Zeus's *"That's not X. That's Y"* | **CLEAR as to Aglaope** (absent). The *shape* appears once in Jameson's mouth (*"That isn't a favor, it's Thursday"*) and I concur with the dialogue pass's reasoning for keeping it: Zeus's device supplies the **true** category; Jameson supplies an **absurd** one to refuse credit. Deflation, not correction, aimed at himself. One instance on a non-owner is under the owner's own allowance. |
| 3 | Only Spector counts ALOUD (incl. *N-of-the-M*) | **CLEAR IN THE FINAL TEXT.** The Jameson instances (*four findings … three of them*; *twice this year … both times*) were caught and removed at dialogue-polish, and the surviving *twice a year / both times* is **Dessen's**, load-bearing (she applied twice and was refused twice), appearing once in the chapter. **The offence row should now be amended: it lists "Ch.10 (Jameson)" as broken, and it was found AND FIXED before the chapter reached me.** Fourth consecutive chapter in which the construction appeared in a *different* mouth and was caught — the narrator-level diagnosis in that row is confirmed again. |
| 4 | Rx's denial capped at 5/5 | **CLEAR.** Zero instances. |
| 5 | The tidying gesture | **CLEAR. Zero.** Grepped `squar/quarter-turn/straighten/tidy/lined up/aligned` — nothing. |
| 6 | Hands flat on a surface (Ch.1's) | **CLEAR. Zero.** Nearest is *"He set his hands on the arms of the chair"* — a different object, a different gesture. |

**Gesture vocabulary is the cleanest in the book.** Two characters hold two large uncontaminated physical vocabularies for four thousand words in one room: the **pen** (19 instances, Dessen only, this chapter only) and the **cap** (6 instances, Jameson only, `grep "his cap"` returns chapter-10 exclusively). Vexx gets the table **edge** — the correct Ch.9 substitute for offence #6. The new character picked up neither over-spent gesture.

**Two residuals I log rather than fix:**
- *"He set the pad down on the table without looking at where it landed"* (Jameson) shares six words with Ch.6's *"set the pad down on the wood face-down"* (Voss). One each, opposite meanings (her controlled face-down return vs. a man who has never had to track his own props). **A third user makes it bleed.**
- The **file-family** appears twice in Ch.10 — *"filed where nobody would have cause to open it again"* and *"in the voice of a woman filing something."* The **CLOSED** phrase (`filed it away` / `filed away`) is untouched, verified manuscript-wide. Both uses are literal and neither connects Vexx's coping verb to Ch.19's line. Cleared, and recorded so it is not re-derived.

---

## Cover-the-Name — run independently

I stripped tags, beats and turn order from all 116 quoted spans plus the italic interface turns and read them cold against the twenty-voice cast. **I concur with the dialogue pass's numbers and with its conclusion, and I want to add the measurement that makes the conclusion checkable.**

**36% of the quoted turns in this chapter are three words or fewer** (42 of 116; median turn 5 words; 22% are two words or fewer). A ≤3-word turn is not a voice test in any book by any author. All 13 of the reported INDISTINCT turns are in that bucket — Vexx's four bare *"No."*s, *"Yes."*, *"I did."*; Dessen's *"Inconclusive."*, *"That's it,"*; Jameson's *"All of it."* Lengthening them to satisfy a metric would destroy the airlessness the chapter exists for.

**The test that matters is whether the four voices collide, and they do not.** Every INDISTINCT that was a *misassignment* — a line landing on the wrong character because it wore that character's device — is gone; there were three and there are none. My own spot checks landed correctly and unmistakably:

- *"Every last one of these dies at the tail. Every single one. They're bought by the gross."* → nobody else in this book is annoyed about stationery → **Dessen**
- *"It doesn't, I'd have to argue the distinction, I'd win it, it would take four months."* → a woman who has costed an argument in months and knows she would win → **Dessen**
- *"Then let me put your case, because I don't think you've put it hard enough."* → improve the objection, then defeat it → **Jameson**
- *"You wouldn't. I didn't log an extension. I said that because you asked me a question I had no answer to, and it seemed better to have one."* → a man correcting the terms of his own lie → **Vexx**, and it is his device turned inward, which is the best use of it in the manuscript.

**Verdict on the 51.1% strict rate: it is the form, not a defect — with one qualification.** The rate is depressed by a structural property of a caution interview (a third of turns are monosyllables) and not by voice convergence. The place voice convergence *does* occur in this chapter is **narration, not dialogue** — F2, where two characters are described with the identical instrument. Cover-the-name measures whether a line is distinctive; it has never measured whether the *narrator* is describing two people the same way, and that is the second time this project has found the drift one register below the instrument.

**Dialogue share: 47.9%** (2,196 of 4,588), the highest in the book and above `voice-dna.md`'s 28–40% band. **Reported, not flagged**: the author's own Ch.5 runs 46.4%, so Ch.10 is 1.5 points above his maximum in a chapter that is structurally one long interrogation. At his ceiling, not beyond it.

---

## The Brief's Testable Items, Answered

**1. Is the gratitude genuinely felt, and earned rather than asserted? YES.** It is placed in the same anatomical location Ch.2 used, and it happens four times with escalating loss of control: to Dessen with *"more in it than he had meant to put there"*; to Jameson formally (*"I wanted to say thank you"*); to Jameson involuntarily, two words with no narration, four seconds after a sentence about his brother failed to arrive; and finally to nobody, in an empty corridor, by learning a week of barometric pressure. **The disruptor's two-word addition is the strongest single edit made to this chapter by any pass.** Before it, the coda's last emotional event was a competent deflection. Now the deflection is followed immediately by the thing leaking through the gap it left, and Jameson's *"As you like"* does not notice.

**2. Is Dessen's case correct, and is she neither stooge nor bully? YES, and the writer's out-of-outline addition is the reason.** The outline asked only that her case be *correct*, which would have made it a procedure argument, and a reader sides with the protagonist against a procedure every time. The fifth scene break gives her the moral half and it is the chapter's value shift: *"That plate cannot now be put in front of anybody. Not because it's contaminated — because there's no longer anyone who can say it isn't."* / *"You didn't destroy it. You did something narrower. You made it useless to him."* **This is what makes Jameson's rescue a bad thing to be grateful for, and without it the chapter has no cost left at the end.** It should be protected in any future edit.

**3. The triple question — verified, and it works.**

| | Question | Change | Answer | Length |
|---|---|---|---|---|
| 1 | *"What was the material required for."* | — | *"Secondary examination."* | 2 words |
| 2 | *"What was the material used for."* | **required → used** (one word) | *"I looked at it again… on a kitchen table with a lamp brought down close to it."* | 47 words |
| 3 | *"What is the material being used for."* | **was → is + being** (two tokens, one tense) | *"It isn't," he said. "Being used."* | 4 words, split across a tag |

**The card says one word and the prose does it with a tense shift on the third. The prose wins, and it wins for a reason worth writing into the card:** only a tense shift moves the question from *history* to *present possession*, which is the entire point — each version drags the material one step closer to his bed (a form → a kitchen table → a drawer he cannot name). **The difference is diagnostic of Vexx, not of her method**, and the chapter proves it structurally: her method never varies (same tone, no pause, and she writes all three *"each under the last, drawing no line between them"*). What changes is the *shape of his answers* — 2 words, 47 words, 4 words. The middle one is long because he is telling the truth and does not yet know it is damning; the outer two are short because one is quoted off a form and the other has nothing behind it. **Recommendation: amend the Dessen card to read "one word or one tense."**

**4. Withholding vs fabricating — the chapter finds the difference, and it finds it in matched prose.** Withheld: *"'I don't remember.' That came out level, easy, a shade ahead of the question — and went down in the book without comment, because it was the truth about a thing he was choosing not to say, and there is no strain in that at all."* Fabricated: *"'I logged an extension.' It was out of him before he had decided anything… And his body knew the difference about a second before his mouth caught up with it."* Then: *"'Against which reference.' / Nothing came."* Two passages, the same syntax, opposite results. This is the chapter's cleanest piece of craft after the pen.

**5. Eight seconds, then the apology — and the apology IS better than the anger.** The anger is genuinely ugly and genuinely unfair (*"somebody who has never in her life had to decide anything in under a minute"*), and it stops *"like a machine stopped by somebody taking the power off it rather than switching it."* The apology is four items, itemised, and it refuses to soften: *"The first part was temper. The second part I chose."* / *"I'd like to say I'll repair it. I can't — there isn't a mechanism. I'm sorry. All four things."* **And the writer's inversion of the outline's beat order is better than the outline.** He arrives, goes off before he has said one useful thing, apologises, and only then does the work — badly discredited in the room and doing it beautifully anyway. What the outline promised was *the apology is better than the anger*; what the chapter delivers is *the competence is better than the apology*, which is a harder shape and a worse man to have to like.

**6. No exit line — verified.** *"…and if it goes in under six hours what you want is your windows shut, everything off the—"* / *"The elevator came. He got into it, still talking, and the doors took the rest of the sentence."*

**7. The REVEAL — verified mechanically and it recontextualises.** Two instances, **byte-identical**, 382 characters each (string comparison, not eye). Second reading given to **Dessen**, at l.254, **~750 words before the end** and inside the audit rather than at the close — which is what stops it repeating Ch.8's re-read ending. The recontextualisation is not *threat → nothing*; it is **threat → permission**. First time it is a charge that could end his career. Second time it is *"Every word of it true. Entered, finished with, filed where nobody would have cause to open it again"* — and the narration immediately shows the reader the object, in a drawer, half a mile east, *"where it would still be tonight."* The finding has become the document that will stop anyone looking. **That is a better second meaning than the outline asked for.**

**8. Reading speed — the acceleration lands at the door.** Verified independently: §5 (*what it cost Corwin*) runs a narration median of **7.0** with **no ≥40-word sentence in it at all** — the tightest passage in the chapter and the only one without a long breath. Then *"The door opened."* (3w) → 14w / 36w / 5w / 6w → seven consecutive sub-nine-word turns. The hook pass's relocation was correct and I would not have found the pre-pass version acceptable: a 50-word sentence about weather laid across the fastest moment in the chapter.

**9. No unlock spent — verified.** Jameson is present in person for ~1,900 words and nothing fires. Rx's near-silence from the moment he enters is a *plant*, costs nothing, and is not flagged by Vexx. Stage 3 is intact for Ch.13.

**10. The shareable moment is on the page and it is one sentence.** See Shareability.

---

## The Tomorrow Test

**What the reader remembers:** a woman writing down a man's apology at exactly the speed she wrote down his insult — *"the only thing in that room, from first to last, that treated the two of them as the same size."* And, second: a man alone in a corridor learning a week of barometric pressure so he will have something to say to his brother's killer.

**Anchor type:** IMAGE ×3 (pen · drawer · the memorised week). No quote-anchor in the strict sense; the strongest single line (*"That isn't a favor, it's Thursday"*) is shareable but not an anchor.
**Verdict: ANCHOR EXISTS.** +0.5 applied to CVI-Launch.

**Cross-chapter anchor-type check:** Ch.9's anchors were an object-with-a-history (the pen-worked logic grid) and a document detail (Ansel/Anseth). Ch.10's are an object-in-motion (the pen writing) and an action (learning the figures). **Related but not repeating** — Ch.9's anchors are things found; Ch.10's are things done. Log it: **the pipeline has now produced four consecutive chapters whose anchor is a small object in an institutional room.** That is not yet repetition, but it is a narrowing, and Ch.11–13 should not make it five.

## The Shareability Test

**What a reader texts a friend:** *"the guy he thinks murdered his brother walks in and saves his career — and MEANS it — and he's grateful, and then he goes and memorises the weather report so he'll have something to talk to him about."* One sentence, no spoilers required, and it is the outline's declared shareable moment landing intact. **This is the strongest shareable moment in the manuscript to date.** Manuscript running total: comfortably past the 3–4 minimum.

---

## Reader Reports

### The Devourer
Stops nowhere before l.200. The summons, the paper notebook and *"That's two sentences, and I've been three weeks on them"* buy the first 800 words; the withheld clerk's name buys the next 400; the triple question is the fastest reading in the chapter. **Skims once, at l.200–232** — the disposition-line dismantling, where the win requires following a legal argument about schedules, remits and property returns. They will pick up again at *"They broke it. He inherited it."* and read the last 900 words without lifting their eyes. They turn the page on dread, not on a question, which for this reader is a slightly weaker pull than Ch.9's.

### The Critic
Fifteen underlines, listed above. Marks the pen sentence as the best sentence in the manuscript since Ch.1 and will read it twice. **Will circle two things**, and both are F2: *"whatsoever"* used twice in a book that had never used it once, and the two *like a man/woman doing a flat professional task* similes eighty lines apart on two different characters. Will also notice, approvingly, that no emotion is named anywhere in 4,588 words, and will notice that Jameson's *"It sits in the second field for the rest of a man's service"* is the most quotable thing the antagonist has said in ten chapters — which is exactly the trap the book is setting.

### The Hostile
Goes to the clock and the procedure first, because that is where a compliance chapter fails. **Finds no hole.** The heating functions as a three-beat clock and never contradicts itself; the summons times reconcile (1020 for 1140); Rx's twenty-two minutes fits; the disposition-line argument is legally coherent (a board struck the material from the evidentiary record three weeks before the release, so what left the lock left as property — the schedule doesn't distinguish, she'd have to argue the distinction, she'd win it, it would take four months, so she doesn't). Their **one probe**: *"had said almost nothing since the audit-room door opened"* against the ~65 words Rx says at l.92. It holds — see the note above — and they will move on. Their **second probe** is F1: they will ask why the narrator keeps telling them these two people are sincere.

### The Casual Reader — **8.5/10, exactly on the gate, and 8.0 is defensible**
They like Dessen inside twenty lines, because of the notebook and because she offers him the bad water. They like Jameson enormously, which is the point and which they will not forgive the book for later. **The vibes are strong and unusual: two competent adults being decent in a small room, and a third one who has done something wrong and knows it.** They do not need to understand the schedule to feel the eight seconds or the apology, and they will feel *"Thank you."*

The two things that hold this at 8.5 rather than 9.0: **(a)** the chapter takes ~800 words of institutional procedure before a live stake appears, which is longer than a casual reader gives a mid-book chapter; **(b)** the l.200–232 dismantling is the only passage in ten chapters where this reader has to *work* to know who is winning. Neither is fixable without breaking something better. **I am recording that this is the second consecutive chapter to meet the Casual gate exactly rather than clear it.** That is a trend the orchestrator should watch even though both chapters pass: a book that meets the canary gate exactly twice running is one skimmable passage from missing it.

### The Devoted Reader (SFF — active)
**Adopts this chapter and will re-read it first.** It is the chapter their subreddit post is about, because it is the chapter that is a *different chapter* the second time: every warm thing Jameson does becomes something else and not one word changes. They will notice Rx's silence from the moment the door opens and will build the timeline of it. They will notice that the finding is quoted twice and is byte-identical, and will diff it themselves. They will notice *"the second field"* and set it beside Ch.10's earlier *"He had read the second field of the form"* and Ch.2's *"personally written the report that buried it"*, and they will be right. They will collect *"That isn't a favor, it's Thursday."*

---

## Cross-Reader Matrix

| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| F2 — twin flat-professional simile + `whatsoever` ×2 | — | **flags** | — | — | **flags** | **SHOULD FIX** |
| F1 — narrator sincerity certification ×6 | — | **flags** | **flags** | — | — | **SHOULD FIX** |
| l.200–232 dismantling is a work passage | **skims** | — | — | **flags** | — | **SHOULD FIX** (but see cost) |
| F3 — Ch.19's concept pre-figured | — | — | — | — | **flags** | INVESTIGATE (carry-forward) |
| Close is a mood-load, not an obligation-load | **flags** | — | — | — | — | INVESTIGATE (deliberate) |
| Rx's *"almost nothing"* | — | — | probes, clears | — | — | NOT A FINDING |

---

## Revision Recommendations (Ranked)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| **F1** | l.190, l.298 (2 of 6 instances) | **Style / Voice** — narrator vouching | Six narration clauses certify Jameson and Dessen as unperforming by denying a performative act and attributing it to a generic person. Author max is 2 per chapter and his are counterweighted; these six are not. | The chapter's design is *"the reader supplies the chill; the scene supplies none."* It must also not supply the **warmth** — *decent* is the one word a reader has to reach unassisted, and the narration reaches it for them six times. The disruptor cut the verdict and left the work. | Cut the interpretive tails of **two**, leaving four (still above the author but inside a defensible band). Cheapest: l.298 *"nothing on his own but the ordinary concern of somebody who has noticed that the person in front of him is having difficulty"* → **"nothing on his own at all"**; l.190 *"pulling one out, turning it, doing none of the small business a man does to make a point of arriving late"* → **"pulling one out, turning it, sitting."** The behaviour stays entirely intact. | **YES** |
| **F2** | l.144 and l.224 | **Style / Voice** — narrator-level device on two characters | *"without any softening on it whatsoever, like a woman reading out a train time"* (Dessen) and *"with no lift on it whatsoever, like a man reporting a figure off a gauge"* (Jameson), 80 lines apart. `whatsoever`: 0 uses in Ch.1–9, 2 in Ch.10. | At the two moments the chapter most needs these characters to be different sizes, the narration renders them with the identical instrument. Cover-the-name cannot see it because both lines are in character; this is STANDING OFFENCE #3's narrator-level diagnosis in a new coat. | **Recast, do not cut** (see cost). l.144 → *"She said this without any softening on it, like a platform announcement."* l.224 → *"Jameson said it with no lift on it at all, like a figure read off a gauge."* Both keep the comparison, move the vehicle from *generic person performing a task* to *object/event*, and remove one `whatsoever`. | **YES** |
| **F3** | l.162, Jameson | **Continuity / series** | *"It sits in the second field for the rest of a man's service, every board that ever opens him reads it first."* | Ch.19's payoff is Corwin's *"They don't kill you. They file you."* This is the same concept — the file as the instrument of institutional harm — nine chapters early, in a more articulate mouth. It clears the gate condition and clears `voice-dna.md` §4 (which bans the **narration** making the connection, not a character), but it narrows Corwin's gap. | **No Ch.10 edit.** Carry the note into the Ch.19 brief so Corwin's line is written against a reader who has already met the idea — his version must be about *people*, not careers, and must be shorter and worse-spoken than Jameson's. | **YES** (carry-forward) |
| **F4** | l.290 | **Prose** (minor, **RECOMMEND NOT ACTIONING**) | *"…the same as it had been in a briefing room two levels below anything with a name on the door, the first time a man he had never met said his brother's name out loud and got the weight of it right."* The second clause recaps Ch.2's event for the reader. | The location alone is sufficient: a reader who remembers Ch.2 gets everything; one who does not gets a physical fact they do not need glossed. | **Do not action — the arithmetic blocks it.** Cutting the clause takes a 48w sentence to 28w and drops it out of the ≥40w bucket: **17/115 = 14.8% → 16/115 = 13.9%, against a floor of 13.0.** 0.9pp of margin on a floor is writing to the gate. Published so the next pass does not re-derive it. | No |
| **F5** | close, l.246–323 | **Momentum** (**recorded, NOT for repair**) | The chapter's live obligation (*"You'll get a property return notice inside a fortnight" / "People say that."*) lands at the 85% mark; the final 650 words renew no obligation and close on mood. | It is the reason Momentum is 8.5 rather than 9.0, and it is also the correct artistic choice — the brief forbids converting the moral pull into a plot hook and the hook pass declined to, rightly. | **No edit.** Recorded so the editor does not chase it and so the orchestrator can see exactly what the half-point is. | No |
| **F6** | l.200–232 | **Pacing** (**cost-blocked, logged**) | ~500 words in which the reader must follow schedules, remits, disposition lines and property returns to know who is winning. The only work passage in the manuscript. | The Devourer skims it and the Casual Reader flags it; it is what holds Casual at 8.5 rather than 9.0. | **Any repair here costs a gated metric.** The section's narration median is already 9.5 (the second-tightest in the chapter) and shortening further pushes `≤6w` toward the 30.0% ceiling from 27.8%. A *human image* inside the argument would be word-neutral and is the only safe move — but it is the passage where Jameson is most purely competent, and that is the point of him. **Logged, not ordered.** | No |

### Fix order: F1 → F2 → (F3 carried) → (F4/F5/F6 logged, not actioned)

**Total metric cost of F1 + F2, computed:**
```
F1: -33 narration words. Narration 2,392 -> 2,359.
    Neither cut clause contains `and`, so narration `and` /1k rises 18.39 -> 18.65.
    Author band 18.19-18.90. STILL IN BAND, mid.  ✓
    l.298 is 65w; -20w leaves it at 45w, still in the >=40w bucket. 14.8% unchanged. ✓
    l.190's sentence is already <40w. No bucket change. Median 17.0 (floor 14.0 /
    ceiling 18.0) can only fall, and has 3.0 points of room. ✓
F2: -4 words. Comparison count UNCHANGED at 10 -> 2.19/1k against a FLOOR of 2.0. ✓
    (A cut rather than a recast would take it to 8 = 1.74/1k and BREACH the floor.
    This is why the direction is "recast, do not cut.")
    l.224's paragraph opens with a quotation mark and is classified as dialogue by the
    splitter, so it touches no narration breath metric at all. ✓
    l.144: 17w -> 12w. Median can shift by at most 1, from 17.0 to 16.0. ✓
Every other gated band: untouched. Em-dash 10.46 unchanged. Semicolons 0. `?` count 5.
```

---

## Strengths to PRESERVE

1. **The pen writing the apology at the speed of the insult.** The chapter's anchor, its thesis, and its stopping sentence, carried entirely by an object with zero intensity-words in it. Nothing may be added to it or taken from it.
2. **The fifth scene break (*what it cost Corwin*).** Not in the outline; it is the chapter's value shift and the reason the rescue is a bad thing to be grateful for. Narration median 7.0, no long sentence, the tightest and best-paced passage in the manuscript. **Protected.**
3. **The disruptor's two words — *"Thank you."*** The chapter's stated emotional surprise executed as a leak rather than a description. No narration, no reflection, nobody notices. Do not gloss it, ever.
4. **Zero retrospective-narrator intrusions.** The book's defining voice move is absent from this chapter *because using it would break the gate condition.* This is structural intelligence and must not be "restored."
5. **The imprecision at l.278** (*"since the audit-room door opened"*). Load-bearing vagueness — sharpening it to *"since Jameson came in"* would make Vexx notice something suspicious. Do not fix.
6. **Dessen's finding stands.** She is right, she concedes only what she has checked herself, and the recommendation — not the finding — is what falls. Any future compression that lets Jameson win outright destroys the chapter.
7. **The barometer, twice, landing on nobody**, and the exit taken mid-clause by a lift door.
8. **The three-answer shape of the triple question** — 2 words / 47 words / 4 words. The arithmetic is the diagnosis.

---

## Cross-Chapter Pattern Detection (Ch.1–10)

| Axis | Finding |
|---|---|
| **Opening structure** | Ten distinct openings. Ch.10 opens on a fragment of time-and-place (mandated); Ch.9 opened on unattributed dialogue. No convergence. |
| **Closing shape** | Ten distinct shapes, verified against the writer's ledger and independently spot-checked. Ch.10's — *an unremarked act of preparation for the antagonist* — is genuinely new; its nearest neighbour is Ch.9 and the separating axis is motive (Ch.9 is a refused method executed; Ch.10 is an unrequested kindness rehearsed). |
| **Emotional rendering** | **The strongest convergence in the manuscript, and it is §THE FLAT-MAN.** Feeling is displaced onto objects (correct, it is the voice) *and* affectlessness is rendered via generic-person manner attribution in four of five pipeline chapters at 0.69–0.89/1k against an author who reaches 0.67 once in five. **Plateaued, not rising — which is worse.** |
| **Simile architecture** | Clean. Zero explanatory extensions in Ch.10; broad Pattern #11 at 1.09/1k is below the author's minimum. The Ch.6→Ch.9 gloss habit is closed and stayed closed. |
| **Dialogue pattern** | Ch.10 is the messiest chapter in the book (7 interruptions/broken turns) and the highest dialogue ratio. No convergence. |
| **Character introduction** | Dessen is introduced through a paper notebook, a pen and a refusal to perform — not through competence cascade. Distinct from Goliath (Ch.2, presence), Zeus (Ch.2, stillness), Merrick (Ch.8, symptom), Corwin (Ch.3, correction). |
| **Anchor type** | **Narrowing, logged.** Four consecutive chapters anchor on a small object in an institutional room (the requisition, the re-read document, the pen-worked grid, the notebook-and-pen). Not yet repetition. Ch.11–13 should not make it five. |
| **Narrator certification** | **NEW in Ch.10.** §THE VOUCH-BY-NEGATION: 0 instances in Ch.6–9, 6 in Ch.10. Chapter-local so far. |

---

## RETRACTIONS AND CLOSURES — findings of previous evaluations, tested against this chapter

**RETRACTION 1 (not mine — the Ch.9 evaluation's, and it does not survive).** Ch.9 §THE SEAM logged a hypothesis: *"The chapter's rule-of-three cadence runs at roughly 3.0/1k, which is elevated… The mechanism may be the conversion itself — merging short sentences into em-dashed appositive catalogues is a triad factory. I flag this as a hypothesis, explicitly, because it is not testable on the surviving artifacts."*

**It is testable on Ch.10, which had its own breath conversion (five splits), and the hypothesis is NOT SUPPORTED.**
```
metric:            triad proxy — "A, B, and C" tails (a comma within 70 chars before ", and")
                   plus asyndetic three-item runs of short noun phrases; whole text, per 1k.
author benchmark:  Ch.1 5.70 · Ch.2 4.56 · Ch.3 6.00 · Ch.4 4.63 · Ch.5 5.83 → 4.56–6.00
this chapter:      5.67/1k  → INSIDE the author's range, near his median
pipeline:          Ch.6 7.09 · Ch.7 9.22 · Ch.8 7.72 · Ch.9 5.37 · Ch.10 5.67
```
Ch.9 (5.37) and Ch.10 (5.67) are the two lowest pipeline chapters and both are inside the author's band; the two highest (Ch.7, Ch.6) had *no* conversion. **Splitting is not a triad factory. The hypothesis is retired.**

**CLOSURE 1 — §THE HINGE stays closed.** The `, which` gloss in narration: Ch.6 0.78 → Ch.7 0.00 → Ch.8 0.83 → Ch.9 0.57 → **Ch.10 0.00** (paragraph splitter) / **0.38** (span splitter). Two chapters inside the author's band since the gate was added. The gate works and its ceiling of 1.0 is correctly placed on both definitions.

**CLOSURE 2 — the narration `and` finding is answered.** Predicted to fire from Ch.10; Ch.10 posts 18.39 against a band of 18.19–18.90, reversing a four-chapter monotonic rise and landing on his median. **And the floor did the work the ceiling could not** — the writer reports the conversion overshot to 16.9, under the author's own minimum, and four conjunctions were deliberately put back. Both ends of the band earned their keep in one chapter.

**CLOSURE 3 — §THE QUESTION MARK is answered.** 0.00 → 1.09/1k, inside the author's band, and the unmarked form is legible as technique again because it now tracks whether the speaker is on the record.

**CLOSURE 4 — numeric density.** Inside the author's range under the definition that generated the warning; 1.07× his maximum under the writer's tighter one. Gateable at 16.0 on Def C. **See §THE DEFINITION HAZARD — this closure comes with a live warning attached.**

**CORRECTION 1 — to the brief I was given, not to a previous evaluation.** The brief compares Ch.10's *whole-chapter* `and` (17.7) to the author's *narration* band (18.2–18.9), which makes a compliant chapter look 0.5 points under his floor. Measured like for like, narration is 18.39 and in band. The Ch.9 evaluation retracted itself for this exact error mode two days ago; it has already recurred, in a brief written after the retraction. **That is worth more than the correction: a documented failure mode reappearing immediately in a downstream document means it needs to be a template line, not a lesson.** Recommend the Writer/Evaluator brief template carry a fixed field: `metric | register measured | author band for THAT register`.

**CORRECTION 2 — to `character-bible.md` §STANDING OFFENCES row 3.** The row records *"Ch.10 (Jameson)"* as a breach. It was found and removed at dialogue-polish; **the finished chapter is clean and the surviving `twice a year / both times` is Dessen's and load-bearing.** The row should read *"Ch.10 (Jameson) — CAUGHT AND FIXED PRE-GATE."* The diagnosis in that row is confirmed a fourth time: four chapters, four different mouths, and the predicted pairs held every time.

**One of my own findings I decline to make, with the arithmetic published.** I measured Ch.10's whole-text `, which` at 1.09/1k against the author's whole-text maximum of 0.53 — 2.1×, and my first instinct was a finding. Four of the five are Jameson's, whose card licenses the explanatory register in terms. **Gating a character's licensed device is the mistake `style_check.py`'s own comments warn about three separate times.** Reported, not found. If a future pass measures 2.1× and reaches for it, the reasoning is here.

---

## PATH TO 9.0 on the two dimensions I would most like to move
*(PATH TO 8.5 is not owed — the floor is 8.5. This is offered because the average, 8.64, is the lowest of the passing chapters and the two lifts are cheap and specified.)*

- **Prose & Voice 8.5 → 9.0 requires exactly F1 + F2 and nothing else.** Two clause-cuts and two simile recasts, all four costed above, none of which touches a gated band. The chapter already has the citable close-the-book sentence; what holds it at 8.5 is that an editor would circle two sentences on the same page as the best sentence in the manuscript. Remove those two circles and the number moves. **The exact surgery is in the F1 and F2 rows; do not substitute a different repair, because the comparison floor and the ≥40w floor between them block every alternative I tested.**
- **Momentum 8.5 → 9.0 requires nothing to be written and one thing to be decided.** The half-point is (a) placement — the live obligation at 85%, the last 650 words carrying mood — and (b) F3. **(a) is a deliberate artistic choice the brief mandates and I am not asking for it back.** If the orchestrator judges that a mood-load close is a full-strength close for this book, Momentum is 9.0 and the average is 8.71, level with Ch.1 and Ch.9. **That is a judgement above my pay grade and I have published both numbers so it can be made without re-deriving my analysis.**

---

## VERDICT

**PASS.** Genesis Floor **8.5** · Genesis Average **8.64** · Casual Reader **8.5** · CVI-Launch **9.0** · CVI-Legacy **6.6**.

Both gate conditions are met. **One of them is met exactly and I want that visible rather than buried: Casual Reader 8.5 is the least robust number on this page, 8.0 is defensible, and this is the second consecutive chapter to meet the canary gate exactly rather than clear it.** The two things that hold it there (the 800-word procedural runway and the l.200–232 dismantling) are both cost-blocked, which means the margin cannot be bought back cheaply and the next chapter should be built with more of it.

**The book's central Jameson scene does the thing it was built to do.** He is warm, he is right, he is rude and then sorry about it, he saves a man's career on a public document any competent officer could have found, he gets no exit line, and he is not given one sentence that Vexx could ever replay and hear differently. The chill is entirely the reader's and the scene supplies none of it. The one adjacent failure the disruptor correctly named — the narrator vouching — survives in six instances that wear behaviour's clothes, and that is this chapter's revision work, not its gate.

**And the mechanical state is the best in the pipeline's five chapters, on my own measurements and not the writer's:** narration `and` on the author's median, breath inside a band that is closed at both ends, Pattern #11 below his minimum, zero emotion words, zero metacognition, zero flash-forwards, zero retrospective intrusions, zero `as if`, zero `the particular`, zero `the way X`, zero semicolons, zero tidying gestures, zero hands-flat, and the two gates that were open a chapter ago both closed.

---

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose, and the brief told me three prior passes had already cleared the one condition the chapter must be judged on — which stacks confirmation bias on top of authorship bias. Countermeasures applied, and stated so they can be audited:

- **Every number in this document was computed by me**, in one run, on `style_check.py`'s own `words()`, `sentences()` and `split_registers()`, with all ten chapters measured by the identical instrument. I did not carry forward a single figure from the writer report, the dialogue pass, the hook pass, the disruption report, or the brief. Where my numbers differ from theirs (narration `and` 18.39 vs 18.49; numeric 15.04 vs 14.3) I report both and the difference is tokenizer handling, not disagreement.
- **The gate condition was audited independently and adversarially**, all 23 turns read twice, and I tested three lines no prior pass named — including one (F3) that I am recording as a cost even though it clears.
- **The Pattern #11 arithmetic that would fail this chapter is published in full again**, and is shown to fail the locked Ch.1 harder than it fails Ch.10.
- **Every numeric recommendation in this document carries the four required lines**, and I ran the benchmark check *before* stating the threshold in every case. **One of my own findings died in that check and I am reporting the death rather than the finding**: my first measurement of §THE VOUCH-BY-NEGATION returned author 0.00 across all five chapters and Ch.10 at 1.71/1k — an infinite multiple, and a very attractive number. It was wrong. The regex named `people do` and not `men bring`, and the author's own Ch.2 contains *"none of the small props men bring into a room where they expect to be weighed"* — the construction, in the benchmark, in the introduction of a major character. Corrected, the author's per-chapter maximum is **2** and the honest multiple is ~3×, not ∞. **The finding survives in a smaller and more defensible form, and the threshold I ended up proposing (flag at ≥3) is one the benchmark passes; the threshold my first measurement implied (flag at ≥1) would have put the author's own Ch.2 in breach.** That is the eleven-point failure in miniature and I committed it in the first ten minutes of measuring.
- **I found a second instance of the same failure mode sitting live in this project's committed documents** (§THE DEFINITION HAZARD) and a third in the brief I was handed (CORRECTION 1). All three have the identical shape: a metric computed one way, compared to a band derived another way.
- **A previous evaluation's live hypothesis is retired** on a measurement it could not run and this chapter could (RETRACTION 1).
- **I declined a finding I wanted** (whole-text `, which` at 2.1× the author) and published the arithmetic for it anyway.

Three temptations interrogated. **(1) The temptation to find the gate condition broken, because "a chapter that reads well is exactly where a gate condition failure would hide" is an invitation to manufacture one** — rejected; I could not construct a reading in which any extra meaning is available to Jameson rather than to the reader, and I have published the sharpened test so my reasoning can be attacked. **(2) The temptation to hold Momentum at 9.0 to match Ch.9 and keep the average at 8.71** — rejected, and both reasons for the 8.5 are published with the note that I would not fight hard for it. **(3) The temptation to inflate Prose to 9.0 because the chapter's best sentence is the best in the manuscript** — rejected; two sentences on the same page are the kind an editor circles, and the anti-inflation rule does not care that the neighbours are excellent.

Confidence in any score above 8.0 requires external validation — beta readers, an editor, comp analysis. **The number I would defend hardest is Emotion 9.0, because it rests on four anchors and a zero-emotion-word count anyone can grep. The number I am least sure of is Casual Reader 8.5, which sits exactly on the gate for the second chapter running and which I would not fight anyone over. The number that should worry the orchestrator most is not a score: it is §THE FLAT-MAN at 0.87/1k in the fourth of five pipeline chapters, flat rather than rising, ungated, invisible to every existing instrument, and — unlike every previous fingerprint this project has caught — not a habit the pipeline is drifting into, but one it has already settled in.**
