# Workflow and hooks

This repo ships with an opinionated git workflow, enforced by hooks rather than by good
intentions. It is **configurable** — if it isn't right for you, one line changes it.

## The default: main-only

**Work happens only on `main`. No other branches, no pull requests.** Everything commits
and pushes straight to `main`.

That is unusual for a code repo and deliberate for a prose one. A manuscript is not
mergeable: two people editing chapter 12 don't produce a resolvable diff, they produce two
chapter 12s. Branches fragment a book's history and make "what is the current text?"
ambiguous — which is the one question a writing project can never afford to be ambiguous
about. For a solo author, a branch is pure overhead.

It is enforced in two places:

- **`.claude/hooks/session-start.sh`** — a session that starts on a non-`main` branch is
  moved to `main` (uncommitted work carried across via stash) and the stray branch is
  deleted.
- **`.claude/hooks/enforce-main-law.sh`** — a `PreToolUse` guard that blocks branch
  creation (`git checkout -b`, `git switch -c`, `git branch <name>`) and pull requests
  (`gh pr create`, the `create_pull_request` MCP tool) before they run.

## Turning it off

In **`.claude/pipeline.conf`**:

```sh
WORKFLOW_LAW="off"      # normal branches and PRs; hooks stop policing git
```

Both hooks read that file. Nothing else in the pipeline depends on the setting — agents,
gates, tools and docs work identically either way.

**Turn it off if** more than one person works in the repo, you want review before changes
land, you're integrating with CI, or your host requires PR-based workflows. **Keep it on
if** you're a solo author who wants one linear history and no chance of a manuscript
existing in two states at once.

If you keep it on, also update the root `CLAUDE.md` — it states the law in prose, and the
model reads that file every session. Contradicting yourself between `CLAUDE.md` and
`pipeline.conf` is worse than either choice.

## `.claude/pipeline.conf` in full

| Setting | Values | Meaning |
|---|---|---|
| `WORKFLOW_LAW` | `main-only` (default) / `off` | Git enforcement, as above |
| `AGENT_SOURCE` | `repo` (default) / `upstream` | Where `~/.claude/agents` is installed from |
| `PIPELINE_MODEL` | model id, or empty | Default model for sub-agent dispatches |
| `PIPELINE_MAXTURNS` | integer (default 120) | Sub-agent turn budget |

**`AGENT_SOURCE=repo` keeps your fork self-contained** — the agents come from this repo's
own `.claude/agents/`, which carry every improvement made under the UPDATE RULE. Setting it
to `upstream` refetches the original Best Seller Studio project and *overwrites* the local
copies, dropping those improvements. Only use it if you're deliberately tracking upstream.

**`PIPELINE_MAXTURNS` defaults to 120 for a reason.** The upstream agents ship with 40,
which truncates a full chapter write-plus-gate-loop partway through — the agent stops
mid-revision and the chapter looks finished when it isn't.

## What the SessionStart hook does

Runs only in the remote (web) environment; local sessions skip it.

1. Enforces `WORKFLOW_LAW`.
2. Sets `ANTHROPIC_MODEL` so sub-agents don't silently drop to a smaller model.
3. Installs build dependencies: `reportlab` + `pillow`, Ghostscript, and
   `language-tool-python` (the ~250MB LanguageTool engine downloads lazily on first
   `--languagetool` use, not at session start).
4. Installs the 12 agents into `~/.claude/agents` and normalizes `maxTurns`.
5. Verifies both agent locations and reports what's missing.
6. Installs the Gemini CLI when a key is present.

### The agent-registry gotcha (web sessions)

**In Claude Code on the web, only agents COMMITTED to the repo's `.claude/agents/` are
dispatchable by name.** The agent registry is built from the clone at session start, *before*
hooks run — so anything the hook writes to `~/.claude/agents` is not dispatchable as
`subagent_type` until the next session.

The practical consequences:

- Commit agent changes. An edited agent takes effect **next session**, not this one.
- The hook deliberately does **not** copy `~/.claude/agents` back over the repo copies —
  that would leave every session starting with a dirty working tree.
- If you must run a modified agent in the current session, run a general-purpose agent and
  have it read the agent file and follow it directly.

## `setup-script.sh` and `tools/install.sh`

**`setup-script.sh`** is the environment-level installer for Claude Code on the web: paste
it into the environment's setup-script field. It runs before the session starts and installs
the Python dependencies plus Ghostscript. It deliberately does **not** install the agents —
those load from the repo clone, which is the only place they can be dispatched by name from.

It also ships with no personal content in it. It runs for every repo in your environment, so
it's a convenient place to install your own account-wide `~/.claude/CLAUDE.md`; there's a
commented placeholder at the bottom for exactly that. What goes in it is yours — a repo that
installs its author's standing instructions into everyone else's account is a bug, not a
feature.

**`tools/install.sh`** is the local equivalent, since the SessionStart hook only runs in the
remote environment. It installs `requirements.txt`, checks for Ghostscript, and copies the
agents into `~/.claude/agents` with `maxTurns` normalized. Re-run it after pulling pipeline
changes.

**`tools/doctor.sh`** verifies the result — dependencies, agents in both locations, hook
syntax, config, tools, templates, API keys, and each book's `STATE.yaml` (placeholder
fields, missing character bible, a series block pointing at a bible that doesn't exist). It
exits non-zero if anything required is missing, so it also works as a CI check.

## Git identity

```bash
git config user.email noreply@anthropic.com
git config user.name Claude
```

Set per your own preference in a fork — this is just what this repo uses so commits are
attributed consistently.

## Committing prose

- **Commit per chapter.** `git add -A && git commit -m "finalize chapter N"`. It is the
  only reliable undo a manuscript has, and it makes "when did this line change?" answerable.
- **Commit the state files with the prose that changed them** — `STATE.yaml`,
  `ENTITY_STATE.yaml`, `character-bible.md`, the series bible. A state file that lags the
  manuscript is how the next session starts from a false premise.
- **Don't commit API keys.** They live in `~/.gemini_env` / `~/.grok_env`, outside the repo.
- Large binaries (cover art, print PDFs) hit GitHub's 100MB per-file limit; use Git LFS if
  you get there.
