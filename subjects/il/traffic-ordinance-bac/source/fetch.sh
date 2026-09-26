#!/usr/bin/env bash
# Re-fetch the deposited sources at their PINNED revisions and re-check the digests.
# Usage: source/fetch.sh
# Wikimedia rate-limits aggressively: descriptive User-Agent, serial fetches, a pause between.
set -euo pipefail
cd "$(dirname "$0")"
UA="l4-canon/1.0 (https://github.com/legalese/canon)"
W='https://he.wikisource.org/w/index.php'
get() { curl -sfL --retry 3 --retry-delay 10 -A "$UA" "$1" -o "$2"; sleep 3; }
get "$W?title=%D7%A4%D7%A7%D7%95%D7%93%D7%AA_%D7%94%D7%AA%D7%A2%D7%91%D7%95%D7%A8%D7%94&action=raw&oldid=3081544" traffic-ordinance.wiki
get "$W?title=%D7%AA%D7%A7%D7%A0%D7%95%D7%AA_%D7%94%D7%AA%D7%A2%D7%91%D7%95%D7%A8%D7%94&action=raw&oldid=3081414" traffic-regulations.wiki
get "https://fs.knesset.gov.il/18/law/18_lsr_301018.pdf" sefer-hachukim-2265-p91-amendment-97.pdf
get "https://olaw.org.il/takanot/takanot-6825.pdf" kovetz-hatakanot-6825-p114.pdf
sha256sum -c SHA256SUMS
