# IL-06 decided answers (independent test author, written before opening the encoding)

Finished: Tue Oct  6 15:03:48 UTC 2026 (`date -u`)

Author: `fid-il-06`, an independent test author, working from the Hebrew source alone.
Before this file was finished I had read: the source (s 1 lines 120-229, s 65 line 799, s 66 line 813, s 67 line 816, s 68 lines 820-835, and also s 69(d)-s 73 lines 840-859 to check which provisions displace ss 67-68), `BRIEF.md`, and a plain `ls` of the encoding directory.
I had not opened `NOTES.md`, `encoding.json`, `check.sh`, `tools/` or any `.l4` file in the encoding directory.

Source: `registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`, sha256 `78bf47ee29a300d51c5c7646cf85992d7de78aa1380bd8460a4a18265f552a97` (re-hashed by me, matches).
Line numbers below are lines of that file.

## Figures used, and where they come from

Two kinds of amount input appear below.

1. **Chosen inputs.** Where a scenario says "chosen inputs", I chose the three basic amounts for the child allowance to be the figures printed in s 1 paragraph (2) itself: (2)(a) = 150, (2)(b) = 188, (2)(c) = 140 (lines 187-189).
   These are a choice of input, not a claim about any day.
   They coincide with the NII's row for 1.05.2015 (below).
2. **NII published figures.** The National Insurance Institute's table "הסכום הבסיסי לחישוב קצבאות", `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/הסכום הבסיסי לחישוב קצבאות.aspx`, fetched 2026-10-06 14:59:55 UTC through the Israeli-IP proxy, sha256 of the HTML `f873d1eff32a5030dcd3a7fe5334145e980d2aed90b442a5998e8939d57d1aec`.
   Its "סכום בסיסי 2" columns (child allowance: "בעד הילד הראשון, החמישי ואילך" / "בעד הילד השני, השלישי והרביעי" / "לעניין גמלה לפי חוק הבטחת הכנסה"):

   | from (החל ביום) | (2)(a) | (2)(b) | (2)(c) |
   | --- | --- | --- | --- |
   | 1.05.2015 | 150 | 188 | 140 |
   | 1.01.2018 | 150 | 189 | 140 |
   | 1.01.2019 | 152 | 191 | 142 |
   | 1.01.2020 | 152 | 192 | 142 |
   | 1.01.2021 | 152 | 192 | 142 |
   | 1.01.2022 | 156 | 197 | 145 |
   | 1.01.2023 | 164 | 207 | 153 |
   | 1.01.2024 | 169 | 214 | 158 |
   | 1.01.2025 | 169 | 214 | 158 |
   | 1.01.2026 | 173 | 219 | 162 |

   There is no row for 1.01.2016 or 1.01.2017, so the 1.05.2015 figures run to 31.12.2017.
   The rows before 1.05.2015 in the same page are a different table with a single child-allowance figure (140 from 1.01.2014), i.e. a different text of the law.
   Also fetched: the NII per-child page `https://www.btl.gov.il/benefits/children/Pages/שיעורי הקצבה.aspx`, same time, sha256 `779380f35381d596d6b16abb98b2b04cb422e4e0cfa2d5d67b2dc4207c320ac9`: "החל מ- 01.01.2026": ראשון 173, שני 219, שלישי 219, רביעי 219, חמישי ואילך 173; supplement "עבור הילד השלישי והרביעי במשפחה בסך 113 ש"ח לכל ילד".
   And the NII abroad page `.../benefits/children/Pages/שהות בחוץ לארץ.aspx`, sha256 `b86cea0a7a977a8b91f22591f07e22d7a9c1956879087034809ca94a6e33679d`, which says a child abroad keeps the allowance "למשך 3 החודשים הראשונים לשהותו בחוץ לארץ" and loses it "החל בחודש הרביעי".

All amounts are NIS per month **before rounding** (s 381 not in scope), so a supplement of 70% of 162 is 113.4, not the NII's printed 113.

## Defaults for every scenario unless it says otherwise

- The parent is insured under s 65(a) limb (2): resident in Israel, not absent, not insured under Chapter 11, not a housewife.
- The parent has no income chargeable to additional tax under ITO s 121B (an input from outside scope).
- The parent is not paid an Income Support benefit nor a payment under the Maintenance (Assurance of Payment) Law.
- Every child is the parent's own child (born to them), unmarried, in Israel throughout, under 18 on the day.
- No child is born before 1 June 2003 (so s 68(b) cannot bite) unless the scenario gives dates.
- "Count" means the number of children in that parent's count under s 67; "total" means the monthly child allowance for that parent under s 68.
- The count is ordered **eldest first by date of birth**. The text does not say this in words; see C8 and the note there.

Confidence: **H** = the words leave no room; **M** = my reading, a different reading is arguable; **L** = I would not be surprised to be wrong.

## A. Entitlement: s 66 and the definitions it relies on

| id | facts | expected | licensed by | conf |
| --- | --- | --- | --- | --- |
| A1 | Single insured parent, one child aged 5. Chosen inputs. | Entitled; count 1; total 150. | s 66 l.814 "הורה מבוטח זכאי לקצבת ילדים חודשית ... בעד כל ילד"; s 68(a) l.821 "בסכום השווה לסכום הבסיסי הקבוע לגביו"; s 1(2)(a) l.187 "בעד הילד הראשון" | H |
| A2 | As A1 but the parent is not resident in Israel and not insured under Chapter 11. | Not insured; not entitled; total 0 (no allowance). | s 65(a) "מבוטח" limbs (1) l.802 and (2) l.803; s 66 requires "הורה מבוטח" | H |
| A3 | As A1 but the parent is insured under Chapter 11 and is not a housewife. | Insured (limb (1)); entitled; total 150. | s 65(a)(1) l.802 "מבוטח לפי פרק י״א, למעט עקרת בית" | H |
| A4 | As A1 but the parent, a resident, is abroad on an absence the authorised Institute employee considers temporary and reasonable. | Insured (limb (2)); entitled; total 150. | s 65(a)(2) l.803 "ואינו נעדר ממנה אלא העדר ארעי שהוא סביר, לדעת עובד המוסד שהוסמך לכך" | H |
| A5 | As A1 but the parent has income chargeable to additional tax within ITO s 121B. | Not entitled; total 0. | s 66 l.814 "למעט הורה מבוטח שיש לו הכנסה החייבת במס נוסף כמשמעותה בסעיף 121ב" | H |
| A6 | As A5 but no such income (the other side). | Entitled; total 150. | s 66 | H |
| A7 | Single insured parent; the only child is 17 and married. | The married 17-year-old is not a "child"; count 0; total 0. | s 1 l.170 "ילד – ... ולמעט נער ונערה נשואים" (applied through s 65's "ילדו") | M |
| A8 | Single insured parent; two unmarried children aged 17 and 7; then the 17-year-old marries. | Before: count 2, total 338 (chosen). After the elder marries: count 1, total 150 (the younger becomes first). | s 1 l.170; s 1(2)(a)/(b) | M |
| A9 | Insured step-parent; child is the step-parent's spouse's child, lives with the step-parent; the child's natural parents are not insured. | The child is the step-parent's "child"; counted with the step-parent; count 1, total 150 (chosen). | s 1 l.170 "לרבות ילד חורג"; s 65 l.805 "ילדו של מבוטח"; s 67(a) l.817 | M |
| A10 | Single insured adoptive parent of one adopted child. | Counted; count 1; total 150 (chosen). | s 1 l.170 "וילד מאומץ" | H |
| A11 | Insured grandmother; grandchild lives with her; it is proved to the satisfaction of the Administration's delegate that she supported him for the prescribed period; the grandchild's parents are not insured. | The grandchild is her "child" and she is a "parent"; count 1; total 150 (chosen). | s 65 l.806 "מי שאינו ילדו, אם הוכח, להנחת דעתו של מי שהסמיכה לכך המינהלה, כי בתקופה שנקבעה בתקנות פירנס אותו המבוטח"; l.807 "והמונחים ”אב“, ”אם“ ו”הורה“ יתפרשו בהתאם לכך" | H |
| A12 | As A11 but support is not proved. | Not her "child"; count 0; total 0. | s 65 l.806 | H |
| A13 | Single insured parent; child of 5 who lives abroad (no absence from Israel to speak of; the child is simply not in Israel). | Not a "child" (proviso); count 0; total 0. | s 65 l.807 "ובלבד שהילד נמצא בישראל" | H |

## B. The count: s 67

Parents are F (father), M (mother); both insured unless stated. "With" = where the child is (נמצא).
Amounts are with chosen inputs.

| id | facts | expected | licensed by | conf |
| --- | --- | --- | --- | --- |
| B1 | F and M (natural parents) both insured; one child, with both. | In F's count. F count 1 total 150; M count 0 total 0. | s 67(b) l.818 "ילד שיש לו שני הורים, יבוא במנין האב המבוטח"; s 67(a) l.817 "לא יבוא ילד ... במנין ילדים של יותר מהורה מבוטח אחד" | H |
| B2 | As B1, child with M only. | In M's count; F count 0. | s 67(b) "זולת אם הוא נמצא עם האם בלבד" | H |
| B3 | As B1, child with F only. | In F's count. | s 67(b) | H |
| B4 | As B1, child with neither parent (lives with an aunt who is not shown to support him). | In F's count: the only exception is "with the mother only". | s 67(b) literal | M |
| B5 | F insured, M not insured; child with both. | In F's count. | s 67(b) | H |
| B6 | F not insured, M insured; child with both. | In M's count: s 67(b) assigns to "the insured father" and there is none; s 66 entitles M "בעד כל ילד" and s 67(a) is not engaged. | s 66; s 67(a),(b) | M |
| B7 | F not insured, M insured; child with F only. | In M's count (same reasoning as B6; s 66 does not require the child to be with the parent). | s 66 | M |
| B8 | Neither F nor M insured. | Nobody's count; no allowance. | s 66 | H |
| B9 | F and M both insured; three children, all with both. | F count 3, total 526; M count 0. | s 67(b); s 68(a); s 1(2) | H |
| B10 | F and M both insured; two children with both, one child (the youngest) with M only. | F count 2, total 338 (150 + 188); M count 1, total 150. Each parent's count has its own "first child". | s 67(b); s 68(a) "שבמנין ילדיו של ההורה"; s 1(2)(a) "במניין ילדיו של ההורה" | H |
| B11 | Natural M insured, step-father S insured, natural father not insured; child with M only (S lives elsewhere). | In M's count. | s 67(b) second limb l.818 "ילד שיש לו הורה טבעי והורה אחר והם מבוטחים, יבוא במנין ילדי אותו הורה אשר עמו הוא נמצא" | H |
| B12 | As B11, child with S only. | In S's count. | s 67(b) second limb | H |
| B13 | Two adoptive parents, both insured; child with both. | In the adoptive father's count (a child with two parents). | s 1 l.170 "וילד מאומץ"; s 67(b) first limb | M |
| B14 | As B13, child with the adoptive mother only. | In the adoptive mother's count. | s 67(b) first limb | M |
| B15 | "Excluded father": F and M both insured; child with both; F has s 121B income. | Child is in F's count (F is still "הורה מבוטח", the words s 66 itself uses for him); F is not entitled, so F's total 0; M may not count the child (s 67(a)), so M's total 0. No allowance for this child. | s 66 "למעט הורה מבוטח שיש לו ..."; s 67(a),(b) | L |
| B16 | As B15 but the child is with M only. | In M's count; M entitled; M total 150. | s 67(b) | H |
| B17 | Natural M insured; insured grandmother G proved to support the child; child lives with G only. | In G's count. | s 65 l.806-807; s 67(b) second limb | M |
| B18 | Any family: no child is in two counts on one day. | Sum of the counts equals the number of countable children. | s 67(a) | H |

## C. The amount: s 68 and s 1 paragraph (2)

Single insured parent unless stated. Chosen inputs (150/188/140) unless stated.

| id | facts | expected | licensed by | conf |
| --- | --- | --- | --- | --- |
| C0 | count 0 | total 0 | s 68(a) | H |
| C1 | count 1 | 150 | s 1(2)(a) "בעד הילד הראשון" | H |
| C2 | count 2 | 338; the 2nd child 188 | s 1(2)(b) "בעד הילד השני" | H |
| C3 | count 3 | 526; 3rd child 188 | s 1(2)(b) "השלישי" | H |
| C4 | count 4 | 714; 4th child 188 | s 1(2)(b) "והרביעי" | H |
| C5 | count 5 | 864; 5th child 150 | s 1(2)(a) "והחמישי ואילך" | H |
| C6 | count 6 | 1014; 6th child 150 | s 1(2)(a) "ואילך" | H |
| C7 | Per-child: the k-th child in a count of 6 gets 150, 188, 188, 188, 150, 150 for k = 1..6. | as stated | s 1(2)(a),(b) | H |
| C8 | Order: two children born 2015-01-01 and 2018-01-01. | The elder (2015) is first, 150; the younger second, 188. | Not stated in words. Read from s 68(b) l.822, which ties the place in the count to a birth date ("ילד שנולד לפני ... והוא הילד הרביעי ואילך"), and the NII's own practice ("מחושב לפי מספר הילדים במשפחה, תאריך הלידה של הילדים"). | M |
| C9 | Three children, born 2008-10-06, 2012-01-01, 2015-01-01. Day 2026-10-05 vs 2026-10-06. | 2026-10-05: count 3, total 526 (chosen) / 611 (NII 2026). 2026-10-06: the eldest is 18, count 2, total 338 (chosen) / 392 (NII 2026); the 2012 child is now first. | s 65 l.807 "ולא מלאו לו 18 שנים"; s 1(2) | H |
| C10 | s 68(b), 4th child born **before** 1 June 2003: day 2016-01-01; children born 1998-02-01, 1999-03-01, 2000-04-01, 2003-05-31. Figures 150/188/140. | 4th child = 150 × 2.24 = 336; total 150 + 188 + 188 + 336 = 862. | s 68(b) l.822 "ילד שנולד לפני יום א׳ בסיון התשס״ג (1 ביוני 2003), והוא הילד הרביעי ואילך"; (b)(2) l.824 "הקבוע בפסקה (2)(א) ... כשהוא מוכפל ב־2.24" | H |
| C11 | As C10 but the 4th child is born **on** 2003-06-01. | 4th child = 188; total 714. | s 68(b) "לפני" (strictly before) | H |
| C12 | s 68(b)(3): day 2016-01-01; five children born 1998-02-01, 1999-03-01, 2000-04-01, 2001-05-01, 2002-06-01. | 4th = 336; 5th = 150 × 2.36 = 354; total 1216. | s 68(b)(3) l.825 "הילד החמישי ואילך ... מוכפל ב־2.36" | H |
| C13 | Six children, all born before June 2003 (1998-02-01, 1999-01-01, 2000-01-01, 2001-01-01, 2002-01-01, 2003-01-01), day 2016-01-01. | 150 + 188 + 188 + 336 + 354 + 354 = 1570. | s 68(b)(2),(3) | H |
| C14 | Day 2016-01-01; five children born 1998-02-01, 1999-03-01, 2000-04-01, 2003-05-31, 2005-01-01. | 4th = 336 (pre-June-2003); 5th born 2005 is not "כאמור", so s 68(a) and (2)(a): 150. Total 1012. | s 68(b) applies only to "ילד שנולד לפני ..."; s 68(a) | H |
| C15 | Day 2016-01-01; three children born 1999-01-01, 2001-01-01, 2003-01-01 (the 3rd is pre-June-2003). | s 68(b) does not reach a 3rd child: 188. Total 526. | s 68(b) "הרביעי ואילך" | H |
| C16 | s 68(b) multiplies (2)(a), not (2)(b): day 2019-06-01, NII figures 152/191/142; children born 2001-07-01, 2002-02-01, and twins 2003-05-31. | 152 + 191 + 191 + 152 × 2.24 (= 340.48) = 874.48. | s 68(b)(2) "בפסקה (2)(א)" | H |
| C17 | Income Support recipient, count 2. | No supplement; 338. | s 68(c) l.826 "בעד שלושה ילדים או יותר" | H |
| C18 | Income Support recipient, count 3. | 526 + 70% × 140 (= 98) = 624. | s 68(c) "תיווסף ... בעד הילד השלישי ובעד הילד הרביעי ... תוספת בסכום השווה ל־70% מן הסכום הבסיסי הקבוע בפסקה (2)(ג)"; s 1(2)(c) l.189 | H |
| C19 | Income Support recipient, count 4. | 714 + 2 × 98 = 910. | s 68(c) | H |
| C20 | Income Support recipient, count 5. | 864 + 2 × 98 = 1060 (no supplement for the 5th). | s 68(c) "השלישי ובעד הילד הרביעי" only | H |
| C21 | Maintenance (Assurance of Payment) Law payment recipient, count 3. | 624. | s 68(c) "או תשלום חודשי לפי חוק המזונות (הבטחת תשלום)" | H |
| C22 | Neither, count 3. | 526. | s 68(c) | H |
| C23 | Income Support recipient, C10's family (4th child pre-June-2003), 2016-01-01. | 862 + 196 = 1058: the supplement is added to an allowance under (b) too. | s 68(c) "כאמור בסעיפים קטנים (א) או (ב)" | H |
| C24 | Income Support recipient, 2026-03-01, NII figures 173/219/162; count 3 and count 4. | count 3: 611 + 113.4 = 724.4; count 4: 830 + 226.8 = 1056.8. | s 68(c) "(2)(ג)" | H |
| C25 | Income Support recipient with three children, one abroad over 3 months without an Institute decision. | Count 2; no supplement; 338. | s 65 l.807, l.809; s 68(c) | H |
| C26 | Mother paid Income Support; F and M both insured; three children with both (so in F's count); F not paid Income Support. | No supplement: the parent paid Income Support must be the one entitled for three or more. F total 526. | s 68(c) "הורה שמשתלמים לו ... והוא זכאי בעד אותו חודש לקצבת ילדים ... בעד שלושה ילדים או יותר" | M |

## D. Age, absence and day-level edges

| id | facts | expected | licensed by | conf |
| --- | --- | --- | --- | --- |
| D1 | Child born 2008-10-06; day 2026-10-05. | A child (17). | s 65 l.807 "ולא מלאו לו 18 שנים" | H |
| D2 | Same child; day 2026-10-06 (18th birthday). | Not a child. | s 65 l.807 (18 years are completed on the birthday) | M |
| D3 | Quadruplets born 2003-05-31; day 2021-05-30; NII 2021 figures 152/192/142. | All four are children; the 4th is pre-June-2003: 152 + 192 + 192 + 340.48 = 876.48. | s 65 l.807; s 68(b)(2) | M (order among same-day children does not change the total) |
| D4 | Quadruplets of D3 on 2021-05-31. | None is a child; total 0. | s 65 l.807 | H |
| D5 | Child left Israel for a completed absence of exactly three months, now back; day during that absence. | Not regarded as abroad; counted. | s 65(b) l.809 "לא יראו ילד כנמצא בחוץ לארץ אם יצא מישראל לתקופה שאינה עולה על שלושה חודשים" | H (month level) |
| D6 | Child left Israel for a period exceeding three months; the Institute has decided not to treat him as in Israel; day in the 4th month. | Abroad; not a child; not counted. | s 65 l.807 "ובלבד שהילד נמצא בישראל"; s 65(b) | H |
| D7 | As D6 but the Institute has decided to regard him as in Israel. | Counted. | s 65(b) "אולם המוסד רשאי לראותו כאילו הוא בישראל גם אם יצא מישראל לתקופה העולה על שלושה חודשים" | H |

## E. Dates, commencement and the published figures

| id | facts | expected | licensed by | conf |
| --- | --- | --- | --- | --- |
| E1 | Any family, day 2015-04-30. | The deposited text does not answer: REFUSE. | The text in this file is s 68 as amended by תשע״ו־3 (l.820 tag); the NII table starts the 150/188/140 regime on 1.05.2015 and has a single 140 figure before it, i.e. a different s 1(2). The brief's 1 May 2015 is consistent with the NII table. | M (the date itself comes from outside the source text) |
| E2 | Day 2015-05-01, one child. | Answers; figures 150/188/140; total 150. | as E1 | M |
| E3 | Published figures on both sides of each 1 January in the NII table. | 2017-12-31: 150/188/140. 2018-01-01: 150/189/140. 2018-12-31: 150/189/140. 2019-01-01: 152/191/142. 2019-12-31: 152/191/142. 2020-01-01: 152/192/142. 2021-01-01: 152/192/142. 2021-12-31: 152/192/142. 2022-01-01: 156/197/145. 2022-12-31: 156/197/145. 2023-01-01: 164/207/153. 2023-12-31: 164/207/153. 2024-01-01: 169/214/158. 2024-12-31 and 2025-01-01: 169/214/158 (s 1 updating para (3) l.197: "ב־1 בינואר של שנת 2025 לא יתעדכנו הסכומים הקבועים בפסקה (2)"). 2025-12-31: 169/214/158. 2026-01-01: 173/219/162. 2016-01-01 and 2017-01-01: 150/188/140 (no row). | NII table (see top) | H (as figures) |
| E4 | Published figures for 2027-01-01. | No published figure at retrieval: REFUSE (a day's figure is not invented). | brief "Do not invent a number"; s 1 updating clause l.197 needs a CPI not yet published | H |
| E5 | NII per-child amounts by year (single parent, places 1..5): 2018: 150, 189, 189, 189, 150. 2020: 152, 192, 192, 192, 152. 2024: 169, 214, 214, 214, 169. 2025: same as 2024. 2026: 173, 219, 219, 219, 173. Supplement per 3rd/4th child under s 68(c): 2018 98; 2020 99.4; 2024 and 2025 110.6; 2026 113.4. | as stated | s 68(a),(c); NII table | H |
| E6 | Single parent with two children, 2025-12-31 vs 2026-01-01. | 383 vs 392. | s 68(a); NII table | H |

## F. Where the source does not answer

The right result in each is a refusal (or, where the encoding takes the missing fact as an explicit input, a refusal when the input is absent; never a silent `FALSE`, `0` or default).

| id | facts | expected | why | conf |
| --- | --- | --- | --- | --- |
| F1 | Two mothers, both insured (same-sex couple); child with both. | REFUSE. | s 67(b) first limb assigns to "האב המבוטח" unless "עם האם בלבד"; there is no father. | H |
| F2 | Natural M and step-father S both insured; child with both. | REFUSE. | s 67(b) second limb: "אותו הורה אשר עמו הוא נמצא" picks no one when he is with both; reading the first limb instead (S as "father" under l.807) is an argument, not the text. | M |
| F3 | As F2, child with neither. | REFUSE. | second limb picks no one. | M |
| F4 | F insured, M not insured, child with M only. | REFUSE. | Literal s 67(b): not in F's count ("זולת אם הוא נמצא עם האם בלבד") and M has no count, so nobody; structural reading: s 67(b) only arbitrates between two insured parents, so F. The text does not choose. | M |
| F5 | Insured man with children by more than one woman. | REFUSE (s 69A displaces ss 67-68 and is out of scope). | s 69A l.843 "על אף האמור בכל מקום אחר בסימן זה, היו למבוטח ילדים ממספר נשים" | H |
| F6 | Parent who was insured and has died or ceased to be insured. | REFUSE (s 71 is out of scope). | s 65 l.805 "או של מי שהיה מבוטח"; s 71 l.851 | H |
| F7 | Child abroad more than three months; whether the Institute exercises its s 65(b) power is not known. | REFUSE (or the decision is a required input with no default). | s 65(b) "המוסד רשאי" is discretion. | H |
| F8 | Child born 2008-02-29; day 2026-02-28. | REFUSE or a recorded fork: the law does not say when a 29 February child completes 18 years in a common year. 2026-02-27: a child. 2026-03-01: not a child. | s 65 l.807 | M |
| F9 | Child on a trip that will last six months; a day in the first month. | REFUSE or a recorded fork: the statute's "יצא מישראל לתקופה ... העולה על שלושה חודשים" reads as the whole trip (abroad from the first day), while the NII applies it as "the first three months count". | s 65(b) l.809; NII abroad page | M |
| F10 | Mother is a "housewife" within s 238. | REFUSE or explicit input: s 65(a)(1) excludes her; s 65(a)(2) "ואינו מבוטח לפי פרק י״א, למעט עקרת בית" can be read either to let her in or to keep her out. | s 65(a) l.802-803 | L |
| F11 | Natural F, natural M and step-father S, all insured; child with M and S. | REFUSE. | both limbs of s 67(b) engage and disagree. | M |

Scenario count: A 13, B 18, C 27, D 7, E 6, F 11 = 82.

## Revised after seeing the encoding

Everything above this heading was finished at 15:03:48 UTC and has not been changed (a frozen copy taken then has sha256 `0f7be179243e42a6183708188807118f175408a313c25e2c09d2e7013747d19f`; the text above is byte-identical to it).
This section was added afterwards, after reading the `.l4` modules, running `tests-independent.l4`, and then reading `NOTES.md`.
**No expected value above has been revised.**

1. **F10 (the housewife), my confidence moves, not my expected value.**
   On reflection the phrase "מבוטח לפי פרק י״א, למעט עקרת בית כהגדרתה בסעיף 238" is one noun phrase, and it appears verbatim in both limbs: limb (1) is that phrase, and limb (2) is "ואינו" + that phrase, i.e. "and is not [insured under Chapter 11 other than a housewife]".
   Read that way the limbs partition the residents, and a resident housewife not within limb (1) falls into limb (2): she is insured for Chapter 4 if resident and not absent.
   The encoding reads "למעט עקרת בית" in limb (2) as a second exclusion, so a housewife is never insured for Chapter 4.
   I still record REFUSE as the expected value, because both parses are grammatical, but I now think the encoding's parse is the weaker of the two, and it is not in its fork register.
2. **F7 could not be expressed.** The interface takes the Institute's s 65(b) decision as a required BOOLEAN (`the Institute regards the child as in Israel`), with no way to say "not known".
   That meets the alternative this file allowed ("or the decision is a required input with no default"), so no assertion was written; it is counted as not expressible.
3. **Two assertions were added after seeing the interface**, in section X of `tests-independent.l4`, licensed by the same source text: X1, the other side of A4 (a resident whose absence is not a reasonable temporary one is not insured, s 65(a)(2) line 803); X2, a child who came back before the day is in Israel on the day (s 65 line 807), so a finished absence supplied by a caller must either be rejected as a fact or leave the child counted.
4. **E1's date.** The encoding's `nii-il06-period.l4` cites s 29(a) of the Economic Efficiency Law 5776-2015 (Sefer HaChukim 2511, p. 247) for 1 May 2015.
   That agrees with the NII table row I relied on; I did not fetch that Law myself.
5. **The NII table hash.** My fetch of the basic-amounts page (193,012 bytes, sha256 `f873d1ef…1aec`) and the encoder's (193,110 bytes, sha256 `d1998550…4139`) differ in bytes; every child-allowance figure in the two agrees (E3, all 21 assertions satisfied). The page carries dynamic content, so a byte hash of it does not identify the figures.
