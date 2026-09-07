#!/bin/sh
# Run the encoding with the l4 binary and the prelude that MATCHES it.
# CLAUDE.md § 3.1: never point an l4 binary at a prelude newer than itself.
# Both come from the same worktree, so they agree by construction.
WT=${OFEK_L4_WORKTREE:-/Users/mengwong/src/legalese/l4wt/ofek-build}
L4=$WT/dist-newstyle/build/aarch64-osx/ghc-9.10.3/jl4-0.1/x/l4/build/l4/l4
export JL4_LIBRARY_PATH=$WT/jl4-core/libraries
cd "$(dirname "$0")" || exit 1
status=0
for f in ofek-domain.l4 ofek-salary-table.l4 ofek-placement.l4 ofek-worktime.l4 \
         ofek-supplements.l4 ofek-fiscal-2025.l4 ofek-pay.l4 ofek-cases.l4; do
  [ -f "$f" ] || continue
  out=$("$L4" run "$f" 2>&1)
  bad=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  printf '%-26s %s\n' "$f" "$([ "$bad" -eq 0 ] && echo 'ok' || echo "$bad ERRORS")"
  [ "$bad" -eq 0 ] || { status=1; printf '%s\n' "$out" | grep -B6 'DiagnosticSeverity_Error' | head -60; }
done
exit $status
