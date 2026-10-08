# PROGRESS — VN-28 (enc-vn-28), run VN-28-20261007

For a resumed session: what is done, the last `check.sh` TOTAL, what remains.

## How the .l4 files are made

The modules are generated from templates in the scratch directory
`/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn28/tpl/*.l4.tpl`
by `scratch/vn28/expand.py RAW VNSRC DEPOSIT TEMPLATE...`, which turns each `-- QUOTE N M` line into `vnsrc.py quote` output and each `-- INCLUDE f` into `scratch/vn28/gen/f` (written by `gen_tables.py` from the raw text).
If the scratch directory is gone, edit the .l4 files in DEPOSIT directly and quote with `tools/vnsrc.py quote`.

## Done (all deliverables)

- First pass: the sources then held Articles 24-89 only (gazette 979+980); the lead added 977+978 (Articles 1-23) on 2026-10-07.
- Eleven .l4 modules (eight library modules, two tests modules, one findings module).
- First pass: NOTES.md (27 forks, 14 findings, 59 coverage rows), GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md.

## Last check.sh TOTAL

`TOTAL (11 modules) 0 366 0 0`, exit 0 (2 min 42 s wall, third pass).

## Last vnsrc check

`vnsrc check: 562 src: lines, 501 Vietnamese runs, 0 problems`

## Second pass (2026-10-07, after the lead added gazette 977+978)

The lead added `source/raw/law36-2024-qh15-977-978.txt` (Articles 1-23) and an extended `tools/vnsrc.py` (`quoteid`; `src:law36-2024-qh15-977-978:N` lines).
Existing quotes re-checked with the new tool: `vnsrc check: 489 src: lines, 402 Vietnamese runs, 0 problems` (unchanged).
Read Articles 1-9 in full. Article 9(2) forbids driving with any alcohol in blood or breath; 9(10) forbids converting other automobiles into passenger automobiles.

## Second pass: done so far

- Alcohol module renamed `law36-art9-81-87-alcohol.l4`; Article 9(2)-(3) encoded; Decision 2 now answers (the Law permits no alcohol; blood alcohol found endogenous excepted, forks F8, F28, F29).
- Article 2(2), 2(7), 2(9), 9(1), 9(10) quoted; `Article 9(10) — prohibits the conversion of` added; finding R9 re-scenarioed.
- Tests and findings updated. check.sh: `TOTAL (11 modules) 0 334 0 0`, exit 0. vnsrc over .l4: 515 src: lines, 0 problems.

## Second pass: complete

- NOTES.md now: 29 forks, 15 findings (R15 reading only), 72 coverage rows (36 encoded, 14 inert, 18 out-of-scope, 4 reached-and-refused, 0 deferred).
- GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md updated for both sources.
- check.sh: `TOTAL (11 modules) 0 334 0 0`, exit 0.
- vnsrc over all .l4 and .md except BRIEF.md: `vnsrc check: 515 src: lines, 463 Vietnamese runs, 0 problems`.

## Third pass: complete

At the lead's request: Article 9(7), 9(8) with Article 35(1), Article 2(8) and 2(12) encoded; finding R15 now demonstrated; R16 added (reading only).
- NOTES.md: 31 forks, 16 findings, 77 coverage rows (41 encoded, 14 inert, 18 out-of-scope, 4 reached-and-refused, 0 deferred).
- check.sh: `TOTAL (11 modules) 0 366 0 0`, exit 0.
- vnsrc over all .l4 and .md except BRIEF.md: `vnsrc check: 562 src: lines, 501 Vietnamese runs, 0 problems`.

## Remaining

- Nothing for this session; the lead commits. HG1 and an independent test pass are not done.
