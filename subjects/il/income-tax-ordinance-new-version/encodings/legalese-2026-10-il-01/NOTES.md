# IL-01: Income Tax Ordinance ss 33A, 34, 36, 36A (credit points) — notes

Row `legalese-2026-10-il-01`, run `IL-01-20261006`, encoder `enc-il-01` (one session, no sub-agents).
Status: **draft**. No domain expert has read it against the source; HG1 not sought.

Read this file first.
The brief is `BRIEF.md`; the self-check is `check.sh`; `render_source.py` renders source lines and checks every Hebrew quotation in the modules against the deposited text.

## 1. What is encoded, and what is not

Encoded: Income Tax Ordinance [New Version] s 33A (the definitions of a credit point, "נקודת זיכוי", and of an allowance point, "נקודת קיצבה"), s 34 (two points for an individual who was an Israeli resident in the tax year), s 36 (a quarter point, "as a travel credit", for an Israeli resident individual) and s 36A (half a point for a woman), from the Hebrew Wikisource consolidation deposited at `../../registers/source-bundle/` (retrieved 2026-10-06, sha256 `b87f2cf4…b81b6`).

Not encoded, and taken as inputs: the year's indexed value of a credit point (s 120B, row IL-03), the tax against which the credit is set off (s 121 and its neighbours, row IL-03), whether an individual was an Israeli resident in the tax year (the s 1 definition), and whether an individual is a woman, a foreign worker, or an Area resident who is not an Israeli citizen.

Reached and refused: s 48 (an order of 5755-1995 extends ss 34 and 36 to Area residents who are not Israeli citizens) and s 48A (regulations of 5775-2014 may take the Chapter's credits from a foreign worker).
Where either could decide the case, ss 34, 36 and 36A refuse with a named reason; everywhere else they answer.

Not a total: the aggregates are named for the sections they add ("under sections 34 and 36", "under sections 34, 36 and 36A").
A person's total credit points also include ss 35, 37–40D, 45 and others (row IL-08), and ss 41 and 66 rework the points for spouses (rows IL-08, IL-02).

**Tax years (an assumption, not ruled).**
The slice's own text carries no dated arm, so no rule takes a date and the rule-version mechanism is not used.
The amendment lists in the section headings end at תשס״ד־2 (s 33A, 5764 = 2003–04), תשל״ה־2 (s 34), תשל״ז־4 (s 36) and תשנ״ו (s 36A); on that record — which I have not checked against the amending Acts — the text encoded here has stood since 5764, and the encoding answers any tax year since then for which the caller supplies the point value.
It has been exercised only at the 2025 value (NIS 2,904, published) and checked against the monthly figure for 2024, 2025 and 2026 (NIS 242, published).
For 2025–2027 s 120B(e)(1) (line 4344, row IL-03) freezes the figure at its 1 January 2024 value, which is consistent with the three booklets printing the same monthly 242.

| module | lines | what it holds |
| --- | ---: | --- |
| `ito-credit-points-nouns.l4` | 52 | `Person` (an individual, or a body of persons) and `Individual` (four facts); `DECLARE` only |
| `ito-s33a-credit-point.l4` | 103 | s 33A: the 504 constant, points to an amount, the set-off, the allowance point |
| `ito-s34-s36-s36a-credits.l4` | 237 | ss 34, 36, 36A, each as written and as reached by ss 48 and 48A; the two aggregates; the `@export` |
| `ito-credit-points-published-figures.l4` | 77 | Israel Tax Authority figures, labelled as published figures and not law |
| `ito-credit-points-tests.l4` | 227 | 58 assertions, every expected value from the source |

## 2. Coverage table

Every provision this row met, with its disposition.
Line numbers are lines of `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` (sha256 `b87f2cf437ccfed35c3164681f4fc7ee015a111633454622751930c8894b81b6`).

### In scope

| provision | heading / words | lines | disposition | where |
| --- | --- | --- | --- | --- |
| s 33A chapeau | "בפרק זה –" | 1562 | encoded | `ito-s33a-credit-point.l4`, `§§ Section 33A`: by placement under the Chapter's heading, with a comment; the confinement changes no answer here because every rule that uses the definitions is in the Chapter |
| s 33A "נקודת זיכוי" limb 1 | an amount of NIS 504 for a tax year | 1563 | encoded | `the amount of a credit point as written in section 33A, before indexation` (504); `the amount of … credit points at a credit-point value of …` |
| s 33A "נקודת זיכוי" limb 2 | indexed "כאמור בסעיף 120א" | 1563 | out-of-scope | The indexation is s 120B's (row IL-03); the year's indexed figure is the input `the value of one credit point`, with no default. Fork F6 records that the cross-reference names s 120A. |
| s 33A "נקודת זיכוי" limb 3 | "המקוזז כנגד המס לאותה שנה" | 1563 | encoded | `the tax for the year after setting off … against …`; fork F5 |
| s 33A "נקודת קיצבה" | the credit point at 31.12.1996, adjusted under s 120B, divided by twelve | 1564 | encoded | `the amount of an allowance point, given …`: limb (3), the division, is encoded; limbs (1)-(2) are one figure s 120B produces (row IL-03), taken as the input |
| s 33A editorial notes | Wikisource figures for 1987, 2023, 2024–2027; pointer to the ITA simulator | 1563, 1564, 1567 | inert | Quoted in comments and marked "NOT statute text, NOT used". Two of the figure pairs are used in tests only as hypothetical inputs for the division by twelve, labelled as such. |
| s 34 | זיכוי לתושב ישראל — two points | 1569–1570 | encoded | `ito-s34-s36-s36a-credits.l4`, `§§ Section 34`: `section 34, as written, applies to`, `section 34 applies to`, `the credit points under section 34 for` |
| s 36 | זיכוי בעד נסיעה למקום ההשתכרות — a quarter point | 1593–1594 | encoded | `§§ Section 36`: the same three rules; forks F2, F3 |
| s 36A | זיכוי לאשה — half a point | 1596–1597 | encoded | `§§ Section 36A`: the same three rules; fork F1 |

### Definitions in s 1 that the slice uses

| provision | words | lines | disposition | reason |
| --- | --- | --- | --- | --- |
| s 1 "אדם" | "לרבות חברה וחבר בני־אדם" | 108 | encoded | `ito-credit-points-nouns.l4`: `Person IS ONE OF \`an individual\` …, \`a body of persons\`` |
| s 1 "חבר בני אדם" | a public body, company, association … | 124 | encoded | the constructor `a body of persons`, which has no facts and gets no points under ss 34, 36 or 36A |
| s 1 "תושב ישראל" (a), individuals | centre of life, the 183-day and 30/425-day presumptions, rebuttal, the Minister's power | 143–163 | out-of-scope | The definition is a whole regime of its own: an evaluative "centre of life" test over family, economic and social ties, two rebuttable day-count presumptions that either the individual or the assessing officer may displace, and regulations of 5766-2006 under para (4) that deem some individuals resident and others not. Whether a person was resident in a tax year is the gateway fact of nearly every computation in the Ordinance, not a question this slice owns, so the encoding takes the status as determined under s 1 as an input and encodes none of the test. Encoding the presumptions alone would answer a rebuttable question as if it were conclusive. |
| s 1 "שנת מס" | twelve months from 1 January, or a special assessment period | 202 | out-of-scope | The slice never computes a period: a tax year enters only as the label of the published credit-point figure, and special assessment periods (the second limb) do not reach any rule here. |

### Reached by a rule in scope, not encoded: the rule refuses

| provision | words | lines | disposition | reason |
| --- | --- | --- | --- | --- |
| s 48 | זיכויים לתושבי האזור — the Minister may by order apply ss 34, 36 and 37 to Area residents who are not Israeli citizens "as if they were Israeli residents" | 1806–1808 | out-of-scope, refused | Assigned to IL-08 as a credit section, and its order (5755-1995, known here only from the Wikisource note at line 1808) is not in the source bundle. A rule in this row reaches it exactly when an individual who is not an Israeli resident is an Area resident and not an Israeli citizen: ss 34 and 36 then refuse with `section 48 and the order made under it are not encoded in this model`. s 48 does not name s 36A, so s 36A never reaches it. |
| s 48A | זיכויים לעובד זר — the Minister may disapply the chapter's credits, wholly or partly, to a foreign worker "even if treated as a resident" | 1810–1812 | out-of-scope, refused | Assigned to IL-08 as a credit section; the Regulations of 5775-2014 (line 1812) are not in the source bundle. The power can only remove or reduce credits, so a rule reaches it only where ss 34, 36 or 36A would otherwise give a foreign worker points, and there it refuses with `section 48A and the regulations made under it are not encoded in this model`; where the section gives a foreign worker nothing anyway, the answer 0 stands. |

### Out of scope

| provision | heading | lines | disposition | reason |
| --- | --- | --- | --- | --- |
| s 35 | זיכוי לעולה | 1572–1588 | out-of-scope | Assigned to IL-08 by the lead. The new-immigrant credit is a month-by-month schedule over 42 or 54 months with two dated regimes (immigration before 2022 and from 2022), a spouse rule in (b), an absence rule in (c), a definition of "עולה" and "תושב חוזר" in (d), and a ministerial power in (e). It shares only the unit (a credit point) with this slice. |
| s 35A | (repealed) | 1590–1591 | out-of-scope | Repealed; a section number with no text under it. Listed so the numbering has no silent gap. |
| s 37 | זיכוי בעד בן־זוג | 1599–1600 | out-of-scope | Assigned to IL-08. A further point for a "יחיד מוטב" who proves to the assessing officer that a spouse was maintained, turning on retirement age, blindness and disability under s 9(5). It is also conditioned on proof "להנחת דעתו של פקיד השומה", a condition ss 34, 36 and 36A do not carry. |
| s 38 | זיכוי בעד בן זוג עובד | 1602–1604 | out-of-scope | Assigned to IL-08. Applies in a joint computation of a registered spouse; it gives "1⁄4 נקודת זיכוי לפי סעיף 36" for a working spouse's income and is cited in the fork register (F2) as evidence about s 36, but it is not encoded. |
| s 39 | זיכוי בעד בן־זוג עוזר | 1606–1608 | out-of-scope | Assigned to IL-08. A spouse who works in the other spouse's business. |
| s 39A | זיכוי לחייל משוחרר | 1609–1618 | out-of-scope | Assigned to IL-08 as one of "the other credit sections": a discharged soldier's credit: a fraction of a point for each of the 36 months after regular service ends, the fraction scaled by the length of service (line 1610–1611). |
| s 39B | זיכוי בעד שירות מילואים כלוחם | 1619–1630 | out-of-scope | Assigned to IL-08 as one of "the other credit sections": a credit in the following tax year for combat reserve duty, scaled by days served (line 1620–1621); its heading lists one amendment, תשפ״ו. |
| s 40 | נקודות קיצבה וזיכוי בעד ילדים | 1631–1647 | out-of-scope | Assigned to IL-08 as one of "the other credit sections". It is the main consumer of the "נקודת קיצבה" defined in s 33A, which this row does encode; s 40 itself (which parent gets which points for which child in which year) is not encoded here. |
| ss 40A–40D | credits for a remarried divorcee, a youth, an academic degree, a vocational qualification | 1648–1682 | out-of-scope | Assigned to IL-08 as "the other credit sections". Each has its own conditions and years; none modifies ss 34, 36 or 36A. |
| s 40E | מניעת כפל | 1683–1685 | out-of-scope | An election between s 40C and s 40D; it does not touch ss 34, 36 or 36A. |
| s 40F | (expired) | 1686–1687 | out-of-scope | Expired ("פקע"); listed so the numbering has no silent gap. |
| s 41 | בן זוג שהיה נשוי חלק מהשנה | 1689–1693 | out-of-scope | Assigned to IL-08. It CONSUMES this slice: a non-registered spouse married for part of the year gets "1⁄12 מנקודות הזיכוי לפי סעיפים 34, 36, 40(ב) ו־40ב" for each unmarried month. It does not change what ss 34 and 36 say, so this row's answers stand and s 41 multiplies them; a caller asking about such a spouse must apply s 41 on top. |
| s 41A | דיווח לכנסת | 1694–1696 | out-of-scope | A reporting duty on officials to the Knesset Finance Committee by 30 June 2019; not a rule about any taxpayer. |
| ss 42, 43 | (repealed) | 1697–1702 | out-of-scope | Repealed; listed so the numbering has no silent gap. |
| ss 44–46C | institutional care, incapacitated persons, insurance premiums, donations | 1703–1762 | out-of-scope | Credits computed as a percentage of an expense rather than in credit points (s 44, 35%, line 1704; s 45A, 25%, line 1715; s 46, 35%, line 1745), or in points with their own conditions (s 45, two points per qualifying child, line 1708). Assigned to IL-08 as "the other credit sections"; none modifies ss 34, 36 or 36A. ss 45B and 46C are repealed. |
| ss 47–47C | deductions for pension and national-insurance payments | 1763–1805 | out-of-scope | Deductions (ניכויים) from income, not credits against tax; outside this row and not credit points at all. s 47B is repealed. |
| s 57 | המס בקיבוץ שיתופי | 1869–1883 | out-of-scope | Applies "סעיפים 34 עד 46א ו־47" to a kibbutz's members as if its income were divided among them; a consumer of this slice in a special regime (Part D). |
| s 66 | חישוב נפרד | 2454–… | out-of-scope | Row IL-02. In a separate computation each spouse is entitled to the credit points of ss 34 and 36 (s 66(c)(1), line 2461), and "האשה תהא זכאית ל־1⁄2 נקודת זיכוי לפי סעיף 36א" (s 66(c)(4), line 2465). This row's rules are what s 66 applies per spouse. |
| s 120A | הגדרות (Part 6.1) | 4327–4335 | out-of-scope | The definitions of Part 6.1. s 33A's cross-reference "צמוד למדד כאמור בסעיף 120א" lands here, where the definition of "מדד" has been deleted; see fork F6. Not assigned to a row I know of. |
| s 120B | הצמדה | 4337–4345 | out-of-scope | Row IL-03. Fixes the indexed value of a credit point and of an allowance point each 1 January, freezes it for 2025–2027 at its 1 January 2024 value (s 120B(e)(1), line 4344), and is the source of the number this row takes as a `GIVEN`. |
| s 121 | שיעור המס ליחיד | 4349–4451 | out-of-scope | Row IL-03. Produces "the tax" against which s 33A says the credit-point amount is set off; this row takes that tax as a `GIVEN`. |
| ss 55(b), 60A(2) | a kibbutz member's assessment on income not passed to the kibbutz | 1864, 1916 | out-of-scope | Consumers in a special regime: in such an assessment the credit points already used in the kibbutz's assessment are not counted again. |
| s 91(e)(1), (e)(2)(b) | spreading a real capital gain over up to four tax years | 3381, 3384 | out-of-scope | A consumer: the tax on each year's slice is computed taking into account "יתרת נקודות הזיכוי" (the balance of credit points) for that year. Cited in fork F5 as evidence that an unused balance of credit points exists, that is, that the set-off is limited by the tax. |
| s 135(1)(a) | the assessing officer's power to demand returns, including of children "שהם זכאים בעדם לנקודות זיכוי" | 4878 | out-of-scope | Mentions credit points only to identify whose capital may be demanded in a return; no effect on the points. |
| s 134A(2) | exemption from filing below three times "סכום נקודות הזיכוי שעל פי סעיפים 34 ו־36" | 4864 | out-of-scope | A consumer. The aggregate it names is provided by this row as its own rule, because the Ordinance names it; s 134A itself (a ministerial power to exempt from filing) is not encoded. |


## 3. Fork register

Every place the text bore more than one reading, the readings, the one taken, and the words that license each.
None of these has been settled by a court or the Tax Authority to my knowledge; I did not search case law.

**F1 — does s 36A require residence?**
Text, line 1597: "בחישוב המס של אשה תובא בחשבון 1⁄2 נקודת זיכוי."
Reading A: no; any woman whose tax is computed gets half a point.
Reading B: yes; the personal credit points are for Israeli residents, and s 36A should be read with ss 34 and 36 beside it.
For A: s 34 says "יחיד שהיה תושב ישראל בשנת המס" and s 36 "יחיד תושב ישראל", so where the legislature wanted residence in this run of sections it said so; and s 48 (line 1807), which lets an order extend credits to non-resident Area residents "as if they were Israeli residents", lists ss 34, 36 and 37 and not s 36A, which is what one would expect if s 36A needed no extending.
For B: the shared context of the Chapter's personal credits; Tax Authority practice, which I have not sourced.
**Taken: A**, because the operative words impose no residence condition and the two textual signals point the same way.
Effect: a non-resident woman gets 0.5 points under this row (tests at `§§ Section 36A — illustrations`). Open question Q1.

**F2 — does s 36 require earning, or travel to a place of earning?**
Text: heading "זיכוי בעד נסיעה למקום ההשתכרות" (line 1593); body "בחישוב המס של יחיד תושב ישראל תובא בחשבון 1⁄4 נקודת זיכוי כזיכוי נסיעה." (line 1594).
Reading A: no; every resident individual gets the quarter point, and "as a travel credit" only names it.
Reading B: only an individual with income from personal exertion (who travels to earn it).
For B: the heading; and s 38(a) (line 1603), which in a joint computation gives "1⁄4 נקודת זיכוי לפי סעיף 36" for the other spouse only once it is proved that spouse's income is from personal exertion — suggesting the legislature linked the s 36 quarter point to earning.
For A: the body has no such condition; s 38(a)'s condition belongs to s 38's own joint-computation regime and is stated there, not in s 36; and, weakly, s 134A(2) (line 4864) measures the income of people with no income from work, business or profession against "סכום נקודות הזיכוי שעל פי סעיפים 34 ו־36" — weak because a yardstick need not be anyone's entitlement.
**Taken: A.** Open question Q2.

**F3 — the residence limb of s 36 has no "in the tax year".**
s 34: "שהיה תושב ישראל בשנת המס"; s 36: "יחיד תושב ישראל".
Reading A: the same test — resident for the tax year whose tax is computed — because s 1's definition determines residence by reference to a tax year (the presumptions at lines 151–153 are "בשנת המס").
Reading B: residence at some other moment (when the tax is computed).
**Taken: A**; both sections read the one field `an Israeli resident in the tax year`.

**F4 — part-year residence.**
"שהיה תושב ישראל בשנת המס" could mean resident for the tax year as a whole (s 1 decides one status per year) or resident at any time during it; and the sections say nothing about apportioning the points for part of a year (contrast s 41, line 1691, which apportions ss 34 and 36 by months for a spouse married part of the year).
**Taken:** residence is one status per tax year, supplied by the caller, and the points are never apportioned by this row. If the Tax Authority apportions for a person who becomes or ceases to be resident during the year, it does so under some provision this row has not met. Open question Q3.

**F5 — what "המקוזז כנגד המס לאותה שנה" does when the credit exceeds the tax.**
Reading A: the credit reduces that year's tax to no less than zero; the excess is not refunded and not carried to another year.
Reading B: the excess is refunded (a negative tax).
For A: "set off against" extinguishes a debt up to its amount; "לאותה שנה" ties it to that year; s 91(e)(1) and (e)(2)(b) (lines 3381, 3384) speak of "יתרת נקודות הזיכוי", a balance of credit points left unused in a year, which exists only if the set-off is capped by the tax; and the Tax Authority describes a credit point as "סכום המופחת מהמס", an amount deducted from the tax ([itc135-2025] p. 4).
**Taken: A**, `max 0 (tax − amount)`.
Not decided here: the order in which several credits are set off against one year's tax, which matters as soon as any other credit is in play.

**F6 — the cross-reference in s 33A points at s 120A.**
s 33A: "צמוד למדד כאמור בסעיף 120א" (line 1563).
s 120A (lines 4327–4335) is the definitions section of Part 6.1, and its definition of "מדד" is deleted ("(נמחקה)", line 4329); the provision that actually indexes "סכומי נקודת זיכוי" is s 120B(a) (line 4338), and "מדד" is defined in s 1 (line 179).
Readings: the reference is to Part 6.1 as a whole (in practice s 120B), or it is a stale reference.
**Taken:** s 120B governs, and the result does not change any answer here, because the indexed figure is an input either way. Recorded because a reviewer reading s 33A alone will look in the wrong section.

**F7 — the editorial figures are not law.**
The notes inside `{{ח:הערה|…}}` at lines 1563 and 1564 give "נקוב לשנת 1987" and figures for 2023 and 2024–2027.
They are Wikisource's, not the Knesset's, and are used nowhere as values.
Two of them appear in tests as hypothetical inputs to the division by twelve (2,820 → 235; 2,904 → 242), labelled as such; both pairs are consistent with "ומחולק בשנים עשר".

**F8 — no claim, no proof.**
ss 34, 36 and 36A say the points "יובאו בחשבון" / "תובא בחשבון" (shall be taken into account), with no claim and no proof "להנחת דעתו של פקיד השומה" — which s 37 (line 1600) does require.
**Taken:** an entitlement computed from the facts, not a permission the taxpayer exercises; no deontic rule.

**F9 — "אשה" is not defined.**
Neither s 1 nor Chapter Three defines "woman".
**Taken:** an input fact, `a woman`. A dispute about who counts is outside what the text settles. Open question Q4.

**F10 — what to answer where ss 48 and 48A reach.**
For a non-resident Area resident who is not an Israeli citizen, and for a foreign worker whom ss 34, 36 or 36A would otherwise credit, the answer depends on an instrument not in the bundle.
Readings: (a) answer as if the instrument did not exist (0 for the Area resident; full points for the foreign worker); (b) answer from the Wikisource note's one-line summary of the 1995 order; (c) refuse.
(a) gives a confidently wrong answer whenever the instrument applies; (b) encodes an order from an editor's paraphrase.
**Taken: (c)**, with the refusal placed so that every case the instrument cannot affect still answers (a foreign worker whom the section gives nothing gets 0; an Israeli resident needs no s 48 order).
The refusals are not dated, because no rule here takes a date: for a tax year before the 2014 Regulations the model still declines on a resident foreign worker, where the law then may well have given full points.

## 4. Answer table

Points under each section, for each kind of person, as this row reads the source.
"refused" means the model declines and names the instrument it lacks.

| person | s 34 (l. 1570) | s 36 (l. 1594) | s 36A (l. 1597) | ss 34 + 36 | ss 34 + 36 + 36A |
| --- | ---: | ---: | ---: | ---: | ---: |
| resident man | 2 | 1/4 | 0 | 2 1/4 | 2 1/4 |
| resident woman | 2 | 1/4 | 1/2 | 2 1/4 | 2 3/4 |
| non-resident man | 0 | 0 | 0 | 0 | 0 |
| non-resident woman | 0 | 0 | 1/2 (F1) | 0 | 1/2 |
| body of persons (e.g. a company) | 0 | 0 | 0 | 0 | 0 |
| resident, foreign worker | refused (s 48A) | refused (s 48A) | 0 if a man; refused (s 48A) if a woman | refused | refused |
| non-resident, foreign worker | 0 | 0 | 0 if a man; refused (s 48A) if a woman | 0 | 0 if a man; refused if a woman |
| non-resident Area resident, not an Israeli citizen | refused (s 48) | refused (s 48) | 0 if a man; 1/2 if a woman | refused | refused |
| resident in Israel, also an Area resident and not a citizen | 2 | 1/4 | as for any resident | 2 1/4 | as for any resident |

The credit-point amount, in NIS, at the Tax Authority's published figure:

| tax year | NIS per point, annual | NIS per point, monthly | resident man (2 1/4) | resident woman (2 3/4) | non-resident woman (1/2) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2024 | not sourced (refused) | 242 [booklet-2024 p. 11] | — | — | — |
| 2025 | 2,904 [itc135-2025 p. 4] | 242 [booklet-2025 p. 10] | 6,534 | 7,986 | 1,452 |
| 2026 | not sourced (refused) | 242 [booklet-2026 p. 9] | — | — | — |

The 2025 amounts are the Authority's own rule, "the product of the number of credit points and the value of one credit point", applied to this row's points.
The row does not derive an annual figure from a monthly one; s 120B(e)(1) would make 2026 equal 2024 and 2025, but that is row IL-03's to compute.

## 5. What `check.sh` prints

Run on 2026-10-06 as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, with the binary at `/Volumes/transcend/caches/cabal/store/ghc-9.10.3-fe9c/jl4-0.1-0ee0100b/bin/l4`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118` (it has no `--version`; its file time changed to 21:20 that evening, so another session may have reinstalled it during this run).

```
module                                    errors satisfied  failed  refused  expected
ito-credit-points-nouns.l4                     0         0       0        0         0
ito-credit-points-published-figures.l4         0         0       0        0         0
ito-credit-points-tests.l4                     0        58       0        0         0
ito-s33a-credit-point.l4                       0         0       0        0         0
ito-s34-s36-s36a-credits.l4                    0         0       0        0         0
TOTAL (5 modules)                              0        58       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Every module: 0 errors, 0 failed, 0 refused.
The 58 satisfied assertions are all in the tests module, 9 of them `#ASSERT REFUSED … BECAUSE "…"` pinning a refusal's wording.
No assertion is expected to fail, so `expected_failed` is 0 everywhere and there is no red file.

That the harness can fail was checked on a scratch copy outside this directory: one expected value changed and s 36A's half point replaced by a `REFUSE` produced `1 failed, 8 refused`, `exit=1`.

The only diagnostic besides the results is an environment warning: `l4` reports a second copy of `prelude` in `~/.local/share/jl4/libraries/` and uses the copy compiled into the binary.

`python3 -I render_source.py --check *.l4` reports every Hebrew quotation found verbatim in the rendered source (44 checked, 0 missing).

No independent test pass (skill step 8) has been run: the lead asked for one session without sub-agents.
It is the first thing to add.

## 6. Open questions for a domain expert

- **Q1 (F1).** Does the Tax Authority give the s 36A half point to a woman who is not an Israeli resident? If it does not, on what text?
- **Q2 (F2).** Is the s 36 quarter point given to a resident with no income from personal exertion (a pensioner on passive income, say)?
- **Q3 (F4).** Are ss 34 and 36 apportioned for an individual who becomes, or ceases to be, an Israeli resident during a tax year? Under which provision?
- **Q4 (F9).** Is "אשה" in s 36A read from the population register, or otherwise?
- **Q5 (F5).** Confirm that an excess of credit-point amount over the tax lapses, outside the s 91 spreading regime.
- **Q6.** The 1995 order under s 48 and the 2014 Regulations under s 48A: are they in force in the form the Wikisource notes describe? Row IL-08 should fetch and encode them.

## 7. Nouns to reconcile at IL-07

Observed on 2026-10-06 by reading the sibling directories; nothing here was changed, and nothing imports from them.

- **The woman.** IL-02 (`ito66-nouns.l4`) declares `Sex IS ONE OF \`a woman\`, \`a man\`` as a field `sex` of `A spouse`; this row declares a BOOLEAN field `a woman` on `Individual`. Same fact (s 36A, s 66(c)(4)), two shapes — and the IL-02 constructor and this row's field share the name `a woman`, which will collide if one module imports both.
- **The individual.** This row: `Person IS ONE OF \`an individual\` HAS \`the individual\` IS AN Individual, \`a body of persons\``, with `Individual` carrying residence, sex, Area status and foreign-worker status and no tax year. IL-03 (`ito-il03-nouns.l4`): `An individual in a tax year` with `tax year`, `date of birth`, items of income. IL-02: `A spouse`. Residence in the tax year appears only here.
- **The allowance point.** This row translates "נקודת קיצבה" as "allowance point" (the Chapter's heading is "…וקיצבאות ילדים", child allowances); IL-03 calls it "pension point" (`A kind of amount adjusted under section 120B`). One English name should be chosen.
- **The credit-point value.** IL-03's `A kind of amount adjusted under section 120B` includes `the amount of a credit point`; its output for a tax year is this row's input `the value of one credit point`. At IL-07 the input can be wired to IL-03's rule.
- **s 36A twice.** IL-02's `ito66-c-credit-points.l4` carries its own "one half point under section 36A, by paragraph (4)"; this row's `the credit points under section 36A for` is the same half point from s 36A itself.

## 8. Sources read, and provenance

- The deposited Wikisource source, read-only, by line number as cited (sha256 checked against the `.meta.json` on 2026-10-06).
- Israel Tax Authority publications, fetched 2026-10-06 as Internet Archive captures because gov.il returned a Cloudflare challenge to direct requests; full URLs, capture timestamps and sha256s are in the header of `ito-credit-points-published-figures.l4`. They are not deposited: they are government publications, not among the classes (statutes, regulations, Knesset records, judicial decisions) that s 6 of the Copyright Act 5768-2007 excludes from copyright, so only short quotations are carried.
- The L4 skills (`encoding-a-subject`, `writing-l4-rules` with `drafting-patterns.md`, `gotchas.md` and the `source-patterns/` pages 01, 03, 04 (4.7–4.8), 09 (9.4–9.5, 9.9) and 11), and the commons layout (`canon-deposit.md`) and the HVAC row's `encoding.json` as the worked example.
- The sibling directories `legalese-2026-10-il-02` and `-il-03`, read-only, for section 7 only.
- Not read: anything from the Axiom Foundation or any RuleSpec encoding, under any of the paths the brief forbids. Web searches were limited to the Tax Authority's own figures on gov.il.
