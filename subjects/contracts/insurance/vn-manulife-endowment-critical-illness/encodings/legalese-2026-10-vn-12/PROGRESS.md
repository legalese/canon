# PROGRESS — row VN-12 (enc-vn-12), Manulife CSTD

Working state, kept current in case the session is killed. Not a deliverable.

## How the files are made

- Templates with `{{src N M}}` placeholders: `scratchpad/vn12/tmpl/cstd-*.l4` (scratchpad = `~/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad`).
- `scratchpad/vn12/build.sh` expands them into DEPOSIT via `tools/vnsrc.py quote`, then runs `tools/gen_annex.py` (writes `cstd-annex-tables.l4`, `cstd-tests-annex.l4`, splices enums into `cstd-nouns.l4`).
- If the scratch templates are lost, the DEPOSIT `.l4` files are the expanded source of truth; edit them directly.
- `tools/conditions.py` is the hand-written annex mapping (147 conditions, 118 thresholds).
- Diagnostics viewer: `python3 -I scratchpad/vn12/l4msgs.py FILE -q`.

## Done

- Modules, all typecheck: cstd-nouns, cstd-annex-tables (generated), cstd-annex-rules, cstd-ch1-general (Art 1-11), cstd-ch2-conditions (Art 18-19), cstd-ch2-benefits (Ch 2 preamble, Art 12-17, CI and death claim decisions), cstd-ch3-premiums (Art 20-28), cstd-ch4-claims (Art 29-32), cstd-tests-fixtures.
- Tests: all six test modules green.
- NOTES.md (all sections; §6 and §7 placeholders {{CHECK}} {{VNSRC}} to fill), GLOSSARY.md, COMPARABLES.md, encoding.json written (2026-10-07).

## Last check.sh seen (2026-10-07)

TOTAL (14 modules) 0 errors, 557 satisfied, 0 failed, 0 refused; exit 0.

## Remaining, in order

All done 2026-10-07 05:2x: final check.sh TOTAL (14 modules) 0 errors, 557 satisfied, 0 failed, 0 refused, exit 0; NOTES §6 and §7 filled; vnsrc gate 0 problems (1711 src lines, 1190 runs). Only the final report to the lead remains. Quote volume accepted as is (Meng, 2026-10-07).

## Fork ids used in the L4 comments (to be written up in NOTES §3)

F-T1 days calendar; F-1.6a Tuổi strict "trước"; F-1.3 age at application; F-3a death on end day outside; F-4 21st day last; F-7a proportional SA; F-12a funeral strictly after 1 year; F-12b late decision on/before death; F-13.4a Tuổi as fixed for the policy year; F-13.4b no age for (b)(ii); F-13.5b 20th anniversary; F-15a loyalty at the anniversary ending the term; F-15b readings of "trừ thời hạn đóng phí" coincide; F-16.4 dividends not paid twice; F-18a after 90 days = day 91+; F-18b death on day 30 passes; F-18c Accident excuses both (a) and (b); F-19a 2nd anniversary not within; F-20 grace ends due+60; F-28 6 months exclusive; F-29a claim last day = event + 1 year; F-29b insured event = diagnosis; F-29c Art 29 for all claims; F-29d refusal within 30 days; F-31a 31.3 ends 13.4 too; F-C2 floor before 12.3/Debt; F-CI-1 each separately headed condition is a CI.

## Findings ids (NOTES §4)

X-1 32.4 literal ends at 66; X-2 12-month definitions vs 1-year claim bar; X-3 mutual CAD bars; X-4 "same illness" undefined; X-5 coupon negative; X-6 26.5 lapse vs 32.7 terminate; X-7 invasive melanoma early; X-8 temp cover accident < suicide; X-9 "Người Được Bảo Hiểm 2"; X-10 1.2 Tuổi for policyholder; X-11 special cash benefit undefined; X-12 Business Procedures discretion; X-13 temp cover illness gap; X-14 Art 6 gap; X-15 Art 21 gap; X-16 13.4 vs 31.3; X-17 accident excuses survival; X-19 tracheostomy bar unreachable; X-24 retroactive 11.1(b); X-27 CJD 2/6.
