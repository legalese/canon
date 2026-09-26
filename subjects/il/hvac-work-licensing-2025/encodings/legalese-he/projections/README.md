# `projections/` — STALE as of 2026-09-22

These renderings were generated on 2026-09-21, from the Hebrew twin **as it stood before**
the two enacted texts of reg. 2 were moved onto L4's rule-effective-time axis. They still
describe the retired three-value `נוסח` (`Vintage`) enum and the rules that hung off it
(`האגרה לפי`, `הסכום הכולל שיש לשלם לפי`, `תוצאת SimpLEX לפי`), none of which exist any more.

This row is GENERATED from `../legalese` by `../../source/revoice.py`; the `.l4` modules
here were regenerated with the rewrite and are current. Only these renderings are not,
because `l4 render --lang` and `l4 nlg --lang` need a binary at or after l4-ide `unstable`
PR #432 (2026-09-19), and the newest prerelease reachable from the machine the rewrite was
done on was `unstable-20260907-9d6536a`, which predates it and cannot lex `@lang he` at all.

Regenerate all of them with a binary at or after PR #432. This row is the mirror of
`../legalese`: Hebrew by default, English on request.

```sh
for m in hvac-law-he hvac-fees-he; do
  l4 render --lang he --format html "$m.l4" > "projections/$m.he.html"
  l4 render --lang en --format html "$m.l4" > "projections/$m.en.html"
  l4 nlg                            "$m.l4" > "projections/$m.nlg-he.txt"
  l4 nlg --lang en                  "$m.l4" > "projections/$m.nlg-en.txt"
done
```

and then delete this file.
