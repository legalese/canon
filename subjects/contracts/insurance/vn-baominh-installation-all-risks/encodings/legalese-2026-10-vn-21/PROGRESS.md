# PROGRESS — row VN-21 (`legalese-2026-10-vn-21`), encoder enc-vn-21

State on disk, for a resume. Read BRIEF.md and this file first, then re-run check.sh.

## How the .l4 files are made

The `.l4` modules in this directory are GENERATED. Edit the templates, not the outputs:

- templates: `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn21/tpl/*.l4`
- regenerate all: `scratchpad/vn21/build.sh` (runs `expand.py`, which replaces each `{{src N M}}` line with the output of `python3 -I tools/vnsrc.py quote ../../source/raw/baominh-ear.txt N M`)
- typecheck one: `/Users/mengwong/.local/bin/l4 check FILE`

## Done

- `bm-ear-nouns.l4` — all DECLAREs (parties, causes, kinds of property, works, schedule items, schedule, answers, policy, duties, conduct, occurrence, Part I loss, Part II liability, dispute, claim, grounds, burden, GC1 readings, acts). Typechecks.
- `bm-ear-period.l4` — period of insurance (src:40-57). Typechecks.
- `bm-ear-general-exclusions.l4` — GE (a)-(d), burden-of-proof clause. Typechecks.
- `bm-ear-general-conditions.l4` — preamble, GC1-GC9, whole-claim grounds. Typechecks.

- `bm-ear-part1-material-damage.l4`, `bm-ear-part2-third-party.l4`, `bm-ear-duties.l4` — written, all typecheck (2026-10-07). `scratchpad/vn21/fixgiven.py` reorders GIVEN blocks to head order.

## Status: COMPLETE (2026-10-07)

All deliverables exist: 14 modules, NOTES.md, GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md. Final report sent to the lead.

## Forks taken so far (numbers used in module comments)

F01 parties: only "the Insured" and Bao Minh. F03 burden clause literal (Insured's allegation); BM allegation refused. F04 GC1 questionnaire limb reading (ii) true+complete. F05 premium: paid by the occurrence. F06 cover begins at the EARLIER of works commencement and item unloading. F07 same-day start/end EVENT -> REFUSE. F08 4 weeks = 28 days from project testing start. F09 date limits inclusive (schedule date, day 28). F10 "tested" = test run completed. F11 no-repair-before-inspection is implied duty. F12 GC5 unrepaired item: cover ends for later occurrences. F13 14 days calendar, day of occurrence not counted, receipt. F14 "that limit" = per-occurrence limit in schedule if stated. F15 order of arithmetic; per-item cap per occurrence. F16 cash/repair option not modelled. F17 causes list, no weighing. F18 one month = calendar month via `add months`. F19 GC8 bar runs only from an award. F20 GC9 proportion: refuse if not determined. F21 debris only with a covered Part I loss. F22 excl 3 carve-back only for workmanship. F23 item 4 average vs value of surrounding property; other items (not 1,2,4) refuse. F24 temp repairs all-or-nothing. F26 non-SI part subtracted in basis (a) only. F27 constructive total loss compares gross restoration cost.

## Last check.sh totals

2026-10-07, final: TOTAL (14 modules) 0 errors, 188 satisfied, 0 failed, 0 refused; exit 0.
vnsrc gate (all .l4 and .md except BRIEF.md): `vnsrc check: 214 src: lines, 389 Vietnamese runs, 0 problems`.
