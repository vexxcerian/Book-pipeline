# Chapter 6 — breath repair (narration ≥40w share)

Single defect: the chapter was not reaching for the author's long accumulating sentence.
Narration ≥40w sat at **9.3% (14/150)** against a measured author floor of 11.5%
(his own Ch.1–5 range: 11.6–16.3%). Everything else in Ch.6 already passed.

Fix: **four joins**, punctuation and conjunction only. No idea, image, beat, object or line
of dialogue changed; no word added except lowercasing at the seams; one word removed (a
list conjunction). No dialogue paragraph touched. `git diff` on chapter-6.md is four lines.

## Result

| metric | before | after | requirement |
|---|---|---|---|
| narration ≥40w | 9.3% (14/150) | **12.4% (18/145)** | ≥11.5% — now mid-band |
| narration median | 13.0 | 13 | ≥13.0 |
| narration ≤6w | 24.0% | 24.1% | ≤33.0% |
| em-dash | 41 (9.5/1k) | 44 (10.1/1k) | 8.5–12.0/1k |
| "and" | 23.7/1k | **23.5/1k** | ≤24.0 — moved *down* |
| comma | 58.8/1k | 59.3/1k | ≥58.0 |

`style_check.py`: Ch.6 shows **no CEILING line at all**. Ch.1–5 and Ch.7 output byte-identical
to before. `grammar_check.py`: clean, Ch.6 still 0 errors / 2 long-sentence notes.
`voice_wear_check.py`: clean. Motif cap clean; no new repeated phrase.

## The four joins

Every join is the author's own idiom: an em-dashed self-interruption, or comma-accumulated
clauses with the conjunction *removed*. Three of the four spend one em-dash; one spends none.
Net conjunction change across all four: **−1 "and"**.

---

### 1. The mess-hall light (Ch.6 line 132) — 12w + 29w → **41w**, +1 em-dash, ±0 "and"

**Before**
> The light in the mess hall had been wrong for eleven hundred. It came in off to one side, the long kind, late in the day — and he had been calling it eleven hundred to himself for something over twenty years.

**After**
> The light in the mess hall had been wrong for eleven hundred — it came in off to one side, the long kind, late in the day — and he had been calling it eleven hundred to himself for something over twenty years.

The paired-dash interruption is the chapter's own most characteristic shape — it is the
coffee sentence and the gravy-smell sentence exactly: *statement — parenthetical accumulation —
and the turn.* The existing dash before "and he had been calling it" is the sting, and it
survives untouched; the new dash only stops the first clause standing alone. Note this is
the flash-memory correcting itself mid-breath, which is what the shape is for.

---

### 2. The room resuming after the realisation (line 200) — 11w + 17w + 38w → **66w**, ±0 em-dash, ±0 "and"

**Before**
> The trolley wheel squeaked at the far end of the room. The woman at the card table moved her chair a few inches, sat back down in it. The orchard smell came in through the crack in the window — cold, green, faintly of rot off the windfalls still lying in the grass — and the gardener straightened up, put a hand in the small of his back.

**After**
> The trolley wheel squeaked at the far end of the room, the woman at the card table moved her chair a few inches, sat back down in it, the orchard smell came in through the crack in the window — cold, green, faintly of rot off the windfalls still lying in the grass — and the gardener straightened up, put a hand in the small of his back.

The cheapest of the four (no punctuation bought at all — two full stops become commas) and,
I think, the one that reads best. This paragraph sits immediately after *It had come off a
man who went back for it and missed*, a run of one-line punches. As three sentences the room
comes back in ticks; as one it floods, which is what happens to a man who has just gone off
somewhere private and has to come back. Comma-accumulation across changing subjects is the
author's, verbatim: *"It was the middle of the afternoon, the light came across the tables in
long bars, the room was quiet like a waiting room is quiet."* 66w is inside this chapter's own
range (it already carries 69w and 72w narration sentences).

---

### 3. The drive, on the way out (line 260) — 6w + 36w → **41w**, +1 em-dash, **−1 "and"**

**Before**
> Outside, the light had barely moved. The saplings stood in their double row down the drive, with their stakes and their ties, the gate was open, and a bird was going at something in the leaf litter of the guard post step.

**After**
> Outside, the light had barely moved — the saplings stood in their double row down the drive, with their stakes and their ties, the gate was open, a bird was going at something in the leaf litter of the guard post step.

The one flagged in the brief, and it does move both metrics the right way at once: the
list-closing "and" goes, an em-dash arrives. The dash turns the whole drive into an
appositive of *the light had barely moved* — the place is unchanged, which is the point of
the beat (he has been inside for an afternoon and left a permanent line in a log, and the
gate is still just open).

---

### 4. The transit shelter (line 266) — 8w + 35w → **43w**, +1 em-dash, ±0 "and"

**Before**
> There were four other people in the shelter. One of them, an older woman with a shopping trolley parked against her knee, asked him whether the next one went straight through to the coast, or whether you had to change at the junction.

**After**
> There were four other people in the shelter — one of them, an older woman with a shopping trolley parked against her knee, asked him whether the next one went straight through to the coast, or whether you had to change at the junction.

Chosen deliberately as the last thing before the closing move. The chapter's final beat is a
misdirected answer to a stranger; lengthening the run-up makes the four-word swerve
(*"I don't know whether it went,"*) land harder. The closing line, its attribution, and the
two paragraphs after it are untouched.

## Considered and rejected

- **"He had pulled a man out of a jungle… / That was a real thing, a decent thing. / Vexx
  intended to do it."** (28+8+5 → 41w). Arithmetically ideal and idiomatic, but every version
  that read well needed a new "and" before *Vexx intended to do it*, and there is ~1 word of
  headroom on that metric. The conjunction-free rewrites (*"…a decent thing, one Vexx intended
  to do"*) cost the flat declarative, which is the sound of Vexx telling himself the pretext is
  clean immediately before *He also intended*. Left alone.
- **Voss: "She squared the folder of authorisations… — without appearing to have decided to."**
  (31w, would reach 53w joined to the sentence before it). This is the chapter's model sentence
  for the whole idiom; burying it in a longer breath dulls the undercut. Left alone.
- **"Vexx waited for the rest of it. / There was no rest of it. / She went back to her
  authorisations…"** (→41w). The join needs a colon or a third dash, and it costs the flat
  *There was no rest of it*, which is the dismissal landing. Left alone.
- **The list beat — "The food, which… / The orchard, which… / A dog that belonged to nobody…"**
  (→44w). In idiom as accumulation, but the fragments *are* the beat: small talk with the
  weight gone out of it. Joining them makes it sound composed. Left alone.
- **"Vexx sat with his hands on his knees. / He read nothing."** into the dried-fruit sentence
  (→46w). Would have destroyed a deliberate punch pair. Left alone.
- **The clinician's coffee-contract chatter** (12+6+27 → 45w). Workable, but it would have put
  a 45w sentence directly behind the 72w clinician sentence that opens the same paragraph —
  two long breaths back to back where the paragraph currently steps down. Left alone.

## Noticed and deliberately left alone

- **Header metadata is now stale by one word**: the comment reads `Word count: 4,340 | Revision: 1`;
  the chapter is 4,337 by `style_check`'s count (one "and" removed). I did not touch the header —
  out of scope for this repair. Someone should decide whether this counts as Revision 2.
- **`"vexx sat with his hands"` is flagged ×3 across chapters 6, 7 and 8** in the repeated-phrase
  block. Not a Ch.6 defect on its own — Ch.6 has the first instance — but it is at the motif cap
  and the next chapter to use it breaks the gate. Flagging for whoever holds Ch.7/8.
- **Ch.8 is currently failing** (`AND 41.6/1k`, `EM-DASH 8.0/1k`, `THE-WAY ×6`) and is being
  written by another agent; I did not open it. `git diff --stat` shows chapter-8.md modified by
  that agent, not by me — my diff is chapter-6.md only, 4 insertions / 4 deletions.
- Nothing committed.
