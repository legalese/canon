# PROGRESS — row VN-03 (enc-vn-03), PTI Phúc An Sinh

State on disk, for a resumed session. Read BRIEF.md first, then this.

## How the .l4 files are made

The `.l4` files in this directory are GENERATED. Edit the templates, not the deposit:

- templates: `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn03/tpl/*.l4`
- regenerate: `python3 -I <scratch>/vn03/expand.py <DEPOSIT> <scratch>/vn03/tpl`
  (`{{src N M}}` lines become `-- src:` lines via `tools/vnsrc.py quote`; `{{gen shortrate rows|tests}}` runs `tools/gen_shortrate.py`).
- If the scratch directory is lost: the deposit `.l4` files are complete and can be edited directly.

## Done

- `pti-nouns.l4` (DECLARE only), `pti-part1-definitions.l4`, `pti-part4-conditions.l4`, `pti-part2-benefits.l4`, `pti-part3-exclusions.l4`, `pti-part5-claims.l4`, `pti-assessment.l4`: all typecheck clean (`l4 check`), no assertions in them.
- `pti-tests-fixtures.l4`: typechecks; one smoke evaluation gave `payable OF 2000000` for a clean benefit-1 line.
- Test modules written and parse clean: `pti-tests-conditions.l4`, `pti-tests-cover.l4`, `pti-tests-exclusions.l4`, `pti-tests-claims.l4`, `pti-findings.l4`. First full run in progress (scratch `runall.sh`, outputs in `<scratch>/vn03/out/`).
- Parser lessons: bracket a mixfix call's first argument when it is itself an application; keep every mixfix call on one line; parenthesise a `LIST` used as a record field value.
- `tools/gen_shortrate.py`: generates the short-period scale rows and tests from src:583-589.

- COMPARABLES.md (25 rows) and GLOSSARY.md (298 rows) written by scripts in `<scratch>/vn03/docs/` that assert every Vietnamese term occurs in the raw text; both pass vnsrc check.
- SOURCE-LICENSE.md written (placeholder {{NSRC}} = number of src: lines, fill at the end).
- NOTES.md template `<scratch>/vn03/docs/NOTES.tpl.md` (placeholders {{COVERAGE}} from `docs/coverage.py`, {{TOTAL}}, {{CHECK}}, {{VNSRC}}, {{VNSRCLIT}}); encoding.json template `docs/encoding.tpl.json` ({{DATE}}, {{ERR}}, {{OK}}, {{BAD}}, {{REF}}, {{VNSRC}}).
- 2026-10-07 00:50: renamed `the notice of` c `was late` -> `the notice was late, for` c and `the claim file of` c `is complete` -> `the claim file is complete, for` c (one-argument mixfix may not end in a keyword).

## Remaining, in order

1. Fix type errors from the first run; failing assertions are findings, not edits.
3. NOTES.md (sections 0-8), GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md.
4. `L4=/Users/mengwong/.local/bin/l4 ./check.sh`; vnsrc gate = `python3 -I tools/vnsrc.py check ../../source/raw/pti-phuc-an-sinh.txt *.l4` plus every `.md` except BRIEF.md.

## Performance warning

Typechecking a module that imports everything costs about 70 s CPU (the machine is shared; wall time several minutes). Run test modules in the background.

## Forks so far (numbers used in the .l4 comments)

F2 effect starts at later of certificate day and day after premium; F3 continuous renewal measures waiting/pre-existing/excl 12, 26 from date of joining (def 5 alone resets yearly: finding X3); F4 "đến 65 tuổi" inclusive of age 65; F5 clause 1 bars tested at each period start; F6 epilepsy bars Programme I only; F7 waiting period counts first day as day 1; F8 occupational disease is illness for clause 5; F9 TPD 104-week window tested on onset (finding X1); F10 Appendix 03 rate is % of sum insured; F11 Programme II other benefits illness only; F12 def 17 "52 weeks" = at least 52 weeks; F13 def 21 three years end at start date; F14 transport "appropriate" not "nearest"; F15 days of stay inclusive; F16 def 33 list closed; F17 sailing > 5 km; F18 co-pay before limit; F19 cancellation notice sent >= 30 days before; F20 unexpired premium = annual - short-rate; F21 clause 6 larger of two methods (Law art 24); F22 ratio uses benefit sub-limit; F23 subrogation vs Law art 16(4)/38 (LAW); F24 occupational disease shares accident medical limit; F25 pre-admission window = 30 days before admission day; F26 Asia extension whole contract; F27 newborn counts against newborn and maternity limits; F28 benefit 4(b) waiting only for benefit 4, none for newborn; F29 age 18 on admission day; F30 benefit 6 cancer bar at period start, no continuity exception; F31 excl 2 limb 1 excludes traffic breaches (finding X7); F32 excl 9 vaccination-after-bite proviso limits vaccination limb (finding X8); F33 excl 12 proviso governs both limbs; F34 B2 life-sustaining prosthesis prevails over excl 18 (finding X4); F35 excl 27 does not reach benefits granted for treatment outside a stay (finding X5); F36 financial/medical document split; F37 deadline day X + N; F38 network stay: no documents; daily allowance proved by discharge paper; taxi none; F39 further medical info within 120 days; F40 forfeiture on late filing, not late notice (finding X2); F41 LAW art 30 one year vs 180 days; F42 LAW art 31 15 days to pay.

## Findings so far (X numbers used in comments)

X0 Appendices 01/03/04 missing from published file; X1 TPD 104 weeks illusory on literal reading; X2 notice forfeiture reading; X3 def 5 start date resets at renewal; X4 B2 prosthesis vs excl 18; X5 excl 27 literal removes outpatient-type benefits; X6 def 31 (24h) vs def 32 (overnight); X7 excl 2 age-14 limb dead on literal reading; X8 excl 9 bite-vaccination proviso dead on literal reading; X9 illness PPD only via injury table; X10 def 13 makes main limit redundant; X11 extensions for pre-existing/special diseases never defined; X12 clause 6 two methods, no chooser; X13 inspection discretion; X14 subrogation vs Law; X15 excl 16 "routine treatment as regulated by MoH"; X16 licence copy for every traffic accident; X17 benefit 6 disablement needs death certificate; X18 no time for PTI to pay; X19 180-day filing vs 104-week TPD; X20 short-rate on PTI cancellation; X21 renewal guarantee vs PTI free cancellation; X22 renewers end at first due date after 65th birthday, new entrants accepted to 65 completed; X25 day surgery falls between B2 and outpatient.

## Test runs so far

- 2026-10-07 ~01:30: `pti-tests-conditions.l4` alone: 0 errors, 141 satisfied, 0 failed, 0 refused.
- cover, exclusions, claims, findings rerun after fixing GIVEN order and two renamed functions.

- 2026-10-07 ~02:30: separate runs all green: conditions 141, cover 96, exclusions 78, claims 54, findings 36 satisfied; 0 failed, 0 refused, 0 errors. Then 8 `#ASSERT REFUSED` pinned with BECAUSE.
- Full `check.sh` started ~02:35, output to `<scratch>/vn03/check.out`.
- Docs built provisionally by `<scratch>/vn03/docs/build_docs.py DEPOSIT CHECK_OUT GATE_LINE_FILE LIT_LINE_FILE DATE`; vnsrc gate and literal command both 0 problems.

## Last check.sh totals

2026-10-07, full run, exit 0:

```
TOTAL (13 modules)                             0       405       0        0
```

vnsrc gate (every .l4 and .md except BRIEF.md): `vnsrc check: 973 src: lines, 600 Vietnamese runs, 0 problems`.

## State

DONE. All deliverables exist: 13 modules, NOTES.md, GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md, tools/gen_shortrate.py. Final report sent to the lead.
