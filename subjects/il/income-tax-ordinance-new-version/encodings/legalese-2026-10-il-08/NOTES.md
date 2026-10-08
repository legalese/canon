# NOTES — il/income-tax-ordinance-new-version, encoding row `legalese-2026-10-il-08`

The Income Tax Ordinance half of row IL-08, the extension of the Israel tier: ss 1 ("Israeli resident" for an individual), 2, 35, 37, 38, 39, 40, 45A, 47, 64B, 65 and 121A, taken in the order row IL-07's `GAPS.md` needs them.
One agent, one session, no sub-agents (run `IL-08-20261007`, encoder `enc-il-08`, 2026-10-07), from the brief in `BRIEF.md`.
Status: **draft**.
No domain expert has read it; HG1 has not been sought; no independent test pass has been run.

The National Insurance Law half (Schedule A1 Part D, ss 72 and 335, and the dispositions of NII ss 65 and 67A) is the companion row, `../../../national-insurance-law-consolidated-version-5755-1995/encodings/legalese-2026-10-il-08/`.

## 0. What `check.sh` prints

Run from 2026-10-07T00:21:52Z to 00:22:26Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset.
The binary is `~/.local/bin/l4` → `~/.cabal/bin/l4` → cabal store `jl4-0.1-ff13a0ea`, sha256 `f65015688970231681a024ceb9ff3a58abba1f5280837cc955c2bba56dbfa8bc`.
That is **not** the build rows IL-01 to IL-07 recorded (`jl4-0.1-0ee0100b`, sha256 `64bbcb15…e118`); the link `~/.cabal/bin/l4` carries a modification time of 2026-10-06T22:41Z, before this row's first run.
No module changed during the run (sha256 of every module taken before and after).

```
module                                    errors satisfied  failed  refused  expected
ito-il08-nouns.l4                              0         0       0        0         0
ito-il08-published-figures.l4                  0         0       0        0         0
ito-il08-tax-years.l4                          0         0       0        0         0
ito-il08-tests-s1-s2.l4                        0        19       0        0         0
ito-il08-tests-s35.l4                          0        31       0        0         0
ito-il08-tests-s37-s40.l4                      0        52       0        0         0
ito-il08-tests-s45a-s47.l4                     0        65       0        0         0
ito-il08-tests-s47-deduction.l4                0        12       0        0         0
ito-il08-tests-s64b-s65.l4                     0        21       0        0         0
ito-s1-israeli-resident.l4                     0         0       0        0         0
ito-s2-sources-of-income.l4                    0         0       0        0         0
ito-s35-new-immigrant.l4                       0         0       0        0         0
ito-s37-s38-s39-spouse-credits.l4              0         0       0        0         0
ito-s40-children-credit-points.l4              0         0       0        0         0
ito-s45a-insurance-and-pension-credit.l4       0         0       0        0         0
ito-s47-deduction.l4                           0         0       0        0         0
ito-s47a-definitions.l4                        0         0       0        0         0
ito-s64b-s65-registered-spouse.l4              0         0       0        0         0
TOTAL (18 modules)                             0       200       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0.
200 assertions, all satisfied; 23 of them are `#ASSERT REFUSED … BECAUSE "…"`, each pinning a refusal's exact words.
No assertion is expected to fail, so `expected_failed` is 0 everywhere and there is no expected-red module: no test found the source inconsistent with itself.
The rule modules carry no assertions.
Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies.

That the harness can fail was shown on a scratch copy of the companion row's modules (same `check.sh`): one expected value altered, one `#ASSERT REFUSED` pointed at an expression that answers, and one plain `#ASSERT` on an expression that refuses gave `2 failed, 1 refused`, exit 1.

Every assertion was satisfied on the first run that evaluated it.
Before that, some test modules failed to **compile**, never to evaluate: helper names whose mixfix segments clashed with their own parameters, one-argument mixfix names ending in a keyword, and `GIVEN` lists in a different order from the definition's parameters.
Each was fixed by renaming or reordering; no expected value changed.
That all passed first time shows the rules do what their author worked by hand from the text; it does not show the readings are right, which an independent test pass would test.

Mechanical checks, run on 2026-10-07 over every module: `python3 -I tools/srcquote.py SOURCE *.l4` regenerates every `-- src:N |` line from line N of the source; `python3 -I tools/hebcheck.py SOURCE *.l4` finds every other run of Hebrew verbatim in the source (exit 0).
The `ext:` quotations were checked by a script (kept in the session scratchpad) against the text `pdftotext -layout` extracts from the fetched PDFs: 34 pieces from `[booklet-2026]` and 3 from `[a262]`, all found.

## 1. What is encoded, and what is not

**Encoded**, each in its own module:

| module | lines | holds |
| --- | ---: | --- |
| `ito-il08-nouns.l4` | 378 | the records every rule reads; `DECLARE` only |
| `ito-il08-tax-years.l4` | 59 | the period gate: tax years from 2024 (assumption A1) |
| `ito-il08-published-figures.l4` | 90 | the Tax Authority's 2024-2026 booklet figures for ss 45A and 47; not law |
| `ito-s47a-definitions.l4` | 186 | s 47(a)(1)-(8): qualifying income, income for a self-employed member, insured income, additional income, beneficiary member |
| `ito-s45a-insurance-and-pension-credit.l4` | 408 | s 45A(a)-(f), with s 47(c) and s 48A |
| `ito-s47-deduction.l4` | 179 | s 47(b), (b1), (b2), (c), (d) |
| `ito-s40-children-credit-points.l4` | 315 | s 40(b)(1), (1A), (1A1), (1B), (2), (3); s 40(a) and (c) as comments; s 48A |
| `ito-s37-s38-s39-spouse-credits.l4` | 274 | ss 37, 38, 39, with ss 48 and 48A |
| `ito-s35-new-immigrant.l4` | 230 | s 35(a)-(e), both texts of (a)(1) (Amendment 262), s 48A |
| `ito-s1-israeli-resident.l4` | 99 | s 1 "תושב ישראל" (a) for an individual |
| `ito-s2-sources-of-income.l4` | 51 | s 2's territorial charge and sources; s 1 "הכנסת עבודה" |
| `ito-s64b-s65-registered-spouse.l4` | 140 | s 64B(a)-(d); s 65 |
| six `ito-il08-tests-*.l4` | 994 | 200 assertions |

**Not encoded, and why** (section 2 gives each provision its disposition):
the National Health Insurance Law and s 164 with the Income Tax (Deduction from Salary and Wages) Regulations 5753-1993, which need their own source deposits (ruled out of this row);
the instruments the text names but the bundle does not hold (the order under s 48, the Regulations under ss 1(a)(4), 47(d) and 48A, the rules under s 35(e), the Retirement Age Law), each reached and declined by name, or an input;
the credit sections GAPS item 8 lists that the ruled scope does not (ss 39A, 39B, 40A-40D, 44, 45, 46).

**Figures.** Every amount the sections print that s 120B adjusts (1,632; 84,000; 118,800) and the average wage are inputs (`The amounts of sections 45A and 47 in force in the tax year`), with no default.
`ito-il08-published-figures.l4` carries what the Tax Authority published for 2024-2026 and derives the yearly figures as twelve times its monthly ones, an assumption named in every rule that does it (A3).

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt`.
"GAPS" is the item of row IL-07's `GAPS.md` the provision discharges, wholly or in part.
**Totals: 51 encoded, 8 inert, 21 out-of-scope, 0 deferred** (80 rows, counted by script over the four tables below; "encoded" includes a status encoded as an input, and "out-of-scope" includes the provisions reached and refused).

### In the ruled scope: the row's own list

| provision | lines | gist | disposition | where | GAPS |
| --- | --- | --- | --- | --- | --- |
| s 45A(a) chapeau, (a)(1) | 1715-1716 | 25% of life-insurance premiums, if he is resident | encoded | `s 45A(a)(1) — the life-insurance sums that may be credited, for`; fork F4 | 1 |
| s 45A(a)(2) | 1717 | (deleted) | inert | comment | — |
| s 45A(b) | 1718 | 35% of sums to a pension fund, to keep a pension right, for survivors' insurance | encoded | `s 45A(b) — …` (three rules) | 1 |
| s 45A(b1) | 1719 | a beneficiary member's child of 18 or more | encoded | `s 45A(b1) — …`; fork F9 | 1 |
| s 45A(c) | 1720-1724 | definitions; three borrowed from s 47 | encoded (as the classification of the sums, and by s 47(a)) | nouns; `ito-s47a-definitions.l4` | 1 |
| s 45A(d) chapeau, (1), (2)(a) | 1725-1728 | not a beneficiary member: the higher of 1,632 and the lower of the sums and a percentage | encoded | `s 45A(d)(2) — …`, `s 45A(d)-(e) — the limit that governs, for` | 1 |
| s 45A(d)(2)(b)(1)-(2) | 1729-1730 | 5% or 7% of qualifying income; the provisos | encoded | `s 45A(d)(2)(b) — …`; forks F5, F7 | 1 |
| s 45A(e) chapeau, (1), (2)(a) | 1731-1734 | a beneficiary member: the same shape | encoded | `s 45A(e)(2) — …` | 1 |
| s 45A(e)(2)(b)(1)-(2)(a)-(b) | 1735-1738 | 5% of taxable income; 7% of insured qualifying income plus 5% of income not insured; the provisos | encoded | `s 45A(e)(2)(b) — …`; forks F5, F6 | 1 |
| s 45A, the credit | 1715-1738 | the sums at each rate within the limits | encoded, declining where the limits cut sums of both rates | `s 45A(a)-(e) — the credit …`; fork F1 | 1 |
| s 45A(f) | 1739 | 35% of a self-employed member's deposits, to 0.5% of business income | encoded | `s 45A(f) — …` | 1 |
| s 40(a) | 1632 | allowance points under the National Insurance Law, paid by the Institute | inert | comment; read by ss 38, 39 as an input; fork F19 | 2 |
| s 40(b)(1) | 1633 | a parent in a single-parent family: the table, per child with him | encoded | `s 40(b)(1) — …` | 2 |
| s 40(b)(1A) | 1634-1637 | the father of a child in a single-parent family; the proviso moving the points to the mother | encoded | `s 40(b)(1A) — …`; forks F14, F15 | 2 |
| s 40(b)(1A1) | 1638 | the mother's election | encoded | `s 40(b)(1A1) — …`; fork F13 | 2 |
| s 40(b)(1B) | 1639 | a child of one parent: one more point, and the (1A) table | encoded | `s 40(b)(1B) — …`; forks F16, F17 | 2 |
| s 40(b)(2) | 1640 | parents living apart | encoded | `s 40(b)(2) — …`; forks F16, F18 | 2 |
| s 40(b)(3) | 1641-1645 | "child of one parent", year of birth, year of majority | encoded ("פעוט" deleted: inert) | `s 40(b)(3) — …` | 2 |
| s 40(c) | 1646 | (expired) | inert | comment | — |
| s 37 | 1600 | a beneficiary individual who maintained the spouse: one point | encoded | `ito-s37-s38-s39-spouse-credits.l4`; fork F20 | 7 |
| s 38(a) | 1603 | a registered spouse whose income includes a working spouse's | encoded | `s 38(a) — …`; fork F21 | 7 |
| s 38(b) | 1604 | spouse's income up to five times the points: left out | encoded | `s 38(b) — …`; fork F22 | 7 |
| s 39 | 1607 | a spouse who helped in the business; the election | encoded | `s 39 — …`; fork F23 | 7 |
| s 35(a)(1), old text | 1574 | 1/4 a month for 18 months (immigrated before 2022) | encoded | `s 35(a), before Amendment 262 — …` | 8 |
| s 35(a)(1), (1A), (2), (3) | 1575-1578 | 1/12, 1/4, 1/6, 1/12 a month over 54 months | encoded | `s 35(a), from Amendment 262 — …` | 8 |
| Amendment 262 s 2 | (ext) | the 54-month text for one who first became an immigrant from 1 January 2022 | encoded | `s 35 — the text that governs` | 8 |
| s 35(b) | 1579 | the consolidated calculation with an immigrant spouse | encoded | `s 35(b) — …` | 8 |
| s 35(c) | 1580 | the months resided, the first time only, an absence left out | encoded | `s 35 — the place in the period …`; forks F24, F25 | 8 |
| s 35(d) "עולה" | 1582 | the four grounds and the exclusion | encoded | `s 35(d) — an immigrant:` | 8 |
| s 35(d) "תושב חוזר" | 1584 | returned 16 May 2010 to 30 September 2012 after six years | encoded | `s 35(d) — a returning resident …` | 8 |
| s 35(d), the Vietnamese refugees note | 1583 | regulations of 5741-1980 | inert (a class the Minister determined is an input) | comment | — |
| s 35(e) | 1585-1588 | the Minister's rules (of 5738-1977) | out-of-scope, refused | `the rules under section 35(e) are not encoded in this model` | 8 |
| s 1 "תושב ישראל" (a)(1) | 144-150 | centre of life on the whole of the ties | encoded as an input finding | nouns; `s 1 "Israeli resident" (a) — …` | 13 |
| s 1 "תושב ישראל" (a)(2) | 151-154 | the 183-day and 30/425-day presumptions; "יום" | encoded | `s 1 "Israeli resident" (a)(2) — …` | 13 |
| s 1 "תושב ישראל" (a)(3) | 155 | rebuttable by either | encoded | the presumption decides only unrebutted and without a finding; fork F26 | 13 |
| s 1 "תושב ישראל" (a)(4) | 156-163 | the Minister's regulations (5766-2006) | out-of-scope, refused | `the regulations under paragraph (4) …` | 13 |
| s 1 "תושב ישראל" (b) | 164 ff. | a body of persons | out-of-scope | The row encodes the individual, whom every section here and the capstone are about; the corporate test (incorporation, control and management) is a different regime reached by nothing in this row. | — |
| s 1 "הכנסת עבודה" | 121 | income under s 2(2) | encoded | `s 1 — work income:` | 13 |
| s 1 "בן זוג" | 112 | married, living with and running a joint household | encoded as an input status (`has a spouse`) | nouns | 7 |
| s 1 "גיל הפרישה" | 115 | as in the Retirement Age Law 5764-2004 | out-of-scope (input) | The Retirement Age Law is not in the source bundle; whether a person reached the age is a status the caller supplies (fork F20). | 7 |
| s 2 chapeau | 210 | resident: income anywhere; foreign resident: income in Israel | encoded | `s 2 — …` | 13 |
| s 2(1)-(10) | 213-245 | the ten sources | encoded as an enumeration (the caller classifies) | nouns | 13 |
| s 2(2)(a) | 216 | employment | encoded | `s 1 — work income:` | 13 |
| s 2(2)(b) | 217-220 | the Minister fixes the value of a car or phone | out-of-scope | Its regulations (5747-1987, 5762-2002) are not in the source bundle; the value is part of the item's amount, which the caller supplies. | — |
| s 2(3) | 223 | (repealed) | inert | comment | — |
| s 121A | 4452-4453 | (repealed; its only text is "(בוטל)") | inert | listed here; row IL-03 records the same | — |

### In the ruled scope: added from the capstone's gap order

| provision | lines | gist | disposition | where | GAPS |
| --- | --- | --- | --- | --- | --- |
| s 47(a) chapeau | 1764 | "in this section" | encoded (scope of the module) | `ito-s47a-definitions.l4` | 1 |
| s 47(a)(1) | 1765-1768 | qualifying income, three limbs | encoded | `s 47(a)(1) — …` | 1 |
| s 47(a)(2), (6) | 1769, 1775 | (deleted) | inert | comments | — |
| s 47(a)(3) | 1770 | income for a self-employed member | encoded | `s 47(a)(3) — …`; fork F3 | 1 |
| s 47(a)(4) | 1771 | insured income | encoded as an input, with a consistency rule | `s 47(a)(4) — …` | 1 |
| s 47(a)(5) | 1772-1774 | additional income | encoded | `s 47(a)(5) — …`; fork F3 | 1 |
| s 47(a)(7) | 1776 | beneficiary member: 16% of the year's average wage | encoded | `s 47(a)(7) — …`; forks F2, F8 | 1 |
| s 47(a)(8) | 1777 | the average wage as in s 3(e3)(2) | encoded as an input (the Institute's figure) | nouns; assumption A4 | 1 |
| s 47(b) | 1778-1782 | the deduction for one who is not a beneficiary member | encoded | `s 47(b) — …`; fork F27 | 1 |
| s 47(b1) | 1783-1785 | the deduction for a beneficiary member | encoded, declining where the 12% test's two readings part | `s 47(b1) — …`; forks F28-F30 | 1 |
| s 47(b2) | 1786 | no double deduction | encoded by construction | comment | 1 |
| s 47(c) | 1787 | a deducted sum is out of s 45A | encoded | `s 45A(b) — the pension sums that may be credited, for`; fork F10 | 1 |
| s 47(d) | 1788-1789 | higher rates by regulations (5740-1980) | out-of-scope, refused | `the regulations under section 47(d) are not encoded in this model` | 1 |
| s 64B(a) | 2440 | the officer may determine: more than 50% two years back | encoded | `s 64B(a) — …` | 3 |
| s 64B(b) | 2441 | the couple's election | encoded | `s 64B(b) — …`; fork F31 | 3 |
| s 64B(c) | 2442 | neither had income | encoded | `s 64B(c) — …`; fork F32 | 3 |
| s 64B(d)(1), (d)(2) | 2443-2444 | five years; the officer's power where the elected income falls below 25% | encoded | `s 64B(d)(1) — …`, `s 64B(d)(2) — …` | 3 |
| s 64B(e) | 2445 | the Director's rules | inert | A power to make rules; none in the source bundle; nothing to compute. | — |
| s 65 | 2448 | the couple's income is the registered spouse's; four kinds of his child's income | encoded | `s 65 — …`; fork F33 | 3 |

### Reached by a rule in scope, not encoded: the rule declines

| provision | lines | disposition | reason | GAPS |
| --- | --- | --- | --- | --- |
| s 48 and its order of 5755-1995 | 1806-1808 | out-of-scope, refused | s 48 lets an order apply s 37 (with ss 34, 36) to Area residents who are not Israeli citizens; the order is not in the bundle and s 48 is not in the ruled scope (GAPS item 12). s 37 declines a non-resident Area resident it would credit "as if" resident, in row IL-01's words. | 12 |
| s 48A and the Regulations of 5775-2014 | 1810-1812 | out-of-scope, refused | The Regulations may take any credit of the Chapter from a foreign worker; ss 35, 37, 38, 39, 40(b) and 45A decline a foreign worker they would credit, in row IL-01's words. s 47 is a deduction, which s 48A does not reach. | 12 |
| s 14(b) | 1141 | out-of-scope, refused | It displaces the definition of "Israeli resident" for a first-time resident's adjustment year; outside the ruled scope. | 13 |

### Out of this row

| provision | disposition | reason | GAPS |
| --- | --- | --- | --- |
| National Health Insurance Law 5754-1994 | out-of-scope | Ruled out of this row: its text is not deposited (the subject `il/national-health-insurance-law-5754-1994/` holds none), and a row needs its source. | 4 |
| s 164 and the Income Tax (Deduction from Salary and Wages) Regulations 5753-1993 | out-of-scope | Ruled out of this row: the Regulations, which fix the month's withholding "in the manner and at the rates prescribed", are not in the source bundle. | 5 |
| ss 39A, 39B | out-of-scope | Listed in GAPS item 8 but not in this row's ruled scope (the row's list, plus ss 47, 64B, 65 and NII ss 72, 335): a discharged soldier's and a combat reservist's credits (lines 1609-1630); s 39B carries a 2026-2027 temporary provision. | 8 |
| ss 40A-40F | out-of-scope | Same reason: a remarried divorcee, a youth, academic degrees, vocational qualifications, their non-accumulation, and an expired section (lines 1648-1687). | 8 |
| s 41 | out-of-scope | A spouse married for part of the year (lines 1689-1693); it apportions ss 34, 36, 40(b) and 40B by months; not in the ruled scope, and not reached by the capstone's whole-year households. | — |
| ss 44, 45, 46-46C | out-of-scope | GAPS item 8; not in the ruled scope: institutional care, an incapacitated child, donations (lines 1703-1762). | 8 |
| s 47A | out-of-scope | Not in the ruled scope: the deduction for national-insurance contributions on non-work income (lines 1791-1797). | — |
| s 35A | out-of-scope | Repealed (line 1591); listed so the numbering has no silent gap. | — |
| s 65A | out-of-scope | A file's name (lines 2450-2452); procedure, nothing to compute. | — |
| s 66 | out-of-scope | Row IL-02. s 66 applies "notwithstanding s 65"; this row's s 65 says so and does not re-encode s 66. | 3 |
| s 120B | out-of-scope | Row IL-03. It adjusts the amounts of ss 45A and 47 ("הנחות סוציאליות", s 120A, line 4332) and freezes them for 2025-2027; this row takes the year's amounts as inputs. | 1 |
| Minimum Wage Law 5747-1987 | out-of-scope | GAPS item 11; not in the ruled scope and not deposited. | 11 |

## 3. Tax years, and assumptions

**A1 — tax years from 2024.**
The last amendment entry on each section encoded: s 40 תשפ״ד־3 (in force from tax year 2024, by the two Tax Authority circulars row IL-02 cites); s 35 תשפ״ב־7 (Amendment 262, in force from 1 January 2022, read for this row); s 45A תשע״ז־3; s 47 תשע״ו־4; s 37 תשפ״ב; ss 38, 39 תשס״ה־6; s 64B תשע״ד־3; s 65 תשס״ה־9; s 1 תשע״ז־13; s 2 תשס״ב־9.
So from 2024 every section's deposited text is its latest, unless an amendment exists that the consolidation does not show.
Every top-level rule declines a tax year before 2024: "row IL-08 does not hold the text of these sections for a tax year before 2024".
For s 40(b) the earlier text certainly differed; for the others the commencement of their older amendments was not checked.

**A2 — a tax year after 2026** is answered on the text as it stood at retrieval: a projection.

**A3 — a yearly amount is twelve times the booklet's monthly figure.**
The Ordinance prints the s 45A and s 47 amounts per year; the Tax Authority's withholding booklet, per month.
`ito-il08-published-figures.l4` derives the yearly figure as twelve times the monthly and says so in the rule's name.
Support, not proof: the booklet's yearly beneficiary-member figure (26,436) is 16% of twelve times its monthly average wage (26,436.48) to the shekel below; its 19,400 for s 45A(e)(2) is twice 9,700, as the text's "twice the paragraph (1) amount" is; its 24,250 for additional income is two and a half times 9,700, as s 47(a)(5)(2) is.
The Wikisource editorial notes print the same yearly figures (116,400; 164,400; 2,268), but they are not law and are not used.

**A4 — the average wage for the year is twelve times the Institute's monthly figure.**
s 47(a)(7) reads "16% מסך כל השכר הממוצע במשק באותה שנת מס", the average wage summed over the tax year; s 47(a)(8) and s 3(e3)(2) take the figure the National Insurance Institute publishes, which the booklet prints as 13,769 for 2026 (12,536 for 2024 and 2025).
Taken as the same in every month of the year; the input is the year's total, so a caller who knows otherwise supplies it.

**A5 — classifications outside the row are inputs**: residence where no finding or presumption decides it; "a parent in a single-parent family" (not defined in the Ordinance: the phrase occurs only at lines 1633, 1634 and 1639); retirement age; blindness or disability under s 9(5); proofs "להנחת דעתו של פקיד השומה"; the registered spouse; which limb of s 45A a payment belongs to; insured income; the months an immigrant resided in Israel.

## 4. Fork register

None has been settled by a court or the Tax Authority to my knowledge; no case law was searched.

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | s 45A(d), (e) | The limits cap "the total for which credit is given", but the sums are credited at 25% and 35%: which are credited when a limit cuts sums of both rates? And under (e)(2)(b)(2), is a survivors' sum in part (a) or part (b)? | (i) the 35% sums first; (ii) in proportion; (iii) the text does not say | **(iii): declined by name** where it matters, and computed exactly where it does not: nothing cut (every sum at its rate), or every creditable sum at 35% (the rate is one, and which sum inside a capped part is cut changes no shekel). The common employee case (pension contributions only) always answers. |
| F2 | s 47(a)(7) | Which sums make a beneficiary member: every sum paid to a pension fund for him (employer's benefits and severance, and his own), or some? | (i) every sum "שולמו בעדו"; (ii) the benefits components only | **(i)**: "סכומים לקופת גמל לקצבה" is not qualified. The input is the total, so a caller who reads it otherwise supplies a different total. |
| F3 | s 47(a)(3), (5)(2) | A subtraction that comes out negative (insured income above the paragraph (1) amount). | nil, or a negative income | **nil**: an income is not negative; read as no such income. |
| F4 | s 45A(a)(1) | "אם הוא תושב ישראל": is "he" the individual or the insurance (company)? | the individual; the insurer | **the individual**: masculine "הוא" agrees with "יחיד", not with "חברת ביטוח" (feminine). A non-resident's life-insurance sums earn nothing under (a). |
| F5 | s 45A(d)(2)(b), (e)(2)(b) provisos | Do the provisos (survivors' 1.5%, the 5% part) bind when limb (1)'s fixed amount is the higher? | (i) only when limb (2) governs; (ii) always | **(i)**: they are part of limb (2)(b)'s text; limb (1) is a floor that does not depend on how the sums are made up. |
| F6 | s 45A(e)(2)(b)(2)(a); s 47(b)(2)(a) | Which part of the work income is in qualifying income, the insured or the uninsured? | (i) insured first; (ii) uninsured first; (iii) in proportion | **(i)**: "הכנסתו המזכה שהיא הכנסה מבוטחת" = the lesser of the insured income and the qualifying work income. Only an individual with both insured and uninsured work income above 116,400 is affected. |
| F7 | s 45A(d)(2)(b)(2) | "ובשל הכנסה שאינה מעבודה" in the 5% proviso | (i) pension sums paid in respect of income not from work; (ii) something else | **(i)**, with that part of the sums an input (`of the pension sums above, those paid in respect of income not from work`). |
| F8 | s 47(a)(7) | The booklet prints 26,436 for 2026; 16% of 165,228 is 26,436.48. | the exact figure; the booklet's | **exact**: "שלא פחת מ־16%". A test shows 26,436 is not enough under the text; the booklet's rounded figure would say it is. Fifty agorot apart; open question 4. |
| F9 | s 45A(b1) | "בכפוף לתנאים האמורים באותם סעיפים קטנים": does (a)(1)'s residence condition reach the child's life insurance? | yes; no | **yes**: the words incorporate the conditions of (a) and (b). |
| F10 | s 47(c) | Out of which s 45A limb do sums deducted under s 47 come? | the pension-fund and pension-right limbs; any | **those two**: s 47 deducts only such sums. |
| F11 | s 45A | The credit is money "יזוכה ממס", set off against the tax with the credit points and other credits. In what order? | — | **Not decided here**: the rule returns the credit; the set-off is the composer's (row IL-07's fork K3 asks the same of credit points and s 121B). |
| F12 | s 40(b)(1) | "שבשנת המס טרם מלאו להם תשע־עשרה שנה" | turned 18 or less in the tax year; under 19 on some day | **turned 18 or less**: the table's last band is the year of majority (18), in which the child is still in. Row IL-02's F15 reads the like words of s 66(a)(3), "not yet 18 in the tax year", the same way (aged 17 or less in the year). |
| F13 | s 40(b)(1A1) | Does the mother's election reach (1A) points that the proviso gives her, and (1B)'s (1A) points? | yes; (1) only | **yes**: "נקודות הזיכוי שלהן היא זכאית כאמור באותן פסקאות" names (1) and (1A). |
| F14 | s 40(b)(1A) | The proviso turns on the other parent's entitlement under (1). | compute it; take it as given | **taken as an input on the child's record**: it is this module's own answer about the other parent, which a caller obtains by asking about that parent. |
| F15 | s 40(b)(1A) | "ואינו זכאי לנקודות זיכוי לפי פסקה (1)": per child, or under (1) at all? | per child; at all | **per child**: the mother's limb says "בשל אותו ילד", and "בשל כל ילד כאמור" follows. A single father of other children still has (1A) points for a child not with him. |
| F16 | s 40(b)(1B), (2) | "נקודת זיכוי אחת נוספת": once, or per child? | once; per child | **once**: the singular, attached to the parent, not to "כל ילד". |
| F17 | s 40(b)(1B) | Its second limb sets the (1A) points "כנגד הכנסתו של ההורה": against all his income, or against income from personal exertion? | personal exertion; all | **personal exertion**: they are "the points under that paragraph", which (1A) sets against that tax; the words name whose income, displacing (1A)'s allocation to the father. |
| F18 | s 40(b)(2) | Must the parent who shares the maintenance be resident? | no condition; resident | **no condition**: (2) has none, unlike (1) and (1A). |
| F19 | s 40(a); ss 38, 39 | Is anyone "entitled to allowance points under s 40(a)" today? s 40(a) points at s 109 of the 1968 consolidation, which the present Law's table maps to s 68 and Schedule D (NII lines 5405, 4518), and Schedule D is repealed. | an input either way | **An input** (`entitled to allowance points under section 40(a)`): it chooses 1 1/2 or 1 3/4 points in ss 38 and 39. Open question 3. |
| F20 | s 37 | When must the retirement age have been reached: by the end of the tax year, at its start, for all of it? | — | **an input**, `has reached retirement age`, read as reached in or before the tax year; the Retirement Age Law is not in the bundle. |
| F21 | s 38(a), s 39 | "ולענין יחיד מוטב כהגדרתו בסעיף 37 תובא בחשבון גם נקודת זיכוי": must the s 37 maintenance be proved too? | the status alone; all of s 37 | **the status alone**: the words point at the definition ("כהגדרתו"), and where the spouse works the maintenance could rarely be proved. |
| F22 | s 38(b) | "סכום חלקי נקודות הזיכוי האמורות": does it include the s 37 point? And with the income left out, does the s 37 point by s 38 go too? | — | **the fractional points of (a) only** (1/4 + 1 1/2 or 1 3/4); and **all of s 38's points go**, because (a)'s premise (income that includes the spouse's) then fails. s 37 may still apply on its own terms. Note the consolidation's words "לא תיכלל הכנסתו של בן הזוג הרשום" read literally as "the registered spouse's income shall not be included"; read as the other spouse's income not being included in the registered spouse's. |
| F23 | ss 37, 38, 39 | s 37 applies on its own terms and s 38 or s 39 adds "the point under s 37": one point or two? | one; two | **one**: both cross-references are to the same point, "כאמור באותו סעיף". |
| F24 | s 35(a), (c) | Months of the period: calendar months from the month of immigration, or months from the day? | calendar, the month of immigration first; from the day | **calendar months**, because (c) credits a year "לפי מספר החדשים שהעולה ישב בישראל באותה שנה", a count of the year's months. |
| F25 | s 35(c) | A month abroad not left out at the immigrant's request: does it use up a month of the period? | yes, uncredited; no | **yes**: only a continuous absence of six months to three years may be left out, and only on request. |
| F26 | s 1 "תושב ישראל" (a) | No finding and no presumption: not resident? | not resident; unknown | **unknown, declined**: the presumptions are one-sided; their absence is no finding that the centre of life is abroad. |
| F27 | s 47(b) | "לא יעלה על – (1) …; (2) …": two caps that add, or alternatives? | add; the lower; the higher | **add**: the limbs measure different income (not from work; work not insured). |
| F28 | s 47(b1)(2) | "16% מהשכר הממוצע במשק": monthly or of the year? | the year's total | **the year's total**, as s 47(a)(7) says expressly. |
| F29 | s 47(b1)(2) proviso | Which "sums deposited for the beneficiary member" are the first 16%? | all deposits for him; the sums of (b1) only | **all deposits for him** (the figure that made him a beneficiary member): (2) reaches only the part of the sums not deducted under (1) that lies above it. |
| F30 | s 47(b1)(2) | The 12% test: on all the sums not deducted under (1), or only those the proviso lets (2) reach? | — | **declined where the two readings give different limits**; they usually agree. |
| F31 | s 64B(b) | "לפחות שלושה חדשים לפני תחילתה של שנת מס": the last day for notice | 1 October; 30 September | **1 October** of the year before (three months before 1 January, inclusive). |
| F32 | s 64B(a), (c) | Equal incomes two years back: neither above 50%, neither at nil. | no power; either | **as written: neither power arises.** |
| F33 | s 65 | The exception (inheritance, bodily injury) names interest, a REIT's income and capital gain, not a transparent company's income. | not excepted; excepted | **not excepted**, as written. |

## 5. Answer tables

### s 45A for an employee, tax year 2026 (tests `ito-il08-tests-s45a-s47.l4`)

The employer pays 6.5% and 6% (severance) to a pension fund on the whole salary, which is all insured income; the employee pays the percentage shown; no other sums.
Figures: 2,268; 116,400; 164,400; 165,228 (A3, A4).

| monthly salary | deposits for him in the year | beneficiary member (≥ 26,436.48) | subsection | the limit | his own payments | credit |
| ---: | ---: | --- | --- | ---: | ---: | ---: |
| 5,000 | 11,100 | no | (d): 7% of 60,000 = 4,200 | 4,200 | 3,600 (6%) | 1,260 |
| 10,000 | 22,200 | no | (d): 7% of 116,400 = 8,148 | 8,148 | 7,200 (6%) | 2,520 |
| 15,000 | 33,300 | yes | (e): 7% of 116,400 + 5% of 0 = 8,148 | 8,148 | 10,800 (6%) | 2,851.8 |
| 15,000 | 35,100 | yes | (e) | 8,148 | 12,600 (7%) | 2,851.8 |
| 20,000 a year | 3,700 | no | (d): limb (1) 2,268 governs | 2,268 | 1,200 | 420 |

So 2,851.8 (35% of 7% of 116,400) is the most any employee whose salary is all insured income can get under (a)-(e); s 47 gives such an employee nothing (`ito-il08-tests-s47-deduction.l4`).

### s 40(b), credit points per child, from tax year 2024

Age = the tax year less the child's tax year of birth.

| age in the tax year | (1), parent the child is with | (1) with the mother's (1A1) election | (1A), the other parent (man's table) |
| --- | ---: | ---: | ---: |
| 0 | 2 1/2 | 1 1/2 | 2 1/2 |
| 1 | 4 1/2 | 5 1/2 | 4 1/2 |
| 2 | 4 1/2 | 4 1/2 | 4 1/2 |
| 3 | 3 1/2 | 3 1/2 | 3 1/2 |
| 4, 5 | 2 1/2 | 2 1/2 | 2 1/2 |
| 6 to 17 | 2 | 2 | 1 |
| 18 | 1/2 | 1/2 | 0 |
| 19 and over | 0 | 0 | 0 |

Beside these: (1B) one further point (once) and the (1A) column for each child of one parent, against the tax on income from personal exertion; (2) one further point to the parent entitled under (1) where the parents live apart, and to the other parent one point times his share of the maintenance.
For a household like row IL-07's H12 (a single father, children turning 11 and 7), if he lives apart from their mother: 4 under (1) and 1 under (2), 5 points against the tax generally; 4 if not.

### s 35, fractions of a point per month of the period

| place in the period | immigrated before 1 January 2022 | first became an immigrant from 1 January 2022 |
| --- | --- | --- |
| 1-12 | 1/4 | 1/12 |
| 13-18 | 1/4 | 1/4 |
| 19-30 | 1/6 | 1/4 |
| 31-42 | 1/12 | 1/6 |
| 43-54 | — | 1/12 |

### ss 37-39, points

| case | s 37 | s 38 | s 39 | together |
| --- | ---: | ---: | ---: | ---: |
| beneficiary individual, spouse maintained, proved | 1 | — | — | 1 |
| registered spouse, working spouse earning more than 25,410 (2026), no allowance points | — | 1 3/4 | — | 1 3/4 |
| the same, with allowance points (bar 29,040) | — | 2 | — | 2 |
| the same, a beneficiary individual | — | 2 3/4 | — | 2 3/4 |
| spouse helped in the business | — | — | 1 1/2 | 1 1/2 |
| both s 38 and s 39 apply, no election / electing s 39 | — | 1 3/4 / 0 | 0 / 1 1/2 | 1 3/4 / 1 1/2 |

## 6. What these rows imply for the capstone's adapters

For a later version of row IL-07; nothing here was edited in it.

- **GAPS 1, s 45A (and s 47).** The input "no credit or deduction beyond those the composed rows encode" can give way, for pension contributions, to `the credit under section 45A for`, built from the salary (work and insured income), the deposits for the earner (employer and employee), the employee's own contribution, and `the amounts of sections 45A and 47, as twelve times the Tax Authority's monthly figures, for tax year` 2026. The credit is money, not points; where it is set off against the tax beside the credit points is the capstone's fork K3 again (F11). s 47 is nil for a fully insured employee. A household that also pays life insurance may be declined (F1).
- **GAPS 2, s 40(b).** The refusal for a parent without a spouse can give way to `the credit points under section 40(b) for`, with the (1)/(2) points against the tax generally and the (1A)/(1B) points against the tax on income from personal exertion, which for a salaried earner is the whole s 121 tax. New inputs: single-parent family, living apart, the share of maintenance, and per child whether it is with and maintained by the parent.
- **GAPS 3, s 65 with s 64B.** Where no separate calculation governs, `s 65 — the income charged in the registered spouse's name` gives the income for IL-03's s 121; the credits are then each section's own for the registered spouse (IL-01's ss 34, 36, 36A; this row's ss 35(b), 37, 38, 39). Read as row IL-07 itself reads it (its K4), neither s 66(c) nor s 40(b) gives children's points in a consolidated calculation of a couple living together. For H11 (180,000, registered, wife at home, children 3 and 7) that is 25,392 − 2.25 × 2,904 = 18,858 against 5,790 under a separate calculation: a reading for the capstone to test, not a computed answer of this row. s 64B's rules check that a recorded registered spouse could have been determined or elected; who is registered remains an input.
- **GAPS 7, s 37** becomes computable from status facts; ss 38 and 39 matter only under s 65.
- **GAPS 8, s 35** is computable from the day of immigration and the months resided.
- **GAPS 13.** `s 1 "Israeli resident" (a) — an Israeli resident in the tax year:` decides residence where a finding or an unrebutted presumption does; `s 1 — work income:` and s 2's charge classify the salary.
- **Not discharged:** GAPS 4 (health insurance) and 5 (s 164, withholding) are out of this row; GAPS 11 (Minimum Wage Law) and 12 (ss 48 and 48A's instruments) are outside its ruled scope, and 12 is declined where reached.

The companion row's notes cover GAPS 6 (s 72), 9 (s 335) and 10 (Part D).

## 7. Nouns to reconcile

Read from rows IL-01, IL-02, IL-03 and IL-07 (read-only); nothing imported.

- **The individual.** IL-01 `Individual` (resident, `a woman`, Area resident, `a foreign worker`); IL-02 `A spouse`; IL-03 `An individual in a tax year` (date of birth, items of income); this row four records, one per group of sections: `An individual in a tax year, for sections 45A and 47`, `A parent in a tax year, for section 40(b)`, `An individual in a tax year, for sections 37 to 39`, `An immigrant in a tax year, for section 35`. The field names `tax year`, `an Israeli resident in the tax year` and `a foreign worker` are IL-01's and IL-03's spellings. One person record for the subject would carry all of them.
- **The child.** IL-02 `A child` (`tax year of birth`, whose child, `the mother elects to count one birth-year credit point in the following tax year`, the child's income); IL-06 `A child` (date of birth); this row `A child, for section 40(b)` with IL-02's two field names. Row IL-07 already proposes qualifying IL-02's and IL-06's names (its RECONCILE.md N3); this row's name is qualified.
- **Father or mother.** IL-06 `Father or mother` (`the child's father`, `the child's mother`); this row `Father or mother of the child, for section 40(b)` (`the father of the child`, `the mother of the child`). Same fact, different constructors.
- **Which spouse.** IL-02 `Which spouse` (`registered spouse`, `spouse who is not the registered spouse`); this row `Which of the couple` (`the first spouse`, `the second spouse`), because s 64B decides which is registered and cannot presuppose it.
- **Items of income.** IL-02 `An item of income from personal exertion`; IL-03 `An item of income`; this row `An item of income, for section 2` (source, in Israel or not) and `An item of a household's income, for section 65` (whose, kind, the inheritance exception). Four shapes of one thing.
- **Income split.** This row's s 45A/47 record splits taxable income into work and other income "before the deductions under sections 47 and 47A"; IL-03's items carry `from personal exertion` and `under section 2(1) or 2(2)`. Work income (s 2(2)) is a subset of income from personal exertion; an adapter maps one to the other.
- **The credit-point value** is an input here (`the value of one credit point`, IL-01's name) for s 38(b) and s 35(b).
- **The amounts of ss 45A and 47** are IL-03's s 120B "social deductions" (its `A kind of amount adjusted under section 120B` constructor `a social deduction`); IL-03 could compute the frozen 2025-2027 figures from the 1 January 2024 ones, as row IL-07 does for the credit point (its K2).
- **Refusals for ss 48 and 48A** use IL-01's exact words, under names prefixed "row IL-08", so a caller sees one message for one gap.
- **Retirement age** here (Retirement Age Law, via ITO s 1) and in the companion row's Part D (NII Schedule A1, a different table) are different ages; they must not be joined.

## 8. Sources: what was read, fetched, and not

**Read**: the deposited Ordinance, by line, for every provision cited; the deposited National Insurance Law at the lines cited for s 40(a) (the table of old and new section numbers, and Schedule D); row IL-07's `GAPS.md`, `BRIEF.md`, `NOTES.md`, `RECONCILE.md`; rows IL-01, IL-02 and IL-03's `BRIEF.md`, `encoding.json`, nouns and some rule modules, and their `NOTES.md` up to and **not including** the section headed "Comparison with Axiom's RuleSpec" (IL-01 before line 249, IL-02 before 220; IL-03's NOTES.md was not read); rows IL-05 and IL-06's NOTES.md likewise (IL-05 before 347, by search; IL-06 before 232); the two skills and `gotchas.md`, `builtins.md`; `l4-pipeline/BACKLOG.md` lines 55-94 (the Tier 1 table and its notes, which name the reference files and case counts of the Axiom Foundation's encodings but quote none of their content).
**Not read**: anything of the Axiom Foundation, any path the brief forbids, any `INDEPENDENT-FINDINGS.md`, `DECIDED-ANSWERS.md` or `tests-independent.l4`. The session scratchpad holds files named for Axiom and for other agents' independent passes; their names were seen in a directory listing and none was opened.

**Fetched**, into the session scratchpad, not deposited:

| what | URL | retrieved (UTC) | bytes | sha256 | used for |
| --- | --- | --- | --- | --- | --- |
| [a262] Income Tax Ordinance (Amendment No. 262) Law, 5782-2022, Sefer HaChukim 2994 p. 1000 (5 July 2022), 2 pp. | `https://web.archive.org/web/20240203193315id_/https://fs.knesset.gov.il/24/law/24_lsr_648920.pdf` (a direct fetch of the Knesset URL was redirected to its geographic maintenance page) | 2026-10-06T23:44:38Z | 161,990 | `baf0284bbaa0f265f49257b95d3b1884dc50885ef775108b2a59bf81bbbf265c` | s 35: which text governs (s 2, commencement and application) |
| [booklet-2026] Israel Tax Authority, monthly withholding booklet for 2026, 36 pp. | `https://web.archive.org/web/20260207101513id_/https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf` | 2026-10-06T23:46:08Z | 610,829 | `282bb886ccae1cc718840127af378fce88ca37ee3b2b9f00ed2cd44467e86285` (row IL-01 recorded the same) | PDF p. 9: the s 45A and s 47 figures and the average wage |

Also read, not re-fetched: row IL-01's copies of the 2024 and 2025 booklets in the session scratchpad (sha256 `35aed117…` and `41496dd3…`, as IL-01 records them, re-checked on 2026-10-07), PDF pp. 11 and 10, for the same figures; and its copy of the 2025 form-135 notes, searched for a worked example of s 45A (none found).
No officially published worked example of s 45A or s 47 was found in the two documents searched; the tests are worked from the text.
The Israeli fetch proxy was not used.

## 9. Open questions for a domain expert

1. F1: when the s 45A limits cut sums credited at 25% and at 35%, which are credited? And under (e)(2)(b)(2), to which part does a survivors' insurance sum belong?
2. F2 and F29: do the employer's severance deposits count towards the 16% that makes a beneficiary member, and towards (b1)(2)'s first 16%?
3. F19: is anyone today "entitled to allowance points under s 40(a)", so that ss 38 and 39 give 1 3/4 points rather than 1 1/2?
4. F8: does the Tax Authority treat 26,436 or 26,436.48 as the 2026 beneficiary-member threshold?
5. F15-F17: the per-child reading of (1A), and the once-only point of (1B) and (2).
6. F24: does the Tax Authority count an immigrant's months from the month of immigration, as this row does?
7. F30: on which sums is s 47(b1)(2)'s 12% test made?
8. F11: in what order is the s 45A credit set off against the tax, beside the credit points?

## 10. What was not done

- **No independent test pass** (skill step 8): one session without sub-agents, as briefed. It is the first thing to add; a test author given `BRIEF.md`, the source and the booklet could work the cases without reading the rules.
- **HG1** not sought.
- **The capstone was not touched**; section 6 says what its adapters would need.
- **Not committed**: the brief forbids any git change.
- **The ITO credit sections outside the ruled scope** (ss 39A, 39B, 40A-40D, 44, 45, 46) remain unencoded; they are the obvious next unit, and GAPS item 8 lists them.

## Comparison with Axiom's RuleSpec (2026-10-07)

Written by the comparison author for row IL-08 (`lad-il-08`), one session, no sub-agents, on 2026-10-07, after both halves of the row and both independent passes had been deposited, as the semi-cleanroom ruling of 2026-10-06 requires.
This section covers the Income Tax Ordinance half only; the National Insurance half's `NOTES.md` carries its own.
Nothing else in this row, and nothing in the commons, was edited; nothing was repaired.
A divergence below is a finding, not a fix.

### What was read

**Axiom.** A local clone of the Axiom Foundation's `rulespec-il`, read-only, at commit `95c6f32c87c75e318631cbd77c14b840bc536c15` (the merge of its PR #8, 2026-10-03); nothing was pulled.
Read: `NOTICE`; the heads of `LICENSE` and `LICENSE-CODE`; `data/coverage/tax-benefit-source-map.json` (whole); `docs/ENCODING-GAPS.md` (lines 140-714, and its headings above); `docs/encoding-charter.md` lines 40-55; `known-missing-money-atoms.yaml` and `known-validation-gaps.yaml` (whole; neither has any entry); `README.md` by search; `il/statutes/composed/worker-with-children-monthly-net-pipeline.yaml` (lines 1-535, and its rule list) and the child facts and outputs of all 15 cases in its `.test.yaml`; `il/statutes/income-tax-ordinance/section-66.yaml` lines 1-140 (its deferrals) and the input names of its `.test.yaml`; the residence condition in `section-34.yaml` and `section-36.yaml`.
No Axiom module exists for any provision of this half (`ls il/statutes/income-tax-ordinance/`: ss 33A, 34, 36, 36A, 66, 120B, 121, 121B only), so there was no module or companion test file of theirs to read for it.
Nothing of any other Axiom repository was read, and nothing under `l4-ide/specs/research/AXIOM-*`.

**Ours.** This row's `BRIEF.md`, `NOTES.md`, `encoding.json`, `INDEPENDENT-FINDINGS.md`, `DECIDED-ANSWERS.md` and `tests-independent.l4`, in full; the modules `ito-il08-tax-years.l4`, `ito-il08-published-figures.l4`, `ito-s1-israeli-resident.l4`, `ito-s2-sources-of-income.l4`, `ito-s35-new-immigrant.l4`, `ito-s40-children-credit-points.l4` and `ito-s64b-s65-registered-spouse.l4` in full; `ito-s37-s38-s39-spouse-credits.l4` to line 120; `ito-s45a-insurance-and-pension-credit.l4`, `ito-s47-deduction.l4`, `ito-s47a-definitions.l4` and `ito-il08-nouns.l4` through their headers, exported rules and the records the comparison used.
Row IL-07's `GAPS.md`.
The deposited Ordinance at the lines cited below (sha256 `b87f2cf4…94b81b6`, checked), and the deposited National Insurance Law at the lines cited for F19.

**Licence.** `NOTICE` puts Axiom's encodings, companion test cases, parameter values and provenance metadata under CC BY 4.0 (`LICENSE`) and its tooling under Apache 2.0 (`LICENSE-CODE`); confirmed from the three files.
Axiom material appears here only as short attributed snippets: Axiom Foundation RuleSpec corpus (CC BY 4.0), https://github.com/TheAxiomFoundation.

**Runs.** Axiom's cases were put through a scratch copy of this directory (the session scratchpad, `lad-il-08/ito/zz-axiom-cases.l4`; cross-directory `IMPORT` does not work), with `/Users/mengwong/.local/bin/l4 run`, `JL4_LIBRARY_PATH` unset, at 2026-10-07T05:59:57Z.
The binary had changed since section 0: `~/.cabal/bin/l4` is now `/Volumes/transcend/caches/cabal/bin/l4`, sha256 `6015a4c3fa181842c597c95948290fe45537963d279ae5b5918a106a0c3b54a6`, modified 2026-10-07T05:35:45Z.
Under it this row's `ito-il08-tests-s37-s40.l4` still gives 52 satisfied, 0 failed, 0 refused, as section 0 records.
The scratch module: 33 assertions, 33 satisfied, 0 errors.

### Coverage: what Axiom did with each provision of this half

Axiom's own inventory, `tax-benefit-source-map.json`, lists the Ordinance's encoded sections as ss 33A, 34, 36, 36A, 66, 120B, 121 and 121B (lines 33-42); its `not_encoded` list names "§35 עולה credit", "§37-§39 credits", s 40(a) and (b), s 45A and s 121A, after "every other section of the Ordinance" (lines 51-58); and its `applied_without_a_module` list names ss 2, 1 and 40, each as one quoted definition used inside the composed pipeline (lines 59-78).

| provision (ours) | source lines | ours | Axiom | Axiom file, status |
| --- | --- | --- | --- | --- |
| s 1 "Israeli resident" (a), individual | 143-163 | encoded: (a)(2)-(3); (a)(1) a recorded finding; (a)(4) refused | **input**: Boolean `taxpayer_is_israeli_resident`, fed to ss 34 and 36 | composed pipeline lines 310-326; `ENCODING-GAPS.md` lines 516-520 ("the Ordinance's §1 residence definition is not encoded") |
| s 1 "work income", s 2(2)(a) | 121, 216 | encoded | **applied without a module**: the whole wage is classed as s 2(2) income, quoting the words of s 2(2)(a) | composed pipeline lines 253-275; source map lines 60-65 |
| s 2 chapeau and (1)-(10) | 209-245 | encoded (territorial charge; sources an enumeration) | **left out** ("every other section") | — |
| s 35 | 1572-1588 | encoded; (e) refused | **left out**, named | source map line 53; `section-66.yaml` lines 35-38 name it among the "unavailable mechanics" of s 66(c)(1) |
| s 37 | 1599-1600 | encoded | **left out**, named | source map line 54; `section-66.yaml` lines 39-43: s 66(c)(2)'s half point kept as a parameter, its application deferred for want of s 37 |
| s 38, s 39 | 1602-1607 | encoded | **left out**, named | source map line 54 |
| s 40(a) | 1632 | inert (fork F19; an input to ss 38, 39) | **left out**, named | source map line 55; `ENCODING-GAPS.md` lines 425-429; `section-66.yaml` lines 44-46 (s 66(c)(3) deferred for want of it) |
| s 40(b)(1), (1A), (1A1), (1B), (2) | 1633-1640 | encoded | **left out**, named; "A single-parent household therefore cannot be computed by this pilot" | source map line 55; `ENCODING-GAPS.md` lines 425-429 |
| s 40(b)(3) "year of birth", "year of majority" | 1644-1645 | encoded (derived from the child's tax year of birth) | **applied without a module**: the 18 of "year of majority" as a parameter; year of birth and year of majority as Boolean inputs per child | composed pipeline lines 432-453; source map lines 72-77; `ENCODING-GAPS.md` lines 410-415 |
| s 45A | 1714-1739 | encoded | **left out**, named; "deliberately out of scope" | source map line 56; `encoding-charter.md` lines 51-53; `ENCODING-GAPS.md` line 682 |
| s 47 | 1763-1789 | encoded; (d) refused | **left out** (not named; "every other section") | `section-66.yaml` lines 35-38 names it with s 45A among s 66(c)(1)'s "unavailable mechanics" |
| s 64B | 2439-2445 | encoded (the conditions on the power and the election) | **left out**; whether a person is the non-registered spouse is an input of their s 66 | `section-66.yaml` line 670 (input `person_is_nonregistered_spouse`) |
| s 65 | 2447-2448 | encoded | **left out**; the composition assumes a separate calculation is elected | composed pipeline lines 137-140; `ENCODING-GAPS.md` lines 522-525 |
| s 121A | 4452-4453 | inert (repealed) | **left out**, named, no reason given | source map line 57; `section-66.yaml` lines 35-38 ("unavailable mechanics" of s 121A) |
| *not ours:* s 1 "tax year" | 202 | **not encoded, no coverage row** | **applied without a module**: 12 months, to annualise the wage and to divide the year's tax | composed pipeline lines 183-198; source map lines 66-71 |

**Counts**, over the fourteen rows of ours: encoded by Axiom as a module, **0**; applied without a module inside their composition, **2** (s 1 "work income" with s 2(2), and s 40(b)(3)); handled as an input, **2** (residence; the registered-spouse status s 64B decides); left out, **10**, of which 7 are named in their `not_encoded` list (ss 35, 37, 38-39, 40(a), 40(b)(1)-(2), 45A, 121A) and 3 fall only under "every other section" (s 2's charge, s 47, s 65).
Where Axiom gives a reason for leaving a provision out, the reason is one of scope (the pilot's bounds, its entity model, its charter), never a reading of the text; the one stated reason that is wrong on the text is s 121A's (A10 below).

### Where Axiom applies one of our provisions: scope, numbers, readings, interface

**s 40(b)(3)** (lines 1644-1645).
Axiom quotes the definition of the year of majority as one parameter, `child_maturity_age_years` = 18, effective 2026-01-01, and uses it as the upper bound of the age-six-to-majority band of s 66(c)(4)-(5) (`age < 18`).
The year of birth and the year of majority are two further Boolean inputs per child (`child_N_is_in_birth_year`, `child_N_is_in_maturity_year`), independent of the age input; their s 66 module says it "does not infer a maturity year from an invented age" (`section-66.yaml` lines 52-55).
Their `child_N_age_years` is "the age the child reaches during the tax year" (composed pipeline lines 72-81), which is our s 40(b)(3) age (the tax year less the tax year of birth).
The text leaves nothing open here; the difference is in the interface.
Where the inputs disagree with each other Axiom has no check: by their formula (composed pipeline lines 492-506), an age of 18 with the maturity flag FALSE gives 0 points, and an age of 17 with it TRUE gives a woman 0.5, without a diagnostic (read, not run).
Ours derives all three from one fact and cannot be contradicted.

**s 2(2)(a)** (line 216) and **s 1 "work income"** (line 121).
Axiom classes the composition's whole wage as s 2(2) income so that it falls in the first category of s 121B(e); it quotes the words of s 2(2)(a) as a definition and computes nothing from s 2.
Ours takes the item's source from the caller and encodes s 2's territorial charge and s 1's "work income".
They agree.

**s 1 "tax year"** (line 202) is applied by Axiom as `months_in_tax_year` = 12, quoting the first limb only (twelve consecutive months from 1 January); the second limb, a special assessment period, does not reach an employee.
This half does not encode it and its coverage table has no row for it; the independent pass's D004 lists it as not represented.

### Axiom's cases put through our encoding

Axiom has no test case of its own on any provision of this half.
The 15 cases of its composed pipeline (`worker-with-children-monthly-net-pipeline.test.yaml`, all for 2026) each rest on our s 1 residence and s 2(2), and, where there are children, on s 40(b)(3); they were put through ours as far as their facts allow.

| Axiom case(s) (test-file line) | what the case takes from our provisions | put through ours | result |
| --- | --- | --- | --- |
| C1 (1), C3 (123), C5 (245), C10 (548), C15 (837): children aged 2 and 8 | s 40(b)(3): neither child in its year of birth or of majority | `s 40(b)(3) — the age the child turns in tax year` 2026, children born 2024 and 2018 | **match** (age 2 and 8; neither 0 nor 18) |
| C2 (62): the same children, a father | the same | the same | **match** |
| C6 (304), C7 (365), C13 (731): a child in its year of birth (age 0) and one in its year of majority (age 18) | s 40(b)(3), both flags | born 2026 and 2008 | **match** (0 is the year of birth; 18 the year of majority) |
| C8 (426): aged 3 and 5 | s 40(b)(3) | born 2023 and 2021 | **match** |
| C9 (487): aged 19 and 8 | s 40(b)(3): 19 is past the year of majority | born 2007 and 2018 | **match** |
| C11 (609): aged 17 and 8 | s 40(b)(3) | born 2009 and 2018 | **match** |
| C12 (670): `child_1_age_years` 3, `child_1_age_at_month_years` 2 | s 40(b)(3): the age reached in the year, 3 | born 2023 | **match** |
| C4 (184), C14 (792): no children | — | — | not applicable |
| all 15 | s 2(2): the wage (12 × the monthly wage) is s 2(2) income | `s 1 — work income:` and s 2's charge on an employment item of 180,000 (C1's figure; the rule does not read the amount) | **match** |
| all 15 | s 1 residence | — | **could not be run**: the case supplies the conclusion (`taxpayer_is_israeli_resident: true`), not the days in Israel or a finding our rule reads |
| all 15 | s 1 "tax year" (12 months) | — | **could not be run**: not encoded in this half |

Beside these, labelled as a cross-check of figures and not of a reading: the per-child points Axiom's composition reads from s 66(c)(4)(a) (a woman) and s 66(c)(5) (a man), at every age its cases use, equal our s 40(b)(1) table (2.5, 4.5, 3.5, 2.5, 2, 2, 0.5, 0 at ages 0, 2, 3, 5, 8, 17, 18, 19) and our s 40(b)(1A) table (2.5, 4.5, 1, 0 at ages 0, 2, 8, 18).
The two Ordinance provisions print the same ladders (lines 1633, 1635-1637; 2466, 2473-2476).
12 assertions, all satisfied.

A probe, not an Axiom case: the father of C2's children (aged 2 and 8) as a single parent with whom they live gets 6.5 points under our s 40(b)(1) (4.5 + 2, against the tax generally, 0 against the tax on income from personal exertion; 2 assertions, satisfied).
C2's own figures for the same children, under s 66(c)(5), are 4.5 + 1 = 5.5; that is what Axiom's composition gives such a father, since nothing in its inputs says he has no spouse (A6).

### Divergences and differences

| id | provision | ours | Axiom | source lines | classification | repair if ours is wrong |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | s 40(b)(3) | year of birth and of majority derived from the child's tax year of birth | the 18 as a parameter; both years as Boolean inputs per child, unchecked against the age | 1644-1645 | representational difference; no case diverges | — |
| A2 | s 2(2), s 1 "work income" | caller classifies the item; territorial charge encoded | the whole wage is s 2(2) income, quoted | 121, 210, 216 | representational difference; agree | — |
| A3 | s 1 "tax year" | not encoded; no coverage row | applied: 12 months | 202 | scope difference (a gap in our coverage table, not in a rule; D004 of the independent pass says the same) | none needed in a rule; a coverage row in section 2 |
| A4 | s 1 "Israeli resident" | encoded as far as the text decides, refusing otherwise | a Boolean input | 143-163 | scope difference | — |
| A5 | s 40(a) | inert; F19: the old s 109 it points at maps to the present s 68 and Schedule D, and Schedule D is repealed | described as a live entitlement ("נקודות קיצבה for children, paid by the National Insurance Institute under §109 of the 1968 Law"); their s 66(c)(3) deferral calls them "pension points" and says computing them "requires the unavailable section 40(a) entitlement" | ITO 1632, 2464; NII 5405, 4518 | genuine ambiguity, recorded by us and not by them; no figure differs (neither computes it) | — |
| A6 | s 40(b)(1)-(2) and a single parent | encoded | not encoded, and the composition has no input for whether the earner has a spouse: a single parent put to it gets s 66(c)'s ladders | 1633-1640; s 66(a)(1) line 2456 gives the separate calculation to "a spouse who is not the registered spouse" | scope difference, silent on their side (their gap entry says single parents cannot be computed; the pipeline does not refuse them) | — |
| A7 | s 45A, s 47 | encoded | left out; the composition's taxable income is twelve times the wage, with no s 47 deduction, no s 45A credit and no input for either | 1714-1739, 1763-1789 | scope difference, documented in their prose, silent in their output | — |
| A8 | s 35, ss 37-39 | encoded | left out; their s 66(c)(1) and (c)(2) deferrals name ss 35, 37, 45A and 47 as missing dependencies | 1572-1607; s 66(c)(1)-(2) lines 2461, 2463 | scope difference; our modules are the dependencies their deferrals name, subject to each module's inputs | — |
| A9 | s 64B, s 65 | encoded | left out; separate calculation assumed; the non-registered status an input to their s 66 | 2439-2448 | scope difference, silent on their side for a couple assessed under s 65 | — |
| A10 | s 121A | inert: repealed, its only text "(בוטל)" | in `not_encoded` without a reason, and among the "unavailable mechanics" their s 66(c)(1) deferral says it needs | 4452-4453; s 66(c)(1) line 2461 still names it | **theirs wrong** in a stated reason (a repealed section has no mechanics to supply); no figure affected | — |
| A11 | s 40(b)(1A1); their s 66(c)(4)(a1) | the mother's election applied from the child's record (a flag, and the age 0 or 1) | the parallel election of s 66(c)(4)(a1) not applied: it "needs the same mother and child connected across two tax years, which this pilot's entity surface cannot express" | 1638; `ENCODING-GAPS.md` lines 417-423 | representational difference (two provisions, one device); ours applies it, and the independent pass found it moves two points for a child of one parent (its observation 1) | — |
| A12 | tax years | every top-level rule refuses a year before 2024 (A1) | the composition answers from 2026-01-01; most of their atomic modules carry `effective_from: '0001-01-01'` and "will answer a request for any earlier year with the current text" | `ENCODING-GAPS.md` lines 192-217 | representational difference; no Axiom module of this half for it to bite on | — |

No divergence shows a rule of this half wrong on the text.

### Our independent pass's findings, and Axiom

| finding (`INDEPENDENT-FINDINGS.md`) | Axiom |
| --- | --- |
| 1, D187: the s 45A(d)(1) floor is lost when survivors' insurance exceeds it (an encoding error, a cliff) | nothing: s 45A not encoded |
| R1, D183: life insurance alone above the 5% proviso refused where the text answers | nothing: s 45A not encoded |
| 2, D019: the second limb of "foreign resident" (lines 167-169) can overlap a centre-of-life residence | nothing: residence is a Boolean input, so their caller decides; neither encoding has a coverage row for "foreign resident" |
| 3, D055: a second immigration, and the rules of s 35(e) | nothing: s 35 not encoded |
| 4-6, D190, D236: whether the s 47(b) deduction or the s 45A credit takes a payment first | nothing: both left out, and their s 66(c)(1) deferral names both |
| 7, D244: the tester's own error | — |
| R2-R8: years before 2024 refused (A1) | see A12 |
| observation 1: (1A1) moves two points for a child of one parent | see A11: Axiom declined the parallel election rather than apply it |
| D004 (not represented): a date's tax year | Axiom applies s 1's definition (A3) |
| D300, D303 (not represented): the value of a credit point | Axiom also takes it as an input, `credit_point_value_for_tax_year_ils`, 2,904 in every case, sourced from OECD TaxBEN as "a reference, not a source of law" (`ENCODING-GAPS.md` lines 366-368) |
| D109, D271, D292, D293 (silent paths on ss 39, 64B, 65) | the same class of silent assumption in their composition: a separate calculation is assumed, with no input for spouses, the registered spouse or s 65 (A9) |

### Our forks, and F19

Axiom encodes none of ss 35, 37-40(b), 45A, 47, 64B and 65, so none of F1-F33 has an Axiom reading to set against it.
Two touch something Axiom does.
F12 (a child "not yet 19 in the tax year" is in through the year of majority) agrees with the banding of their s 66 ladders, which give the year of majority its own band and nothing from 19 (their C9).
F19: Axiom's record does not address it.
`ENCODING-GAPS.md` (lines 425-429) describes s 40(a) as allowance points paid "under §109 of the 1968 Law", and their s 66 module defers s 66(c)(3) because computing those points "requires the unavailable section 40(a) entitlement"; neither notes that the National Insurance Law's own table maps the old s 109 to the present s 68 and Schedule D (NII line 5405) and that Schedule D is repealed (NII line 4518).
One further piece of evidence for F19 found in this pass: the consolidation's own link on the words "s 109 of the National Insurance Law [Consolidated Version], 5728-1968" at ITO line 1632 targets the present Law's s 68 (an editorial link of an unofficial consolidation, not law).
F19 stays open; it is a question for a domain expert, not one Axiom's material settles.

### What Axiom does that this half does not, and the reverse

**Axiom, not us**: s 1's definition of the tax year (A3); a composed monthly net with proof atoms quoting each figure, reporting the statute's nominal child-allowance amounts beside the supplied current ones; a written list of what the composition assumes (`composed-capstone-bounds`); records of encoder runs that failed, and why.
**Us, not Axiom**: every one of the fourteen provisions in the table above, with refusals where the text does not decide (the s 35(e) rules, the s 47(d) regulations, s 48, s 48A, s 14(b), s 1(a)(4)), the year gate, the Tax Authority's 2024-2026 figures carried as published figures and not as law, and 33 recorded forks.
Of Axiom's own stated dependencies, our modules supply s 66(c)(1)'s ss 35, 45A and 47, s 66(c)(2)'s s 37, and s 66(c)(4)(a)'s s 40(b)(3); s 66(c)(3)'s s 40(a) we do not supply either (F19).

### Bottom line

Axiom encodes none of the provisions of this half.
Two of them it applies as one-line definitions inside its composed pipeline, and on those our encoding agrees with every one of its fifteen cases.
No finding of this comparison shows a rule of this half wrong.
What the comparison shows is mostly about scope: Axiom's composed net leaves out ss 35, 37-40(b), 45A, 47 and 65 by design, with no input by which a caller could say any of them applies, so a single parent, a pension contributor, a new immigrant or a couple assessed together is answered without them and without a diagnostic, where row IL-07 declines such households and this row supplies the sections.
Axiom's record treats one repealed section (s 121A) as a missing dependency, and does not examine s 40(a)'s pointer to a repealed schedule (F19).
Two definitions are worth carrying into this row's coverage table, as rows and not as repairs: s 1's "tax year", which Axiom applies (A3), and s 1's "foreign resident", which our own independent pass raised (D019) and which Axiom does not touch either.
