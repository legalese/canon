#!/usr/bin/env bash
# Expand (default) or check (--check) the source quotations of the given .l4 files against the four deposited sources.
# Run from the encoding directory:  tools/sq.sh [--check] FILE.l4 ...
set -eu
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
B="$HERE/../../registers/source-bundle"
MODE=""
if [ "${1:-}" = "--check" ]; then MODE="--check"; shift; fi
exec python3 -I "$HERE/tools/srcquote.py" $MODE \
  "ito=$B/income-tax-ordinance-new-version.he.wiki.txt" \
  "reg35=$B/regulations/income-tax-credit-for-immigrants-special-cases-rules-5738-1977.he.wiki.txt" \
  "reg47=$B/regulations/income-tax-deduction-of-payments-for-benefits-or-pension-regulations-5740-1980.he.wiki.txt" \
  "ral=$B/../../../retirement-age-law-5764-2004/registers/source-bundle/retirement-age-law-5764-2004.he.wiki.txt" \
  -- "$@"
