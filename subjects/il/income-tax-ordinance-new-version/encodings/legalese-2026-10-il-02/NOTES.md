# NOTES — Income Tax Ordinance s 66 (separate calculation), row IL-02

Encoder: one Claude session (Opus 5.5), run IL-02-20261006, 2026-10-06, working alone from `BRIEF.md`.
Status: **draft**.
No domain expert has read this against the source; HG1 has not been sought.
No independent test pass was run (the run was instructed to work alone, without sub-agents); see section 8.

## 1. What is encoded, and what is not

Section 66 of the Income Tax Ordinance [New Version], every subsection and paragraph, from the Hebrew text at lines 2454-2484 of `registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` (Hebrew Wikisource, retrieved 2026-10-06, sha256 `b87f2cf437ccfed35c3164681f4fc7ee015a111633454622751930c8894b81b6`).
That file is an unofficial consolidation of the law as amended at retrieval; Hebrew is authoritative.

What the modules answer, for a married couple in a tax year from 2024:

- whether subsection (a) applies at all, given a common source of income (s 66(d));
- whether the spouse who is not the registered spouse may claim, and has made, a separate calculation, and which of that spouse's income from personal exertion it covers, with the pension proviso (s 66(a)(1));
- which spouse takes the pooled income not from personal exertion (s 66(a)(2)), and which children's income is the registered spouse's (s 66(a)(3));
- whether each spouse's pre-marriage or inherited property income is calculated separately, joined to another separate calculation, or left in the pool (s 66(b));
- the taxable income in each calculation, assembled from the above (`ito66-ab-taxable-income.l4`);
- what s 66(c) does with each provision it names, whether (c) governs each spouse's calculation (including a (c)(1A) request), and the credit points (c) itself gives: ½ under s 36A for the woman, ½ under s 37, and the children's points under (c)(4), (4A), (5), (6) with the mother's (a1) election;
- the children's credit as set against the tax on income from personal exertion, given the value of a credit point and that tax.

What is not encoded, and is taken as an input or left to its owner:
s 65 itself (the consolidated calculation is named as an outcome, not computed); the credit-point counts under ss 34, 35, 36 (IL-01 for 34 and 36); s 37's conditions (a GIVEN per spouse); the value of a credit point (s 33A, IL-01) and the tax on income from personal exertion (ss 121 ff., IL-03), both GIVENs of the one rule that needs them, with no default; the classification of income as personal exertion, transparent-company, REIT, interest or capital gain (the caller's); the determination of the registered spouse under s 64B (an input).

## 2. Coverage table

### s 66 itself

| provision | source line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| 66 heading | 2454 | חישוב נפרד | inert | module headers |
| 66(a) chapeau | 2455 | notwithstanding s 65 | encoded | arm order, `s 66(a)-(b) — the calculations, for` |
| 66(a)(1) | 2456 | the other spouse may claim; the pension proviso | encoded | `ito66-a-separate-calculation.l4` |
| 66(a)(2) | 2457 | non-personal-exertion income to the spouse with higher personal-exertion income; none → registered | encoded | same |
| 66(a)(3) | 2458 | a child's transparent-company, REIT, interest, capital-gain income is the registered spouse's | encoded | same |
| 66(b) | 2459 | pre-marriage or inherited property income; the proviso | encoded | `ito66-b-property-income.l4` |
| 66(c) chapeau | 2460 | the provisions applying to the separate calculation | encoded | `s 66(c) — governs the calculation of the` |
| 66(c)(1) | 2461 | ss 34, 35, 36, 45A, 47, 47A, 121A, 10, 11 for each spouse | encoded | `s 66(c) — in a separate calculation, as to` |
| 66(c)(1A) | 2462 | a separate calculation even if the other has no personal-exertion income | encoded | `s 66(c)(1A) — …` |
| 66(c)(2) | 2463 | s 37 ½ only; no ss 38, 39 | encoded | `ito66-c-credit-points.l4` |
| 66(c)(3) | 2464 | s 40(a) pension points to the registered spouse only | encoded | same |
| 66(c)(4) chapeau | 2465 | the woman: ½ under s 36A; children's points against tax on personal-exertion income | encoded | same |
| 66(c)(4)(a) | 2466 | the woman's table; definitions by reference to s 40(b)(3) | encoded | `s 66(c)(4)(a) — the woman's credit points …` |
| 66(c)(4)(a1) | 2467 | the mother may count one birth-year point in the next year | encoded | `s 66(c)(4)(a)-(a1) — …` |
| 66(c)(4)(b) | 2468 | (נמחקה) | inert | stub |
| 66(c)(4)(c) | 2469 | (נמחקה) | inert | stub |
| 66(c)(4)(d) | 2470 | (פקעה) | inert | stub |
| 66(c)(4), unnumbered tail | 2471 | year of birth / year of majority as in s 40(b)(3), repeated | encoded | `the age the child … turns in tax year` |
| 66(c)(4A) | 2472 | a woman married to a widower: his children | encoded | `s 66(c)(4A), (6) — …` |
| 66(c)(5) chapeau | 2473 | the man: children's points against tax on personal-exertion income | encoded | `ito66-c-credit-points.l4` |
| 66(c)(5)(a) | 2474 | 2½ in the year of birth | encoded | `s 66(c)(5) — the man's credit points …` |
| 66(c)(5)(b) | 2475 | 4½ (1-2), 3½ (3), 2½ (4-5) | encoded | same |
| 66(c)(5)(c) | 2476 | 1 from 6 to the year before majority | encoded | same |
| 66(c)(5A) | 2477 | (פקעה) | inert | stub |
| 66(c)(6) | 2478 | a man married to a widow: her children | encoded | `s 66(c)(4A), (6) — …` |
| 66(d)(1)(a)-(c) | 2479-2482 | (a) applies to spouses with a common source only if all three | encoded | `ito66-d-common-source.l4` |
| 66(d)(2) | 2483 | definition of common source | encoded, as an input | the MAYBE `common source of income` |
| 66(e) | 2484 | (בוטל) | inert | stub |

**Totals for s 66: 22 encoded, 6 inert, 0 out-of-scope, 0 deferred.**

### Provisions s 66 points at

| provision | what s 66 needs from it | disposition |
| --- | --- | --- |
| s 1, "הכנסה מיגיעה אישית", paras (1)-(7), lines 170-178 | which kinds of income are in (a)(1), and which are pensions | encoded, as the `Kind of income from personal exertion` enumeration |
| s 40(b)(3), lines 1644-1645 | year of birth, year of majority | encoded where (c)(4)(a) uses it |
| s 65, line 2448 | the rule (a) and (b) displace; the meaning of "ריבית" | out-of-scope: named as an outcome, not computed; interest classified by the caller |
| s 64B, lines 2440-2445 | who is the registered spouse | out-of-scope: an input |
| ss 64A1, 64A2 | transparent company, real estate investment trust | out-of-scope: the caller classifies the income |
| ss 34, 35, 36, 45A, 47, 47A, 121A, 10, 11 | their own deductions, credits, benefits | out-of-scope: (c)(1) is encoded as "each spouse"; the amounts are those sections' |
| s 36A, line 1597 | ½ point for a woman | out-of-scope: the ½ is stated in (c)(4) itself and encoded there |
| s 37, line 1600 | whether the spouse would have a point | out-of-scope: a GIVEN per spouse |
| ss 38, 39 | nothing: (c)(2) excludes them | out-of-scope |
| s 40(a) | pension points | out-of-scope: (c)(3) is encoded as "registered spouse only" |
| s 33A, line 1563 | the value of a credit point | out-of-scope: a GIVEN, no default (IL-01) |
| ss 121 ff. | the tax on income from personal exertion | out-of-scope: a GIVEN, no default (IL-03) |

**Totals for cross-references: 2 encoded, 10 out-of-scope.**

## 3. Tax years, and assumptions

**A1 — the text governs tax years from 2024.**
The amendment list for s 66 (line 2454) ends at תשפ״ג־6 and תשפ״ד־3.
The page header (line 5) resolves them to ס״ח תשפ״ג, 400 (חוק הגדלת נקודות זיכוי להורים במס הכנסה והרחבת מענק עבודה) and ס״ח תשפ״ד, 630 (חוק סיוע להורים לילדים עד גיל שלוש (תיקוני חקיקה)), counting each `ח:תיבה` entry including the three pages 163, 171, 177 of the 5783 Economic Efficiency Law as three.
The amending Acts could not be fetched: `fs.knesset.gov.il` redirected to a geographic maintenance page (2026-10-06).
The commencement is taken from two Israel Tax Authority circulars (section 7), which say both changes to s 66 apply from tax year 2024, the second "רטרואקטיבית החל מיום 1.1.2024".
For a tax year before 2024 every top-level rule refuses: `this encoding does not hold the text of section 66 for a tax year before 2024`.
That is deliberate: the circulars print different 2023 figures for the children's table, so the earlier text certainly differed, and which other paragraphs differed is not known.

**A2 — a tax year after 2026** is answered on the text as it stood on 2026-10-06; that is a projection, not a statement of what was enacted for that year.

**A3 — (c)(1A) moves no income.** It is encoded for its stated consequence, the requesting spouse's entitlement to the (4) or (5) credit points against tax on that spouse's personal-exertion income. It does not create a separate income calculation for the registered spouse in `ito66-ab-taxable-income.l4`.

**A4 — ages are by tax year.** A child's "age in the tax year" is the tax year less the tax year of birth, as s 40(b)(3)'s definitions make every band of (c)(4)(a) and (c)(5).

**A5 — the amounts are the caller's.** Every amount is taxable income in shekels, already classified by the caller.

## 4. Fork register

Each fork: the readings, the one taken, and the text that licenses each.
None has been settled by a court or the Tax Authority to my knowledge; I did not search case law.

| id | where | readings | taken | why |
| --- | --- | --- | --- | --- |
| F1 | (d)(1), line 2479 | (i) the gate is on the COUPLE: where conditions fail, (a) does not apply to them at all; (ii) it is on the INCOME from the common source only | (i) | "הוראות סעיף קטן (א) יחולו לגבי בני זוג שיש להם מקור הכנסה משותף, רק אם …" names spouses, not income. For (ii): s 64B(b), line 2441, speaks of "הכנסה ממקור הכנסה משותף לפי סעיף 66(ד) שלא מתקיימות לגביה הוראות אותו סעיף", and s 67(a) applies (d) to farm income. |
| F2 | (a)(1) proviso, line 2456 | is a sum received on commuting a pension (s 1 def. para (6)) a "קיצבה" for the proviso? | no | para (6) calls it "סכום המתקבל עקב היוון קיצבה", distinguishing it from the pensions of paras (1)-(4); (5) and (7) are a grant and rent. |
| F3 | (a)(2), line 2457 | spouses with EQUAL non-zero income from personal exertion: neither sentence answers | refuse | "גבוהה יותר" presupposes one is higher; the second sentence covers only "no income". Not filled with a guess. |
| F4 | (a)(2) | is the comparison on the spouse's whole personal-exertion income, or only what is calculated separately? | whole | "הכנסתו החייבת מיגיעה אישית" is not qualified. The other reading would exclude a pension the (a)(1) proviso keeps on the registered spouse. |
| F5 | (a)(3), line 2458 | "ילדו": the registered spouse's own child only, or any child of the couple? | own child | the possessive is singular and attached to "בן הזוג הרשום". A child of the other spouse alone is not reached. |
| F6 | (a)(3) | does s 65's exception (assets from inheritance, or compensation or insurance for bodily injury) apply? | no | (a)(3) restates s 65's child rule without the exception and imports only s 65's meaning of "ריבית". The opposite reading: (a)(3) is s 65's rule under s 66, and the exception travels with it. |
| F7 | (b) proviso, line 2459 | "הכנסה אחרת לגביה נערך חישוב מס נפרד": only the (a)(1) calculation of the other spouse; or also the registered spouse's income once (a) applies, or a (1A) request | (a)(1) only | the registered spouse's income is assessed on him under s 65 as modified, and s 66 calls only the other spouse's calculation "חישוב נפרד". So a registered spouse's claimed (b) income is always calculated on its own. |
| F8 | (c)(1A), line 2462 | is a (1A) request shut by the (d) gate? | no | (d) gates "סעיף קטן (א)"; (1A) is in (c). The opposite reading: (c) states provisions for "the separate calculation", which (a) creates, so (d) reaches it indirectly. |
| F9 | (c)(4)-(6) | a couple of the same sex: who is "האשה", who is "הגבר"? | refuse | the definite articles presuppose one of each; the text does not say. (c)(3), which does not turn on sex, still answers. |
| F10 | (c)(1)-(4) | a provision (c) does not name (ss 39A, 39B, 40A-40D, 44, 45, 46, …) | refuse | s 66 is silent; the provision's own wording decides, outside this slice. |
| F11 | (c)(4)(a1), line 2467 | does the election reach a step-mother's points under (4A)? | no | "אמו של ילד": the child's mother. |
| F12 | (c)(4A), (6), lines 2472, 2478 | a partner's children from an earlier marriage that ended other than by death | not counted | the paragraphs say "לאלמן" / "לאלמנה". |
| F13 | (c)(1A), (4), (5) | "כנגד המס החל על הכנסתה מיגיעה אישית": a cap on the children's credit, or only an ordering? | a cap: the credit is the lesser of points × value and that tax | a credit point is "המקוזז כנגד המס" (s 33A); naming one tax confines the set-off to it. The ½ under s 36A precedes "ובנוסף" and is not confined. |
| F14 | (a)(2) with (a)(3) | does the children's (a)(3) income, once deemed the registered spouse's, join the (a)(2) pool and move with it? | no: it stays on the registered spouse | (a)(3) says whose income it is, specifically; reading it into the pool would let (a)(2) send it to the other spouse, contradicting "בן הזוג הרשום". |
| F15 | (a)(3) | "שטרם מלאו לו בשנת המס 18 שנים": a child who turns 18 during the year | excluded | read as "has not turned 18 by the end of the tax year"; age in the year at most 17. |
| F16 | (c) chapeau with (c)(4), (5) | once (a)(1) gives a separate calculation, does (c) govern the registered spouse's calculation too? | yes | (c)(1) says "לכל אחד מבני הזוג", and (c)(4)/(5) speak of the woman and the man, one of whom is the registered spouse. |
| F17 | (c)(4), (5) | must the child be maintained by, or live with, the spouse (as s 40(b)(1) requires)? | no condition | (c)(4) and (5) say only "ילדיה" / "ילדיו". |
| F18 | (c)(1A) | does "בן זוג" include the registered spouse? | yes | the paragraph says "בן זוג", not "בן זוג שאיננו בן זוג רשום" as (a)(1) does, and it would otherwise add nothing to (a)(1). |

**A consolidation oddity, not a fork.**
The definitions of "שנת לידה" and "שנת בגרות" appear twice: inside (c)(4)(a) at line 2466 ("לעניין זה ולעניין פסקה (5) …") and again as an unnumbered line after (c)(4)(d) at line 2471 ("לענין זה …").
Both refer to s 40(b)(3) and say the same thing, so nothing turns on it; the second is probably a survivor of an earlier layout of the paragraph.

## 5. Answer table: the children's credit points under s 66(c), tax years from 2024

Age = the tax year less the child's tax year of birth.

| age in the tax year | the woman, (c)(4)(a), line 2466 | the man, (c)(5), lines 2474-2476 | ITA circulars (section 7) |
| --- | --- | --- | --- |
| 0 (year of birth) | 2½ — or 1½ if she elects under (a1), line 2467 | 2½ — (5)(a) | 2.5, each parent |
| 1 | 4½ — or 5½ after the (a1) election | 4½ — (5)(b) | 4.5 |
| 2 | 4½ | 4½ — (5)(b) | 4.5 |
| 3 | 3½ | 3½ — (5)(b) | 3.5 |
| 4, 5 | 2½ | 2½ — (5)(b) | not printed |
| 6 to 17 | 2 | 1 — (5)(c) | woman 2, man 1 |
| 18 (year of majority) | ½ | 0 — no row | not printed |
| 19 and over | 0 | 0 | — |

Through (4A) a woman married to a widower has the woman's column, without the (a1) election, for each of his children; through (6) a man married to a widow has the man's column for each of hers.
Beside the children's points, (c)(4) gives the woman ½ under s 36A, and (c)(2) gives ½ (not 1) to a spouse whom s 37 would give a point.

## 6. What `check.sh` prints

Run on 2026-10-06 as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
The binary has no `--version`; it resolves to a cabal-store build `jl4-0.1-0ee0100b`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
`JL4_LIBRARY_PATH` unset; the embedded standard library was used.

```
module                                    errors satisfied  failed  refused  expected
ito66-a-separate-calculation.l4                0         0       0        0         0
ito66-ab-taxable-income.l4                     0         0       0        0         0
ito66-b-property-income.l4                     0         0       0        0         0
ito66-c-credit-points.l4                       0         0       0        0         0
ito66-d-common-source.l4                       0         0       0        0         0
ito66-fixtures.l4                              0         0       0        0         0
ito66-nouns.l4                                 0         0       0        0         0
ito66-tax-years.l4                             0         3       0        0         0
ito66-tests-ita.l4                             0        23       0        0         0
ito66-tests.l4                                 0       139       0        0         0
TOTAL (10 modules)                             0       165       0        0
```

No assertion is expected to fail; no module is listed in `expected_red`.
"refused 0" counts plain `#ASSERT`s that refused; the 11 `#ASSERT REFUSED` directives that test a refusal (1 in `ito66-tax-years.l4`, 8 in `ito66-tests.l4`, 2 in `ito66-tests-ita.l4`) are among the 165 satisfied.
Every expected value was written from the source text before the rule was run; all passed on their first run, which is evidence that the tests and the code share one reader, not that both are right (section 8).
As a control that the harness can fail, a scratch copy outside this directory asserted three wrong values and a refusal of a value-producing rule: all four were reported as failures.

## 7. Aids consulted, with provenance

Neither is a source of law; both were used only to date the text (A1) and as a second test oracle (`ito66-tests-ita.l4`).
`curl` received a Cloudflare challenge page, so both were fetched in a browser session; the sha256 is of the bytes that session received, and the text was extracted in the page with pdf.js 4.0.379.

| document | URL | retrieved (UTC) | bytes | sha256 |
| --- | --- | --- | --- | --- |
| ITA circular 2024-000012, 3 January 2024, "חוק הגדלת נקודות זיכוי להורים במס הכנסה, התשפ״ג–2023" | https://www.gov.il/BlobFolder/dynamiccollectorresultitem/employers-info-030124/he/IncomeTax_employers-info-030124.pdf | 2026-10-06T13:16:27Z | 134,504 | `88f871fb8677de7aa673b03d8ff5aeeeb2525301c7fcbf81c4ac9183530e7290` |
| ITA circular 2024-001090, 26 March 2024, "חוק סיוע להורים לילדים עד גיל שלוש (תיקוני חקיקה), התשפ״ד-2024" | https://www.gov.il/BlobFolder/dynamiccollectorresultitem/employers-info-260324/he/IncomeTax_employers-info-260324.pdf | 2026-10-06T13:16:55Z | 106,995 | `71cf63a3539ab500df36d9dbaaa2216958178d28bf5faf68c28f0170ecef361a` |

Copies are not deposited (the browser session could not hand the bytes to the file system); re-fetch and compare the sha256.
pdf.js returned the Hebrew with most word spaces dropped (`חוק זה יחולרטרואקטיביתהחלמיום1.1.2024`); the few words quoted from the circulars here and in `ito66-tests-ita.l4` have their spaces restored and are otherwise as extracted.

Every Hebrew string quoted from the Ordinance in the modules, `NOTES.md` and `BRIEF.md` was checked mechanically against the deposited file (templates resolved to their display text, each piece between elisions searched for): all are present, apart from labels such as "(ד)(1)" whose spacing differs and citations assembled from the page header (`ס״ח תשפ״ג, 400` plus the title).
Not fetched: the amending Acts at `fs.knesset.gov.il/24/law/24_lsr_624898.pdf`, `25/law/25_lsr_2301411.pdf`, `25/law/25_lsr_2656507.pdf`, `25/law/25_lsr_4239836.pdf` (geographic block).

## 8. Open questions for a domain expert

1. F1: is the (d) gate on the couple or on the common-source income? It decides whether a couple with a failing common source loses the separate calculation of unrelated salary too.
2. F3: what does the Tax Authority do with equal incomes from personal exertion under (a)(2)?
3. F6 and F14: does s 65's inheritance / bodily-injury exception apply under (a)(3), and does a child's income move with the (a)(2) pool?
4. F7: may a registered spouse's (b) income be joined to anything, or is it always alone?
5. F8 and F18: is (c)(1A) a route for the registered spouse, and does (d) reach it?
6. F9: how are (c)(4)-(6) applied to a same-sex couple in practice?
7. F13: is the children's credit capped at the tax on personal-exertion income, or may the excess be set against tax on other income?
8. F10: which unnamed credit provisions (ss 39A, 39B, 40A-40D, 44, 45, 46) apply to each spouse in a separate calculation?
9. The text before 2024: encoding the earlier vintages needs the amending Acts (ס״ח 3048 and 3184, and earlier), which this run could not fetch.

Recommended next step: the independent test pass of the encoding skill (`references/second-pass.md`), in a fresh session given only `BRIEF.md` and the source, then a refuter on the (a)/(b) assembly, where the forks concentrate.

## 9. Nouns to reconcile at IL-07

Read from the sibling directories on 2026-10-06, read-only; nothing imported.

- **The person.** IL-01 declares `Individual` (`ito-credit-points-nouns.l4`) with `a woman` as a BOOLEAN; this row declares `A spouse` with `sex` IS A `Sex` (`a woman` | `a man`). Same person, two shapes; the constructor `a woman` here and IL-01's field `a woman` will also collide by name if both modules are imported together.
- **Residence.** IL-01 declares `an Israeli resident in the tax year` on `Individual`; this row does not declare residence at all, because s 66 does not test it.
- **Income items.** IL-03 declares `An item of income` (`amount`, `from personal exertion` BOOLEAN, …) inside `An individual in a tax year`; this row declares `An item of income from personal exertion` (`kind`, `taxable amount`) and keeps income not from personal exertion as one NUMBER on `A spouse`. Same items, different granularity: this row needs the s 1 paragraph of each item for the (a)(1) pension proviso.
- **The tax year.** IL-03's `An individual in a tax year` and this row's `Spouses in a tax year` both have a field `tax year` (NUMBER); two record fields of one name in one import scope are ambiguous in L4.
- **The credit point and the tax.** The value of a credit point is a GIVEN here; IL-01's `ito-s33a-credit-point.l4` is where it is computed. The tax on income from personal exertion is a GIVEN here; IL-03's s 121 module computes tax, and whether it yields the tax on income from personal exertion alone, the figure (c)(4)-(5) needs, is for IL-07 to check.
- **Pension points** (s 40(a), "נקודת קיצבה"): IL-03 declares `A pension-point amount in a tax year`; this row only records that (c)(3) gives them to the registered spouse alone.

## 10. Semi-cleanroom

Nothing under `/Volumes/transcend/src/Axiom/`, no `rulespec-*`, no Axiom Foundation repository or encoding, no `ENCODING-GAPS.md`, no `.axiom/`, no `tax-benefit-source-map.json`, and no `specs/research/AXIOM-*` was read, searched or fetched.
The one web search was restricted to gov.il, knesset.gov.il and taxes.gov.il and asked for the commencement of the 5784 amending Act.
