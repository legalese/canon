# Encoding brief: Income Tax Ordinance ss 1, 2, 35, 37-40, 45A, 47, 64B, 65 and 121A, in L4 (row IL-08)

Row IL-08, run id `IL-08-20261007`, encoder `enc-il-08` (one session, no sub-agents).
This brief restates the lead's task in the shape of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, so that a reviewer or an independent test author can work from it and the source alone.
Its companion is the National Insurance Law row of the same id, `../../../national-insurance-law-consolidated-version-5755-1995/encodings/legalese-2026-10-il-08/`.

## The subject

**פקודת מס הכנסה [נוסח חדש]**, the Income Tax Ordinance [New Version], as consolidated on Hebrew Wikisource and deposited at `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` (retrieved 2026-10-06, sha256 `b87f2cf4…94b81b6`).
Hebrew is authoritative; the file is an unofficial consolidation stated as amended at retrieval.

IL-08 is the **extension** row of the Israel tier: the provisions row IL-07 (the capstone, the monthly net income of an employed parent) needed and no earlier row encodes.
Its work order is IL-07's `GAPS.md`, in the order the capstone needs them.

## Scope, as ruled (`l4-pipeline/BACKLOG.md`, Tier 1, row IL-08 and the paragraph after the table)

**The row's own list:** ITO ss 1, 2, 35, 37 to 39, 40, 45A and 121A; NII s 65, s 67A and Schedule A1 Part D (the NII provisions are in the companion row).
**Added from the capstone's gap order, taken after the row's list:** ITO s 47, ITO s 64B with s 65, NII s 72, NII s 335.
**Out of this row:** the National Health Insurance Law, and ITO s 164 with its Regulations, because each needs its own source deposit.
Order of work: the row's list in GAPS order (s 45A, s 40, ss 37-39, s 35, then ss 1 and 2), then the additions in GAPS order (s 47, ss 64B and 65).
Because s 45A borrows three of s 47(a)'s definitions, s 47(a) was encoded with s 45A, and s 47(b)-(d) in its own turn.

Not edited: the capstone, and every existing row (IL-01 to IL-07).
Integrating these rows into the capstone is a later version of IL-07.

## Deliverables, all in this directory

1. `.l4` modules: a nouns module (`DECLARE` only); a tax-years module; a published-figures module (not law); one rule module per section or pair of sections, split along the source; six tests modules.
2. `NOTES.md`: coverage table (every provision in scope: encoded, inert, out-of-scope with a reason, or deferred), fork register, answer tables, what `check.sh` prints, open questions, nouns to reconcile, and which `GAPS.md` item each provision discharges.
3. `check.sh` (the skill's), `encoding.json` (status draft, HG1 not sought), `SOURCE-LICENSE.md`, and `tools/` (the quotation generator and checker, copied from rows IL-03 and IL-06).

## Rules that matter

- Isomorphic: one source provision, one recognisable place, its line number in an `@ref` or a `src:` comment.
- Hebrew is quoted only mechanically: `src:N` lines are generated from the source by `tools/srcquote.py`; every other Hebrew run is checked by `tools/hebcheck.py`; quotations of other documents are on `ext:[TAG]` lines and checked by script against the extracted text.
- Where the text does not decide, `REFUSE "…"` with a name; never a guessed 0 or FALSE.
- Figures that are not statutory constants are inputs; the Tax Authority's published figures are carried in a module labelled as not law, with URL, retrieval time and sha256.
- Tests come from the source; a failing assertion is a finding; expected values are never edited to match the code.
- Each row self-contained: cross-directory `IMPORT` does not work with this `l4`, so what another row declares is re-declared here, and every difference is recorded under "Nouns to reconcile".
- Semi-cleanroom with respect to the Axiom Foundation (ruled 2026-10-06): nothing of theirs read, and no row's "Comparison with Axiom's RuleSpec" section read.

## Toolchain

`/Users/mengwong/.local/bin/l4` (no `--version`), `JL4_LIBRARY_PATH` unset; `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
