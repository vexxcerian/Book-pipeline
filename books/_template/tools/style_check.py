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
    # Add THIS book's deliberate recurring motifs / canon terms here (string or (string, cap)).
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
# Ceilings for the chapters the PIPELINE writes. These exist because the argparse
# defaults are generic anti-AI settings, and on a book whose author legitimately writes
# with (say) heavy em-dashes they would fail a new chapter for correctly matching the
# voice it was told to match — which pressures the editor into sanding the book flat.
#
# Set these from the author's MEASURED range, slightly TIGHTER than he actually runs:
# the pipeline should be able to reach his voice but never to amplify it. Leave empty to
# use the generic defaults (right for a book with no hand-written benchmark).
# VOICE-MATCH FLOORS — the counterpart to the ceilings, and the half that is easy to forget.
# A ceiling stops the pipeline EXCEEDING the author. A floor stops it falling SHORT of him.
# That second failure is the one that actually happens: a writer told "do not exceed 9.5
# em-dashes per 1,000 words" scores a safe 4.7 and produces prose that is calm where the
# author is nervous. No single chapter looks wrong; twenty of them are a second author.
# Set these from the author's measured range too. Empty = no floor (right for a book with no
# hand-written benchmark to match).
PIPELINE_FLOORS = {}
AUTHOR_FLOORS = {}

PIPELINE_CEILINGS = {}

AUTHOR_DRAFTED = set()          # e.g. {1, 2, 3}
AUTHOR_CEILINGS = {             # applied ONLY to chapters listed above
    # "simile_per1k": 5.0,
    # "emdash_per1k": 12.0,     # density ceiling; replaces the absolute em-dash check
    # "adverb_per1k": 20.0,
    # "theway": 6,
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
