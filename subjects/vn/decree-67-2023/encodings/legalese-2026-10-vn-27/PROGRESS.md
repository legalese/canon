# PROGRESS — row VN-27 (enc-vn-27)

Updated 2026-10-07, end of session.

## Done

- All 10 `.l4` modules written and green. Last `check.sh` (2026-10-07, after the last module change): `TOTAL (10 modules) 0 errors, 445 satisfied, 0 failed, 0 refused`, exit 0, about 46 s.
- Harness shown to fail: a scratch copy with three expected values altered printed 3 failed, 3 errors, exit 1 (NOTES.md §6); the copy is deleted.
- Generated file: `nd67-vn27-art17-tests.l4` <- `python3 -I tools/art17.py ../../source/raw/nd67-congbao-1017-1018.txt` (316 tests).
- NOTES.md, GLOSSARY.md, COMPARABLES.md, SOURCE-LICENSE.md, encoding.json written.
- vnsrc gate (every .l4 and .md except BRIEF.md): 0 problems (the exact line is in NOTES.md §7 and encoding.json).

## Remaining

Nothing but the final report to the lead.

## Where the hand-written modules come from

Templates `scratchpad/vn27/tpl/*.l4.in`, expanded by `scratchpad/vn27/expand.py DEPOSIT TPL [NAME...]` (replaces `--@ 67|6719|220 N [M]` with `vnsrc.py quote/quoteid` output, gazette running heads dropped). The deposited `.l4` files are complete without them; edit the `.l4` directly if the scratch is gone.

## Decisions

Forks V1-V24 and LAW L1-L6, findings R1-R16: NOTES.md §3-§4. The vintage is the one in force on the event's date (V1); Decree 220 changes no provision this row encodes; no answer differs between vintages. One encoding error was caught by a test and fixed (an unforced vintage let a pre-Decree-67 date through; every answer function now forces it).
