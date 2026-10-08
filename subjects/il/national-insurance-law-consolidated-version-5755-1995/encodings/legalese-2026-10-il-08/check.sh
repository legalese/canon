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
# Exit status: 0 only when no module has an error other than its expected failed
# assertions, and each module fails exactly as often as expected_failed says and refuses
# exactly as often as expected_refused says (0 for every module but the ones it names;
# version 0.2.0, as row IL-04's check.sh).
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
L4="${L4:-l4}"

# A module that is MEANT to fail (a draft's test cases run against the text as made,
# say) is listed here with its exact count, and named in encoding.json `expected_red`.
# Version 0.2.0 (BACKLOG IL-20): the independent tester's module, tests-independent.l4.
# Its remaining failure, an #ASSERT REFUSED that gets a value:
#   line 247  72-57 recorded as not paid: fork N2, inventory 08n-N2 (AMBIGUITY, waits on a ruling)
# Line 248 (72-57 recorded as paid, inventory 08n-PAID) passes from 0.2.0.
# Version 0.3.0 (BACKLOG IL-41): lines 733, 735 and 737 (D-46 to D-48, a day the later month lacks;
# fork N4, inventory DATE) pass: Meng ruled on 2026-10-08 (SHRUG) that such a day is declined by
# default. They were failing from 0.1.0 to 0.2.0, when the day was clamped. 4 became 1.
expected_failed() {
  case "$1" in
    # tests-red.l4) echo 3 ;;
    tests-independent.l4) echo 1 ;;   # line 247 (08n-N2); 733, 735, 737 (DATE) pass from 0.3.0
    *) echo 0 ;;
  esac
}

# Version 0.2.0: a module that is MEANT to refuse some assertions is listed with its exact count.
# tests-independent.l4 refuses 22 assertions, all of one cause and one class, SCOPE (inventory
# 08n-A2, AMBIGUITY (scope); assumption A2, the lead's choice, assumed, not ruled): this row answers
# months from May 2015, and the tester decided that s 72's untagged text answers them. Not tester
# error: the tester's values stand as its reading of s 72 for 1995-2015, and these are the assertions
# to re-check if the scope is ever widened to the Law's commencement (s 402, 1 October 1995).
# All 22 meet the reworded refusal, "this row answers months of the child allowance from May 2015,
# a scope chosen to compose with row IL-06, not the commencement of the Law (s 402: 1 October 1995)".
#   lines 120, 171       the export asked about October 1995 (72-14) and May 2008 (72-30), as in 0.1.0
#   lines 122, 167-205   the first-month rule, and the months-paid count built on it, for October 1995
#                        (72-14) and for children born 2007-2010 (72-30 to 72-39): lines 122, 167, 169,
#                        173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201,
#                        203, 205. Answered in 0.1.0 because the period was applied only on the
#                        export; refused from 0.2.0, which applies it to every rule that gives a month
#                        (inventory 08n-GATE). Class SCOPE (08n-A2), as lines 120 and 171.
expected_refused() {
  case "$1" in
    tests-independent.l4) echo 22 ;;   # lines 120, 122, 167-205: SCOPE (08n-A2; the last twenty surfaced by 08n-GATE)
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
exit $status
