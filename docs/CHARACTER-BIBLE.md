# The character bible

`books/<slug>/character-bible.md` — the canonical home for the cast's **voice and
distinctness**. One entry per named character, each ending in a DISTINCTNESS GUARANTEE.

This is the file that stops a thirty-chapter book with twenty named characters from
collapsing into one voice wearing different hats. It is also the file most likely to be
skipped, because a book seems fine without it right up until chapter nineteen, when three
characters have started sounding like the narrator and the fix is a manuscript-wide pass.

## The three canon files, and which one you want

| File | Holds | Question it answers |
|---|---|---|
| `ENTITY_STATE.yaml` | Facts: names, ages, places, objects, timeline, who-knows-what-when | "Was her coat green in chapter 4?" |
| `voice-dna.md` | The **narration's** voice + the cast-wide differentiation matrix and anti-pattern budget | "How does this book sound?" |
| `character-bible.md` | Each **character's** voice: worldview, syntax, evasion, physicality, tic | "Would Marek say this line?" |

They overlap on purpose but they are not substitutes. A continuity error is an
ENTITY_STATE problem; a character who sounds like everyone else is a character-bible
problem, and no amount of fact-checking catches it.

## Who writes it, and when

**The architect seeds it** during the voice dispatch (Phase 2.5), alongside `voice-dna.md`.
It is a **required deliverable**, not an optional extra — a missing bible means re-dispatch
the architect. It should cover, at minimum, the protagonist, the antagonist, and every
character who speaks in two or more scenes.

**The writer maintains it.** The moment a new named character appears on the page — even a
functional one — the writer adds their entry *before finalizing the chapter*. That timing
matters: written at introduction, the voice gets designed. Written retroactively at chapter
30, it gets described, and by then the drift has already happened.

**The evaluator audits against it.** A newcomer with no entry, or one whose tic duplicates
an existing character's, is a finding — and tic proliferation caps the Characters dimension
at 7.5 no matter how good the chapter otherwise is.

**The dialogue-polish pass writes from it**, running the cover-the-name test against the
cards.

## How distinctness actually works: the four axes

Distinctness is **not** "give everyone a verbal tic." A cast where everybody has a
catchphrase is the single most common way a large cast reads as machine-made. Characters
are separated on four axes, in roughly this order of power:

1. **Attention / worldview** — what they *notice*, and what they reduce the world to. The
   deepest differentiator by a distance. A carpenter, a priest and a thief walk into the
   same room and three different rooms come out.
2. **Syntax / register** — sentence shape and formality. Clips vs spirals; subordinate
   clauses vs fragments; questions vs statements.
3. **Evasion** — what they will *not* say. The subject, register or feeling they refuse.
   Silence characterizes harder than speech.
4. **Physicality / silence** — the body-tell or pause that stands in for a spoken tic.

A verbal tic is a fifth thing, rare and earned. Most characters should carry **none**.

## The TIC BUDGET (hard rule)

Recorded in the bible itself, designed up front:

- **≤2–3 characters in the whole book** may LEAD with a verbal tic, and each must be
  earned — the character's psychology surfacing, not decoration (a bookkeeper who numbers
  even his regrets). Name the roster explicitly.
- **No two characters share a DEVICE.** Counting, listing, pricing, rating, quantifying and
  cataloguing are *the same device in different coats* — one character each, at most. Write
  the one-device-per-character map into the bible.
- **No signature repeats across your other books.** The cross-book pattern rule: a tic that
  worked in the last novel is a fingerprint if it comes back in this one.
- **Watch for device bleed from the narrator.** The POV character's signature habit leaking
  onto secondary characters is the specific failure that makes everyone sound alike, and
  it is nearly invisible from inside a single chapter.

### The Amelia Lesson

Named after the book where it happened, and kept in the template so it doesn't happen
again: a quantifying/counting device and the phrase **"never once"** calcified into a tic,
then *bled across multiple characters* until the cast sounded alike — and fixing it needed
a manuscript-wide de-tic pass.

The lesson isn't "watch for that phrase." It's that voice tics **spread**, because each
chapter's writer imitates the voice they can see in the previous chapters, and a habit
repeated three times reads as intentional. So the bible carries a **retired / at-risk
phrase list** (seeded with "never once"), and `voice_wear_check.py` catches calcification
early. Prevention by construction, because detection at chapter 30 is already too late.

## The card format

```
#### MAREK VOSS — harbourmaster, Rieke's estranged brother
- Attention / worldview: reads people the way he reads weather — for what they are about
  to do, never for what they mean.
- Vocabulary band: dockside trade, tide tables, ship names; no abstractions he can't touch.
- Syntax fingerprint: clips. Two clauses maximum, then he stops. Never subordinates.
- Evasion — never says: anyone's name who has died. Substitutes "him", "her", "that one".
- Physicality / silence: turns his cup a quarter-turn before answering anything hard.
- Verbal tic: none — distinguished by evasion + clipped syntax.
- DISTINCTNESS GUARANTEE: the only character who refuses names, against Rieke, who uses
  them like handholds.
- Sample line: "Tide's wrong. Ask me tomorrow."
```

Then the cast-wide matrix, which is the cover-the-name test pre-solved:

| Character | Sharpest distinguisher | Contrast vs nearest character |
|---|---|---|
| Marek | refuses to say names | Rieke over-names everyone |

If any two characters share their sharpest marker, differentiate further **before** you
finish the bible. Solving it here costs a sentence; solving it in chapter 22 costs a pass
over every scene they share.

## The cover-the-name test

Take a page of dialogue, delete every speaker tag and name, hand it to someone. If they
can't tell who is speaking, the voices aren't distinct — regardless of how good the cards
look. `dialogue-polish` runs this on all speaking characters in a chapter; the evaluator
runs it as part of Dimension 3.

## Retrofitting a bible onto an existing manuscript

Common case: a draft exists (yours, or an earlier pipeline run) and there's no bible.

1. **Extract the facts first.** Run `entity-tracker` in BUILD mode over the manuscript to
   get `ENTITY_STATE.yaml` — you need the full cast list before you can audit voices.
2. **Sample each character's dialogue.** For every named speaker, pull their lines across
   the whole draft (`grep` on names is a blunt but effective start). You are looking for
   what they already do, not what you wish they did.
3. **Write the card from the evidence**, on the four axes. Where a character has no
   distinguishing voice yet, say so in the card — that's a revision target, not a failure.
4. **Audit for the collapse.** Count how many characters lead with a tic; look for two
   characters sharing a device; look for the narrator's device on secondary characters. In
   an unguided draft you will usually find at least one.
5. **Fix by subtraction first.** De-tic the bleed (remove the habit from everyone who
   borrowed it) before adding new distinguishing habits. Subtraction is safer: it can't
   introduce continuity problems, and an over-tic'd cast is nearly always the actual
   disease.
6. **Then let the evaluator re-score Dimension 3** and treat the delta as your check.

## Series

A returning character keeps their card. Copy it forward into the new book's bible and
evolve it deliberately — a book of grief should change a voice — but never re-invent it
from scratch, and never hand a returning character a tic they never had. Re-check the tic
budget against the *new* book's cast, since a new cast can quietly push you over the
≤2–3 ceiling. See [SERIES.md](SERIES.md).

## Common failure modes

| Symptom | What's actually wrong |
|---|---|
| Everyone sounds thoughtful and observant | The narrator's worldview has been given to the whole cast |
| Every character has a catchphrase | Tic budget ignored; distinctness outsourced to decoration |
| Two characters feel like one | Device collision — check the one-device map |
| Voices fine early, mushy after ch.20 | The bible stopped being updated at introduction time |
| A phrase that was striking now grates | Motif calcification — check the retired/at-risk list and the motif cap |
