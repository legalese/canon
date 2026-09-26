#!/usr/bin/env bash
# Re-fetch the consolidated Penal Law from the Open Book of Laws (Hebrew Wikisource).
# Records the revision it fetched so the deposit can be compared against a later one.
# Usage: source/fetch.sh [revid]   -- with a revid, fetches that exact revision (oldid).
set -euo pipefail
cd "$(dirname "$0")"
UA="l4-canon/1.0 (https://github.com/legalese/canon)"
TITLE='%D7%97%D7%95%D7%A7_%D7%94%D7%A2%D7%95%D7%A0%D7%A9%D7%99%D7%9F'   # חוק_העונשין
API='https://he.wikisource.org/w/api.php'
if [ "${1:-}" ]; then OLD="&oldid=$1"; else OLD=""; fi
curl -sf -A "$UA" "https://he.wikisource.org/w/index.php?title=$TITLE&action=raw$OLD" -o penal-law-1977.wikitext
curl -sf -A "$UA" "$API?action=query&prop=revisions&titles=$TITLE&rvprop=ids|timestamp|user|comment|size&rvlimit=1&format=json" \
  | python3 -c 'import json,sys; r=[p for p in json.load(sys.stdin)["query"]["pages"].values()][0]["revisions"][0]; print(json.dumps(r, ensure_ascii=False))' \
  > revision.json
curl -sf -A "$UA" "$API?action=parse&page=$TITLE&prop=text&format=json${OLD:+&oldid=$1}" \
  | python3 - <<'PY'
import json,re,html,sys
h=json.load(sys.stdin)['parse']['text']['*']
h=re.sub(r'<(script|style)[^>]*>.*?</\1>','',h,flags=re.S)
h=re.sub(r'<br\s*/?>','\n',h)
h=re.sub(r'</(p|div|li|tr|h[1-6]|table|section)>','\n',h)
h=re.sub(r'<td[^>]*>',' | ',h)
t=html.unescape(re.sub(r'<[^>]+>','',h))
t=re.sub(r'[ \t ]+',' ',t); t=re.sub(r'\n\s*\n+','\n\n',t).strip()
open('penal-law-1977.txt','w',encoding='utf-8').write(t+'\n')
PY
shasum -a 256 penal-law-1977.wikitext penal-law-1977.txt | tee SHA256SUMS
cat revision.json
