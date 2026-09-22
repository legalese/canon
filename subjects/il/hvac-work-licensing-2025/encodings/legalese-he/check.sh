#!/bin/sh
# Run the HEBREW-CANONICAL row with an l4 binary and the prelude that MATCHES it.
# l4-ide CLAUDE.md section 3.1: never point an l4 binary at a prelude newer than itself.
#
#   HVAC_L4=/path/to/l4 HVAC_LIBS=/path/to/jl4-core/libraries sh check.sh
#
# With neither variable set, JL4_LIBRARY_PATH is left UNSET and the binary uses its own
# EMBEDDED standard library, which is always the one that matches it. Set HVAC_LIBS only
# when you are running a binary built from a worktree and want that worktree's libraries.
# Pointing an l4 at a prelude newer than itself does not report a version mismatch; it
# fails as a cascade of `could not find a definition`.
# The binary must carry `l4 nlg --lang` (l4-ide unstable at or after PR #432).
#
# This row is GENERATED from ../legalese by ../../source/revoice.py. Nothing here is
# hand-written, so a failure is a bug in that script or in glossary.json -- or, more
# usefully, a sign that the English row moved and this one has not been regenerated.
# The twin of this file is ../legalese/check.sh; run both.
WT=${HVAC_L4_WORKTREE:-/Users/mengwong/src/legalese/l4wt/smart-quotes}
L4=${HVAC_L4:-$WT/dist-newstyle/build/aarch64-osx/ghc-9.10.3/jl4-0.1/x/l4/build/l4/l4}
if [ -n "${HVAC_LIBS:-}" ]; then export JL4_LIBRARY_PATH="$HVAC_LIBS"; else unset JL4_LIBRARY_PATH; fi
cd "$(dirname "$0")" || exit 1
status=0

# The linearizer's own connective vocabulary is English in every language: `with`, `and`,
# `is equal to`, `not`, and the trace frame. A tag names a rendering; it does not localise
# the frame around it. So the herald-purity checks below strike these out before looking.
CONNECTIVES='^(with|and|is|equal|to|not|executing|contract|at|the|following|events|party|did)$'

# 1. Green files: zero errors, and every assertion satisfied.
for f in hvac-law-he.l4 hvac-fees-he.l4 hvac-tests-simplex-he.l4 hvac-tests-generated-he.l4; do
  [ -f "$f" ] || { printf '%-32s MISSING\n' "$f"; status=1; continue; }
  out=$("$L4" run "$f" 2>&1)
  bad=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  ok=$(printf '%s\n' "$out" | grep -c '^  assertion satisfied')
  printf '%-32s %s  (%s assertions satisfied)\n' "$f" "$([ "$bad" -eq 0 ] && echo ok || echo "$bad ERRORS")" "$ok"
  [ "$bad" -eq 0 ] || { status=1; printf '%s\n' "$out" | grep -B6 'DiagnosticSeverity_Error' | head -60; }
done

# 2. The red file is the positive control: EXACTLY 3 failed assertions, no other error.
f=hvac-tests-simplex-red-he.l4
out=$("$L4" run "$f" 2>&1)
bad=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
failed=$(printf '%s\n' "$out" | grep -c '^  assertion failed')
if [ "$bad" -eq 3 ] && [ "$failed" -eq 3 ]; then
  printf '%-32s ok  (fails on exactly 3 assertions, as intended)\n' "$f"
else
  printf '%-32s WRONG: %s errors, %s failed assertions (expected 3 and 3)\n' "$f" "$bad" "$failed"; status=1
fi

# 3. Renderings. This row is the mirror of ../legalese: HEBREW by default, English on
#    request. Identifiers are Hebrew in BOTH renderings -- that is what makes the row
#    Hebrew-canonical -- so the check strips every backticked name before judging the
#    language of the herald around it.
for m in hvac-law-he hvac-fees-he; do
  he_english=$("$L4" nlg "$m.l4" 2>/dev/null | sed 's/`[^`]*`/ /g' \
                 | grep -o '[A-Za-z][A-Za-z]*' | sort -u | grep -vE "$CONNECTIVES")
  en_hebrew=$("$L4" nlg --lang en "$m.l4" 2>/dev/null | sed 's/`[^`]*`/ /g' | grep -c '[א-ת]')
  he_lines=$("$L4" nlg "$m.l4" 2>/dev/null | grep -c '[א-ת]')
  en_lines=$("$L4" nlg --lang en "$m.l4" 2>/dev/null | wc -l | tr -d ' ')
  printf '%-32s nlg: %s lines he by default, %s lines under --lang en\n' "$m.l4" "$he_lines" "$en_lines"
  if [ -n "$he_english" ]; then
    printf '%-32s WRONG: English herald words in the default rendering: %s\n' "$m.l4" "$(echo $he_english)"; status=1
  fi
  if [ "$en_hebrew" -ne 0 ]; then
    printf '%-32s WRONG: %s lines of Hebrew herald text under --lang en\n' "$m.l4" "$en_hebrew"; status=1
  fi
done

# 4. Cross-row agreement. The English row is the oracle; this row may differ in vocabulary
#    and in nothing else. For each test module, two things must hold:
#      (a) the two rows satisfy the same NUMBER of assertions;
#      (b) their `Result:` blocks are IDENTICAL, line for line, once the Hebrew names are
#          mapped back through the inverse of glossary.json. That is stronger than
#          comparing counts or numeric values: it compares every #EVAL's answer, including
#          the enum constructors (`registration approved`), the MAYBE wrappers and the
#          dates, in order. A difference here means the two rows disagree about the law.
for pair in hvac-tests-simplex hvac-tests-generated hvac-law hvac-fees; do
  en_out=$("$L4" run "../legalese/$pair.l4" 2>&1)
  he_out=$("$L4" run "$pair-he.l4" 2>&1 | python3 ../../source/revoice.py --unmap)
  en_n=$(printf '%s\n' "$en_out" | grep -c '^  assertion satisfied')
  he_n=$(printf '%s\n' "$he_out" | grep -c '^  assertion satisfied')
  en_r=$(printf '%s\n' "$en_out" | grep -A1 '^Result:' | grep -v '^Result:$' | grep -v '^--$')
  he_r=$(printf '%s\n' "$he_out" | grep -A1 '^Result:' | grep -v '^Result:$' | grep -v '^--$')
  n_r=$(printf '%s\n' "$en_r" | grep -c .)
  if [ "$en_n" -eq "$he_n" ] && [ "$en_r" = "$he_r" ]; then
    printf '%-32s agrees with ../legalese/%s.l4  (%s assertions, %s Result blocks identical)\n' \
           "$pair-he.l4" "$pair" "$en_n" "$n_r"
  else
    printf '%-32s DISAGREES with ../legalese/%s.l4: %s vs %s assertions\n' \
           "$pair-he.l4" "$pair" "$en_n" "$he_n"; status=1
    printf '%s\n' "$en_r" > /tmp/hvac-en-$$.txt
    printf '%s\n' "$he_r" > /tmp/hvac-he-$$.txt
    diff /tmp/hvac-en-$$.txt /tmp/hvac-he-$$.txt | head -40
    rm -f /tmp/hvac-en-$$.txt /tmp/hvac-he-$$.txt
  fi
done

exit $status
