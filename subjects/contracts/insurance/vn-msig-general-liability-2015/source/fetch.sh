#!/usr/bin/env bash
# Fetch the publisher's document(s), refuse any whose sha256 differs from the pinned one, and write
# raw/<id>.pdf plus raw/<id>.txt (`pdftotext -layout`). raw/ is git-ignored: this repository holds no copy
# of the source (ruling of 2026-10-01: cite an openly published document by URL and digest and fetch it).
# `src:N` in the encodings means line N of raw/<id>.txt.
# Pinned 2026-10-06. Needs: curl, shasum, pdftotext (poppler). The text layer is a function of the poppler
# version; a different version can move line numbers, which is why the digest pins the PDF, not the text.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
mkdir -p raw
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
fetch() {  # id url sha256 [referer]
  local id="$1" url="$2" sha="$3" ref="${4:-}"
  local args=(-fsSL -m 120 -A "$UA")
  [ -n "$ref" ] && args+=(-e "$ref")
  curl "${args[@]}" -o "raw/$id.pdf" "$url"
  local got; got="$(shasum -a 256 "raw/$id.pdf" | cut -d' ' -f1)"
  if [ "$got" != "$sha" ]; then
    mv "raw/$id.pdf" "raw/$id.pdf.rejected"
    echo "fetch.sh: $id: sha256 $got, expected $sha (the publisher changed the file, or served an error page); kept as raw/$id.pdf.rejected" >&2
    return 1
  fi
  pdftotext -layout "raw/$id.pdf" "raw/$id.txt" 2>/dev/null
  echo "ok  $id  $(wc -l < "raw/$id.txt") lines"
}
fetch "msig-cgl" "https://www.msig.com.vn/sites/default/files/downloads/Revised%20CGL%20Policy%20Form%2012%20Jan%202015.pdf" "cb17d805daa65afec62e78861fc2835a246d2d9fee306ea098b8d29c107d3814" ""
