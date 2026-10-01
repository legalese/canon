#!/usr/bin/env bash
# Run every .l4 module in this encoding and print, per module: error diagnostics,
# assertions satisfied, assertions failed, assertions refused.
#
# Adapted from the encoding-a-subject skill's assets/check.sh, which undercounts in two
# ways that the independent test pass of this encoding found (NOTES.md section 6):
#   * `#ASSERT REFUSED e` where e produces a value prints "Message:" and then, on the
#     NEXT line, "assertion failed: expected a refusal, ...". The skill's grep, which
#     wants "assertion failed" on the Message line, misses it.
#   * `#ASSERT e` where e refuses prints "assertion refused" at Warning severity. The
#     skill's script counts it nowhere, so a refusing assertion looks green.
# This script reads the line after every "Message:" and counts both. The same fix to
# the skill's asset is legalese/l4-ide#533. This script also counts
# "assertion could not be evaluated" as a failure.
#
# Why not trust the exit code: `l4 run` exits 0 when an #ASSERT fails or refuses.
#
# Expected failures: tests-independent.l4 carries exactly 1 failing assertion on purpose
# (scenario P-19, the alternative reading of 22757.3.1(a)(2)(B)(iii), fork F16).
#
# Usage:  check.sh [DIR]          (DIR defaults to the directory this script is in)
# Env:    L4   the l4 binary      (default: `l4` on PATH); leave JL4_LIBRARY_PATH unset
#
# Exit status: 0 only when no module has an error other than its expected failed
# assertions, no assertion refused, and every module fails exactly as often as expected.
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
L4="${L4:-l4}"

expected_failed() {
  case "$1" in
    tests-independent.l4) echo 1 ;;
    *) echo 0 ;;
  esac
}

if ! command -v "$L4" >/dev/null 2>&1; then
  echo "check.sh: no l4 binary at '$L4'. Set L4=/path/to/l4 or put l4 on PATH." >&2
  exit 2
fi

status=0 total_err=0 total_ok=0 total_bad=0 total_ref=0 n=0
printf '%-26s %7s %9s %7s %8s %9s\n' module errors satisfied failed refused expected
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
  printf '%-26s %7d %9d %7d %8d %9d\n' "$m" "$err" "$ok" "$bad" "$ref" "$exp"
  [ $((err - bad)) -eq 0 ] && [ "$ref" -eq 0 ] && [ "$bad" -eq "$exp" ] || status=1
  total_err=$((total_err + err)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad)) total_ref=$((total_ref + ref)) n=$((n + 1))
done
printf '%-26s %7d %9d %7d %8d\n' "TOTAL ($n modules)" "$total_err" "$total_ok" "$total_bad" "$total_ref"
echo "(a failed assertion is also an error; any error that is not a failed assertion, or any refused assertion, makes the run red)"
exit $status
