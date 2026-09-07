# Documentation

Everything needed to run this book pipeline on your own books.

## Start here

| Doc | What it covers |
|---|---|
| **[GETTING-STARTED.md](GETTING-STARTED.md)** | Fork it, set the environment up, produce your first book. Read this first. |
| **[PIPELINE.md](PIPELINE.md)** | The 12 agents, the phases, the chapter loop, what every file is for. The reference. |
| **[CHARACTER-BIBLE.md](CHARACTER-BIBLE.md)** | How the cast stays distinct: voice cards, the four axes, the TIC BUDGET, retrofitting a bible onto an existing draft. |
| **[SERIES.md](SERIES.md)** | Multi-book series: the series bible, canon carry-over, voice continuity, the checklist when starting book N+1. |
| **[QUALITY-GATES.md](QUALITY-GATES.md)** | Every gate a chapter has to clear, the scoring system, the mechanical checkers, cross-model second opinions. |
| **[PUBLISHING.md](PUBLISHING.md)** | Manuscript → EPUB + print PDFs → IngramSpark. The file specs and the rejections we already ate. |
| **[WORKFLOW-AND-HOOKS.md](WORKFLOW-AND-HOOKS.md)** | The git workflow law, the hooks that enforce it, and how to turn it off in your fork. |
| **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** | The failures you will actually hit, and what they mean. |
| **[GLOSSARY.md](GLOSSARY.md)** | Genesis Score, CVI, Pattern #11, cover-the-name, the Amelia Lesson, and the rest of the vocabulary. |

## The short version

A book is a **folder** under `books/`. The **pipeline is shared** — one copy at the repo
root in `.claude/` and `tools/`, used by every book, improved in one place.

```
bash tools/install.sh                        # deps + agents (local; the web hook does this)
bash tools/doctor.sh                         # verify the checkout is ready
bash tools/new-book.sh my-book "My Book"     # scaffold
# stage source material in books/my-book/research/, fill STATE.yaml
# then, in Claude Code:
#   "Run the book-architect on books/my-book"
#   "Write chapter 1 of books/my-book"  → the chapter loop
python3 books/my-book/tools/style_check.py   # the mechanical gate
python3 tools/make_epub.py books/my-book     # the ebook
```

Three ideas carry most of the value, and they are worth understanding before you run
anything:

1. **The floor is the score.** A chapter is as good as its weakest dimension, not its
   average. Gates are set on the floor, so nothing hides behind a strong average.
2. **Prevention beats detection.** The anti-AI machinery (structural variety, the tic
   budget, the anti-pattern budget) is aimed at *not writing* the tells in the first
   place; the scanners are a backstop, not the plan.
3. **State lives in files, not in the conversation.** `STATE.yaml`, `ENTITY_STATE.yaml`,
   `character-bible.md`, `feedback/progress.md`. Any session can be resumed by any model
   from those files alone — which is the whole reason a 200k-word book is finishable.
