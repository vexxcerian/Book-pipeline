# Quality gates

Everything a chapter has to clear, and why each gate exists. Two independent layers: the
**judgement layer** (the evaluator's scores) and the **mechanical layer** (Python scripts
that count things). Neither can substitute for the other — a model can talk itself into
thinking a chapter is clean; `grep` can't.

## The Genesis Score — 7 dimensions

1. **Originality** (genre-adjusted)
2. **Theme** (as a question, never an answer)
3. **Characters** — including the cover-the-name test and the tic-proliferation scan
4. **Prose & voice**
5. **Pacing & coherence** — the #2 predictor of commercial success in the benchmark
6. **Emotion** — assessed against the book's engagement type, not a single empathy standard
7. **Configurable** — set per book in `STATE.yaml` (structure, world-building,
   intellectual engagement, momentum, or identity effect)

**The floor is the score.** A chapter is as strong as its weakest dimension. Both floor and
average get recorded, but gates are on the floor — that is what stops a chapter with
brilliant prose and no characters from passing on its average.

### The gate

- **Hard floor** (genre-adjusted): literary 7.5, commercial 7.0, thriller 7.0, memoir 7.5,
  prescriptive NF 7.0. Below this a chapter is *broken* and never ships.
- **Pass** = **Floor ≥ 8.5 AND Casual Reader ≥ 8.5.** Nothing else is a pass. "Good enough"
  is not a state this pipeline has.
- In between: the polish loop. `book-editor` fixes only the 1–2 dimensions holding the
  floor down, quoting the evaluator's "PATH TO 8.5" and the "Strengths to PRESERVE" list —
  the second half matters, since the classic revision failure is fixing a weakness by
  flattening a strength. Max 5 cycles, then escalate.

### Anti-inflation

A model scoring prose produced by the same model is at maximum bias, so the protocol
assumes 0.5–1.0 of inflation by default:

- No score may jump more than **+0.5 per revision cycle**. So 7.5 → 8.5 takes at least two
  cycles. That is expected — budget for it rather than abandoning the loop early.
- Every score needs **textual evidence**: a cited passage.
- A floor above 8.0 without extraordinary evidence should be **challenged**.
- The evaluator scores chapters it did **not** write.

## CVI — the Commercial Viability Index

Co-equal with the Genesis Score, because the benchmark showed the two measure different
things: floor-7.0 books in the sample sold 62M copies between them; floor-8.5 books sold
6M. Craft quality does not predict sales.

- **Genesis Score** governs *revision priority* — what to fix, in what order.
- **CVI-Launch** governs *submission readiness* — commercial pacing, the Tomorrow Test,
  the casual reader's verdict, shareability, concept pitch, human closeness.
- **CVI-Legacy** governs *long-term potential* — originality, theme depth, cultural
  vocabulary, re-readability.

**When Genesis and CVI diverge by 2.0+, the divergence is itself the finding**: well-crafted
but commercially fragile, or commercially potent but critically limited. Both are useful to
know before you publish; neither is automatically a problem to fix.

## The reader simulation

Five readers, run against every chapter. They exist because "is this good?" is the wrong
question — different readers fail a book for different reasons.

| Reader | Fails on |
|---|---|
| **The Devourer** | Boredom. Would they keep turning pages? |
| **The Critic** | Craft. Cliché, unearned emotion, sloppy structure. |
| **The Hostile** | Everything. Fed by the hostile persona from `reader-personas.md`. |
| **The Casual Reader** | Effort. The gate reader — must score ≥ 8.5 to pass. |
| **The Devoted Reader** | Genre expectations, when the genre has them. |

Plus the **Tomorrow Test** (what concrete anchors does the reader still remember tomorrow?),
the **Discovery Test** on chapter 1 (BUY / MAYBE / PUT BACK from three pages) and the
**Residue Test** on the final chapter (emotional residue, not a cliffhanger).

## The 20-pattern anti-AI scan

Ten surface patterns (forced symmetry, empty poetic vocabulary, rule of three, excessive
em-dashes, empty metaphors, "And" openings, pseudo-philosophical closings, excessive
parallelism, over-smooth transitions, described emotions) and ten deep ones. The deep ones
are the ones that matter, because they survive editing:

**#11 Explanatory Extension** — observations that explain themselves; similes with an
extension that unpacks the comparison. The single most reliable AI fingerprint, and the
disruptor's priority-one target. Write similes **raw**; do not extend them.

Then: #12 binary negation openers ("Not X. Not Y. It was Z."), #13 precision flex
(unnecessarily exact numbers), #14 emotional control demonstration (notice → manage →
continue, always successfully), #15 authoritative description (settings with no gaps or
wrong impressions), #16 philosophical asides (thoughts that work on coffee mugs), #17 clean
dialogue (orderly turn-taking, no interruptions or cross-talk), #18 thematic echo chamber
(every detail resonates; zero texture, zero noise), #19 graduated reveal (the same
establish → anomaly → escalate → close shape every chapter), #20 emotional temperature
reports at even intervals.

Scoring is by **density per 1,000 words**, not raw count, and thresholds are
**genre-adjusted** — human bestsellers score 0–13/20 on this scan, and commercial fiction
is *supposed* to hit more of these than literary fiction. Clean bands: literary 0–3,
memoir 0–4, commercial 0–8, prescriptive NF 0–12.

**Prevention beats detection.** The whole anti-AI apparatus is aimed at not writing these
in the first place — the writer works under the anti-pattern budget, the architect varies
structure, the bible caps tics. The scan is the backstop.

## The mechanical gates

Per-book scripts in `books/<slug>/tools/`. They are deterministic, they gate by exit code,
and they catch what judgement misses across a whole manuscript.

### `style_check.py`

```bash
python3 books/<slug>/tools/style_check.py
python3 books/<slug>/tools/style_check.py --max-simile 4
```

- **Verbal tics** — crutch words (just, suddenly, seemed, somehow, for a moment…) over a
  ceiling.
- **Repeated phrases** — distinctive 4–6 word n-grams reused within or across chapters.
- **Simile/metaphor load** — markers per 1,000 words against a ceiling.
- **Connective habit** — `and`, comma and vague-pronoun density per 1,000 words.
- **Breath** — sentence-length distribution of the NARRATION: median, share of sentences
  ≥40 words, share ≤6 words. The dialogue:narration ratio is reported alongside them.
- Reports adverb (-ly) and em-dash density per chapter.

#### Ceilings AND floors — the half that is easy to forget

A ceiling stops the pipeline **exceeding** the author. A floor stops it falling **short** of
him. The second failure is the one that actually happens. Told "no more than 9.5 em-dashes
per 1,000 words", a writer scores a safe 4.7 and produces prose that is calm where the
author is nervous. No individual sentence is wrong, every other check passes, and twenty
chapters of it is a second author standing behind the first.

So `PIPELINE_FLOORS` is as load-bearing as `PIPELINE_CEILINGS`, and both exist because of
the same finding: **the pipeline's most durable fingerprint is not vocabulary or simile —
it is how it JOINS things.** Left alone it chains clauses on `and`. This author interrupts
himself with em-dashed appositives. On the book this was found in, three consecutive
chapters drafted at 35–45 `and` per 1,000 words against the author's 15–20, each on a brief
that carried the warning in writing. The conversion is free — a clause chained with `and`
becomes an interruption set off by em-dashes, same idea, same image, same order — and it is
now a mid-draft self-check in `book-writer.md` rather than a repair afterwards.

#### Calibrating a floor or ceiling — read this before setting one

Four separate thresholds on that book were once set **tighter than the author's own
measured range**, and every one of them pushed the prose *away* from his voice while
appearing to protect it. Two of the four were caught only after they had forced edits to
prose that was already right. The rules that came out of it:

1. **Measure the author with the gate's own tokenizer**, not a scratch script. Two
   reasonable implementations disagreed by a full point, which was enough to invert a
   verdict.
2. **Set the threshold AT the author's measured extreme, not inside it.** If his range is
   9.0–11.8, the ceiling is 12.0 and not 9.5.
3. **Measure the right text.** Breath was nearly gated on whole-chapter sentence length.
   Everyone's dialogue is short — this author's runs to a median of 6–10 words and puts up
   to 47% of its lines at six words or fewer — so a chapter with a big speaking cast reads
   "short" no matter who wrote it. The un-split gate would have told a writer to lengthen
   people's speech, which is the opposite of the fix. **Gate the narration; report the
   dialogue ratio and read it with a human eye** (that ratio is deliberately *not* gated —
   the author himself swings 0.44:1 to 1.16:1, so there is no band to defend).
4. **Density thresholds are unstable below ~2,500 words.** At 1,500 words two instances of
   anything score 1.33/1k. Check the raw count before cutting. The evaluator's Pattern #11
   clause now disapplies its density half below that length for exactly this reason.

`PUNCH_CHAPTERS` exempts a chapter the **outline** declares fragmented (log lines, white
space, short paragraphs) from the breath floors. The exemption must be earned in writing
*before* the chapter is drafted — it is never granted afterwards to a chapter that simply
failed, and a chapter listed there is recorded as *exempt and passing*, not as *in band*.

**The ALLOWLIST is per-book** and is the one pipeline file that is *not* shared — your
deliberate motifs are yours. It is also **a capped registry, not an exemption**:

> **The motif cap.** No signature narrative phrase may recur more than **3 times across a
> whole book**. Declaring a motif in the ALLOWLIST does *not* license unlimited use — it
> exempts the phrase from the generic repeat check while still holding it to the cap.
> Entries are `"phrase"` (cap 3) or `("phrase", N)` to raise the cap for a genuinely
> load-bearing image. Keep overrides rare and small. The gate fails if a motif exceeds its
> cap.

That rule exists because a motif is only a motif at low frequency. At the seventh use it
is a tic, and readers notice the shape of it before they notice the meaning.

### `grammar_check.py`

```bash
python3 books/<slug>/tools/grammar_check.py
python3 books/<slug>/tools/grammar_check.py --languagetool     # optional tier 2
```

**Tier 1 gates** (deterministic, near-zero false positives): doubled consecutive words
("the the", "Bella Bella"), space before punctuation, a/an mismatch. **Tier 1 reports**
(non-gating, needs judgement): the longest sentences per chapter, double spaces. **Tier 2**
(optional, never gates): tense/agreement/dangling-modifier scan via LanguageTool — an
assist, not an authority, because it is false-positive-prone on fiction dialogue.

### `voice_wear_check.py`

```bash
python3 books/<slug>/tools/voice_wear_check.py
```

Shipped with every new book. The Amelia Lesson made mechanical: three layers —
book-wide **retired phrases** (a hard gate; seeded with "never once"), **auto-detected
self-repetition per POV** (no configuration; it finds phrases a POV repeats across its own
chapters), and optional **named-device caps** per character. Multi-POV books get a
`feedback/pov-map.txt` (`chapter-N: Name` per line); single-POV books can skip it.

### Other per-book checkers

Books that needed them grew them; copy any into a book with the same problem:
`rhythm_check.py`, `tic_report.py`, `show_tell_check.py`, `metaphor_check.py`.

### The word floor

```bash
wc -w books/<slug>/manuscript/chapters/chapter-*.md
```

Gated on the **book total** against `manuscript_min_words`. There is deliberately **no
per-chapter floor** — a per-chapter minimum recreates the uniform 20 × 5,000-word shape
the architect works hard to avoid. `shortest_chapter_floor` is only a sanity check on the
shortest allowed chapter.

## Cross-model second opinions

The evaluator shares a model family with the writer, which makes it blind in exactly the
places the writer is.

```bash
bash tools/gemini_review.sh books/<slug>/manuscript/chapters/chapter-12.md
bash tools/grok_review.sh   books/<slug>/manuscript/chapters/chapter-12.md "focus on the middle sag"
```

Or the slash commands `/gemini-second-opinion` and `/grok-second-opinion`.

The editor persona and book briefing are **derived from the book** by
`tools/review_context.py`: it walks up to the nearest `STATE.yaml` and builds the context
from title, genre, premise, comps, series position and the settled guardrails (so the
outside model doesn't propose undoing decisions you already made). Override it per book by
writing `books/<slug>/review-context.md`, or per run with `REVIEW_CONTEXT="..."`.

Keys live **outside the repo**: `~/.gemini_env` / `~/.grok_env` (mode 600) or the
environment. Never commit them.

Treat the result as a second opinion, not an authority. Where two different models agree,
the finding is high-confidence. Where an outside model objects to something your canon
settled deliberately, note it and move on.

## APODICTIC

`tools/apodictic/` is a full developmental-editing plugin (enabled in `.claude/settings.json`)
that works at the manuscript level rather than the chapter level: structural diagnosis,
plot-architecture selection, specialized audits (scene, character architecture, emotional
craft, comedy, consent, interiority, shelf positioning), submission-readiness verdicts, and
a nonfiction argument engine. Start with `/apodictic:start`, which routes you in two or
three questions. Use it when a finished draft has a *structural* problem — the chapter loop
polishes chapters, and no amount of chapter polish fixes a spine.

## The running order

```bash
# per chapter, after the agent loop
python3 books/<slug>/tools/style_check.py
python3 books/<slug>/tools/grammar_check.py
python3 books/<slug>/tools/voice_wear_check.py   # whole-book; run periodically
git add -A && git commit -m "finalize chapter N"

# every 3-5 chapters
#   entity-tracker UPDATE, continuity-guardian audit

# at the end
wc -w books/<slug>/manuscript/chapters/chapter-*.md    # word floor
#   full-manuscript evaluation, then Phase 5 revision to floor 8.5 everywhere
```
