#!/usr/bin/env python3
"""make_epub.py — build a reflowable EPUB3 (with EPUB2 NCX fallback) for any book
in this repo. Cover + title + optional "Also by" + copyright + dedication +
chapters + back matter, with a navigable TOC. Pure stdlib.

    python3 tools/make_epub.py books/your-book
    python3 tools/make_epub.py books/your-series/book-two --out /tmp/test.epub

Configuration comes from `<book>/delivery/ebook.yaml`, with anything it omits
falling back to the book's STATE.yaml. Copy the annotated starting point from
books/_template/delivery/ebook.yaml. All paths in it are relative to the book
folder, so a book folder stays portable.

INPUT: an assembled single-file manuscript whose chapters are marked

    CHAPTER ONE

    The Chapter Title

    ...prose...

which is what the per-book assemble_manuscript.py produces. If `manuscript` is
not set, the newest `manuscript/full-manuscript*.md` is used; if a REVISION file
exists, the manuscript matching that revision wins.

The ebook ISBN in the config becomes the EPUB's package identifier, which is what
retailers read — it must be the EBOOK ISBN, not the print one.
"""

import os, re, zipfile, html, uuid, sys, datetime, argparse

FONTWORDS = {"ONE":1,"TWO":2,"THREE":3,"FOUR":4,"FIVE":5,"SIX":6,"SEVEN":7,
    "EIGHT":8,"NINE":9,"TEN":10,"ELEVEN":11,"TWELVE":12,"THIRTEEN":13,
    "FOURTEEN":14,"FIFTEEN":15,"SIXTEEN":16,"SEVENTEEN":17,"EIGHTEEN":18,
    "NINETEEN":19,"TWENTY":20}
WORDTITLE = {v:k.title() for k,v in FONTWORDS.items()}

def parse(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    chapters=[]; i=0
    while i < len(lines) and not re.match(r"^CHAPTER\s+[A-Z]+\s*$", lines[i].strip()):
        i+=1
    while i < len(lines):
        m=re.match(r"^CHAPTER\s+([A-Z]+)\s*$", lines[i].strip())
        if not m: i+=1; continue
        word=m.group(1); i+=1
        while i<len(lines) and not lines[i].strip(): i+=1
        title=lines[i].strip() if i<len(lines) else ""; i+=1
        buf=[]
        while i<len(lines) and not re.match(r"^CHAPTER\s+[A-Z]+\s*$", lines[i].strip()):
            buf.append(lines[i]); i+=1
        chapters.append((FONTWORDS.get(word,0), title, "\n".join(buf)))
    return chapters

def inline(s):
    s=html.escape(s, quote=False)
    s=re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    s=re.sub(r"_(.+?)_", r"<em>\1</em>", s)
    return s

def paras(text):
    out=[]
    for b in re.split(r"\n\s*\n", text.strip()):
        s=b.strip()
        if not s: continue
        if s in ("* * *","***","———","* * * *","* * *  *"):
            out.append(("scene",None))
        else:
            out.append(("p"," ".join(l.strip() for l in s.split("\n"))))
    return out

CSS = """body{font-family:Georgia,'Times New Roman',serif;line-height:1.5;margin:5%;}
h1,h2,h3{font-weight:normal;text-align:center;}
h2.chnum{margin-top:3em;letter-spacing:.15em;text-transform:uppercase;font-size:1em;}
h3.chtitle{font-style:italic;margin:.3em 0 2em;font-size:1.3em;}
p{margin:0;text-indent:1.3em;text-align:justify;}
p.first{text-indent:0;}
p.scene{text-align:center;text-indent:0;margin:1.4em 0;letter-spacing:.4em;}
.center{text-align:center;}.title-main{font-size:1.6em;letter-spacing:.1em;margin-top:25%;}
.subtitle{font-style:italic;font-size:1.2em;margin-top:.6em;}
.author{margin-top:3em;letter-spacing:.2em;}
.cp{font-size:.85em;text-align:center;line-height:1.8;margin-top:30%;}
.ded{font-style:italic;text-align:center;margin-top:40%;}
img.cover{max-width:100%;height:auto;display:block;margin:0 auto;}"""

def xhtml(title, body):
    return ('<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" '
        'xmlns:epub="http://www.idpf.org/2007/ops" lang="en">\n<head>\n'
        f'<title>{html.escape(title)}</title>\n'
        '<meta charset="utf-8"/>\n<link rel="stylesheet" type="text/css" href="style.css"/>\n'
        f'</head>\n<body>\n{body}\n</body>\n</html>\n')

def build_epub(cfg):
    chapters=parse(cfg["manuscript"])
    assert chapters, "no chapters parsed"
    uid="urn:isbn:"+cfg["isbn"]
    items=[]  # (id, href, content_str_or_path, media_type, in_spine, nav_label)

    # cover image
    cover_ext = os.path.splitext(cfg["cover"])[1].lower().lstrip(".")
    cover_mt = "image/jpeg" if cover_ext in ("jpg","jpeg") else "image/png"
    items.append(("coverimg","cover."+cover_ext, ("FILE",cfg["cover"]), cover_mt, False, None))
    # author photo for the About the Author page (manifest only, not in the spine)
    photo_rel = None
    if cfg.get("photo") and os.path.exists(cfg["photo"]):
        photo_rel = "author-photo" + os.path.splitext(cfg["photo"])[1].lower()
        items.append(("authorphoto", photo_rel, ("FILE", cfg["photo"]),
                      "image/jpeg", False, None))
    # cover page
    cover_body=f'<div class="center"><img class="cover" src="cover.{cover_ext}" alt="Cover"/></div>'
    items.append(("coverpage","cover.xhtml", xhtml("Cover",cover_body), "application/xhtml+xml", True, None))
    # title page
    _main = cfg.get("series_title") or cfg.get("title") or cfg["full_title"]
    tp=(f'<div class="center"><div class="title-main">{html.escape(_main).upper()}</div>'
        + (f'<div class="subtitle">{html.escape(cfg["subtitle"])}</div>' if cfg.get("subtitle") else "")
        + f'<div class="author">{html.escape(cfg["author"]).upper()}</div></div>')
    items.append(("titlepage","title.xhtml", xhtml("Title Page",tp), "application/xhtml+xml", True, "Title Page"))
    # "Also by" — front matter, right after the title page, as in the print book
    if cfg.get("also_by"):
        _hdr = f'Also by {cfg["author"]}'
        ab = f'<h2 class="chnum">{html.escape(_hdr)}</h2>' + cfg["also_by"]
        items.append(("alsoby","alsoby.xhtml", xhtml(_hdr,ab),
                      "application/xhtml+xml", True, _hdr))
    # copyright
    cp_lines=[f"Copyright &#169; {cfg.get('year', datetime.date.today().year)} {cfg['author']}","All rights reserved.",
        "This is a work of fiction. Names, characters, places, and incidents are "
        "products of the author&#8217;s imagination or are used fictitiously.",
        "No part of this book may be reproduced without written permission from "
        "the author, except for brief quotations in a book review.",
        "Ebook Edition",f"ISBN {cfg['isbn_hyphen']}",cfg.get("publisher") or cfg["author"]]
    cp='<div class="cp">'+"<br/><br/>".join(cp_lines)+"</div>"
    items.append(("copyright","copyright.xhtml", xhtml("Copyright",cp), "application/xhtml+xml", True, None))
    # dedication
    if (cfg.get("dedication") or "").strip():
        items.append(("dedication","dedication.xhtml",
            xhtml("Dedication", f'<div class="ded">{cfg["dedication"]}</div>'),
            "application/xhtml+xml", True, "Dedication"))
    # chapters
    for n,title,text in chapters:
        body=[f'<h2 class="chnum">Chapter {WORDTITLE.get(n,n)}</h2>']
        if title: body.append(f'<h3 class="chtitle">{inline(title)}</h3>')
        for kind,content in paras(text):
            if kind=="scene": body.append('<p class="scene">* * *</p>')
            else:
                cls=' class="first"' if (body and body[-1].startswith("<h")) else ""
                body.append(f"<p{cls}>{inline(content)}</p>")
        lbl=f"Chapter {WORDTITLE.get(n,n)}"+(f" — {title}" if title else "")
        items.append((f"ch{n}", f"chapter-{n}.xhtml", xhtml(lbl,"\n".join(body)),
                      "application/xhtml+xml", True, lbl))
    # back matter
    photo_html = (f'<div class="center"><img src="{photo_rel}" alt="" '
                  'style="max-width:45%;margin:0 auto 1em;"/></div>') if photo_rel else ""
    bm = ""
    if cfg.get("bio"):
        bm += f'<h2 class="chnum">About the Author</h2>{photo_html}<p class="first">{cfg["bio"]}</p>'
    if cfg.get("ack"):
        bm += f'<h2 class="chnum">Acknowledgments</h2><p class="first">{cfg["ack"]}</p>'
    if bm:
        items.append(("backmatter","backmatter.xhtml", xhtml("About the Author",bm),
                      "application/xhtml+xml", True, "About the Author"))

    # nav.xhtml
    navlis="".join(f'<li><a href="{h}">{html.escape(lbl)}</a></li>\n'
        for (_id,h,_c,_m,spine,lbl) in items if lbl)
    nav=('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">\n'
        '<head><title>Contents</title><meta charset="utf-8"/></head>\n<body>\n'
        '<nav epub:type="toc" id="toc"><h1>Contents</h1>\n<ol>\n'+navlis+'</ol></nav>\n</body></html>\n')

    # toc.ncx (epub2 fallback)
    points=""; pn=1
    for (_id,h,_c,_m,spine,lbl) in items:
        if lbl:
            points+=(f'<navPoint id="np{pn}" playOrder="{pn}"><navLabel><text>'
                f'{html.escape(lbl)}</text></navLabel><content src="{h}"/></navPoint>\n'); pn+=1
    ncx=('<?xml version="1.0" encoding="utf-8"?>\n'
        '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
        f'<head><meta name="dtb:uid" content="{uid}"/></head>\n'
        f'<docTitle><text>{html.escape(cfg["full_title"])}</text></docTitle>\n'
        f'<navMap>\n{points}</navMap>\n</ncx>\n')

    # content.opf
    manifest=['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '<item id="css" href="style.css" media-type="text/css"/>']
    spine=[]
    for (_id,h,_c,mt,insp,lbl) in items:
        props=' properties="cover-image"' if _id=="coverimg" else ""
        manifest.append(f'<item id="{_id}" href="{h}" media-type="{mt}"{props}/>')
        if insp: spine.append(f'<itemref idref="{_id}"/>')
    opf=('<?xml version="1.0" encoding="utf-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">\n'
        '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
        f'<dc:identifier id="bookid">urn:isbn:{cfg["isbn"]}</dc:identifier>\n'
        f'<dc:title>{html.escape(cfg["full_title"])}</dc:title>\n'
        f'<dc:language>{cfg.get("language","en")}</dc:language>\n'
        f'<dc:creator>{html.escape(cfg["author"])}</dc:creator>\n'
        f'<dc:publisher>{html.escape(cfg.get("publisher") or cfg["author"])}</dc:publisher>\n'
        f'<dc:description>{html.escape(cfg["desc"])}</dc:description>\n'
        '<meta property="dcterms:modified">2026-06-24T00:00:00Z</meta>\n'
        '<meta name="cover" content="coverimg"/>\n</metadata>\n'
        '<manifest>\n'+"\n".join(manifest)+'\n</manifest>\n'
        '<spine toc="ncx">\n'+"\n".join(spine)+'\n</spine>\n</package>\n')

    # write zip
    out=cfg["out"]
    with zipfile.ZipFile(out,"w") as z:
        z.writestr("mimetype","application/epub+zip",compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
            '<?xml version="1.0"?>\n<container version="1.0" '
            'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
            '<rootfiles><rootfile full-path="OEBPS/content.opf" '
            'media-type="application/oebps-package+xml"/></rootfiles></container>\n',
            compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf",opf,compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/nav.xhtml",nav,compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/toc.ncx",ncx,compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css",CSS,compress_type=zipfile.ZIP_DEFLATED)
        for (_id,h,content,mt,insp,lbl) in items:
            if isinstance(content,tuple) and content[0]=="FILE":
                z.write(content[1], "OEBPS/"+h, compress_type=zipfile.ZIP_DEFLATED)
            else:
                z.writestr("OEBPS/"+h, content, compress_type=zipfile.ZIP_DEFLATED)
    return out, len(chapters)


# ---------------------------------------------------------------------------
# Configuration: <book>/delivery/ebook.yaml, backed by STATE.yaml, paths relative
# to the book folder.
# ---------------------------------------------------------------------------

REQUIRED = ("manuscript", "cover", "out", "full_title", "author", "isbn", "isbn_hyphen")


def _load_yaml(path):
    try:
        import yaml
    except ImportError:
        sys.exit("error: pyyaml is required — pip install -r requirements.txt")
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _find_manuscript(book):
    """Newest assembled manuscript; a REVISION file, if present, decides."""
    d = os.path.join(book, "manuscript")
    if not os.path.isdir(d):
        return None
    cands = sorted(f for f in os.listdir(d) if f.startswith("full-manuscript") and f.endswith(".md"))
    if not cands:
        return None
    rev_file = os.path.join(book, "REVISION")
    if os.path.isfile(rev_file):
        rev = open(rev_file, encoding="utf-8").read().strip()
        for c in cands:
            if rev in c:
                return os.path.join("manuscript", c)
    return os.path.join("manuscript", cands[-1])


def build_config(book, overrides=None):
    book = os.path.abspath(book)
    cfg_path = os.path.join(book, "delivery", "ebook.yaml")
    cfg = _load_yaml(cfg_path) if os.path.isfile(cfg_path) else {}

    state = {}
    if os.path.isfile(os.path.join(book, "STATE.yaml")):
        state = _load_yaml(os.path.join(book, "STATE.yaml"))
    proj = (state.get("project") or {}) if isinstance(state, dict) else {}
    series = (state.get("series") or {}) if isinstance(state, dict) else {}

    # Fall back to what STATE.yaml already knows.
    cfg.setdefault("title", proj.get("title") or os.path.basename(book))
    cfg.setdefault("full_title", cfg["title"])
    cfg.setdefault("desc", proj.get("premise") or "")
    if series.get("name"):
        cfg.setdefault("series_title", series["name"])
    cfg.setdefault("manuscript", _find_manuscript(book))
    cfg.setdefault("out", os.path.join("delivery", "ebook",
                                       re.sub(r"[^A-Za-z0-9]+", "-", cfg["title"]).strip("-") + ".epub"))

    if overrides:
        cfg.update({k: v for k, v in overrides.items() if v})

    # Resolve every path relative to the book folder.
    for key in ("manuscript", "cover", "out", "photo"):
        if cfg.get(key) and not os.path.isabs(cfg[key]):
            cfg[key] = os.path.join(book, cfg[key])

    missing = [k for k in REQUIRED if not cfg.get(k)]
    if missing:
        sys.exit(
            "error: missing required config: " + ", ".join(missing)
            + f"\n       set them in {os.path.join(book, 'delivery', 'ebook.yaml')}"
            + "\n       (start from books/_template/delivery/ebook.yaml)")

    for key in ("manuscript", "cover"):
        if not os.path.isfile(cfg[key]):
            sys.exit(f"error: {key} not found: {cfg[key]}")

    cfg["isbn"] = str(cfg["isbn"]).replace("-", "")
    return cfg


def main():
    ap = argparse.ArgumentParser(description="Build an EPUB for a book folder.")
    ap.add_argument("book", help="path to the book folder, e.g. books/your-book")
    ap.add_argument("--manuscript", help="override the assembled manuscript path")
    ap.add_argument("--cover", help="override the cover image path")
    ap.add_argument("--out", help="override the output .epub path")
    args = ap.parse_args()

    if not os.path.isdir(args.book):
        sys.exit(f"error: not a directory: {args.book}")

    cfg = build_config(args.book, {"manuscript": args.manuscript,
                                   "cover": args.cover, "out": args.out})
    os.makedirs(os.path.dirname(cfg["out"]), exist_ok=True)
    out, n = build_epub(cfg)
    print(f"wrote {out}  ({n} chapters, {os.path.getsize(out) // 1024} KB)")
    if n == 0:
        print("warn: no chapters parsed — check that the manuscript uses 'CHAPTER ONE' headings",
              file=sys.stderr)


if __name__ == "__main__":
    main()
