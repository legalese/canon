#!/usr/bin/env bash
# Fetch the publisher's document(s), refuse any whose sha256 differs from the pinned one, and write
# raw/<id>.pdf plus raw/<id>.txt (`pdftotext`, with `-layout` unless the row says reading order).
# raw/ is git-ignored: this repository holds no copy of the source (ruling of 2026-10-01: cite an
# openly published document by URL and digest and fetch it). `src:N` in the encodings means line N of raw/<id>.txt.
# A file already at raw/<id>.pdf whose sha256 matches is used as is; that is how a document the server
# refuses to curl (403, a bot challenge) is supplied: download it in a browser, save it as raw/<id>.pdf, rerun.
# Pinned 2026-10-06. Needs: curl, shasum, pdftotext (poppler). The text layer is a function of the poppler
# version; a different version can move line numbers, which is why the digest pins the PDF, not the text.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
mkdir -p raw
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
fetch() {  # id url sha256 referer mode
  local id="$1" url="$2" want="$3" ref="${4:-}" mode="${5:-layout}"
  if [ -f "raw/$id.pdf" ] && [ "$(sha "raw/$id.pdf")" = "$want" ]; then
    echo "have $id (sha256 matches)"
  else
    local args=(-fsSL -m 120 -A "$UA")
    [ -n "$ref" ] && args+=(-e "$ref")
    if ! curl "${args[@]}" -o "raw/$id.pdf" "$url"; then
      echo "fetch.sh: $id: the server refused curl. Download <$url> in a browser, save it as $(pwd)/raw/$id.pdf, and rerun." >&2
      return 1
    fi
    local got; got="$(sha "raw/$id.pdf")"
    if [ "$got" != "$want" ]; then
      mv "raw/$id.pdf" "raw/$id.pdf.rejected"
      echo "fetch.sh: $id: sha256 $got, expected $want (the publisher changed the file, or served an error page); kept as raw/$id.pdf.rejected" >&2
      return 1
    fi
  fi
  case "$mode" in
    reading) pdftotext "raw/$id.pdf" "raw/$id.txt" 2>/dev/null ;;
    ocr) ./ocr.sh "raw/$id.pdf" raw "$id" > /dev/null ;;
    *) pdftotext -layout "raw/$id.pdf" "raw/$id.txt" 2>/dev/null ;;
  esac
  echo "ok  $id  $(wc -l < "raw/$id.txt") lines  ($mode)"
}
fetch "aia-khoe-tron-ven" "https://www.aia.com.vn/content/dam/vn-wise/san-pham/bao-hiem-suc-khoe/b%E1%BB%87nh-hi%E1%BB%83m-ngh%C3%A8o/kh%E1%BB%8Fe-tr%E1%BB%8Dn-v%E1%BA%B9n/pdf/Khoe-Tron-Ven-Quy-Tac-Dieu-Khoan-Mau.pdf" "10008a684833b3ce6ba4a4b5274432cbc3c49cc488a124bb6559211c716326a6" "https://www.aia.com.vn/" "layout"
