# PROGRESS

State at the end of the session (2026-10-10): every deliverable exists and `./check.sh` is clean (the numbers are in NOTES.md section 0, generated from the tool's output).

Workflow, for anyone resuming: modules are written as `templates/NAME.l4.in` and expanded with `python3 -I tools/expand.py` into `NAME.l4` (a `@@q N M` line becomes generated `-- src:` lines; a `@@fx` line becomes a complete test fixture). Edit the template, never the `.l4`. Then `./check.sh`. Documents: `python3 -I tools/gen_glossary.py` (GLOSSARY.md), `python3 -I tools/gen_notes.py` (NOTES.md, SOURCE-LICENSE.md, encoding.json; runs `check.sh` and `vnsrc`); prose lives in `templates/NOTES.md.in`, `templates/GLOSSARY-A.md`, `templates/coverage.tsv` and `tools/notes_data.py` (forks and findings).

Done:
- All 157 articles and 25 clauses have a disposition (see `tools/roadmap.py status registers/roadmap-*.json`): none `deferred`, none `out-of-scope`; 21 articles `inert` with reasons in NOTES.md section 2.
- Modules: law08-vintage, law08-nouns, law08-ch1-general, law08-ch2-general, law08-ch2-life-health, law08-ch2-property, law08-ch3-scope, law08-ch3-licensing, law08-ch3-products, law08-ch3-finance, law08-ch3-solvency, law08-ch4-intermediaries, law08-ch5-ch6-micro-state, law08-ch7-commencement, with one tests module each and law08-tests-findings (evidence for the findings).

If anything further is done: re-run `expand.py`, `check.sh`, `gen_glossary.py`, `gen_notes.py`, in that order, and copy the `vnsrc` line from NOTES.md section 7.
