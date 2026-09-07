# Progress — Valkyr: Book One

Scaffolded 2026-09-07 by `tools/new-book.sh` into `books/valkyr/valkyr-book-1/`.

## Where this stands

**The architect pass is done. No prose has been written by the pipeline, and no chapter has
passed a quality gate.** `manuscript/chapters/` is empty on purpose — the author's five
drafted chapters are still sitting in `research/original-draft.md` awaiting a decision about
how much they get touched.

| Artifact | State |
|---|---|
| `foundation.md` | ✅ 12,110w — characters, theme-as-question, anchors, motifs, opening strategy |
| `outline.md` | ✅ 19,665w — macro-structure + all 26 chapters |
| `voice-dna.md` | ✅ 4,228w — voice reverse-engineered from the author's own prose |
| `character-bible.md` | ✅ 8,357w — 22 entries, §TIC BUDGET, cover-the-name test run in-file |
| `voice-bank/` | ✅ README + 13 samples (4 breaking, 2 irrelevant-thought, 5 verbatim author prose) |
| `ENTITY_STATE.yaml` | ❌ not built — run `entity-tracker` in BUILD mode before Ch.6 |
| `manuscript/chapters/` | ❌ empty |

## The structure, in one paragraph

**Four-movement kishōtenketsu**, not three acts, as four titled Parts — INTEGRATION (Ch.1–2) /
ASSESSMENT (Ch.3–13) / RECLAMATION (Ch.14–19) / DISPOSITION (Ch.20–26), turning at 8 / 48 /
72%. Chosen because Book One's ending is a locked **non**-climax and kishōtenketsu is the one
common structure whose fourth movement is reconciliation rather than resolution. The author's
Act Three is **split, not altered** — the *ten* sits inside it. **Σ = 95,829 words**
(14,629 drafted + 81,200 new), chapters 1,400–6,800 (4.9× spread). Full reasoning is in the
`## Macro-Structure` block at the top of `outline.md` — read it before questioning the shape.

## Resume point — do these in order

1. **Answer the blocking author decisions** (in `STATE.yaml` → `open_author_decisions`). Two
   of them gate drafting rather than delivery:
   - **AI-speech formatting.** The architect calls this load-bearing and it must be fixed
     before Ch.6 is written. Recommended: keep the author's split — quoted speech for voices
     in the air, italic-unquoted for the interface — which makes Rx typographically
     not-in-the-room.
   - **The em-dash / simile gate.** The author's prose runs 10.35 em-dashes per 1,000 words
     against a ~10/1k ceiling and 3.38 similes/1k against 4/1k. **That is the voice.** Raise
     the threshold or widen the ALLOWLIST; do not sand Ch.2–5 to fit a gate.
2. **Decide how much Ch.2–5 get touched.** Ch.1 is LOCKED either way. Recommended: (b)
   evaluate-only, and polish just what a gate flags.
3. **Promote Ch.1–5** from `research/original-draft.md` into `manuscript/chapters/`, then
   re-measure with `wc -w` and update `word_floor.drafted_words` (currently 14,629; `wc` on
   the research copy gives 14,768 — kept low deliberately so the budget carries margin).
4. **Add the new names to the series registry.** The architect introduced **Dessen, Merrick,
   Ives, Beck, Holst** and the place-name **Ashgrove**. They are not yet in
   `../SERIES-BIBLE.md`'s naming registry, and Ashgrove becomes series canon the moment Ch.20
   is drafted.
5. **Run `entity-tracker` in BUILD mode** over the drafted chapters + the bible to create
   `ENTITY_STATE.yaml` before new prose starts.
6. **Then the chapter loop from Ch.6:** write → dialogue-polish → hook-craft → disruptor →
   evaluate → quality gate. Commit per chapter.

## Things not to re-litigate

These are settled and the reasoning is written down; changing one means changing the outline.

- The kishōtenketsu structure and the four Part titles (`outline.md` §Macro-Structure).
- **The second cell** — the *ten*. Vexx's cell assesses; another disposes. Built from the
  locked "no contact between cells" rule; it is what retroactively converts the drafted
  Ch.3–5 from spent beats into evidence, and it is why Ch.1–5 do not need rewriting.
- **Ives dies** (cleared Ch.13, dead Ch.14) and **Reyes lives** (canon) — Reyes surviving is
  what makes the pattern legible.
- Stage-3 unlock lands in **Ch.13**. The "man I suspect is the man I report to" turn is
  **Ch.21**. The ending runs **Ch.24 → Ch.26**.
- **Jameson has no verbal tic, deliberately.** A catchphrase would make him legible, and a
  scene where the reader can see he is the villain is a failed scene.
- The donor-stock plant is **one Spector line in Ch.18**, marked `CUTTABLE-PLANT` inline.
  Nothing in Ch.19–26 depends on it.

## Known risks

- **The gates will fire on the author's own prose** the moment Ch.1–5 are promoted (em-dash
  and simile density, above). Expected; it is a calibration decision, not a defect.
- `research/original-draft.md` was rebuilt from the PDF's text layer. The words are the
  author's; **paragraph breaks are faithful but not byte-perfect and the original italics did
  not survive.** The PDF itself is preserved unmodified at `research/valkyr-source.pdf` —
  check it before assuming a formatting question.
- Comp titles in `STATE.yaml` are provisional; `book-researcher` has not run on this book.
