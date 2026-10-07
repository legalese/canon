# PROGRESS — VN-28 (enc-vn-28), run VN-28-20261007

For a resumed session: what is done, the last `check.sh` TOTAL, what remains.

## How the .l4 files are made

The modules are generated from templates in the scratch directory
`/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn28/tpl/*.l4.tpl`
by `scratch/vn28/expand.py RAW VNSRC DEPOSIT TEMPLATE...`, which turns each `-- QUOTE N M` line into `vnsrc.py quote` output and each `-- INCLUDE f` into `scratch/vn28/gen/f` (written by `gen_tables.py` from the raw text).
If the scratch directory is gone, edit the .l4 files in DEPOSIT directly and quote with `tools/vnsrc.py quote`.

## Done (all deliverables)

- Source holds Articles 24-89 only (gazette 979+980); Articles 1-23 incl. 2 and 9 are in 977+978, not deposited. Lead told (2026-10-07).
- Eleven .l4 modules (chain of eight library modules, two tests modules, one findings module).
- First pass: NOTES.md (27 forks, 14 findings, 59 coverage rows), GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md.

## Last check.sh TOTAL

`TOTAL (11 modules) 0 323 0 0`, exit 0 (about 90 s wall).

## Last vnsrc check

`vnsrc check: 489 src: lines, 402 Vietnamese runs, 0 problems`

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

## Third pass (lead's message of 2026-10-07: encode 9(1)-(3), (7), (8) at least; Article 2 definitions used)

Plan:
- nouns: `An event on the road` (Art 2(12)); `A person in road traffic` (Art 2(8)-(9)); two Art 35(1) facts on `A registered vehicle`.
- art34 module: Art 2(2) group of a vehicle, 2(8)-(9) role, 2(12) accident.
- registration module: Art 35(1) conditions and Art 9(8).
- decisions module: Art 9(7) (handing a vehicle to a person not qualified).
- tests and findings (R15 demonstrable; R16 reading only: "người được chở" against "hành khách").
- docs, check.sh, vnsrc.

## Remaining

- The third pass above; then report the real TOTAL to the lead.
