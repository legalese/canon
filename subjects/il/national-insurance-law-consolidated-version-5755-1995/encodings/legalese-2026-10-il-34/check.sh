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
# exactly as often as expected_refused says (0 for every module: row IL-34 declares no
# expected failure and no refused assertion; an #ASSERT REFUSED that is satisfied is
# counted as satisfied).
#
# Copied from ../legalese-2026-10-il-06/check.sh and changed (row IL-34, 2026-10-09): its
# comments on the other row's expected failures are removed; the logic is the same.
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
L4="${L4:-l4}"

# A module that is MEANT to fail is listed here with its exact count. Row IL-34 has none.
expected_failed() {
  case "$1" in
    # fid-il-34: C143 to C147 (lines 220-223 and 225 of tests-independent.l4) divide by the PRINTED total 14.60; the list form of s 28(a) divides by the sum of the cells given
    # (14.49). Version 0.1.1 makes that a named switch (fork R1) for a caller that gives the printed total; the plain list form stays at the cells, so these 5 still fail by design.
    tests-independent.l4) echo 5 ;;
    *) echo 0 ;;
  esac
}

# A module that is MEANT to refuse some assertions is listed with its exact count. Row IL-34 has none.
expected_refused() {
  case "$1" in
    # fid-il-34: C269 (AMBIGUITY, line 326) is refused by fork C1. C013 (line 129) was refused until version 0.1.1 and now passes (the Order does not apply to 31.12.1998).
    tests-independent.l4) echo 1 ;;
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
