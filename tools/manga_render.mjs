#!/usr/bin/env node
// manga_render.mjs — render a manga panel (or character sheet) from a text
// prompt using Google's Gemini image model ("nano-banana"), optionally
// conditioning on reference images (character sheets / layout templates).
//
// This is the DRAWING step of the manga pipeline. Everything upstream (script,
// panel YAML, character sheets) is produced by the text pipeline; this turns an
// approved prompt into an actual PNG.
//
// Auth: reads GEMINI_API_KEY from the environment, else sources ~/.gemini_env
//       (mode 600, kept OUTSIDE the repo so it is never committed) — same
//       convention as tools/gemini_review.sh.
//
// Usage:
//   node tools/manga_render.mjs --prompt-file panel.txt --out panel-01.png \
//        [--ref character-bal.png] [--ref layout-6panel.png] \
//        [--model gemini-2.5-flash-image] [--aspect 3:4]
//   node tools/manga_render.mjs --prompt "Bal, one-handed, standing in..." --out sheet.png
//
// Exit codes: 0 ok, 1 usage/auth, 2 API error.

import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";

// ---- tiny arg parser ----
const args = process.argv.slice(2);
const opt = { ref: [] };
for (let i = 0; i < args.length; i++) {
  const a = args[i];
  const next = () => args[++i];
  if (a === "--prompt") opt.prompt = next();
  else if (a === "--prompt-file") opt.promptFile = next();
  else if (a === "--out") opt.out = next();
  else if (a === "--ref") opt.ref.push(next());
  else if (a === "--model") opt.model = next();
  else if (a === "--aspect") opt.aspect = next();
  else { console.error(`Unknown arg: ${a}`); process.exit(1); }
}

const model = opt.model || "gemini-2.5-flash-image";
if (!opt.out) { console.error("Missing --out <file.png>"); process.exit(1); }

let prompt = opt.prompt;
if (opt.promptFile) prompt = readFileSync(opt.promptFile, "utf8");
if (!prompt || !prompt.trim()) { console.error("Missing --prompt or --prompt-file"); process.exit(1); }
if (opt.aspect) prompt = `${prompt.trim()}\n\n[Aspect ratio: ${opt.aspect}]`;

// ---- load API key (env first, then out-of-repo file) ----
let key = process.env.GEMINI_API_KEY;
if (!key) {
  const envFile = join(homedir(), ".gemini_env");
  if (existsSync(envFile)) {
    const m = readFileSync(envFile, "utf8").match(/GEMINI_API_KEY\s*=\s*["']?([^"'\n]+)/);
    if (m) key = m[1].trim();
  }
}
if (!key) {
  console.error("GEMINI_API_KEY not set. Add it to the environment or ~/.gemini_env (mode 600).");
  process.exit(1);
}

// ---- build request parts: text prompt + optional inline reference images ----
const parts = [{ text: prompt }];
const mimeFor = (p) => p.toLowerCase().endsWith(".jpg") || p.toLowerCase().endsWith(".jpeg")
  ? "image/jpeg" : "image/png";
for (const r of opt.ref) {
  if (!existsSync(r)) { console.error(`Reference image not found: ${r}`); process.exit(1); }
  parts.push({ inline_data: { mime_type: mimeFor(r), data: readFileSync(r).toString("base64") } });
}

const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`;

const res = await fetch(url, {
  method: "POST",
  headers: { "Content-Type": "application/json", "x-goog-api-key": key },
  body: JSON.stringify({ contents: [{ parts }] }),
});

if (!res.ok) {
  console.error(`Gemini API error ${res.status}: ${await res.text()}`);
  process.exit(2);
}

const data = await res.json();
const outParts = data?.candidates?.[0]?.content?.parts || [];
const img = outParts.find((p) => p.inline_data?.data || p.inlineData?.data);
if (!img) {
  console.error("No image returned. Raw response:\n" + JSON.stringify(data, null, 2).slice(0, 2000));
  process.exit(2);
}
const b64 = img.inline_data?.data || img.inlineData?.data;
writeFileSync(opt.out, Buffer.from(b64, "base64"));
console.log(`Wrote ${opt.out} (${model}${opt.ref.length ? `, ${opt.ref.length} ref img` : ""})`);
