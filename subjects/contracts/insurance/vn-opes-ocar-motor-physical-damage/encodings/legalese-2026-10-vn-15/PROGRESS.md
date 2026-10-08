# PROGRESS — row VN-15 (enc-vn-15)

State on disk, in case the session is killed and resumed. Read this and BRIEF.md first, then re-run `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.

## Where the sources of the deposit live

- Templates: `scratchpad/vn15/vn15tpl/*.l4` (scratchpad = `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad`). They carry `--@src N M` marker lines.
- `scratchpad/vn15/vn15expand.py TPLDIR DEPOSIT` expands each marker by calling `tools/vnsrc.py quote` and writes every template into DEPOSIT. Never hand-edit a DEPOSIT `.l4`; edit the template and re-expand.
- `scratchpad/vn15/gen_tables.py RAW OUT` generates `vn15tpl/ocar-tests-tables.l4` from the raw text (regexes over the source lines).
- Probe copy for running: `scratchpad/vn15/probe2/` (copy of the DEPOSIT `.l4`).

## Done (updated 2026-10-07 00:30)

- Scratch moved to `scratchpad/vn15/` (was `enc-vn-15/`); templates `vn15/vn15tpl/`, also NOTES.md, GLOSSARY.md, COMPARABLES.md, SOURCE-LICENSE.md templates there (NOTES has @@ placeholders for the check numbers); `vn15/encoding.json.tpl` likewise.
- GLOSSARY.md, COMPARABLES.md (25 rows), SOURCE-LICENSE.md written; vnsrc clean.
- NOTES.md drafted: coverage table, forks F1-F40 + L1-L8, findings X1-X29, answer table, open questions. Needs §0/§6/§7 numbers.
- Test fixes: `JUST 60%` parses as `(JUST 60)%`; every percent argument is now parenthesised; `the 2026 policy with` (LIST ..) parenthesised as an argument.
- ocar-tests-process.l4: 56 assertions satisfied, 0 errors, traces as expected (before the % fixes, which did not touch it).

- Rule modules (all typecheck): ocar-nouns, ocar-01-definitions, ocar-02-03-term-termination, ocar-04-05-06-duties, ocar-07-10-claims-process, ocar-11-12-cover, ocar-13-valuation, ocar-14-settlement, ocar-15-16-deductible-reductions, ocar-17-supplementary, ocar-personal-data, ocar-claim. Imports form a chain (l4 re-checks a module per import path).
- Tests written: ocar-tests-fixtures (helpers), ocar-tests-tables (generated), ocar-tests-cover, ocar-tests-amounts, ocar-tests-process, ocar-tests-findings. First full run in progress at the time of writing.

## Remaining, in order

1. Run the tests; fix encoding errors (never edit an expected value to match).
2. NOTES.md (build, scope, coverage table, forks F1-F35 + L-forks, findings X1-X29, answer table, check.sh, vnsrc line, open questions).
3. GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md.
4. vnsrc gate: `python3 -I tools/vnsrc.py check ../../source/raw/opes-ocar.txt *.l4 $(ls *.md | grep -v BRIEF.md)`.

## Decisions so far (full list goes in NOTES.md)

- Version: chosen by the date the contract was concluded; Decision 124/2019 from 31/12/2019, Decision 17/2022 from 28/03/2022; before 2019 declined; 2019 contracts listing BS02-BS07 declined, BS01 read as the clause 14.1.2(c) names (F1, F2).
- Personal data clause: undated, cites Decree 13/2023 of 17/04/2023; part-of-contract is an input; earlier contracts declined (F3).
- Working days: caller-supplied list of non-working days (F8); "kể từ ngày X" excludes day X (F7).
- Order of layers: Art 14 → Art 9 share → deductible (partial only) → Art 16 reduction → + 11.2 costs → cap at sum insured (F31, F25, F18, F19).

## Last check.sh totals

A first check.sh run (00:13) was killed by a signal (exit 144) after six rule modules, all 0 0 0 0. Test modules now run in parallel detached into `scratchpad/vn15/run2-*.txt`; then check.sh again. After that: `python3 -I scratchpad/vn15/fill.py CHECKOUT VNSRCLINE DATE scratchpad/vn15/vn15tpl DEPOSIT` fills NOTES.md and encoding.json (run vn15expand.py first, then fill.py; expand rewrites NOTES with placeholders).

## 00:50 status

- Separate runs (probe2): ocar-tests-cover 92/92 satisfied, 0 errors; ocar-tests-tables 50/50. Amounts, process, findings running (`scratchpad/vn15/run2-*.txt`).
- Quotations trimmed in templates (not yet expanded into DEPOSIT): nouns now points to the module that quotes each clause; inert passages quoted by first line only. Was 978 src lines (862 unique of 1,026 non-blank source lines).
- A regex that parenthesised percent literals also hit backticked names; undone (`new (100%) when insured` etc. restored).

## 01:10 status

- Separate runs: cover 92/92, tables 50/50, process 56/56, findings 32/32, amounts 118/119; the one failure was a test whose facts did not make the total loss it meant (damage 500m vs 75% of 700m); facts corrected to 600m, expected value unchanged; noted in NOTES §6.
- Templates expanded into DEPOSIT; vnsrc gate (all .l4 and .md except BRIEF.md): 769 src lines, 0 problems.
- Official check.sh launched detached at 01:08, output to `scratchpad/vn15/check2.txt` (ends with an `exit N` line). Then: fill.py, final report.

## 01:45 — done

- check.sh (official, 2026-10-07): `TOTAL (18 modules) 0 349 0 0`, exit 0. Output in NOTES.md §6.
- vnsrc gate (all .l4 and .md except BRIEF.md): `vnsrc check: 769 src: lines, 492 Vietnamese runs, 0 problems`. Literal command (with BRIEF.md): 1 problem, in BRIEF.md.
- NOTES.md, GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md filled. Coverage: 68 encoded, 30 inert, 1 out-of-scope, 0 deferred. Forks F1-F40 and L1-L8; findings X1-X29.
- Nothing remains but the final report.
