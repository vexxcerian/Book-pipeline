# Progress — Valkyr: Book One

Scaffolded 2026-09-07 by `tools/new-book.sh` into `books/valkyr/valkyr-book-1/`.

## Where this stands

**The architect pass is done and the author's Ch.1–5 are promoted into the manuscript with all
three mechanical gates passing.** No chapter has been through `book-evaluator` yet, so nothing
carries a Genesis score. The pipeline has not written any prose.

| Artifact | State |
|---|---|
| `foundation.md` | ✅ 12,110w — characters, theme-as-question, anchors, motifs, opening strategy |
| `outline.md` | ✅ 19,665w — macro-structure + all 26 chapters |
| `voice-dna.md` | ✅ 4,228w — voice reverse-engineered from the author's own prose |
| `character-bible.md` | ✅ 8,357w — 22 entries, §TIC BUDGET, cover-the-name test run in-file |
| `voice-bank/` | ✅ README + 13 samples (4 breaking, 2 irrelevant-thought, 5 verbatim author prose) |
| `manuscript/chapters/` | ✅ Ch.1–5, **14,630 words** (`wc -w`), the author's italics restored |
| style / grammar / voice-wear | ✅ all three clean, calibrated to the author's measured voice |
| `feedback/pov-map.txt` | ✅ single POV, Vexx, Ch.1–5 |
| `ENTITY_STATE.yaml` | ⏳ being built by `entity-tracker` |
| Genesis scores | ❌ none — `book-evaluator` has not run on any chapter |

## The structure, in one paragraph

**Four-movement kishōtenketsu**, not three acts, as four titled Parts — INTEGRATION (Ch.1–2) /
ASSESSMENT (Ch.3–13) / RECLAMATION (Ch.14–19) / DISPOSITION (Ch.20–26), turning at 8 / 48 /
72%. Chosen because Book One's ending is a locked **non**-climax and kishōtenketsu is the one
common structure whose fourth movement is reconciliation rather than resolution. The author's
Act Three is **split, not altered** — the *ten* sits inside it. **Σ = 95,829 words**
(14,630 drafted + 81,200 new), chapters 1,400–6,800 (4.9× spread). Full reasoning is in the
`## Macro-Structure` block at the top of `outline.md` — read it before questioning the shape.

## What was decided on 2026-09-07 (all reversible — say so and it changes)

1. **AI-speech formatting: the author's convention, recovered not guessed.** The italics were
   pulled back out of the PDF's *font layer* (`DejaVuSerif-Italic`), so Rx and the AIs speak in
   unquoted italics exactly as written, and voices in the room keep their quotes. 233 italic
   runs restored. Paragraph breaks were rebuilt at the same time — the earlier staging copy had
   merged Rx's dialogue into the narration around it.
2. **The gates were calibrated to the author, not the author to the gates.** The strict
   ceilings exist to catch a *machine's* tells; several were firing on ordinary human phrasing.
   `tools/style_check.py` now has `AUTHOR_DRAFTED`/`AUTHOR_CEILINGS` and
   `tools/voice_wear_check.py` has `RETIRED_EXEMPTIONS` — **Ch.1–5 measured, Ch.6–26 stay
   strict.** Not one word of the author's prose was edited to pass a gate.
3. **`drafted_words` = 14,630**, by `wc -w`, the same tool the floor gate uses.

## Resume point — do these in order

1. **Decide how much Ch.2–5 get touched.** Ch.1 is LOCKED either way. They now pass the
   mechanical gates but have never seen `book-evaluator`. Recommended: (b) evaluate-only, and
   polish only what the evaluator flags.
2. **Finish `ENTITY_STATE.yaml`** if the entity-tracker run did not complete.
3. **Then the chapter loop from Ch.6:** write → dialogue-polish → hook-craft → disruptor →
   evaluate → quality gate. Commit per chapter.

## Worth the author's eye (passing, but notable)

- **Ch.2 is the densest chapter in the book** — simile 7.0/1k and em-dash 11.1/1k, both the
  highest of the five. It passes because the ceilings are set to the author's own range, but
  if any chapter would benefit from a trim, it is this one.
- **Ch.2, "never once"** — `"a man who had never once in his career been kept waiting"`. On the
  pipeline's retired list as a model crutch; kept because here it is doing real
  characterisation work. Declared explicitly in `RETIRED_EXEMPTIONS`, not silently excused.
- **"the first time since"** is allowlisted at a cap of 4 (its current count). Vexx dates
  everything from a grief landmark — the gray room, the empty casket, a folder full of nothing.
  Deliberate, and now capped so Ch.6–26 cannot help themselves to more of it.

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

- **`research/original-draft.md` is SUPERSEDED** — it is the staging copy, has no italics, and
  has coarser paragraph breaks. The live text is `manuscript/chapters/`. Edit the manuscript.
  The unmodified source is preserved at `research/valkyr-source.pdf`; check it before assuming
  anything about formatting.
- **The manuscript was machine-reconstructed from a PDF.** The words and the italics are the
  author's and were recovered from the font layer rather than guessed, but paragraph breaks
  were rebuilt by a line-length heuristic. They read correctly on inspection; a human proofread
  against the PDF is still worth one pass before this text is considered final.
- Comp titles in `STATE.yaml` are provisional; `book-researcher` has not run on this book.
- **Word counts: always use `wc -w`.** Python's `.split()` counts a standalone " — " as a word
  and `wc` does not, so on this em-dash-heavy prose the two differ by ~150 words over five
  chapters. The floor gate and `doctor.sh` both use `wc -w`; quote that figure and no other.
