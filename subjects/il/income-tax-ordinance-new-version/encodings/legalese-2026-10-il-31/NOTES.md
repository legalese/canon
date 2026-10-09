# IL-31 notes: earlier vintages of ITO s 66(c)(4)-(6), and s 121B(a1) for 2025

Version 0.1.0, 2026-10-08.
Row IL-31, run id `IL-31-20261008`, agent `enc-il-31`, one session (Claude Sonnet 5.5), no sub-agents, from `BRIEF.md`.
Status `draft`: no domain expert has read this against the sources.

## 0. The short answer

Read this first.

- **s 66(c)(4)-(6) before 2024: the three Acts do not let anyone answer any earlier tax year.**
  They are Acts of amendment ("in place of X put Y").
  They confirm that the text row IL-02 holds begins on 1 January 2024.
  They do not print the base text they amend, and the base text is deposited nowhere.
  So tax years 2023, 2021 and every earlier year are declined by name, with the missing source named.
  Tax year 2022 is declined too, except for one thing: the further credit point that Act SH 2972 adds for that year only (encoded as an addition, never as a total).
- **s 66(c)(4)-(6) from 2024:** the Acts' own words give the children's credit points by age, and they agree with row IL-02 in 132 of 132 comparisons (section 11, item O3).
  The mother's birth-year election of (4)(a1) is not in any deposited Act, so that module stops before it.
- **s 121B(a1) for 2025: answered.**
  Act SH 3342 s 3(a) commences the Act on 1 January 2025, and s 3(b) applies (a1) to income produced or received from that day.
  Tax year 2025 is a calendar year, so every item of it is caught.
  Section 121B is encoded for tax year 2025, with the (a) amount supplied, the residential-apartment threshold at the 5,385,285 the Act prints, and (a1) at 2%.
  Tax year 2024 and earlier are declined by name; tax year 2026 onward is row IL-03's.
- The same Act confirms two things row IL-03 had to assume: that the 5785 amendment of s 120B is Sefer HaChukim 3342 (amendment 276), and that its freeze begins with tax year 2025.

## 1. What is encoded and what is not

**Encoded, Part A (`il31-ito66-vintages.l4`, nouns in `il31-nouns.l4`).**
The vintage ladder for s 66(c)(4), (4A), (5) and (6): which text governs which tax year, and the first tax year of the text of Acts SH 3048 and SH 3184 (2024).
The credit points that text gives a child, by age in tax years, for each of the four claimants of those paragraphs, before any (4)(a1) election.
The further credit point Act SH 2972 gives in tax year 2022 (paragraphs (4)(d), (5A), and (6) as that Act reads it), as an addition to a base this row does not hold.
Named refusals for tax years 2023, 2022 (the base) and before 2022.

**Encoded, Part B (`il31-ito121b-2025.l4`).**
Section 121B as Act SH 3342 leaves it, for tax year 2025: (a), (a1), (b), (d) as an input convention, (e) with both definitions.
The commencement and application rule of the Act's s 3.
The residential-apartment threshold for 2025.

**Not encoded, and why.**

- s 66(a), (b), (c)(1)-(3), (d) before 2024.
  No deposited Act changes them, and none shows an earlier text of them.
  The amendment list of s 66 (source line 2454) ends `תשפ״ב־5, תשפ״ג־2, תשפ״ג־6, תשפ״ד־3`; of these the deposited Acts are the first, the third and the fourth.
  The second, a 5783 amendment, is not deposited.
- s 40 in any vintage.
  The row names s 66.
  The same three Acts amend s 40(b) in parallel with s 66(c), and Act SH 2972 adds s 40(c)(1) and (2) for 2022; see the coverage table.
- The work-grant provisions of the same Acts (the 2007 Work Grant Law), which are not the Ordinance.
- Section 121B before 2025, and section 121B from 2026 (row IL-03).
- The rounding Order under s 120B(d), the CBS index, and the Tax Authority's 2025 figure for the s 121B(a) amount: none is deposited, so the amount is an input.

## 2. Coverage table

Dispositions: `encoded`, `inert` (quoted, no effect on any answer), `read-only` (read to confirm something, nothing encoded), `out-of-scope` (with a reason).
No row is `deferred`.

### The Acts

| Act | provision | what it does | disposition | where |
| --- | --- | --- | --- | --- |
| SH 2972 (5782-2022) | s 1 opening | the Ordinance is read as follows for income produced from 1 January to 31 December 2022 | encoded | `Act SH 2972 reads the Ordinance for income produced in tax year` |
| SH 2972 | s 1(1) | adds s 40(c)(1), (2): a further point for a child under 13 who is not a toddler | out-of-scope: s 40 is not the row's section; the same words as s 66(c)(4)(d) and (5A) | — |
| SH 2972 | s 1(2)(a) | adds s 66(c)(4)(d): the further point to the woman | encoded | `Act SH 2972 — the further credit point of` |
| SH 2972 | s 1(2)(b) | adds s 66(c)(5A): the further point to the man | encoded | same |
| SH 2972 | s 1(2)(c) | s 66(c)(6) points the man who married a widow at (5) or (5A) | encoded (through the claimant) | same |
| SH 2972 | s 2 | the Work Grant Law | out-of-scope: not the Ordinance | — |
| SH 3048 (5783-2023) | s 1 | the Work Grant Law | out-of-scope: not the Ordinance | — |
| SH 3048 | s 2(1) | s 40(b)(1), (1a), (1b), (3) | out-of-scope: s 40 | — |
| SH 3048 | s 2(2)(a)(1) | appends to s 66(c)(4)(a) the 2½ and 2 point bands | encoded, as replaced in part by SH 3184 | `s 66(c)(4)(a) — the credit points for a child of` |
| SH 3048 | s 2(2)(a)(2) | deletes s 66(c)(4)(b) and (c) | inert: their text is not in any deposited source | — |
| SH 3048 | s 2(2)(b) | in (5): deletes "toddlers", adds (c), one point from age 6 | encoded | `s 66(c)(5) — the credit points for a child of` |
| SH 3048 | s 2(2)(c) | in (6): deletes "toddlers" | encoded (through the claimant) | `the credit points the paragraph gives` |
| SH 3048 | s 3(a), (d) | commences on 1 January 2024, on income produced from then; s 3(a) adds a proviso, that the 2024 Budget Law be adopted by then | encoded as the first tax year; the proviso is observation O1 | `the first tax year of the text … that Acts SH 3048 and SH 3184 leave` |
| SH 3048 | s 3(b), (c) | the Work Grant Law's commencement and application | out-of-scope | — |
| SH 3184 (5784-2024) | s 1(1) | s 40(b)(1), (1a) | out-of-scope: s 40 | — |
| SH 3184 | s 1(2)(a) | s 66(c)(4)(a): replaces the opening up to "five years" with the 2½, ½, 4½, 3½, 2½ bands | encoded | `s 66(c)(4)(a) — …` |
| SH 3184 | s 1(2)(b) | s 66(c)(5)(a) "1½" becomes "2½"; (5)(b) replaced | encoded | `s 66(c)(5) — …` |
| SH 3184 | s 2, s 4 | the Work Grant Law | out-of-scope | — |
| SH 3184 | s 3 | the s 40 and s 66 amendments commence on 1 January 2024 | encoded | same as SH 3048 s 3 |
| SH 3342 (5785-2024) | s 1(1) | adds s 120B(e): the 2025-2027 freeze, the 2028 restart | read-only: row IL-03's; read to confirm its identification and its text | section 11, O4 |
| SH 3342 | s 1(2)(א) | heading: "additional tax" | inert | — |
| SH 3342 | s 1(2)(ב) | deletes the defining parenthesis in (a) | inert: it changes no word of the charge | — |
| SH 3342 | s 1(2)(ג) | adds (a1) | encoded | `SH 3342 text — s 121B(a1) — the additional tax on` |
| SH 3342 | s 1(2)(ד) | (b) names (a) and (a1) | encoded | `SH 3342 text — s 121B(b) — …` |
| SH 3342 | s 1(2)(ה)(1)-(2) | (e): punctuation; the threshold 5,385,285; the base index of 15 January 2027 | encoded | the threshold and betterment rules |
| SH 3342 | s 1(2)(ה)(3) | (e): adds "הכנסה חייבת ממקור הוני" | encoded | `SH 3342 text — from a capital source` |
| SH 3342 | s 2 | amends the Real Estate Taxation Law s 9 | read-only: `s 9(c2)` is read to see that the adjustment s 121B(e) borrows is not made in 2025 to 2027 | section 11, O5 |
| SH 3342 | s 3(a), (b) | commences 1 January 2025; (a1) applies to income produced or received from then | encoded | `s 121B(a1) applies to income produced or received on` |

### The Ordinance, s 66(c)(4)-(6), and s 121B

| provision | source line | disposition | where |
| --- | --- | --- | --- |
| s 66(c)(4) intro, ½ point under s 36A | 2465 | out-of-scope: s 36A is row IL-01's; the ½ is not a child's point | — |
| s 66(c)(4)(a) | 2466 | encoded, from 2024 | `s 66(c)(4)(a) — …` |
| s 66(c)(4)(a1) | 2467 | out-of-scope: its enacting Act is not deposited; row IL-02 encodes it | — |
| s 66(c)(4)(b), (c) | 2468-2469 | inert: "(נמחקה)", text unknown | — |
| s 66(c)(4)(d) | 2470 | encoded, as the 2022 addition only ("(פקעה)" in the consolidation) | `Act SH 2972 — …` |
| s 66(c)(4A) | 2472 | encoded | the claimant |
| s 66(c)(5)(a)-(c) | 2474-2476 | encoded | `s 66(c)(5) — …` |
| s 66(c)(5A) | 2477 | encoded, as the 2022 addition only | `Act SH 2972 — …` |
| s 66(c)(6) | 2478 | encoded | the claimant |
| s 66(a), (b), (c)(1)-(3), (d) | 2455-2464, 2479-2487 | out-of-scope: earlier vintages not held, and no deposited Act alters them | — |
| s 121B(a) | 4456 | encoded, tax year 2025 | `SH 3342 text — s 121B(a) — …` |
| s 121B(a1) | 4457 | encoded | `SH 3342 text — s 121B(a1) — …` |
| s 121B(b) | 4458 | encoded | `SH 3342 text — s 121B(b) — …` |
| s 121B(c) | 4459 | inert: no other enactment is encoded in the row that it could displace | — |
| s 121B(d) | 4460 | an input convention: items are taken after any s 8(c) spreading | `ito-il03-nouns.l4` |
| s 121B(e) "הכנסה חייבת" | 4462 | encoded | the threshold, betterment and taxable-income rules |
| s 121B(e) "הכנסה חייבת ממקור הוני" | 4463-4465 | encoded | `SH 3342 text — from a capital source` |

## 3. Tax years answered

| provision | 2021 and earlier | 2022 | 2023 | 2024 onward | 2025 | 2026 onward |
| --- | --- | --- | --- | --- | --- | --- |
| s 66(c)(4)-(6) credit points for a child | declined: the amending Acts of those years are not deposited | declined: the base text is not deposited; **the 2022 addition is answered** | declined: the base text and the 5783 Act are not deposited | answered by the Acts' words, before (4)(a1); IL-02 holds (a1) | (same) | (same; a projection, IL-02 A2) |
| s 121B | declined: text not deposited | declined | declined | — | **answered** | row IL-03 |

Every refusal names the source it needs.
The refusal texts are in `il31-ito66-vintages.l4` and `il31-ito121b-2025.l4` and are asserted in full by `il31-tests.l4`.

## 4. Fork register

The policy of Meng's ruling SHRUG of 2026-10-08 applies to every row below: where the text is silent or two readings are arguable and give different answers to a question someone would ask, one named switch, the default a refusal by name, the other readings kept by name and tested; where the readings agree the answer is given.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| A1 | SH 2972 s 1(2)(a), (b): "אשר בשנת 2022 טרם מלאו לו שלוש עשרה שנים" | On which day of 2022 is a child's age tested, for a child who completes thirteen years during 2022 (born in 2009)? | (i) counted in tax years (s 40(b)(3) counts a child's age by the tax year of the birthday): 2022 minus 2009 is 13, not less than 13, so out; (ii) tested at the start of 2022: the child has not completed thirteen years, so in | **ruled by Meng 2026-10-08 (SHRUG)**: one switch, `section 66(c)(4)(d), (5A) — the reading this row takes for the age limit of thirteen years in 2022`, default `declined where the reading changes the answer`; (i) and (ii) kept by name and tested. The default declines for a child born in 2009 only, and answers for every other birth year, where the two agree (born 2010 or later: in; born 2008 or earlier: out). Year-only input cannot tell a child born on 1 January 2009 from the rest of 2009, so (ii) takes the whole of 2009 as in. |
| A2 | SH 2972, "פעוט כהגדרתו בסעיף 40(ב)(3)" | Is the child a toddler? | the definition was in s 40(b)(3) and SH 3048 s 2(1)(ד) deleted it; the consolidation prints `”פעוט“ – (נמחקה)`; its words are in no deposited source | **needs a source**: the caller supplies the flag, `a toddler under the definition of section 40(b)(3) as it stood in 2022`. A toddler gets nothing from the further point, whatever the age limit. Not a fork of two readings; a missing input. |
| A3 | SH 2972 s 1(2)(a): the point is "נוספת על נקודות הזיכוי לפי פסקת משנה (ב)" (additional to the points under sub-paragraph (b)) | Is the further point conditional on the child's entitlement to the (4)(b) points? | (i) no: the phrase says what the point is added to; (ii) yes | **assumed, not ruled: (i)**. Sub-paragraph (b) is a deleted text that no deposited source shows, so the question cannot be posed on the sources, and the readings can differ only on a case (a non-toddler under 13 who has no (b) points) that no source lets anyone identify. Revert: make the function take a flag `the child has points under the base paragraph (4)(b)`. |
| A4 | SH 3048 s 3(a): the Act commences "provided that by then the 2024 Budget Law has been adopted" | Does the proviso gate tax year 2024? | the proviso's fact is not deposited | **observation O1**, not a fork of the answers: SH 3184 s 3 independently commences ss 40 and 66 "as worded in s 1 of this Law" on 1 January 2024 with no condition, so tax year 2024 is the first year of the text either way; the proviso is recorded, not read. |
| A5 | a tax year as a special assessment period | s 1 "שנת מס" has a second limb | — | **not modelled**: the tax year is a calendar year, as in rows IL-02 and IL-03 (IL-03 F12). |
| B1 | SH 3342 s 3(b): "הכנסה שהופקה או התקבלה ביום התחילה ואילך" (produced or received on or after 1 January 2025) | Does (a1) charge income produced in 2024 and received in 2025, and to which tax year does that income belong? | the text does not allocate it | **declined for tax year 2024 and earlier by name**; irrelevant to 2025, because every item of tax year 2025 was produced or received on or after 1 January 2025. Not a switch: no input of this row reaches it. |
| B2 | s 121B(e) with RETL s 9(c2) | Is the 5,385,285 threshold adjusted in 2025? | (i) no: s 9(c2) is made "in every tax year, except in the tax years 2025 to 2027", from a base index of 15 January 2027; (ii) yes | **(i)**, on the deposited RETL text (line 239 and line 247 of the consolidation) and Act SH 3342 s 2(1)(ג). Not a fork: the text decides. |
| B3 | s 121B(a) amount | the amount in 2025 | s 120B(e)(1): the 1 January 2024 figure after rounding | **an input**, as in row IL-03; the rounding Order is not deposited. |
| B4 | s 121B(e), the exemption condition | Does "and the sale is not exempt from tax under any law" govern only the residential limb? | (i) yes, it sits inside the "ואולם לגבי מכירת זכות … בדירת מגורים" clause; (ii) all betterment | **(i)**, as IL-03 F9. Not re-opened here: it is IL-03's reading of the same words, and the Act of 2025 does not touch them. |
| B5 | s 121B(e), the threshold's year | Which tax year's threshold applies to a sale? | (i) the case's tax year; (ii) the sale date | **(i)**, as IL-03 F10; moot in 2025, which is the only year this module answers. |
| B6 | s 121B(a1) "ממקורות הוניים" against the definition "ממקור הוני" | Plural against singular | (i) the defined term; (ii) an undefined phrase | **(i)**, as IL-03 F11, and here more firmly: the same Act, s 1(2)(ג) and (ה)(3), adds (a1) and the definition together, so the definition has no other use. Classed as not arguable, so no switch. |
| B7 | s 121B(a), (a1), (e): "עלתה על" and "עולה על" (exceeded, exceeds) | At exactly the threshold | strict | **strict**, as IL-03 F14; tested at both sides of both thresholds. |
| B8 | s 121B(e) | Is real-estate betterment capital-source income? | — | **yes**, as IL-03 F15: it is neither s 2(1)/(2) income nor personal-exertion income, the only two exclusions. |

## 5. Answer table

All values are from the Hebrew text, worked by hand; the arithmetic is beside each assertion in `il31-tests.l4`.

### s 66(c)(4)-(6) from tax year 2024, credit points by the child's age in tax years (year minus year of birth), before the (4)(a1) election

| age | the woman, (4)(a), and the woman who married a widower, (4A) | the man, (5), and the man who married a widow, (6) |
| --- | --- | --- |
| 0 (year of birth) | 2½ | 2½ |
| 1 and 2 | 4½ | 4½ |
| 3 | 3½ | 3½ |
| 4 and 5 | 2½ | 2½ |
| 6 to 17 | 2 | 1 |
| 18 (year of maturity) | ½ | none |
| 19 and over, or not yet born | none | none |

Sources: SH 3184 s 1(2)(a) and (b); SH 3048 s 2(2)(a)(1) and (b)(3); the consolidation, lines 2466 and 2474-2476.

### Tax year 2022: the further credit point of Act SH 2972, in addition to a base this row does not hold

| the child | the age limit read as (i), counted in tax years | (ii), tested at the start of 2022 | default |
| --- | --- | --- | --- |
| a toddler, any year of birth | 0 | 0 | 0 |
| not a toddler, born 2010 to 2022 | 1 | 1 | 1 |
| not a toddler, born 2009 | 0 | 1 | declined |
| not a toddler, born 2008 or earlier | 0 | 0 | 0 |
| any child, any tax year other than 2022 | 0 | 0 | 0 |

The same for the woman, the woman who married a widower, the man and the man who married a widow.

### s 121B for tax year 2025, with the (a) amount A supplied (scenario value 721,560, not law)

| facts | (a) 3% above A | (a1) 2% of capital-source income above A | total |
| --- | --- | --- | --- |
| salary 1,000,000 | 8,353.2 | 0 | 8,353.2 |
| dividend 1,000,000 | 8,353.2 | 5,568.8 | 13,922 |
| salary 800,000, dividend 300,000 | 11,353.2 | 0 | 11,353.2 |
| salary 100,000, dividend 800,000 | 5,353.2 | 1,568.8 | 6,922 |
| dividend 900,000 | 5,353.2 | 3,568.8 | 8,922 |
| capital gain 1,000,000 of which inflationary 100,000 | 5,353.2 | 3,568.8 | 8,922 |
| residential sale, value 5,385,286, betterment 2,000,000 less 300,000 | 29,353.2 | 19,568.8 | 48,922 |
| the same, value 5,385,285 | 0 | 0 | 0 |
| any income exactly A | 0 | 0 | 0 |
| any salary A + 1 | 0.03 | 0 | 0.03 |
| any dividend A + 1 | 0.03 | 0.02 | 0.05 |

## 6. What `check.sh` prints

Run 2026-10-08T23:38:36Z to 2026-10-08T23:38:40Z, with `l4` on PATH: `/Users/mengwong/.local/bin/l4`, which resolves to the cabal-store build `jl4-0.1-6df1397b`.
sha256 before the run `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`, after the run `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`: the same.
`JL4_LIBRARY_PATH` unset.

```
module                                    errors satisfied  failed  refused  expected
il31-ito121b-2025.l4                           0         0       0        0         0
il31-ito66-vintages.l4                         0         0       0        0         0
il31-nouns.l4                                  0         0       0        0         0
il31-tests.l4                                  0       114       0        0         0
ito-il03-nouns.l4                              0         0       0        0         0
TOTAL (5 modules)                              0       114       0        0
```

Exit 0.
No module is expected to fail or refuse; `expected_red` in `encoding.json` is empty.
Every assertion passed on its first run; no expected value was edited to match what the code computed.

### Controls

- **A control copy with four expected values made wrong** (a credit point, a tax amount, a refusal message, a switch default) reported 4 failures and 108 satisfied (of the 112 assertions then in the file), in a scratch directory, so the assertions can fail.
- **Differential against row IL-03.**
  Twenty-two cases (income lists, sales of real estate, and both, several at the thresholds), run through IL-03's own `the additional tax under section 121B for` at tax year 2026 and through this row's rule at tax year 2025, with the same facts and the same amount, gave identical results in all 22.
  (IL-03 refuses 2025; the comparison moves the year only.)
- **Differential against row IL-02.**
  `s 66(c)(4)-(6) — the credit points of …` against IL-02's `s 66(c)(4)-(6) — the credit points of the … in … for …` for birth years from 21 years before to the tax year itself, for tax years 2024, 2025 and 2026, both columns: 132 assertions, all satisfied.
  This is the Acts' words against the consolidation's, which is the strongest check the sources allow that the 2024 text is what the Acts leave.
- `tools/actcheck.py` checks every `-- act:` Hebrew run against the PDFs' text layers: 61 runs, 2 not found, both because the text layer is corrupt at that place (section 7).
  `tools/hebcheck.py` checks every other Hebrew run against the consolidation.

## 7. Sources, and how the Acts were read

| file | Sefer HaChukim | sha256 (matches `SOURCES.json` and `shasum` at 2026-10-08) |
| --- | --- | --- |
| `24_lsr_624898.pdf` | 2972 | `5ccb5e726e03f543cb3af1a442326d29cb2c14bcbc7f669e6865cf30df0b00da` |
| `25_lsr_2656507.pdf` | 3048 | `0438740db2a93edbe174e37ee8b83d142ff3092bd73228ed0eea9ba52b6d1f79` |
| `25_lsr_4239836.pdf` | 3184 | `6ffd3f51b2b75f89cfb90b68b1c71b1882eb3eaea605bf01b71b94972e9ac969` |
| `25_lsr_5396578.pdf` | 3342 | `1f33320a746f4d2b191d94e963224fc4a7efaedbe569ed22f793f44a09f25e70` |
| the consolidation | — | `b87f2cf437ccfed35c3164681f4fc7ee015a111633454622751930c8894b81b6` |
| the Real Estate Taxation Law consolidation (read for s 9(c2) only) | — | `aa4217b3b917a48356d8069b9e9510694b456506ec77c9b4527a99c6c16dd1ca` |

**How the Acts were read.**
Each PDF was rendered to page images (`pdftoppm`, 150 to 260 dpi) and every figure, date, paragraph letter and Hebrew quotation was read from the image.
The text layers were then used as a cross-check on the Hebrew words only: in SH 2972, SH 3048 pages 1-2, SH 3184 and SH 3342 they are legible Hebrew with scrambled digits and parentheses; SH 3048 pages 3 and 4 are a doubled, interleaved layer and are readable from the image alone.
Two `-- act:` runs are not found in the text layers and are image-read: SH 3048 s 3(d) (the layer is the interleaved one) and the clause of SH 2972 s 1 "יקראו את פקודת מס הכנסה" (a footnote mark falls inside it in the layer).
Where the image and the layer disagree on a digit, the image governs; none disagreed on a figure that matters.

The figures that matter, as read: 13 years (SH 2972, text layer and image agree); 2½, ½, 4½, 3½, 2½, 2 (SH 3184 s 1(2)(a), SH 3048 s 2(2)(a)(1)); 1½ replaced by 2½ (SH 3184 s 1(2)(b)(1)); 1 January 2024 and 20 Tevet 5784 (SH 3184 s 3, SH 3048 s 3(a)); 1 January 2025 and 1 Tevet 5785 (SH 3342 s 3(a)); 2% and 5,385,285 (SH 3342 s 1(2)); "2025 to 2027" and 15 January 2027 (SH 3342 s 1(1), s 2).

## 8. Vendored files

| file | from | sha256 | note |
| --- | --- | --- | --- |
| `ito-il03-nouns.l4` | `../legalese-2026-10-il-03/ito-il03-nouns.l4` | `0c8b52c31d9026867ecd8818cb345f7c64391a55a1acfb045fcc3138095c5f20` | byte for byte, at the IL-03 tree of 2026-10-08; never edited here. If IL-03 changes its nouns, this copy goes stale and `cmp` will say so. |

The rules of Part B were written from the Hebrew, not copied from `ito-121b-additional-tax.l4` (sha256 `6d54cd5113e49566…`), and then compared with it (section 6, Controls).

## 9. What IL-02, IL-03 and the capstone would change to call this row

This is not this row's job; it is the exact change.

**Row IL-03 (preferred; then Part B of this row is evidence, not a dependency).**
In `ito-121b-additional-tax.l4` (sha256 `6d54cd5113e49566…`), the boundary `2026` becomes `2025` at three places, and the residential helper's test follows:

- lines 77-80: `the text fixes the residential-apartment sale value for tax year` — `LESS THAN 2026` becomes `LESS THAN 2025`, and `ELSE the tax year EQUALS 2026` becomes `ELSE the tax year AT MOST 2027` if IL-03 adopts observation O5, otherwise `AT MOST 2026`;
- lines 99-101: `the residential-apartment sale value in section 121B(e) for tax year` — `LESS THAN 2026` becomes `LESS THAN 2025`;
- lines 229-231: `the additional tax under section 121B for` — `LESS THAN 2026` becomes `LESS THAN 2025`;
- the refusal text at lines 91-92 and its three call sites, the header comment at lines 18-31, and IL-03's NOTES.md A1, S13 and question 4, which say the commencement is unknown.

Its independent tester's two refused lines (`tests-independent.l4` 371 and 384) would then be answered, and equal 8,922 and 2,353.2, which are the values this row's tests derive by hand.

**The capstone (IL-07)** asks `the additional tax under section 121B for` through `il07-adapter-il03.l4` lines 73-86 and `il07-pipeline.l4` lines 322-330, with the amount from `il07-published-figures.l4`, which holds 2026 only.
For tax year 2025 it needs two things, neither of which this row can do:

1. IL-03's change above, or, without it, a branch in the adapter on the tax year of the month: tax year 2025 calls `the additional tax under section 121B in tax year 2025 for` (this row), every later year calls IL-03's rule.
   One module can import both: this row's helpers carry the prefix `SH 3342 text — ` so that nothing collides with IL-03's (tested: both imported, each answered, no definition clash).
   The capstone vendors its own copy of IL-03's modules, so it would also vendor this row's `il31-ito121b-2025.l4`.
2. An amount for 2025: see section 10.

**Row IL-02.**
`ito66-tax-years.l4` needs no code change, because no earlier year can be answered.
Its NOTES.md assumption A1 (lines 421-441), which rests on two Tax Authority circulars because "the amending Acts could not be fetched", is now confirmed by the Acts themselves: SH 3048 s 3(a) and (d), and SH 3184 s 3 (its "retroactive from 1.1.2024" is the Act's own commencement).
Its refusal sentence could add what it needs ("the base text before SH 3048, and the 5783 Act tagged תשפ״ג־2"); that is optional.

## 10. Inputs this row takes that the capstone does not supply today

For IL-55 to follow.

Part A:

- `A claimant under section 66(c)(4)-(6)`: which of the four people the taxpayer is; the capstone has the woman and the man of a couple (IL-02's types) but not the step-parent classification as a value.
- `A child in section 66(c)`: the tax year of birth; IL-02's child record already carries it.
- `a toddler under the definition of section 40(b)(3) as it stood in 2022`: not held by any row; the definition is not deposited.
- the age-limit reading, `A reading of Act SH 2972 on the age limit of thirteen years in 2022`: the default declines for a child born in 2009 only.

Part B:

- `An individual in a tax year` (IL-03's record: the tax year, a date of birth, the items of income with their classifications, the sales of rights in real estate with betterment, inflationary amounts, sale value and exemption): the capstone builds it for 2026 in `il07-adapter-il03.l4` and would build it for 2025.
- **The s 121B(a) amount for 2025.**
  The capstone carries 721,560 for 2026 only, from the Tax Authority's 2026 booklet.
  For 2025 the amount is the 1 January 2024 figure after rounding (s 120B(e)(1), confirmed by SH 3342 s 1(1)); the consolidation's editorial note says 721,560 for 2024-2027, which is an aid; no 2025 publication of the Tax Authority is deposited.
  The capstone can route it through IL-03's s 120B for 2025 (which answers 2025) from the 1 January 2024 figure, as it does for the value of a credit point.

## 11. Findings and observations

**O1. SH 3048 s 3(a) is conditional.**
The Act commences on 1 January 2024 "and provided that by that date the Budget Law for 2024 has been adopted" (ובלבד שעד אותו מועד התקבל חוק התקציב לשנת 2024).
Whether the Budget Law was adopted by then is a fact no deposited source states, and this row does not read it.
It does not decide tax year 2024: SH 3184 s 3, enacted on 20 March 2024, commences ss 40 and 66 "as worded in s 1 of this Law" on 1 January 2024, unconditionally, and its s 1(2) amends text that SH 3048 supplied.
The consolidation carries both amendments in s 66's list.
The observation matters only to someone who asks what the law was between 7 June 2023 and 20 March 2024.

**O2. The enacting Act of s 66(c)(4)(a1) is not deposited, and may be needed for 2023.**
The mother's election (the point moved from the year of birth to the year after) is in neither SH 3048 nor SH 3184.
The section's amendment list has a 5783 entry `תשפ״ג־2` between the 2022 Act and SH 3048; row IL-02's notes name a Knesset file `25_lsr_2301411.pdf` among those it could not fetch.
Section 40's list has the same entry, and s 40(b)(1a1) is the same election.
If that Act commenced for 2023, the 2023 text would hold a feature the 2024 text also holds.
Needs a source.

**O3. The Acts alone reproduce IL-02's table.**
132 of 132 comparisons agree (section 6, Controls).
The table is the product of two Acts that each patch the other's text, so this agreement checks both readings at once.

**O4. SH 3342 confirms IL-03's identification and years for s 120B.**
IL-03's header says it identifies the 5785 amendment of s 120B from the list's order and title and "the amending Law itself was not read".
SH 3342 s 1(1) inserts s 120B(e): "ב־1 בינואר של שנות המס 2025 עד 2027 לא יתואמו הסכומים לפי הוראות סעיפים קטנים (א) ו־(ב), והסכומים באותן שנות מס יהיו כפי שהיו ביום כ׳ בטבת התשפ״ד (1 בינואר 2024) לאחר עיגולם לפי סעיף קטן (ד)", and (e)(2) for 1 January 2028 "טרם עיגולם".
That is the consolidation's text at source lines 4344-4345.
The page header prints `פקודת מס הכנסה – מס׳ 276 והוראת שעה`, Sefer HaChukim 3342, p. 150.
IL-03's assumption A1 about s 120B and fork F13 (2027 included) stand.

**O5. IL-03 declines the residential threshold from 2027; the sources may decide it.**
Section 121B(e) says the 5,385,285 "יתואם בהתאם להוראות סעיף 9(ג2) לחוק מיסוי מקרקעין".
That subsection, in the deposited Real Estate Taxation Law (line 239), adjusts the amounts "בכל שנת מס, למעט בשנות המס 2025 עד 2027", and SH 3342 s 2(1)(ג)(1) is the Act that wrote those words.
Read so, no adjustment is made in tax year 2027 either, and the threshold is 5,385,285 for 2025, 2026 and 2027.
IL-03 declines 2027 ("from 2027 it moves under s 9(c2) … which is not encoded").
This row answers only 2025 and does not decide it; the observation is recorded for IL-03's owner.

**O6. The consolidation doubles a phrase.**
Line 4462 reads "המדד שפורסם ביום המדד שפורסם ביום ז׳ בשבט התשפ״ז (15 בינואר 2027)".
SH 3342 s 1(2)(ה)(2) replaces the quoted words "המדד שפורסם ביום ד׳ בשבט התשע״ג (15 בינואר 2013)" by "המדד שפורסם ביום ז׳ בשבט התשפ״ז (15 בינואר 2027)", which gives one occurrence.
It is an editorial slip of the consolidation and changes no figure.

**O7. SH 2972 s 1(1) and s 66(c)(4)(d), (5A) are the same rule twice.**
For 2022 the Act adds one point under s 40(c) (a parent in a single-parent family, and a parent of a child "אשר אילו היה פעוט") and one under s 66(c) (a separate calculation).
This row encodes the s 66 side only.

**O8. The base text of the children's credit points needs a source.**
For every year before 2024 the row needs the text of s 66(c)(4)-(6) and s 40(b)(1), (1a), (3) as they stood, including the definition of "toddler".
The Tax Authority's circulars of January and March 2024 print the old figures, but row IL-02 holds them only by link and hash, they are an aid, and this row did not fetch them.

## 12. Open questions for a domain expert

1. Which day of 2022 tests the age limit of thirteen years (fork A1)?
   Does a child born in 2009 get the further point?
2. Is the further point of s 66(c)(4)(d) conditional on the child's entitlement under (4)(b) (fork A3)?
3. What was the definition of "toddler" (פעוט) in s 40(b)(3) in 2022?
4. Did the 5783 Act tagged `תשפ״ג־2` commence the mother's election for tax year 2023 (observation O2)?
5. Was the 2024 Budget Law adopted by 1 January 2024, so that SH 3048 s 3(a) was satisfied (O1)?
6. Does s 121B(e) escape adjustment in 2027 by s 9(c2) of the Real Estate Taxation Law (O5)?
7. Which tax year does income produced in 2024 and received in 2025 belong to, for (a1) (fork B1)?

## 13. Semi-cleanroom

Ruled 2026-10-06: nothing from the Axiom Foundation or any RuleSpec encoding may be read.
This row read none.
It read rows IL-02 and IL-03 (their NOTES.md, modules and, for IL-03, the independent tester's `tests-independent.l4`), the capstone's modules and the lead's brief; it did not read any "Comparison with Axiom" section.
One line of a grep over IL-03's NOTES.md (line 717 of that file) came back with an Axiom comparison cell in it; it was not used, and no figure in this row comes from it.
The expected values of this row were worked from the Hebrew before the assertions were run.
Two values coincide with the IL-03 tester's expectations (8,922 at line 371 and 2,353.2 at line 384 of its `tests-independent.l4`).
Both were first worked here before that file was opened (the capital gain of 1,000,000 with 100,000 inflationary, and the salary of 500,000 with a sale of other land); the dividend of 900,000 and the salary of 600,000 with a residential sale were added to the tests after reading those lines, their values worked by hand again from the text, with the arithmetic beside them.
