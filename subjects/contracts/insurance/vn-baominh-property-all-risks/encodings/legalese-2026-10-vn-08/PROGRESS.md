# PROGRESS — row VN-08 (`legalese-2026-10-vn-08`), encoder `enc-vn-08`

State at 2026-10-07, after the usage-limit reset.

## Done

- All 12 `.l4` modules (nouns, cover, exclusions, quantum, conditions, claim, fixtures, four tests modules, findings).
- `NOTES.md` (sections 0-9: coverage table of 92 rows, 34 forks, 23 findings), `GLOSSARY.md` (283 rows), `COMPARABLES.md` (25 rows), `encoding.json`, `SOURCE-LICENSE.md`.
- Last `check.sh` run (2026-10-06, all modules as they now stand): `TOTAL (12 modules) 0 262 0 0`, exit 0.
- Harness shown to fail: a mutated copy of the quantum tests gave 5 errors, 5 failed, exit 1.

## Remaining

Nothing but the final report. The vnsrc gate (every `.l4` and `.md` except `BRIEF.md`) ends `vnsrc check: 455 src: lines, 856 Vietnamese runs, 0 problems`; it is in `NOTES.md` section 7 and `encoding.json`.

## Where the generated files come from

Scratch directory: `scratchpad/enc-vn-08/` (this session's scratchpad), never the shared root.
- `bin/expand.py` expands `tmpl/baominh-par-*.l4` into this directory, generating every `-- src:N |` line with `tools/vnsrc.py quote`; `bin/build.sh` runs it and typechecks.
- `bin/gen-scale.py` generates the GC 3 short-period rows and their tests from `src:277-281` (`tmpl/scale-rows.inc`, `tmpl/scale-tests.inc`).
- `bin/gen-glossary.py` writes `GLOSSARY.md`.
If the scratch directory is lost, the `.l4` files here are the authority: edit them directly.

## Decisions

All forks are in `NOTES.md` section 3 and `encoding.json` `forks`; none is pending.
