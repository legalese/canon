#!/usr/bin/env bash
# Run every .l4 module of this row and print, per module, the numbers that matter:
# error diagnostics, assertions satisfied, assertions failed, assertions refused.
#
# This is the encoding-a-subject skill's check.sh with two changes for a composed row:
#   1. it first runs `vendor.sh --check`, and stops if a vendored copy of a composed row's
#      module is missing or differs from its source or from VENDORED.sha256;
#   2. it runs only this row's own modules: the vendored copies are checked as the imports
#      of these, and their own rows report their numbers.
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
# Exit status: 0 only when the vendored copies check, no module has an error other than
# its expected failed assertions, and each module fails exactly as often as expected_failed
# says and refuses exactly as often as expected_refused says (0 for every module but the
# independent tests, version 0.2.0). On this machine a full run takes several minutes:
# the modules that reach row IL-06 are slow.
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
L4="${L4:-l4}"

# A module that is MEANT to fail is listed here with its exact count, and named in
# encoding.json `expected_red`.
expected_failed() {
  case "$1" in
    il07-tests-expected-red.l4) echo 4 ;;   # NOTES.md section 6: R1 (2), R2 (1), R3 (1, added in 0.2.0)
    tests-independent.l4) echo 18 ;;         # the independent tester's record against v0.1.0, not edited: 15 reworded refusals, H43's tax, H45's two; NOTES.md 11.8, 11.13
    *) echo 0 ;;
  esac
}

# Version 0.2.0: the independent tests, written against version 0.1.0 and never edited,
# carry assertions that version 0.2.0 refuses where 0.1.0 answered (NOTES.md section 11).
# Every other module must refuse nothing.
expected_refused() {
  case "$1" in
    tests-independent.l4) echo 2 ;;          # H44n's allowance and net: NII s 72 and fork K15
    *) echo 0 ;;
  esac
}

if ! command -v "$L4" >/dev/null 2>&1; then
  echo "check.sh: no l4 binary at '$L4'. Set L4=/path/to/l4 or put l4 on PATH." >&2
  exit 2
fi

"$DIR/vendor.sh" --check || { echo "check.sh: vendored modules do not check; run vendor.sh (see its messages)" >&2; exit 2; }

vendored="$(grep -v '^#' "$DIR/VENDORED.sha256" | awk '{print $3}')"

status=0 total_err=0 total_ok=0 total_bad=0 total_ref=0 n=0
printf '%-40s %7s %9s %7s %8s %9s\n' module errors satisfied failed refused expected
for f in "$DIR"/*.l4; do
  [ -e "$f" ] || { echo "check.sh: no .l4 files in $DIR" >&2; exit 2; }
  m="$(basename "$f")"
  if printf '%s\n' "$vendored" | grep -qxF "$m"; then continue; fi
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
exit $status
