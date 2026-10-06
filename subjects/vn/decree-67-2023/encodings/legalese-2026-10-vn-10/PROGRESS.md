# PROGRESS — row VN-10 (enc-vn-10)

Updated 2026-10-07 00:0x SGT.

## Done

- All 14 `.l4` modules written and green. Last `check.sh` (2026-10-07, after the last module change): `TOTAL (14 modules) 0 errors, 1487 satisfied, 0 failed, 0 refused`, exit 0.
- Generated files and their scripts (run from DEPOSIT with `python3 -I`):
  - `nd67-annex6-table.l4`, `nd67-annex6-tests.l4` ← `tools/annex6.py ../../source/raw/nd67-congbao-1019-1020.txt` (1,135 rows, 1,235 tests).
  - `nd67-annex1-tests.l4` ← `tools/annex1.py ../../source/raw/nd67-congbao-1017-1018.txt` (55 tests; prints the NOTES §5.1 table).
- `tools/vnsrc.py` extended with `src:ID:N` (approved by the lead).
- NOTES.md, GLOSSARY.md, COMPARABLES.md, SOURCE-LICENSE.md, encoding.json written.

## Remaining

Nothing. NOTES.md §6-§7 carry the final numbers (check.sh TOTAL 0 errors, 1487 satisfied, 0 failed, 0 refused; vnsrc gate `vnsrc check: 2062 src: lines, 651 Vietnamese runs, 0 problems`; literal command 6 problems, all in BRIEF.md). Final report sent to team-lead. Follow-up 2026-10-07: Decrees 105/2025 and 347/2026 read; neither reaches the motor provisions (NOTES §1.2a); downloads deleted.

## Where the hand-written modules come from

Templates `scratchpad/vn10/tpl/*.l4.in`, expanded by `scratchpad/vn10/expand.py DEPOSIT TPL OUT` (replaces `--@ 67a|67b|220 N [M]` with `vnsrc.py quote/quoteid` output). The deposited `.l4` files are complete without them; edit the `.l4` directly if the scratch is gone.

## Decisions

Forks F1-F36 and LAW L1-L9, findings R1-R16: NOTES.md §3-§4. Vintage chosen by contract conclusion date (F1); Decree 220 changes only the third-party word for the motor chapter; no answer differs between vintages.
