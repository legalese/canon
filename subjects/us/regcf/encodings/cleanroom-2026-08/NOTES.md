# us/regcf — `cleanroom-2026-08` row

Free prose for humans. **No script reads this file.**

## 0. Where this row came from

Deposited on 2026-09-23 from `legalese/l4-ide`, byte-identical to `jl4/examples/legal/regcf/denovo/` at l4-ide `7df7a3ca6`.
That covers `regcf-denovo.l4`, its four goldens under `tests/`, and the four deposit registers, now under `registers/`.
The source text it was encoded from, `denovo/source/`, is now the subject-level `../../source/`, because the text is a fact about the regulation and not about this row.
The history is in l4-ide.
l4-ide's vendored mirror places this row at `jl4/examples/canon/us/regcf/cleanroom/`.

The row is named for its occasion, as `sg/succession`'s second encoding is.
l4-ide's pipeline sidecar, `etc/go/subjects/regcf/subject.json`, declares it under the same id.

## 1. Why it exists

It is an independent encoding of the same regulation, written without reading the `legalese` row.
Its point is the comparison: `registers/surface-map.json` pairs decisions across the two rows, and l4-ide's differential oracle (`etc/go/lib/denovo-diff.mjs`) evaluates both over a generated battery.
Two encodings that agree because one was copied from the other would make that a self-check.

## 2. Paths inside these files are l4-ide paths

`regcf-denovo.l4:27` names its source as `jl4/examples/legal/regcf/denovo/source/part227.txt`.
That file is `subjects/us/regcf/source/part227.txt` here, and it is byte-identical: the `sha256` on the next line of the module still matches it.
The comment is left as deposited, because editing it would change the module's exactprint golden, and the point of this deposit was that nothing changed.
Paths in `registers/` are likewise l4-ide paths.

## 3. Not reviewed

No HG1 grant or waiver was found for this encoding.
