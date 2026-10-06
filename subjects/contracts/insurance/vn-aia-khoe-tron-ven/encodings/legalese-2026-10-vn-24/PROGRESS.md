# PROGRESS — row VN-24 (enc-vn-24)

State on disk, for a resumed session. Read BRIEF.md first, then this.

## How the .l4 files are made

Every `.l4` here is GENERATED from a template in the scratch directory
`/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn24/`:

- templates: `scratchpad/vn24/tpl/<module>.l4.tpl`
- expander: `python3 -I scratchpad/vn24/bin/expand.py DEPOSIT scratchpad/vn24/tpl [module.l4 ...]`
  replaces each `@@src N [M]` line with `tools/vnsrc.py quote` output (watermark-only lines dropped).
- Edit the TEMPLATE, never the generated .l4, then re-expand.
- `scratchpad/vn24/condensed.txt` is a reading aid (source without watermark lines, raw line numbers kept).

## Done (typechecks)

- ktv-nouns.l4 (all DECLAREs incl. 72 CI findings records)
- ktv-annex1-definitions.l4 (dates, ages, eligibility, Hospital, ICU, Doctor, Accident, TPD, fraud)
- ktv-annex2-charges.l4, ktv-annex3-fund.l4
- ktv-annex4-coefficients.l4
- ktv-annex5-cancer.l4, ktv-annex6-early-ci.l4, ktv-annex7-severe-ci.l4 (all 45 items in one module; paediatric age limb at the end)
- ktv-part1-benefits.l4, ktv-part2-owner-rights.l4, ktv-part3-premiums-and-account.l4,
  ktv-part3-exclusions-and-termination.l4, ktv-part4-claims.l4, ktv-part5-general.l4 (all typecheck)
- vnsrc check over ktv-*.l4: 1234 src lines, 0 problems (2026-10-07)
- forks used in comments so far: F1-F6, F12, F14-F28; findings X1-X17 referenced in comments

## State: COMPLETE (2026-10-07)

check.sh (L4=/Users/mengwong/.local/bin/l4): TOTAL (22 modules) 0 errors, 574 satisfied, 0 failed, 0 refused; exit 0.
vnsrc gate (all .l4 and .md except BRIEF.md): 0 problems. Literal command: 1 problem, in BRIEF.md line 23.
Deliverables: 22 .l4 modules, NOTES.md, GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md.
Regenerating: edit scratchpad/vn24/tpl/*.tpl, then scratchpad/vn24/bin/expand.py; NOTES.md via build_notes.py;
GLOSSARY.md via gen_glossary.py; encoding.json via gen_encoding_json.py.
