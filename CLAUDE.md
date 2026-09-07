# CLAUDE.md — Book Pipeline

Guidance for Claude Code working in this repository. **Read this first, every session.**

> **Reference docs live in `docs/`** — [PIPELINE.md](docs/PIPELINE.md) (agents, phases, files),
> [CHARACTER-BIBLE.md](docs/CHARACTER-BIBLE.md) (cast voice + tic budget),
> [SERIES.md](docs/SERIES.md) (series canon carry-over),
> [QUALITY-GATES.md](docs/QUALITY-GATES.md) (scores, gates, checkers),
> [PUBLISHING.md](docs/PUBLISHING.md) (print/ebook/IngramSpark),
> [WORKFLOW-AND-HOOKS.md](docs/WORKFLOW-AND-HOOKS.md), [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md),
> [GLOSSARY.md](docs/GLOSSARY.md). This file is the session-start briefing; the docs are the
> detail. Keep both current — a doc that lags the pipeline is worse than no doc.

## What this repo is

**The book-writing pipeline, and the books written with it.** The shared pipeline lives at
the repo root; each book lives in its own folder under `books/`. There is exactly one copy
of the pipeline and every book uses it — no per-book duplication.

```
/                        ← repo root
├── .claude/             ← the pipeline: 12 book-* agents, /gemini + /grok, hooks, pipeline.conf
├── docs/                ← the reference documentation (see above)
├── tools/               ← shared tools: install.sh + doctor.sh, new-book.sh / new-series.sh,
│                           make_epub.py, make_noicc.sh, collect_completed.py, review scripts, apodictic
├── books/
│   ├── _template/       ← scaffold a new book copies from (NOT a book)
│   ├── _series-template/← scaffold a new SERIES copies from (NOT a series)
│   └── <name>/          ← one folder per book (or a series folder holding several)
└── requirements.txt
```

## ⚖️ BOOK FOLDER LAW — one book, one folder, every time

**Every book gets its own folder under `books/`, and that folder is created by the
scaffolder — never by hand.** No book content lives at the repo root, in `docs/`, in
`tools/`, or loose inside `books/`. This is not a convention; it is enforced.

```
bash tools/new-book.sh <slug> "<Book Title>"                                  # standalone
bash tools/new-book.sh <slug> "<Book Title>" --series <series> --position N   # inside a series
bash tools/new-series.sh <series-slug> "<Series Name>"                        # a new series first
```

**The moment a new book starts — a new idea, a pasted draft, an uploaded manuscript, a
sequel — the FIRST action is to scaffold its folder.** Source material is staged into
that folder's `research/`; it is never worked on where it landed.

**Enforced, not just documented** (while `BOOK_FOLDER_LAW=enforced` in `.claude/pipeline.conf`):
- A **PreToolUse** guard (`.claude/hooks/enforce-book-folder-law.sh`, deciding via
  `book_folder_law.py`) blocks any write of a book artifact — `STATE.yaml`,
  `foundation.md`, `outline.md`, `voice-dna.md`, `character-bible.md`,
  `ENTITY_STATE.yaml`, `premise.md`, `manuscript/chapters/chapter-*.md` — to a path
  outside `books/<slug>/`, and blocks hand-rolling a book folder with `mkdir`/`cp`
  instead of `new-book.sh`.
- `bash tools/doctor.sh` fails on a stray book artifact outside a book folder, and on a
  book folder that was not scaffolded from the template (missing gates, missing STATE).

Why it is a law: a book folder is not just tidiness — `new-book.sh` is what gives a book
its `STATE.yaml`, its three mechanical gates, its per-book `style_check.py` ALLOWLIST and
its `delivery/ebook.yaml`. A hand-made folder is missing the machinery the pipeline
assumes, and the failure shows up much later, at a gate that cannot run.

Exempt (shared pipeline, not book content): `.claude/`, `docs/`, `tools/`,
`books/_template/`, `books/_series-template/`.

## Git workflow

Default: **work only on `main`** — no other branches, no PRs. Manuscripts don't merge, so a
branch mostly creates ambiguity about which text is current. This is enforced by hooks that
read `WORKFLOW_LAW` in `.claude/pipeline.conf`; set it to `off` for a normal branch/PR
workflow, and update this section to match if you do.

Git identity: `git config user.email <you> && git config user.name <you>`

**Enforced, not just documented** (while `WORKFLOW_LAW=main-only`):
- The **SessionStart** hook (`.claude/hooks/session-start.sh`) detects a session that starts
  on a non-`main` branch, switches to `main` (carrying uncommitted work across via stash),
  and deletes the stray branch.
- A **PreToolUse** guard (`.claude/hooks/enforce-main-law.sh`) blocks any command that
  creates a branch or opens a PR before it can run.

## Health check

`bash tools/doctor.sh` verifies the environment, the pipeline files and every book folder
(placeholder STATE fields, missing character bible, a series block pointing at a bible that
does not exist, missing gates). Run it when something behaves oddly, and after pulling
pipeline changes. `bash tools/install.sh` is the local setup (the SessionStart hook covers
the web environment).

## Working on a book

1. **Pick the book folder** under `books/<name>/` (for a series, the specific book
   subfolder).
2. **Read its `STATE.yaml` first**, then `feedback/progress.md` (if present). STATE.yaml is
   the source of truth for that book's premise, canon, gates, and resume point.
3. Run the pipeline agents/commands against **paths inside that book folder**. The pipeline
   itself is shared from the root `.claude/` + `tools/` — never copy it in.
4. A book folder typically holds: `STATE.yaml`, `foundation.md`, `outline.md`,
   `voice-dna.md`, `character-bible.md`, `ENTITY_STATE.yaml`, `research/`,
   `manuscript/chapters/`, `evaluations/`, `feedback/`, `delivery/`, and a per-book
   `tools/style_check.py` (its ALLOWLIST is book-specific).
5. **`character-bible.md` is a required architect deliverable, and the Writer keeps it
   current** — a new named character gets an entry the moment they appear, and the TIC
   BUDGET (≤2–3 tic-bearers per book, no shared devices) is a hard ceiling. See
   [docs/CHARACTER-BIBLE.md](docs/CHARACTER-BIBLE.md).

## Starting a new book

**This is the ONLY way to start one** (see the BOOK FOLDER LAW above — the guard blocks
the alternatives):

```
bash tools/new-book.sh <slug> "<Book Title>"
```
→ creates `books/<slug>/` from `books/_template/`, ready for source material + the architect
pass. The new folder ships with all three mechanical gates (`style_check.py`,
`grammar_check.py`, `voice_wear_check.py`) and a `delivery/ebook.yaml` for
`tools/make_epub.py`.

For a book **inside a series**:
```
bash tools/new-book.sh <book-slug> "<Book Title>" --series <series-slug> --position N
```
→ creates `books/<series-slug>/<book-slug>/` and fills in its `STATE.yaml` `series:` block
(bible + previous book) so canon carries forward. A brand-new series starts with
`bash tools/new-series.sh <series-slug> "<Series Name>"`. Then run the carry-over checklist
at the bottom of the series bible — see [docs/SERIES.md](docs/SERIES.md).

## 🔧 Pipeline is shared — improvements flow to the root (THE UPDATE RULE)

The pipeline (the `book-*` agents, `/gemini` + `/grok`, APODICTIC) is edited in **one place:
this repo's root `.claude/` + `tools/`.** Every book already uses it directly.

**UPDATE RULE:** anytime you make the pipeline better — a new agent/tool, a tweak to an
agent/command/gate, or a better entry to a shared list (anti-AI pattern, craft-mistake rule,
structural-variety option) — edit it at the **root** and commit, so every book inherits it
immediately. Do NOT strand an improvement inside a single book's folder.

**The one exception — per-book, stays per-book:** each book's
`books/<name>/tools/style_check.py` **ALLOWLIST** is book-specific (deliberate motifs
differ). Those stay in the book folder, seeded from `books/_template/`. If you improve the
*template's* allowlist logic (structure, not a book's specific motifs), change
`books/_template/`.

## Structural-variety rule (baked into book-architect)

Books must NOT all converge on ~20 chapters of ~5,000 words in three visible acts with
turning points on the exact quarter-marks — that uniformity is a machine-made tell. The
architect **selects a macro-structure per premise** (Section 0.5 of `book-architect.md`).
Improve that logic at the root so every future book inherits it.

## How the pipeline is installed each session

In Claude Code on the web, `setup-script.sh` (pasted into the Environment's setup-script
field) installs the build toolchain, and `.claude/hooks/session-start.sh` installs the 12
agents into `~/.claude/agents` **from this repo's own `.claude/agents/`**
(`AGENT_SOURCE=repo` in `.claude/pipeline.conf`). Locally, `bash tools/install.sh` does both.

Remember that in web sessions only agents COMMITTED to `.claude/agents/` are dispatchable by
name — the agent registry is built from the clone before hooks run, so an edited agent takes
effect NEXT session.
