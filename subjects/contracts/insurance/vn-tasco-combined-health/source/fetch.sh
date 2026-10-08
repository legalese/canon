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
fetch "tasco-combined-health" "https://file-cdn.baohiemtasco.vn/cms/cms/bh-suc-khoe-ket-hop-1770107736.109.pdf" "378aee5ca0531bb3ac55ba54800f913d7a00f6d1264d735399f45187b3d1e8ec" "https://baohiemtasco.vn/" "layout"
fetch "tasco-guarantee-hospitals" "https://file-cdn.baohiemtasco.vn/cms/cms/danh-sach-bao-lanh-vien-phi-1751438464.823.pdf" "ca66f79394186bcbdec344fc279239dd20314d6694d61d701647c5cc0f973550" "https://baohiemtasco.vn/" "layout"
fetch "tasco-excluded-facilities" "https://file-cdn.baohiemtasco.vn/cms/cms/danh-sach-co-so-y-te-loai-tru-1751438446.156.pdf" "e39c6d6097cee43c71ea91721283995e5ac1e049050b3ac8afec5f349ce05fc9" "https://baohiemtasco.vn/" "layout"
