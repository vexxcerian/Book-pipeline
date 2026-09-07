# Publishing

Manuscript → EPUB + print PDFs → IngramSpark. Everything here was learned by uploading real
books, including the rejections. The specs are fussier than they look, and the spine is the
one dimension a reprint cannot fix.

## What IngramSpark actually wants

Three files per title, and they are not the files you'd guess:

| File | Spec |
|---|---|
| **Interior** | Print PDF, **grayscale, no ICC profile**, exact trim (6×9 here), fonts fully embedded, **even page count** for perfect binding |
| **Cover** | Full wrap (back + spine + front) at full bleed, **CMYK, no ICC**, real EAN-13 barcode for the print ISBN, **no price add-on** |
| **EPUB** | Carries the **eBook ISBN** as its package identifier, with a working navigation TOC (`nav.xhtml` + `toc.ncx`) |

Plus a **standalone front-cover JPG** for the ebook listing: RGB, ≥1600px on the short side,
aspect ratio around 1.414 (retailers accept 1.33–1.6).

**Do not upload the PDF/X-1a builds.** They are archival/prepress copies and stay in each
book's `delivery/` folder. Upload takes the grayscale interior and the CMYK cover.

## Building the files

```bash
# interior -> grayscale, no ICC
bash tools/make_noicc.sh gray delivery/production/INTERIOR-r7.pdf INTERIOR-r7-GRAY-noicc.pdf

# cover wrap -> CMYK, no ICC
bash tools/make_noicc.sh cmyk delivery/cover/WRAP-r7-fullbleed-rgb.pdf WRAP-r7-CMYK-noicc.pdf
```

Needs Ghostscript. Verify a finished PDF is clean by confirming `OutputIntent` and
`/ICCBased` are both absent.

### The EPUB

```bash
python3 tools/make_epub.py books/<slug>
```

Config lives in `books/<slug>/delivery/ebook.yaml` (new books get an annotated copy;
otherwise start from `books/_template/delivery/ebook.yaml`). Required: `full_title`,
`author`, `isbn` + `isbn_hyphen`, `cover`. Everything else falls back to `STATE.yaml` or is
optional — subtitle, series title, publisher, year, dedication, bio, acknowledgments, author
photo, and an "Also by" page. All paths are relative to the book folder, so a book folder
stays portable.

Input is an assembled single-file manuscript using `CHAPTER ONE` headings — what the
per-book `assemble_manuscript.py` produces. If `manuscript` isn't set, the newest
`manuscript/full-manuscript*.md` is used, or the one matching a `REVISION` file.

**The `isbn` must be the EBOOK ISBN**, not the print one: it becomes the EPUB's package
identifier, which is what retailers read.

The output is EPUB3 with an EPUB2 NCX fallback, mimetype stored first and uncompressed, and
a working `nav.xhtml` + `toc.ncx`.

EPUB ISBN swap (when reusing an existing build for a new identifier, rather than rebuilding):
unzip, replace the ISBN in `OEBPS/content.opf` (`dc:identifier`), `OEBPS/toc.ncx`
(`dtb:uid`) and `OEBPS/copyright.xhtml`, then rezip with **mimetype stored first**:

```bash
zip -X -q0 OUT.epub mimetype && zip -X -qrg OUT.epub . -x mimetype
```

`build_pdf.py` and `assemble_manuscript.py` stay per-book, because trim size, front matter
and typography differ per title. A series with locked shared front matter can keep its own
builder in the series folder; `tools/make_epub.py` covers everything else.

## The gotchas, in the order they bit

**Image resolution: 300 ppi is a target, not a floor.** An upload was rejected for
*excessively high* resolution ("Excessively high resolution images will not increase the
quality of the printed book, and can lead to the book being delayed"). Their preflight
objects to too-high as well as too-low. `make_noicc.sh` downsamples to 300 (600 for bitmap
line art) — and the threshold overrides matter, because Ghostscript's `/prepress` only
downsamples above 1.5× the target by default, so 300–450 ppi images would slip through.

**The Ghostscript pass costs the text layer.** The grayscale/CMYK conversion drops the
fonts' ToUnicode mapping, so non-ASCII characters (em dashes, curly quotes, ©, ø) don't
*extract* from the upload PDF. Printing is unaffected. If you need a searchable or
accessible PDF, use the RGB build from `delivery/`.

**Cover wrap must be tight full-bleed.** IngramSpark's current template wants no white
margins. Wraps built to the older Lightning Source template have white margins that shift
the back-cover content into the spine. Crop to the true art box.

**Supply your own barcode.** On the cover step choose "my cover already includes a barcode"
so IngramSpark doesn't overlay its own white box on yours. Generate the EAN-13 from the
print ISBN with `python-barcode`, no price add-on.

**Print and eBook are separate formats** with separate interior + cover steps — and the
"Preview my book" button validates *all* formats, so an empty eBook format blocks you while
you're still on the print tab.

**The eBook interior must be an EPUB or .docx.** A PDF is rejected there. The eBook "page
count" field is nominal; enter the print count to match.

**The ICC-profile warning is non-blocking.** If "PDF CONTAINS ICC COLOR PROFILES" appears
despite profile-free files, you can proceed — but order a printed proof and confirm the
interior text prints solid black, not gray.

**Type the title once.** Entering it repeatedly is what made a title display three or four
times on the product page.

**Confirm the paper stock before ordering a proof.** Spine width is computed from page
count × paper thickness (IngramSpark white 50# = 0.002252"/pp here; one book uses cream
50#). Re-check the final number against IngramSpark's own spine calculator.

## `completed-books/` — the upload staging folder

Every finished book's three upload files, collected in one place.

```bash
python3 tools/collect_completed.py           # refresh from each book's current revision
python3 tools/collect_completed.py --check   # verify nothing has gone stale (exit 1 if it has)
```

**It is generated — never hand-edit it.** Copies go stale the moment a book is re-cut, and
a stale print file is exactly the kind of thing that gets uploaded by mistake. Every file
is checksummed into `MANIFEST.md` alongside the revision it came from, so staleness is
*detectable* rather than silent. Re-run after any re-cut, and add new books to the `BOOKS`
list in the script.

`completed-books/LISTING-METADATA.md` holds the answers to the publishing form per book —
including the ones with byte limits (IngramSpark's Short Description cap is 250 **bytes**,
not characters, which matters the moment you use a curly quote or an em dash).

## Uploading from a locked-down device

If the machine you're on can't drive a file picker (a locked phone, a kiosk), the route
that works is a full Linux desktop in **Google Cloud Shell** — XFCE plus real Firefox,
streamed into the browser — with the book files pulled straight from your repo into that
desktop's `~/Downloads`. The desktop's file picker works, and the device is just a screen.

Keep your own notes on this in the book folder once you've done it — including the "an error
has occurred during the upload" path, which is the one that wastes an afternoon. One warning
if you do: never commit a GitHub access token to those notes. Secret scanning auto-revokes
any token pushed to a repo, so it would be dead within minutes anyway — mint a fresh one when
you need it (about 30 seconds).

## Before you approve for sale

- Order a **printed proof**. Check the interior prints solid black, the spine text is
  centred, and nothing has crept into the gutter.
- Confirm the ISBNs: print and ebook are **different ISBNs**, and the one baked into the
  barcode must match the print ISBN on the record.
- Confirm the author name field matches the cover and title page exactly — a pen name that
  differs between the record and the artwork is a rejection.
- Run `collect_completed.py --check` one last time so you know the files in your hand are
  the current build.
