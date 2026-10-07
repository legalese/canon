# Decided answers, IL-08 National Insurance half (independent test author `fid-il-08b`)

**Finished: Wed Oct  7 00:42:39 UTC 2026** (from `date -u`), before any `.l4` file, `NOTES.md`, `encoding.json` or `check.sh` in the encoding directory was opened.
Read beforehand: `skills/encoding-a-subject/references/second-pass.md`, `skills/writing-l4-rules/SKILL.md` and its source-patterns 04 and 11, the encoding's `BRIEF.md`, and a plain `ls` of the encoding directory.

Source: `registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt` (sha256 `78bf47ee…552a97`), lines read in full:
s 1 definitions (120–228); Chapter 3 s 39–41 (545–561); Chapter 4 s 65–72 (799–856); s 75 (943–953); s 150 (1403–1407); s 158 (1441–1454); s 180 (1818–1827); s 195 (1921–1942); s 223 (2165–2184); s 238–247 (2401–2497); s 334–337, 340–342 (3601–3675); s 351 (3809–3835); s 402–406 (4314–4351); Schedule A1, Parts A–E (4367–4476).
Amending Laws: the three PDFs under `registers/source-bundle/amending-laws/`, extracted with `pdftotext -layout` into my scratch directory and searched.
None of them amends s 72, s 335 or Schedule A1: Amendment 252 touches s 1 ("הסכום הבסיסי" freeze), s 32, s 74ה, s 340, new s 340א and Schedule J; the 2025 Budget-year Law touches s 32, s 334, s 341, s 342, s 345ב and Schedule J; the 2023 Economic Efficiency Law touches s 32, s 149א, Schedule J (temporary), s 182, s 183, s 195, s 202, s 238, s 320 and s 345ב.
No figure in this file comes from the National Insurance Institute or from the encoding.

## Readings I took, stated once

- **RD-1 "עד 15 בחודש פלוני" includes the 15th.** s 72(א) has two limbs, "עד 15" and "אחרי 15"; "אחרי 15" plainly excludes the 15th, and the two limbs are written to cover every day of the month, so the 15th belongs to the first limb.
- **RD-2 Entitlement arises on the day of birth.** s 66 gives the allowance "בעד כל ילד"; s 65(א) makes a child of an insured a "ילד" from birth. s 72(ב) is a condition on *payment* ("לא תשולם קצבת ילדים אלא בעד ילד שחי שבעה ימים לפחות או שיצא מבית החולים"), not the moment entitlement arises. So a child born on 12 March who survives is paid from 1 March even though the seven days complete on 19 March. (Alternative reading, not taken: entitlement arises when s 72(ב) is satisfied.)
- **RD-3 A child "מלאו לו 18 שנים" on the 18th anniversary of the date of birth**, and ceases to be a "ילד" under s 65(א) ("ובלבד שהילד ... לא מלאו לו 18 שנים") on that day. (The English common-law rule that an age is attained at the start of the day before the anniversary is not taken; it would move the month for a child born on the 1st.)
- **RD-4 A 29 February anniversary in a common year is not answered by the source.** Every child born on 29 February has a common-year 18th anniversary (a leap year plus 18 is ≡ 2 mod 4). The law does not say whether such a child turns 18 on 28 February or 1 March, so the *month* in which entitlement ceases is undetermined.
- **RD-5 s 72(ג) "שלושה חודשים מתום החודש שבו נפטר"**: payment continues for the three whole months after the month of death; the last day paid is the last day of (month of death + 3). The month of death itself is paid under s 72(א) third limb.
- **RD-6 s 335 is read alone.** It says for whom ("בעדו") contributions are paid in each branch; who pays is s 342, the rates are s 337 and Schedule J, and exemptions are s 351. None of those is in scope, so none is applied below. s 335(י) "אין הוראות סעיף זה גורעות זו מזו" makes the subsections cumulative.
- **RD-7 The nine branches s 335 names**: maternity (ביטוח אימהות, (א) and (ט)); children (ביטוח ילדים, (ב)); work injury (נפגעי עבודה, (ג)); accident victims (נפגעי תאונות, (ד)); unemployment (אבטלה, (ה)); employees' rights in insolvency (זכויות עובדים בהליכי חדלות פירעון, (ו)); disability (נכות, (ז)); long-term care (סיעוד, (ח)); senior citizens and survivors (אזרחים ותיקים ושאירים, (ט)). Health insurance is not among them.
- **RD-8 Schedule A1 Part D answers one question**: the age of entitlement to a senior citizen's pension *for a woman*, by her month of birth ("גיל הזכאות לקצבת אזרח ותיק לנשים לפי חודש לידתן"). It is read through s 245(א)(2), s 342(ג)(2), s 351(ב) and s 406(א)(4)(א). Its first row has no lower bound ("עד יוני 1939") and its last none above ("מאי 1950 ואילך"). Ages are given below both as years-and-months and as total months.
- **RD-9 Commencement.** s 402: "תחילתו של נוסח משולב זה היא ביום ז׳ בתשרי התשנ״ו (1 באוקטובר 1995)". Before that the 1968 consolidation governed (s 72 was its s 114, s 335 its s 157), and it is not in the bundle. Schedule A1 carries "תיקון: תשס״ד" (added in 2004); the text of Part D before then, and the date it took effect, are not in the consolidation. The text of s 72, s 335 and Part D carries no other date of its own.

## s 72 — the period of the child allowance

### A. When payment starts (s 72(א), "נוצרה זכאות לקצבת ילדים עד 15 בחודש פלוני, תשולם הקצבה החל ב־1 באותו חודש; נוצרה הזכאות אחרי 15 בחודש פלוני, תשולם הקצבה החל ב־1 בחודש שלאחריו")

| id | entitlement arose on | payment starts on | licensed by |
|---|---|---|---|
| 72-01 | 2026-03-01 | 2026-03-01 | first limb ("עד 15") |
| 72-02 | 2026-03-14 | 2026-03-01 | first limb |
| 72-03 | 2026-03-15 | 2026-03-01 | first limb, RD-1 |
| 72-04 | 2026-03-16 | 2026-04-01 | second limb ("אחרי 15 ... ב־1 בחודש שלאחריו") |
| 72-05 | 2026-03-31 | 2026-04-01 | second limb |
| 72-06 | 2026-02-15 | 2026-02-01 | first limb |
| 72-07 | 2026-02-28 (last day, common year) | 2026-03-01 | second limb |
| 72-08 | 2024-02-29 (leap day) | 2024-03-01 | second limb |
| 72-09 | 2024-02-28 (leap year, not the last day) | 2024-03-01 | second limb |
| 72-10 | 2025-12-16 | 2026-01-01 | second limb, across the year |
| 72-11 | 2025-12-31 | 2026-01-01 | second limb, across the year |
| 72-12 | 2025-12-15 | 2025-12-01 | first limb |
| 72-13 | 2026-04-30 (last day of a 30-day month) | 2026-05-01 | second limb |
| 72-14 | 1995-10-01 (commencement day) | 1995-10-01 | first limb; s 402 |

### B. When payment ends (s 72(א), "תשלום הקצבה יסתיים ביום האחרון של החודש שבו נפסקה הזכאות")

| id | entitlement ceased on | last day paid | licensed by |
|---|---|---|---|
| 72-20 | 2026-05-01 | 2026-05-31 | third limb |
| 72-21 | 2026-05-15 | 2026-05-31 | third limb |
| 72-22 | 2026-05-16 | 2026-05-31 | third limb (no 15th-day split on cessation) |
| 72-23 | 2026-05-31 | 2026-05-31 | third limb |
| 72-24 | 2026-02-10 | 2026-02-28 | third limb, common year |
| 72-25 | 2028-02-10 | 2028-02-29 | third limb, leap year |
| 72-26 | 2028-02-29 | 2028-02-29 | third limb, leap day |
| 72-27 | 2026-12-01 | 2026-12-31 | third limb |
| 72-28 | 2026-04-10 | 2026-04-30 | third limb, 30-day month |
| 72-29 | a 17-year-old marries on 2025-06-10 | 2025-06-30 | s 1 "ילד" "ולמעט נער ונערה נשואים" ends entitlement that day; third limb |

### C. A child born, and turning 18 (s 72(א) with s 65(א) "לא מלאו לו 18 שנים"; RD-2, RD-3)

| id | date of birth | payment starts | turns 18 on | last day paid | months paid |
|---|---|---|---|---|---|
| 72-30 | 2008-05-01 | 2008-05-01 | 2026-05-01 | 2026-05-31 | 217 |
| 72-31 | 2008-05-15 | 2008-05-01 | 2026-05-15 | 2026-05-31 | 217 |
| 72-32 | 2008-05-16 | 2008-06-01 | 2026-05-16 | 2026-05-31 | 216 |
| 72-33 | 2008-05-31 | 2008-06-01 | 2026-05-31 | 2026-05-31 | 216 |
| 72-34 | 2007-12-31 | 2008-01-01 | 2025-12-31 | 2025-12-31 | 216 |
| 72-35 | 2008-01-01 | 2008-01-01 | 2026-01-01 | 2026-01-31 | 217 |
| 72-36 | 2010-02-15 | 2010-02-01 | 2028-02-15 | 2028-02-29 | 217 |
| 72-37 | 2008-02-28 | 2008-03-01 | 2026-02-28 | 2026-02-28 | 216 |
| 72-38 | 2008-03-01 | 2008-03-01 | 2026-03-01 | 2026-03-31 | 217 |
| 72-39 | 2008-02-29 | 2008-03-01 | **undetermined** | **REFUSE** (RD-4: 28 Feb or 1 Mar 2026, so February or March) | **REFUSE** |

### D. The seven-day condition (s 72(ב), "לא תשולם קצבת ילדים אלא בעד ילד שחי שבעה ימים לפחות או שיצא מבית החולים")

| id | facts | allowance payable for this child? |
|---|---|---|
| 72-40 | born 2026-03-01, died 2026-03-08 (7 days by date difference), never left hospital | **yes**: seven days on either count (7 elapsed, 8 calendar days inclusive) |
| 72-41 | born 2026-03-01, died 2026-03-06 (5 days), never left hospital | **no**: under seven days on either count, and did not leave hospital |
| 72-42 | born 2026-03-01, died 2026-03-07 (6 days by date difference), never left hospital | **REFUSE**: 6 days elapsed or 7 calendar days inclusive; the source does not say how "שבעה ימים" is counted and dates alone cannot settle it |
| 72-43 | born 2026-03-01, left hospital 2026-03-03, died 2026-03-04 | **yes**: "או שיצא מבית החולים" |
| 72-44 | born at home 2026-03-01, never in hospital, died 2026-03-04 | **no**, on the literal words (neither lived seven days nor left a hospital); low confidence, a purposive reading could differ |
| 72-45 | born 2026-03-01, alive and at home at 2026-04-01 | **yes** |

### E. Continuation after a child's death (s 72(ג), "נפטר ילד שבעדו שולמה קצבת ילדים, ימשיכו בתשלום הקצבה שלושה חודשים מתום החודש שבו נפטר"; RD-5)

| id | facts | last day paid |
|---|---|---|
| 72-50 | allowance paid; child died 2026-03-10 | 2026-06-30 |
| 72-51 | died 2026-03-31 | 2026-06-30 |
| 72-52 | died 2026-04-01 | 2026-07-31 |
| 72-53 | died 2027-11-15 | 2028-02-29 (leap) |
| 72-54 | died 2026-11-15 | 2027-02-28 |
| 72-55 | died 2026-12-10 | 2027-03-31 |
| 72-56 | born 2026-02-10, left hospital 2026-02-12, died 2026-02-20 | paid from 2026-02-01; last day 2026-05-31 |
| 72-57 | born 2026-02-20, left hospital 2026-02-22, died 2026-02-25 | **REFUSE**: s 72(א) starts payment on 1 March and ends it on 28 February, so no month was ever paid; whether s 72(ג) ("שבעדו שולמה") still runs three months is not answered |
| 72-58 | born 2008-05-20 (would turn 18 on 2026-05-20); died 2026-03-10 | 2026-06-30 on the literal words of (ג), which run three months regardless; recorded alternative: stop at 2026-05-31 |
| 72-59 | born 2026-03-01, died 2026-03-04, never left hospital | nothing paid at all: (ב) fails, so no allowance was paid, so (ג) does not apply |

### F. Dates outside the consolidation

| id | facts | answer |
|---|---|---|
| 72-60 | entitlement arose 1995-01-10 (before s 402 commencement) | **REFUSE**: the 1968 consolidation (its s 114) governed, and it is not in the bundle |

## s 335 — for whom contributions are paid, in which branches (RD-6, RD-7)

Inputs at the level of s 335 itself: resident of Israel; employee; self-employed; insured under Chapter 5, Chapter 6, s 158 para (1), Chapter 8 (as employee), Chapter 9, long-term care (s 223), Chapter 11; housewife (s 238); widow-pensioner (s 238); controlling shareholder (בעל שליטה) in a closely-held company (חברת מעטים); insured under Chapter 3.
Branch letters: M maternity, C children, W work injury, A accidents, U unemployment, I insolvency, D disability, L long-term care, O senior citizens and survivors.

| id | person | branches | not | licensed by |
|---|---|---|---|---|
| 335-01 | resident employee, 30, insured under ch 5, 6, s 158(1), ch 8, 9, LTC, 11 | M C W A U I D L O (all nine) | — | (ב)–(ט); M via (ט) |
| 335-02 | non-resident employee, insured under ch 5 and ch 8 only | M W I | C A U D L O | (א) "עובד ... שאינו תושב ישראל"; (ג); (ו) |
| 335-03 | non-resident self-employed, insured under ch 5 only | M W | C A U I D L O | (א) "עובד עצמאי שאינו תושב ישראל"; (ג) |
| 335-04 | non-resident, neither employee nor self-employed, insured under nothing | none | all | (א) needs employee or self-employed |
| 335-05 | resident self-employed, 40, insured under ch 5, 6, 9, LTC, 11 | M C W A D L O | U I | (ה) needs s 158(1), which needs an employee; (ו) needs an employee |
| 335-06 | resident, 40, neither employee nor self-employed, not a housewife, insured under ch 6, 9, LTC, 11 | M C A D L O | W U I | (ב), (ד), (ז), (ח), (ט) |
| 335-07 | housewife (s 238), resident, 40, insured under ch 6, 9, LTC, 11 | A D L | M C W U I O | (ב) "למעט עקרת בית" via s 65(א)(1); (ט) "למעט עקרת בית"; (ד), (ז), (ח) do not exclude her (s 351(ח)–(י) would, but are out of scope) |
| 335-08 | widow-pensioner (s 238), resident, 50, insured under ch 6, 9, LTC, 11 | C A D L | M W U I O | (ב) excludes only the housewife; (ט) "למעט עקרת בית ואלמנה בת קצבה" |
| 335-09 | controlling shareholder in a closely-held company, employed by it, resident, 45, insured under ch 5, 6, s 158(1), ch 8, 9, LTC, 11 | M C W A D L O | U I | (ה), (ו) "למעט בעל שליטה בחברת מעטים" |
| 335-10 | controlling shareholder in a company that is *not* closely held, otherwise as 335-09 | all nine | — | the exclusion is only for "בחברת מעטים" |
| 335-11 | resident employee, 17, insured under ch 5 and ch 8 only | W I | M C A U D L O | ch 11, 6, 9 and s 158(1) all need 18; (א) needs a non-resident |
| 335-12 | resident employee, man, 68, past retirement age and the Part B age, insured under ch 5, 8, LTC, 11 | M C W I L O | A U D | ch 6 (s 150) and ch 9 (s 195) end at retirement age; s 158(1) at the Part B age |
| 335-13 | 335-06 plus insured under ch 3 | same as 335-06 | — | (ט) "בין שהוא מבוטח גם לפי פרק ג׳ ובין שאינו מבוטח לפיו" |
| 335-14 | resident police officer, 30 (s 75(א)(1) excludes police from ch 5, so not ch 8 either, s 180), insured under ch 6, s 158(1), 9, LTC, 11 | M C A U D L O | W I | (ג), (ו) |
| 335-15 | woman who immigrated at 70, not working, insured for LTC under s 223(4) only | L | all others | (ח) |
| 335-16 | agunah (s 1), not working, resident, 40, insured under ch 6, 9, LTC, 11 | M C A D L O | W U I | s 238 "עקרת בית ... למעט עגונה" |
| 335-17 | married woman, not working, resident, 40, whose husband is not insured under ch 11 | M C A D L O | W U I | s 238 requires "שבן זוגה מבוטח לפי פרק זה", so she is not a housewife |
| 335-18 | married woman who is an employee, resident, 40, all chapters as 335-01 | all nine | — | s 238 "שאינה עובדת" |
| 335-19 | married man, not working, resident, 40, whose wife is insured | M C A D L O | W U I | s 238 "עקרת בית – אשה נשואה": a man is never a housewife |
| 335-20 | widow who is an employee and receives a survivors' pension, resident, 50, all chapters as 335-01 | all nine | — | s 238 "אלמנה בת קצבה – אלמנה שאינה עובדת" |
| 335-21 | temporary resident (תושב ארעי), not a resident, employee, 30, insured under s 158(1), ch 5, ch 8 | M W U I | C A D L O | (א) (not a resident); s 158(1) "תושב ישראל או תושב ארעי" |

| id | question | answer |
|---|---|---|
| 335-R1 | the rate or amount of contributions in any branch | **REFUSE**: s 337 and Schedule J, out of scope |
| 335-R2 | the branches for a rule date before 1995-10-01 | **REFUSE**: s 402; the 1968 consolidation's s 157 governed |
| 335-R3 | whether the housewife of 335-07 actually pays accident, disability or long-term-care contributions | **REFUSE** if asked as a final liability: s 351(ח), (ט), (י) exempt her, and s 351 is out of scope. Answering it as s 335 alone is acceptable if labelled so |
| 335-R4 | who must pay (employer or insured) | **REFUSE**: s 342, out of scope |

## Schedule A1 Part D — women's age of entitlement to a senior citizen's pension, by month of birth (RD-8)

Each row is tested at its first and last month, so every boundary is tested on both sides.

| id | woman born in | age | in months | row (line) |
|---|---|---|---|---|
| D-01 | January 1920 | 65 | 780 | "עד יוני 1939" (4438), no lower bound |
| D-02 | May 1939 | 65 | 780 | 4438 |
| D-03 | June 1939 | 65 | 780 | 4438 |
| D-04 | July 1939 | 65 and 4 months | 784 | "יולי ואוגוסט 1939" (4439) |
| D-05 | August 1939 | 65 and 4 months | 784 | 4439 |
| D-06 | September 1939 | 65 and 8 months | 788 | "ספטמבר 1939 עד אפריל 1940" (4440) |
| D-07 | December 1939 | 65 and 8 months | 788 | 4440, across a year inside a row |
| D-08 | January 1940 | 65 and 8 months | 788 | 4440 |
| D-09 | April 1940 | 65 and 8 months | 788 | 4440 |
| D-10 | May 1940 | 66 | 792 | "מאי עד דצמבר 1940" (4441) |
| D-11 | December 1940 | 66 | 792 | 4441 |
| D-12 | January 1941 | 66 and 4 months | 796 | "ינואר עד אוגוסט 1941" (4442) |
| D-13 | August 1941 | 66 and 4 months | 796 | 4442 |
| D-14 | September 1941 | 66 and 8 months | 800 | "ספטמבר 1941 עד אפריל 1942" (4443) |
| D-15 | April 1942 | 66 and 8 months | 800 | 4443 |
| D-16 | May 1942 | 67 | 804 | "מאי 1942 עד דצמבר 1944" (4444) |
| D-17 | February 1944 | 67 | 804 | 4444 |
| D-18 | December 1944 | 67 | 804 | 4444 |
| D-19 | January 1945 | 67 and 4 months | 808 | "ינואר עד אוגוסט 1945" (4445) |
| D-20 | August 1945 | 67 and 4 months | 808 | 4445 |
| D-21 | September 1945 | 67 and 8 months | 812 | "ספטמבר 1945 עד אפריל 1946" (4446) |
| D-22 | April 1946 | 67 and 8 months | 812 | 4446 |
| D-23 | May 1946 | 68 | 816 | "מאי עד דצמבר 1946" (4447) |
| D-24 | December 1946 | 68 | 816 | 4447 |
| D-25 | January 1947 | 68 and 4 months | 820 | "ינואר עד אוגוסט 1947" (4448) |
| D-26 | August 1947 | 68 and 4 months | 820 | 4448 |
| D-27 | September 1947 | 68 and 8 months | 824 | "ספטמבר 1947 עד אפריל 1948" (4449) |
| D-28 | April 1948 | 68 and 8 months | 824 | 4449 |
| D-29 | May 1948 | 69 | 828 | "מאי עד דצמבר 1948" (4450) |
| D-30 | December 1948 | 69 | 828 | 4450 |
| D-31 | January 1949 | 69 and 4 months | 832 | "ינואר עד אוגוסט 1949" (4451) |
| D-32 | August 1949 | 69 and 4 months | 832 | 4451 |
| D-33 | September 1949 | 69 and 8 months | 836 | "ספטמבר 1949 עד אפריל 1950" (4452) |
| D-34 | April 1950 | 69 and 8 months | 836 | 4452 |
| D-35 | May 1950 | 70 | 840 | "מאי 1950 ואילך" (4453) |
| D-36 | December 1955 | 70 | 840 | 4453 |
| D-37 | January 1956 | 70 | 840 | 4453 (no break at 1956, unlike Part A's women's table) |
| D-38 | March 2000 | 70 | 840 | 4453, no upper bound |

Day of the month does not matter: a woman born on 1 June 1939 and one born on 30 June 1939 both get 65 (D-39a, D-39b); one born on 1 July 1939 gets 65 and 4 months (D-39c).

The date on which she reaches that age (date of birth plus the years and months), where an interface offers it:

| id | date of birth | reaches the age on |
|---|---|---|
| D-40 | 1939-06-15 | 2004-06-15 (65) |
| D-41 | 1939-07-01 | 2004-11-01 (65 and 4 months) |
| D-42 | 1939-08-31 | 2004-12-31 (65 and 4 months) |
| D-43 | 1940-04-30 | 2005-12-30 (65 and 8 months) |
| D-44 | 1950-05-01 | 2020-05-01 (70) |
| D-45 | 1948-02-29 | 2016-10-29 (68 and 8 months; 29 February 2016 exists, so either order of adding gives the same day) |
| D-46 | 1945-10-31 | **REFUSE**: 67 and 8 months lands on 31 June 2013, which does not exist (30 June or 1 July) |
| D-47 | 1944-02-29 | **REFUSE**: 67 lands on 29 February 2011, which does not exist |
| D-48 | 1945-07-31 | **REFUSE**: 67 and 4 months lands on 31 November 2012 |

Refusals at Part D's edges:

| id | question | answer |
|---|---|---|
| D-R1 | Part D's age for a man (any month of birth) | **REFUSE**: Part D is "לנשים" only; a man's age (70) comes from s 245(א)(1), s 342(ג)(2) or s 351(ב), not from Part D |
| D-R2 | Part D as in force on 2003-01-01 | **REFUSE**: Schedule A1 was added by תשס״ד; the consolidation does not carry the earlier law |

## Count

s 72: 14 + 10 + 10 + 6 + 10 + 1 = 51 scenarios (4 refusals: the end date of 72-39, 72-42, 72-57, 72-60; the start date of 72-39 is determinate).
s 335: 21 + 4 = 25 scenarios (4 refusals).
Part D: 38 + 3 + 9 + 2 = 52 scenarios (5 refusals: D-46, D-47, D-48, D-R1, D-R2).
Total 128 scenarios, of which 13 are refusals.

## Revised after seeing the encoding

Appended on 2026-10-07 by a second `fid-il-08b` session, after `tests-independent.l4` was final (01:35:19 UTC, from `date -u`) and after the encoding's `NOTES.md` had been read.
No line above this heading was changed, and no expected value above is revised; every assertion in `tests-independent.l4` still carries the value decided above.

- **RD-9 is incomplete; this is my own error.** It says the text of s 72, s 335 and Part D "carries no other date of its own". That holds for s 72 only: line 853 (`{{ח:סעיף|72|תקופת הקצבה|אחר=[114]}}`) has no amendment tag.
  The heading of s 335 (line 3610) carries "תיקון: תשנ״ו, תשס״ג־8, תשע״ז־12, תשע״ח־5". Part D carries "תיקון: תש״ף" (line 4432) and "תיקון: תשע״ז־12" (line 4433).
  So the present text of s 335 may not be the text in force for every period from 1 October 1995, and the present Part D may not be the text for every date from 2004.
  No scenario above poses such a date, so no expected value changes. But an s 335 scenario dated between 1995 and the תשע״ח־5 amendment would have needed a refusal or a reading of the amending Law, not the answer RD-9 implied.
  The encoding's gate from January 2026 for s 335 (its assumption A3) is therefore more defensible than RD-9 suggested.
  I noticed this because the encoding quotes line 3610; I then read lines 853, 3610, 4432 and 4433 of the source myself.
- **72-57, on reflection.** "ימשיכו בתשלום הקצבה" (they shall continue the payment) presupposes a payment already under way. That supports the encoder's fork N2 (no month was paid, so (ג) does not run) over my REFUSE.
  The REFUSE above stands as decided. I record that I now lean to N2, with the caveat that the encoding reaches N2's answer only when the caller supplies "a child allowance was paid for the child" as FALSE.
- **D-46, D-47 and D-48 are unchanged.** The encoder moves a non-existent day to the last day of the shorter month (fork N4, which it chose so that it agrees with row IL-05's F19).
  The National Insurance Law does not say which day it is, and no Interpretation Law is in the bundle, so REFUSE remains the answer from the sources alone.
- **72-14 and the 2008 starts in 72-30 to 72-39 are unchanged.** The encoding refuses months before May 2015 (its A2) so that it composes with row IL-06. That is a choice about scope. s 72 itself has no amendment tag (the encoder and I agree on this), so s 72's own text still answers October 1995 and May 2008.
