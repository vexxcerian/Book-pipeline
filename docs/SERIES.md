# Writing a series

The pipeline is book-shaped: agents work on one book folder at a time. A series works by
**convention plus carry-over** — a shared bible above the books, and a deliberate handoff
of canon when you start the next one. This layout has carried a completed 3-book trilogy
and a planned 4-book saga.

## Layout

```
books/emberfall/                    ← the series folder
├── SERIES-BIBLE.md                 ← canon shared by every book. Outranks any single book.
├── README.md                       ← the book table, pub vs chronological order, status
├── tools/                          ← optional: production tooling shared across the series
│                                     (cover compositor, make_epub.py, upload guide)
├── emberfall-book-1/               ← a complete book project
│   ├── STATE.yaml                  (with a series: block)
│   ├── character-bible.md
│   ├── ENTITY_STATE.yaml
│   └── manuscript/chapters/ …
├── emberfall-book-2/
└── emberfall-book-3/
```

Each book inside is a **full book project** and runs the standard pipeline unchanged. The
series folder adds canon above them and a place for tooling they share.

## Scaffolding

```bash
# create the series and its first book together
bash tools/new-series.sh emberfall "The Emberfall Cycle" emberfall-book-1 "A Crown of Cinders"

# later books
bash tools/new-book.sh emberfall-book-2 "A Vault of Ash" --series emberfall --position 2
```

`--series` puts the book inside the series folder and fills in its `STATE.yaml`:

```yaml
series:
  name: "The Emberfall Cycle"
  position: 2
  bible: "../SERIES-BIBLE.md"
  previous_book: "../emberfall-book-1"     # auto-detected from position
  carry_forward: [character-bible.md, ENTITY_STATE.yaml, voice-dna.md]
```

Every agent that reads `STATE.yaml` finds the bible and the previous book from there. The
cross-model review scripts pick it up too — a chapter of book 2 is reviewed as *book 2 of
a series*, not as a standalone opening.

## The series bible

`SERIES-BIBLE.md` is canon for every book in the folder, and outranks any single book's
files where they conflict. It holds:

- **The books** — publication order *and* chronological order when they differ (prequels
  published last are common, and they trip up every continuity check that assumes
  otherwise).
- **The series arc** — the escalation ladder book to book: what changes *in kind*, not just
  in degree. Plus which promises made in book 1 get paid off where.
- **World rules** — the magic/tech system and above all its **costs**, geography and travel
  times, factions, the calendar convention used on the page.
- **Cast across books** — who returns, what they know, where each book leaves them. Voice
  cards stay in the per-book bibles; this table is the series-level state.
- **The naming & spelling registry** — one canonical spelling per name, place and invented
  term, with accepted variants and known misspellings. Boring, and it saves the series.
- **Settled decisions**, dated.
- **Open series-level questions** — for the author, not for an agent to invent.

**Keep it current in the same commit as the book that changes it.** When book 2 kills a
character, renames a city, or reveals a rule, that lands in the bible immediately. A series
bible that lags the manuscript is exactly how book 3 contradicts book 1.

## Starting book N+1: the carry-over checklist

This is the part that has no automation and matters most. Run it before the architect
touches the new book.

1. **Character bible.** Copy the previous book's forward. Prune characters who are gone;
   keep returning characters' voice cards verbatim, then evolve them deliberately if the
   last book changed them. Re-check the **TIC BUDGET against the new cast** — a new book's
   newcomers can push you past the ≤2–3 tic-bearer ceiling even though each book looked
   fine alone.
2. **ENTITY_STATE.yaml.** Seed the new book's from the previous book's *final* state
   (`entity-tracker` BUILD mode with the old file as input). This is what preserves
   **who-knows-what across the book boundary** — the single hardest continuity problem in
   a series, because a character who learned a secret in book 1 chapter 30 must still know
   it in book 2 chapter 1, and must not know things the reader learned from another POV.
3. **Series bible.** Re-read **Cast across books** and **Settled decisions**. Everything
   there is binding on the new outline; the architect must read the bible before outlining.
4. **Voice.** Carry `voice-dna.md` forward as the starting point. The narration should
   still sound like the same series — but check whether a POV shift or a time skip warrants
   a deliberate change, and write down which it is. Drift is a bug; evolution is a decision.
5. **Style allowlist.** Carry forward genuinely series-level motifs into the new book's
   `tools/style_check.py` ALLOWLIST — but **the motif cap applies per book**. Three uses in
   each of three books is fine; three uses is still the ceiling *within* one book.
6. **The README table.** Add the new book's row with its status before the architect runs.

## What the architect does differently for a series entry

- Reads `SERIES-BIBLE.md` and the previous book's `character-bible.md` +
  `ENTITY_STATE.yaml` before the foundation.
- Builds the new book's arc **as a movement within the series ladder**, not as a fresh
  standalone arc — while still giving this book its own complete shape. Middle books fail
  when they are only a bridge.
- Picks a macro-structure that **contrasts with the previous book's**. Three books with the
  same shape is the series-scale version of the uniformity tell.
- Carries returning characters' voice cards forward instead of re-deriving them.

## Continuity auditing across books

`continuity-guardian` audits one manuscript. For series-level checks, point it at the
series bible explicitly and ask for a cross-book pass — it catches the categories that
matter here: timeline feasibility across the gap between books, information flow across
the boundary, plot threads opened in an earlier book with no scheduled payoff, and world
rules applied inconsistently between books.

The evaluator's **cross-book pattern detection** is the other half: it flags a signature
device, structure, or phrase repeating from your previous books. In a series that's a
judgement call — some repetition is continuity, some is fingerprint — but it should be a
decision, not an accident.

## Publishing a series

- Front matter carries an **"Also by"** page listing the series in order; update it in
  every book when a new one ships.
- Cover design should be visibly a set. Keep a shared cover compositor and wrap builder in
  the series folder's own `tools/` for exactly this reason — series-level tooling lives at
  the series level rather than being copied into each book.
- Each book gets its **own ISBNs** (print and ebook are separate ISBNs, per book).
- Spine width differs per book (it's a function of page count), so it is computed per book
  even when the cover template is shared.

See [PUBLISHING.md](PUBLISHING.md).
