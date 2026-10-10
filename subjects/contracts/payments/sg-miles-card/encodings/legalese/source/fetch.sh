#!/usr/bin/env bash
# Fetches the issuer documents this row encodes, from the issuers' own URLs.
# Nothing here redistributes them: registers/source-bundle.json pins each by
# url + sha256, and this script refuses any file whose bytes differ, so an
# issuer's silent revision is a loud failure here rather than a quiet change
# under the encoding. Writes raw/<id>.pdf and its `pdftotext -layout`
# rendering raw/<id>.txt, which gen-womans-tables.py reads. raw/ is ignored.
set -uo pipefail
cd "$(dirname "$0")"
mkdir -p raw
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'
bad=0
while IFS=$'\t' read -r id url sha; do
  curl -sSL --max-time 60 -A "$UA" -o "raw/$id.pdf" "$url" || { echo "FETCH FAILED  $id  $url"; bad=1; continue; }
  got=$(shasum -a 256 "raw/$id.pdf" | cut -c1-64)
  if [ "$got" = "$sha" ]; then
    pdftotext -layout "raw/$id.pdf" "raw/$id.txt" && echo "ok            $id"
  else
    echo "DIGEST DIFFERS $id  recorded $sha  got $got  — the issuer has revised it; re-read before trusting the encoding"
    bad=1
  fi
done < <(python3 -c '
import json
for d in json.load(open("../registers/source-bundle.json"))["documents"]:
    print(d["id"], d["url"], d["integrity"]["sha256"], sep="\t")')
exit $bad
