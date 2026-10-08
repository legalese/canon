# PROGRESS — row VN-07 (`legalese-2026-10-vn-07`), encoder enc-vn-07

State as of 2026-10-06, 23:2x local. **All deliverables exist; the row is complete.** The final report has been sent to the lead.

## Done

- Eight `.l4` modules: nouns, insuring clause, exclusions, average and deductible, general conditions, claim, tests (262 assertions, 9 traces), findings (36 assertions).
- `NOTES.md` (sections 0-8: coverage table 58 rows with 0 deferred, 37 F forks + 15 LAW forks, 21 findings), `GLOSSARY.md`, `COMPARABLES.md` (25 rows), `encoding.json`, `SOURCE-LICENSE.md`.
- `check.sh` and `BRIEF.md` unedited.

## Last tool output (final run, 2026-10-06)

- `check.sh`: `TOTAL (8 modules)                              0       298       0        0`, exit 0.
- vnsrc gate (every `.l4` and `.md` here except `BRIEF.md`): `vnsrc check: 350 src: lines, 512 Vietnamese runs, 0 problems` (before this file was added; this file has no Vietnamese).
- vnsrc literal briefed command (includes `BRIEF.md`): `vnsrc check: 350 src: lines, 520 Vietnamese runs, 1 problems`, the one problem being `BRIEF.md:31`, not this encoding's.

## What remains

Nothing required. Optional, only if the lead asks: an independent test pass (brief excluded sub-agents); HG1.

## If resumed

1. Read `BRIEF.md`, then this file.
2. Re-run `L4=/Users/mengwong/.local/bin/l4 ./check.sh` (it can take over two minutes when the machine is busy) and the vnsrc gate:
   `python3 -I tools/vnsrc.py check ../../source/raw/uic-par.txt *.l4 COMPARABLES.md GLOSSARY.md NOTES.md SOURCE-LICENSE.md PROGRESS.md`.
3. If both match the lines above, there is nothing to do.

## Scratch the deposit depends on (not needed to use it; needed to regenerate it)

Directory: `~/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn07/` (private subdirectory; the scratchpad root is shared by all encoders).

- `tpl/*.l4`, `tpl/NOTES.md`, `tpl/GLOSSARY.md`, `tpl/COMPARABLES.md`: templates; `{{src N M}}` lines expand to `tools/vnsrc.py quote` output.
- `gen_tests.py`: builds `tpl/uic-par-tests.l4` from `tests-head.l4.in` + generated Exclusion A triggers (read from the cause lists in `tpl/uic-par-exclusions.l4`) + `tests-body.l4.in`.
- `build.py TPL OUT`: expands the `{{src}}` placeholders, writing to `out/`.
- `fill.py`: fills `{{CHECKSH}}`, `{{VNSRC}}`, `{{VNSRC_MINE}}` in the deposit's `NOTES.md`, and writes `encoding.json` (from `encoding.json.in`) and `SOURCE-LICENSE.md` (from `SOURCE-LICENSE.md.in`), from `checksh.txt`, `vnsrc.txt`, `vnsrc-mine.txt`.
- Regenerate: `python3 -I gen_tests.py && python3 -I build.py tpl out`, copy `out/*.l4` and the three `.md` into the deposit, run check.sh and vnsrc into those three `.txt` files, then `python3 -I fill.py`. Note the deposit's `NOTES.md` §7 carries one later hand edit (the "This is the gate" sentence), mirrored in `tpl/NOTES.md`.

## Decisions to keep

All forks are in `NOTES.md` §3 and `encoding.json`. The ones a regenerator must not lose: F1 (cover from the later of premium and Period start), F5 (A1/A2 reach the causal chain; A3/A4 every cause), F7 ("riot or rebellion" one constructor), F12 (B4 = excess only), F17 (B4, then average, then GC 6, then item cap), F19 (deductible after caps), F20 (GC 6 declines unless nil), F25 (GC 12 tested when the twelve months end).
