# us/regcf — `legalese` row

Free prose for humans. **No script reads this file.**
Facts about the regulation are in `../../subject.json`, and facts about this encoding are in `encoding.json`.

## 0. Where this row came from, and what did not come with it

Deposited on 2026-09-23 from `legalese/l4-ide`, byte-identical to `jl4/examples/legal/regcf/` at l4-ide `7df7a3ca6`: `regcf.l4`, `regcf-wizard.l4`, their eight goldens under `tests/`, and `fork-register.json`, which is now `registers/fork-register.json`.
The encoding's history, from its first commit on 2026-07-25 onward, is in l4-ide.
From this deposit on, a change to the encoding is made **here**. l4-ide's copy becomes its vendored mirror, `jl4/examples/canon/us/regcf/`, in the change that bumps its `etc/canon-pin.json` to a commit containing this row, and after that a change reaches l4-ide only through a pin bump.

Three things stayed in l4-ide, at `jl4/examples/legal/regcf/`, and have no copy here:

- **`README.md`** — the corpus's design record: scope boundary, where the mirrored wiki page is wrong or stale, known gaps, run evidence. It is the fullest account of this encoding and should be read before this file. It stayed because l4-ide's pipeline explainer cites it by line, and a copy here would drift from it unchecked.
- **`PROJECTIONS.md`** — the DMN and BPMN projections of `regcf.l4`, whose goldens are l4-ide's exporter regression tests (`jl4/examples/dmn/expected/regcf-corpus.*`, `jl4/examples/bpmn/expected/regcf-*`).
- **`figures/`** — ladder figures generated from `regcf.l4` by l4-ide's `ts-shared/ladder-svg`, which checks them against the corpus in its own test suite.

The pipeline sidecar for this subject is l4-ide `etc/go/subjects/regcf/`, including the explainer.

## 1. What it encodes

Read `encoding.json`'s `scope`.
The short version: the eight requirement groups a single wiki page presents, and nothing beyond them, with a rule-version axis back to commencement.

## 2. The wiki page it mirrors

`regcf.l4:14` names the page it is scoped to, the Lexipedia page `reg_cf_exemptions`, and `regcf.l4:19-26` follows that page's eight group headings.
The module quotes none of the page's prose.
The page is CC BY-SA 4.0 and is attributed where it is actually discussed, in the README that stayed in l4-ide.

## 3. Paths inside these files are l4-ide paths

Comments in the modules and fields in `registers/` name paths in `legalese/l4-ide` (`jl4/examples/...`), because that is where they were written and where the pipeline that reads them runs.
They are left as deposited.

## 4. Not reviewed

No HG1 grant or waiver was found for this encoding.
