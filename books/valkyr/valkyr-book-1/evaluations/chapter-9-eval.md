# Evaluation: Chapter 9 — 0200
**Evaluator:** book-evaluator | **Date:** 2026-09-10
**Scope:** 3,380 words (`style_check` counter) / 3,480 prose-body words incl. italic interface / 2,005 words of narration after quote-stripping. Two scenes, one break.
**Dimension 7:** Momentum / Series Engine (carried from Ch.6, Ch.7, Ch.8).
**Anti-AI posture:** FULLY LIVE. Genre band: Commercial Fiction (as settled in Ch.6–8).
**Benchmarks:** Ch.1 (LOCKED) Floor 8.5 / Prose 9.0 / Avg 8.71 · Ch.6 8.5 / 8.79 · Ch.7 8.5 / 8.79 · Ch.8 8.5 / 8.79.
**Two-register dialogue convention:** verified correct throughout. **CLOSED IN WRITING AT CH.8. NOT RE-OPENED. NOT A FINDING.**

---

## HEADLINE

**CVI-Launch:** 8.8 | **CVI-Legacy (chapter proxy):** 6.6 | **Genesis Floor:** 8.0 | **Genesis Average:** 8.64
**Engagement Type:** Fascination (primary — the offer, and the moral complexity of the man making it) · Empathy (secondary — Zeus and Aglaope, not Vexx) · Intellectual (tertiary). **This is a shift from Ch.8's Empathy-primary and it is the right engine for this chapter.**
**Verdict: POLISH.** Floor 8.0 (Pacing & Coherence). Casual Reader 8.5.

**Divergence Alert — YES, and it is the shape of the chapter.** CVI-Launch 8.8 vs Genesis Floor 8.0 is a 0.8 gap; Genesis Average 8.64 vs Floor 8.0 is a 0.64 gap. **Single-dimension weakness — Pacing & Coherence is the bottleneck, and it is held down by a countable defect, not by a craft limitation.** Six of seven dimensions sit at 8.5–9.0. The floor is a stopped clock (F1) that three word-level edits repair.

---

## THE FINDING OF THIS EVALUATION, STATED FIRST

**§THE HINGE — the pipeline's Pattern #11 fingerprint has a name, a shape, a number, and no gate. It is the trailing `, which …` clause in narration, and Ch.9 is the manuscript maximum.**

| narration `, which` /1k | Ch.1 | Ch.2 | Ch.3 | Ch.4 | Ch.5 | **Author range** | Ch.6 | Ch.7 | Ch.8 | **Ch.9** |
|---|---|---|---|---|---|---|---|---|---|---|
| instances | 0 | 1 | 0 | 1 | 1 | **3 in 13,651 narr words** | 6 | 4 | 12 | **7** |
| per 1k narration | 0.00 | 0.25 | 0.00 | 0.48 | 0.80 | **0.00–0.80 (mean 0.22)** | 2.00 | 2.60 | 2.93 | **3.49** |

Four pipeline chapters. **Monotonically rising, every chapter, without exception.** Ch.9 runs the construction at **4.4× the author's measured maximum and 16× his mean**. Pooled: pipeline 29 instances in 10,647 narration words (2.72/1k) against the author's 3 in 13,651 (0.22/1k) — **a 12× divergence, the largest this project has measured.** For scale: §THE SEAM's `and` divergence was 1.9×; the simile floor was 2.3×; `somebody`/`nobody` was 1.8×.

Why this matters more than the number:

1. **The Ch.7 and Ch.8 evaluations both declined to apply the Pattern #11 cap on the ground that "the threshold detects the author, not the pipeline," measuring Ch.1 at 4.68/1k explanatory extension. I now believe that measurement was taken on a definition broad enough to sweep in `voice-dna.md` §1.2(b) — the author's own *naming-the-technique* move, which he renders with an em-dash or a fresh sentence.** On the narrow, mechanically countable form — the comma-plus-`which` gloss bolted to the tail of an image — the direction reverses completely and cleanly. The author almost never does it. The pipeline always does, and does it more each chapter.
2. **The disruptor pass named this exact construction, by name, in this exact chapter** — *"the same fingerprint in its other clothes: the trailing appositive `, which …` clause that tells the reader what the image they just read means"* — **cut two, declared the pattern addressed, and did not count the rest. Seven remain.** A pass that identifies the fingerprint correctly and then stops at two instances is worse than one that misses it, because it produces a written record saying the pattern was handled.
3. **No gate counts it.** `style_check.py` has been improved four times by four evaluations (simile floor, `and` register split, `vague_per1k` re-derivation, breath block) and every one of those improvements was a metric the evaluator could name. This one is a two-character regex.

Ch.9's seven, in full, so the fix is executable without re-deriving anything:

> *"…which is what two hours in a chair will do to a man."* · *"…which he took for a fault in his own query until the third time."* · *"…which did nothing whatever to the cup."* · *"…which he had not done all night."* · *"…which was that she reads the last twenty back every night."* · *"…which had gone cold in the time it took him not to say them."* · *"…which is most of what a man would need."*

Four of the seven are true glosses (1st, 3rd, 6th, 7th). Two are narrative continuation (2nd, 4th). One is syntactic necessity (5th). Cutting to the author's ceiling means removing **three**, and the three cheapest are the 1st, 3rd and 7th. **Pipeline fix, root, per the UPDATE RULE: add `which_gloss_per1k` to `PIPELINE_CEILINGS` at 0.80** — the author's measured maximum, per `style_check.py`'s own calibration rule #2 ("set the threshold AT the author's measured extreme"), measured on quote-stripped narration only.

**Second finding, smaller but cleaner: §THE QUESTION MARK.** Ch.9 contains **zero question marks in 3,480 words** — in the chapter with the highest dialogue ratio in the manuscript (1.68:1) and eleven direct spoken interrogatives across all four speakers.

| `?` /1k | Ch.1 | Ch.2 | Ch.3 | Ch.4 | Ch.5 | **Author** | Ch.6 | Ch.7 | Ch.8 | **Ch.9** |
|---|---|---|---|---|---|---|---|---|---|---|
| | 0.10 | 2.19 | 2.90 | 2.02 | 1.01 | **1.01–2.90** (Ch.1 excl., all-memory) | 0.89 | 0.65 | 1.02 | **0.00** |

`voice-dna.md` §1.3 lists *"The unanswered question, WITHOUT QUESTION MARKS"* as one of **four PRESSURE behaviours** — a break that fires *at maximum load*. The author punctuates ordinary spoken questions normally, including one- and two-word ones (*"Options?"*, *"Ready?"*, *"He got a name?"*, *"Spector confirm?"*). Ch.9 applies the pressure form to *every question by every character*, including *"Do you know the cook's name."* and *"How's it ordered."* **A device that fires on everything marks nothing.** When Aglaope's Ch.23 seed arrives — *"What happens to him if you're wrong. And what happens to him if you're right."* — it is punctuated identically to a question about a cook, and the punctuation channel that was supposed to make it land as pressure has been spent thirty times before it gets there.

There is a real counter-argument and I record it: the outline requires that line be **dropped unflagged**, and uniform punctuation is one way to keep it unflagged. I do not think it survives, because the cost is book-wide and the benefit is one line: this is chapter 9 of 26, and the pressure channel has to work seventeen more times. **Recommendation: restore question marks to ordinary spoken questions and reserve the bare form for load.** Ch.9 needs roughly six restored (Zeus's cook, the bund, *"Did he do it"*, Vexx's *"How's it ordered"*, *"What happened"*, Rx's *"Did you know that"*) and should keep the bare form on *"Why."*, on Vexx's *"How long does it take. Finding out what a man's protecting."* and on Aglaope's Rx line — which then land as what they are.

Both findings share one shape, and it is the same shape as Ch.8's syntactic-uniformity finding: **the pipeline generalises a distinctive device into house style, one register below where the watch-list is looking.** Ch.8 found it in clause-joining. Ch.9 finds it in subordination and in punctuation. The watch-lists guard vocabulary and gesture wording; the drift keeps happening in grammar.

---

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|---|---|---|---|
| Originality | **8.5** | Two moves I cannot name a precedent for. **(a) A corruption offer whose entire reassurance is about the victim's welfare** — *"There's no mark on him. There's nothing on paper anywhere in the building… He goes home. He tells nobody. He'll be at that same desk for the rest of his service, perfectly all right."* A tempter reassures the buyer; this one reassures nobody and describes the clerk's untroubled future as the selling point, which is what makes it obscene. **(b) Aglaope's argument against sorting a casualty list alphabetically** — *"Ansel took an hour and forty minutes longer. I was there for all of it. If I put those two side by side on a list, that hour and forty minutes stops existing. It only exists because they're nine pages apart."* A data-structure argument that is a moral argument, arrived at through a comedy about sub-sorting. Also structural: the temptation's payoff (Zeus's relief) is relocated thirty lines past the refusal into a conversation about coffee, and the corruption is relocated a hundred lines past the offer into a solitary paragraph where nobody is offering anything. | Not 9.0: the *compromised ally makes the dark offer* is one of the genre's oldest scenes, and everything original here is execution-level — consistent with Ch.6, Ch.7 and Ch.8, and now four chapters running. Zeus's Sedge backstory (the board that used all seven of his interviews and found against him) is a familiar institutional shape rescued by one line, not by its design. |
| Theme | **9.0** | The outline says *"the chapter is the theme; stated nowhere."* It is stated nowhere, verified: no line in 3,380 words asks or answers *what are you willing to become.* Instead it arrives three times in three different rooms and one of them is not about Vexx at all. **Zeus:** *"If I start it again I lose Tuesday and Wednesday." / "You've lost them anyway." / "Not while I'm still on it."* — the theme as *what are you willing to keep being.* **Aglaope, displaced onto a clerical decision:** *"if he's on it, then what I do is sit with people. And if he isn't, then what I do is something else, and I've been doing it for eleven years."* **Vexx, in the closing paragraph, without a word of commentary.** And the book gives the devil the strongest line — *"perfectly all right"* is the counter-argument, unanswered. Organic texture is heavy and thematically inert: the guitar peg, the night-urn cook Beattie, the coffee bracket, the laminated card wrong about paging for four years, Zeus being left-handed, the dog at Ridgeway, the boat Curran was buying. | Not 9.5: one narratorial nudge points at the closing paragraph — *"He had got that far before he stopped."* It is a superb sentence and it is also the one place the chapter tells the reader that something has just happened. The theme survives it; 9.5 would not have needed it. |
| Characters | **8.5** | **Chaos 4/4, inhabited.** Irrelevant thought: *SOLID ASH. 1600 BY 800. DELIVERY FOUR TO SIX WEEKS.* dropped into the exact middle of the offer, unattributed, uncommented, never returned to. Unprompted memory: *"There was a dog at the depot at Ridgeway that had learned to lift the gate latch with its nose."* — arriving during Aglaope's eleven years, connected to nothing. Cognitive distortion, in behaviour and unnamed: *"Twice it returned the same seven lines in a different order, which he took for a fault in his own query"* — he attributes the system's behaviour to his own error, and then spends 104 minutes on an index he already knows is closed. Failed management: *"He took hold of it again a second later and did not let go."* **Three secondaries with independent interior lives, none of them functioning as a protagonist tool:** Zeus (the puzzle, Sedge, the note he has answered nine times, the fluorescent that would not settle), Aglaope (Curran, the middle years, two entries counted twice), Rx (Zeus is left-handed; the card has been wrong four years; *somebody laminated it*). **And the observation neither pass made: Vexx's dialogue register changes with his interlocutor.** With Zeus he is monosyllabic — *"Hallam." / "No." / "Don't." / "I know."* With Aglaope he is fluent and will not shut up — a 70-word manifest speech he cannot stop delivering. Same man, two registers, no narration about it. | Not 9.0, three cited reasons. **(a) My own strict cover-the-name rate is ~57 %** — I ran it independently and land where the dialogue pass did; twelve of Vexx's ~30 turns are identifiable cold. I judge this the form and not a defect (see §Cover-the-Name), but a 57 % cast is not a 9.0 cast. **(b) Gesture-grammar convergence:** three characters perform the same physical grammar — adjusting a small object on a table in place of speaking — in one chapter (§Gesture). **(c) The shared question punctuation** (§THE QUESTION MARK) removes one channel of syntactic differentiation from all four voices simultaneously. |
| Prose & Voice | **8.5** | Thirteen citable underline sentences in 2,005 words of narration and 161 dialogue lines. The **stopping sentence**, and it is nine words of clerical procedure carrying a nine-year wound: ***"I read it four times to see whether there were two documents."*** Runners: *"Zeus had not asked what he was doing — had not asked anything at all — and had not left."* · *"Less, if he has children."* · *"Zeus nodded once, at the grid in front of him rather than at Vexx."* · *"He was still sitting when Vexx went out — four bays lit, five dark, a cup he was not going to drink, a puzzle he could not finish and would not start again."* · *"I know you know. I'd rather have said it than found out later that I hadn't."* · *"and the swing door did what that door does — twice, then once more, smaller."* Voice under pressure to `voice-dna.md` §1.3 exactly: after *"Don't."* the interiority switches off and the prose reports physical facts in sequence for a full paragraph. Zero `felt`, `feel`, `realise`, `as if`/`as though`, `the particular`, zero emotional-temperature reports, zero metacognition, zero semicolons. Ugly sentence present and working: *"The urn coffee at that hour is not coffee. He had two cups of it."* Simile 2.7/1k — **the first pipeline chapter back inside the author's 2.5–6.4 band; Ch.8's F3 is CLOSED.** | **Drop from Ch.7/Ch.8's 9.0, with four cited regressions.** (1) **§THE HINGE** — narration `, which` at 3.49/1k, manuscript maximum, 4.4× the author's ceiling. (2) **Pattern #17 collapse** — one interrupted line in 161 dialogue lines against Ch.8's nine in 162, in the chapter with the most dialogue in the book (§Pattern 17). (3) **Numeric density 27.9 → 39.4/1k**, 1.8× the author's maximum, narration precision at ~6.3/1k against Ch.8's 5.1. (4) **The gnomic twin** — the deliberate ugly sentence's construction (*"The urn coffee at that hour is not coffee"*) is reused as the chapter's penultimate sentence (*"The mess at four in the morning is a room with the chairs still down"*), which dilutes the first and costs the close its freshness. **Pattern #11 arithmetic published in full below, three readings, including one that fails the chapter.** |
| Pacing & Coherence | **8.0** | Value shift large and moral rather than situational: he enters believing he can do this lawfully and leaves knowing he cannot, holding a method he refused and has already begun to run. Reading speed genuinely designed, not merely slow — the offer decelerates into two unbroken instructional paragraphs, then *"No,"* / *"No,"* as two-word paragraphs, then the table-edge beat; scene 2 accelerates into a four-word comic volley (*"Four hundred." / "It was an example." / "A full stop."*) and is killed by the Ansel/Anseth deceleration. **The comedy-into-devastation turn is the best pacing move in the manuscript.** Structural variety intact: ninth chapter, ninth shape; two two-handers with one hard cut, no graduated reveal, closes flat on a light switch. Narration histogram in band on all three gated metrics (median 14.5 / ≥40w 14.6 % / ≤6w 21.9 %). | **F1 — the chapter has a stopped clock, and it is the only reason this dimension is not 8.5.** Vexx arrives *"at ten past one"*; the narration says *"nothing else for two hours"* (→03:10) and the chapter's second sentence says *"two hours in a chair"*; Zeus then asks four more questions *"over the next half hour"* (→03:40); the same paragraph's last sentence says *"At two in the morning."* Zeus later states the badge log at *"a hundred and four minutes"* (01:10 + 1:44 = 02:54). **Minimum stated elapsed time is 150 minutes against a stated log of 104 — a 46-minute contradiction, in narration as well as dialogue, in a chapter titled `0200` that runs numerals at 39.4/1k.** Four passes and three gates missed it. Secondary: no chapter-end hook, by design and correctly, but scene-end pull is 1 of 2 by my count. |
| Emotion | **9.0** | Anchor lands exactly as the outline specifies and is unmistakable: **a logic grid worked in pen, row four wrong since Wednesday, and a man who will not start it again because starting again costs him Tuesday.** Second anchor in scene 2 (Ansel/Anseth, nine pages apart). Emotional surprise ×4, all of them the wrong emotion in the right place: the offer delivered in the guitar-peg voice; *"Less, if he has children"* with no adverb and no intensifier; the relief arriving after the refusal instead of the temptation; a comedy about database indexing that turns into the worst thing anyone says. **Body rebel ×3, all unmanaged:** *"It came out ahead of anything he would have called a decision, like a hand coming off a hot pan."* · *"Vexx heard himself say:"* · *"He took hold of it again a second later and did not let go."* Six-plus techniques (object displacement, silence-as-duration, humour-under-dread, catalogue-instead-of-feeling, dialogue subtext, involuntary physical action). | Not 9.5: (a) the POV character carries almost none of the emotional load again — his own beat is four words of hand — which is the same cost Ch.8 paid and is now a two-chapter pattern rather than a design choice; (b) two small narratorial confirmations where inference should carry: *"His shoulders had come down off wherever they had been"* supplies a before-state Vexx never observed, and *"and the silence lasted exactly as long as that did"* measures the pause after Aglaope's Ch.23 seed (F3). |
| Momentum / Series Engine | **9.0** | Two forward loads and both are sharper than the question the chapter closes. **(a) The badge log, planted as a courtesy rather than a threat** — *"It logs that a badge asked it something for a hundred and four minutes at two in the morning. That goes up on Monday with the water and the lights." / "I know." / "I know you know. I'd rather have said it than found out later that I hadn't."* The institutional threat arrives as the most considerate line in the chapter, which is a better Ch.10 seed than any warning would have been. **(b) The method is now in Vexx's head and firing without permission** — the closing paragraph is Zeus's tradecraft running in Vexx's own procedural register, forty minutes after two refusals, and it ends on *"with the door standing open"*, verbatim from the offer. Also loaded and correctly unspent: Zeus's puzzle (Ch.15, Ch.22), Aglaope's Rx line (Ch.23), Curran left on the list (Ch.16/23), Merrick's notebook read three times and brought down unopened. Spends nothing forbidden — no Jameson, no unlock stage, no rampancy, no calendar date, no Rx interiority, no RECLAMATION. | Not 9.5: nothing in the plot moves, which is the brief, but it means momentum is entirely moral and the chapter has no second load for a reader who does not feel the closing paragraph. And Zeus's discretion is *asserted* (he did not report it) rather than tested — the one thing the chapter could have made frightening and did not. |
| **FLOOR** | **8.0** | Pacing & Coherence | |
| **AVERAGE** | **8.64** | | |

**Trajectory: Ch.1 8.5 / 8.71 (locked) → Ch.6 8.5 / 8.79 → Ch.7 8.5 / 8.79 → Ch.8 8.5 / 8.79 → Ch.9 8.0 / 8.64.**

First floor break in the pipeline chapters, and I want to be precise about what it is and is not. It is **not** a quality regression across the board: Theme, Emotion and Momentum all hold 9.0, and the chapter contains the best stopping sentence since Ch.7 and the best pacing move in the manuscript. It is **one countable defect in one dimension**, plus a Prose drop from 9.0 to 8.5 that I have justified with four measurements rather than an impression. Fixing F1 restores the floor to 8.5 and the average to ~8.71 for the cost of three word-level edits. That is the cheapest 0.5 available anywhere in this project.

I have also interrogated whether I am breaking a three-chapter 8.5/8.79 streak in order to look independent. The test I applied: would I have scored Ch.8 at 8.0 for the same defect? Ch.8's F1 (eleven people on the apron) was a *headcount* the reader assembles across three sentences; Ch.9's is a *duration* contradicted inside one paragraph, in a chapter named after a clock time, restated four times. It is a bigger error in a more visible place. I would not have dropped Ch.8 for its version and I do drop Ch.9 for this one, and I am satisfied that is a measurement rather than a mood.

---

## §THE SEAM — Ch.9's conversion, measured, and the scar named

The brief asks for the final measurement and whether the 60 %-mark conversion left a scar. **It did, and it is not where anyone was looking.**

The whole-chapter figure is compliant: `and` **21.9/1k** against a ceiling of 24.0. But `and` has to be read split, and the gate's own paragraph-open splitter puts embedded dialogue into the narration bucket, so I measured it a second way — stripping every quoted and italic run and measuring the remainder — and report both.

| `and` /1k (quote-stripped) | Ch.1 | Ch.2 | Ch.3 | Ch.4 | Ch.5 | **Author range** | Ch.6 | Ch.7 | Ch.8 | **Ch.9** |
|---|---|---|---|---|---|---|---|---|---|---|
| **Narration** | **21.6** | 19.6 | 20.0 | 13.7 | 17.4 | **13.7–21.6** | 19.8 | 19.8 | 22.0 | **21.5 ✓** |
| **Dialogue** | — | 13.8 | 13.0 | **21.0** | 11.9 | **11.9–21.0** | 28.2 ✗ | 8.6 | 23.9 ✗ | **21.0 ✓** |
| **Register sum** | 21.6 | 33.4 | 33.0 | 34.7 | 29.3 | **29.3–34.7** | 48.0 ✗ | 28.4 | 45.9 ✗ | **42.5 ✗** |

**Both registers are inside the author's range. Both are sitting on his ceiling to one decimal place** — narration 21.5 against his maximum of 21.6, dialogue 21.0 against his maximum of 21.0.

That is the scar, and it is a real one. **The author trades.** When his narration chains at maximum (Ch.1, 21.6) his dialogue is at 16.5; when his dialogue chains at maximum (Ch.4, 21.0) his narration is at 13.7. He never runs both registers hot at once — his register sum ranges 29.3–34.7 and never exceeds 34.7. Ch.9 posts **42.5**, which is 7.8 above his maximum. The conversion did not leave a stylistic seam anyone can hear in a sentence; it left the chapter with **no counter-balance and no margin**, sitting on the ceiling in both registers simultaneously, which is a state no chapter of the author's is in.

Two consequences, one good and one not:

- **F4 from the Ch.8 evaluation — the dialogue-side chaining breach — is CLOSED.** Ch.6 28.2, Ch.8 23.9, **Ch.9 21.0**, the first pipeline chapter back inside the author's dialogue band. The writer's decision to measure dialogue separately and leave it alone was the right one and it worked.
- **Register sum is the metric this project has been missing.** It is the only number that shows the trend honestly — 48.0 → 45.9 → 42.5, improving monotonically and still out of band — and it cannot be gamed by moving the habit from one register to the other, which is exactly what happened between Ch.8 and Ch.9. **Pipeline fix: report `and` narration + dialogue as a sum, ceiling 34.7** (the author's measured extreme, per calibration rule #2). The current 24.0 whole-chapter ceiling sits 5 points above the author's narration maximum and cannot see either half.

**One secondary scar, noted without alarm.** The chapter's rule-of-three cadence runs at roughly 3.0/1k (§Pattern 3), which is elevated against Ch.8's ~0.5. The mechanism may be the conversion itself — merging short sentences into em-dashed appositive catalogues is a triad factory. **I flag this as a hypothesis, explicitly, because it is not testable on the surviving artifacts** (the conversion happened at the 57–60 % mark of the draft with nothing saved before it). **Recommendation: the next chapter that has to make a large `and`-conversion should save its pre-conversion draft**, so the hypothesis can be tested once rather than guessed at four times.

---

## Anti-AI Scan (20 patterns) — density on 3,380 words

| # | Pattern | Verdict | Density | Citation / reasoning |
|---|---|---|---|---|
| 1 | Forced symmetry | **FOUND — deliberate, half weight** | 1 frame | The chapter opens on an unattributed line about Paladin's guitar peg and Aglaope's exit line closes it — *"Tell Paladin about the peg. He thinks it's him."* One frame, earned, and the narrator points at neither. |
| 2 | Empty poetic vocabulary | **CLEAR** | 0 | Nine comparisons, every one physical/domestic/soldiering. No abstractions. |
| 3 | Automatic rule of three | **FOUND — moderate** | ~3.0/1k (≈10) | *"the item field empty, then the date range wide, then the date range narrow"* · *"a two-letter code, a subsection under that, a duty roster under that"* · *"You sit down. You let him understand… You never say…"* · *"came on, and it ran, and it stopped"* · *"a dent in a tag, two dates one under the other, a date read out twice"* · *"two, then two, then two"*. Elevated 6× against Ch.8. **Partial mitigation and it is real:** roughly half break the pattern on the third element (*"depot, no answer — depot, no answer — depot, called back, will send a man"*), and the chapter's best cadence is a deliberate anti-three: *"twice, then once more, smaller."* See §THE SEAM for the suspected mechanism. |
| 4 | Excessive em dashes | **CLEAR** | 9.8/1k (33) | Inside the author's 9.0–11.8 band, above the 8.5 floor, under the 12.0 ceiling. Narration-only figure is 12.0/1k against an author narration range of 7.8–12.0 — at the ceiling, same story as §THE SEAM, recorded not actioned. |
| 5 | Empty metaphors | **CLEAR** | 2.7/1k, all bare | Nine comparisons, **none extended, none explained**. *"like a shop closing up in reverse"* · *"like elastic out of a cuff"* · *"like a hand coming off a hot pan"* · *"like a man reporting a fault on a vehicle he means to go on driving"* · *"like a wire somewhere inside a wall"*. **First pipeline chapter back inside the author's simile band. Ch.8's F3 is closed.** |
| 6 | Dramatic "And" openings | **CLEAR** | 0 in narration | Four in dialogue, all speech rhythm. |
| 7 | Pseudo-philosophical closing | **CLEAR** | 0 | Closes on *"turned the strip light off over the servery, and went up."* Fourth consecutive chapter clear. |
| 8 | Excessive parallelism | **FOUND — moderate** | ~1.2/1k | *"What happens to him if you're wrong… And what happens to him if you're right."* (the anchor, deliberate) · *"if he's on it, then what I do is… And if he isn't, then what I do is…"* · *"Leave was harder. Leave is held on the section sheet and the section sheet does not travel."* All three are load-bearing; the last is Vexx's procedural mind on the page. |
| 9 | Overly smooth transitions | **CLEAR — inverted** | 0 | One hard cut, no mediation, and the bridge is carried by a character rather than a narrator. Within-scene, the furniture listing detonates in the middle of the offer with no join on either side. |
| 10 | Described emotions | **CLEAR** | **0** | Zero `felt` / `feel` / `realise`. Closest approach is a negation — *"No heat in it, no embarrassment either"* — which names emotions in order to rule them out. |
| 11 | **Explanatory Extension** | **FOUND — see the three readings below** | **4 clear / 1.18 per 1k (broad)** · **7 / 3.49 per 1k narration (narrow — §THE HINGE)** | Clear (broad): *"which is what two hours in a chair will do to a man"* · *"the way a unit knows a thing it has agreed not to make a subject of"* · *"the way you leave a thing for whoever comes in after you"* · *"sitting the way she sat in rooms she meant to leave soon."* |
| 12 | Binary Negation Opener | **FOUND — moderate, half weight on two** | ~1.2/1k (4) | *"That's not caution. That's a man rationing himself"* and *"It's the water. Not the grounds."* are **Zeus's bible-registered device** and are half-weighted. *"The urn coffee at that hour is not coffee"* is the declared ugly sentence. *"Merrick's in you. He isn't this."* is Aglaope's — negation without substitution, which is the correct repair of Standing Offence #2 and is verified clean. |
| 13 | Precision Flex | **FOUND — strong** | **39.4/1k gross · ~6.3/1k narration precision choices** | 1.8× the author's whole-chapter maximum (10.1–21.8), manuscript's second-highest after Ch.7's records search, and the narration figure is worse than Ch.8's 5.1. **The disruptor declined Precision Deflation entirely on the ground that "every number here is load-bearing." Most are; the aggregate is not.** Protect absolutely: *"a hundred and four minutes"* (the Ch.10 seed), *"two hundred and nine" / "two hundred and eleven"*, *"an hour and forty minutes"*, *"nine pages apart"*, *"Seven interviews… all seven… Same seven interviews"*, *"I read it four times."* The flags are texture-precision: *"a quarter out from it"*, *"one boot up on the crossbar"*, *"banks of two… two, then two, then two"*, *"about two seconds"*, *"about thirty degrees"*, *"four seconds"*. And it has produced a coherence failure (F1) — the third consecutive chapter in which a precision habit has generated one. |
| 14 | Emotional Control Demonstration | **CLEAR — inverted** | 0 | Three control failures, none recovered: Vexx's hand going back to the table edge and staying; Zeus's cup-turn and the badly-timed *"I'd have been sorry if you'd taken it"*; Aglaope revealing she has been sitting undecided since half past two. **Nobody in this chapter notices an emotion and successfully manages it.** The disruptor's single addition is what makes this true and it was the right edit. |
| 15 | Authoritative Description | **FOUND — minor, half weight** | ~0.6/1k | *"The records annex sat against the outer wall on the north side of the operations block, where the ducting had been costed twice and run neither time — the coldest room in the building, by a margin everybody knew about and nobody had put on a form."* Encyclopedic institutional confidence, and it is `voice-dna.md` §1.2(b) working as specified. The closing paragraph asserts how a base accommodation office at Kell operates, from a man who has never been there — cleared on thirty years of ONI service, and it is the point of the paragraph. |
| 16 | Philosophical Asides | **FOUND — moderate** | ~1.2/1k narration (4) | *"which is what two hours in a chair will do to a man"* · *"The urn coffee at that hour is not coffee."* · *"The mess at four in the morning is a room with the chairs still down."* · *"the way you leave a thing for whoever comes in after you."* **The finding is not the count, it is the repetition of the frame.** Two of them share an identical construction — [definite noun phrase] + [time adverbial] + *is* + [flat predicate] — and they sit at the opening and the close of scene 2. One is the declared ugly sentence; the other is the chapter's penultimate sentence. Having the same shape in both spends the ugliness of the first and costs the close its surprise. See F5. |
| 17 | Clean Dialogue | **FOUND — moderate. THE MANUSCRIPT'S WORST RESULT, in the chapter with the most dialogue.** | **1 interruption in 161 dialogue lines (0.6 %)** vs Ch.8's **9 in 162 (5.6 %)** — a 9× regression | The single break is *"or it'll take you—"*, and it is an interruption *by Aglaope*, not a false start. **Zero false starts. Zero cross-talk. Zero self-corrections. Zero trailing off.** Two exhausted people at four in the morning speak in complete, terminated sentences for 1,568 words. **The disruptor explicitly declined Dialogue Mess (#8), and its reasoning is where the error is:** it cited *"How's it ordered." / "In order." / "Chronological." / "That's what in order means."* as evidence the dialogue is "already the least orderly thing in it." That is **non-responsiveness**, not disorder — semantically evasive turns that are prosodically immaculate. They are different properties and the pass substituted one for the other. Ch.9 has the highest non-responsiveness in the manuscript and the lowest prosodic mess. |
| 18 | Thematic Echo Chamber | **CLEAR** | ~30 % pure texture | The guitar peg and the fourth string; Beattie the night-urn cook; the coffee bracket argument; the col versus the ridge; Gaia's acoustics story; the laminated card wrong about paging for four years; Zeus being left-handed; the boat Curran was buying; the dog at Ridgeway; *SOLID ASH. 1600 BY 800.* None of it resonates with anything. |
| 19 | Graduated Reveal | **CLEAR** | 0 | Two two-handers, one hard cut, closes flat on a light switch and a staircase. Ninth chapter, ninth shape. |
| 20 | Emotional Temperature Report | **CLEAR** | **0** | Zero. Fifth consecutive chapter. |

**Total: 9/20 found. Commercial Fiction band: WATCH (9–11), at the bottom of it.** Ch.6 9 → Ch.7 8 → Ch.8 11 → **Ch.9 9.**

Three of the nine fire at half weight or are explicitly deliberate (#1, #12, #15). **Five of the six deep structural tells are CLEAR (#7, #10, #14, #18, #20) — and #17, the sixth, is the one that regressed, badly, in the chapter that had the most room to get it right.** The three that matter are #11, #13 and #17, and all three are in the findings table.

**Standing caveat on the band, recorded because it has never been re-examined and it decides a category.** This book's prose ambition is literary; its shelf is genre. Ch.6–8 settled on the Commercial Fiction band (0–8 clean / 9–11 watch / 12+ fingerprint). On a Literary Fiction reading (0–3 clean / 7+ fingerprint) every pipeline chapter including this one scores as **AI FINGERPRINT**. I keep the Commercial band for continuity with three prior evaluations and I do not think the choice is wrong, but it is doing more work than any single dimension score and the orchestrator should know it is a choice.

### ⚠️ Pattern #11 — the arithmetic in full, three readings, and which I applied

The V3.4 hard check: *Commercial Fiction: >6 instances **OR** >0.8/1k → cap Prose at 7.5.* The density clause disapplies below 2,500 words. **Ch.9 is 3,380 words, so both thresholds are live as written and the length-artefact escape is not available.**

```
READING (A) — V3.4 as written, broad definition (explanatory extension of any shape)
  Ch.9 clear instances ............ 4          threshold >6        → not breached
  Ch.9 density .................... 1.18/1k    threshold >0.8/1k   → BREACHED
  Strict mechanical consequence ... Prose 7.5 → Genesis Floor 7.5 → FAIL

READING (B) — the Ch.7/Ch.8 amendment (threshold = the author benchmark), broad definition
  Ch.1 (LOCKED, author) ........... ~4.68/1k   (measurement carried from Ch.8 eval)
  Ch.9 ............................ 1.18/1k    = 25 % of benchmark → PASS comfortably

READING (C) — the same amendment, NARROW definition (§THE HINGE, trailing ", which" gloss)
  Author Ch.1-5 ................... 0.00-0.80/1k narration, mean 0.22
  Ch.9 ............................ 3.49/1k narration        → BREACHED, 4.4x benchmark
```

**Which I applied: none of the caps. Prose scored 8.5, with §THE HINGE cited as one of four reasons it is not 9.0.**

Reasoning, published so the orchestrator can overrule me. Reading (A) fails the chapter, and applied consistently it also fails the author's locked Ch.1, so there is no version of it under which Ch.9 fails and Ch.1 passes — the same conclusion Ch.7 and Ch.8 reached and I confirm it. Reading (B) is the amendment those evaluations recommended, and **I now think it was operationalised on the wrong definition**: the broad measure sweeps in `voice-dna.md` §1.2(b), the author's genuine signature, and therefore exonerates the pipeline by measuring the author's voice as the pipeline's fingerprint. Reading (C) is the same amendment done correctly, and it **breaches** — which is the honest result and the one that produced this evaluation's headline finding.

I do not cap on (C) either, for one reason and it is not a soft one: **four clear glosses in 3,380 words is not prose that reads as machine-explained.** The chapter's images overwhelmingly stand raw — the cup, the pen, the four bays lit and five dark, the swing door, the hand on the table edge, the furniture listing. A 7.5 cap would describe a chapter that does not exist. But (C) is the correct instrument going forward, it is implementable as a two-character regex, and **it should gate Ch.10 rather than be re-litigated at Ch.10.**

---

## Character Chaos Check — Vexx (primary)

| Marker | Verdict | Evidence |
|---|---|---|
| Irrelevant thought | **PRESENT — inhabited ×2** | *SOLID ASH. 1600 BY 800. DELIVERY FOUR TO SIX WEEKS.* — its own paragraph, in the exact middle of the offer, no attribution, no frame, no return. A callback to Ch.7's furniture listings that nothing in the narration connects. And *"There was a dog at the depot at Ridgeway that had learned to lift the gate latch with its nose — every man on the gate fed it, and not one of them would admit to it."* — arriving in the gap after Aglaope says *"I've been doing it for eleven years."* |
| Cognitive distortion | **PRESENT — in behaviour, unnamed** | *"Twice it returned the same seven lines in a different order, which he took for a fault in his own query until the third time."* He reads the system's behaviour as his own error. And structurally: 104 minutes of queries against an index he has already established is closed to him, with a notebook by his elbow he brought down and did not open. **Weaker than Ch.8's, which produced an operational consequence; this one produces only a wasted night.** |
| Unprompted memory | **PRESENT — inhabited** | The Ridgeway dog. Connected to nothing before or after. |
| Failed emotional management | **PRESENT — four words** | *"He took hold of it again a second later and did not let go."* The disruptor's one addition, and the chapter's only evidence that the refusal cost him anything. No gloss, no reflection, Zeus does not notice, the next line is the lights going out on their timer. |
| Voice under pressure | **DEMONSTRATED — to spec** | After *"Don't." / "All right."*: the paragraph is physical facts in sequence — takes hold, holds, boots pass, stops, does not come back, lets go, takes hold again — with zero interiority. `voice-dna.md` §1.3's primary break executed exactly. Also the flat two-word paragraph: *"'No,' Vexx said."* |

**4/4, inhabited, not mediated.** Commercial Fiction requires 2–3/4. Clears the literary bar, in the mode that unlocks 8.5+. The cognitive-distortion marker is the weakest of the four and the writer report papers over that by relabelling the correction reflex as "cognitive habit in action" — the correction reflex is a compulsion, not a distortion, and the two should not be traded in the report.

---

## Secondary Character Chaos

| Character | Verdict |
|---|---|
| **Zeus** | **Own life, extensively.** The logic grid in pen he has been on since Tuesday. Row four wrong since Wednesday and he will not restart it. Sedge: *"Seven interviews, every one of them mine… then found against me on the last page for what it called an unsound approach to the subjects."* The note he answers at the new year, nine times. *"There was a room at Sedge with a fluorescent in it that wouldn't settle. Two years. Still doing it, I expect."* — arriving unbidden the moment he is thanked, explaining nothing, per his card. |
| **Aglaope** | **Own life.** Two entries counted twice. The middle years she has started getting out of order. Curran, the man who lived, whom she has been sitting up since half past two deciding whether to delete. *"If he's on it, then what I do is sit with people."* Responsibility inflation, straight off her card, and it is the chapter's quietest devastation. |
| **Rx** | **Own moment, small and correct.** Two hours of silent irritation about a man's handwriting and a laminated card, delivered as a complaint about furniture the instant Vexx asks about his silence. He was in the room for the whole offer. He says nothing about it and nobody makes him. |

**No secondary character functions only as a protagonist tool. No cap.**

### Rx's *"Fine."* — smooth, single, at cap, and Ch.13 is safe

*"You've been quiet since I sat down." / **Fine**, Rx said. Then, at his ordinary speed: He's left-handed…"*

**Smooth: YES, verified.** It answers a statement that was not a question, arrives before an honest answer could be assembled, and the only narration attached is *"Then, at his ordinary speed"* — which makes the speed legible by implication and never uses the at-risk *too quick* wording. Nobody notices it. This is the device working exactly as the bible describes.

**Cap status: 5 of 5 smooth firings spent (Ch.1 ×1, Ch.3 ×3, Ch.9 ×1), verified by grep, matching the bible's corrected count and not the writer report's.**

**Does Ch.13 still have what it needs? YES, and the dialogue pass's §8.1 escalation is already resolved.** The pass flags this as *"the highest-priority item in this report"* and asks for an author decision before Ch.13. `character-bible.md`'s RX entry, corrected 2026-09-10, already answers it in writing: *"The cap counts SMOOTH firings only… The Ch.13 break is the device failing, not firing… It does not count against the cap."* Ch.13 needs no budget because a broken tic is not the tic. **Recorded as CLOSED so the orchestrator does not spend an author decision on it.** Structurally the placement is also right: three chapters clustered in Ch.1–3, a six-chapter gap, one clean re-establishment at Ch.9, then the break four chapters later. That is the correct spacing for a reflex the reader has to recognise before it fails.

---

## Device Bleed — audited independently, including gesture

I ran every speaker against every reserved device rather than taking the dialogue pass's table on trust. Its ten edits are sound and I confirm all ten. Three things it did not find:

**(a) THE GESTURE GRAMMAR — three characters, one chapter, and it is not the wording the watch-list guards.**

`character-bible.md` §STANDING OFFENCES #5 records the tidying gesture as a ten-instance, five-character bleed and records Ch.9's Aglaope instance as fixed. **It was. Ch.9 nonetheless contains four object-adjustment beats across two characters, plus two on a third:**

| Line | Character | Text | Status |
|---|---|---|---|
| 94 | Zeus | *"reached over and turned the cup a half-turn on the table, which did nothing whatever to the cup"* | Owner. Licensed. |
| 100 | Zeus | *"Zeus went on turning the cup."* | Owner, same beat. Licensed. |
| 122 | Zeus | *"Zeus turned the sheet a little to take the lamp off the glare."* | Functional. Cleared. |
| **226** | **Vexx** | ***"He turned his cup on the table."*** | **The finding.** |
| 162 / 208 | Aglaope | *"she did not turn the pad over"* → *"She turned the pad face-down at last"* | A deliberate before/after pair on the scene's central object. Good craft. Cleared. |

Line 226 is Vexx performing Zeus's registered gesture, on the same object type, with the same verb, 132 lines later, **for the same reason** — the narration gives Zeus's cup-turn as displacement (*"which did nothing whatever to the cup"*) and gives Vexx's as an answer he will not make. Same grammar, same function, two characters, one chapter.

**Mitigation, and it is genuine: the author did this himself.** Ch.5, line 79: *"He turned her cold cup a quarter turn on the table and left it where it was."* Vexx, in an Aglaope scene, immediately after declining to say the whole truth — which is precisely the Ch.9 beat. Ch.9's instance is a deliberate rhyme with the author's own scene, and the author's precedent grandfathers it.

**So I do NOT apply the shared-device cap on Characters, and I show the arithmetic:** as written, my rubric caps Characters at 7.5 when two characters share a device; on the bible's own grandfathering principle (*"that is his prose and it is not being rewritten to satisfy a map"*) the Vexx instance is licensed and no cap applies. I record it as a WATCH, not a fix, and I make the pipeline recommendation below because the *class* of error is what matters.

**The pipeline finding underneath it: the watch-list guards gesture WORDING and the convergence is in gesture GRAMMAR.** *Squaring an object to the edge* is a phrase; *adjusting a small object on a table in place of speaking* is a grammar, and the second is what the reader absorbs. Ch.9 has three characters performing emotional evasion through tableware. Nobody will notice in one chapter. By Ch.16 it will be the only thing this cast does with its hands. **Recommendation: rewrite §STANDING OFFENCE #5 to name the grammar rather than the wording, and add a per-chapter ceiling of two object-adjustment beats across the whole cast.**

**(b) The spoken N-of-the-M residual, and a rule that was quietly narrowed to fit a line.**

§STANDING OFFENCE #3 reads: *"Only Spector counts ALOUD (**the N-of-the-M construction included**)."* The dialogue pass's Z02 edit removed a *restatement* — *"Two of them sign retention exceptions, which means two of them can…"* → *"…which means they can…"* — and then wrote: *"The bleed here is not the numbers — it is the restatement."* **That is the rule being narrowed by the pass whose job is to enforce it.** What stands is *"Eleven people. Two of them sign retention exceptions,"* which is the N-of-the-M construction, spoken aloud, by a character who is not Spector. Aglaope also runs one — *"Two hundred and nine… I've had two of them on twice."*

**I would keep both lines.** Zeus's is how an intelligence officer describes an office and the numbers are the offer's whole credibility; Aglaope's is her chaos marker and the outline's mandated beat. But **the rule and the practice now disagree in writing**, and that is exactly how a §STANDING OFFENCE is created — a distinctive constraint rounded off toward the ordinary by the pass enforcing it, with a written justification attached. **Fix the rule, not the lines:** narrow §3 formally to *the performed sequence and the restated count*, and record that a single spoken cardinality is not bleed.

**(c) Aggregate, which nobody audited.** All four speakers in this chapter quantify: Zeus (nineteen numeric tokens), Vexx (narration and dialogue), Aglaope (the list), Rx (*"about thirty degrees"*, *"wrong four years"*). Each instance was cleared individually and correctly. In aggregate, in a chapter running numerals at 39.4/1k, the reservation of counting to one absent character is not holding — not because any line is wrong, but because the *habit* is now cast-wide. This is the same aggregate blindness as (a): the audit runs per-instance and the convergence is per-chapter.

**Confirmed clean, checked myself:**
- **Zeus never asks why. CONFIRMED, independently.** `why` occurs once in the chapter (line 124) and it is Vexx's. I read all seven of Zeus's questions and the four reported ones as candidate why-questions in other clothes: *the cook's name* (who), *what did you tell the commander about the bund* (what-was-said), *did he do it* (yes/no), *col or ridge* (which), *where Gaia learned the acoustics thing* (where, about a third party), *who won the coffee-bracket argument* (who), *whether Vexx ever owned a dog* (yes/no). **Nothing remains, in speech, in reported speech, or in narration.** The Z01 repair of the Ch.8-and-Ch.9 offence holds. He also never asks what Vexx is looking for, what the record is, or what he intends to do with it — three questions the scene begs for, all absent. And when Vexx asks *him*: *"Why." / "Ask a different question."*
- **The private tally / spoken count carve-out: NOT CROSSED.** Vexx's counting is narration only — *"Nine bays of shelving, of which four held anything"*, *"a materiel record in twenty-two lines, of which he had seven"*, *"four bays lit, five dark."* Never spoken. Canon. (One small note: the *N X, of which M* frame fires twice within thirty lines, plus a third variant at the scene close. Three uses of one syntactic frame in one scene is worth thinning by one — F6.)
- **Aglaope does not use *"That's not X. That's Y"*.** A01's repair holds: *"Merrick's in you. He isn't this."* is negation without substitution, which is her axis.
- **Zeus's *"That's not X. That's Y"* fires exactly twice** (*caution/rationing*, *water/grounds*), which the dialogue pass correctly calls the ceiling. Confirmed at two.

---

## THE BRIEF'S FIVE QUESTIONS, ANSWERED PLAINLY

### 1. Does the beat subversion land? Does Zeus read as tempting?

**It lands. He does not read as tempting, and the mechanism is one nobody in the pass reports named.**

The strongest evidence is not the relief, the peg-voice, or the absence of a clock. It is this: **every reassurance in the offer is about the victim, and there is not one about the buyer.**

> *"There's no mark on him. There's nothing on paper anywhere in the building. He doesn't report it… He goes home. He tells nobody. He'll be at that same desk for the rest of his service, perfectly all right."*

A tempter reassures the person he is tempting — *nobody will trace it to you, you'll have it by Wednesday, this is how everyone does it.* Zeus never once says any of that. He does not tell Vexx he will be safe, or that it will work, or that he deserves the record. **The entire comfort content of the speech is directed at a man neither of them has met.** That is structurally impossible to read as a pitch, and it is why the scene survives being 350 words of tradecraft delivered to a man who says four words.

Supporting evidence, verified: he has been in the room two hours and does not raise it — *Vexx's* activity raises it. He never asks why, so he cannot be shaping an appeal to Vexx's motive. He volunteers the worst fact in the chapter unprompted (*"Less, if he has children."*), which no seller does. He does not argue, restate, or leave a door open after the refusal. He puts no clock on it. And *"I'd have been sorry if you'd taken it"* arrives **badly** — into the middle of a conversation about coffee, thirty seconds after a pointless cup-turn — which is what makes it credible.

**Is the *test* reading available to a first-time reader?** Yes, at the level the chapter needs: they get the relief and the line, which is enough to feel that he wanted the answer *no*. They do not get the motive, which is correct — that belongs to Ch.22.

**One risk I want on the record and it is the chapter's largest.** Vexx says *"Zeus."* — an interruption, a request to stop — and Zeus **continues for another 220 words.** A reader who hears *"Zeus."* as *stop* will read the continuation as the one moment he overrides a friend. The scene is saved by a distinction it makes and never explains: he does not stop at a **flinch** (*"Zeus."*) and stops instantly at an **instruction** (*"Don't." / "All right."*). That is a good and defensible characterisation and I judge it on the right side of the line. It is also the single place where a hostile reading of him is available, and it is worth knowing that it rests on one word.

**Does the narration ever confirm he is doing something?** Twice, and one of them should go.

- *"He said all of it at one speed, unhurried, like a man giving directions to a road he drives every week."* — **Keep.** This rules a reading *out* (no relish, no hurry) rather than supplying one, and after 350 words of instruction the reader needs it.
- ***"His shoulders had come down off wherever they had been."*** — **This is the one.** *Off wherever they had been* retroactively supplies a before-state that Vexx never observed and the reader was never shown. It is the narrator confirming the relief exists rather than letting the cup-turn and *"I'd have been sorry"* deliver it — and those two do deliver it, completely. See F4.

### 2. Is Vexx's refusal noble?

**No, and the text earns the alternative without stating it.** Three pieces, none of them glossed:

1. The refusal arrives **before** the decision: *"It came out ahead of anything he would have called a decision, like a hand coming off a hot pan."* A reflex is not a virtue.
2. He then **keeps asking**: *"How long does it take. Finding out what a man's protecting."* A man who had refused on principle does not need the timings. He gets the answer, and it is *"Less, if he has children"*, and he has to say *"Don't."* — which is aimed at himself, and the text never says so.
3. The closing paragraph: he runs the method unbidden, in his own register, forty minutes and two refusals later, and lands on *"with the door standing open"* — verbatim from the offer he turned down.

**Verdict: earned, unstated, and the closing paragraph is the proof.** The one small cost is that the narration does say *"He had got that far before he stopped"*, which points at the moment. It is the best sentence in the paragraph and I would not cut it; I record it as the reason Theme is 9.0 and not 9.5.

### 3. Is Aglaope's Rx line dropped and abandoned?

**Almost. Nine words flag it.**

> *"What happens to him if you're wrong," she said. "And what happens to him if you're right."*
> *The heater under the servery came on, and it ran, and it stopped, **and the silence lasted exactly as long as that did**.*
> *"Tell Paladin about the peg," Aglaope said, standing, taking both cups.*

No character responds. No interiority registers it. She exits on a guitar peg. All of that is right, and the heater is an inspired choice because the chapter established it 180 lines earlier with **no** weight attached: *"The heater at the far end came on, ran a while, went off again."*

**The trailing clause is the flag.** The first heater is not measured. The second is, and measuring the silence is the narrator saying *note this pause.* The counter-argument is real and I weighed it — converting a loaded silence into an appliance cycle is deflationary, and the clause is what performs the conversion. I do not think it survives, because the deflation is already complete without it: *came on, and it ran, and it stopped* is three flat verbs about a heater, and adding *the silence lasted exactly as long as that did* re-inflates by naming the silence the reader was supposed to feel and not be told about. **Cut nine words** (F3). Metric consequence: −1 `and` in narration (helps §THE SEAM), −10 words, sentence 23 → 13 words, no band crossed.

### 4. Reading speed — does the quiet earn itself?

**Yes, and it is not merely slow — it is engineered.** The chapter has five measurable gears: the annex establishment (long accumulating sentences, median high); the four-question run (compressed to a single reported sentence, which is the chapter's one acceleration in scene 1); the offer (two unbroken instructional paragraphs, the chapter's floor for reading speed); the refusal (two-word paragraphs); and scene 2's comic volley (*"Four hundred." / "It was an example." / "A full stop."*) killed by the Ansel/Anseth deceleration.

**The comedy-into-devastation turn is the best pacing move in the manuscript** and it is built correctly: the writer report notes the outline's order was swapped so the comedy dies *before* Curran is raised, and that swap is why the honest question is not played for warmth.

**I do not score the quiet as a defect.** I do score two skim windows (§Casual) and one absent scene-end pull (scene 2 is the chapter close and closes flat by design; scene 1's pull is a question-plant and works).

### 5. The single scene break — does it carry?

**Yes, and it carries on a character rather than a narrator, which is the right choice.** Location arrives in the first clause (*"The mess had the urn off and one strip light burning over the servery"*), time arrives two lines later (*"It's been off since one"*), and the bridge is spoken: *"You came up from the annex."*

**One structural echo at the join, and there is a fix nobody proposed.** The dialogue pass's §6 correctly flags that Aglaope's *"You came up from the annex"* shares its surface form with Zeus's scene-opening *"You came down here with a notebook you haven't opened"* — the chapter's only join is carried by the same device that opened the scene before it. The pass declares both repairs worse than the problem, and it is right about the two it tested. **A third exists: reorder her first two lines.** Open her on *"There's an inch left in the urn. It's been off since one, so it's an inch of something else now,"* and let *"You came up from the annex"* land second, after he has poured it. The observation still fires, the device is still hers, and the scene no longer opens on the same shape the last one did. Cost: two lines swapped. Metric: neutral. See F7.

### 6. The declared shareable moment — landing or buried?

**Half-landed, and it is the one outline item this chapter does not deliver.**

The outline names *"the interrogator who never asks why."* The absence is made legible three times — *"Zeus had not asked what he was doing — had not asked anything at all — and had not left"*; the run of four irrelevant questions; *"Why." / "Ask a different question."* — and that is good work. But a reader can only formulate *the interrogator who never asks why* as a **rule** after watching it fail to happen repeatedly, and Ch.9 gives them one chapter. What is shareable here is a **line** (*"Ask a different question"*) and a **concept the reader has not yet been given enough evidence to name.**

The fix must not state the rule; stating it kills it. **It should be given to Rx**, who has been in the room for two hours cataloguing irrelevancies and complaining about handwriting. One italic sentence in his block, delivered as a grievance rather than an insight, would make the absence visible without a narrator confirming anything and without Zeus gaining a gram of design. See PATH TO 8.5.

---

## Cover-the-Name — run independently

I stripped all 161 dialogue lines and 5 interface turns of tag, beat and turn-order and read them cold against the full twenty-voice cast. **My strict rate lands at roughly 57 %, which is within noise of the dialogue pass's 58.9 %.** I confirm its single remaining INDISTINCT (Vexx's *"I know."* at line 136, colliding with Zeus's ninety lines earlier) and I agree with leaving it, because fixing it destroys *"I know you know. I'd rather have said it than found out later that I hadn't."*

**Is 57 % a defect or the form? The form — and I want to say why the metric is the wrong instrument here rather than just excusing the number.**

In a two-hander, alternation assigns every turn, so the writer is free to use four-word turns that carry no identity and are not *supposed* to. Thirty-one of the weak turns are four words or shorter. Lengthening them to survive isolation would be writing to the metric and would destroy the only thing the chapter is for.

**The right test for a two-hander is different, and I ran it: take a ten-line block at random and identify which of the two scenes it comes from.** Ch.9 passes decisively. Scene 1 is questions that do not want answers and second-person conditionals; scene 2 is an argument in which every turn is the other person's word held up to the light. And the strongest single result in the chapter is one neither pass reported:

**Vexx's dialogue register changes with his interlocutor.** With Zeus: *"Hallam." / "So I hear." / "No." / "Don't." / "I know."* — monosyllables, twelve turns under four words. With Aglaope: a 70-word manifest speech he cannot stop delivering, escalating past two clear stop signals, including *"And when it's over four hundred you'll want it grouped by year inside the letter, or it'll take you—"*. Same man, two registers, and the narration does not remark on it once. That is a harder thing to do than making every line identifiable in isolation, and it is worth more.

**Clean passes on strict:** Zeus (wrong-order questions, never repeats, never asks why, the registered reframe ×2). Aglaope (*"That's what in order means."* · *"It's an argument for me checking."* · the Ansel/Anseth speech · *"Merrick's in you. He isn't this."*). Rx (all three turns — the speed, the demoted vocabulary, the complaint about a laminated card). **Confirmed weak and correctly so:** Vexx's procedural monosyllables, which are the author's own practice.

---

## The Tomorrow Test

**What the reader remembers:**
1. **A logic-grid puzzle worked in pen, row four wrong since Wednesday, and a man who will not start it again because starting again costs him Tuesday.** [IMAGE + QUOTE] — the outline's declared anchor, delivered intact.
2. ***"Less, if he has children."*** [QUOTE] — four words, no adverb, said kindly, by the most considerate person in the chapter.
3. ***"I read it four times to see whether there were two documents."*** [QUOTE] — nine years of institutional injury delivered as a filing action.
4. ***"It only exists because they're nine pages apart."*** [QUOTE] — probable rather than confident; it needs its 100-word run-up to land, which makes it harder to carry away.

**Anchor type: BOTH, quote-weighted (1 image, 3 quote).** This is a shift — Ch.8's anchor set was image-weighted. Worth tracking: three consecutive quote-heavy chapters would mean the book's memorable moments are migrating into dialogue, which is a different book.

**Verdict: ANCHOR EXISTS — the strongest quote set in the manuscript.** +0.5 to CVI-Launch.

## The Shareability Test

**What a reader texts a friend:** *"there's a scene where a guy very kindly explains how to blackmail a records clerk and the worst line in it is 'less, if he has children'"* — that is one sentence, it survives retelling, and it is the best shareable in the pipeline chapters so far. Second: *"someone argues you shouldn't alphabetise a list of the dead because it would put two men next to each other who died an hour and forty minutes apart."*

**Manuscript running total: 4–5 shareable moments across nine chapters.** Above the 3–4 threshold. The VIBES PROBLEM flag raised provisionally at Ch.7 can be lowered.

---

## Reader Reports

### The Devourer
Reads the offer scene at full speed and does not breathe from *"If you were going to do this"* to *"No."* Skims two places: the 130-word annex/index paragraph on page 1 (*"He had tried the item field empty, then the date range wide, then the date range narrow"*) and the manifest escalation in scene 2 (lines 186–206). Both recover. **Stops nowhere.** Would be irritated only that nothing happens — and would then find themselves quoting a line about children to somebody at work.

### The Critic
Underlines eleven sentences. Marks *"Zeus nodded once, at the grid in front of him rather than at Vexx"* as the most economical piece of characterisation in the book. Notes that a chapter which is thematically *what are you willing to become* never says any part of that sentence, and gives it credit. Marks two things down: **the gnomic twin** (*"The urn coffee at that hour is not coffee"* / *"The mess at four in the morning is a room with the chairs still down"* — the same construction opening and closing the same scene) and **the trailing `, which` habit**, which they will not be able to name but will feel as the narrator explaining images that did not need it.

### The Hostile
Goes straight to the clock and finds it inside ninety seconds. *"Two hours in a chair"* on page one; *"nothing else for two hours"* four paragraphs later; *"over the next half hour"*; then *"At two in the morning"* in the same sentence; then *"a hundred and four minutes."* **Writes: 1:10 + 2:00 + 0:30 = 3:40, and 1:10 + 1:44 = 2:54, and the chapter is called 0200.** Then asks why an ONI psych-ops officer who has just described a blackmail methodology in a room with a logged terminal is not more careful, and answers themselves correctly (the log records the badge, not the conversation) — the chapter has that covered. Then asks whether a records annex has a door that can be shut, and the chapter says *"with the door shut"*, so yes. **One hole and it is F1.**

### The Casual Reader
**8.5, borderline.** They will not remember the index or the manifest. They will remember a kind man at two in the morning explaining, patiently, how to take a stranger apart with forty minutes and an open door, and then being *sorry* about the offer being accepted — and they will not have a word for why that is the most frightening thing they have read this week. They like Zeus. **That is the vibe, and it is strong enough to carry a chapter in which nothing happens.**

Two risk windows and one is structural: **the chapter's most important paragraph is written to look like its most boring one.** The closing 90 words are base-accommodation procedure. A skimming reader disengages at *"a base accommodation office publishes its waiting list, because a waiting list has to be seen to be fair."* **They are rescued by the nine-word paragraph underneath it** — *"He had got that far before he stopped."* — which no eye skips. The design holds, narrowly, on one short paragraph. See F8.

### The Devoted Reader (SFF — active)
**Adopts this chapter.** Notices unprompted that **Kell is where Zeus was moved sideways to for two years** and that the office he is offering to work is in the building he was exiled to — and that nobody in the chapter remarks on it. Notices that the four-question run is a technique and that the narration refuses to say so. Will re-read the closing paragraph after Ch.22 and find that *"with the door standing open"* is quoted. Will build a theory about the laminated card. **Will also build a timeline spreadsheet and post F1 to a subreddit.**

---

## Cross-Reader Matrix

| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| The clock (F1) | — | — | **FLAG** | — | **FLAG** | **IMPORTANT** |
| Skim risk on the closing paragraph (F8) | FLAG | — | — | **FLAG** | — | **SHOULD FIX** |
| The `, which` gloss habit (F2) | — | **FLAG** | — | — | — | INVESTIGATE (pipeline-level) |
| *"the silence lasted exactly as long"* (F3) | — | FLAG | — | — | FLAG | SHOULD FIX |
| The gnomic twin (F5) | — | **FLAG** | — | — | FLAG | SHOULD FIX |
| Nothing happens | FLAG | — | — | — | — | INVESTIGATE (by design) |
| Question marks absent (§QM) | — | — | FLAG | — | FLAG | SHOULD FIX (book-level) |

---

## Revision Recommendations (Ranked)

*Fix order: Logic/Character → Structural → Connective → Prose → Factual. **Metric consequence stated for every finding. Narration is 96 sentences; the ≥40 w share has 3.1 pp of margin above its floor and the median has 1.5 words. Cutting one long narration sentence costs ~1.0 pp of the ≥40 w share.***

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Metric consequence | Project rule? |
|---|---|---|---|---|---|---|---|
| **F1** | Lines 8, 18, 44, 50, 134, 144 — the chapter's clock | **Logic** | Arrival at *"ten past one"*; *"two hours in a chair"* (l.8); *"nothing else for two hours"* (l.18); *"over the next half hour"* then *"At two in the morning"* **in the same sentence** (l.44); *"you've been typing two hours"* (l.50); *"a hundred and four minutes"* (l.134); *"for two hours"* (l.144). | Minimum stated elapsed 150 min against a stated log of 104 — a 46-minute contradiction, in narration as well as dialogue, in a chapter titled `0200` and running numerals at 39.4/1k. Ch.8's F1 established that exact numbers invite exact reading; this is the same failure one order of magnitude larger, and the Hostile and Devoted readers both find it in under two minutes. | **Option (a), recommended — keep 104 minutes, shorten the durations.** l.18 *"nothing else for two hours"* → *"nothing else for an hour and a half"*; l.50 *"typing two hours"* → *"typing an hour and a half"*; l.144 *"for two hours"* → *"for an hour and a half."* Leave l.8's *"two hours in a chair"* — it is Vexx's own rounding at the chapter's opening, before any clock is established, and it is the better sentence. This makes the whole chapter land at 02:54, which fits *"at two in the morning"* ×3, the title, Aglaope's *"half past two"* and *"four in the morning"* exactly. **Option (b) — keep the two hours, move the log to *"a hundred and fifty-five minutes"* and change *"ten past one"* to *"ten past twelve."*** Costs three edits instead of three and breaks nothing, but *104* is the more characterful number and the title argues for (a). **Do not leave it undecided.** | Option (a): +2 words each on l.18 and l.144, +2 on l.50 (dialogue, ungated). l.18's sentence 11 → 13 words: still above the ≤6 w band, does not cross 40. Numeric tokens roughly neutral (*two hours* → *an hour and a half* trades one numeral for one). No band crossed on any metric. | **Yes** — record the resolved timeline in `ENTITY_STATE.yaml` so no later pass re-derives it. |
| **F2** | Whole manuscript — narration `, which` at **3.49/1k** (author 0.00–0.80) | **Style — PIPELINE-LEVEL, new, and the highest-value finding here** | Seven instances in 2,005 narration words. Four are true glosses. Rising in every pipeline chapter: 2.00 → 2.60 → 2.93 → **3.49**. Pooled pipeline 2.72/1k vs author 0.22/1k — **12×**. | This is the mechanically countable form of Pattern #11 and **it is what the pipeline actually does that the author does not.** The Ch.7 and Ch.8 evaluations waived #11 on a broad measurement that swept in the author's own §1.2(b) signature and therefore exonerated the pipeline by measuring his voice as its fingerprint. **The disruptor named this exact construction in this exact chapter, cut two, and left seven** — producing a written record saying the pattern was handled. | **Ch.9 edit: cut three, restoring the author's ceiling.** The three cheapest, in order: (i) l.8 *"…who was asking, which is what two hours in a chair will do to a man."* → *"…who was asking. Two hours in a chair will do that to a man."* (converts the gloss to a free-standing gnomic, which is the author's form); (ii) l.94 *"…on the table, which did nothing whatever to the cup."* → *"…on the table. It did nothing whatever to the cup."*; (iii) l.244 *"…the date the claim went in, which is most of what a man would need."* → *"…the date the claim went in. Most of what a man would need."* **Pipeline fix, root: add `which_gloss_per1k` to `PIPELINE_CEILINGS` at 0.80, measured on quote-stripped narration.** | (i) splits one 22-word sentence into 13 + 10: −0 from ≥40 w, median unaffected (both above 6, both below 40), +1 narration sentence. (ii) splits a 41-word sentence into 34 + 7 — **this costs one ≥40 w narration sentence (14.6 % → 13.6 %, floor 11.5 %, still 2.1 pp of margin) and adds one ≤6 w-adjacent sentence.** Acceptable but spend it knowingly. (iii) 34 → 26 + 8, no band crossed. All three remove one `and`-free comma each; comma density 61.5 → ~60.6, floor 58.0, safe. | **Yes — implement the gate.** This is the fourth consecutive evaluation to recommend a `style_check.py` addition and the previous three were all implemented; this one closes the last unmeasured layer of §THE SEAM. |
| **F3** | Line 238 — *"The heater under the servery came on, and it ran, and it stopped, **and the silence lasted exactly as long as that did**."* | **Style — the outline's explicit constraint** | The narration measures the silence immediately after Aglaope's Ch.23 seed. | The outline's writer warning (c) is unusually strong: the line *"must be dropped and abandoned; no one picks it up; **it must not be flagged.**"* No character reacts and no interiority registers it — all correct — but a narratorial clause that measures the pause **is** a flag, and the deflation the clause performs is already complete without it: three flat verbs about a heater. The chapter establishes the unflagged version 180 lines earlier (*"The heater at the far end came on, ran a while, went off again."*) and the second one should be the same shape, not a bigger one. | **Cut nine words.** → *"The heater under the servery came on, and it ran, and it stopped."* | −10 words, −1 `and` in narration (**helps §THE SEAM's register sum: 42.5 → ~42.0**). Sentence 23 → 13 words; above the ≤6 w band, nowhere near ≥40 w. No band crossed. | No |
| **F4** | Line 98 — *"**His shoulders had come down off wherever they had been.** He looked at the grid."* | **Voice — narratorial confirmation** | The narration supplies a before-state (shoulders up) that Vexx never observed and the reader was never shown. | The brief's own test: *does the narration ever confirm he is doing something, where the reader should be left to notice?* This is the one place it does. And it is redundant — the cup-turn *"which did nothing whatever to the cup"* and *"I'd have been sorry if you'd taken it"* deliver the relief completely, in that order, in the same paragraph. The narrator is standing one step downstream of Vexx. | **Replace with a fact Vexx can see, holding length.** e.g. *"He sat back off the edge of the chair for the first time since Vexx had come in."* Or cut the clause entirely and let *"He looked at the grid"* carry it — the paragraph already has three physical beats. | Replacement is +6 words, holds the sentence out of both bands. Cut is −10 words and takes a 10-word narration sentence out entirely (median 14.5, floor 13 — one sentence removed from 96 moves the median by at most half a position; verify before committing). | No |
| **F5** | Lines 160 and 248 — *"The urn coffee at that hour is not coffee."* / *"The mess at four in the morning is a room with the chairs still down."* | **Style — Pattern #16** | The declared ugly sentence and the chapter's penultimate sentence share an identical construction: [definite NP] + [time adverbial] + *is* + [flat predicate], present tense, gnomic. They open and close the same scene. | The ugly sentence's whole job is to be the one bump in the prose. A twin at the close converts the bump into a device, and the closing line — which should be the freshest sentence in the chapter — arrives wearing something the reader met 88 lines ago. The Critic marks this. | **Change the close, not the ugly sentence.** The ugly sentence is doing declared work and is protected. Recast l.248's opening clause into the past-tense narration the rest of the close is in: *"There were still chairs down all along the mess."* Or delete the clause and open the paragraph on the action: *"Vexx put his cup upside down on the rack…"* | Recast is word-neutral. Deletion is −13 words and removes one 13-word narration sentence (see F4's median note — do not do both F4-cut and F5-delete without re-measuring the median). | No |
| **F6** | Lines 16 and 46 — *"Nine bays of shelving, of which four held anything."* / *"a materiel record in twenty-two lines, of which he had seven"* (+ *"four bays lit, five dark"* at l.140) | **Style — repeated frame** | The *N X, of which M* construction fires twice within thirty lines, with a third variant closing the scene. | Vexx's private tally is canon (§THE ONE CARVE-OUT) and none of these is spoken, so this is not device bleed. It is a **syntactic frame used three times in one scene**, and it is the frame the reader will most associate with the chapter's boring middle. Thinning by one costs nothing and makes the other two sharper. | **Recast l.16 only.** → *"Nine bays of shelving. Four of them held anything."* Keep l.46 (it is the dead end, and the ratio is the point) and keep *"four bays lit, five dark"* (it is the scene's closing image and the best of the three). | Splits a 9-word sentence into 5 + 5, adding two ≤6 w narration sentences: 21.9 % → 23.9 % against a **ceiling of 33 %**, safe. Numeric tokens unchanged. | No |
| **F7** | Lines 154–158 — Aglaope's first two turns | **Structural — the chapter's only join** | The scene opens on *"You came up from the annex,"* which shares its surface form with Zeus's scene-opening *"You came down here with a notebook you haven't opened."* The dialogue pass logged this (§6) and judged both available repairs worse. | The chapter's single break is carried by the same device that opened the scene before it. Their axes are genuinely separate (he reads activity, she reads weight) but the surface form is what a reader hears, and it lands at the one structural seam in the chapter. | **The repair the pass did not test: swap her first two turns.** Open on *"There's an inch left in the urn. It's been off since one, so it's an inch of something else now."* Let him pour and drink. Then *"You came up from the annex."* The observation still fires, it is still unasked, and the scene no longer opens on the previous scene's shape. | Zero — two dialogue lines reordered, no words added or cut, no narration touched. | No |
| **F8** | Lines 244–248 — the closing paragraph | **Pacing / Exposition** | 90 words of base-accommodation procedure (*"a base accommodation office publishes its waiting list, because a waiting list has to be seen to be fair"*) before the concrete beat arrives in the final sentence (*"by asking him about his summer"*). | **The chapter's most important paragraph is written to look like its most boring one.** It is the trap closing, and it is the one place a Casual or Devourer reader disengages. The design survives on the nine-word paragraph underneath it, which no eye skips — but that means the whole moral payload of the chapter rests on the reader's willingness to read 90 words of office procedure first. | **Move one concrete human image into the paragraph's first third, word-neutrally.** The chapter has the right one already and uses it earlier: *"people on the roster, who would come in at eight in the morning and hang their coats on a hook."* An equivalent here — the man's name on a waiting list beside the date his claim went in — puts a person in the paragraph before the procedure and buys the last sentence its reader. | Must be word-neutral or lengthening. The paragraph carries the chapter's only two ≥40 w sentences in its last 100 words; do not shorten either. Watch numeric tokens — this paragraph is already numerically dense (*ten minutes*, *first*). | No |
| **F9** | Whole book — **question marks** | **Style — PIPELINE-LEVEL, new** | Ch.9 contains zero question marks in 3,480 words with eleven spoken interrogatives. Pipeline trend 0.89 → 0.65 → 1.02 → **0.00**; author 1.01–2.90/1k. | `voice-dna.md` §1.3 declares the bare question a **PRESSURE behaviour**. The author punctuates ordinary spoken questions normally, down to *"Options?"* and *"Ready?"*. Applying the pressure form universally spends the channel: Aglaope's Ch.23 seed is punctuated exactly like a question about a cook. Seventeen chapters remain. | **Restore ~6 question marks in Ch.9** (Zeus's cook / the bund / *"Did he do it"*; Vexx's *"How's it ordered"* and *"What happened"*; Rx's *"Did you know that"*). **Reserve the bare form** for *"Why."*, *"How long does it take. Finding out what a man's protecting."* and Aglaope's Rx line. **Pipeline fix, root: add a `?`/1k floor at 1.00** (the author's measured minimum outside his all-memory chapter) and a note in `voice-dna.md` §1.3.2 that the bare form is load-triggered, not house style. | Zero on every gated metric — punctuation substitution only. | **Yes** — the floor and the §1.3.2 note. |
| **F10** | `character-bible.md` §STANDING OFFENCES #3 and #5 | **Continuity — rule hygiene** | #3 says the N-of-the-M construction is included in the counting-aloud reservation; the Ch.9 dialogue pass narrowed it in writing to *"the restatement"* to justify keeping *"Eleven people. Two of them sign retention exceptions."* #5 names the tidying gesture by **wording** and Ch.9 has three characters performing it by **grammar**. | A rule narrowed by the pass enforcing it, with the justification written into the record, is exactly how a §STANDING OFFENCE is created. And a watch-list that guards phrases cannot see a convergence in syntax — the same blind spot as Ch.8's F4 (uniform clause-chaining). | **Do not edit the lines. Edit the rules.** (a) Narrow §3 formally: the reservation covers *the performed sequence and the restated count*; a single spoken cardinality is not bleed. Record Zeus's *"Eleven people. Two of them…"* and Aglaope's *"Two hundred and nine"* as cleared under the narrowed rule. (b) Rewrite §5 to name the **grammar** — *adjusting a small object on a table in place of speaking* — and add a per-chapter ceiling of **two** such beats across the whole cast. Record Vexx's l.226 cup-turn as licensed by the author's own Ch.5 precedent. | Zero — documentation only. | **Yes — both.** |
| **F11** | Whole manuscript — `and` **register sum 42.5** (author 29.3–34.7) | **Style — PIPELINE-LEVEL, new metric** | Narration 21.5 (author max 21.6) and dialogue 21.0 (author max 21.0) — both registers on the ceiling simultaneously. The author never runs both hot: his sum ranges 29.3–34.7. Pipeline 48.0 → 45.9 → **42.5**. | The 24.0 whole-chapter ceiling sits 5 points above the author's narration maximum and cannot see either half, so the habit can be moved from one register to the other and score as an improvement — **which is exactly what happened between Ch.8 and Ch.9.** Ch.8's F4 (dialogue chaining) is genuinely closed; the sum shows the underlying habit is not. | **No Ch.9 edit** — both registers are inside the author's range and de-conjuncting either would be writing to a metric. **Pipeline fix, root: report narration `and` + dialogue `and` as a sum and gate it at 34.7**, the author's measured extreme, per `style_check.py` calibration rule #2. Report the two halves alongside it. | Zero for Ch.9. Adding the gate would put Ch.6 and Ch.8 in retroactive breach; recommend it fire from Ch.10 forward with those recorded as pre-gate, as was done for the simile floor. | **Yes** |
| **F12** | Ch.9's rule-of-three at ~3.0/1k (Ch.8 ~0.5) | **Style — hypothesis, not yet a finding** | Roughly ten triadic structures in 3,380 words, 6× Ch.8's rate, in the chapter that made the largest `and`→appositive conversion. | Merging short sentences into em-dashed appositive catalogues is a triad factory, and this is the fourth consecutive chapter to draft with the chaining fingerprint and convert at the self-check. If the conversion manufactures triads, the pipeline has been trading one anti-AI pattern for another for four chapters and nobody has been able to see it. | **No edit — half the triads break on the third element, which is the author's own move.** **Process fix: the next chapter that makes a large `and` conversion must save its pre-conversion draft to `evaluations/chapter-N-pre-conversion.md`**, so this is tested once rather than guessed at four more times. | Zero. | **Yes** — the process rule. |

### Fix order: F1 → F10 → F7 → F8 → F3 → F4 → F2 → F5 → F6 → (F9, F11, F12 are pipeline)

---

## Strengths to PRESERVE

1. ***"Less, if he has children."*** Four words, no adverb, no intensifier, in answer to a question Vexx could not stop himself asking, in the same voice as the guitar peg. **Never lengthen it, never let anything within two lines comment on it, never move it.**
2. **The offer's reassurances are all about the victim.** *"There's no mark on him… He goes home. He tells nobody. He'll be at that same desk for the rest of his service, perfectly all right."* This is the single structural reason Zeus cannot be read as a tempter, and it is worth more than every behavioural cue combined. **Record it in `character-bible.md` under Zeus so no later pass "improves" the pitch.**
3. ***"I'd have been sorry if you'd taken it."*** Delivered badly, into the middle of a conversation about coffee, thirty seconds after turning a cup for no reason. Its badness is the whole point.
4. ***"Zeus nodded once, at the grid in front of him rather than at Vexx."*** The most economical piece of characterisation in the manuscript.
5. **The four-question run and its refusal to explain itself.** The hook pass's cut of *"he did not work out until a great deal later what the order of them had been for"* was the single best editorial decision made on this chapter — it removed the plot promise, the POV breach, the menace, and the pre-empted shareable in twenty-five words. **Do not restore it in any form.**
6. **The closing paragraph, ending on *"with the door standing open."*** The corruption relocated a hundred lines past the offer, into a room with nobody in it, in the victim's own procedural register. Fix the skim risk (F8); do not touch the mechanism.
7. ***"I read it four times to see whether there were two documents."*** The chapter's stopping sentence, and the whole of Zeus's life.
8. **The comedy-into-devastation turn** (*"Four hundred." / "It was an example."* → *"Alphabetical puts Ansel next to Anseth."*) and the outline-order swap that made it possible. Best pacing move in the manuscript.
9. **Aglaope's Rx line landing on a heater and exiting on a guitar peg.** Fix the nine-word flag (F3); the rest of the drop is exemplary.
10. **The furniture listing detonating in the exact middle of the offer.** Unattributed, uncommented, never returned to, connected to nothing. Protected absolutely.
11. ***"He took hold of it again a second later and did not let go."*** The disruptor's only addition and it is the chapter's only evidence that the refusal cost anything.
12. **Merrick's notebook: brought down, read three times, not opened, unremarked by anyone.** The outline's hardest instruction and it is executed exactly.

---

## Cross-Chapter Pattern Detection (Ch.1–9)

| Pattern | Verdict |
|---|---|
| Same opening structure | **CLEAR — four shapes in four chapters.** Ch.6 transit, Ch.7 a table at night, Ch.8 mid-dialogue mid-argument, Ch.9 unattributed dialogue with no speaker and no room. **One WATCH:** Ch.7 and Ch.9 are both Vexx alone at a screen at 0200 with furniture listings in them. Deliberate (the writer report calls it a callback) and two in three chapters. A third would be a setting. |
| Same emotional rendering | **CLEAR — and it is the author's, not the pipeline's.** Emotion held to objects with interiority withheld, in Ch.1 (the dog tag, the empty casket) as in Ch.9 (the cup, the pen, four bays lit and five dark). |
| Same simile architecture | **CLOSED.** Nine bare comparisons, none extended, none explained, 2.7/1k — **first pipeline chapter inside the author's 2.5–6.4 band.** Ch.8's F3 gate (`simile_per1k` floor 2.0) was implemented and worked on the first chapter it governed. |
| Same dialogue pattern | **REGRESSION — the manuscript's worst.** Ch.7 flagged for turn-based cleanliness; Ch.8 posted the best result in the book (9 breaks + 1 cross-talk in 162 runs); **Ch.9 posts 1 in 161, in the chapter with the most dialogue.** See §Pattern 17. |
| Same character introduction | **CLEAR.** No new character appears on the page. Beattie, Curran, Ansel and Anseth are mentioned-only and correctly carded in `character-bible.md` with no tic spent. |
| **Rhythm signature (§THE SEAM)** | **Punctuation layer CLOSED (Ch.7). Breath layer CLOSED (Ch.8). Dialogue-chaining layer CLOSED (Ch.9 — F4 answered, 28.2 → 23.9 → 21.0).** **NEW LAYER: register sum 42.5 vs author 29.3–34.7 (F11).** |
| **Subordination (§THE HINGE)** | **NEW — narration `, which` 2.00 → 2.60 → 2.93 → 3.49/1k against the author's 0.00–0.80. Rising every chapter. Ungated. The strongest single divergence measured on this book (F2).** |
| **Punctuation (§THE QUESTION MARK)** | **NEW — `?`/1k 0.89 → 0.65 → 1.02 → 0.00 against the author's 1.01–2.90. A declared pressure device generalised into house style (F9).** |
| `somebody`/`nobody` | **CLOSED.** 3.46 → 3.33 → 4.60 → **2.7/1k.** The re-derived `vague_per1k` ceiling was implemented and the metric corrected itself without an edit. |
| Numeric density | **WORSENING.** 21.9 → 54.0 → 27.9 → **39.4/1k** against the author's 10.1–21.8. Third consecutive chapter above the 20/1k flag the Ch.8 evaluation set, and the second in which a precision habit has produced a coherence failure. |
| Chapter closers | **CLEAR.** Ch.7 found text, Ch.8 a re-read document, Ch.9 a light switch and a staircase. The hook pass's *"no third document"* note was honoured. |
| Chaos marker coverage | **HOLDING.** Ch.6 3/4, Ch.7 3/4, Ch.8 4/4, Ch.9 4/4 — but Ch.9's cognitive-distortion marker is weaker than Ch.8's (no operational consequence) and the writer report substitutes a different marker for it in the record. |
| **Pass-report reliability** | **NEW — WATCH.** Three claims in this chapter's pass reports do not survive checking: the disruptor's `, which` pattern declared handled at two cuts with seven remaining (F2); the dialogue pass narrowing §STANDING OFFENCE #3 in writing to fit a line it wanted to keep (F10); the disruptor conflating dialogue *non-responsiveness* with dialogue *mess* to decline Operation #8 (§Pattern 17). All three are reasoning errors in reports that are otherwise the most rigorous in the project, and all three have the same shape: **a correct diagnosis followed by a stopping rule that was too generous to the text.** |

---

## CVI-Launch Breakdown (chapter proxy)

| Input | Weight | Raw | Normalised | Evidence |
|---|---|---|---|---|
| Commercial Pacing | 20 % | 7.0 | 7.0 | Two scenes averaging ~1,690 words, one hard cut, no chapter-end hook by design. One very strong mid-chapter engine (the offer) and one live Ch.10 seed (the badge log). Against: two skim windows, and the payload paragraph is the least inviting prose in the chapter (F8). |
| Tomorrow Test | 20 % | 3 confident + 1 probable (1 image / 3 quote) | 9 | §Tomorrow Test. The strongest **quote** anchor set in the manuscript. |
| Casual Reader | 20 % | 8.5 | 8.5 | §Casual. Borderline; 8.0 defensible. They like Zeus and cannot say why he frightens them. |
| Shareability | 20 % | Quote **4** / Plot **1** / Emotional **3** | **6.93** | MAX(8) × 0.6 + AVG(5.33) × 0.4. Plot 1/5 is the brief (*"nothing in the plot moves"*), and the MAX-weighted formula is why it does not sink the score. |
| Concept Pitch | 10 % | yes | 10 | Book-level premise, one sentence, survives retelling. |
| Human Closeness | 10 % | yes | 10 | 100 % of the chapter. Four voices, two tables, 1,568 words of intimate conversation. |

**CVI-Launch = 8.29, +0.5 (strong anchor) = 8.79 → 8.8.** Ch.6 8.7 → Ch.7 9.1 → Ch.8 8.9 → **Ch.9 8.8.**

## CVI-Legacy Breakdown (chapter proxy — default weights; engagement is Fascination-primary, not Aspiration)

| Input | Weight | Score | Evidence |
|---|---|---|---|
| Originality | 30 % | 8.5 | Used directly per V3.6. |
| Theme Depth | 25 % | 9.0 | Used directly. |
| Cultural Vocabulary | 20 % | **2** | Nothing here enters language. *"The interrogator who never asks why"* is a concept the book never phrases. |
| Re-readability | 15 % | **7** | Higher than Ch.8's 6, and earned. Kell is where Zeus was exiled and is the yard he offers to work, unremarked. Aglaope's Rx line reads entirely differently after Ch.23. The closing paragraph quotes the offer verbatim and a first reader cannot know it. Zeus's *"I'd have been sorry"* is a different sentence after Ch.22. |
| Identity Effect | 10 % | 5 | Moderate — reading it makes you feel like a person who notices what is not being said. |

**CVI-Legacy = 6.73.** Ch.6 7.2 → Ch.7 7.6 → Ch.8 6.6 → **Ch.9 6.7.** Driven almost entirely by Cultural Vocabulary 2/10; a chapter-proxy legacy score remains the wrong instrument for a chapter that coins nothing on purpose.

---

## PATH TO 8.5 (MANDATORY — Genesis Floor is 8.0)

One dimension holds the floor and one fix clears it. The other two items are the difference between clearing the bar and clearing it well.

- **Pacing & Coherence 8.0 → 8.5 requires exactly one thing: F1.** Change three duration statements at lines 18, 50 and 144 from *"two hours"* to *"an hour and a half"* and the chapter's clock resolves to 02:54, which agrees with the title, with *"at two in the morning"* ×3, with *"a hundred and four minutes"*, with Aglaope's *"half past two"* and with *"four in the morning"* simultaneously. **Leave line 8's *"two hours in a chair"* alone** — it is Vexx's own rounding before any clock exists and it is the better sentence. **No other dimension is touched, no metric band is crossed, and the total edit is six words.** This is the cheapest 0.5 available anywhere in this project. Then record the resolved timeline in `ENTITY_STATE.yaml` so it is never re-derived.

- **Prose & Voice 8.5 → 9.0 requires closing §THE HINGE in this chapter, not just gating it for the next one.** The surgery is three sentences and it is specified verbatim in **F2** — lines 8, 94 and 244. Each converts a trailing `, which` gloss into the author's own form (a free-standing declarative), which is the move `voice-dna.md` §1.2(b) actually describes. That takes narration `, which` from 3.49/1k to 1.99/1k. **To reach the author's 0.80 ceiling, take a fourth: line 232's *"which had gone cold in the time it took him not to say them."*** It is the loveliest of the seven and it is also the purest instance — an object annotated with its own meaning. Recast as *"He drank what was left in the cup instead. It had gone cold in the time it took him not to say them."* Same words, same beat, no hinge. **Watch the ≥40 w band while doing this: F2(ii) costs one long narration sentence and the margin is 3.1 pp.**

- **Momentum 9.0 → 9.5 requires the declared shareable to land, and the site is Rx's block at line 144–148.** The outline names *"the interrogator who never asks why"* and the chapter makes the absence legible three times without ever making it a **rule**, which is what a reader needs in order to carry it out of the book. The narrator must not say it and Zeus must not gain a plan, so it goes to **Rx** — who has been in the room for two hours cataloguing a man's handwriting and a laminated card, and who will deliver it as a grievance rather than an insight. **One italic sentence, ~14 words, placed after *"He's left-handed"* and before the card**, in the shape of a complaint about something else: *He asked you seven questions and not one of them was the one anybody would ask.* No number in it (the counting rule), no diagnosis, no reaction from Vexx, and the next line is still about lamination. Cost: +14 words of italic dialogue. Metric: zero on narration median, ≥40 w, ≤6 w and comparison; +0 numerals if the count is left out as written. **This is the highest-value fourteen words available in the chapter** — it converts a concept the reader half-sees into one they can text to somebody.

---

## VERDICT

**POLISH.** Genesis Floor **8.0** (Pacing & Coherence) · Genesis Average **8.64** · Casual Reader **8.5** · CVI-Launch 8.8.

Below the 8.5 gate, to `book-editor`. **The PATH TO 8.5 above is mandatory and its first item is six words long.** This is not a chapter with a craft problem; it is a chapter with an arithmetic problem sitting on top of the best dialogue scene the pipeline has produced. Six of seven dimensions are at 8.5–9.0, the Prose drop from 9.0 is a measured four-regression call rather than an impression, and F1 alone restores the floor and takes the average to ~8.71.

**Do not action F2's Ch.9 edits and F5's deletion in the same pass without re-measuring the narration median and the ≥40 w share.** The chapter has 3.1 pp of margin on the long-sentence floor and 1.5 words on the median, and three of the recommended fixes spend from the same account.

---

**BIAS CHECK:** This evaluation was produced by the same system that wrote this prose, and bias is at maximum. Countermeasures applied and stated so they can be audited: every dimensional claim is anchored to a quoted line; every rhythm, subordination, punctuation and precision claim is a measurement computed against the author's own five chapters as control with one consistent tokenizer, and both the gate's splitter and a clean quote-strip are reported where they disagree; the cover-the-name test was re-run from the raw text rather than taken from the dialogue pass; the Pattern #11 arithmetic that would **fail** this chapter is published in full, in three readings, including the one I believe the last two evaluations got wrong in the pipeline's favour; and the two headline findings (§THE HINGE, §THE QUESTION MARK) are counts, not judgements, and both reverse or complicate conclusions this project has been carrying since Ch.7.

I have specifically interrogated three temptations. **(1) The temptation to hold 8.5/8.79 for a fourth chapter** — rejected; the clock error is larger and more visible than Ch.8's, which I did not drop Ch.8 for, and I have stated the comparison rather than assumed it. **(2) The temptation to break the streak for its own sake** — checked by confirming that Theme, Emotion and Momentum genuinely hold 9.0 on cited evidence and that the Prose drop rests on four measurements rather than a mood. **(3) The temptation to accept the four pass reports' own audits** — rejected on principle and it was the right call three times (F2, F10, §Pattern 17); those reports remain the most rigorous artifacts in this project and all three failures have the same shape, which is itself the finding.

Confidence in any score above 8.0 requires external validation — beta readers, an editor, comp analysis. **The number I would defend hardest is Pacing 8.0, because it rests on arithmetic anybody can check. The number I am least sure of is Prose 8.5 — treat it as 8.5 ± 0.5, and note that the same evidence supports 9.0 if §THE HINGE is judged a pipeline metric rather than a reading experience.** The Casual Reader 8.5 is borderline against 8.0 and does not change the verdict either way.

---
---

# RE-EVALUATION: Chapter 9 — 0200 (post-polish)
**Evaluator:** book-evaluator | **Date:** 2026-09-10 (second pass)
**Scope:** 3,357 words (`style_check` counter) · 1,761 words of narration under the CORRECTED
register splitter · 107 quoted runs + 9 italic runs (166 dialogue lines by the gate's count).
**This section is appended, not a replacement.** The first pass and its reasoning stand on the
record above, including the parts of it I retract below.

## RE-EVALUATION HEADLINE

**Genesis Floor: 8.5 | Genesis Average: 8.71 | Casual Reader: 8.5 | CVI-Launch: 8.8 | CVI-Legacy: 6.7**
**VERDICT: PASS.** Floor ≥ 8.5 and Casual ≥ 8.5, both met — **and one of them is met exactly.**

One dimension moved: **Pacing & Coherence 8.0 → 8.5.** Its single cited cap reason (F1, the
stopped clock) is verified repaired. No other dimension moved in either direction, and I show
below why three of them did not move despite work being done on them.

**The most important thing in this section is not the score.** It is that **my own F11
finding was wrong and is retracted**, and that the retraction was only possible because
someone fixed the instrument I measured it with. Details in §RETRACTIONS.

---

## 1. THE TIMELINE — rebuilt from the text, independently

I did not check the writer's arithmetic against the writer's account of it. I extracted every
temporal statement in the chapter and rebuilt the clock from scratch.

| Line | Statement | Implied time |
|---|---|---|
| 18 | *"He had been there when Vexx came in **at ten past one**."* | **01:10** — the anchor |
| 18 | *"Vexx had said good evening, then nothing else **for an hour**."* | 02:10 |
| 8 | *"…which is what **an hour in a chair** will do to a man."* (the opening exchange) | **02:10 ✓ agrees** |
| 16 | *"…it was into a man's back **inside the hour**."* | consistent, non-binding |
| 44 | *"Zeus asked four more **over the next half hour**."* | 02:40 |
| 50 | *"you've been typing **an hour and a half**"* | 01:10 + 1:30 = **02:40 ✓ agrees** |
| 44, 54 | *"**At two in the morning**"* ×2 · chapter title `0200` | 02:10–02:40 band ✓ |
| 134 | *"a badge asked it something for **a hundred and four minutes** at two in the morning"* | 01:10 + 1:44 = **02:54** |
| — | offer → refusal → cup → row four → Sedge → thanks → door → log → exit | **~14 min, 02:40 → 02:54** |
| 158 | *"It's been off **since one**"* (the urn) | independent ✓ |
| 218 | Aglaope: *"I've been sitting here **since half past two**"* | 02:30, ~50 min before he sits ✓ |
| 248 | *"The mess at **four in the morning**"* | ~03:00 → ~04:00, scene 2 ✓ |

**THE CLOCK CLOSES.** There is no longer a contradiction anywhere in the chapter, in narration
or in dialogue. Every one of the eleven temporal statements is simultaneously satisfiable, and
the two that were previously load-bearing errors (l.18 and l.50) are now the two that
independently confirm 02:40. The badge log at 104 minutes, the title `0200`, *"at two in the
morning"* ×2, *"half past two"* and *"four in the morning"* all agree. **F1 is CLOSED.**

The tightest joint is the 14 minutes between 02:40 and 02:54, which has to carry ~1,100 words
of scene. At conversational pace with the silences the chapter explicitly writes in, that is
comfortable — 1,100 words of dialogue is 8–9 minutes spoken. **It holds.** The loosest joint is
scene 2 (~03:00 → 04:00 for ~1,400 words), which is elastic but contradicts nothing, because
nothing states when scene 2 begins.

### Two residuals, both minor, neither floor-holding — and one of them the repair created

**R1 — Rx's *"two hours"* (l.144).** *"it has been driving me up the wall for two hours."* Rx
entered with Vexx at 01:10; at ~02:55 that is 1 h 45 m. As idiom in a complaint it survives;
as a number in the mouth of the book's precision character — who says *"thirty-one per cent
complete"* and *"seven years and four months"* — it is the one figure a Hostile reader can
still round on. **Fix (one phrase, zero metric cost, and it improves two other things):**
*"and it has been driving me up the wall **all night**."* Non-numeric, better complaint
register, and it removes one of the three numerals crowded into Rx's three-line block
(*thirty degrees*, *four years*, *two hours*) — which helps Pattern #13 and §STANDING
OFFENCE #3's aggregate problem at the same time.

**R2 — a new echo on the chapter's first line, introduced by the fix itself.** l.8 now reads
*"…which is what **an hour** in a chair will do to a man. 'He got one off the quartermaster.
It won't hold past **an hour**.'"* Two *an hour*s twenty words apart, on the chapter's opening
line, where before the repair the two durations differed. This is a real cost of my own
recommended edit and I did not anticipate it. **The gloss side is not available** — *"an hour
in a chair"* is now the sentence that makes the 02:10 open legible, so it is load-bearing
timeline. **Fix the string instead:** *"It won't hold **a day**."* In voice, keeps the
diagnosis (the peg, not the string), removes the echo, and removes one numeral. −1 word, no
band crossed.

---

## 2. THE OTHER THREE FINDINGS — verified applied

| Finding | Verified | Effect |
|---|---|---|
| **F4** — *"His shoulders had come down off wherever they had been"* | **CUT** (l.98 now: *"'It's been the water since August.' He looked at the grid. 'I'd have been sorry if you'd taken it.'"*) | See the risk note below. |
| **F3** — *"and the silence lasted exactly as long as that did"* | **CUT** (l.238 now: *"The heater under the servery came on, and it ran, and it stopped."*) | Aglaope's Ch.23 seed is now dropped with **zero** narratorial flag. The outline's writer warning (c) is satisfied exactly. −1 narration `and`. |
| **§THE HINGE / F2** — trailing `, which` gloss | **6 of 7 removed or recast**, 3.8 → **0.5/1k** (gate reads 0.6). Gate `which_gloss_per1k` implemented at **1.0**; all five author chapters and all four pipeline chapters now pass. | See §3 — this is now closed on all three readings. |

### ⚠️ The one real risk in the repair, and it did not fire

**Two independent passes each removed a signal I had called load-bearing for the same beat.**
F4 removed the shoulders line; the gloss repair (9.3) removed *"which did nothing whatever to
the cup"* — and my first pass had written that the cup-turn gloss and *"I'd have been sorry"*
*"deliver the relief completely."* Between them, two of the three signals for Zeus's relief
were deleted by passes that could not see each other. **That is exactly the aggregate blindness
I flagged under §Pass-report reliability, and it happened again, in my favour this time by
accident.**

I re-read the beat cold. **It survives, and it is better:**

> *"Zeus picked up the pen, held it over the fourth row a while, put it down again on the paper
> without having written a thing with it, then reached over and turned the cup a half-turn on
> the table. 'It's the water,' he said. 'Not the grounds.' … 'It's been the water since
> August.' He looked at the grid. 'I'd have been sorry if you'd taken it.'"*

Three purposeless motions in one sentence — pen up, pen held, pen down having written nothing,
cup turned — then a deflection about coffee, then the line. The relief is now delivered by
accumulated pointless movement instead of by a narrator annotating one gesture. **The gloss was
doing less work than I credited it with, because the sentence it sat in already contains its
own evidence.** This is the strongest single argument in the manuscript for the gloss gate.

**Recorded as a process finding, not a text finding:** the two passes got a good outcome without
either of them knowing the other was spending from the same account. Next time it will not
land this way. **Pipeline recommendation: when an evaluation names a beat's signals as
load-bearing, the editor pass and the style-repair pass must both be given that list.**

---

## 3. PATTERN #11 — RESOLVED, and the arithmetic that resolves it

Four evaluations have argued about this check. It can now be closed, because the corrected
splitter makes one consistent measurement possible across author and pipeline.

**The instrument:** the three mechanically countable forms of explanatory extension —
`the way X` (the author's §1.2(b) signature), `, which` (the pipeline's), and `as if/as
though` — counted identically in every chapter, whole text, no register split, no judgement.

| /1k | Ch.1 | Ch.2 | Ch.3 | Ch.4 | Ch.5 | **Author range** | Ch.6 | Ch.7 | Ch.8 | **Ch.9** |
|---|---|---|---|---|---|---|---|---|---|---|
| broad #11 | **1.30** | 2.08 | 2.35 | 2.11 | 3.19 | **1.30–3.19** | 2.29 | 1.99 | 1.58 | **1.49** |
| of which `, which` | 0 | 1 | 0 | 1 | 1 | **0–1 instance** | 8 | 1 | 4 | **2** |
| of which `the way` | 5 | 8 | 7 | 4 | 5 | **4–8** | 2 | 2 | 5 | **3** |

```
READING (A) — V3.4 as written, threshold >0.8/1k
  Ch.9 count 5 (threshold >6)      → not breached
  Ch.9 density 1.49/1k             → BREACHED
  BUT: it breaches for ALL FIVE author chapters, including the LOCKED Ch.1 at 1.30.
  A threshold that fails the benchmark is measuring the language, not the pipeline. NOT APPLIED.

READING (B) — author-benchmarked, broad definition
  Author 1.30-3.19/1k · Ch.9 1.49/1k  → PASS. Second-lowest in the manuscript;
  below four of the author's five chapters.

READING (C) — author-benchmarked, NARROW (the `, which` gloss, narration only)
  Author 0.00-0.99/1k (corrected denominators) · Ch.9 0.57/1k  → PASS.
  Was 3.9/1k before the repair.
```

**All three coherent readings now agree. No cap. §THE HINGE is CLOSED.** And the shape has
changed, not just the count: Ch.9's distribution (3 `the way` / 2 `, which`) is for the first
time **author-shaped** — the author's total comes almost entirely from his own signature form
and almost none from the gloss, and Ch.9 now does the same. Ch.6 (2 / 8) was the inverse.

**The gate's ceiling of 1.0/1k is correctly placed** on the corrected numbers — the author's
measured maximum is 0.99/1k (his Ch.5). That is closer to right than my own recommended 0.80
would have been. Noted, because I recommended 0.80 from a bad denominator (§RETRACTIONS).

---

## 4. §THE SEAM — RE-DERIVED on the corrected splitter, as instructed

The brief is right that my breath and register numbers were taken through a splitter that
counted wholly-italic paragraphs as narration. I re-derived everything that depended on it.
**One finding dies. One survives with a smaller multiple. One new one appears.**

| `and` /1k (gate's own splitter + word function) | Ch.1 | Ch.2 | Ch.3 | Ch.4 | Ch.5 | **Author** | Ch.6 | Ch.7 | Ch.8 | **Ch.9** |
|---|---|---|---|---|---|---|---|---|---|---|
| **Narration** | 18.4 | 18.3 | 18.9 | 18.2 | 18.8 | **18.2–18.9** | 20.7 | 20.4 | 22.1 | **24.4 ✗** |
| **Dialogue** | 27.2 | 17.1 | 13.9 | 20.4 | 11.4 | **11.4–27.2** | 27.1 | 10.2 | 25.1 | **20.1 ✓** |
| **Register sum** | **45.6** | 35.4 | 32.8 | 38.6 | 30.3 | **30.3–45.6** | 47.8 | 30.7 | 47.1 | **44.5 ✓** |

- **F11 (register sum) is RETRACTED.** I reported the author's range as 29.3–34.7 and Ch.9 at
  42.5, a 7.8-point breach. Corrected: the author's range is **30.3–45.6** — his own locked
  Ch.1 posts 45.6 — and **Ch.9 posts 44.5, inside it.** The claim that "he never runs both
  registers hot at once" was an artefact of reading his 30 italic paragraphs as narration.
  See §RETRACTIONS.
- **The divergence relocates, and it is real.** The author's **narration** `and` band is
  extraordinarily tight — **18.2–18.9/1k, a 0.7-point spread across five chapters**, which is
  as strong a signature as anything measured on this book. The pipeline: **20.7 → 20.4 → 22.1
  → 24.4, rising every chapter, Ch.9 the manuscript maximum at 1.29× his ceiling.** The
  whole-chapter gate (22.3 against 24.0) cannot see it, because the dialogue half is low.
- **Second measurement pointing the same way.** Ch.9's narration `≤6w` share is **19.4%**
  against an author range of **20.8–29.9%** — the least punchy narration in the manuscript,
  the only chapter below his floor. Longer chains, fewer short sentences: one habit, two
  instruments.

### Why this is NOT a Ch.9 edit, with the arithmetic

The brief asks which metric a finding moves. I ran the simulation. The obvious repair — split
chained narration sentences — is blocked:

```
Current (gate): 93 narration sentences | median 14.0 (FLOOR 14.0) | >=40w 14.0% (floor 13.0) | <=6w 19.4% (ceiling 30.0)
Split a >=40w sentence into 34+6 : >=40w 14.0% -> 12.9%   → BREACHES the 13.0 floor
Split three 18-24w into 14+6     : median holds 14.0 (passes only on strict `<`)
                                   >=40w 14.0% -> ~13.5%  (0.5 pp of margin left)
                                   <=6w  19.4% -> ~22%    (back inside the author's band)
                                   narration `and` 24.4 -> ~22.8/1k (still 1.21x his ceiling)
```

**The median floor of 14.0 and the ≥40w floor of 13.0 together mandate long chained narration,
and the excess `and` cannot be removed subtractively without breaching one of them.** The
author reaches the same breath with 5.5 fewer `and`s per thousand because he chains with
commas, em-dashes and colons instead — and Ch.9's narration em-dash is already at 14.2/1k
against his 6.8–13.9, so that channel is also full.

**Conclusion: this is a pipeline calibration finding for Ch.10, not an editor work order for
Ch.9.** De-conjuncting three sentences to satisfy a metric, with 0.5 pp of margin on a floor,
is writing to the gate. **Recommendation (root, per the UPDATE RULE): report
`and_narration_per1k` per chapter with a ceiling of 18.9 (the author's measured maximum),
firing from Ch.10 forward with Ch.6–9 recorded as pre-gate — the simile-floor precedent — and
a note that the repair is structural (chain with commas/colons/em-dashes, his mix) and never
subtractive.**

**Also retired:** the claim that Ch.7 is "the shortest-breathed chapter in the manuscript at
median 9.0." Its real narration is median 11. Nothing in my Ch.9 reasoning rested on that
figure — §THE SEAM's Ch.9 argument was about `and`, not breath — but the Ch.7/Ch.8 line of
findings should be re-read with 11 substituted for 9.0.

---

## 5. THE TWO FINDINGS DELIBERATELY NOT ACTIONED — judged

### §THE QUESTION MARK — the finding STANDS, and not gating it was RIGHT

**Both halves of that sentence matter.**

**Not gating it was correct.** An interrogative detector that returns zero for a chapter with
eleven spoken interrogatives is broken, and gating a metric on a broken detector is worse than
leaving it ungated — it manufactures false clean reports, which is the specific failure mode
this project has been fighting since Ch.7. Building the detector, finding it wrong, and
declining to ship it is the right call and better practice than the finding that prompted it.

**But the prose defect never depended on that detector, and it stands undiminished.** It rests
on two things, both intact: a `?`/1k count, which is trivially reliable and which the gate now
reports; and a hand count of interrogatives, which is a human reading.

| `?` /1k (gate) | Ch.1 | Ch.2 | Ch.3 | Ch.4 | Ch.5 | **Author** | Ch.6 | Ch.7 | Ch.8 | **Ch.9** |
|---|---|---|---|---|---|---|---|---|---|---|
| | 1.0 | 2.3 | 3.0 | 2.1 | 1.1 | **1.0–3.0** | 0.9 | 0.7 | 1.1 | **0.0** |

**Zero question marks in 3,357 words at a dialogue ratio of 1.78:1 — the highest in the book.**
Not one author chapter is below 1.0, including the all-memory Ch.1. `voice-dna.md` §1.3 makes
the bare question one of four PRESSURE behaviours; Ch.9 fires it on *every* question by *every*
character, including *"Do you know the cook's name."* and *"How's it ordered."* A device that
fires on everything marks nothing, and Aglaope's Ch.23 seed is currently punctuated exactly
like a question about a cook.

**The fix, specified, since the brief asks for it. Six restorations, four holds, zero metric
cost — punctuation substitution only:**

- **Restore `?`:** l.32 *"Do you know the cook's name?"* · l.36 *"What did you tell the station commander about the bund?"* · l.40 *"Did he do it?"* · l.120 *"What happened?"* · l.174 *"How's it ordered?"* · l.144 (Rx) *"Did you know that?"*
- **Hold the bare form — these are the load:** l.124 *"Why."* · l.82 *"How long does it take. Finding out what a man's protecting."* · l.228 *"Have you told anybody but him,"* · l.236 *"What happens to him if you're wrong," … "And what happens to him if you're right."*

That is six ordinary questions punctuated ordinarily and four loaded ones left bare, which is
the author's own practice and which makes the Ch.23 seed land as pressure instead of as house
style. **This is chapter 9 of 26 and the channel has to work seventeen more times.** It does
not hold any dimension below 8.5 — it is one of three cap reasons holding Characters off 9.0 —
but it gets more expensive every chapter it is deferred.

**Gate recommendation, revised:** do not gate the interrogative count. **Gate the `?`/1k floor
at 1.0** (the author's measured minimum, already reported) and add one human item to the
dialogue-polish checklist: *"if the bare-question form fires more than three times in a
chapter, restore the ordinary ones."* A floor on a two-character regex is measurable; the
detector is not needed for it.

### Pattern #17 — I NARROW MY OWN FINDING. Leaving the interruption count at 1 was right; the finding survives in a smaller and sharper form

Verified: **1 dash-terminated dialogue line in 166. Zero ellipses. Zero self-repairs. Zero
repeated-word stumbles.** The count is unchanged and it is still the manuscript's lowest in the
chapter with the most dialogue.

**Two things I under-weighted in the first pass, and they are good arguments:**

1. **The single interruption is optimally placed.** *"or it'll take you—" / "Four hundred."* is
   the comedy-into-devastation hinge, which I called the best pacing move in the manuscript. If
   a chapter gets one interruption, that is where to spend it. Adding more would flatten it.
2. **The chapter does have dialogue mess — it is just not prosodic.** *"How long does it take.
   Finding out what a man's protecting."* is a false start followed by a self-specification.
   *"There was a thing to say — he could see the shape of it, could have done it in four words
   — and he left it where it was"* is a narrated abandoned sentence. *"How's it ordered." / "In
   order." / "Chronological." / "That's what in order means."* is four turns of refusal to
   answer. Two exhausted professionals declining to say things IS the chapter's subject, and
   interrupting each other is a different chapter.

**So I withdraw the demand for more interruptions and narrow the finding to what actually
survives it: zero self-correction.** Zeus delivers 350 words of blackmail methodology at 02:45
without one mid-sentence repair. False starts do not require rudeness; they require tiredness,
and the chapter's premise is tiredness. **Highest-value single edit, ~4 words, zero metric
cost:** in l.66, *"they go looking for something enormous, there isn't one, they give up"* →
*"they go looking for something enormous — there isn't one, there's never one — they give up."*
One self-correction, from a man who has said this before and is deliberately not relishing it.
**It does not hold any score.** It is worth doing because Ch.8 proved this pipeline can produce
9 breaks in 162 lines, so the capability exists and only needs pointing.

---

## 6. REVISED GENESIS SCORE

| Dimension | 1st pass | **Now** | What changed |
|---|---|---|---|
| Originality | 8.5 | **8.5** | Untouched by the repair. Both cited originality moves intact. |
| Theme | 9.0 | **9.0** | Cap reason (*"He had got that far before he stopped"*) unchanged and I would still not cut it. |
| Characters | 8.5 | **8.5** | All three cap reasons stand: cover-the-name ~57% (the form, not a defect), gesture-grammar convergence, shared question punctuation. `turn`-verbs rose from 12 to 13 (9.4's chair recast) but the **grammar** count did not — a chair turned *toward* an interlocutor is the opposite function from a cup turned instead of speaking. WATCH holds, no cap. Chaos still **4/4 inhabited**; 9.2's recast preserves the cognitive-distortion marker verbatim in coordinate form. |
| Prose & Voice | 8.5 | **8.5** | **One of four cited regressions closed; three stand; one new appears.** See below. |
| **Pacing & Coherence** | **8.0** | **8.5** | **F1 verified closed.** The clock is rebuilt above and it closes on all eleven statements. Not 9.0: two skim windows (F8) unfixed — the 130-word index paragraph and the manifest escalation — and scene-end pull is 1 of 2, with the chapter closing flat by design. |
| Emotion | 9.0 | **9.0** | **One of two cap reasons cleared** (both narratorial confirmations cut; the relief beat verified stronger without them). The other holds and was always the sufficient one: the POV character carries almost none of the emotional load — his own beat is four words of hand — now a two-chapter pattern. 9.5 is available only by giving Vexx a load the chapter is designed to withhold from him. |
| Momentum / Series Engine | 9.0 | **9.0** | Both forward loads intact. The PATH's Rx line (the declared shareable, *"the interrogator who never asks why"*) was **not** added — l.144 is unchanged — so the cap reason stands. Verified independently: `why` occurs **once** in the chapter and it is Vexx's. §STANDING OFFENCE #1 holds. |
| **FLOOR** | 8.0 | **8.5** | |
| **AVERAGE** | 8.64 | **8.71** | Floor/average gap 0.21 — **no single-dimension bottleneck. The chapter is now flat at 8.5–9.0.** |

**Trajectory: Ch.1 8.5/8.71 (locked) → Ch.6 8.5/8.79 → Ch.7 8.5/8.79 → Ch.8 8.5/8.79 → Ch.9 8.0/8.64 → Ch.9 rev.4 8.5/8.71.**

### Why Prose did not move, stated plainly — because the editor did exactly what I asked

My PATH wrote: *"Prose & Voice 8.5 → 9.0 requires closing §THE HINGE in this chapter, not just
gating it for the next one."* **It was closed, and more thoroughly than I specified — six
instances against the four I named.** The editor is entitled to an accounting.

The 8.5 came with **four** cited regressions, of which the hinge was (1):

| | 1st pass | Now |
|---|---|---|
| (1) `, which` gloss 3.49/1k | regression | **CLOSED** — 0.5/1k, inside the author's band, author-shaped distribution |
| (2) Pattern #17, 1 break in 161 lines | regression | **STANDS** at 1 in 166 — narrowed to *zero self-correction* (§5), but standing |
| (3) Numeric density | regression | **STANDS and is unimproved** — 41.8/1k on a like-for-like regex against the author's 11.7–23.4. **1.79× his maximum, and now the largest remaining measured divergence on this chapter.** |
| (4) The gnomic twin (Pattern #16) | regression | **STANDS, and has tightened.** F5 was not actioned. Worse: 9.7's recast (*", which is most of what a man would need"* → *"That is most of what a man would need."*) — which I recommended — converts a subordinate gloss into a free-standing gnomic, so the closing 500 words now carry **three** present-tense gnomic declaratives (*"That is most of what a man would need." / "Leave is held on the section sheet…" / "The mess at four in the morning is a room with the chairs still down."*) where they carried two. The trade was subordination for aphorism. It is the author's form and it is the right trade, but it concentrates #16 in the paragraph that most needs to be fresh. |
| **(5) NEW** | — | **Narration `and` 24.4/1k against the author's 18.2–18.9, manuscript maximum, rising in all four pipeline chapters; plus narration `≤6w` at 19.4% against his 20.8–29.9% floor.** §4. |

**One closed, three standing, one new. Prose holds at 8.5.** I am not moving a goalpost: the
hinge was named as the *dominant* regression, not the only one, and I wrote in the first pass
that Prose was "8.5 ± 0.5." The honest position now is that the ± has collapsed downward — the
same evidence no longer supports 9.0, because the measurement that would have supported it is
the one that got fixed, and two others moved against the chapter in the same pass.

**Prose 8.5 → 9.0 is now two edits, both specified: F5's recast of l.248 and the l.66
self-correction.** Neither touches a gated metric. The narration-`and` finding is explicitly
NOT part of that path (§4 shows it is not repairable inside the bands).

---

## 7. ANTI-AI SCAN — re-run on the patterns the edits touched

| # | 1st pass | Now |
|---|---|---|
| **11** Explanatory Extension | FOUND, 3 readings, one failing | **FOUND — minor. 5 instances / 1.49 per 1k, below four of the author's five chapters. All three coherent readings pass (§3). No cap.** |
| **16** Philosophical asides | FOUND — moderate, ~1.2/1k (4) | **FOUND — moderate, ~1.5/1k (5).** Slightly up, and clustered: three gnomics in the closing 500 words. The count rose *because of* the recommended repair. F5 is now more valuable than it was. |
| **3** Automatic rule of three | FOUND — moderate ~3.0/1k | **Unchanged.** 9.2's recast adds a coordinate `and`, not a triad. The anti-three (*"twice, then once more, smaller"*) survives. |
| **10** Described emotions | CLEAR, 0 | **CLEAR, 0.** Verified: zero `felt`/`feel`/`realise`/`as if`/`as though`. The shoulders cut removes the chapter's only narratorial before-state. |
| **13** Precision Flex | FOUND — strong | **FOUND — strong, unimproved. 41.8/1k vs author 11.7–23.4.** Trend 24.0 → 56.4 → 30.8 → **41.8**. It no longer produces a coherence failure (that was F1), but the habit is ungated and this is now the chapter's largest divergence. |
| **14** Emotional control demonstration | CLEAR — inverted | **CLEAR — inverted, and strengthened.** The shoulders cut removes the one place a recovery was narrated. |
| **17** Clean dialogue | FOUND — "manuscript's worst," 9× regression | **FOUND — narrowed. 1 break in 166. I withdraw "collapse"; the finding is zero self-correction, not too few interruptions (§5).** |
| **4** Em-dash | CLEAR 9.8/1k | **CLEAR whole-chapter (9.8, band 8.5–12.0). Narration-only 14.2/1k against the author's 6.8–13.9 — marginally over, recorded not actioned; the channel is full, which matters for §4.** |
| 1, 2, 5, 6, 7, 8, 9, 12, 15, 18, 19, 20 | as recorded | **Unchanged. Verified untouched by the diff.** |

**Total: 9/20 found. Commercial Fiction band: WATCH (9–11), at the bottom.** Ch.6 9 → Ch.7 8 →
Ch.8 11 → Ch.9 9 → **Ch.9 rev.4 9.** The count is flat but the composition improved: the
deepest structural tell (#11) went from a contested breach to a clear pass, and #13 replaced it
as the top divergence. **The standing caveat on the band choice from the first pass still
applies and is still a choice the orchestrator should know about.**

---

## 8. RETRACTIONS — my first pass was wrong about two things

The brief invites me to say if my original scoring was wrong in either direction. The **8.0 was
right**: a 46-minute contradiction stated in narration, in a dimension named "Pacing &
Coherence," in a chapter titled `0200`, restated four times, found by two of five simulated
readers in under two minutes. I would score it 8.0 again. But two of the *findings* attached to
that pass do not survive.

**RETRACTION 1 — F11, the `and` register sum. Withdrawn in full.** I reported the author's
register-sum range as **29.3–34.7** and Ch.9 at **42.5**, called it a 7.8-point breach, wrote
that "the author trades — he never runs both registers hot at once," and **recommended a
pipeline gate at 34.7.** All of that was computed through a splitter that read the author's
italic register as his narrator's prose. Corrected: his range is **30.3–45.6**, his own locked
Ch.1 posts **45.6**, and Ch.9 posts **44.5 — inside his range.** *Had that gate been
implemented at 34.7 it would have put the author's locked benchmark chapter in breach by 11
points, and every chapter of the book would have been "repaired" toward a voice he does not
have.* This is the exact failure the gate file's own calibration comment warns about — "a
threshold set tighter than the author's measured range pushes the prose AWAY from his voice
while appearing to protect it" — and I committed it while quoting the rule.

**RETRACTION 2 — §THE HINGE's multiples were overstated, though its direction was right.** I
reported the author's narration gloss range as 0.00–0.80/1k and a pooled 12× divergence. On
corrected denominators the author's range is **0.00–0.99/1k** and the pooled divergence was
**~8×, not 12×**. The finding itself survives — the pipeline glossed and the author does not,
and the repair validated it on the first chapter it governed — but I recommended a ceiling of
**0.80, below the author's actual maximum of 0.99.** The implemented ceiling of **1.0 is better
than the number I gave**, and whoever chose it over mine was right.

**Both errors have the same shape and it is worth naming, because it is a lesson about this
role and not about this chapter: I derived thresholds from a measurement I had not validated,
in a document that spends four pages attacking other passes for doing exactly that.** Two
evaluations were spent finding that the pipeline's fingerprint hides one register below where
the watch-lists look; the instrument that measures registers was itself miscalibrated the whole
time. **Standing rule I am adding for myself and recommending for the root: an evaluator
proposing a numeric gate must first report that metric for the author's locked Ch.1 and state
whether Ch.1 passes it.** Neither of my two proposed gates would have survived that one line of
verification.

---

## 9. WHAT DID NOT CHANGE

The four-reader simulation is not re-run, because only one score moved and it moved on a
verified arithmetic repair. Two reader positions do change and are recorded:

- **The Hostile Reader** — previously "goes straight to the clock and finds it inside ninety
  seconds. **One hole and it is F1.**" **Now: no hole.** I re-ran the check as the Hostile and
  the reconstruction in §1 is what they get. The only rounding left is Rx's *"two hours"* (R1),
  which is a 15-minute idiom in a complaint, not a contradiction — but Rx is the worst mouth in
  the book to put a rounded number in, and this reader knows it.
- **The Devoted Reader** — previously "will build a timeline spreadsheet and post F1 to a
  subreddit." **They will still build the spreadsheet. It now closes.**

Unchanged: Devourer (stops nowhere, skims two places), Critic (eleven underlines; will still
mark the gnomic twin, and will no longer feel the gloss habit), **Casual Reader 8.5 —
borderline, unchanged, 8.0 still defensible.** The two skim windows that make it borderline
(F8) were not actioned.

**CVI-Launch 8.8** (Commercial Pacing 7.0 · Tomorrow 9 · Casual 8.5 · Shareability 6.93 ·
Pitch 10 · Closeness 10 = 8.29, +0.5 anchor). **CVI-Legacy 6.7.** Both unchanged — the repair
was invisible to every commercial input, which is the correct outcome for an arithmetic fix.
**Tomorrow Test: ANCHOR EXISTS**, all four anchors verified intact and untouched by the diff.

---

## 10. OUTSTANDING — ranked, for whoever takes this chapter next

Nothing here blocks the gate. Fix order: Logic → Prose → Pipeline.

| # | Location | Type | Direction | Metric cost |
|---|---|---|---|---|
| **R1** | l.144, Rx | Logic (minor) | *"for two hours"* → *"all night."* | Zero. −1 numeral (helps #13). |
| **R2** | l.8, Paladin's string | Style (new, created by the F1 fix) | *"It won't hold past an hour."* → *"It won't hold a day."* | −1 word, −1 numeral. No band. |
| **F5** | l.248 | Style / #16 — **now stronger than at first pass** | Recast the gnomic: *"There were still chairs down all along the mess."* Protect l.160's ugly sentence. | Word-neutral. **Do not also delete — the median has zero headroom.** |
| **§QM** | 6 lines listed in §5 | Style — book-level | Restore 6 `?`, hold 4 bare. | Zero. |
| **#17** | l.66 | Style | One self-correction in Zeus's offer. | +4 words. Zero band. |
| **F8** | l.244–248 | Pacing | Unactioned. A human image in the paragraph's first third — this is what holds Casual at 8.5 rather than 9.0. | Must be word-neutral or lengthening. |
| **F7** | l.154–158 | Structural | Unactioned. Swap Aglaope's first two turns. | Zero. |
| **F6** | l.16 | Style | Unactioned. *N X, of which M* ×3 in one scene; thin by one. | Adds 2 ≤6w sentences — **now desirable** (§4). |
| **P1** | root `style_check.py` | Pipeline | `and_narration_per1k` reported, ceiling 18.9, firing from Ch.10, Ch.6–9 pre-gate. **Verify Ch.1 passes it before shipping.** | — |
| **P2** | root `style_check.py` | Pipeline | `?`/1k **floor** at 1.0. Do NOT gate the interrogative detector. | — |
| **P3** | root `style_check.py` | Pipeline | `numeric_per1k` — the chapter's largest divergence (1.79×). Author max 23.4. **Needs a declared-exemption mechanism on the PUNCH precedent**, because Ch.7 (56.4) is a records search and Ch.9 counts the dead; a flat ceiling would be wrong. | — |
| **P4** | root, evaluator + editor agents | Pipeline | When an evaluation names a beat's signals as load-bearing, both the editor and the style-repair pass must receive that list. Two passes spent from the same account this cycle and got lucky. | — |
| **P5** | root, evaluator agent | Pipeline | **An evaluator proposing a numeric gate must report that metric for the locked Ch.1 and state whether Ch.1 passes.** Both of my proposed gates would have failed this. | — |

---

## RE-EVALUATION VERDICT

**PASS.** Genesis Floor **8.5** · Genesis Average **8.71** · Casual Reader **8.5** ·
CVI-Launch **8.8** · CVI-Legacy **6.7**.

Both gate conditions are met. **One of them is met exactly**, and I want that on the record
rather than buried: Casual Reader 8.5 is the least robust number in this evaluation, I called
8.0 defensible in the first pass, and the two skim windows that make it borderline (F8) were
not fixed. **If the orchestrator wants margin rather than a bare pass, F8 and F5 are the two
cheapest lifts in the chapter and neither costs a gated metric.** Genesis Floor 8.5 is the more
solid of the two — it rests on a timeline anybody can rebuild from the table in §1.

The chapter that arrived here had six dimensions at 8.5–9.0 and one arithmetic error. The error
is gone, six words did it, and the floor moved 0.5 exactly as predicted. Nothing was talked
into place: **four dimensions did not move despite work being done on them, and I have shown
the measurements for each.**

---

**BIAS CHECK:** This re-evaluation was produced by the same system that wrote the prose and by
the same evaluator that produced the first pass — bias toward confirming my own earlier
findings is now stacked on top of bias toward the text. Countermeasures applied and stated so
they can be audited: the timeline was rebuilt from the raw text into a table rather than
checked against the writer's account of it; every metric was recomputed on the book's own
`split_registers` function and its own `words()` tokenizer rather than my previous ad-hoc
splitter, and the author's five chapters were measured with the identical instrument in the
same run; the Pattern #11 arithmetic that would fail this chapter is published again in full,
and is now shown to fail the locked Ch.1 harder than Ch.9; **two of my own first-pass findings
are retracted, one of them a recommended gate that would have put the author's locked benchmark
in breach by 11 points**; one of my findings (#17) is narrowed against my own first-pass
language after I credited an argument the writer made by declining to act; and the score of the
dimension I was asked about moved by exactly the +0.5 the anti-inflation rule permits, on one
cited, independently reconstructed improvement.

Three temptations interrogated. **(1) The temptation to lift Prose to 9.0 because the editor
executed my work order exactly** — rejected, with the four-regression ledger published so the
refusal can be audited; the accounting is one closed, three standing, one new. **(2) The
temptation to hold Pacing at 8.0 to avoid looking like I was reversed by a six-word edit** —
rejected; the clock closes on all eleven statements and I have published the table.
**(3) The temptation to defend F11 rather than retract it** — rejected, and it was the closest
call in this pass, because retracting it costs me the strongest-sounding finding in the
original document and replaces it with a smaller one.

Confidence in any score above 8.0 requires external validation — beta readers, an editor, comp
analysis. **The number I would defend hardest is Pacing 8.5, because it now rests on arithmetic
anybody can check in the table above. The number I am least sure of is Casual Reader 8.5, which
is exactly on the gate and which I would not fight anyone over. The number that should worry
the orchestrator most is not on this page: numeric density at 1.79× the author's maximum, in
the fourth consecutive chapter above the flag, still ungated.**
