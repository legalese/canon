# Encoding brief: Income Tax Ordinance, ss 120B, 121 and 121B (indexation, the individual's rates, the additional tax), in L4

Row IL-03, run id `IL-03-20261006`, encoder `enc-il-03` (one session, no sub-agents).
This brief is the whole specification.
It restates the lead's task in the template of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, so that a reviewer or an independent test author can work from it alone.

## The subject

**פקודת מס הכנסה [נוסח חדש]** — the Income Tax Ordinance [New Version], דמ״י תשכ״א, 120 (New Version, 5721-1961), as amended (amending Laws past no. 285).
It is a Mandate-era ordinance re-enacted in a Hebrew New Version, and it is the central income-tax statute for individuals and companies.
This row covers three provisions:

- **s 120B (הצמדה, indexation)**, in Part 6.1, which on 1 January of each tax year adjusts the income ceilings, the credit-point and pension-point amounts, the social deductions and the recognised donation amounts by the rise in the consumer price index over the previous tax year, and which since the 5785 amendment freezes them for tax years 2025 to 2027;
- **s 121 (שיעור המס ליחיד, the individual's rate of tax)**, the marginal scale for an individual, with reduced rates for income from personal exertion and for an individual who has reached 60;
- **s 121B (מס נוסף על הכנסות גבוהות, additional tax on high incomes)**, a 3% surtax above a threshold, and since 5785 a further 2% on income from capital sources above the same threshold.

There is one vintage in the sources:

| vintage | source | where |
| --- | --- | --- |
| AS AMENDED AT RETRIEVAL | Hebrew Wikisource consolidation, raw MediaWiki, retrieved 2026-10-06, sha256 `b87f2cf437ccfed35c3164681f4fc7ee015a111633454622751930c8894b81b6` | `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` |

Hebrew is authoritative.
The file is an **unofficial consolidation**: Israel publishes no free official consolidated text, and the official version is the original publication plus every amending Law.
The consolidation's editors write adjusted figures into the text and annotate them with `{{ח:הערה|…}}` notes (for s 121, "(הסכומים מתואמים לשנים 2026–2027)"; for s 121B, "(נקוב לשנת 2017; …)").
Those notes and the tables of brackets after s 121 are **aids**, not law.
Earlier vintages of these sections (the text before the 5785 freeze and the 5786 bracket amendment) are not in the sources: **what they do not show, you do not know.**

## Scope — pinned, do not widen or narrow

- s 120B, every subsection: (a), (b), (c) (repealed), (d), (e)(1), (e)(2).
- s 121, every subsection: (a)(1)-(3), (b)(1)(a)-(d), (b)(2).
- s 121B, every subsection: (a), (a1), (b), (c), (d), (e) and its two definitions.
- The definitions these use, cited and encoded only as far as the three sections need them: s 1 ("הכנסה חייבת", "הכנסה מיגיעה אישית", "מדד", "שיעור עליית המדד", "סכום מתואם", "שנת מס", "פנקסים קבילים") and s 120A ("תקרות הכנסה").

Out of scope, with the reason recorded in NOTES.md: s 121A (row IL-08), the credit points of ss 33A-36A (row IL-01), the separate calculation of s 66 (row IL-02), the special-rate sections (ss 91, 122, 125B, 125C and others), and the Income Tax (Rules for Rounding Amounts) Order 5746-1986 made under s 120B(d).
Where one of these feeds a provision in scope, its result is an **input**, with a citation, never an encoding.

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, each starting `@lang en`: a nouns module (`DECLARE` only), one rules module per section (`ito-120b-…`, `ito-121-…`, `ito-121b-…`), and a tests module.
   Identifiers are English backtick names; Hebrew is quoted in comments, copied mechanically from the source file with its line number.
2. A tests module asserting what the SOURCE says: both sides of every band boundary in s 121(a) and (b), the age-60 boundary, the (b)(2) exclusion, both sides of the s 121B threshold and of the residential-apartment threshold, the freeze years and the years either side of them, and the s 1 index arithmetic.
3. `NOTES.md`: scope, a coverage table with no row left `deferred`, a fork register, an answer table for the tax years answered, what `check.sh` prints, open questions.
4. `check.sh` (the skill's template), `encoding.json`, `SOURCE-LICENSE.md`.

## Rules that matter

- **Encode isomorphically.** One source provision, one recognisable place, with an `@ref` naming the section and the line of the source file.
- **The tax year is the vintage selector.** The encoding answers for the tax years the source states its figures for, and declines (`REFUSE`) for every other year rather than borrowing a figure from the text as amended.
- **Do not invent a number.** The consumer price index, any amount published by the Israel Tax Authority, and any figure that appears only in an editorial note, is an input with no default.
  The rounding Order under s 120B(d) is not encoded: a rounded amount is either supplied or refused.
- **Where the sources do not answer, `REFUSE "…"`**; never `FALSE`, `0` or a plausible default.
- **A failing assertion is a finding.** Never edit an expected value to match what the code computed.
- **Read the diagnostics, not the exit code**: run `check.sh` and report the numbers it prints.
- Money is new Israeli shekels (NIS), as a bare `NUMBER`; amounts are annual; rates are written as percent literals exactly as the source prints them.
- Semi-cleanroom (ruled 2026-10-06): nothing from the Axiom Foundation or any RuleSpec encoding may be read.

## Toolchain

`/Users/mengwong/.local/bin/l4` (it has no `--version`; NOTES.md section 0 identifies the build used), with `JL4_LIBRARY_PATH` unset.
`l4 check FILE` type-checks; `l4 run FILE` also evaluates every `#EVAL` and `#ASSERT`.
