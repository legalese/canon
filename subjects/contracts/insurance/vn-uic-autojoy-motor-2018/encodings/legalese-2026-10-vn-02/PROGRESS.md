# PROGRESS — row VN-02 (enc-vn-02)

State on disk, so a killed session can resume. Read BRIEF.md and this file first, then re-run check.sh.

## Done

- 15 `.l4` modules, all green. Last full `check.sh` (2026-10-06 23:40, `L4=/Users/mengwong/.local/bin/l4 ./check.sh`):
  `TOTAL (15 modules)                             0       322       0        0` (errors, satisfied, failed, refused).
  Per module: findings 26, tests-cover 78, tests-duties 14 (+ 21 #TRACE whose printed results match the comments above them), tests-general 68, tests-p2-p3 37, tests-settlement 74, tests-tables 25; rule modules and fixtures 0.
- `vnsrc check` over `*.l4`: 0 problems (before GLOSSARY.md was written).
- GLOSSARY.md written; vnsrc check 0 problems.
- NOTES.md written (148-row coverage table: 125 encoded, 20 inert, 2 out-of-scope, 1 reached-and-refused; forks F1-F44 + LAW points; findings V1-V27); §6 and §7 still carry placeholders for the final check.sh and vnsrc lines.

## Remaining

Nothing but the final report. Final check.sh (2026-10-07 00:30-00:54): `TOTAL (15 modules)                             0       322       0        0`, exit 0.
vnsrc gate (every .l4 and .md except BRIEF.md): `vnsrc check: 1121 src: lines, 688 Vietnamese runs, 0 problems`.
NOTES.md §6-§7 and encoding.json self_check are filled from those outputs (scratchpad/vn02/tools/fill_results.py).

## Scratch I depend on

`scratchpad/vn02/` (the session scratchpad, path in BRIEF's environment):
- `vn02/src/*.l4.in` — the module templates; `--@@src N M` lines are expanded by
- `vn02/tools/expand.py` (calls DEPOSIT `tools/vnsrc.py quote`), driven by
- `vn02/tools/build.sh` (also regenerates `uic-autojoy-tests-tables.l4.in` with `vn02/tools/gen_tables.py` from the raw text).
Edit a template, run `vn02/tools/build.sh`, never edit the deposited `.l4` by hand.
Verified 2026-10-07: rebuilding from `vn02/` reproduces every deposited module byte for byte.
