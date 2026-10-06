# Encoding brief: Income Tax Ordinance s 66 (separate calculation), in L4

You are producing an L4 encoding of section 66 of the Income Tax Ordinance [New Version] from its Hebrew source.
This brief is the whole specification.
Read it fully before opening any source.

Row IL-02, run id IL-02-20261006.
Sibling rows: IL-01 (ss 33A, 34, 36, 36A) and IL-03 (ss 120B, 121, 121B), encoded in parallel and not yet landed.

## The subject

**פקודת מס הכנסה [נוסח חדש], סעיף 66 — חישוב נפרד** — Income Tax Ordinance [New Version] (דמ״י תשכ״א, 120), section 66, "Separate calculation".

Section 66 sits in Part D, Chapter 3 (הכנסת בני־זוג, "income of spouses").
Section 65 makes the income of spouses the income of the registered spouse (בן הזוג הרשום) and charges it in that spouse's name.
Section 66 opens "notwithstanding section 65" and lets the other spouse claim a separate calculation of the tax on income from personal exertion, says where income not from personal exertion goes, lets either spouse claim a separate calculation of income from pre-marriage or inherited property, sets the deductions and credit points that apply in a separate calculation (including the credit points for children), and restricts all of this where the spouses share a common source of income.

There is one text, and one vintage of it:

| vintage | source | where |
| --- | --- | --- |
| AS AMENDED AT RETRIEVAL | Hebrew Wikisource consolidation, retrieved 2026-10-06, sha256 `b87f2cf4…94b81b6`; amendment list for s 66 ends at תשפ״ד־3 | `registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt`, lines 2454-2484 |

Hebrew is authoritative.
The file is an unofficial consolidation, not an official text; Israel publishes no free official consolidation.
It shows the law as amended at retrieval and nothing earlier: what it does not show, you do not know.
Two Israel Tax Authority circulars (an aid, not a source of law) fix the tax year from which the current children's credit-point figures apply; they are cited in NOTES.md.

## Scope — pinned, do not widen or narrow

Section 66, every subsection and paragraph: (a)(1)-(3), (b), (c)(1), (1A), (2), (3), (4) with (a), (a1), (b)-(d), (4A), (5) with (a)-(c), (5A), (6), (d)(1)-(2), (e).
Spent text ("deleted", "expired", "repealed") is carried as an inert stub so the section has no silent gap.

Out of scope, taken as GIVEN inputs with a citation wherever s 66 points at them:
the credit-point counts under ss 34, 35, 36 (IL-01 for 34 and 36), the value of a credit point (s 33A, IL-01), the tax on income from personal exertion (ss 121 ff., IL-03), whether a spouse is entitled to a credit point under s 37, and the content of s 65 itself.
The definition of "year of birth" and "year of majority" in s 40(b)(3) is incorporated by s 66(c)(4) and is encoded where it is used.

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, each starting `@lang en`, English backtick identifiers that read like the section.
   One nouns module (DECLARE only) that every other module imports; then one module per subsection or group of subsections; then the tests.
2. A tests module whose expected values come from the SOURCE: both sides of every threshold, one scenario per route through each paragraph, every row of the children's credit-point table for the woman and for the man.
   A second tests module transcribes the Israel Tax Authority's own published tables for 2024 onward.
3. `NOTES.md`: scope, a coverage table, a fork register, an answer table (credit points per child per age in the tax year, for the woman and for the man), the numbers `check.sh` prints, open questions.
4. `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`.

## Rules that matter

- **Encode isomorphically.** Every rule carries `@ref` to the paragraph and the source line.
- **Tax years.** The text answers tax years from 2024 (the last amendments to s 66 apply from 1 January 2024). For an earlier tax year the encoding does not hold the text, and refuses.
- **Where the source does not answer, `REFUSE "…"`** — never `FALSE`, `0` or a plausible default.
- **A failing assertion is a finding.** Never edit an expected value to match what the code computed.
- **Read the diagnostics, not the exit code.** Report the numbers `check.sh` prints.
- **Numbers that are not statutory constants are not invented.** Section 66 has none of its own; the value of a credit point is a GIVEN with no default.
- **Semi-cleanroom.** Nothing from the Axiom Foundation or any RuleSpec encoding is read.

## Toolchain

The binary is `/Users/mengwong/.local/bin/l4` (no `--version`; build undetermined).
Leave `JL4_LIBRARY_PATH` unset.
`L4=/Users/mengwong/.local/bin/l4 ./check.sh` runs every module.
