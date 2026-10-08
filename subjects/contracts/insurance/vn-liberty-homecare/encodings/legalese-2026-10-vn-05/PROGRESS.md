# PROGRESS — VN-05, Liberty HomeCare, encoder enc-vn-05

Last updated 2026-10-07 (after the usage-limit reset).

## Done

- Rule modules, all typecheck with 0 errors: `homecare-nouns.l4`, `homecare-definitions.l4`, `homecare-perils.l4`, `homecare-general-exclusions.l4`, `homecare-general-conditions.l4`, `homecare-part1.l4`, `homecare-part2.l4`, `homecare-part3.l4`.
- `homecare-test-fixtures.l4` (named cases, hypothetical Summary figures, no assertions).
- Tests, last seen all satisfied, 0 failed, 0 refused: `homecare-tests-part1.l4` (266), `homecare-tests-part2.l4` (82), `homecare-tests-part3-conditions.l4` (109), `homecare-tests-figures.l4` (43, generated).
- `tools/gen_figure_tests.py` regenerates `homecare-tests-figures.l4` from the raw text: `python3 -I tools/gen_figure_tests.py ../../source/raw/liberty-homecare.txt > homecare-tests-figures.l4`.

## How the .l4 files are made

The modules other than the generated one are written as templates in `scratchpad/vn05/tpl/` (the session scratchpad) with `-- @src N M` marker lines; `scratchpad/vn05/bin/expand.py DEPOSIT RAW TEMPLATE` replaces each marker with the output of `tools/vnsrc.py quote RAW N M` and writes the module into this directory; `scratchpad/vn05/bin/build.sh` expands and runs. If the scratchpad is lost, edit the deposited .l4 files directly: they are complete.

- `homecare-findings.l4`: 22 assertions, all satisfied (build.sh, 2026-10-07).
- NOTES.md, GLOSSARY.md, COMPARABLES.md (25 rows), encoding.json, SOURCE-LICENSE.md written.
- Quote gate (every .l4 and .md except BRIEF.md): 0 problems.

## Remaining, in order

1. Final report to the lead. Everything else is done.

## Final state (2026-10-07)

- check.sh, 14 modules: `TOTAL (14 modules)                             0       522       0        0`, exit 0.
- Quote gate (every .l4 and .md except BRIEF.md): `vnsrc check: 1025 src: lines, 473 Vietnamese runs, 0 problems`.
- Literal command (includes BRIEF.md): `vnsrc check: 1025 src: lines, 487 Vietnamese runs, 0 problems`.
