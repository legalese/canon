# PROGRESS — VN-20 (enc-vn-20), Bao Minh fire and special perils

State on disk, for a resume. Read BRIEF.md first, then this.

## How the .l4 files are made

The `.l4` modules are GENERATED. Edit the templates, never the `.l4` directly:

- templates: `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn20/tmpl/*.l4.tmpl`
- expander: `scratchpad/vn20/expand.py` — run `python3 -I expand.py <DEPOSIT> tmpl` from `scratchpad/vn20/`; it replaces each `--@src N M` line with `tools/vnsrc.py quote` output and writes `<DEPOSIT>/<name>.l4`.

## Done (2026-10-07 ~01:05)

- All modules written. Individual `l4 run` results (scratchpad/vn20/run-*.txt): cover 124 asserts satisfied, 0 errors; amount 40, 0 errors; conditions 93, 0 errors (traces as expected); findings 28, 0 errors.
- NOTES.md, GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md written.
- vnsrc gate (every .l4 and .md except BRIEF.md): `vnsrc check: 489 src: lines, 494 Vietnamese runs, 0 problems` (before PROGRESS/NOTES final edits; rerun at the end).
- check.sh started detached (nohup) writing scratchpad/vn20/checksh.txt. Background tasks die at ~10 min, so run long jobs with `( nohup ... & )`.

## Remaining, in order

1. Read checksh.txt; copy totals into NOTES §6 and encoding.json self_check.
2. Rerun the vnsrc gate; put its line in NOTES §7.
3. Final report to team-lead (check.sh TOTAL and vnsrc line verbatim; flag the quotation count, 464 of 471 lines).

## Forks and findings so far (numbers used in module comments)

Forks: F3 abnormal conditions = fact; F4 domestic qualifier governs boiler and gas; F5 A(b)(i)-(iii) item by item; F6 E applies D's exclusions; F7 I(ii) building only, no minimum time; F8 J's sentence is a deductible sentence; F10 pollution "(trừ khi đã bị loại trừ)"; F11 III.2(a) needs specific recording; F12 consequential heads, rent; F13 remaining SI per item and total; F14 VIII.1(a)(i) objects; F15 VIII.2 write-back list mapping; F16 VII.3 local regulations measure; F17 deductible as amount per risk; F18 order of steps; F19 contribution ratio = SI (LAW art 49); F20 "ngay lập tức" fact; F21 period ends inclusive, 30 days from DAMAGE; F22 day/month counting; F23 cancellation 7 days, refund days; F24 short-period boundaries to lower row; F25 VI.5 literal renewal; F26 VI.3 changes concern claimed property; F27 VIII.3 reading R3 (clause 2 prevails; LAW art 27(1)(c)); F29 conditions precedent; F30 V prejudice input; F31 VI.2 no intent.

Findings: X1 J covers own vehicles; X2 lone-wolf / government terrorism not excluded; X3 "Nổi loạn" in III.1(a)(i) and (iii) makes D riot cover illusory; X5 average then contribution double reduction; X6 warranty bites only in renewal; X7 12-month bar runs during arbitration; X8 I(ii) vacant no minimum vs VI.3(b) 30 days; X9 premium: preamble vs VIII.3.1 vs VIII.3.2; X10 III.1(c) incl. lightning; X11 VIII.2 write-back omits flood/water/animal; X12 short-period overlapping rows; X13 refund counted from notice though cover runs 7 more days.

## Last check.sh totals

`TOTAL (12 modules) 0 errors / 285 satisfied / 0 failed / 0 refused`, exit 0 (2026-10-07). vnsrc gate: `vnsrc check: 489 src: lines, 494 Vietnamese runs, 0 problems`. All deliverables written; only the final report remains.
