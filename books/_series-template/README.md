# <SERIES NAME>

<One or two sentences: what the series is, the world, the unifying antagonist, the spine.>

## The books

| # (pub order) | Folder | Title | Status |
|---|---|---|---|
| 1 | `<book-1-slug>/` | <Title> | Planned |

- **Publication order:** <…>
- **Chronological order:** <if different from publication order>

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
