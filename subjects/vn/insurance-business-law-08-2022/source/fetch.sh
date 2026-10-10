#!/usr/bin/env bash
# Fetch the publisher's document(s), refuse any whose sha256 differs from the pinned one, and write
# raw/<id>.pdf plus raw/<id>.txt (`pdftotext`, with `-layout` unless the row says reading order).
# raw/ is git-ignored: this repository holds no copy of the source (ruling of 2026-10-01: cite an
# openly published document by URL and digest and fetch it). `src:N` in the encodings means line N of raw/<id>.txt.
# A file already at raw/<id>.pdf whose sha256 matches is used as is; that is how a document the server
# refuses to curl (403, a bot challenge) is supplied: download it in a browser, save it as raw/<id>.pdf, rerun.
# Pinned 2026-10-10. Needs: curl, shasum, pdftotext (poppler). The text layer is a function of the poppler
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
fetch "law08-2022-qh15" "https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2022/6/37510/41181-1-2022575-57608-2022-qh15.pdf" "1790a7788738008ffd2574f1248aedcfd485e5966647b9f29be07335b17194c4" "https://congbao.chinhphu.vn/" "layout"
fetch "law08-2022-qh15-577-578" "https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2022/6/37510/41184-1-2022577-57808-2022-qh15.pdf" "f2310ab382393a9b4845a9bf09880d80b1e845e5261c07743181fc8c6a4ed58c" "https://congbao.chinhphu.vn/" "layout"
fetch "law139-2025-qh15" "https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/139signed-1769242926123406231234.pdf" "81c81bf4f77ed68f0fbaa4967c6573aa6ff81831960a742de14e8933287ad665" "https://congbao.chinhphu.vn/" "layout"
