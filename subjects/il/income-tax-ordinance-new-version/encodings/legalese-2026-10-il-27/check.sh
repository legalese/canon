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
# assertions, no assertion refused, and each module fails exactly as often as
# expected_failed says.
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
L4="${L4:-l4}"

# A module that is MEANT to fail (a draft's test cases run against the text as made,
# say) is listed here with its exact count, and named in encoding.json `expected_red`.
expected_failed() {
  case "$1" in
    # tests-red.l4) echo 3 ;;
    # tests-independent.l4: three assertions of the independent test author (fid-il-27) are EXPECTED to fail, by line:
    #   476  H07  s 44 income 188,001 over the 188,000 ceiling, expected 0, the encoding computes 12,774.95625 (SCOPE: the ceiling is a caller input)
    #   499  I07  s 46 25,000 + 10,000 carried against the 30,000 cap, expected a refusal, the encoding answers 10,500 (TESTER-WRONG)
    #   526  J11  s 47(b1) 26,436 paid, expected 12,804, the encoding gives 0 (AMBIGUITY: 16% of 165,228 is 26,436.48)
    tests-independent.l4) echo 3 ;;
    *) echo 0 ;;
  esac
}

# A module that is MEANT to refuse some assertions (an assertion whose expected value the encoding declines to give).
expected_refused() {
  case "$1" in
    # tests-independent.l4: eight assertions are EXPECTED to refuse (v0.1.1: E20 371, F39 416 and F52 451 below now answer; they were over-declines
    # and were repaired, so the declared count is 11 - 3 = 8). By line, case id and class:
    #   294 A17, 295 A18  pre-2022 oleh in tax years 2022 and 2023: tax year before 2024 (SCOPE)
    #   356 E12  s 39B reading T, 29 days: 'says nothing of 20 to 29 days' (AMBIGUITY)
    #   (371 E20, repaired in v0.1.1: now answers 4)
    #   389 F23  s 40B born 15 June 2010 at the default: declined (AMBIGUITY; tester decided one reading with low weight)
    #   (416 F39, repaired in v0.1.1: now answers 1)
    #   437 F47, 438 F48, 439 F48  s 40D old-text cases in tax years 2023, 2019, 2020: tax year before 2024 (SCOPE)
    #   (451 F52, repaired in v0.1.1: now answers 1)
    #   465 G07  s 41 registered spouse: declined, expected 0 (AMBIGUITY of presentation: outside s 41)
    tests-independent.l4) echo 8 ;;
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
  printf '%-40s %7d %9d %7d %8d %9d\n' "$m" "$err" "$ok" "$bad" "$ref" "$exp"
  [ $((err - bad)) -eq 0 ] && [ "$ref" -eq "$expref" ] && [ "$bad" -eq "$exp" ] || status=1
  total_err=$((total_err + err)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad)) total_ref=$((total_ref + ref)) n=$((n + 1))
done
printf '%-40s %7d %9d %7d %8d\n' "TOTAL ($n modules)" "$total_err" "$total_ok" "$total_bad" "$total_ref"
echo "(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)"
exit $status
