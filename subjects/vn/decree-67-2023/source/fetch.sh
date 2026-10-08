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
fetch "nd67-congbao-1017-1018" "https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2023/9/40096/46430-1-20231017-101867-2023-nd-cp.pdf" "19a1de3a974866c90498f3478597798a08892ed6f73d4c461c3f1ef5f41253c8" "https://congbao.chinhphu.vn/"
fetch "nd67-congbao-1019-1020" "https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2023/9/40096/46433-1-20231019-102067-2023-nd-cp.pdf" "456cbc7d4cbf8a0eeb3db989ac2edadd0ac9bb3a1fcd024ef4359dcd73b79d59" "https://congbao.chinhphu.vn/"
fetch "nd220-2026-congbao-367" "https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/3/469840-1782964220_v1_1783040868_signed.pdf" "ab0e75cdd5de3b3bc0e0ebc6d3fb03b87b9a4eebfe2658b57b0b16b3c11f3a52" "https://congbao.chinhphu.vn/"
