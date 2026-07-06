# book-pipeline — the single source of truth for the book-writing pipeline

This repo holds the **customized** book pipeline shared by every book repo
(The Saeren Chronicles, Pompei, The Gift, Death & Rememberance / Finding Lady
Death, and any future book). It is cloned into `~/.claude/` at the start of
every web session by the environment setup script, so **every** repo — including
brand-new books — gets the exact same pipeline with zero per-repo copying.

## What's in here (the canonical versions)

- `.claude/agents/` — the 12 customized `book-*` + skill agents
  (book-architect/writer/editor/evaluator/disruptor/researcher/orchestrator/
  packager, continuity-guardian, entity-tracker, dialogue-polish, hook-craft).
  **Customizations that live here and NOT upstream:** `maxTurns: 120` on all
  agents; the 4 skill-based agents (entity-tracker, continuity-guardian,
  dialogue-polish, hook-craft) with agent frontmatter; default model = Opus.
- `.claude/commands/` — `/gemini-second-opinion`, `/grok-second-opinion`.
- `.claude/hooks/` + `.claude/settings.json` — SessionStart deps + APODICTIC enablement.
- `tools/apodictic/` — the vendored APODICTIC structural-editing plugin.

## ⚖️ THE UPDATE RULE — READ EVERY SESSION (this is the whole point)

**This repo is the ONLY place the pipeline is edited. Improvements flow BACK here.**

Anytime the pipeline gets better, it must be committed **here** so every book
inherits it. Specifically — whenever you:

- **create a new book** (a new agent behavior, a new command, a new tool the
  pipeline should always have), OR
- **modify an agent/tool/command** to make it better (e.g. bump `maxTurns`, sharpen
  `book-writer`'s instructions, fix a gate script), OR
- **add an entry to a shared list** that improves results (a new anti-AI pattern,
  a new craft-mistake rule, a reusable motif convention, a new second-opinion model),

→ then **make that change in THIS repo and push to `main`**. Every book repo picks
it up on its next session. Do NOT hand-edit `~/.claude/` or a single book's
`.claude/` as the permanent home — that strands the improvement in one place
(exactly the problem this repo solves). If you tweak it live to test, mirror the
final version back here before ending the session.

### The ONE exception — per-book, stays per-book
`tools/style_check.py` **ALLOWLISTs** are book-specific (each book's deliberate
motifs differ). Those live in each book's own `book/genesis/<slug>/tools/style_check.py`,
seeded from `book/genesis/_template/`. Do NOT centralize those here. If you improve
the **template's** allowlist logic (structure, not a specific book's motifs), that
improvement goes to `_template` in the book repos.

## Starting a new book

- **Whole new repo:** `new-book-repo <slug> "<Title>"` (installed on PATH by the setup
  script; source is `new_book_repo.sh` here). Builds a complete standalone book repo on
  `main`, wired with the pipeline, ready to push. GitHub repo creation itself can't be
  automated from a session — create the empty repo, then the script pushes.
- **New book folder inside an existing multi-book repo:** that repo's `book/genesis/new_book.sh`.

## Structural-variety rule (baked into book-architect)

Books must NOT all converge on ~20 chapters of ~5,000 words in three visible acts with
turning points on the exact quarter-marks — that uniformity is a machine-made tell. The
architect now **evaluates each premise and SELECTS a macro-structure** (Section 0.5 of
`book-architect.md`): a menu of 3-act/4-act-kishōtenketsu/5-act/diptych/in-media-res/
mosaic/slow-burn/circular, with jittered turning points, chapter length/count that emerge
from content (not `word_target ÷ floor`), and no reflexive "ACT ONE/TWO/THREE" labels. If
you improve this logic, do it HERE so every future book inherits it.

## Workflow Law (same as every book repo)
Work only on `main`. No other branches, no PRs. Commit and push straight to `main`.

## How it's wired
The environment setup script (`setup-script.sh` in this repo, pasted into the web
Environment settings) clones this repo into `~/.claude/` every session. Update the
script only if the install mechanism changes; update **this repo** for everything else.
