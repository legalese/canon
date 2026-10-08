# PROGRESS — row VN-16 (enc-vn-16)

Working state, kept so a resumed session can continue. Not a deliverable; the lead may delete it.

## How the deposit is built

- Drafts live in `scratchpad/vn16-pti268/drafts/*.l4` (scratchpad = `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad`).
- `scratchpad/vn16-pti268/gen/build.sh [MODULE.l4 ...]` regenerates the Part V table (`gen/table.py`, `gen/table_rows.py`, `gen/injury-table.template`), the table tests (`gen/tests-table.template` + `gen/table-tests.l4`), expands every `--@src N M` marker into `-- src:` lines with `tools/vnsrc.py quote` (`gen/expand.py`), writes every draft into DEPOSIT, then `l4 check`s the named modules.
- Edit the DRAFTS, never the deposit `.l4` files directly; build.sh overwrites them.

## Done (typechecks clean)

pti268-nouns, -definitions, -injury-table, -extensions, -exclusions, -conditions, -benefits, -claims, -annex-transport, -decision, -fixtures, -tests-table (143 satisfied), -tests-parts (218 satisfied, 3 traces fulfilled, 3 breached as designed).
GLOSSARY.md, COMPARABLES.md (vnsrc 0 problems each), NOTES.md (placeholders @@CHECK@@, @@TOTALS@@, @@CHECKDETAIL@@, @@VNSRC@@ to fill), encoding.json (@@SELFCHECK@@ to fill), SOURCE-LICENSE.md (@@SRCLINES@@, @@DISTINCT@@ to fill).

## In progress / remaining, in order

1. DONE: pti268-tests-claims.l4 168 satisfied 0 failed; pti268-findings.l4 34 satisfied 0 failed (individual l4 run, 2026-10-07).
2. check.sh run; fill the placeholders above; coverage totals.
3. vnsrc gate: every .l4 and .md except BRIEF.md.
4. Final report to team-lead.

## Forks so far (numbered as in the module comments)

F1 def 38 start date; F2 "up to 70/18/24" inclusive; F3 "unmarried" on the 24 limb only; F4 completed years/months; F5 "bắt đầu tuổi 66" = reached 66; F6 def 35 "và" as union; F7 listed total-injury rows count as TPD; F8 3 years before the start date; F9 III.8 bars only def-58 pre-existing; F10 day counted from is day 1; F11 IV second-32 table replaces III.8's 365 days for B4/B6 in groups >=30; F12 groups <30 = 12 months; F14 narrower reading of exclusions (Law art 24); F15 IV.28 verb governs all three objects; F16 traffic offence under 14 not caught by the general limb; F17 III.4 notice at least 30 days; F18 maternity days count start as day 1; F19 III.13 "quyền lợi 3" read by description as Benefit 2; F20 III.11 larger of the two methods; F21 III.6 "toàn phần" = TPD, 2 years from injury; F22 principle 6 declined for unlisted injuries; F23 limb cap = highest rate of items 8/27; F24 VI.1 notice is a condition; F25 pro rata by days; F26 VI.2 "without prejudice" over "condition precedent"; F27 limits aggregate per period; F28 VI.3 20% cap on all traditional medicine (+ no Đông y cover without VI.3); F29 VI.5 lifts exclusion 8 for strikes; F30 VI.6 suffocation counts as accident; F31 VI.8 does not deem accident; F32 VI.11 uses def 34; F33 ">50" row governs; F34 III.7 rows are exact terms; F35 waiting tested at date of loss; F36 III.12 list closes at "và quyền anh"; F37 VI.12 under Benefit 6; F38 accident insurance = B1/B2; F39 pre/post-hospital paid with the stay; F40 B2 list closed outside a stay; F41 diagnostic procedure as a test; F42 consumables as surgery under B4; F43 B5 days cap per claim; F44 no-treatment claims count from date of loss; F45 12-month docs limit accident only; F46 15 working days, Mon-Fri; F47 90 days at the time of the event; F48 Annex II.4 "place of the accident" read as place of event; F49 Part VII limits only outside the network; F50 leave/death papers whatever the accident; F51 Annex "main policy" = B4 or B2. LAW forks L2 (III.10 vs art 22(2)), L3 (III.14 vs art 32), L4 (notice vs art 19(3)), L5 (120 days vs art 30).

## Last check.sh totals

2026-10-07, whole deposit: `TOTAL (15 modules) 0 563 0 0`, exit 0 (findings 34, tests-claims 168, tests-parts 218, tests-table 143).
vnsrc gate (every .l4 and .md except BRIEF.md): `vnsrc check: 1019 src: lines, 459 Vietnamese runs, 0 problems`.
All deliverables written; placeholders filled. Remaining: final report to team-lead.
