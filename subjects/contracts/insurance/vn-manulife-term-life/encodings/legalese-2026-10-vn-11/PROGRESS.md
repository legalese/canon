# PROGRESS: row VN-11 (enc-vn-11)

State on disk, for a resumed session. Read this and `BRIEF.md` first, then re-run `check.sh`.

## Done

- Modules, all type-checking: `vn11-nouns.l4`, `vn11-art01-02-definitions.l4`, `vn11-art03-benefits.l4`, `vn11-art04-07-premiums.l4`, `vn11-art08-13-conditions.l4`, `vn11-art14-18-administration.l4`, `vn11-death-claim.l4`, `vn11-tests.l4` (128 assertions), `vn11-findings.l4` (16 assertions).
- `NOTES.md` (sections 0-8: coverage table of 48 rows, forks F1-F26 and L1-L12, findings 1-16), `GLOSSARY.md`, `COMPARABLES.md` (25 rows), `encoding.json`, `SOURCE-LICENSE.md` (162 distinct src lines quoted).
- Last `check.sh` seen (2026-10-06, after the stray `vn13-nouns.l4` had been removed): `TOTAL (9 modules) 0 144 0 0`, exit 0.
- Gate (every `.l4` and every `.md` except `BRIEF.md`) last seen ending `0 problems`.

## Remaining, in order

Nothing. `check.sh` was re-run at 00:06 on 2026-10-07: `TOTAL (9 modules) 0 144 0 0`, exit 0. The gate (every `.l4` and `.md` except `BRIEF.md`) ends `0 problems` (NOTES.md section 7). The one step left after writing this line is sending the final report to the lead; a resumed session that cannot tell whether it went should send it again.

## How the `.l4` files are made

They are generated, not hand-edited: templates in `scratchpad/enc-vn-11/tpl/vn11-*.l4` hold `{{Q N M}}` placeholders, and `python3 -I scratchpad/enc-vn-11/vn11_expand.py` replaces each with `tools/vnsrc.py quote` output and writes the result here.
`{{GEN TABLE 3B}}` in the tests template is replaced by the output of `scratchpad/enc-vn-11/vn11_table3b.py`, which reads the Art 3(b) table from the raw text.
Edit the template, never the deposited `.l4`, or the next expansion overwrites the edit.
(`scratchpad` is `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad`, shared with other encoders; only `enc-vn-11/` is this row's.)

## Decisions

All recorded in `NOTES.md` section 3 (forks) and section 4 (findings); `encoding.json` summarises them.
