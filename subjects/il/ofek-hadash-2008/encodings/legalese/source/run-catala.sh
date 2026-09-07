#!/bin/sh
# Compile this encoding to Catala, typecheck it, and RUN the worked cases
# against the emitted module — no L4 in the loop once the .catala_en exists.
#
# The six figures printed at the end must equal the ones ofek-cases.l4 asserts.
# That equality is the whole point of the exercise: it shows the lowering
# preserved the arithmetic, which `catala typecheck` alone does not.
#
#   OFEK_CORPUS=<checkout-of-ofek-hadash-corpus> source/run-catala.sh
#
# Needs catala + clerk 1.2.1 on an opam switch named `catala`, and an l4 binary
# built from the same tree as the prelude it is pointed at (CLAUDE.md § 3.1).
set -e

HERE=$(cd "$(dirname "$0")/.." && pwd)
WT=${OFEK_L4_WORKTREE:-/Users/mengwong/src/legalese/l4wt/ofek-build}
L4=$WT/dist-newstyle/build/aarch64-osx/ghc-9.10.3/jl4-0.1/x/l4/build/l4/l4
export JL4_LIBRARY_PATH=$WT/jl4-core/libraries
CATALA="opam exec --switch=catala --"

: "${OFEK_CORPUS:?set OFEK_CORPUS to a checkout of morimovilimcatala/ofek-hadash-corpus}"

cd "$HERE"

echo "== regenerating the single-module rendering from the corpus =="
python3 source/build-catala-module.py > ofek-catala.l4

echo "== l4: the generated module evaluates green =="
"$L4" run ofek-catala.l4 2>&1 | grep -c 'DiagnosticSeverity_Error' | sed 's/^/   errors: /'

echo "== l4 catala: emit the Catala module =="
# Catala requires the basename to be a valid module name: letters, digits and
# underscore only. `ofek-hadash.catala_en` is refused.
"$L4" catala ofek-catala.l4 -o catala/ofek_hadash.catala_en 2>&1 \
  | grep -c 'did not become' | sed 's/^/   directives not lowered to #[test]: /'

# A 36-arm BRANCH lowers to one 9,771-character line. Wrapping it at the row
# boundaries changes no token — wrap-catala.py refuses to write if it does —
# and the typecheck and the six cases below are run against the WRAPPED file,
# so the claim is checked rather than asserted.
python3 source/wrap-catala.py catala/ofek_hadash.catala_en

echo "== catala: typecheck, then run the cases =="
WORK=$(mktemp -d)
cp catala/ofek_hadash.catala_en catala/ofek_hadash_cases.catala_en "$WORK/"
cd "$WORK"
$CATALA clerk start >/dev/null 2>&1

# The interpreter needs each stdlib module compiled, and clerk builds them one
# target at a time; `clerk build` with no target refuses without a clerk.toml.
for f in _build/libcatala/*.catala_en; do
  m=$(basename "$f" .catala_en)
  M="$(printf '%s' "${m%"${m#?}"}" | tr 'a-z' 'A-Z')${m#?}"
  $CATALA clerk build "_build/libcatala/ocaml/$M.cmxs" >/dev/null 2>&1 || true
done

$CATALA catala typecheck ofek_hadash.catala_en
$CATALA catala typecheck ofek_hadash_cases.catala_en
$CATALA clerk build _build/ocaml/Ofek_hadash.cmxs >/dev/null

echo
echo "   scope                              catala says      ofek-cases.l4 asserts"
set -- \
  "YaelInSeptember2024:11,008.03" \
  "YaelInNovember2025:10,903.453,715" \
  "YaelInNovember2025HavingAdvanced:10,773.453,715" \
  "YaelOnHalfAPost:6,004.38" \
  "DvoraInOctober2026:18,673.689,801" \
  "NoaInSeptember2024:5,000.987,5"
rc=0
for pair; do
  s=${pair%%:*}; want=${pair#*:}
  got=$($CATALA catala interpret ofek_hadash_cases.catala_en -s "$s" 2>&1 \
        | grep -o 'pay = .*' | head -1 | sed 's/pay = //')
  if [ "$got" = "$want" ]; then mark="ok"; else mark="MISMATCH"; rc=1; fi
  printf '   %-34s %-16s %-16s %s\n' "$s" "$got" "$want" "$mark"
done

cd - >/dev/null
rm -rf "$WORK"
exit $rc
