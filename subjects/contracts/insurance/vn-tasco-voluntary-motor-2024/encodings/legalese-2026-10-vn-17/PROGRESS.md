# PROGRESS — row VN-17

State on 2026-10-07: **all deliverables written**; NOTES.md §6 and §7 carry the final `check.sh` and `vnsrc check` output.

If resumed: read BRIEF.md and NOTES.md, re-run `L4=/Users/mengwong/.local/bin/l4 ./check.sh` and
`python3 -I tools/vnsrc.py check ../../source/raw/tasco-voluntary-motor.txt` over every `.l4` and `.md` except BRIEF.md.

The `.l4` modules are generated from templates in the session scratch directory
(`scratchpad/vn17/tpl/`, expanded by `scratchpad/vn17/expand.py`); the injury table and its tests by
`scratchpad/vn17/table_gen.py` from `reviewed.tsv` (built by `mk_reviewed.py` from `draft.tsv`,
`edits.tsv`, `corrections.tsv`). Edit the templates, not the deposited files, if the scratch survives;
otherwise edit the deposited files directly and drop the templates.

All 82 pages have been viewed as images. Nothing remains deferred.
