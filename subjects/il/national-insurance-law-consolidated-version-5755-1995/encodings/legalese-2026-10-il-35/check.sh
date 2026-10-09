#!/usr/bin/env bash
# Run every .l4 module in an encoding and print, per module, the numbers that matter:
# error diagnostics, assertions satisfied, assertions failed, assertions refused.
#
# Why not trust the exit code: `l4 run` exits 0 when an #ASSERT fails AND when it
# refuses. An encoding that "ran green" by exit code can be carrying either.
#
# Why read the line AFTER "Message:": l4 prints some outcomes on the Message line
# itself ("Message:  assertion failed") and others on the next one:
#   * `#ASSERT REFUSED e` where e produces a value: "assertion failed: expected a
#     refusal, but the expression produced a value" (Error severity);
#   * `#ASSERT e` where e REFUSES: "assertion refused: ..." (Warning severity, so it
#     never shows up as an error at all).
# A script that greps the Message line alone undercounts the first and never sees the
# second; a refusing assertion then looks green.
#
# Usage:  check.sh [DIR]          (DIR defaults to the directory this script is in)
# Env:    L4   the l4 binary      (default: `l4` on PATH)
#
# Row IL-35 (version 0.1.0): no module is expected to fail or to refuse; after the modules it runs tools/ (regenerate-and-diff of the
# published-figures module, a spot-check of the tests against the JSON, and the Hebrew check).
#
# Exit status: 0 only when no module has an error other than its expected failed
# assertions, and each module fails exactly as often as expected_failed says and refuses
# exactly as often as expected_refused says (0 for every module but the ones it names;
# version 0.2.0, as row IL-04's check.sh does).
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
L4="${L4:-l4}"

# A module that is MEANT to fail (a draft's test cases run against the text as made,
# say) is listed here with its exact count, and named in encoding.json `expected_red`.
expected_failed() {
  case "$1" in
    *) echo 0 ;;
  esac
}

# Every assertion that expects a refusal is written #ASSERT REFUSED (a satisfied assertion), so no module is
# expected to have a refused (unsatisfied) assertion either.
expected_refused() {
  case "$1" in
    *) echo 0 ;;
  esac
}

if ! command -v "$L4" >/dev/null 2>&1; then
  echo "check.sh: no l4 binary at '$L4'. Set L4=/path/to/l4 or put l4 on PATH." >&2
  exit 2
fi

status=0 total_err=0 total_ok=0 total_bad=0 total_ref=0 n=0
printf '%-40s %7s %9s %7s %8s %9s\n' module errors satisfied failed refused expected
for f in "$DIR"/*.l4; do
  [ -e "$f" ] || { echo "check.sh: no .l4 files in $DIR" >&2; exit 2; }
  m="$(basename "$f")"
  out="$("$L4" run "$f" 2>&1)"
  msgs="$(printf '%s\n' "$out" | grep -A1 -E '^[[:space:]]*Message:')"
  err=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  ok=$(printf '%s\n' "$msgs" | grep -cE 'assertion satisfied')
  bad=$(printf '%s\n' "$msgs" | grep -cE 'assertion failed|assertion could not be evaluated')
  ref=$(printf '%s\n' "$msgs" | grep -cE 'assertion refused')
  exp=$(expected_failed "$m")
  expref=$(expected_refused "$m")
  if [ "$expref" -eq 0 ]; then shown="$exp"; else shown="$exp/$expref"; fi
  printf '%-40s %7d %9d %7d %8d %9s\n' "$m" "$err" "$ok" "$bad" "$ref" "$shown"
  [ $((err - bad)) -eq 0 ] && [ "$ref" -eq "$expref" ] && [ "$bad" -eq "$exp" ] || status=1
  total_err=$((total_err + err)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad)) total_ref=$((total_ref + ref)) n=$((n + 1))
done
printf '%-40s %7d %9d %7d %8d\n' "TOTAL ($n modules)" "$total_err" "$total_ok" "$total_bad" "$total_ref"
echo "(a failed assertion is also an error; any other error, or a refused assertion a module is not expected to have, makes the run red; \"expected\" is failed/refused where a module may refuse)"

# The tools: regenerate the published-figures module and diff it; cross-check the tests against the JSON;
# check every run of Hebrew against the deposited texts.
ENC="$DIR"
SB="$ENC/../../registers/source-bundle"
ITO="$ENC/../../../income-tax-ordinance-new-version/registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt"
NII="$SB/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt"
echo "-- tools"
python3 -I "$ENC/tools/gen_published_figures.py" --check || status=1
python3 -I "$ENC/tools/spotcheck_tests.py" | tail -2 || status=1
python3 -I "$ENC/tools/hebcheck.py" "$ITO" "$ENC/cpi-il35-nouns.l4" "$ENC/cpi-il35-published-figures.l4" "$ENC/cpi-il35-index-rules.l4" "$ENC/ito-s120b-index.l4" "$ENC/cpi-il35-tests.l4" && echo "hebcheck (ITO text): ok" || status=1
python3 -I "$ENC/tools/hebcheck.py" "$NII" "$ENC/nii-s334-index.l4" && echo "hebcheck (NII text): ok" || status=1
exit $status
