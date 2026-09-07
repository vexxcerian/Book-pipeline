#!/usr/bin/env python3
"""Collect every finished book's upload-ready files into completed-books/.

  python3 tools/collect_completed.py           # refresh the folder
  python3 tools/collect_completed.py --check   # verify it matches source, exit 1 if stale

WHY THIS IS A SCRIPT AND NOT A HAND-COPIED FOLDER
Copies go stale the moment a book is re-cut, and a stale print file is exactly the
kind of thing that gets uploaded by mistake. So the folder is generated, every file
is checksummed into MANIFEST.md alongside the revision it came from, and --check
tells you whether what is sitting in completed-books/ is still the current build.

Each book contributes the THREE files IngramSpark actually wants:
  INTERIOR     the grayscale, no-ICC print interior
  COVER        the CMYK, no-ICC full wrap (back + spine + front, full bleed)
  EPUB         the ebook
  EBOOK-COVER  the standalone front-cover JPG the ebook listing asks for separately
The PDF/X-1a builds are archival/prepress copies and deliberately stay behind in
each book's own delivery/ folder.
"""
import hashlib, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "completed-books")

BOOKS = [
    # One entry per finished book. Paths are relative to the book folder; "{rev}" is
    # substituted from that book's REVISION file, so a re-cut is picked up automatically.
    #
    # dict(order="01", title="Your Book", folder="01-your-book",
    #      series="Your Series, Book One", pen="Your Pen Name",
    #      book="books/your-book",
    #      interior="delivery/production/Your-Book-6x9-interior-{rev}-GRAY-noicc.pdf",
    #      cover="delivery/cover/Your-Book-FULL-WRAP-{rev}-CMYK-noicc.pdf",
    #      epub="delivery/ebook/Your-Book.epub",
    #      ebookcover="delivery/cover/ebook-cover-your-book.jpg",
    #      pages=294, spine='0.662"', isbn="978-0-0000-0000-0", eisbn="978-0-0000-0001-7"),
]


def rev(b):
    return open(os.path.join(ROOT, b["book"], "REVISION"), encoding="utf-8").read().strip()


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def slug(t):
    return t.replace(" ", "-")


def plan():
    """[(book, revision, [(src_abs, dst_abs, label)])]"""
    out = []
    for b in BOOKS:
        r = rev(b)
        dst_dir = os.path.join(OUT, b["folder"])
        files = []
        for key, label in (("interior", "INTERIOR"), ("cover", "COVER"),
                           ("epub", "EPUB"), ("ebookcover", "EBOOK-COVER")):
            src = os.path.join(ROOT, b["book"], b[key].format(rev=r))
            ext = os.path.splitext(src)[1]
            if label == "EPUB":
                name = f"{slug(b['title'])}{ext}"
            elif label == "EBOOK-COVER":          # not revision-stamped: art, not a build
                name = f"{slug(b['title'])}-{label}{ext}"
            else:
                name = f"{slug(b['title'])}-{r}-{label}{ext}"
            files.append((src, os.path.join(dst_dir, name), label))
        out.append((b, r, files))
    return out


def main(check=False):
    if not BOOKS:
        print("No books registered yet. Add an entry to the BOOKS list in this script")
        print("(there is a commented example) once a book has its three upload files:")
        print("  the grayscale no-ICC interior, the CMYK no-ICC cover wrap, and the EPUB.")
        return 0
    os.makedirs(OUT, exist_ok=True)
    missing, stale = [], []
    wanted = {}          # dir -> filenames that belong there
    p = plan()
    for b, r, files in p:
        for src, dst, _ in files:
            if not os.path.exists(src):
                missing.append(src); continue
            if check:
                if not os.path.exists(dst) or sha(src) != sha(dst):
                    stale.append(os.path.relpath(dst, ROOT))
            else:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                wanted.setdefault(os.path.dirname(dst), set()).add(os.path.basename(dst))
    if missing:
        print("MISSING SOURCE FILES:"); [print("  ", os.path.relpath(m, ROOT)) for m in missing]
        return 1
    if check:
        for b, r, files in p:
            d = os.path.join(OUT, b["folder"])
            keep = {os.path.basename(dst) for _, dst, _ in files}
            if os.path.isdir(d):
                stale += [os.path.relpath(os.path.join(d, f), ROOT)
                          for f in sorted(os.listdir(d)) if f not in keep]
        if stale:
            print("STALE — completed-books/ does not match the current builds:")
            [print("  ", s) for s in stale]
            return 1
        print("completed-books/ is up to date with every book's current REVISION")
        return 0

    # --- remove superseded revisions -----------------------------------------
    # Filenames carry the revision, so a re-cut leaves the previous build sitting
    # beside the new one. That is precisely the stale-file hazard this folder exists
    # to prevent — someone uploads r19 because it sorted first. Anything in a book's
    # folder that is not part of the current build goes.
    removed = []
    for d, keep in wanted.items():
        for f in sorted(os.listdir(d)):
            if f not in keep:
                os.remove(os.path.join(d, f))
                removed.append(os.path.relpath(os.path.join(d, f), ROOT))

    # --- MANIFEST -----------------------------------------------------------
    lines = ["# Manifest\n",
             "Generated by `tools/collect_completed.py`. Do not edit by hand — rerun the\n"
             "script instead. `--check` verifies these checksums against the live builds.\n"]
    for b, r, files in p:
        lines.append(f"\n## {b['title']} — {r}\n")
        lines.append(f"{b['series']} · by {b['pen']}\n")
        lines.append(f"\n{b['pages']} pages · spine {b['spine']} · "
                     f"print ISBN {b['isbn']} · eBook ISBN {b['eisbn']}\n\n")
        lines.append("| file | sha256 (short) | size |\n|---|---|---|\n")
        for src, dst, label in files:
            kb = os.path.getsize(dst) // 1024
            lines.append(f"| `{os.path.basename(dst)}` | `{sha(dst)}` | {kb} KB |\n")
    open(os.path.join(OUT, "MANIFEST.md"), "w", encoding="utf-8").write("".join(lines))

    for b, r, files in p:
        print(f"{b['title']:28s} {r:4s} -> completed-books/{b['folder']}/")
    if removed:
        print(f"\nremoved {len(removed)} superseded file(s):")
        for f in removed:
            print("  ", f)
    print("\nwrote completed-books/MANIFEST.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv))
