# `projections/` — STALE as of 2026-09-22

These renderings were generated on 2026-09-21, from the encoding **as it stood before**
the two enacted texts of reg. 2 were moved onto L4's rule-effective-time axis. They still
describe the retired three-value `DECLARE Vintage IS ONE OF` design and the rules that
hung off it (`the fee under`, `the total to be tendered under`, `the SimpLEX outcome
under`), none of which exist any more.

They were **not** regenerated with the rewrite because `l4 render --lang` and
`l4 nlg --lang` need a binary at or after l4-ide `unstable` PR #432 (2026-09-19), and the
newest prerelease reachable from the machine the rewrite was done on was
`unstable-20260907-9d6536a`, which predates it and cannot lex `@lang en` at all.

Regenerate all of them with a binary at or after PR #432:

```sh
for m in hvac-law hvac-fees hvac-tests-simplex; do
  l4 render --format html          "$m.l4" > "projections/$m.en.html"
  l4 render --lang he --format html "$m.l4" > "projections/$m.he.html"
  l4 nlg                            "$m.l4" > "projections/$m.nlg-en.txt"
  l4 nlg --lang he                  "$m.l4" > "projections/$m.nlg-he.txt"
done
```

and then delete this file.
