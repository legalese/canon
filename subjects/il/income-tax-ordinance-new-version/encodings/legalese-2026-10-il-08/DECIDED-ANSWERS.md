# Decided answers, row IL-08 (income tax half), independent test author fid-il-08a

Finished (UTC, from `date -u`): Wed Oct  7 00:45:44 UTC 2026. The pre-encoding reading ends at the "Completed" line at the foot of the main body; anything after it is labelled as written later.

Written from the Hebrew source alone, before any `.l4` file, `NOTES.md`, `encoding.json`, `check.sh` or `tools/` in the encoding directory was opened.
The only file in the encoding directory read before this one was finished is `BRIEF.md`, and the only listing was a plain `ls`.

Source: `income-tax-ordinance-new-version.he.wiki.txt`, sha256 `b87f2cf437ccfed35c3164681f4fc7ee015a111633454622751930c8894b81b6` (checked with `shasum -a 256`).
Line numbers below are lines of that file.
Provisions read in full: s 1 (lines 106-204), s 2 (209-245), s 35 (1572-1588), s 37 (1599-1600), s 38 (1602-1604), s 39 (1606-1607), s 40 (1631-1646), s 45A (1714-1739), s 47 (1763-1789), s 64B (2439-2445), s 65 (2447-2448).
Read for context only, because the text in scope points at them: s 33A (credit point, 1561-1564), s 3(ה3)(2) (average wage, about line 313), s 9(5) (631-652), s 66 (2454-2484), s 120A and s 120B (4327-4347), s 121A (4452-4453, repealed: `(בוטל)`).

## Figures I chose (inputs, not law)

No official Israeli publication was fetched.
Every figure below is an input I chose, taken from an **editorial note** (`{{ח:הערה|…}}`) in the unofficial Wikisource consolidation, not from statutory text.
Section 120B(e)(1) (line 4344) is statutory and freezes the indexed amounts for tax years 2025 to 2027 at their 1 January 2024 values: `ב־1 בינואר של שנות המס 2025 עד 2027 לא יתואמו הסכומים … והסכומים באותן שנות מס יהיו כפי שהיו ביום כ׳ בטבת התשפ״ד (1 בינואר 2024)`.
So a 2024-2027 figure in a note is the right kind of number for 2026, provided the note is accurate.

| symbol | meaning | value for tax year 2026 | where the note is |
|---|---|---|---|
| CPV | value of one credit point (s 33A) | 2,904 NIS | line 1563, `בשנים 2024–2027, 2,904 ש״ח` |
| A1 | s 47(a)(1)(1) amount | 116,400 NIS | line 1766 |
| A2 | s 47(a)(1)(2) amount | 164,400 NIS | line 1767 |
| F45 | s 45A(d)(1) amount | 2,268 NIS | line 1726 |
| AW | average wage, monthly (s 47(a)(8), s 3(ה3)(2)) | 13,769 NIS; 16% of the annual total = 26,436.48 (the note prints 26,436) | line 1776 |

Where a test can take a figure as an input, it supplies these values.
Where the encoding hard-codes a figure, a difference from these values is reported as a figure difference, not a legal error.

## Conventions

- Tax year 2026 unless stated.
- "pts" = credit points (נקודות זיכוי). NIS amounts are before any rounding rule (s 120B(d) rounding is outside scope).
- **REFUSE** means: the source in scope does not decide the question, or the answer depends on a provision outside the scope; the right result is a refusal, or a fact taken as an explicit input (I say which I would accept).
- "my reading" marks an answer I am confident the text supports but where another reading is arguable; the alternative is named.

---

## A. Section 1: definitions

| id | facts | expected | provision and words |
|---|---|---|---|
| D001 | A and B are married and live together with a joint household | A is B's spouse (בן זוג) | s 1, line 112: `”בן זוג“ – אדם נשוי החי ומנהל משק בית משותף עם מי שהוא נשוי לו` |
| D002 | A and B are married but live apart, no joint household | not spouses for the Ordinance | same words: both "married" and "lives and runs a joint household" are required |
| D003 | A and B are not married, live together, joint household | not spouses by the text (practice on reputed spouses is outside the text) | same words: `אדם נשוי` |
| D004 | date 2026-12-31 / 2027-01-01 | in tax year 2026 / in tax year 2027 | line 202: `”שנת מס“ – תקופה של שנים עשר חדשים רצופים, שתחילתה ב־1 בינואר` |
| D005 | individual, 183 days in Israel in 2026 | presumption of residence holds | line 152: `אם שהה בישראל בשנת המס 183 ימים או יותר` |
| D006 | 182 days in 2026; 100 in 2025; 100 in 2024 (total 382) | presumption does not hold (neither limb) | lines 152-153 |
| D007 | 30 days in 2026; 200 in 2025; 195 in 2024 (total 425) | presumption holds under (2)(b) | line 153: `30 ימים או יותר, וסך כל … 425 ימים או יותר` |
| D008 | 30 days in 2026; total over three years 424 | presumption does not hold | line 153 |
| D009 | 29 days in 2026; 300 in 2025; 300 in 2024 | presumption does not hold (fails the 30-day leg) | line 153 |
| D010 | presumption holds (D005) but rebutted: centre of life shown to be abroad | not resident | line 155: `החזקה שבפסקה (2) ניתנת לסתירה הן על ידי היחיד והן על ידי פקיד השומה` |
| D011 | no presumption (D006) but centre of life in Israel on the para (1) factors | resident | line 144: `לגבי יחיד – מי שמרכז חייו בישראל` |
| D012 | individual not resident under the "תושב ישראל" definition | foreign resident | line 167: `”תושב חוץ“ – מי שאינו תושב ישראל` |
| D013 | income under s 2(2) | is "employment income" (הכנסת עבודה) | line 121: `”הכנסת עבודה“ – הכנסה לפי סעיף 2(2)` |
| D014 | pension paid by a former employer | personal-exertion income (הכנסה מיגיעה אישית) | line 171, para (1) |
| D015 | interest on a bank deposit (not from personal exertion) | not personal-exertion income | lines 170-178: the list does not include it, and interest is not exertion |
| D016 | rent from an asset used 10+ years to produce personal-exertion income | personal-exertion income under para (7) | line 178 |
| D017 | individual aged 67, male; asked "has he reached retirement age?" | **REFUSE** (or take as an input): retirement age is defined by the Retirement Age Law, outside scope | line 115: `”גיל הפרישה“ – גיל הפרישה כמשמעותו בחוק גיל פרישה` |
| D018 | individual is in a class the Minister of Finance deems resident under para (4) (e.g. a state employee abroad) | **REFUSE**: depends on the 2006 regulations, outside scope | lines 156-163 |
| D019 | individual abroad 183+ days in 2025 and in 2026; centre of life in Israel in those years; not in Israel in 2027 and 2028 | **REFUSE**: the second limb of "תושב חוץ" (`וכן יחיד שהתקיימו בו כל אלה`) can overlap a centre-of-life residence, and the text does not say which prevails, nor for which year the deeming operates | lines 167-169 |

## B. Section 2: sources of income and territorial reach

| id | facts | expected | provision and words |
|---|---|---|---|
| D020 | Israeli resident; employment income produced abroad | taxable under s 2; source s 2(2) | line 210: `על הכנסתו של אדם תושב ישראל שהופקה או שנצמחה בישראל או מחוץ לישראל` |
| D021 | foreign resident; employment income produced in Israel | taxable under s 2 | line 210: `ועל הכנסתו של אדם תושב חוץ שהופקה או שנצמחה בישראל` |
| D022 | foreign resident; income produced and accrued abroad | not taxable under s 2 | line 210, by its terms |
| D023 | Israeli resident; interest accrued abroad | taxable; source s 2(4) | lines 210, 226 |
| D024 | dividend | source s 2(4) | line 226 |
| D025 | annuity / pension (קיצבה) | source s 2(5) | line 229 |
| D026 | rent from a building or land | source s 2(6) | line 232 |
| D027 | income from agriculture | source s 2(8) | line 239 |
| D028 | business profit | source s 2(1) | line 213 |
| D029 | sale of a patent by its inventor, invention outside his ordinary occupation | source s 2(9) | line 242: `אם הומצאה האמצאה … שלא בתחום עיסוקם הרגיל` |
| D030 | same, but the invention is within his ordinary occupation | not s 2(9) | line 242 |
| D031 | gain from a source not in (1)-(9), not expressly excluded, not exempt | source s 2(10) | line 245 |
| D032 | same, but exempt under another law | not s 2(10) | line 245: `ולא ניתן עליו פטור בפקודה זו או בכל דין אחר` |
| D033 | employer reimburses employee's car costs, not allowed to the employee as an expense | employment income s 2(2) | line 216: `תשלומים בשל החזקת רכב … אך למעט תשלומים כאמור המותרים לעובד כהוצאה` |
| D034 | same, but allowed to the employee as an expense | not s 2(2) income | line 216 |
| D035 | gambling or lottery winnings | **REFUSE**: governed by s 2A, outside scope | lines 247-252 |
| D036 | the value of a company car to the employee | **REFUSE** for the figure: set by the Minister's regulations (s 2(2)(b)) | line 217 |
| D037 | where income was produced (Israel or abroad) not stated | **REFUSE**, or an explicit input: place of production is not defined in s 2 | line 210 |

## C. Section 35: new immigrant (עולה)

Months are counted as calendar months, the month of aliyah being month 1, because `”חודש“ – לרבות חלק ממנו` (line 126) makes a part-month a month.
This is my reading; a reader who runs months from the day of aliyah gets different splits across years.
Immigrant resides in Israel throughout unless stated.

Regime for aliyah in 2022 or later (lines 1575-1578): months 1-12 at 1/12 pt; 13-30 at 1/4; 31-42 at 1/6; 43-54 at 1/12; total 8.5 pts over 54 months.
Regime for aliyah before 2022 (lines 1574, 1577-1578): months 1-18 at 1/4; 19-30 at 1/6; 31-42 at 1/12; total 7.5 pts over 42 months.
The split by year of aliyah is carried only in editorial notes (`(חל על עולה שעלה בשנת 2022 ולאחריה)`), not in the operative text; I follow the notes.

| id | facts | expected | provision |
|---|---|---|---|
| D040 | aliyah 2023-03-15; tax year 2023 (months 1-10) | 10/12 = 0.8333 pts | s 35(a)(1) new, line 1575; s 35(c) |
| D041 | same; 2024 (months 11-22) | 2/12 + 10/4 = 2.6667 pts | (a)(1), (a)(1א) |
| D042 | same; 2025 (months 23-34) | 8/4 + 4/6 = 2.6667 pts | (a)(1א), (a)(2) |
| D043 | same; 2026 (months 35-46) | 8/6 + 4/12 = 1.6667 pts | (a)(2), (a)(3) |
| D044 | same; 2027 (months 47-54 then none) | 8/12 = 0.6667 pts | (a)(3); (c) `תקופת 54 החודשים` |
| D045 | same; 2028 | 0 | (c): the year is wholly outside the 54 months |
| D046 | same; sum over all years | 8.5 pts | arithmetic check |
| D047 | aliyah 2021-07-10; 2021 (months 1-6) | 6/4 = 1.5 pts | (a)(1) old, line 1574 |
| D048 | same; 2022 (months 7-18) | 12/4 = 3 pts | (a)(1) old |
| D049 | same; 2023 (months 19-30) | 12/6 = 2 pts | (a)(2) |
| D050 | same; 2024 (months 31-42) | 12/12 = 1 pt | (a)(3) |
| D051 | same; 2025 | 0 | (c): 42 months for pre-2022 aliyah |
| D052 | aliyah 2022-01-01; 2022 (months 1-12) | 1 pt (new regime) | notes `בשנת 2022 ולאחריה` |
| D053 | aliyah 2021-12-31; 2021 (month 1) / 2022 (months 2-13) | 0.25 pts / 3 pts (old regime) | note `לפני שנת 2022` |
| D054 | aliyah 2026-01-20; 2026 (months 1-12) | 1 pt | (a)(1) new |
| D055 | second aliyah (already received the credit on a first aliyah) | **REFUSE**: (c) says `ולא יינתן אלא בפעם הראשונה`, but (e)(1) lets the Minister make rules for former immigrants and such rules were published (line 1588, 1977 rules), outside scope; a flat 0 ignores them | lines 1580, 1586, 1588 |
| D056 | returned to residence 2011-06-01 after 6 consecutive years as a foreign resident | is an עולה (returning resident) | line 1584 |
| D057 | returned 2010-05-16 after 6 years abroad / returned 2010-05-15 | עולה / not עולה (by this limb) | line 1584: `מיום ג׳ בסיוון התש״ע (16 במאי 2010)` |
| D058 | returned 2012-09-30 / returned 2012-10-01 | עולה / not עולה (by this limb) | line 1584: `עד יום י״ד בתשרי התשע״ג (30 בספטמבר 2012)` |
| D059 | returned 2011-06-01 after 5 years as a foreign resident | not עולה by this limb | line 1584: `שש שנים רצופות` |
| D060 | holder of an oleh certificate whose citizenship was revoked under s 10(ד) Citizenship Law | not עולה | line 1582: `אך למעט מי שאזרחותו הישראלית התבטלה` |
| D061 | continuous absence abroad of exactly 6 months, immigrant requests exclusion | may be excluded from the 54 months | line 1580: `שאיננה פחותה מששה חדשים ואיננה עולה על שלוש שנים` |
| D062 | continuous absence of 5 months | may not be excluded | same |
| D063 | continuous absence of exactly 36 months | may be excluded | same |
| D064 | continuous absence of 37 months | may not be excluded | same |
| D065 | person in a class the Minister declared to be treated as an עולה | **REFUSE** (or explicit input): depends on an instrument outside scope (line 1583) | line 1582 |
| D066 | s 35(b): registered spouse, joint computation; non-registered spouse is an עולה, aliyah 2025-01-15 (so 3 pts in 2026, months 13-24 at 1/4); s 38 applies at 1.75 pts (not entitled to קיצבה points); non-registered spouse's income 80,000 | the immigrant points (3) are taken into account; income included | line 1579 |
| D067 | same; non-registered spouse's income 60,000 (threshold 5 x (3 + 1.75) x 2,904 = 68,970) | income not included; the immigrant points not taken into account | line 1579: `איננה עולה על סכום שהוא פי חמישה מסכום נקודות הזיכוי האמורות בסעיף קטן (א) ובסעיף 38` |
| D068 | same; income exactly 68,970 / 68,971 | not included (does not exceed) / included | same words, `איננה עולה על` |

## D. Section 37: spouse credit

"יחיד מוטב" = an individual who, or whose spouse, has reached retirement age, or who, or whose spouse, is blind or disabled within s 9(5)(a) or (a1). Retirement age and the s 9(5) status are facts from outside the scope (D017), taken as inputs.

| id | facts | expected | words (line 1600) |
|---|---|---|---|
| D070 | resident; has reached retirement age; spouse's maintenance on him, proved | 1 pt | `תובא בחשבון נקודת זיכוי אחת` |
| D071 | resident; spouse has reached retirement age, he has not; maintenance proved | 1 pt | `שהוא או שבן זוגו הגיע לגיל פרישה` |
| D072 | resident; blind within s 9(5)(a); maintenance proved | 1 pt | `עיוור או נכה כמשמעותם בסעיף 9(5)(א) או (א1)` |
| D073 | resident; neither retirement age nor blind/disabled; maintenance proved | 0 | not a `יחיד מוטב` |
| D074 | not resident; retirement age; maintenance proved | 0 | `יחיד מוטב תושב ישראל` |
| D075 | resident; retirement age; maintenance not proved | 0 | `שהוכיח להנחת דעתו של פקיד השומה כי בשנת המס שכלכלת בן זוגו היתה עליו` |
| D076 | resident; retirement age; married but living apart (so no בן זוג, D002) | 0 | no spouse to maintain |

## E. Section 38: working spouse

My reading of `יובאו בחשבון 1/4 נקודת זיכוי לפי סעיף 36, 1½ נקודות זיכוי אם הם אינם זכאים …, ו־1¾ נקודות זיכוי אם הם זכאים` (line 1603): three items, the first unconditional, so the total is 1/4 + 1½ = 1.75 pts, or 1/4 + 1¾ = 2.0 pts, plus 1 pt more for a יחיד מוטב.
"הם" ("they") I read as the couple; entitlement to קיצבה points under s 40(a) is an input.

| id | facts | expected | provision |
|---|---|---|---|
| D080 | resident registered spouse; joint computation; spouse's income is employment income of 60,000; couple not entitled to s 40(a) points | 1.75 pts | s 38(a) |
| D081 | same; couple entitled to s 40(a) points | 2.0 pts | s 38(a) |
| D082 | as D080, and he is a יחיד מוטב | 2.75 pts | s 38(a): `ולענין יחיד מוטב … תובא בחשבון גם נקודת זיכוי כאמור באותו סעיף` |
| D083 | as D080 but the spouse's only income is interest | 0 | `הושגה מיגיעתו האישית מעסק או משלח יד או מעבודה` |
| D084 | as D080 but the spouse's only income is rent under para (7) of the s 1 definition | 0 | `כאמור בפסקאות (1) עד (6) להגדרתה` (para (7) excluded) |
| D085 | as D080 but the spouse's income is a pension from a former employer (para (1)) | 1.75 pts | same words, para (1) included |
| D086 | the claimant is the non-registered spouse | 0 | `שהוא בן זוג רשום` |
| D087 | registered spouse not resident | 0 | `יחיד תושב ישראל` |
| D088 | registered spouse, but the spouse's income is not included in his taxable income (separate computation) | 0 | `והכנסתו החייבת כוללת את הכנסת בן זוגו` |
| D089 | s 38(b), not entitled to s 40(a): threshold 5 x 1.75 x 2,904 = 25,410; spouse's income 25,410 | the s 38 points not taken into account (0) | line 1604: `איננה עולה על סכום שהוא פי חמישה מסכום חלקי נקודות הזיכוי האמורות, לפי הענין` |
| D090 | same; spouse's income 25,411 | 1.75 pts | same |
| D091 | s 38(b), entitled to s 40(a): threshold 5 x 2.0 x 2,904 = 29,040; spouse's income 29,040 / 29,041 | 0 / 2.0 pts | same |
| D092 | s 38(b) consequence for income | Textual anomaly: the text says `לא תיכלל הכנסתו של בן הזוג הרשום` ("the **registered** spouse's income shall not be included"), which read literally is absurd. Purposive reading (matching s 35(b), line 1579): the **non-registered** spouse's income is not included in the registered spouse's. Expected: a recorded fork, or a refusal on the inclusion question; the points answer (D089) is unaffected | line 1604 |
| D093 | s 38(b) threshold for a יחיד מוטב: does the s 37 point enter "חלקי נקודות הזיכוי"? | **REFUSE**, or a recorded fork; my reading: no, "חלקי" points to the fractional points only | line 1604 |

## F. Section 39: helping spouse

| id | facts | expected | provision (line 1607) |
|---|---|---|---|
| D100 | resident; spouse helped him at least 24 hours every week during 9 months of 2026 in earning his business income; not entitled to s 40(a) points | 1.5 pts | `לפחות 24 שעות בכל שבוע בתוך 9 חדשים … יובאו בחשבון 1½ נקודות זיכוי אם הוא איננו זכאי` |
| D101 | same; entitled to s 40(a) points | 1.75 pts | `ו־1¾ נקודות זיכוי אם הוא זכאי` |
| D102 | 23 hours a week | 0 | `לפחות 24 שעות` |
| D103 | 24 hours a week but only during 8 months | 0 | `בתוך 9 חדשים` |
| D104 | spouse helped in his employment (he is an employee), not a business | 0 | `מעסק או ממשלח ידו` |
| D105 | as D100 and he is a יחיד מוטב | 2.5 pts | `ולענין יחיד מוטב … גם נקודת זיכוי` |
| D106 | as D100 but not resident | 0 | `יחיד תושב ישראל` |
| D107 | entitled under both s 38 and s 39 for the same spouse, chose s 38 (not entitled to s 40(a)) | s 38: 1.75 pts; s 39: 0 | `יינתנו לו הזיכויים לפי אחד משני הסעיפים, לפי בחירתו` |
| D108 | same, chose s 39 | s 39: 1.5 pts; s 38: 0 | same |
| D109 | same, no choice recorded | **REFUSE** (the choice is the taxpayer's; no default in the text) | same |
| D110 | entitled under both, total for the spouse | never both: total is 1.75 (choosing s 38) or 1.5 (choosing s 39), not 3.25 | same |

## G. Section 40: קיצבה points and children

| id | facts | expected | provision |
|---|---|---|---|
| D120 | how many קיצבה points a resident gets for a child under s 40(a) | **REFUSE** (or input): fixed by the National Insurance Law, outside scope | line 1632: `כקבוע בסעיף 109 לחוק הביטוח הלאומי` |
| D121 | non-resident parent | not entitled to s 40(a) points | line 1632: `יחיד תושב ישראל זכאי` |
| D122 | is the parent "a parent in a single-parent family"? | **REFUSE** (or input): "משפחה חד־הורית" is not defined in the Ordinance (grep finds it only in s 40(b)) | lines 1633-1639 |

### s 40(b)(1): resident single parent, children with him, maintained by him, not entitled to the s 37 point; tax year 2026

"שנת לידה" = tax year of birth; "שנת בגרות" = tax year in which the child turned 18 (lines 1644-1645).

| id | child born in | age reached in 2026 | expected pts | words (line 1633) |
|---|---|---|---|---|
| D130 | 2026 | birth year | 2.5 | `2½ נקודות זיכוי בשל כל ילד בשנת לידתו` |
| D131 | 2025 | 1 | 4.5 | `4½ … החל בשנת המס שלאחר לידתו ועד לשנת המס שבה מלאו לו שנתיים` |
| D132 | 2024 | 2 | 4.5 | same |
| D133 | 2023 | 3 | 3.5 | `3½ … בשנת המס שבה מלאו לו שלוש שנים` |
| D134 | 2022 | 4 | 2.5 | `2½ … בשנות המס שבהן מלאו לו ארבע שנים וחמש שנים` |
| D135 | 2021 | 5 | 2.5 | same |
| D136 | 2020 | 6 | 2 | `ושתי נקודות זיכוי … החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו` |
| D137 | 2009 | 17 | 2 | same |
| D138 | 2008 | 18 (majority) | 0.5 | `ו־½ נקודת זיכוי בשל כל ילד בשנת בגרותו` |
| D139 | 2007 | 19 | 0 | no amount; and `טרם מלאו להם תשע־עשרה שנה` |
| D140 | two children, born 2026 and 2020 | | 4.5 | sum per child |
| D141 | child born 2020, but the parent is entitled to the s 37 point | | 0 | `אך אינו זכאי לנקודת זיכוי לפי סעיף 37` |
| D142 | child born 2020 not living with the parent | | 0 | `בשל ילדיו כאמור הנמצאים אצלו` |
| D143 | parent not resident | | 0 | `יחיד תושב ישראל` |
| D144 | child's maintenance not on the parent | | 0 | `ושכלכלתם היתה עליו` |

### s 40(b)(1א): father, not entitled under para (1); 2026

Default facts: the child lives with the mother, who is resident and entitled under para (1) for that child.

| id | facts | expected pts (father) | words (lines 1634-1637) |
|---|---|---|---|
| D150 | child born 2026 | 2.5 | `(א) 2½ נקודות זיכוי בשנת לידתו של הילד` |
| D151 | born 2024 | 4.5 | `(ב) 4½ …` |
| D152 | born 2023 | 3.5 | `3½ … בשנת המס שבה מלאו לו שלוש שנים` |
| D153 | born 2021 | 2.5 | `2½ … ארבע שנים וחמש שנים` |
| D154 | born 2020 | 1 | `(ג) נקודת זיכוי אחת … החל בשנת המס שבה מלאו לו שש שנים` |
| D155 | born 2009 | 1 | same, `ועד לשנת המס שקדמה לשנת בגרותו` |
| D156 | born 2008 (majority year) | 0 | para (1א) has no majority-year amount |
| D157 | born 2020; the mother is resident and NOT entitled under para (1) for that child | father 0; the 1 pt goes against the mother's personal-exertion income | `ואולם אם אמו … היא תושבת ישראל ואינה זכאית … יובאו בחשבון … כנגד הכנסתה מיגיעה אישית, ולא כנגד הכנסתו של האב` |
| D158 | born 2020; the mother is not resident and not entitled under para (1) | father 1 | the proviso needs a resident mother |

### s 40(b)(1א1), (1ב), (2)

| id | facts | expected | words |
|---|---|---|---|
| D160 | single mother entitled under (1), child born 2025, no election | 2025: 2.5; 2026: 4.5 | line 1638 |
| D161 | same, elects to move one birth-year point to the following year | 2025: 1.5; 2026: 5.5 | line 1638: `נקודת זיכוי אחת … תובא בחשבון בשנת המס שבה נולד הילד או בשנת המס שלאחריה` |
| D162 | "child of one parent" (other parent died in 2020), born 2016 (10 in 2026), surviving parent entitled under (1) | 2 + 1 + 1 = 4 pts (para (1), the additional point of (1ב), and the para (1א)(ג) point) | line 1639 |
| D163 | same, child born 2026 | 2.5 + 1 + 2.5 = 6 pts | line 1639 |
| D164 | same, child born 2008 (majority year) | 0.5 + 1 + 0 = 1.5 pts | line 1639; (1א) has no majority-year amount |
| D165 | two children of one parent, born 2016 and 2018 | my reading: (1) 2+2, (1א) 1+1, one additional point once = 7 pts. Arguable: one additional point per child (8). **REFUSE** or recorded fork acceptable | line 1639: `נקודת זיכוי אחת נוספת` (no `בשל כל ילד`) |
| D166 | "child of one parent": a parent died in the tax year itself | qualifies | line 1642: `נפטר בשנת המס או קודם לכן` |
| D167 | "child of one parent": registered without one parent's details | qualifies | line 1642 |
| D168 | "child of one parent" aged 19 in the tax year | does not qualify | line 1642: `טרם מלאו לו תשע עשרה שנים` |
| D169 | parents live apart; the parent entitled under (1) | 1 additional pt | line 1640: `יקבל ההורה הזכאי לנקודת זיכוי לפי פסקה (1), נקודת זיכוי אחת נוספת` |
| D170 | parents live apart; maintenance divided; the parent not entitled under (1) bears 30% | 0.3 pt (my reading: a fraction of one point equal to the share) | line 1640: `נקודת זיכוי אחת או חלק ממנה לפי חלקו בהוצאות הכלכלה` |
| D171 | parents live apart; maintenance not divided; parent not entitled under (1) | 0 under (2) | same |

## H. Section 45A: credit for insurance and pension contributions

All amounts are NIS for 2026, with F45 = 2,268, A1 = 116,400, AW as above.
"Base" = the amount for which credit is given; credit = 25% of base for life insurance (45A(a)(1)), 35% for pension and survivors' pension insurance (45A(b)).
"Insured income" (הכנסה מבוטחת) is s 47(a)(4); "beneficiary member" (עמית מוטב) is s 47(a)(7); "qualifying income" (QI) is s 47(a)(1) (section I below).
Amounts paid are paid by the individual or the spouse, not the employer.

| id | facts | expected | provision |
|---|---|---|---|
| D180 | employee, not a beneficiary member; employment income 100,000, all insured; pays 6,000 to a pension fund; no other payments; s 47 deduction is nil (D235) | base 6,000; credit 2,100 | s 45A(b) 35%; (d)(2): min(6,000, 7% x 100,000 = 7,000) = 6,000; max with 2,268 = 6,000 |
| D181 | employee, not beneficiary; employment income 200,000, all insured; pays 12,000 pension | QI 116,400; base 7% x 116,400 = 8,148; credit 2,851.80 | (d)(2)(b)(2) |
| D182 | employee, not beneficiary; employment income 20,000 insured; pays 1,800 pension | cap = max(2,268, min(1,800, 1,400)) = 2,268; base 1,800; credit 630 | (d)(1) floor |
| D183 | employee, not beneficiary; employment 100,000 insured; pays only life insurance 6,000; resident | base 5,000 (the 5% proviso); credit 25% = 1,250 | (a)(1), (d)(2)(b)(2) proviso `לביטוח חיים … לא יעלה על 5%` |
| D184 | same as D183 but the individual is not resident | 0 | (a)(1): `אם הוא תושב ישראל` |
| D185 | not resident, employment income 100,000 in Israel, insured; pays 6,000 pension; not beneficiary | credit 2,100: (b) has no residence condition | (b), line 1718 |
| D186 | employee, not beneficiary; employment 100,000 insured; pays only survivors' pension insurance 2,000 | (d)(2) gives 1,500 (1.5% proviso) but (d)(1) floor 2,268 is higher; base 2,000; credit 700 | (d): `לא יעלה על הגבוה מבין` |
| D187 | employee, not beneficiary; employment 100,000 insured; survivors' pension insurance 5,000 only | (d)(2) = 1,500, floor 2,268; base 2,268; credit 793.80 | same |
| D188 | self-employed, not beneficiary, no employment income; taxable income 100,000 (QI 100,000); pays 20,000 pension | s 47(b) deduction 11,000 (D240); remainder 9,000; base min(9,000, max(2,268, 5% x 100,000 = 5,000)) = 5,000; credit 1,750 | (d)(2)(b)(1) 5%; s 47(c) |
| D189 | same, pays 12,000 | deduction 7,000; base 5,000; credit 1,750 | same (the two possible orders of applying s 47(b) and s 45A agree at exactly 12%) |
| D190 | same, pays 10,000 | **REFUSE** or recorded fork: the source does not say whether the s 47(b) deduction or the s 45A credit takes the payment first; deduction-first gives deduction 7,000 and credit 1,050, credit-first gives credit 1,750 and deduction 5,000 | s 47(b), s 47(c), s 45A(b),(d) |
| D191 | beneficiary member; pays life insurance for his child aged 20 | creditable under (b1) | line 1719: `ובלבד שגילו של אותו ילד, בשנת המס, היה 18 שנים ומעלה` |
| D192 | beneficiary member; child aged 16 | not creditable under (b1) | same |
| D193 | not beneficiary; child aged 20 | not creditable under (b1) | line 1719: `עמית מוטב יזוכה` |
| D194 | beneficiary; employment income 150,000, all insured; pays 10,000 pension; s 47(b1) deduction is nil (D246) | (e)(2)(b)(2)(a): 7% x QI-that-is-insured (116,400) = 8,148; (b) 5% x non-insured taxable = 0; cap 8,148; base 8,148; credit 2,851.80 | (e) |
| D195 | beneficiary, self-employed, no insured income; taxable 100,000; pays 30,000 pension | s 47(b1) deduction 11,000 (D245); (e)(2)(b)(1): 5% x 100,000 = 5,000; base 5,000; credit 1,750 | (e)(2)(b)(1) |
| D196 | beneficiary, no insured income, taxable 300,000 | the (e)(2)(b)(1) ceiling is 5% x min(300,000, 2 x 116,400 = 232,800) = 11,640 | line 1735: `עד לסכום השווה לפעמיים הסכום האמור` |
| D197 | not beneficiary; pays both life insurance and pension; total above the 7% cap | **REFUSE** or recorded fork for the credit amount: the base cap is clear but the text does not say whether the 25% items or the 35% items fill it first | (a), (b), (d) |
| D198 | s 45A(f): self-employed, not beneficiary, no s 32(14)(b) deduction, no insured income, business income 100,000; pays 20,000 pension, of which 11,000 deducted under s 47(b) and 5,000 credited under (b) | (f) base min(4,000 remaining, 0.5% x 100,000 = 500) = 500; extra credit 175; total s 45A credit 1,925. My reading; it assumes the order of D188 | line 1739 |
| D199 | as D198 but he was allowed a s 32(14)(b) deduction | no (f) credit | line 1739: `יחיד שלא נוכו לו סכומים … לפי סעיף 32(14)(ב)` |
| D200 | payment to a body for preserving pension rights: is that body one "שקבע שר האוצר"? | **REFUSE** (or input): depends on a determination outside scope | line 1718 |

## I. Section 47: definitions and deduction

| id | facts | expected | provision |
|---|---|---|---|
| D220 | QI: only employment income 100,000 | 100,000 | s 47(a)(1)(1), line 1766 |
| D221 | QI: only employment income 150,000 | 116,400 | same |
| D222 | QI: no employment income, business 150,000 | 150,000 | (a)(1)(2), line 1767 |
| D223 | QI: no employment income, 200,000 | 164,400 | same |
| D224 | QI: employment 60,000 + business 150,000 | 60,000 + min(150,000, 164,400 - min(60,000, 116,400)) = 60,000 + 104,400 = 164,400 | (a)(1)(3), line 1768. My reading of `לפי הנמוך מביניהם`: subtract the lower of (employment income, A1). The other reading (take the lower of the two remainders) gives 60,000 + 48,000 = 108,000 |
| D225 | QI: employment 130,000 + business 100,000 | 116,400 + min(100,000, 164,400 - 116,400) = 164,400 | same |
| D226 | QI: employment 20,000 + business 30,000 | 50,000 | same |
| D227 | QI: employment 100,000 + business 10,000 | 110,000 | same |
| D228 | "income for a self-employed member": taxable 150,000, insured 40,000 | min(150,000, 116,400) - 40,000 = 76,400 | (a)(3), line 1770 |
| D229 | "additional income": taxable 250,000, insured 100,000 | min( min(150,000, 116,400), min(250,000, 291,000) - max(100,000, 116,400) ) = min(116,400, 133,600) = 116,400 | (a)(5), lines 1772-1774 |
| D230 | "additional income": taxable 200,000, insured 150,000 | min(50,000, 200,000 - 150,000) = 50,000 | same |
| D231 | "additional income": taxable 150,000, insured 0 | min(116,400, 150,000 - 116,400) = 33,600 | same |
| D232 | beneficiary member: paid for him in 2026 to pension funds 26,437 | yes | (a)(7): `בסכום שלא פחת מ־16% מסך כל השכר הממוצע במשק באותה שנת מס` (16% x 12 x 13,769 = 26,436.48) |
| D233 | same, 26,000 | no | same |
| D234 | insured income: employment income for which the employer paid into a pension fund / for which there is a pension right by law or contract / neither | insured / insured / not insured | (a)(4), line 1771 |
| D235 | not beneficiary, only employment income 100,000 all insured; pays 6,000 pension | s 47(b) deduction 0: (b)(1) 7% of non-employment QI = 0; (b)(2)(a) 5% of employment QI that is not insured = 0 | (b) |
| D236 | not beneficiary, self-employed (no employment income), taxable 100,000; pays 5,000 / 7,000 | not decidable without the order question of D190 (deduction-first: 5,000 / 7,000; credit-first: 0 / 2,000) -> **REFUSE** or fork | (b)(1) with s 47(c) |
| D240 | not beneficiary, self-employed, taxable 100,000; pays 20,000 | 7,000 + min(20,000 - 12,000, 4,000) = 11,000 | (b)(1): `ואולם אם שילם סכום העולה על 12% … ניכוי נוסף עד ל־4%` |
| D241 | same, pays 16,000 | 7,000 + 4,000 = 11,000 | same |
| D242 | same, pays 13,000 | 7,000 + 1,000 = 8,000 (both orders agree) | same |
| D243 | same, pays 12,000 | 7,000 (no extra: 12% is not exceeded) | same |
| D244 | not beneficiary, self-employed, taxable 200,000 (QI 164,400); pays 30,000 | 7% x 164,400 = 11,508; extra min(30,000 - 19,728, 4% x 164,400 = 6,576) = 6,576; total 18,084 | same |
| D245 | beneficiary, self-employed, no insured income, taxable 100,000; pays 30,000 | (b1)(1): 11% x (min(100,000, 116,400) - 0) = 11,000; (b1)(2): additional income = min(100,000, 100,000 - 116,400 < 0) -> 0; deduction 11,000 | (b1), line 1784 |
| D246 | beneficiary, employment income 150,000 all insured; pays 10,000 | income for self-employed member = 116,400 - 150,000 < 0 -> 0; additional income = 0; deduction 0 | (a)(3), (a)(5), (b1) |
| D247 | beneficiary pays into a pension fund for his child aged 20 / 17 | deductible under (b1) / not | line 1783: `לטובת ילדו שגילו, בשנת המס, 18 שנים ומעלה` |
| D248 | not beneficiary, pays only to a provident fund that is not a pension fund (קופת גמל לתגמולים) | no s 47(b) deduction | line 1778: `לקופת גמל לקצבה בלבד` |
| D249 | an amount deducted under (b) | cannot also be deducted under (b1), and is not taken into account for s 45A | (b2), (c), lines 1786-1787 |
| D250 | an individual in a class for which the Minister prescribed higher deduction rates | **REFUSE**: depends on the 1980 regulations (line 1789) | (d), line 1788 |
| D251 | (b1)(2) last proviso: `שלא יינתן ניכוי לפי פסקה זו בשל סכומים שהופקדו בעד העמית המוטב שסכומם אינו עולה על 16% מהשכר הממוצע במשק` | **REFUSE** or fork: unclear whether the 16% is of the monthly or the annual wage, and whether it is a threshold on the total or a carve-out of the first slice | line 1785 |

## J. Section 64B: registered spouse

Tax year first considered: 2026, so the comparison year in (a) is 2024 (`בשנת המס שקדמה בשנתיים`).

| id | facts | expected | provision |
|---|---|---|---|
| D260 | 2024 taxable income: A 120,000, B 80,000 | the officer may designate A (and only A) under (a) | line 2440: `באשר הכנסתו החייבת בשנת המס שקדמה בשנתיים … היתה למעלה מ־50%` |
| D261 | 2024: A 100,001, B 99,999 | A | same |
| D262 | 2024: A 100,000, B 100,000 | **REFUSE**: neither exceeds 50%; (a) does not apply; (c) applies only if neither had taxable income | lines 2440, 2442 |
| D263 | 2024: neither had taxable income | the officer may designate either one (c); who is designated is **REFUSE** (discretion) unless the designation is an input | line 2442 |
| D264 | election for 2027 notified on 2026-10-01 | in time | line 2441: `לפחות שלושה חדשים לפני תחילתה של שנת מס פלונית` |
| D265 | election for 2027 notified on 2026-10-02 | late for 2027 | same |
| D266 | notice in 2026 electing B; 2025 income: B 25,000, A 100,000 | condition met (exactly 25%) | line 2441: `שהכנסתו בשנת המס שקדמה לשנת המס שבה ניתנה ההודעה היא לפחות בגובה של 25% מהכנסת בן זוגו` |
| D267 | same, B 24,999 | condition not met | same |
| D268 | notice by one spouse alone | not an election under (b) | line 2441: `רשאים בני זוג ביחד להודיע בכתב` |
| D269 | (a) determination effective 2023; officer seeks a fresh (a) determination for 2026 | not allowed: in force at least five tax years (2023-2027) | line 2443: `תעמוד בתקפה לא פחות מחמש שנות מס` |
| D270 | same, for 2028 | allowed | same |
| D271 | (a) determination effective 2023; the couple divorce in 2025 | the determination does not continue | line 2443: `זולת אם בני הזוג אינם עוד בני זוג` |
| D272 | (a) determination effective 2023; the couple elect the other spouse for 2026, in time, 25% condition met | allowed | line 2443: `בכפוף לאמור בסעיף קטן (ב)` |
| D273 | election effective 2024; the couple re-elect the first spouse for 2026 | **REFUSE** or fork: does `בכפוף לאמור בסעיף קטן (ב)` let an election displace an election within five years? | line 2443 |
| D274 | elected registered spouse's 2026 income 20,000; other spouse 100,000 | the officer may determine a registered spouse for 2026 | line 2444: `פחותה מ־25% מהכנסת בן זוגו באותה שנת המס` |
| D275 | same, 25,000 vs 100,000 | the (d)(2) power does not arise | same |
| D276 | the elected spouse's income includes joint-source income under s 66(d) | **REFUSE** (or input): whether s 66(d)'s conditions hold is outside scope | line 2441 |

## K. Section 65: joint computation

A is the registered spouse; B the other; tax year 2026.

| id | facts | expected | provision (line 2448) |
|---|---|---|---|
| D280 | B has employment income 100,000 | deemed A's income, assessed in A's name (s 66 separate computation is outside scope) | `הכנסת בני זוג יראוה … כהכנסת בן הזוג הרשום והיא תחוייב על שמו` |
| D281 | A's child, born 2010 (16), has interest 5,000 | included in A's income | `ככוללות גם הכנסות כאמור של ילדו שטרם מלאו לו בשנת המס 18 שנים` |
| D282 | A's child born 2009 (turns 17 in 2026), interest | included | same |
| D283 | A's child born 2008 (turns 18 in 2026), interest | not included (my reading: the child reached 18 in the tax year; arguable reading: age at the start of the year) | same |
| D284 | the child's interest comes from an inherited asset | not included | `אלא אם כן הנכסים … התקבלו בירושה` |
| D285 | the child's interest comes from compensation for bodily injury | not included | `או שמקורם בפיצויים או בכספי ביטוח שהתקבלו בשל פגיעת גוף` |
| D286 | child (16) has a capital gain | included | `או מרווח הון` |
| D287 | child (16) has employment income | not included | not a listed kind |
| D288 | child (16) has rental income | not included | not a listed kind |
| D289 | child (16) has a dividend | not included | not a listed kind (s 65's `ריבית` is interest, discount, linkage differentials) |
| D290 | child (16) has linkage differentials | included | `מריבית, מדמי ניכיון או מהפרשי הצמדה (לענין סעיף זה – ריבית)` |
| D291 | child (16) has income passed through from a real-estate investment fund (s 64A2) | included | `מהכנסה שהועברה מקרן להשקעות במקרקעין` |
| D292 | A and B married but living apart | s 65 does not apply (they are not spouses, D002) | s 1 "בן זוג" |
| D293 | B claims separate computation of personal-exertion income | **REFUSE**: s 66, outside scope | s 66(a), line 2456 |
| D294 | a child of B only (A's stepchild), 16, interest | **REFUSE** or fork: s 65 says `ילדו` (the registered spouse's child) | line 2448 |

## L. Tax-year edges and refusals that do not fit above

| id | facts | expected | why |
|---|---|---|---|
| D300 | value of a credit point for 2028 | **REFUSE**: s 120B(e)(2) re-indexes on 1 Jan 2028 by an index not yet known | line 4345 |
| D301 | average wage for 2027 | **REFUSE**: published by the National Insurance Institute; not yet published, and outside the Ordinance | s 3(ה3)(2) |
| D302 | s 47 / s 45A figures for 2026 | the 2024 figures (s 120B(e)(1) freeze): A1 116,400, A2 164,400, F45 2,268 | line 4344 |
| D303 | credit-point value for 2026 | 2,904 (same freeze) | lines 1563, 4344 |
| D304 | s 121A | repealed; no credit | line 4453 `(בוטל)` |

## Count

Scenario rows: D001-D019 (19), D020-D037 (18), D040-D068 (29), D070-D076 (7), D080-D093 (14), D100-D110 (11), D120-D122 (3), D130-D144 (15), D150-D158 (9), D160-D171 (12), D180-D200 (21), D220-D236 and D240-D251 (29), D260-D276 (17), D280-D294 (15), D300-D304 (5): **224**.
Scenarios whose expected answer is a refusal (or a refusal or recorded fork): D017, D018, D019, D035, D036, D037, D055, D065, D092, D093, D109, D120, D122, D165, D190, D197, D200, D236, D250, D251, D262, D263, D273, D276, D293, D294, D300, D301: **28**.

Completed (UTC, from `date -u`): Wed Oct  7 00:45:44 UTC 2026

---

## Revised after seeing the encoding

Appended 2026-10-07 at about 01:45 UTC by the session that continued this pass, after `tests-independent.l4` was written and run and after `NOTES.md` was read.
No line above this heading was changed (the file's first 370 lines are byte-identical to the frozen copy, sha256 `71f8ffc0…05618d7d`).
No expected value in `tests-independent.l4` was changed because of anything below.

- **D244 is my own error.** "Not a beneficiary member" and "pays 30,000" cannot both hold in 2026: s 47(a)(7) (line 1776) makes a beneficiary member of one for whom at least 16% of the year's average wage was paid, which is 26,436.48, and a self-employed person's own deposit is a sum paid for him. The figure 18,084 is the s 47(b) answer for someone who is not a beneficiary member. For the facts as they must be (he is one), the answer comes from s 47(b1), which I did not work out. The assertion keeps 18,084 and fails.
- **D190 and D236 are unchanged, but on reflection one reading is stronger.** s 47(c) (line 1787), `סכום שנוכה לפי סעיף קטן (ב) או (ב1) לא יובא בחשבון לצורך סעיף 45א`, assumes the deduction is fixed before s 45A applies. That supports deduction first. The text still does not say the individual must take the largest deduction s 47(b) allows, so I keep the refusal as the expected answer.
- **D019 is unchanged.** The limb in full (lines 167-169): `”תושב חוץ“ – מי שאינו תושב ישראל, וכן יחיד שהתקיימו בו כל אלה: (א) הוא שהה מחוץ לישראל 183 ימים לפחות, בכל שנה, בשנת המס ובשנת המס שלאחריה; (ב) מרכז חייו לא היה בישראל ... בשתי שנות המס שלאחר שנות המס האמורות בפסקת משנה (א)`. By "not in Israel in 2027 and 2028" the scenario meant limb (b): the centre of life was not in Israel in those years.
