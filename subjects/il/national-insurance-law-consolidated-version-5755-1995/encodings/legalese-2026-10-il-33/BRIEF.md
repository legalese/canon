# Encoding brief: National Insurance Law statuses and the surroundings of the child allowance, in L4 (row IL-33)

Row IL-33, run id `IL-33-20261008`, encoder `enc-il-33` (one session, no sub-agents).
This brief restates the lead's task in the template of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, so that a reviewer or an independent test author can work from it alone.
It was written before the modules; the coverage table in `NOTES.md` says what each provision came to.

## The subject

**חוק הביטוח הלאומי [נוסח משולב], התשנ״ה–1995** — the National Insurance Law [Consolidated Version], 5755-1995, as consolidated on Hebrew Wikisource (unofficial; Hebrew is authoritative) and deposited at `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`, sha256 `78bf47ee29a300d51c5c7646cf85992d7de78aa1380bd8460a4a18265f552a97`.
Read with it, each deposited in its own subject:

| instrument | file | sha256 |
| --- | --- | --- |
| National Insurance (Rules for Rounding Amounts) Regulations, 5746-1985 | `../../registers/source-bundle/regulations/national-insurance-rules-for-rounding-amounts-regulations-5746-1985.he.wiki.txt` | `011cb249…d7767d6` |
| National Insurance (Family Allowance) Regulations, 5720-1960 | `../../registers/source-bundle/regulations/national-insurance-family-allowance-regulations-5720-1960.he.wiki.txt` | `fcfeacc2…c80a3c` |
| Income Support Law, 5741-1980 | `../../../income-support-law-5741-1980/registers/source-bundle/income-support-law-5741-1980.he.wiki.txt` | `91649d296640cdda7afa4e15defc85f6326d489e8090628455ab4425e3bca1a7` |
| Maintenance (Assurance of Payment) Law, 5732-1972 | `../../../maintenance-assurance-of-payment-law-5732-1972/registers/source-bundle/maintenance-assurance-of-payment-law-5732-1972.he.wiki.txt` | `0607398dfacb57edabe8a88a89f0e0d25202ee5a1468d5d08bf20a4e27d2e8d7` |
| CBS consumer price index, general (code 120010), January 2000 to August 2026 | `../../registers/source-bundle/data/cbs-cpi-general-120010-2000-01-to-2026-08.json` and the `-with-linkage-coefficients` twin | `11a1b271…eeb8`, `cf440d64…b00f9` |

## Why this row exists

The capstone `employed-parent-monthly-net` (version 0.4.0) and rows IL-06 and IL-08 take as inputs a set of statuses and surrounding provisions, and record them as gaps: capstone `GAPS.md` item 13 (residence, s 238) and item 9 (the statuses s 335 reads); IL-06 `NOTES.md` (not encoded: s 69, s 69A, s 71, s 238, s 381 and the rounding regulations, the updating clause of s 1, the Income Support Law, the Maintenance Law, the Family Allowance Regulations).
This row encodes those, so that the capstone can derive the statuses from facts.
It never edits the capstone or another row.

## Scope — pinned

In priority order, as the lead set it:

1. The statuses s 335 reads and ss 65-66 read, derived from facts: insured under Chapter 5 (ss 75-76), Chapter 6 (s 150), s 158(1) of Chapter 7 (and s 158(2)-(3)), Chapter 8 (ss 180-181), Chapter 9 (s 195), Chapter 10 (s 223, long-term care), Chapter 11 (ss 238-240, 243), with the ages of Schedule A1 (Parts A, B, C, E) and s 1 "גיל הפרישה".
2. s 238 "עקרת בית" (housewife), "אלמנה", "אלמנה בת קצבה"; and residence: s 2A (who is not a resident) and s 65(a) "יושב בישראל".
3. ss 69, 69A and 71.
4. s 381 and the Rounding Regulations 5746-1985.
5. The updating clause of s 1 "הסכום הבסיסי"; the Family Allowance Regulations 5720-1960; the Income Support Law 5741-1980; the Maintenance (Assurance of Payment) Law 5732-1972.

Not in scope, and not to be touched: ss 65-68 and 72 and s 335 themselves (rows IL-06 and IL-08).
IL-06's fork F18 (a resident housewife under s 65(a) "מבוטח") is left as it is: this row encodes the definitions F18 reads and does not rule on it.

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, each starting `@lang en`: one nouns module (`DECLARE` only); one rules module per section or instrument; a published-figures module for the CPI values (data, not law, with provenance); tests modules.
2. `NOTES.md`: scope, coverage table (no row left `deferred`), fork register (each as "ruled by Meng 2026-10-08 (SHRUG)"), answer table, `check.sh` output, open questions, inputs the capstone does not supply today.
3. `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`, `tools/` (`srcquote.py`, `hebcheck.py`, copied unchanged from IL-06).

## Rules that matter

- Policy for every ambiguity (Meng, SHRUG, 2026-10-08): where the text is silent or two readings are arguable and give different answers to a question someone would ask, one named switch, default DECLINE (a refusal by name saying the text does not decide), the other readings kept by name and tested; the default declines only where the readings differ for the question asked.
- Never invent a number: a figure published elsewhere goes in a marked module with its source and hash. Where the sources do not answer, `REFUSE "…"`.
- Expected values worked by hand from the Hebrew before the run; a failing assertion is a finding.
- Semi-cleanroom against the Axiom Foundation: no RuleSpec, tests, ENCODING-GAPS or "Comparison with Axiom" section was read.
- A provision that needs a text not deposited is refused by name and recorded as "needs a source" (the Entry to Israel Law and Regulations; the regulations under ss 75, 243; the Security Service Law s 16(1); the regulations under the Maintenance Law).

## Toolchain

`/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset; `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
The binary's sha256 is recorded before and after each check run.
