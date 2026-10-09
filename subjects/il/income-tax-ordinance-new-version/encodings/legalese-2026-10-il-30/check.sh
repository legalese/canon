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
# version 0.2.0, repair CHK-03).
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
L4="${L4:-l4}"

# A module that is MEANT to fail (a draft's test cases run against the text as made, say) is listed here with its exact
# count, and named in encoding.json `expected_red`. Row IL-30's own tests have none: every refusal they make is asserted with
# `#ASSERT REFUSED ... BECAUSE "..."`, which counts as satisfied. Only the independent tester's module (tests-independent.l4, frozen) is listed.
expected_failed() {
  case "$1" in
    # tests-independent.l4 (fid-il-30, row IL-56). Version 0.1.1 repair: of its 11 declared failures at 0.1.0, 10 are resolved and 1 remains.
    #   line 1307 BT10  TESTER-WRONG   decided 25% on the middle part for a material shareholder (that uplift is ITO s 91(b1)(1)(a)(2), not RE Tax Law s 48A(b1)(1)(b)); the
    #                   encoding is right (INDEPENDENT-FINDINGS.md section 2). Left failing, value unchanged.
    #   Resolved by 0.1.1 and now satisfied: DV12 (line 781, the third reading "at any time" added to forks D1 and D2, default declines); BT09, BT11, BT12 (lines 1305, 1309, 1311) and
    #   BT19, BT20, BT22, BT23 (lines 1325, 1327, 1331, 1333) (the RE Tax Law's day counts: the parts now partition the days under every reading, and the Transition Day reading is named).
    tests-independent.l4) echo 1 ;;
    *) echo 0 ;;
  esac
}

# A module that is MEANT to refuse some assertions (an `#ASSERT` whose expression refuses, shown as a Warning) is listed
# with its exact count.
expected_refused() {
  case "$1" in
    # tests-independent.l4 (fid-il-30, row IL-56): 10 declared refusals where the tester decided a value. At 0.1.0 there were 17.
    #   lines 543, 545 CG20; 553 CG22   SCOPE   the s 88 parts of the real gain for a sale before the fixed date or the change date are declined, though s 88 has no date limit
    #   lines 680 T30; 1319 BT16; 1321 BT17   SCOPE   a sale before 1 January 2012 (assumption A6)
    #   line 702 T49   AMBIGUITY (new at 0.1.1, was a failure)   a right bought and sold in the same tax year: the text does not say whether the empty period of ownership gives no tax year or one (fork 30-F19); declined by default
    #   line 799 DV21   AMBIGUITY   a dividend on 29 February 2024 and a holding on 28 February 2023: the 12-month boundary (the encoding is right to decline)
    #   line 1342 BT27  AMBIGUITY (new at 0.1.1, was a failure)   s 48A(b4) with a 2005 purchase: (b4) and (b1) collide (fork 30-F20); declined by default
    #   line 1477 PT54  SCOPE   the (c1a)(1) window before July 2013: its printed amounts were indexed every 16 January while it ran and the indices are not supplied
    #   Resolved by 0.1.1 and now satisfied (they were SCOPE refusals): PT37, PT43, PT44, PT45, PT47 (the 2022 to 2024 columns), PT48, PT49, PT51 (the 2013 column and the (c1b)(2) scale), PT53 ((c1b)(1)).
    tests-independent.l4) echo 10 ;;
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
