# Encoding brief: Income Tax Ordinance, earlier vintages of s 66(c)(4)-(6) and s 121B(a1) for 2025, in L4

Row IL-31, run id `IL-31-20261008`, encoder `enc-il-31` (one session, no sub-agents).
This brief is the whole specification.
It restates the lead's task in the template of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, so that a reviewer or an independent test author can work from it alone.

## The subject

**פקודת מס הכנסה [נוסח חדש]**, the Income Tax Ordinance [New Version], דמ״י תשכ״א, 120, as amended.
Rows IL-02 (s 66, the separate calculation for spouses) and IL-03 (ss 120B, 121, 121B) encode the text as consolidated at 2026-10-06, and each declines the years its sources do not reach.
This row takes the two gaps those rows recorded, now that the amending Acts are deposited:

1. **s 66(c) before 2024.**
   IL-02 refuses every tax year before 2024 (`ito66-tax-years.l4`; IL-02 NOTES.md assumption A1).
2. **s 121B(a1) for 2025.**
   IL-03 refuses every tax year before 2026 (`ito-121b-additional-tax.l4`; IL-03 NOTES.md assumption A1, fork question 4).

## The vintages and their sources

Hebrew is authoritative.
The sources are the enacting Acts, deposited as the Knesset's own PDFs (`../../registers/source-bundle/amending-laws/`, listed with hashes in `SOURCES.json`), and the unofficial Hebrew Wikisource consolidation of the Ordinance (`../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt`, sha256 `b87f2cf437ccfed35c3164681f4fc7ee015a111633454622751930c8894b81b6`).

| Act | Sefer HaChukim | what it does to the Ordinance | file |
| --- | --- | --- | --- |
| Law for Increasing Credit Points for Parents (Temporary Provision), 5782-2022 | 2972, 18 May 2022 | amendment 260; for income produced in 2022 only, a further credit point for a child under 13 who is not a toddler (s 40(c), s 66(c)(4)(d), (5A), (6)) | `24_lsr_624898.pdf` |
| Law for Increasing Credit Points for Parents and Expanding the Work Grant, 5783-2023 | 3048, 7 June 2023 | amendment 267; rewrites s 40(b) and s 66(c)(4)-(6) (deletes "toddler"); from 1 January 2024 | `25_lsr_2656507.pdf` |
| Law for Assistance to Parents of Children up to Age Three (Legislative Amendments), 5784-2024 | 3184, 20 March 2024 | amendment 271; the credit points of s 40(b) and s 66(c)(4)-(5) by age; from 1 January 2024 | `25_lsr_4239836.pdf` |
| Economic Efficiency Law (Legislative Amendments for the 2025 Budget Year) (Freezing of Tax Updates and Surtax), 5785-2024 | 3342, 26 December 2024 | amendment 276; s 120B(e) (freeze), s 121B(a1) (new), s 121B(e); from 1 January 2025 | `25_lsr_5396578.pdf` |

The Acts' text layers scramble digits and parentheses, so every figure and date was read from the page image and checked against the text layer (NOTES.md section 7).
An Act of amendment says "in place of X put Y"; it never prints the whole text.
So the Acts give a chain that can be walked forward from a base text and cannot be walked backward from the current text without the words each step replaced.
**What the sources do not show, this row does not know.**

## Scope, pinned

- **Part A.** s 66(c)(4), (4A), (5) and (6), the children's credit points, by tax year:
  - 2024 and later, the credit points the Acts' words give a child by age (before the mother's election of (4)(a1), whose enacting Act is not deposited);
  - 2022, the further credit point of Act SH 2972 only;
  - 2023 and every year before 2022, declined by name.
- **Part B.** s 121B in tax year 2025: (a), (a1), (b), (d) as an input convention, (e) with both definitions; (c) inert.
- Out of scope, with reasons in NOTES.md: s 66(a), (b), (c)(1)-(3), (d) in earlier vintages (no Act deposited changes them, and none shows their earlier text); s 40 in every vintage (not named by the row; its amendments by the same Acts are listed in the coverage table); the work-grant provisions of the same Acts; s 120B(e) (row IL-03, which the same Act enacts; read here only to confirm it); the Real Estate Taxation Law (read only for the s 9(c2) adjustment rule that s 121B(e) borrows).

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, each starting `@lang en`: a nouns module (`DECLARE` only), one rules module for each part, a tests module; and `ito-il03-nouns.l4`, vendored from row IL-03 byte for byte (recorded sha256) because imports resolve only beside the importing file.
2. `NOTES.md`: scope, coverage table with no row left `deferred`, fork register, answer table, `check.sh` output, what IL-02, IL-03 and the capstone would change to call this row, inputs the capstone does not supply today, open questions.
3. `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`, `tools/` (the two quotation checkers).

## Rules that matter

- **Vintages are never merged.**
  A tax year the Acts do not reach is declined by a named `REFUSE` that says what source is needed.
- **Do not invent a number.**
  The s 121B(a) amount for 2025 is an income ceiling fixed by s 120B(e)(1); the rounding Order is not deposited, so the amount is an input.
  A test scenario uses 721,560, the consolidation's editorial figure, labelled as not law.
- **Policy for every ambiguity** (Meng, SHRUG, 2026-10-08): one named switch, default decline where the readings give different answers to the question asked, the other readings kept by name and tested; an ambiguity on which the readings agree is answered.
- **A failing assertion is a finding.**
  Every expected value was worked by hand from the Hebrew, with the arithmetic in a comment, before it was run.
- Money is new Israeli shekels, as a bare `NUMBER`; amounts are annual; rates are percent literals.
- Semi-cleanroom (ruled 2026-10-06): nothing from the Axiom Foundation or any RuleSpec encoding was read.
