# Encoding brief: ITO s 164 and the Deduction from Salary and Wages Regulations 5753-1993 (withholding), in L4

Row IL-26, run id `IL-26-20261008`, encoder `enc-il-26` (one session, no sub-agents).
This brief restates the lead's task in the template of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, so that a reviewer or an independent test author can work from it alone.

## The subject

**פקודת מס הכנסה [נוסח חדש], סעיף 164 (חובת ניכוי במקור)** and **תקנות מס הכנסה (ניכוי ממשכורת ומשכר עבודה), התשנ״ג–1993**, the Income Tax (Deduction from Salary and Wages) Regulations 5753-1993, made under ITO ss 164, 166 and 243 and s 6 of the Employers' Tax Law 5735-1975.
Section 164 makes whoever pays certain kinds of income, employment income first among them, deduct tax at the time of payment "in the manner and at the rates prescribed".
For employment income the Regulations prescribe the manner and the rates: for a monthly salary, tax computed by Schedule A on twelve times the month's salary under ss 121 and 121B, less the employee's credit points, divided by twelve and rounded to the shekel, which the employer takes from the table the Director publishes.

There is one vintage in each source.

| source | where | sha256 |
| --- | --- | --- |
| the Ordinance, as amended at retrieval 2026-10-06 (s 164 is source lines 5322-5323) | `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` | `b87f2cf4...6b81b6` |
| the Regulations, as amended to 5785-2025 (Wikisource revision 2987411, retrieved 2026-10-08) | `../../registers/source-bundle/regulations/income-tax-deduction-from-salary-and-wages-regulations-5753-1993.he.wiki.txt` | `e6fd6975...b7b20f` |

Hebrew is authoritative; both files are unofficial Wikisource consolidations.
What they do not show, this encoding does not know.
The Director's published tables, the Tax Authority's monthly booklet and the orders and regulations made under s 164 for kinds of payment other than employment income are not deposited.

## Scope — pinned

- ITO s 164: the duty to deduct, the kinds of payment, the State as payer, and the instrument that prescribes the manner and rates.
- Regulations 1 (the definitions the deduction turns on), 2 (the employee's card), 3(a) and (b) (a month's salary, paid whole or in parts), 4(a) (a non-regular salary), 5(a) to (e) (a partial salary, a pension, an additional position, the sole-income declaration), 9 (what the employee may ask the assessing officer for) and 10 (coordination), and Schedule A in full.
- The annual adjustment is s 120B as IL-03 encodes it, passed through, not re-encoded: Schedule A takes ss 121 and 121B "with the necessary adjustments from s 120B".
- Out of scope, each with its reason in NOTES.md section 2: regulations 3(c)-(d) with Schedules B and C (day employees, foreign workers), 4(b), 6, 7, 8 (kinds of payment other than a resident employee's monthly salary), 11 to 15 (reporting, certificates, forms, commencement), and every kind of payment in s 164 other than employment income.
- A cumulative method of withholding: the Regulations print none; refused by name.

## Deliverables

1. `.l4` modules with ASCII filenames, each starting `@lang en`: a nouns module (`DECLARE` only), rules modules (`ito-il26-s164`, `ito-il26-schedule-a`, `ito-il26-regulations`, `ito-il26-claims`), a published-figures module (not law), and a tests module; plus the four IL-03 modules vendored (`VENDORED.txt`).
2. `NOTES.md`: scope, coverage table with no row left deferred, fork register, answer table, `check.sh` output, open questions, what the capstone needs.
3. `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`.

## Rules that matter

- Isomorphic: one source provision, one recognisable place, an `@ref` naming it and the source line; Hebrew only in `src:` comments generated mechanically.
- Ambiguity (Meng, SHRUG, 2026-10-08): one named switch per fork, default a refusal by name where the readings give different answers, every other reading kept and tested.
- No invented numbers: the credit point and the s 121B(a) amount are inputs, carried from the Tax Authority's published figures with provenance, in a module marked not law.
- Where the sources do not answer, `REFUSE`, never `FALSE` or `0`.
- A failing assertion is a finding; every expected value was worked by hand from the text before it was run.
- Semi-cleanroom against the Axiom Foundation: nothing of theirs was read.
