# je/charities-2014 — `cleanroom-2026-08` row

Free prose for humans. **No script reads this file.**

## 0. Where this row came from, and why its layout was not changed

Deposited on 2026-09-23 from `legalese/l4-ide`, byte-identical to `jl4/examples/legal/charities-cleanroom/` at l4-ide `7df7a3ca6`.
That is all 28 files, **in their original layout**.
The history is in l4-ide.
l4-ide's vendored mirror places this row at `jl4/examples/canon/je/charities-2014/`, and it carries `charity-test.l4`, `tests/`, `encoding.json` and `SOURCE-LICENSE.md`.

The layout departs from the sidecar table in `subjects/README.md` on purpose:

- `SOURCE-EXTRACT.md` (the verbatim source articles) stays in the row, not in a subject-level `source/`.
- `COMPARISON.md` and `PROJECTIONS.md` stay beside the module, not under `report/`.
- `comparison/` stays as it is, not under `registers/`.
- `charity-test.cases.json` stays at the row root.

`README.md` links those files by relative path, and `projections/make-cases.py` writes `../charity-test.cases.json`, so rearranging them would have broken both.
The surface map is therefore `comparison/charity-test.surface-map.json` and not `registers/surface-map.json`.
That keeps it out of l4-ide's mirror, which carries only `registers/*.json`.
Nothing in l4-ide reads it: no pipeline sidecar declares this subject.

## 1. What it is

This is a cleanroom smoke test.
It encodes the charity test of the Law, Articles 5 to 7, **de novo from the primary source**, without sight of the earlier encoding of the whole Law in l4-ide's `paper/case-studies/charities-jersey-2014/`.
`README.md` §7 is the integrity declaration, and it discloses one contamination.
`COMPARISON.md` and `comparison/` are the three-way comparison with that earlier encoding and with a third-party wiki's process model.
`PROJECTIONS.md` records why the emitted DMN does not execute on either engine, and why the obvious fix would give a silent wrong answer.

## 2. Things a reader will trip on

- `comparison/make-surface-map.py:5-6` hard-codes absolute paths on the machine that ran it (`/Users/mengwong/src/legalese/l4wt/charities-cleanroom/...`).
  It will not run anywhere else unedited, and it is left as deposited because it is the record of what produced `comparison/charity-test.surface-map.json`.
- Paths in the surface map and in `README.md` are l4-ide paths.
- `COMPARISON.md` discusses and counts pages of `lexipedia.xyz` from read-only fetches on 2026-08-02/03.
  It describes and counts them, and it contains no block quotation of them.

## 3. Terms

The Open States Assembly Licence – Jersey v1.0.
The attribution is a licence condition, and it is recorded in `NOTICE`.
`SOURCE-LICENSE.md` quotes the publisher's copyright page and the licence, both read and dated 2026-09-23, together with Meng's statement of 2026-09-23 that this deposit rests on.

## 4. Not reviewed

No HG1 grant or waiver was found for this encoding.
