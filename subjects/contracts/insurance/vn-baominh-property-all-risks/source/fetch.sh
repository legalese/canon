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
fetch "baominh-par" "https://www.baominh.com.vn/uploads/source/File%20t%C3%A0i%20li%E1%BB%87u/tai%20san/01-QuytacBHMoiruirotaisan_TV.pdf" "cd83ace07e456de9e2b897595b07fad47fe86f63d2611f123fad190923b987c5" "https://www.baominh.com.vn/"
