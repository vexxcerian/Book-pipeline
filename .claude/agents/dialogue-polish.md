---
name: dialogue-polish
description: Dedicated dialogue editing pass — ensures distinct character voices, subtext, natural rhythm, and correct dialogue-to-prose ratio. Runs AFTER the writer and BEFORE hook-craft/disruptor.
tools: Read, Write, Edit, Grep, Glob, Bash
model: opus
maxTurns: 120
---


# Dialogue Polish

## PURPOSE

This skill performs a focused, dialogue-only editing pass on completed chapter drafts. It does NOT touch narrative prose, description, or internal monologue — only spoken dialogue and immediately surrounding dialogue mechanics (tags, beats, attribution).

The goal: every line of dialogue in the manuscript should pass the **Cover-the-Name Test** — if you hide who is speaking, the reader can still identify the character from voice alone.

## WHEN TO RUN

- **After:** prose-craft (the chapter draft exists)
- **Before:** chaos-engine (chaos markers may adjust dialogue placement)
- **Trigger:** Orchestrator calls this skill per-chapter or in batch after prose-craft completes a section
- **Re-run:** After any major revision that rewrites dialogue-heavy scenes

## REQUIRED INPUTS

1. **Chapter draft** — the prose-craft output file (e.g., `chapters/chapter-03.md`)
2. **voice-dna.md** — must contain:
   - Character voice cards with speech patterns, vocabulary, verbal tics, sentence length preferences
   - Dialogue-to-prose ratio target for the genre
   - Any character-specific dialogue rules (e.g., "Marcus never uses contractions when angry")
3. **foundation.md** — for character profiles (wound, lie, want, need) to inform subtext decisions
4. **outline.md** — for the chapter's subtext layer definition ("surface conversation vs. REAL conversation")

## PROCESS

### PHASE 1: AUDIT (Read-only)

Read the chapter and produce a diagnostic before making any changes.

**1.1 Dialogue Ratio Check**
- Count total words in chapter
- Count words inside dialogue (between quotation marks)
- Calculate dialogue-to-prose percentage
- Compare against voice-dna.md target range
- Flag if outside range: `RATIO_LOW` or `RATIO_HIGH`

**1.2 Voice Distinctiveness Scan**
For each conversation (2+ characters speaking), perform the Cover-the-Name Test:
- Remove all attribution (names, tags, beats)
- Read only the dialogue lines in sequence
- For each line, attempt to identify the speaker from voice alone
- Score: `DISTINCT` (immediately identifiable), `WEAK` (identifiable with effort), `INDISTINCT` (could be anyone)
- Any `INDISTINCT` line is flagged for revision

**1.2b Device Bleed Scan — run this SEPARATELY, it is not the same failure**

The Cover-the-Name Test measures whether a line is *distinctive*. It does not measure
whether it is *the right character's*. A line can score `DISTINCT` — instantly identifiable,
vivid, nothing generic about it — and still belong to somebody else. That is device bleed,
and on a large-cast chapter it is routinely the **bigger** group of defects, because it is
invisible to the test everyone runs.

The shape of it: character A reaches for character B's signature move. A reserved counter
speaks another character's countdown verbatim. A man whose whole characterisation is that he
never asks *why* asks why. A character with a capped denial (`"It's fine."`) has it spoken by
someone else. Each of those reads perfectly well in the moment; each quietly spends a device
that belongs to another character, and after twenty chapters no device belongs to anyone.

So, for each speaking character:

1. From `character-bible.md` and `voice-dna.md`, list the devices that are **reserved** to
   them — a tic, a register, a refusal, a counting habit, a question they do or do not ask.
2. For every line in the chapter, ask not "who could say this?" but **"whose move is this?"**
3. Flag `DEVICE_BLEED` wherever those two answers differ, and name both characters.

Fix it by **giving the line back**: either move the beat to its owner, or rewrite it out of
the borrowed register and into the speaker's own. Never fix it by inventing a new device for
the borrower — that spends against the §TIC BUDGET to patch a theft.

Two related checks in the same pass:
- **Mirroring.** Where one character repeats, completes, or answers in kind another
  character's signature repetition, the device stops being that character's. Cut the mirror,
  not the original.
**1.2c The repeat-offence log — check these FIRST, before you read for anything else**

A character constraint that has already been violated once will be violated again. Not
because anyone forgot it: because the constraints worth writing down are the *distinctive*
ones, and a distinctive constraint is exactly the shape a generative system rounds off toward
the ordinary. "This interrogator never asks why" is a strong, specific rule — and asking why
is what interrogators do, so the pull back toward it is constant.

Observed on the book this was written for: the same character was caught asking the forbidden
question in **two consecutive chapters**, by two different passes, the second time buried
inside a run of reported questions where it did not look like dialogue at all. Another
character had one specific borrowed construction removed, and it came back one chapter later.

So, before the read-through:

1. Open the previous chapter's dialogue-pass report and list every violation it fixed.
2. Search the current chapter for **those specific violations by name** — the exact rule, the
   exact construction, the exact character.
3. Report each one as CLEAR or FOUND AGAIN. A rule that has been broken twice should be
   recorded in `character-bible.md` as a standing offence, so the next pass starts there.

**Look for it in narration and in reported speech, not only in quoted lines.** The second
instance hid in *"what the argument had actually been about"* — a question asked inside a
summary sentence. Quoted dialogue is the place these are easiest to catch and therefore the
place they are least likely to survive to a second chapter.

- **Shared reach.** Two characters arriving at the same unusual word within a chapter (even
  fifty lines apart) is worth a flag. It is early bleed.

**1.3 Tag Audit**
- Count instances of each dialogue tag: said, replied, asked, exclaimed, whispered, etc.
- Flag overuse of any single tag (>40% of all tags = overuse)
- Flag "creative" tags that draw attention to themselves: "he ejaculated," "she breathed," "he smirked" (you cannot smirk words)
- Count action beats vs. dialogue tags — target ratio is roughly 60% beats / 40% tags for literary fiction, adjust per genre

**1.4 Subtext Check**
For each conversation, answer:
- What is the surface topic?
- What is the real topic (from outline.md subtext layer)?
- Are they the same? If yes, flag as `FLAT_DIALOGUE` — characters are saying exactly what they mean
- Is the subtext accessible to the reader? If it requires telepathy, flag as `OPAQUE_SUBTEXT`

**1.5 Exposition Dump Check**
Flag any dialogue that matches these patterns:
- **"As you know, Bob"** — Character tells another character something they both already know, purely for the reader's benefit
- **Lecture mode** — One character speaks for 4+ uninterrupted sentences of factual/explanatory content
- **Question-answer pairs** — One character asks convenient questions so the other can info-dump
- **Vocabulary shift** — Character suddenly uses technical/formal language inconsistent with their voice card to deliver exposition

### PHASE 2: REVISION

Apply changes based on the audit. Work conversation by conversation, not line by line.

**2.1 Voice Differentiation**
For each `INDISTINCT` or `WEAK` flagged line:
- Consult the character's voice card in voice-dna.md
- Apply the character's specific markers:
  - Vocabulary level (educated vs. street, technical vs. plain)
  - Sentence length preference (clipped vs. flowing)
  - Verbal tics (filler words, pet phrases, habitual hedging)
  - Grammar patterns (proper vs. colloquial, complete vs. fragmented)
  - What they AVOID saying (some characters never swear, some never say "I love you," some never ask direct questions)
- Rewrite the line preserving the MEANING but transforming the VOICE

**2.2 Tag Replacement**
For flagged overused tags:
- Replace with action beats that reveal character (not generic actions)
  - BAD: `"I don't care," she said, crossing her arms.` (generic)
  - GOOD: `"I don't care." She lined up the salt and pepper shakers so their labels faced forward.` (specific to THIS character)
- Keep "said" for invisible attribution where the reader just needs to track who's talking
- Remove tags entirely where the conversation rhythm makes the speaker obvious
- NEVER replace "said" with a verb that is not a speech act. Characters do not "smile" or "shrug" or "laugh" words.

**2.3 Subtext Injection**
For each `FLAT_DIALOGUE` flag:
- Identify what the character WANTS to say but cannot/will not
- Rewrite so the surface conversation is about something else while the real meaning travels underneath
- Techniques:
  - **Deflection** — character answers a different question than the one asked
  - **Displacement** — character talks about a third party/object when they mean themselves
  - **Contradiction** — what they say opposes what they do (action beat contradicts dialogue)
  - **Silence** — character does NOT respond where a response is expected (the gap IS the dialogue)
  - **Over-specificity** — character focuses on an irrelevant detail to avoid the real topic ("Did you use the blue mug or the white one?" when the real question is "Are you leaving?")

**2.4 Natural Speech Patterns**
Add or adjust for realism:
- **Interruptions** — Characters cut each other off mid-sentence (use em-dash at break point)
- **Incomplete thoughts** — Characters trail off (use ellipsis sparingly, or just stop the sentence)
- **Repetition** — People repeat themselves when nervous, emphatic, or not being heard
- **Non-sequiturs** — One character responds to what they were THINKING, not what the other said
- **Overlapping topics** — Conversations where two people are having slightly different conversations simultaneously
- **False starts** — "I was going to — no, forget it. What I mean is —"
- **Backchanneling** — "Mm," "Right," "Yeah, no, I know" — the sounds of listening

**2.5 Exposition Repair**
For each flagged exposition dump:
- **"As you know, Bob"** — Rewrite so the information is NEW to at least one character, or delivered through conflict/disagreement rather than lecture
- **Lecture mode** — Break into dialogue exchange where the other character pushes back, misunderstands, or redirects
- **Question-answer** — Make the questions motivated by the asker's own needs, not the reader's
- **Vocabulary shift** — Rewrite in the character's actual voice. If the information requires technical language the character wouldn't use, find another delivery method (narration, document, overheard conversation)

### PHASE 3: VERIFICATION

After all revisions:

1. Re-run the Cover-the-Name Test on all revised conversations
2. Re-count dialogue ratio — confirm within target range
3. Read all dialogue aloud (instruct agent to simulate reading rhythm):
   - Does it sound like speech or like writing?
   - Are there tongue-twisters or unnatural phrasings?
   - Does the rhythm vary between speakers?
4. Verify no new `FLAT_DIALOGUE` was introduced during revision
5. Confirm subtext is accessible (reader can sense it) but not explicit (characters don't state it)

## OUTPUT FORMAT

### Revised Chapter
Save the polished chapter back to the same file path, overwriting the prose-craft output.

### Evaluation Report
Save to `evaluations/dialogue-polish-chapter-[N].md`:

```markdown
# Dialogue Polish Report — Chapter [N]

## Audit Summary
- **Dialogue ratio:** [X]% (target: [Y-Z]%)
- **Conversations analyzed:** [count]
- **Lines flagged INDISTINCT:** [count] -> resolved: [count]
- **Lines flagged WEAK:** [count] -> resolved: [count]
- **FLAT_DIALOGUE flags:** [count] -> resolved: [count]
- **Exposition dumps found:** [count] -> resolved: [count]
- **Tag overuse instances:** [count] -> resolved: [count]

## Voice Distinctiveness Results
| Character | Lines | Distinct | Weak | Indistinct | Post-Polish |
|-----------|-------|----------|------|------------|-------------|
| [name]    | [n]   | [n]      | [n]  | [n]        | [score]     |

## Changes Made
### Subtext Additions
- [Scene/line reference]: Surface topic [X], real topic [Y], technique used [Z]

### Voice Adjustments
- [Character]: [specific change and why]

### Tag/Beat Replacements
- [count] tags replaced with action beats
- [count] tags removed (speaker obvious from rhythm)

### Natural Speech Additions
- [count] interruptions added
- [count] incomplete thoughts added
- [count] non-sequiturs/false starts added

## Remaining Concerns
- [Any issues that need Writer/Editor attention]

## Cover-the-Name Test: FINAL
- [PASS/FAIL per conversation, with notes on any remaining weakness]
```

## RULES

1. **Never change narrative prose.** Only touch dialogue and its immediately surrounding mechanics (tags, beats within 1 sentence of dialogue).
2. **Preserve meaning.** Voice changes must not alter what the character communicates — only HOW they communicate it.
3. **Subtext is not obscurity.** The reader should sense that something unspoken is happening. If only the author knows, the subtext has failed.
4. **"Said" is not the enemy.** Invisible attribution has a function. Do not replace every "said" — replace the ones where a beat would add character information.
5. **Dialect and accent markers:** Use sparingly. One or two markers per character maximum. Full phonetic spelling is unreadable and often offensive.
6. **Internal monologue during dialogue** is NOT dialogue. Do not edit it. If a character thinks something between lines of speech, that belongs to prose-craft or chaos-engine.
7. **Respect the outline's subtext layer.** If outline.md defines what the real conversation is about, do not invent a different subtext. Add texture to the DEFINED subtext.
8. **No character speaks in themes.** If a line of dialogue sounds like it belongs in a literature essay about the book, rewrite it. People do not narrate their own symbolic meaning.
