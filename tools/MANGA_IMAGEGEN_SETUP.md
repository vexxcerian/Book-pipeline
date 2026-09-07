# Manga image generation — setup

The manga pipeline's **script + panel-YAML + character-sheet** steps run purely
in the text pipeline (no key needed). Only the final **drawing** step calls an
external image model. This is what to add to make that step work.

## 1. Get an image-model API key

`tools/manga_render.mjs` uses Google's Gemini image model
(`gemini-2.5-flash-image`, aka "nano-banana") — the same model the note.com
workflow uses.

- Create a key at Google AI Studio (https://aistudio.google.com/apikey).
- The key needs image-generation (Gemini API) access enabled on the project.

## 2. Make the key available (two options)

> **Status:** `GEMINI_API_KEY` has been added to the web **Environment** config
> (option A). It is present as an env var every session automatically — no
> per-session file needed. `manga_render.mjs` picks it up directly.

**A. Persistent (recommended for web sessions) — CONFIGURED.** The container is
ephemeral, so a key written to disk in one session is gone the next. Put it in
the web **Environment** config as an environment variable named `GEMINI_API_KEY`
(Environment → setup/secrets). Then it's present every session automatically.

**B. Per-session file.** Same convention as `tools/gemini_review.sh`:

```bash
printf 'GEMINI_API_KEY=YOUR_KEY_HERE\n' > ~/.gemini_env
chmod 600 ~/.gemini_env   # kept OUTSIDE the repo — never committed
```

`manga_render.mjs` reads the env var first, then `~/.gemini_env`.

## 3. Render

```bash
# a character reference sheet from a text prompt
node tools/manga_render.mjs \
  --prompt-file books/sygl-book/manga/prompts/char-bal.txt \
  --out books/sygl-book/manga/refs/bal.png --aspect 3:4

# a story panel, conditioned on the character sheet + a layout template
node tools/manga_render.mjs \
  --prompt-file books/sygl-book/manga/prompts/ch01-p01.txt \
  --ref books/sygl-book/manga/refs/bal.png \
  --ref books/sygl-book/manga/refs/amelia.png \
  --out books/sygl-book/manga/pages/ch01-p01.png --aspect 3:4
```

Passing character sheets as `--ref` images is what keeps a character looking
consistent panel-to-panel — the model conditions on them.

## Notes
- Do NOT commit the key. `~/.gemini_env` and env vars stay out of git.
- If you'd rather use a different image model, swap the endpoint/model in
  `tools/manga_render.mjs` — the script structure (text prompt + reference
  images → PNG) is model-agnostic.
