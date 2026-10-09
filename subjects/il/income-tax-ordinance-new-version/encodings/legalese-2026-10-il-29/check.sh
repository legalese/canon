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
    # fid-il-29 (IL-56): 8 independent assertions that assert the tester's decided answer and fail against the encoding;
    # lines of tests-independent.l4 (see INDEPENDENT-FINDINGS.md): B06 (175, assumption A3), J08 (664, note-only cap), J32 (666,
    # other motorcycle), J31 (668, note-only L3 amount), K08/K09/K07 (681-683, note-only reductions), L12 (726, note-only ceiling).
    tests-independent.l4) echo 8 ;;
    *) echo 0 ;;
  esac
}

# Row IL-29: no module is meant to refuse an assertion (every refusal is asserted with #ASSERT REFUSED ... BECAUSE,
# which counts as satisfied).  Version 0.1.0 has no independent-tests module yet.
expected_refused() {
  case "$1" in
    # fid-il-29 (IL-56): 8 independent assertions where the tester decided an answer and the encoding refuses by design:
    # A34 (128, fork C2), A35 (131, fork C1), A36 (134, fork C1), C34/C35 default (288, TESTER-WRONG: s 75A circularity),
    # G02 default (462, fork N90), K13 (687, no cap for 2029), L15 default (721, fork XD), L07 (724, workplace-only phone).
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

# Row IL-29 (as row IL-28): every Hebrew run in the encoding must occur in a deposited source, and every `-- src:TAG:N |`
# quotation must equal the reduction of line N of source TAG (tools/hebcheck.py).
if command -v python3 >/dev/null 2>&1; then
  python3 -I "$DIR/tools/hebcheck.py" "$DIR"/*.l4 || status=1
else
  echo "check.sh: python3 not found; the Hebrew quotation check was not run" >&2
  status=1
fi
exit $status
