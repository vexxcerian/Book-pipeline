#!/usr/bin/env python3
"""
Cross-manuscript style checker (per-book copy — edit ALLOWLIST for THIS book).

Catches the three things the per-chapter agents can miss across the whole book:
  1. VERBAL TICS         — overused filler/crutch words (just, suddenly, seemed, somehow...)
  2. REPEATED PHRASES    — distinctive 4-6 word n-grams reused within or across chapters
  3. METAPHOR/SIMILE LOAD — simile markers per 1,000 words vs a ceiling

Also reports adverb (-ly) density and em-dash density per chapter.

Usage:
    python3 tools/style_check.py                 # scan manuscript/chapters/chapter-*.md
    python3 tools/style_check.py --max-simile 4  # set simile-per-1k ceiling (default 4)

Exit code is non-zero if any chapter breaches a ceiling or any cross-chapter
repeated phrase is found — so it can gate the pipeline.
"""
import argparse, glob, os, re, sys
from collections import Counter, defaultdict

# Crutch words / verbal tics to watch (lowercase, whole-word).
TIC_WORDS = [
    "just", "suddenly", "somehow", "seemed", "slightly", "simply", "really",
    "very", "almost", "perhaps", "actually", "felt like", "a beat",
    "for a moment", "for a long moment", "something like", "as if", "as though",
]
# Distinctive fingerprints flagged in a PIPELINE session log to keep rare. These are
# constructions the MODEL over-reaches for — not defects in ordinary English. Several
# ("the kind of", "not because") are common human phrasing, so a hand-written chapter
# will trip them innocently: give those chapters an allowance via
# AUTHOR_CEILINGS["fingerprint"] rather than editing an author's prose to satisfy this.
FINGERPRINT_PHRASES = [
    "there and gone", "the kind of", "not because", "deep water",
    "like water", "drew in", "made herself a smaller target",
]
SIMILE_MARKERS = re.compile(r"\b(like|as if|as though)\b", re.I)
ADVERB = re.compile(r"\b\w+ly\b", re.I)
WORD = re.compile(r"[a-z']+", re.I)

# Deliberate recurring motifs / canon terminology — NOT accidental reuse.
# Deliberate recurring motifs / canon terms — a CAPPED registry, not an exemption.
# An allowlisted phrase is ignored by the generic n-gram repeat check, BUT it is still
# held to a hard book-wide occurrence cap (author's standing rule: no signature narrative
# tic-phrase may recur more than MOTIF_CAP_DEFAULT times across the whole book — declaring
# a motif does NOT license unlimited use). Entries may be:
#   "phrase"            -> capped at MOTIF_CAP_DEFAULT
#   ("phrase", N)       -> capped at N (raise ONLY for a genuinely load-bearing image;
#                          e.g. a finale cosmology motif). Keep overrides rare and small.
MOTIF_CAP_DEFAULT = 3
ALLOWLIST = [
    # Canon terminology — these are the book's nouns, not accidental reuse.
    ("the choosing", 12),
    ("hostile contact", 8),
    # Deliberate epithets for characters the reader is not yet allowed to name. The
    # unnamed recruiter IS "the man in civilian dress" for the length of Ch.1; that is
    # characterisation of an institution, not a repeated phrase.
    ("the man in civilian dress", 6),
    # Rx's condition, described the same way on purpose each time the reader meets it.
    ("flattened, processed, running through speakers", 4),
    # The book's stated motif (foundation.md): grief as a phantom limb / an outline with
    # nothing in it. Load-bearing and deliberately recurrent.
    ("an outline with nothing in it", 3),
    # Vexx dates everything from a grief landmark — "the gray room", "the empty casket",
    # "a folder full of nothing". That construction is the book's emotional clock, not
    # accidental reuse (foundation.md names the casket and the gray room as anchors).
    # Capped at its current 4 uses: the motif is the author's, and Ch.6-26 may not simply
    # help themselves to more of it.
    ("the first time since", 4),
]

# --- AUTHOR-DRAFTED CHAPTERS (per-book) --------------------------------------
# Several ceilings below exist to catch a MACHINE's tells: em-dash spray, the
# "the way [x]" explanatory tic, simile reaching. A human author's SIGNATURE use of
# the same construction is not that defect, and sanding it out to satisfy a gate
# damages the book — the gate is supposed to protect the voice, not flatten it.
#
# So: list the chapters the author wrote by hand, and give them the ceilings that
# author's voice actually sits at (measure first — do not guess). Chapters the
# PIPELINE writes stay on the strict defaults, which is where the anti-AI value is.
# Leave AUTHOR_DRAFTED empty for a book with no hand-written chapters.
# Ch.1-5 are the AUTHOR's own prose, promoted from research/original-draft.md.
# Ch.1 is LOCKED as the voice benchmark (STATE.yaml: chapter_1_locked). The ceilings
# below are MEASURED from that prose, not guessed, and exist so the gate stops
# demanding that the author's voice be sanded down to a machine-tell threshold:
#
#   em-dash   8.9-11.0/1k across Ch.1-5  -> ceiling 12.0/1k
#   simile    2.5-6.8/1k  (Ch.2 is the outlier at 6.8 — the roster chapter)
#   "the way" 5-9 per chapter — the author's signature explanatory construction
#
# Ceilings for the PIPELINE-written chapters (6-26), below. Deliberately a shade tighter
# than the author's own measured range: the pipeline may REACH his voice, not exceed it.
# "fingerprint" is deliberately absent, so those phrases stay on the strict default of 1
# — Ch.6 cleared it without needing the allowance, so the tighter setting stands until a
# chapter genuinely needs "the kind of" twice.
# VOICE-MATCH FLOORS — the counterpart to the ceilings, and the half that is easy to forget.
# A ceiling stops the pipeline EXCEEDING the author. A floor stops it falling SHORT of him.
# That second failure is the one that actually happens: a writer told "do not exceed 9.5
# em-dashes per 1,000 words" scores a safe 4.7 and produces prose that is calm where the
# author is nervous. No single chapter looks wrong; twenty of them are a second author.
# Set these from the author's measured range too. Empty = no floor (right for a book with no
# hand-written benchmark to match).
# Measured across the author's Ch.1-5. These are FLOORS for the pipeline chapters: the rhythm
# the prose has to REACH, not merely stay under. Ch.6 shipped at em-dash 4.7/1k, "and" 40.4/1k,
# commas 45.8/1k — five of seven rhythm metrics outside the author's entire range, all in the
# same direction, describing one habit: the pipeline CHAINS clauses on "and" where this author
# INTERRUPTS himself with em-dashed appositives. No sentence was wrong. Twenty chapters of it
# would be a second author, and no single chapter would be blamed.
#
#   em-dash  author 9.0-11.7/1k  -> floor 8.5   (a shade under his lowest chapter)
#   commas   author 65.9-77.9/1k -> floor 58.0
#   BREATH, over the author's NARRATION ONLY in Ch.1-5, measured with THIS FILE'S OWN
#   sentences()+words() — not with a scratch script and not over the whole chapter.
#   Both of those shortcuts were tried and both produced wrong thresholds; see below.
#     narration median  13 - 18      -> floor 13.0
#     narration <=6w    20.0 - 32.6% -> ceiling 33.0%
#     narration >=40w   11.6 - 16.3% -> floor 11.5%
#   Set AT his measured extremes, not inside them. Three separate thresholds in this file
#   were once set tighter than the author's own range, and every one of them pushed the
#   prose AWAY from his voice while appearing to protect it. Do not make it four.
PIPELINE_FLOORS = {
    "emdash_per1k": 8.5,
    "comma_per1k": 58.0,
    "median_sentence": 13.0,
    "long_sentence_pct": 11.5,
}
# The author's own chapters are the benchmark; they are never gated against themselves.
AUTHOR_FLOORS = {}

# BREATH — sentence length distribution. The third layer of the same problem.
#
# The connective metrics catch a pipeline that JOINS differently from the author. They do
# not catch one that BREATHES differently. Ch.6 and Ch.7 both sat inside the em-dash and
# "and" bands after calibration and were still built out of sentences a third shorter than
# the author's, because the short declarative is what a model reaches for when it is being
# careful.
#
# MEASURE THE NARRATION, NOT THE CHAPTER. This was calibration mistake #4 in this file,
# caught before it shipped rather than after. On a whole-chapter measurement Ch.6 and Ch.8
# looked catastrophic (medians of 8 and 7 against an author minimum of 10) and the obvious
# reading was "the pipeline writes short". It was almost entirely an artefact of how much
# DIALOGUE each chapter carries: Ch.8 runs 201 spoken lines to 149 of narration, more than
# any chapter the author wrote, and everyone's dialogue is short. Split the registers and
# Ch.8's narration comes back at median 12 / >=40w 18.8% — one point under his floor on
# one metric and ABOVE his whole range on another. A gate built on the un-split number
# would have sent a writer off to lengthen people's speech.
#
# What survives the split is small and specific, and it points in OPPOSITE directions in
# the two chapters: Ch.6 hits the median but under-reaches on the long sentence (>=40w
# 9.3% vs his 11.6% floor), while Ch.8 over-reaches on it (18.8%) and sits a point light
# on the median. That is not one habit. Treat each chapter on its own number.
#
# The dialogue:narration ratio is REPORTED and deliberately not gated — the author himself
# swings from 0.44:1 to 1.16:1, so there is no defensible band. Read it with a human eye.
#
# PUNCH_CHAPTERS is the single exemption, and the exemption must be EARNED IN THE OUTLINE
# before the chapter is written, never granted afterwards to a chapter that simply failed.
PUNCH_CHAPTERS = {7}    # Ch.7: outline declares "Fragmented. Log lines and white space."

PIPELINE_CEILINGS = {
    "simile_per1k": 5.0,
    # 12.0, not 9.5. The author measures 9.0-11.8/1k across his five chapters, so a 9.5
    # ceiling capped the pipeline BELOW his own practice in three of them, and combined with
    # the 8.5 floor it left a corridor 1.0 wide against his 2.8-wide spread — Ch.7 could
    # neither add nor drop a single em-dash without failing. THIRD instance of the same
    # mistake in this file: a threshold set tighter than the author's measured range pushes
    # the prose AWAY from his voice while appearing to protect it. Bracket his range; do not
    # squeeze it.
    "emdash_per1k": 12.0,
    "adverb_per1k": 20.0,
    "theway": 5,
    "and_per1k": 24.0,      # the chaining habit — author runs 15.4-18.6/1k
    # MEASURED WITH THIS GATE'S OWN REGEX (which counts someone/no one/anybody/anyone too):
    # the author runs 4.03-6.13/1k. An earlier 3.5 was taken from the evaluator's narrower
    # somebody+nobody figure (0.5-2.6) and applied to a six-term regex — a ceiling stricter
    # than the author himself, which forced edits to his dialogue to satisfy it. Derive a
    # threshold from the SAME measurement the gate makes, never from a differently-defined one.
    "vague_per1k": 6.5,
    "short_sentence_pct": 33.0,   # <=6-word NARRATION sentences, %
}

AUTHOR_DRAFTED = {1, 2, 3, 4, 5}
AUTHOR_CEILINGS = {
    "simile_per1k": 7.0,
    "emdash_per1k": 12.0,       # density, not absolute — chapters run 1,900-4,000 words
    "theway": 9,
    # "the kind of" x6 / "not because" x4 are this author's ordinary phrasing, not the
    # model reaching for a crutch. Ch.6-26 stay on the strict default of 1.
    "fingerprint": 6,
}


def _ceiling(n, key, default):
    """The ceiling for chapter n.

    Author-drafted chapters answer to AUTHOR_CEILINGS (what the author measurably does);
    every other chapter answers to PIPELINE_CEILINGS (what the pipeline is allowed to do,
    normally a little tighter). Anything unset falls through to the generic default.
    """
    if n in AUTHOR_DRAFTED:
        if key in AUTHOR_CEILINGS:
            return AUTHOR_CEILINGS[key]
    elif key in PIPELINE_CEILINGS:
        return PIPELINE_CEILINGS[key]
    return default


def _floor(n, key):
    """The floor for chapter n, or None. Mirrors _ceiling."""
    if n in AUTHOR_DRAFTED:
        return AUTHOR_FLOORS.get(key)
    return PIPELINE_FLOORS.get(key)


def _motif_caps(default):
    """Normalize ALLOWLIST into {phrase_lower: cap} and a list of allow-substrings."""
    caps = {}
    for e in ALLOWLIST:
        if isinstance(e, (tuple, list)):
            caps[str(e[0]).lower()] = int(e[1])
        else:
            caps[str(e).lower()] = default
    return caps

# n-gram repetition settings
NGRAM_MIN, NGRAM_MAX = 4, 6
# stopword-only n-grams are noise; require at least this many "content" words
STOP = set("the a an and or but of to in on at for with as is was were be been "
           "her his its their my your she he it they i you we him them me "
           "that this there here what when which who whom had have has do did does "
           "not no so if then than out up down off over into about back "
           "don't didn't wasn't isn't hasn't hadn't couldn't wouldn't shouldn't "
           "won't aren't weren't doesn't can't it's i'm i'd i'll he'd she'd they'd "
           "you're we're they're he's she's".split())


def sentences(text):
    """Split into sentences with ONE consistent tokenizer.

    Absolute accuracy matters less than consistency: every BREATH threshold in this file
    was calibrated by running THIS function over the author's own chapters. Change the
    splitter and you must re-measure the author before trusting the numbers again.
    """
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"^\s*\*\s*\*\s*\*\s*$", " ", text, flags=re.M)   # scene breaks
    text = re.sub(r"^#.*$", " ", text, flags=re.M)                      # headings
    parts = re.split(r"(?<=[.!?])[\"'\u201d\u2019]?\s+", text)
    return [p for p in (x.strip() for x in parts) if len(words(p)) >= 2]


def split_registers(text):
    """Separate spoken lines from narration.

    A paragraph that OPENS with a quotation mark is a line of dialogue; everything else is
    narration. Crude, and right often enough: it is the paragraph shape a reader sees.

    This split is the whole point of the BREATH block. Measured across the whole chapter,
    sentence length says almost nothing, because dialogue is short in every writer alive —
    this author's own dialogue runs to a median of 6-10 words and puts up to 47% of its
    lines at six words or fewer. A chapter with a big speaking cast therefore reads
    "short" on a whole-chapter median no matter who wrote it, and a gate built on that
    number would send a writer off to lengthen people's speech, which is the opposite of
    the fix. Gate the narration; report the dialogue ratio and let a human read it.
    """
    paras = [p.strip() for p in text.split("\n") if p.strip()]
    is_dia = lambda p: p.startswith("\u201c") or p.startswith('"')
    return ("\n\n".join(p for p in paras if is_dia(p)),
            "\n\n".join(p for p in paras if not is_dia(p)))


def words(text):
    # Normalize the typographic apostrophe first. Without this, WORD splits "don't"
    # into "don" + "t", and the n-gram repeat check then floods with function-word
    # strings ("you don t have to", "i m not going to") that are not repetition at all.
    text = text.replace("\u2019", "'").replace("\u02bc", "'")
    return [w.lower() for w in WORD.findall(text)]


def ngrams(toks, n):
    return [tuple(toks[i:i+n]) for i in range(len(toks)-n+1)]


def content_rich(ng):
    return sum(1 for w in ng if w not in STOP) >= max(2, len(ng)-2)


def scan():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="manuscript/chapters")
    ap.add_argument("--max-simile", type=float, default=4.0,
                    help="simile markers per 1,000 words ceiling")
    ap.add_argument("--max-adverb", type=float, default=20.0,
                    help="-ly adverbs per 1,000 words ceiling")
    ap.add_argument("--tic-ratio", type=float, default=6.0,
                    help="per-1,000-words ceiling for any single tic word")
    ap.add_argument("--max-emdash", type=int, default=4,
                    help="ABSOLUTE em-dashes allowed per chapter (AI tell — keep near zero)")
    ap.add_argument("--max-emdash-per1k", type=float, default=None,
                    help="em-dashes per 1,000 words ceiling. When set (here or via "
                         "AUTHOR_CEILINGS) it REPLACES the absolute count for that chapter — "
                         "fairer across chapters whose lengths vary widely by design")
    ap.add_argument("--max-theway", type=int, default=2,
                    help="ABSOLUTE 'the way [x]' explanatory tic per chapter (pipeline "
                         "fingerprint — HARD CAP 2, and stagger: aim 0-1 in alternating chapters)")
    ap.add_argument("--max-fingerprint", type=int, default=1,
                    help="occurrences of a FINGERPRINT_PHRASES entry allowed per chapter "
                         "before it is flagged (author-drafted chapters can raise this via "
                         "AUTHOR_CEILINGS['fingerprint'])")
    ap.add_argument("--motif-cap", type=int, default=MOTIF_CAP_DEFAULT,
                    help="book-wide occurrence cap for any ALLOWLIST motif (author rule: "
                         "no signature tic-phrase recurs more than this; per-entry (phrase,N) overrides)")
    args = ap.parse_args()
    motif_caps = _motif_caps(args.motif_cap)

    base = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(base)
    chap_dir = os.path.join(root, args.dir)
    files = sorted(glob.glob(os.path.join(chap_dir, "chapter-*.md")),
                   key=lambda p: int(re.search(r"chapter-(\d+)", p).group(1)))
    if not files:
        print("no chapter files found in", chap_dir); return 1

    problems = 0
    phrase_chapters = defaultdict(set)   # ngram -> {chapter numbers}
    phrase_counts = Counter()
    motif_book_counts = Counter()        # motif phrase -> book-wide raw occurrences
    motif_chapters = defaultdict(set)    # motif phrase -> {chapter numbers it appears in}

    print("=" * 70)
    print("PER-CHAPTER STYLE REPORT")
    print("=" * 70)
    for f in files:
        n = int(re.search(r"chapter-(\d+)", f).group(1))
        text = open(f, encoding="utf-8").read()
        text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)  # ignore editorial comments
        toks = words(text)
        wc = len(toks) or 1
        per1k = lambda c: round(c / wc * 1000, 1)

        # Connective habit — how a voice JOINS things. A writer who chains on "and" and a
        # writer who interrupts himself with em-dashed appositives can score identically on
        # every ceiling above and still read as two different people.
        ands = len(re.findall(r"\band\b", text, re.I))
        commas = text.count(",")
        vague = len(re.findall(r"\b(?:somebody|someone|nobody|no one|anybody|anyone)\b", text, re.I))

        similes = len(SIMILE_MARKERS.findall(text))
        adverbs = len(ADVERB.findall(text))
        emdash = text.count("—")

        sim1k, adv1k, em1k = per1k(similes), per1k(adverbs), per1k(emdash)
        max_simile = _ceiling(n, "simile_per1k", args.max_simile)
        max_adverb = _ceiling(n, "adverb_per1k", args.max_adverb)
        max_em1k = _ceiling(n, "emdash_per1k", args.max_emdash_per1k)
        flags = []
        if sim1k > max_simile:
            flags.append(f"SIMILE {sim1k}/1k > {max_simile}"); problems += 1
        if adv1k > max_adverb:
            flags.append(f"ADVERB {adv1k}/1k > {max_adverb}"); problems += 1
        if max_em1k is not None:
            if em1k > max_em1k:
                flags.append(f"EM-DASH {em1k}/1k > {max_em1k} ({emdash} in chapter)"); problems += 1
        elif emdash > args.max_emdash:
            flags.append(f"EM-DASH {emdash}/chapter > {args.max_emdash} (density {em1k}/1k)"); problems += 1

        and1k, comma1k, vague1k = per1k(ands), per1k(commas), per1k(vague)
        for key, val, label in (("and_per1k", and1k, "AND"),
                                ("comma_per1k", comma1k, "COMMA"),
                                ("vague_per1k", vague1k, "SOMEBODY/NOBODY")):
            hi = _ceiling(n, key, None)
            lo = _floor(n, key)
            if hi is not None and val > hi:
                flags.append(f"{label} {val}/1k > {hi}"); problems += 1
            if lo is not None and val < lo:
                flags.append(f"{label} {val}/1k < {lo} (voice-match FLOOR)"); problems += 1
        em_lo = _floor(n, "emdash_per1k")
        if em_lo is not None and em1k < em_lo:
            flags.append(f"EM-DASH {em1k}/1k < {em_lo} (voice-match FLOOR — the pipeline is "
                         f"chaining where this author interrupts himself)"); problems += 1

        # BREATH — sentence-length distribution of the NARRATION (see split_registers).
        dia_text, nar_text = split_registers(text)
        nar = sorted(len(words(x)) for x in sentences(nar_text)) or [0]
        ndia = len(sentences(dia_text))
        mid = len(nar) // 2
        median_s = nar[mid] if len(nar) % 2 else (nar[mid-1] + nar[mid]) / 2
        long_pct = round(100 * sum(1 for L in nar if L >= 40) / len(nar), 1)
        short_pct = round(100 * sum(1 for L in nar if L <= 6) / len(nar), 1)
        breath = (f"      breath (narration): {len(nar)} sentences | median {median_s} | "
                  f">=40w {long_pct}% | <=6w {short_pct}% | dialogue lines {ndia} "
                  f"({round(ndia/len(nar), 2)}:1)")
        if n in PUNCH_CHAPTERS:
            breath += "  [PUNCH — exempt]"
        else:
            lo = _floor(n, "median_sentence")
            if lo is not None and median_s < lo:
                flags.append(f"BREATH narration median {median_s} < {lo} (voice-match FLOOR "
                             f"— the pipeline writes shorter than this author)"); problems += 1
            hi = _ceiling(n, "short_sentence_pct", None)
            if hi is not None and short_pct > hi:
                flags.append(f"BREATH narration <=6w {short_pct}% > {hi}% (over-using the "
                             f"short declarative)"); problems += 1
            lo = _floor(n, "long_sentence_pct")
            if lo is not None and long_pct < lo:
                flags.append(f"BREATH narration >=40w {long_pct}% < {lo}% (voice-match FLOOR "
                             f"— not reaching for the long accumulating mode)"); problems += 1

        low = text.lower()
        for phrase in motif_caps:
            c = low.count(phrase)
            if c:
                motif_book_counts[phrase] += c
                motif_chapters[phrase].add(n)
        theway = len(re.findall(r"\bthe (?:same )?way\b", low))
        max_theway = _ceiling(n, "theway", args.max_theway)
        if theway > max_theway:
            flags.append(f"THE-WAY ×{theway}/chapter > {max_theway} (pipeline fingerprint)"); problems += 1

        tic_hits = []
        for t in TIC_WORDS:
            c = len(re.findall(r"\b"+re.escape(t)+r"\b", low))
            if c and per1k(c) > args.tic_ratio:
                tic_hits.append(f"{t}×{c} ({per1k(c)}/1k)"); problems += 1
        max_fp = _ceiling(n, "fingerprint", args.max_fingerprint)
        fp_hits = [f"'{p}'×{low.count(p)}" for p in FINGERPRINT_PHRASES
                   if low.count(p) > max_fp]

        print(f"\nCh{n:>2}  {wc} words | simile {sim1k}/1k | adverb {adv1k}/1k | em-dash {emdash} ({per1k(emdash)}/1k)")
        print(f"      rhythm: and {and1k}/1k | comma {comma1k}/1k | somebody/nobody {vague1k}/1k")
        print(breath)
        if flags:    print("   CEILING:", "; ".join(flags))
        if tic_hits: print("   TICS:   ", "; ".join(tic_hits))
        if fp_hits:  print("   FINGERPRINTS:", "; ".join(fp_hits)); problems += len(fp_hits)

        # collect n-grams for cross-chapter repetition
        for nlen in range(NGRAM_MIN, NGRAM_MAX+1):
            for ng in ngrams(toks, nlen):
                if content_rich(ng):
                    phrase_counts[ng] += 1
                    phrase_chapters[ng].add(n)

    print("\n" + "=" * 70)
    print("REPEATED PHRASES (4-6 words, content-rich)")
    print("=" * 70)
    # A repeat is only DISTINCTIVE (and therefore a gate failure) when the phrase
    # is long enough to be a real signature AND it recurs strongly:
    #   >= 5 words  AND  (used 3+ times overall OR spread across 3+ chapters).
    # Shorter / x2 generic n-grams are common in any prose — report them as
    # informational context only; they do not fail the gate.
    def distinctive(ng, cnt, chs):
        return len(ng) >= 5 and (cnt >= 3 or len(chs) >= 3)

    candidates = [(ng, phrase_counts[ng], sorted(phrase_chapters[ng]))
                  for ng in phrase_counts
                  if (len(phrase_chapters[ng]) >= 2 or phrase_counts[ng] >= 3)]
    # prefer longer / more-repeated phrases, drop ones fully contained in a flagged longer one
    candidates.sort(key=lambda x: (-len(x[0]), -x[1]))
    shown_flag, shown_info = [], []
    for ng, cnt, chs in candidates:
        s = " ".join(ng)
        # declared motifs are exempt from the GENERIC repeat flag (they are deliberate),
        # but they are separately held to the book-wide cap below.
        if any(allowed in s or s in allowed for allowed in motif_caps):
            continue
        scope = f"chapters {chs}" if len(chs) >= 2 else f"chapter {chs[0]}"
        if distinctive(ng, cnt, chs):
            if any(s in bigger for bigger in shown_flag):
                continue
            shown_flag.append(s)
            print(f"  FLAG ×{cnt}  [{scope}]  \"{s}\"")
            problems += 1
        else:
            if len(shown_info) < 25 and not any(s in bigger for bigger in shown_flag):
                shown_info.append(s)
    if not shown_flag:
        print("  none distinctive (gate clean)")
    if shown_info:
        print(f"\n  (informational — {len(shown_info)} generic/×2 repeats, not gated):")
        for s in shown_info[:25]:
            print(f"     · \"{s}\"")

    # --- MOTIF CAP: declared motifs may not exceed their book-wide cap -------------
    if motif_caps:
        print("\n" + "=" * 70)
        print(f"MOTIF CAP (book-wide occurrences; default cap {args.motif_cap})")
        print("=" * 70)
        over = []
        for phrase, cap in sorted(motif_caps.items()):
            cnt = motif_book_counts.get(phrase, 0)
            if cnt > cap:
                chs = sorted(motif_chapters[phrase])
                over.append((phrase, cnt, cap, chs))
        if over:
            for phrase, cnt, cap, chs in sorted(over, key=lambda x: -x[1]):
                print(f"  OVER ×{cnt} > {cap}  chapters {chs}  \"{phrase}\"")
                problems += 1
        else:
            print("  all motifs within cap (clean)")

    print("\n" + "=" * 70)
    print(f"RESULT: {problems} issue(s) flagged." if problems else "RESULT: clean.")
    print("=" * 70)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(scan())
