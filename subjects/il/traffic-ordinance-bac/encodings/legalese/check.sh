#!/bin/sh
# Run the English row of il/traffic-ordinance-bac, and prove the Hebrew row agrees with it.
#
#   BAC_L4=/path/to/l4 sh check.sh
#
# JL4_LIBRARY_PATH is deliberately UNSET below: the binary carries the standard library it
# was built with. Pointing an older binary at a newer prelude does not produce a version
# error; it produces a cascade of "could not find a definition" that reads as a broken
# encoding (l4-plugin scripts/install-l4.sh says the same).
#
# Built and checked 2026-09-22 on legalese/prereleases tag unstable-20260907-9d6536a
# (linux-x64, l4-ide commit 9d6536a). That binary predates `@lang` and `l4 nlg --lang`
# (l4-ide PR #432 of 2026-09-19), which is why neither row uses them: each row carries
# heralds in its own language only. See NOTES.md section 8.
L4=${BAC_L4:-l4}
unset JL4_LIBRARY_PATH
cd "$(dirname "$0")" || exit 1
command -v "$L4" >/dev/null 2>&1 || { echo "no l4 binary on PATH; set BAC_L4=/path/to/l4"; exit 2; }
status=0

# 1. Both modules run with zero errors, and the test module satisfies EVERY #ASSERT it
#    contains. Counting against the file, not against a number written here, catches an
#    assertion that was silently not evaluated.
for f in drink-driving.l4 drink-driving-tests.l4; do
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

# 2. The two lines that go on the slide, with the answers the binary actually gave.
#    Same rule, same driver, same reading; only the rule-effective date differs.
out=$("$L4" run drink-driving-tests.l4 2>&1)
printf '\n  the Roznai scenario -- a 22-year-old, 100 micrograms per litre of exhaled air:\n'
for d in '2010 12 8' '2010 12 9'; do
  line=$(grep -n "^#EVAL \`EVAL UNDER RULES EFFECTIVE AT\` (YMD $d) (\`the driver is intoxicated\`" drink-driving-tests.l4 | head -1 | cut -d: -f1)
  ans=$(printf '%s\n' "$out" | grep -A3 "^Evaluation\[[0-9]*\] @ drink-driving-tests.l4:$line:" | tail -1 | sed 's/^ *//')
  printf '    RULES EFFECTIVE AT %-12s -> %s\n' "$(echo $d | awk '{printf "%04d-%02d-%02d",$1,$2,$3}')" "$ans"
done
printf '\n'

# 3. The Hebrew-canonical twin at ../legalese-he is the SAME encoding renamed, and it
#    gives the SAME answers. Structural identity first (token for token through
#    glossary.json), then every Result block of the two test modules, in order.
if python3 ../../source/twin-check.py; then :; else status=1; fi
en=$(printf '%s\n' "$out" | grep -A1 '^Result:' | grep -v '^Result:$' | grep -v '^--$')
he=$("$L4" run ../legalese-he/drink-driving-tests-he.l4 2>&1 | python3 ../../source/twin-check.py --unmap \
     | grep -A1 '^Result:' | grep -v '^Result:$' | grep -v '^--$')
n=$(printf '%s\n' "$en" | grep -c .)
if [ -n "$en" ] && [ "$en" = "$he" ]; then
  printf '%-28s agrees with ../legalese-he/drink-driving-tests-he.l4  (%s Result blocks identical)\n' drink-driving-tests.l4 "$n"
else
  printf '%-28s DISAGREES with ../legalese-he/drink-driving-tests-he.l4\n' drink-driving-tests.l4; status=1
  printf '%s\n' "$en" > /tmp/bac-en-$$.txt; printf '%s\n' "$he" > /tmp/bac-he-$$.txt
  diff /tmp/bac-en-$$.txt /tmp/bac-he-$$.txt | head -40
  rm -f /tmp/bac-en-$$.txt /tmp/bac-he-$$.txt
fi
exit $status
