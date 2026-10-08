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
# version 0.2.0, as row IL-04's check.sh does from its version 0.3.0).
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
L4="${L4:-l4}"

# A module that is MEANT to fail (a draft's test cases run against the text as made,
# say) is listed here with its exact count, and named in encoding.json `expected_red`.
expected_failed() {
  case "$1" in
    # tests-red.l4) echo 3 ;;
    # Version 0.2.0 (2026-10-08, BACKLOG IL-19, inventory CHK-08i): the independent tester's module.
    # Five assertions remain failed, each an item of findings/il-2026-10-08/inventory.tsv:
    #   line 92  D019  (08i-D019, AMBIGUITY, fork F34): REFUSED expected of the record alone, which
    #                 carries no later tax year; the form that takes them declines (ito-s1-israeli-resident.l4)
    #   line 676 D190, lines 767-768 D236 (08i-D190, AMBIGUITY, fork F35, waits on BACKLOG IL-24):
    #                 REFUSED expected; the deduction is taken first, as in version 0.1.0
    #                 (version 0.4.0: these three pass; see below)
    #   line 779 D244 (08i-T1, TESTER-WRONG): the tester's facts contradict each other
    # D187 (line 667) and D055 (line 201) passed from version 0.2.0. Lines 286 and 860 were adapted in
    # place to version 0.3.0's interfaces (the lead's note at the end of the file); their assertions pass.
    # Version 0.4.0 (BACKLOG IL-42, Meng's ruling SHRUG on fork F35): the s 47 deduction declines by
    # default where the order of the deduction and the s 45A credit changes the answer, so D190 (676)
    # and D236 (767, 768), which expect that refusal, pass. Two remain: D019 (92) and D244 (779).
    tests-independent.l4) echo 2 ;;
    *) echo 0 ;;
  esac
}

# Version 0.2.0: a module that is MEANT to refuse some assertions is listed with its exact count.
expected_refused() {
  case "$1" in
    # The independent tester's module: seven values for tax years before 2024, which every rule of
    # this row declines (NOTES.md assumption A1; inventory 08i-T2, TESTER-WRONG (scope)): lines 153
    # (D040), 177 (D047), 180 (D048), 183 (D049), 190 (D052), 193 and 195 (D053). D183 (line 659)
    # was answered from version 0.2.0.
    tests-independent.l4) echo 7 ;;
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
