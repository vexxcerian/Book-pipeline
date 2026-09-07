#!/usr/bin/env python3
"""Resample front-cover art up to a print-safe resolution.

  python3 tools/cover_art_to_print_res.py <in.png> <out.png> [--dpi 375]

WHAT THIS DOES AND DOES NOT DO
------------------------------
IngramSpark wants >=300 dpi on the placed cover art. Several of our front covers
are fixed rasters (1587x2245 or 1600x2263) with no design source in the repo to
re-export from, which lands them at ~235-243 dpi once the wrap centre-crops them
to the 6.125 x 9.25" front panel.

This resamples them (Lanczos) so the number clears the spec. **It does not add
detail** — no resampler can. It is worth doing anyway for two reasons: it stops
the preflight warning, and it puts OUR resampler in charge rather than the
printer's RIP. For this particular artwork the cost is unusually low: the art is
soft organic gradient (smoke, glow, a crack) with almost no high-frequency detail,
and the type on it is already antialiased.

The genuinely correct fix, when the original design file is available, is to
re-export the art at >=1838 x 2775 px and drop it in instead — then delete the
"-print" variant so the build picks up the real thing.

Scale & Silver is the exception: its front is composited in-repo
(delivery/cover/compose_cover.py = art bed + HTML/CSS type), so it is re-rendered
at 2x through headless Chromium instead. That gives genuinely sharp *type*, which
is the part that shows softness in print; only its art bed is interpolated.
"""
import sys
from PIL import Image

PANEL_W, PANEL_H = 6.125, 9.25          # front trim + outer bleed, inches
TARGET = PANEL_W / PANEL_H


def placed_dpi(w, h):
    """dpi of the art once the wrap centre-crops it to the front panel."""
    cropped_w = h * TARGET if (w / h) > TARGET else w
    return cropped_w / PANEL_W


def main(src, dst, dpi=375.0):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    before = placed_dpi(w, h)
    if before >= dpi:
        print(f"{src}: already {before:.0f} dpi on the panel — nothing to do")
        return
    scale = dpi / before
    nw, nh = round(w * scale), round(h * scale)
    im.resize((nw, nh), Image.LANCZOS).save(dst, optimize=True)
    print(f"{src}\n  {w}x{h} ({before:.0f} dpi placed)"
          f"  ->  {nw}x{nh} ({placed_dpi(nw, nh):.0f} dpi placed), x{scale:.2f} Lanczos"
          f"\n  wrote {dst}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dpi = 375.0
    if "--dpi" in sys.argv:
        dpi = float(sys.argv[sys.argv.index("--dpi") + 1])
        args = [a for a in args if a != str(dpi) and a != f"{dpi:g}"]
    if len(args) != 2:
        sys.exit(__doc__)
    main(args[0], args[1], dpi)
