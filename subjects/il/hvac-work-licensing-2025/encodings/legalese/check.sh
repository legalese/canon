#!/bin/sh
# Run the encoding with an l4 binary and the prelude that MATCHES it.
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
# There is a HEBREW-CANONICAL twin of this row at ../legalese-he, generated from these
# five modules by ../../source/revoice.py. Run ../legalese-he/check.sh too: its section 4
# compares the two rows' answers directly, so it fails when this row moves and that one
# has not been regenerated.
WT=${HVAC_L4_WORKTREE:-/Users/mengwong/src/legalese/l4wt/smart-quotes}
L4=${HVAC_L4:-$WT/dist-newstyle/build/aarch64-osx/ghc-9.10.3/jl4-0.1/x/l4/build/l4/l4}
if [ -n "${HVAC_LIBS:-}" ]; then export JL4_LIBRARY_PATH="$HVAC_LIBS"; else unset JL4_LIBRARY_PATH; fi
cd "$(dirname "$0")" || exit 1
status=0

# Green files: zero errors, and every assertion satisfied.
for f in hvac-law.l4 hvac-fees.l4 hvac-tests-simplex.l4 hvac-tests-generated.l4; do
  [ -f "$f" ] || { printf '%-30s MISSING\n' "$f"; status=1; continue; }
  out=$("$L4" run "$f" 2>&1)
  bad=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  ok=$(printf '%s\n' "$out" | grep -c '^  assertion satisfied')
  printf '%-30s %s  (%s assertions satisfied)\n' "$f" "$([ "$bad" -eq 0 ] && echo ok || echo "$bad ERRORS")" "$ok"
  [ "$bad" -eq 0 ] || { status=1; printf '%s\n' "$out" | grep -B6 'DiagnosticSeverity_Error' | head -60; }
done

# The red file is the positive control: EXACTLY 3 failed assertions, no other error.
f=hvac-tests-simplex-red.l4
out=$("$L4" run "$f" 2>&1)
bad=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
failed=$(printf '%s\n' "$out" | grep -c '^  assertion failed')
if [ "$bad" -eq 3 ] && [ "$failed" -eq 3 ]; then
  printf '%-30s ok  (fails on exactly 3 assertions, as intended)\n' "$f"
else
  printf '%-30s WRONG: %s errors, %s failed assertions (expected 3 and 3)\n' "$f" "$bad" "$failed"; status=1
fi

# Renderings: English by default, Hebrew on request. Both must exist and differ.
for m in hvac-law hvac-fees; do
  en=$("$L4" nlg "$m.l4" 2>/dev/null | wc -l | tr -d ' ')
  he=$("$L4" nlg --lang he "$m.l4" 2>/dev/null | grep -c '[א-ת]')
  printf '%-30s nlg: %s lines en, %s lines with Hebrew under --lang he\n' "$m.l4" "$en" "$he"
  [ "$he" -gt 0 ] || status=1
done
exit $status
