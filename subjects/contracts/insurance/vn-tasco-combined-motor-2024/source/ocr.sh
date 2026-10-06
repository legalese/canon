#!/usr/bin/env bash
# usage: ocr.sh PDF OUTDIR ID
# OCR of a scanned (image-only) PDF: each page is rendered at 200 dpi and read with tesseract 5 (`-l vie --psm 4`,
# one thread per page); OUTDIR/ID.txt is the pages joined with a form feed after each. OUTDIR/ID.pages/ keeps one
# text file per page. The Vietnamese model is tessdata_best vie.traineddata, pinned by sha256 below.
# `src:N` in the encodings means line N of OUTDIR/ID.txt. Needs: pdftoppm and pdfinfo (poppler), tesseract 5, curl, shasum.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
pdf="$1"; out="$2"; id="$3"
MODEL_URL="https://github.com/tesseract-ocr/tessdata_best/raw/main/vie.traineddata"
MODEL_SHA="b6b49293d95d0b6dbd8780174627e82c75be957b6f4ed9862155540d6b00bb45"
mkdir -p "$here/tessdata"
have() { [ -f "$here/tessdata/vie.traineddata" ] && [ "$(shasum -a 256 "$here/tessdata/vie.traineddata" | cut -d' ' -f1)" = "$MODEL_SHA" ]; }
if ! have; then
  curl -fsSL -o "$here/tessdata/vie.traineddata" "$MODEL_URL"
  have || { echo "ocr.sh: vie.traineddata sha256 mismatch" >&2; exit 1; }
fi
mkdir -p "$out/$id.pages"
n=$(pdfinfo "$pdf" | awk '/^Pages:/{print $2}')
page() { p="$1"; f="$out/$id.pages/p$(printf %03d "$p")"
  pdftoppm -r 200 -gray -f "$p" -l "$p" -png -singlefile "$pdf" "$f"
  TESSDATA_PREFIX="$here/tessdata" OMP_THREAD_LIMIT=1 tesseract "$f.png" "$f" -l vie --psm 4 >/dev/null 2>&1
  rm -f "$f.png"; }
export -f page; export pdf out id here
seq 1 "$n" | xargs -P 6 -I{} bash -c 'page {}'
: > "$out/$id.txt"
for p in $(seq 1 "$n"); do cat "$out/$id.pages/p$(printf %03d "$p").txt" >> "$out/$id.txt"; printf '\f' >> "$out/$id.txt"; done
echo "ocr $id: $n pages"
