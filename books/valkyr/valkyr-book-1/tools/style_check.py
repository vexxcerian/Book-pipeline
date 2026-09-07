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
# Chapters 6-26 are PIPELINE-written and deliberately stay on the strict defaults
# (simile 4.0/1k, em-dash 4/chapter absolute, "the way" x2). That is where the
# anti-AI value of these ceilings actually lives.
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
    """The ceiling for chapter n: the author's calibration if it is a drafted chapter."""
    if n in AUTHOR_DRAFTED and key in AUTHOR_CEILINGS:
        return AUTHOR_CEILINGS[key]
    return default


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
