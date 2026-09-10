# Chapter 6 — BREATH repair #2 (narration median 13.5 → 14.5)

Revision 5. **Two joins. No words added, no words cut.** Punctuation and one
sentence boundary each; every idea, image, beat, object and line of dialogue reaches
the reader in the same order it did before.

## The defect

`style_check.py` flagged one line in the whole manuscript:

```
CEILING: BREATH narration median 13.5 < 14.0 (voice-match FLOOR — the pipeline writes shorter than this author)
```

Ch.6's narration ran 138 sentences at median 13.5 against an author floor of 14.0
(his Ch.1–5 narration runs 14.0–17.5). Nothing was introduced — the floor moved
when the metric stopped counting wholly-italic paragraphs as narration, and Ch.6's
prose was always a little shorter-breathed than his.

## The arithmetic (why two joins were enough)

With n=138 the median sits between the 69th and 70th shortest: `S[68]=13`, `S[69]=14`.
Joining two sentences that are **both at or below the median** into one that lands
**above** it removes two from the bottom and adds one to the top — it moves the median
twice as fast as lengthening a single sentence. Two such joins took n to 136 and the
median to `(14+15)/2 = 14.5`.

Both joins were chosen so that the resulting sentence lands **≥15w**. A join that lands
at exactly 14 sits at the bottom of the upper group and only gets the median to 14.0 —
see "Rejected" below.

## Join 1 — the leave paragraph (9w + 8w → 17w)

The author's own model in this chapter: an em-dashed qualifier that undercuts what
came before (*"It was good coffee — better than anything the program put in front of
him…"*). The two sentences here are already a setup and its undercut, punctuated as
though they were not.

**Before** (two sentences, 9w and 8w):
> He had expected that to be the difficult part. It had taken ninety seconds, and a signature.

**After** (one sentence, 17w):
> He had expected that to be the difficult part — it had taken ninety seconds, and a signature.

Cost: **1 em-dash.** No `and` added. The em-dash was the right instrument here and a
comma was not: `"…the difficult part, it had taken ninety seconds, and a signature"`
makes the closing `", and a signature"` read as a third item in a comma series rather
than as the appositive kick it is.

## Join 2 — the day room (9w + 7w → 16w)

Here the author's *other* long-sentence model applies: accumulation in commas with no
conjunction at all. The paragraph is already built that way two sentences later —
*"It was the middle of the afternoon, the light came across the tables in long bars, the
room was quiet like a waiting room is quiet."* The join simply extends the paragraph's
own rhythm one clause earlier.

**Before** (two sentences, 9w and 7w):
> A radio was on low at the far end. None of them was listening to it.

**After** (one sentence, 16w):
> A radio was on low at the far end, none of them was listening to it.

Cost: **nothing.** No em-dash, no `and`; one full stop becomes one comma.

An em-dash version of this join (`"…at the far end — none of them was listening to
it."`) was written, measured and then **backed out** — see below.

## Resulting metrics

| Ch.6 | before | after | gate |
|---|---|---|---|
| narration median | 13.5 ✗ | **14.5** ✓ | floor 14.0 (author 14.0–17.5) |
| narration sentences | 138 | 136 | — |
| narration ≥40w | 13.0% | **13.2%** ✓ | floor 13.0 — still thin, see Concerns |
| narration ≤6w | 24.6% | 25.0% ✓ | author 20.8–29.9% |
| em-dash | 46 (10.5/1k) | **47 (10.8/1k)** ✓ | ceiling 12.0 |
| `and` | 23.3/1k | **23.3/1k** (unchanged) ✓ | ceiling 24.0 |
| comma | 59.5/1k | 59.7/1k | — |
| simile | 2.1/1k | **2.1/1k** (unchanged) ✓ | floor 2.0 |
| words | 4372 | **4372** (unchanged) | — |

**Budget spent: 1 em-dash of ~6 available. 0 of the ~2 `and`s available.**
No comparison touched — simile stays at 2.1/1k, and `"like a man checking a table for
dust"` is left exactly as it was for the author to judge.

Gates: `style_check.py` **clean, no CEILING line anywhere in the manuscript**;
`grammar_check.py` **clean** (Ch.6's three LONG SENTENCE notes byte-identical to
before); `voice_wear_check.py` **clean**.

Chapters 1–5, 7, 8, 9: style report **byte-identical**, grammar report
**byte-identical**. `git diff --stat` = one file, three lines.

## Considered and rejected

**a) `"A radio was on low at the far end — none of them was listening to it."`**
This was the first version of Join 2, and it hit median 14.5 too. Backed out because
of what it did to the page rather than to the number: it puts an em-dashed sentence
immediately after another em-dashed sentence (*"…a woman doing a jigsaw alone at a card
table — the box lid propped against a chair leg…"*), and combined with Join 1 that gave
Ch.6 **two** adjacent-em-dash sentence pairs. The author does that **once in five
chapters** (Ch.1: *"…something larger than himself. Not command, not yet — just a seat
at the table…"*), and Ch.6 had none. One is his rate; two is a tic. The comma version
gets the same number for free and echoes the paragraph's own accumulation instead.

**b) `"The door was not locked, not one of them watched him down the corridor."`** (5w + 9w → 14w)
Idiomatically clean, costs no em-dash — but 14w lands at the *bottom* of the upper
group, so it only carried the median to **14.0**, zero margin above the floor. It also
flattens *"The door was not locked."*, which is doing deadpan work on its own after
Corwin's request about the letter. Reverted.

**c) `"The place had taken clippers to his hair, without much interest in the result —
he was in soft clothes, gray, the kind a person could sleep in."`**
Arithmetically fine (removes a 13 and a 14). Rejected: the preceding sentence in that
paragraph already ends on an em-dashed appositive (*"…until some of it came back — the
face had corners in it now…"*), so this is the same adjacency problem as (a); and the
comma-splice alternative stacks four commas in a row and goes muddy.

**d) Joining `"The man in the green coat had finished with the tree, moved down the row
to the next one."` to `"The woman with the jigsaw had found an edge piece."`**
Only moves the median by one step (it consumes an above-median sentence as well as a
below-median one), and it welds two separate things Vexx is watching into one
observation. Not worth it for half the effect.

**e) The standalone one-sentence paragraphs** — *"He went through the doors at the
end."*, *"He might have been reading out a manifest."*, *"Vexx put his cup down on the
table."*, *"It had come off a man who went back for it and missed."*, *"He heard it, a
beat after it was out of him."* All sit below the median and all are load-bearing
beats. Untouched.

**f) `"The trolley wheel squeaked at the far end…"`, the visitor-form opening, and the
closing exchange with the woman at the shelter.** Protected; not read for candidates.

## Concerns for re-evaluation

1. **`>=40w` is 13.2% against a floor of 13.0.** It was 13.0 — exactly on the floor —
   before this repair, and it only rose because n fell from 138 to 136. Two long
   narration sentences separated into short ones, anywhere in Ch.6, would put this
   under. It is the chapter's thinnest margin, not the median.
2. **Word-count header left at 4375.** Not a slip: no word was added or removed by
   this repair (`style_check` reports 4372 both before and after; alphanumeric-token
   count 4369 both before and after). The header's 4375 comes from an earlier counting
   method and is unchanged by these edits, so changing the number would have made it
   *less* accurate. Only the `Revision:` field was updated.
3. **`voice_wear_check.py` does not strip HTML comments.** The `<!-- Word count | Revision -->`
   headers feed the informational WARN list — that is where `[UNKNOWN] self-repeat:
   "word count revision voice match gloss"` and friends come from. Editing the Ch.6
   header re-sorted that WARN display and pushed one real ch.8/ch.9 prose phrase
   (`"s been the water since august"`, still present, 2× as before) off the bottom of
   the list's display cap. The gated result is unchanged and clean, and terser header
   wording lowered the Vexx-bucket noise from 123 to 119 phrases. Flagged as a
   pipeline observation only — **not fixed here** (it is a root-`tools/` question, not
   a Ch.6 one).
4. **Standing offence #5 (the tidying gesture, ×4)** — untouched and unchanged.
   Neither join is near a squaring/turning beat and nothing was added to the count.
