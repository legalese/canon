# Independent test report — Metrication Act 1970

Expectations were decided from `../source/MA1970.txt`, `PROVENANCE.md` and `BRIEF.md` alone and
written down in `independent-expectations.md` before any `.l4` was opened. Tests:
`tests-independent.l4`. Run: `~/.local/bin/l4 run tests-independent.l4` from this directory
(JL4_LIBRARY_PATH unset).

## Counts

| | |
|---|---|
| assertions | 97 |
| satisfied | 97 |
| failed (`assertion failed`) | 0 |
| parse / type / other errors | 0 |

Covered: s 3(1) both sides of 15 Feb 1971; s 2(2) "SI"; s 2(1)(a)/(b) with the Fourth Schedule
included by default and excluded where context is inconsistent; every row of the First (6),
Second (15) and Fourth (4) Schedules — unit, schedule, symbol and quantity — and the counts;
every Third Schedule factor (unit and multiple), its "exactly"/"approximately", its SI unit, and
its s 5(a)/(b) system; refusal for a unit not in the Third Schedule; s 4 order validity (all three
limbs); s 7(1) both sides of the order date (day before, day of, day after), the "only" ground,
and no order yet made; s 7(2).

## Failures

None.

## Expectations I could not fully express against the encoding's names

- **Gallon, two rows.** The Third Schedule prints the gallon twice (litres; cubic decimetres). The
  encoding carries one row with SI unit `"litres (= cubic decimetres)"`. I tested the factor
  4.54609 and "approximately", which agree; I did not assert the SI-unit string for the gallon.
  The "(= cubic decimetres)" gloss asserts an identity the Schedule does not state (it prints two
  approximate conversions), but the numbers are the same, so it is a presentational point only.
- **S8 vs S9.** The two s 2(1)(b) exceptions ("subject or context inconsistent"; "therein otherwise
  expressly provided") are merged into one input `the context excludes the Fourth Schedule`; I
  tested the merged input only.
- **O1 vs O2** (equivalent vs desirable approximation) are merged into one boolean input; tested
  only as merged.
- **s 7(1) "any order".** The encoding's FORK F1 (the order touching that act) matches my R7.
- **T10 (foot, ounce, picul)** — the encoding has no constructor for them, only `another unit`;
  tested that `another unit` and a non-Third-Schedule SI unit (metre) refuse, which matches R2.
- s 4 "relating to such departments and subjects as may be appropriate", s 6 power — inert;
  nothing to assert.


## Triage by the encoder (2026-10-05)

No failures. The two notes are accepted as they stand. The gallon's single row with "(= cubic decimetres)" in its unit name is a presentational merge of the Schedule's two approximate rows, as `NOTES.md` says. The merged s 2(1)(b) and s 4(1)(a)/(b) inputs are deliberate: each pair is a judgement about another written law or about an order, not something this Act computes.
