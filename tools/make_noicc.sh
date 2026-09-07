#!/usr/bin/env bash
# Produce the profile-free PDFs IngramSpark actually wants on upload.
#
#   bash tools/make_noicc.sh gray <interior.pdf> <out-GRAY-noicc.pdf>
#   bash tools/make_noicc.sh cmyk <wrap.pdf>     <out-CMYK-noicc.pdf>
#
# Why not the PDF/X-1a file: per INGRAMSPARK-UPLOAD-GUIDE Part C, the print
# interior uploads as **grayscale, no ICC** (a text-only B&W interior) and the
# cover as **CMYK, no ICC**. The X-1a builds are kept as the archival/prepress
# copies; these are the upload copies. An embedded ICC profile only triggers the
# "PDF CONTAINS ICC COLOR PROFILES" warning, so we ship without one.
#
# Images are downsampled to 300 ppi (600 for bitmap line art), which is what
# IngramSpark asks for.
#
# This was briefly set to preserve native resolution instead, on the theory that
# landing on exactly 300.0 risked reading as under-spec. That was wrong, and
# IngramSpark rejected the upload for it: "UNNECESSARY HIGH RESOLUTION IMAGES IN
# FILE ... Excessively high resolution images will not increase the quality of the
# printed book, and can lead to the book being delayed while processing." Their
# preflight objects to too-high as well as too-low. 300 is the target, not a floor.
#
# The threshold overrides matter: /prepress only downsamples above 1.5x the target
# by default, so 300-450 ppi images would have slipped through untouched.
set -euo pipefail

MODE="${1:?usage: make_noicc.sh <gray|cmyk> <in.pdf> <out.pdf>}"
IN="${2:?missing input pdf}"
OUT="${3:?missing output pdf}"

case "$MODE" in
  gray) CS=Gray; PCM=DeviceGray ;;
  cmyk) CS=CMYK; PCM=DeviceCMYK ;;
  *) echo "ERROR: mode must be 'gray' or 'cmyk', got '$MODE'"; exit 1 ;;
esac

[ -f "$IN" ] || { echo "ERROR: input PDF not found: $IN"; exit 1; }
command -v gs >/dev/null || { echo "ERROR: ghostscript (gs) not installed"; exit 1; }

gs -q -dBATCH -dNOPAUSE -dNOSAFER -sDEVICE=pdfwrite \
   -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress \
   -sColorConversionStrategy="$CS" -sProcessColorModel="$PCM" \
   -dAutoRotatePages=/None \
   -dEmbedAllFonts=true -dSubsetFonts=true \
   -dDownsampleColorImages=true  -dColorImageResolution=300 \
   -dDownsampleGrayImages=true   -dGrayImageResolution=300 \
   -dDownsampleMonoImages=true   -dMonoImageResolution=600 \
   -dColorImageDownsampleThreshold=1.0 \
   -dGrayImageDownsampleThreshold=1.0 \
   -dMonoImageDownsampleThreshold=1.0 \
   -sOutputFile="$OUT" "$IN"

# Verify it really is profile-free — an ICC profile here is the one thing that
# makes IngramSpark complain, and it is silent otherwise.
if grep -qa "/ICCBased\|/OutputIntent" "$OUT"; then
  echo "WARNING: $OUT still contains an ICC profile or output intent"
else
  echo "wrote $OUT (${MODE}, no ICC)"
fi
