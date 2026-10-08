# PROGRESS — row VN-09 (`legalese-2026-10-vn-09`), encoder enc-vn-09

Updated 2026-10-07 00:53 SGT. Complete.

## Done

- All 13 `.l4` modules written and green. Last `check.sh` (2026-10-06 23:32-23:51): `TOTAL (13 modules) 0 285 0 0`, exit 0 (amounts 87, cover 176, findings 22 satisfied; every other module 0).
- `vnsrc check` over every `.l4` and `.md` except BRIEF.md: `vnsrc check: 632 src: lines, 0 Vietnamese runs, 0 problems`. The literal brief command (with BRIEF.md) reports 2 problems, both in BRIEF.md.
- GLOSSARY.md, COMPARABLES.md (25 rows), SOURCE-LICENSE.md written.
- NOTES.md and encoding.json complete (no placeholders left).

## Remaining

Nothing. Harness probe run (3 failed + 1 "expected a refusal" failed + 1 satisfied, 4 errors, exit 0, as designed); NOTES.md and encoding.json placeholders filled; gate re-run 2026-10-07: `vnsrc check: 632 src: lines, 0 Vietnamese runs, 0 problems`. The `.l4` files have not changed since 23:17, before the check.sh run whose totals are recorded. Final report sent to the lead.

## How the generated files are made

- The `.l4` files are expanded from templates in `scratchpad/vn09/tpl/` by `python3 -I scratchpad/vn09/vn09_expand.py scratchpad/vn09/tpl DEPOSIT`: it replaces `@@src N M` markers with `tools/vnsrc.py quote` output, and generates the refusal table and the fact list in msig-cgl-record.l4 from the `A fact` enum in the nouns template. If the scratchpad is lost, the DEPOSIT `.l4` files are the source of truth; edit them directly.

## Decisions

Forks F1-F40 and findings X1-X23 are in NOTES.md §3-§4; encoding.json lists the forks.
