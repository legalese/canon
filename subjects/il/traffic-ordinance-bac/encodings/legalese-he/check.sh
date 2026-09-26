#!/bin/sh
# Run the HEBREW-CANONICAL row of il/traffic-ordinance-bac, and prove it agrees with the
# English row at ../legalese, which is the oracle.
#
#   BAC_L4=/path/to/l4 sh check.sh
#
# JL4_LIBRARY_PATH is deliberately UNSET: the binary's embedded standard library is the one
# matched to it. Checked 2026-09-22 on legalese/prereleases unstable-20260907-9d6536a
# (linux-x64). The twin of this file is ../legalese/check.sh; either one runs the
# cross-row comparison, so running both is belt and braces, not a requirement.
L4=${BAC_L4:-l4}
unset JL4_LIBRARY_PATH
cd "$(dirname "$0")" || exit 1
command -v "$L4" >/dev/null 2>&1 || { echo "no l4 binary on PATH; set BAC_L4=/path/to/l4"; exit 2; }
status=0

# 1. Zero errors, and every #ASSERT in the file satisfied.
for f in drink-driving-he.l4 drink-driving-tests-he.l4; do
  out=$("$L4" run "$f" 2>&1)
  bad=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  ok=$(printf '%s\n' "$out" | grep -c '^  assertion satisfied')
  want=$(grep -c '^#ASSERT' "$f")
  if [ "$bad" -eq 0 ] && [ "$ok" -eq "$want" ]; then
    printf '%-28s ok  (%s of %s assertions satisfied)\n' "$f" "$ok" "$want"
  else
    printf '%-28s FAIL: %s errors, %s of %s assertions satisfied\n' "$f" "$bad" "$ok" "$want"; status=1
    printf '%s\n' "$out" | grep -B2 -A10 'DiagnosticSeverity_Error' | head -60
  fi
done

# 2. The slide lines, in Hebrew: same rule, same driver, same reading, two dates.
out=$("$L4" run drink-driving-tests-he.l4 2>&1)
printf '\n  התרחיש של רוזנאי – נהג בן 22, 100 מיקרוגרם אלכוהול בליטר אוויר נשוף:\n'
for d in '2010 12 8' '2010 12 9'; do
  line=$(grep -n "^#EVAL \`EVAL UNDER RULES EFFECTIVE AT\` (YMD $d) (\`הנהג שיכור\`" drink-driving-tests-he.l4 | head -1 | cut -d: -f1)
  ans=$(printf '%s\n' "$out" | grep -A3 "^Evaluation\[[0-9]*\] @ drink-driving-tests-he.l4:$line:" | tail -1 | sed 's/^ *//')
  printf '    RULES EFFECTIVE AT %-12s -> %s\n' "$(echo $d | awk '{printf "%04d-%02d-%02d",$1,$2,$3}')" "$ans"
done
printf '\n'

# 3. Structural identity with the English row through glossary.json, then every Result
#    block of the two test modules compared in order after mapping this row's names back.
if python3 ../../source/twin-check.py; then :; else status=1; fi
he=$(printf '%s\n' "$out" | python3 ../../source/twin-check.py --unmap | grep -A1 '^Result:' | grep -v '^Result:$' | grep -v '^--$')
en=$("$L4" run ../legalese/drink-driving-tests.l4 2>&1 | grep -A1 '^Result:' | grep -v '^Result:$' | grep -v '^--$')
n=$(printf '%s\n' "$en" | grep -c .)
if [ -n "$en" ] && [ "$en" = "$he" ]; then
  printf '%-28s agrees with ../legalese/drink-driving-tests.l4  (%s Result blocks identical)\n' drink-driving-tests-he.l4 "$n"
else
  printf '%-28s DISAGREES with ../legalese/drink-driving-tests.l4\n' drink-driving-tests-he.l4; status=1
  printf '%s\n' "$en" > /tmp/bac-en-$$.txt; printf '%s\n' "$he" > /tmp/bac-he-$$.txt
  diff /tmp/bac-en-$$.txt /tmp/bac-he-$$.txt | head -40
  rm -f /tmp/bac-en-$$.txt /tmp/bac-he-$$.txt
fi
exit $status
