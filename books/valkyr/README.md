# Valkyr

A two-book military-SF conspiracy story set in the Halo universe, at the UNSC/ONI black-ops
tier. **Valkyr** is a program so classified it has no acknowledged existence, built to watch
the UNSC's own supersoldiers and to end them if the judgment comes back wrong. Vexx — a
Spartan who walked away — is pulled back into it by the only piece of his dead twin brother
that survived: Rx's mind, running as an AI who will bond with no one else. Vexx rebuilds the
program from the ground up, in good faith, under the command of **Richard Jameson** — the man
who murdered Rx personally and whose entire authority is built on having buried it.

**The spine:** what do you owe an institution that has already lied to you once, and what does
it cost to find out?

## The books

| # (pub order) | Folder | Title | Status |
|---|---|---|---|
| 1 | `valkyr-book-1/` | Valkyr: Book One (working title) | In progress — Ch.1–5 drafted by the author, architect pass done |
| 2 | — | Book Two (untitled) | Planned — outlined only in `SERIES-BIBLE.md` |

- **Publication order:** Book One → Book Two.
- **Chronological order:** the same. The founding incident sits four years before Book One and
  is told in fragments, never as a prequel volume.
- **Book One ends on suspicion, not revelation.** The confrontation with Jameson and the full
  memory unlock are Book Two's, and Book One may not reach them.

**Series bible (canon for every book):** `SERIES-BIBLE.md` — read it before touching any book
in this folder.

## Working in this series

Each book below is a full book project in its own right (`STATE.yaml`, `foundation.md`,
`outline.md`, `voice-dna.md`, `character-bible.md`, `manuscript/`, `tools/`) and uses the
shared root pipeline exactly like a standalone book does. The only additions are:

- every book's `STATE.yaml` carries a `series:` block pointing at `SERIES-BIBLE.md` and the
  previous book's folder;
- returning characters carry their voice cards forward instead of being re-invented;
- shared production tooling (cover compositor, `make_epub.py`, upload guide) can live at this
  series level rather than being copied into each book.

Full workflow: `docs/SERIES.md` at the repo root.
