# Series Bible — <SERIES NAME>

> **What this is.** The canon shared by every book in this series: the world, the rules, the
> cast, the arc that spans the books, and the settled decisions no single book may contradict.
> A per-book `STATE.yaml`, `foundation.md`, and `character-bible.md` govern ONE book; this file
> governs all of them and outranks any of them on shared canon.
>
> **Who reads it.** Every agent working on any book in this series reads this FIRST — the
> architect before outlining, the writer before drafting, the continuity-guardian when auditing,
> the entity-tracker when reconciling. Point them at it via `series.bible` in the book's
> `STATE.yaml`.
>
> **Keep it current.** When a book LOCKS something that binds later books (a death, a rule, a
> renamed place, a revealed secret), record it here in the same commit. A series bible that
> lags the manuscript is how book three contradicts book one.

## The books

| # (pub order) | Folder | Title | Status |
|---|---|---|---|
| 1 | `<book-1-slug>/` | <Title> | Planned |

- **Publication order:** <book 1 → book 2 → …>
- **Chronological order:** <if it differs — prequels, framing devices — say so here>
- **Unifying antagonist / pressure:** <who or what spans the series>
- **Thematic spine:** <the question the whole series is asking>

## Series arc (the shape across books)

- **Book-level escalation ladder** — what changes in kind, not just degree, per book:
  - Book 1: <the terms of the story>
  - Book 2: <how the terms change>
- **What is answered when** — the promises made in book 1 and where each is paid off.
- **The ending the series is driving at** — write it down even if it moves. An unwritten
  destination is how a series sprawls.

## World rules (hard canon — never violate)

- **Magic / technology / power system:** <rules, and above all the COSTS>
- **Geography & travel times:** <distances that constrain plot>
- **Politics & factions:** <who holds power, who wants it>
- **Calendar / dating convention:** <how time is referred to on the page>

## Cast across books

Voice cards live in each book's `character-bible.md`. This section records only what is
SERIES-level: who returns, what they know, where a book leaves them.

| Character | Books | State at end of latest book | Knows | Notes |
|---|---|---|---|---|
| <Name> | 1– | <alive/where/what changed> | <secrets they hold> | <POV? tic-bearer?> |

**Voice carry-over rule.** A returning character keeps the voice card from the previous book.
Copy it forward into the new book's `character-bible.md` and evolve it deliberately (a book of
grief changes a voice); do NOT re-invent it from scratch, and do NOT let a new book hand them a
tic they never had.

## Naming & spelling registry (the boring file that saves the series)

One canonical spelling per name, place, title, and invented term. Every book checks against
this list; the continuity-guardian audits against it.

| Canonical | Also appears as (accepted) | Never |
|---|---|---|
| <Name> | <nickname, title> | <misspelling seen in drafts> |

## Settled decisions (with the date they were settled)

- YYYY-MM-DD — <decision, and what it forecloses>

## Open series-level questions (ask the author; do NOT invent)

- <question that affects more than one book>

## Continuity carry-over checklist (run when starting the NEXT book)

1. Copy the previous book's `character-bible.md` forward; prune characters who are gone,
   keep the returning cast's voice cards, re-check the TIC BUDGET across the NEW book.
2. Seed the new book's `ENTITY_STATE.yaml` from the previous book's final one (entity-tracker
   BUILD mode, with the previous file as input) so who-knows-what survives the book boundary.
3. Re-read this bible's **Cast across books** and **Settled decisions** — everything there is
   binding on the new outline.
4. Carry the ALLOWLIST forward in `tools/style_check.py` for motifs that are genuinely
   series-level — but re-apply the motif cap PER BOOK (a motif used three times in each of
   three books is fine; three times in one book is the ceiling).
5. Record the new book's row in **The books** table above before the architect runs.
