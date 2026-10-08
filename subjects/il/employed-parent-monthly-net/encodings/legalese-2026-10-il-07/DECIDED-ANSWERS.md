# IL-07 independent test author: answers decided from the sources, before opening the encoding

Finished (UTC, from `date -u`): 2026-10-06T23:46:05Z

Author: `fid-il-07`, an independent test author working alone.
Written before any `.l4` file, `NOTES.md`, `RECONCILE.md`, `GAPS.md`, `check.sh` or `vendor.sh` in `ENCODING_DIR` was opened, and before any of the six rows' directories was opened.
The only file in `ENCODING_DIR` read so far is `BRIEF.md`; its directory was listed once with a plain `ls`.
This file is not revised after that point except by appending a section headed "Revised after seeing the encoding".

## 0. What I read, and the figures I chose

Sources, all read-only, hashes checked before reading:

- ITO Hebrew text, `income-tax-ordinance-new-version.he.wiki.txt`, sha256 `b87f2cf4…94b81b6` (matches the brief).
  Read: s 1 (definitions of בן זוג, בן זוג רשום, הכנסה חייבת, הכנסה מיגיעה אישית), s 33A, s 34, s 35, s 36, s 36A, s 37 to s 40B, s 64B, s 65, s 66, s 120B, s 121, s 121B.
- NII Hebrew text, `national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`, sha256 `78bf47ee…f552a97` (matches).
  Read: s 1 (הסכום הבסיסי, השכר הממוצע, ילד), s 65 to s 73, s 334 to s 342, s 348, Schedule J (both the temporary 2025–2026 table and the permanent one), Schedule K.
- Amending Laws (pdftotext of the Knesset PDFs; sha256 of all three match `SOURCES.json`):
  Amendment 252 and temporary provision (25_lsr_5482787.pdf) ss 1, 6, 7;
  2025 Budget-year Law (25_lsr_6133485.pdf) ss 19, 20, 21 (Part E, commencing 1 January 2026);
  the 2023 Economic Efficiency Law (25_lsr_2572039.pdf) was not needed beyond what the Wikisource table already shows for 2024–2027 (work-injury 2.06 / 0.47).

Official figures fetched (saved under my scratch `fetched/`; retrieval times UTC):

| figure | value | source | retrieved | sha256 of the bytes |
| --- | --- | --- | --- | --- |
| reduced collection threshold (מדרגת גבייה מופחתת) from 1.1.2026 | 7,703 | btl.gov.il `/Insurance/Rates/Pages/לעובדים שכירים.aspx` | 2026-10-06T23:39:00Z | `f5bd019cf26adb815f5e84108933c7e86885114a84db4766b546080a41227f03` |
| maximum income for contributions from 1.1.2026 | 51,910 | same page | same | same |
| employee NI rate, reduced / full | 1.04% / 7% | same page | same | same |
| employee health rate, reduced / full (used only to choose the health input) | 3.23% / 5.17% | same page | same | same |
| child allowance per child from 1.1.2026: 1st 173, 2nd–4th 219, 5th+ 173 | 173 / 219 | btl.gov.il `/benefits/children/Pages/שיעורי הקצבה.aspx` | 2026-10-06T23:39:11Z | `faa9149a3758c6b1d2eb7901c5bcff77e914588e16bf2c20019f30557ab71f34` |
| average wage (s 1) from 1.1.2026 | 13,566 | btl.gov.il `/Mediniyut/GeneralData/Pages/שכר ממוצע.aspx` | 2026-10-06T23:39:21Z | `11e2ad2f79a4a067cb9fc3f526d34c25566547ed88278dd20aec80ff8a26ebba` |
| credit point 2026 | 242 a month (2,904 a year) | ITA "לוח עזר לחישוב מס הכנסה ממשכורת … לחודש ינואר 2026 ואילך", gov.il BlobFolder PDF; gov.il returned 403, fetched from Wayback capture 20260207101513 | 2026-10-06T23:40:03Z | `282bb886ccae1cc718840127af378fce88ca37ee3b2b9f00ed2cd44467e86285` |

Each agrees with the Wikisource annotation in the deposited text (ITO s 33A note "בשנים 2024–2027, 2,904 ש״ח"; NII s 1 notes 173 / 219 / 13,566 / 10,382; NII s 334 note 7,703).
51,910 = 5 × 10,382, the s 1 basic amount para (3) for 2026, as Schedule K item 1 requires ("לחודש – הסכום הבסיסי, כפול 5", and Schedule K's own definition points at para (3)).

**The 2026 tax brackets: a conflict between two official-ish sources, and my choice.**
The deposited ITO s 121 (amendment תשפ״ו־6, annotated "הסכומים מתואמים לשנים 2026–2027") reads: 31% / 35% / 47% at 301,200 and 560,280, and in s 121(b)(1) for personal-exertion income 10% to 84,120, 14% to 120,720, **20% to 228,000, 31% to 301,200**.
The ITA booklet captured on 7 February 2026 shows the **pre-amendment** 2026 table (20% to 193,800, 31% to 269,280).
Press and accountants' sites (not official, not hashed: maariv.co.il, malam-payroll.com) say the widening was enacted with the 2026 budget legislation and applies retroactively from 1 January 2026.
I could not retrieve an official post-amendment ITA publication (gov.il 403; the Wayback capture of the ITA employer notice of 30.03.26 is a 404).
**I take the brackets from the deposited statute**, because it is the source the rows encode and it is the later law; the February booklet predates the amendment.
H08 and H09 discriminate between the two readings.

## 1. The readings, provision by provision

### 1.1 Income tax (ITO)

- **Rates, s 121(a) and (b)(1)**: salary is "הכנסה חייבת בשנת המס מיגיעה אישית", so the reduced rates of (b)(1) apply up to 301,200: "על כל שקל חדש מ־84,120 השקלים החדשים הראשונים – 10%; … מ־84,121 … עד 120,720 – 14%; … מ־120,721 … עד 228,000 – 20%; … מ־228,001 … עד 301,200 – 31%", then (a)(2) "מ־301,201 … עד 560,280 – 35%" and (a)(3) "על כל שקל חדש נוסף – 47%".
- **Additional tax, s 121B(a)**: "יחיד אשר הכנסתו החייבת בשנת המס עלתה על 640,000 … (בשנים 2024–2027, 721,560 ש״ח), יהיה חייב במס נוסף על חלק הכנסתו החייבת העולה על … בשיעור של 3%". The (a1) 2% on capital income does not arise.
- **Indexation, s 120B(e)(1)**: "ב־1 בינואר של שנות המס 2025 עד 2027 לא יתואמו הסכומים" — so 2026 uses the frozen 1.1.2024 figures (credit point 2,904, the 721,560 threshold); the bracket figures in s 121 are as amended for 2026.
- **Credit point, s 33A**: "סכום של 504 … (בשנים 2024–2027, 2,904 ש״ח) לשנת מס … המקוזז כנגד המס לאותה שנה". "Offset against the tax" — I read that the credits reduce tax to zero and not below (no refund of unused points). **Tax = max(0, rates − points × 2,904).**
- **Personal points**: s 34 "יחיד שהיה תושב ישראל … שתי נקודות זיכוי" (2); s 36 "יחיד תושב ישראל … ¼ נקודת זיכוי כזיכוי נסיעה" (¼); s 36A "בחישוב המס של אשה תובא בחשבון ½ נקודת זיכוי" (½). Resident man 2¼, resident woman 2¾.
- **Spouses, ss 64B, 65, 66**: the earner's spouse has no income. Joint assessment (s 65) makes the earner the registered spouse. Child points for a married parent exist only inside a separate calculation, s 66(c)(4) for "האשה" and s 66(c)(5) for "הגבר". s 66(c)(1א): "בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד על הכנסתו מיגיעה אישית, ויהיה זכאי … לנקודות זיכוי כאמור בפסקאות (4) או (5)". I read this as available to the sole earner, who would always claim it because it only adds points. **My expectation: a married earner gets the s 66(c)(4)/(5) child points.** (Confidence: medium; the registered-spouse question in s 66(a)(1) is a possible fork.)
- **Child points, mother, s 66(c)(4)(a)** by the age the child attains in tax year 2026: born 2026 ("שנת לידתו") 2½; born 2025 or 2024 ("החל בשנת המס שלאחר שנת לידתו ועד לשנת המס שבה מלאו לו שנתיים") 4½; born 2023 (turns 3) 3½; born 2022 or 2021 (turns 4 or 5) 2½; born 2020 to 2009 (turns 6 to 17, "החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו") 2; born 2008 ("שנת בגרות" = the year he turns 18, s 40(b)(3)) ½.
- **Child points, father, s 66(c)(5)**: born 2026 2½; born 2025/2024 4½; born 2023 3½; born 2022/2021 2½; born 2020 to 2009 "נקודת זיכוי אחת" 1; no point in the year of majority.
- **Mother's deferral option, s 66(c)(4)(a1)**: one birth-year point may be taken in the following year. I avoid it (no mother in my set has a child born in 2025), and for a child born in 2026 I assume the point is taken in 2026 (the default reading of "בשנת הלידה").
- **Single parent with children, s 40(b)**: the points of s 40(b)(1), (1a), (1b), (2) belong to s 40, which the brief lists as a gap ("ITO ss 35, 37-40"). "משפחה חד־הורית" is not defined in the bundle. **I expect the capstone to decline the income tax (and so the net) for a single parent with children.** (Guess about the mechanism; the source certainly gives points the rows do not encode, so answering with zero child points would be wrong.)
- **Month from year**: the brief says the capstone gives annual tax and one twelfth of it. Every 2026 threshold is a multiple of 12 (7,010, 10,060, 19,000, 25,100, 46,690, 60,130 a month; 242 a point), so annual ÷ 12 equals the monthly-table withholding exactly for a constant salary. The child points of the whole tax year count in every month, including months before a birth (H29).

Monthly form used below (annual ÷ 12, S = monthly gross): rates R(S) = 10% to 7,010 (701 at the top); 14% to 10,060 (1,128); 20% to 19,000 (2,916); 31% to 25,100 (4,807); 35% to 46,690 (12,363.5); 47% above; plus 3% on S above 60,130. Credits: 242 per point.

### 1.2 National insurance deducted from salary (NII)

- s 337(a)(1): an employee's monthly contributions are Schedule J percentages "מהכנסתו החודשית".
- s 342(c)(1): "ינכה המעביד משכרו של העובד אחוזים מההכנסה … כאמור בלוח י׳ ובסעיף 337" — Schedule J column D is the employee's deduction (the employer's deduction from salary).
- Schedule J, temporary 2025–2026 table (Amendment 252 s 7(a)(3)(b), "בתקופה שמיום התחילה עד יום … (31 בדצמבר 2026)"): column D, part not exceeding the threshold **1.04%** (0.10+0.03+0.02+0.29+0.03+0.57); part above **7.00%**.
- Column D's heading: the Wikisource temporary table still reads "על חלק השכר העולה על 60% מהשכר הממוצע" for the 7% part. The 2025 Budget-year Law s 19(6), commencing 1 January 2026 (s 21), replaces "60% מהשכר הממוצע" "בלוח י', בכל מקום" with "מדרגת הגבייה המופחתת כהגדרתה בסעיף 334(א)". **I read 7% as applying to the part above 7,703** (not above 60% × 13,566 = 8,139.60). H05 and H47 discriminate. (s 19(6) speaks of Schedule J of the principal law; whether it reaches the column the temporary provision of Amendment 252 substitutes is arguable, but reading it not to would leave 7,703 to 8,139.60 unrated, which BTL's published table does not do.)
- s 334(a) "מדרגת גבייה מופחתת" — 7,522 for 2025, indexed by CPI on 1.1.2026: 7,703 (BTL).
- s 348(a) and Schedule K item 1: income above "הסכום הבסיסי, כפול 5" a month is ignored: 51,910.
- s 348(b) minimum (minimum wage) — does not bind for any salary in my set except H45 (a guess).
- Monthly deduction D(S) = 1.04% × min(S, 7,703) + 7% × (min(S, 51,910) − 7,703)⁺. At the threshold 80.1112; at the maximum 80.1112 + 3,094.49 = 3,174.6012. No rounding.

### 1.3 Health insurance

The National Health Insurance Law is not in the bundle; the brief makes the health contribution an input.
I supply, as that input, the figure from BTL's published 2026 rates: 3.23% × min(S, 7,703) + 5.17% × (min(S, 51,910) − 7,703)⁺ (248.8069 at the threshold). The capstone should subtract the input unchanged.

### 1.4 Child allowance (NII ss 65–72)

- s 66: "הורה מבוטח זכאי לקצבת ילדים חודשית … בעד כל ילד, **למעט הורה מבוטח שיש לו הכנסה החייבת במס נוסף כמשמעותה בסעיף 121ב לפקודת מס הכנסה**". I read "has income subject to additional tax" against tax year 2026 (annual taxable income above 721,560, i.e. S above 60,130). (Timing is my reading; medium confidence.)
- s 65(a) "ילד": the insured's child, "ובלבד שהילד נמצא בישראל ולא מלאו לו 18 שנים".
- s 67(b): "ילד שיש לו שני הורים, יבוא במנין האב המבוטח זולת אם הוא נמצא עם האם בלבד". In a couple the counting parent is the father; for a single parent, the earner. So the s 66 exclusion bites when the counting parent has additional-tax income: a high-earning **father** in a couple, or a high-earning single parent; not a high-earning mother whose husband has no income (H31). (My reading; medium confidence.)
- s 68(a) with s 1 "הסכום הבסיסי" para (2): first child and fifth onwards 173; second, third, fourth 219 (2026). s 68(b) (children born before 1.6.2003) cannot arise in 2026.
- s 72(a), **a gap in the brief's list**: "נוצרה זכאות … עד 15 בחודש פלוני, תשולם הקצבה החל ב־1 באותו חודש; נוצרה הזכאות אחרי 15 בחודש … החל ב־1 בחודש שלאחריו; תשלום הקצבה יסתיים ביום האחרון של החודש שבו נפסקה הזכאות". So a child born on or before the 15th counts for the month of birth; a child born after the 15th from the next month; a child who turns 18 counts for the whole month of the 18th birthday and not after. I read "עד 15" as inclusive.
- s 72(b): a newborn must live seven days; my newborns do.
- s 73: the allowance is not income for tax.
- Amounts with n children: 1 → 173; 2 → 392; 3 → 611; 4 → 830; 5 → 1,003.

### 1.5 The net

**Net = S − monthly income tax − NI deducted − health input + child allowance.** Whether the capstone's "net" includes the allowance is a guess from the brief ("the child allowance for the month, and the net"); each component is also asserted on its own so a composition difference is localised.

## 2. Worked households

Common facts unless stated: resident of Israel (ITO s 1 "תושב"; NII s 65 "מבוטח"), aged 35, one employer, same gross every month of 2026, no other income, no pension contribution, no immigrant status, no reserve service, spouse (where married) has no income, children are the couple's own, unmarried, in Israel, living with the parents. Month June 2026 unless stated. All amounts NIS; "tax/m" is one twelfth of the annual tax.

Arithmetic key: R(S) = rates on the monthly salary per §1.1; P = credit points; D(S) and H(S) per §1.2–1.3.

### Group A — no children; every bracket and contribution threshold on both sides

**H01** man, single, S 7,000 (below the reduced threshold and inside the 10% band).
R = 10% × 7,000 = 700. P = 2 (s 34) + ¼ (s 36) = 2¼ → 544.5. tax/m = 155.5; annual = 10% × 84,000 − 2¼ × 2,904 = 8,400 − 6,534 = 1,866.
D = 1.04% × 7,000 = 72.8. H = 3.23% × 7,000 = 226.1. Allowance 0.
Net = 7,000 − 155.5 − 72.8 − 226.1 = **6,545.6**.

**H02** man, single, S 7,010 (top of the 10% band; annual 84,120 exactly).
R = 701. tax/m = 701 − 544.5 = 156.5; annual 1,878. D = 72.904. H = 226.423. Net = **6,554.173**.

**H03** man, single, S 7,011 (one shekel into 14%).
R = 701 + 14% × 1 = 701.14. tax/m = 156.64; annual 1,879.68. D = 72.9144. H = 226.4553. Net = **6,554.9903**.

**H04** woman, single, S 7,703 (exactly the reduced threshold).
R = 701 + 14% × 693 = 798.02. P = 2¾ (ss 34, 36, 36A) → 665.5. tax/m = 132.52; annual 1,590.24.
D = 1.04% × 7,703 = 80.1112. H = 3.23% × 7,703 = 248.8069. Net = 7,703 − 132.52 − 80.1112 − 248.8069 = **7,241.5619**.

**H05** woman, single, S 7,704 (one shekel above the threshold; tests the s 19(6) heading).
R = 701 + 14% × 694 = 798.16. tax/m = 132.66; annual 1,591.92.
D = 80.1112 + 7% × 1 = 80.1812 (stale-heading reading would give 80.1112). H = 248.8069 + 0.0517 = 248.8586.
Net = **7,242.3002**.

**H47** woman, single, S 8,000 (between 7,703 and 60% of the average wage, 8,139.60).
R = 701 + 14% × 990 = 839.6. tax/m = 839.6 − 665.5 = 174.1; annual 2,089.2.
D = 80.1112 + 7% × 297 = 100.9012 (stale-heading reading: 80.1112). H = 248.8069 + 5.17% × 297 = 264.1618.
Net = **7,460.837**.

**H06** man, single, S 10,060 (top of 14%).
R = 1,128. tax/m = 583.5; annual 7,002. D = 80.1112 + 7% × 2,357 = 245.1012. H = 248.8069 + 5.17% × 2,357 = 370.6638. Net = **8,860.735**.

**H07** man, single, S 10,061.
R = 1,128.2. tax/m = 583.7; annual 7,004.4. D = 245.1712. H = 370.7155. Net = **8,861.4133**.

**H08** man, single, S 19,000 (top of the 2026 20% band; under the February ITA table this would be in 31%).
R = 1,128 + 20% × 8,940 = 2,916. tax/m = 2,371.5; annual 28,458. (Pre-amendment reading: 2,685.)
D = 80.1112 + 7% × 11,297 = 870.9012. H = 248.8069 + 5.17% × 11,297 = 832.8618. Net = **14,924.737**.

**H09** man, single, S 19,001.
R = 2,916.31. tax/m = 2,371.81; annual 28,461.72. D = 870.9712. H = 832.9135. Net = **14,925.3053**.

**H10** man, single, S 25,100 (top of 31%).
R = 2,916 + 31% × 6,100 = 4,807. tax/m = 4,262.5; annual 51,150. D = 80.1112 + 7% × 17,397 = 1,297.9012. H = 1,148.2318. Net = **18,391.367**.

**H11** man, single, S 25,101.
R = 4,807.35. tax/m = 4,262.85; annual 51,154.2. D = 1,297.9712. H = 1,148.2835. Net = **18,391.8953**.

**H12** man, single, S 46,690 (top of 35%).
R = 4,807 + 35% × 21,590 = 12,363.5. tax/m = 11,819; annual 141,828. D = 80.1112 + 7% × 38,987 = 2,809.2012. H = 2,264.4348. Net = **29,797.364**.

**H13** man, single, S 46,691.
R = 12,363.97. tax/m = 11,819.47; annual 141,833.64. D = 2,809.2712. H = 2,264.4865. Net = **29,797.7723**.

**H14** man, single, S 51,910 (exactly the Schedule K maximum).
R = 12,363.5 + 47% × 5,220 = 14,816.9. tax/m = 14,272.4; annual 171,268.8. D = 80.1112 + 7% × 44,207 = 3,174.6012. H = 248.8069 + 5.17% × 44,207 = 2,534.3088. Net = **31,928.69**.

**H15** man, single, S 55,000 (above the maximum: s 348(a) "לא יבוא בחשבון סכום ההכנסה … העולה על הסכום המרבי").
R = 12,363.5 + 47% × 8,310 = 16,269.2. tax/m = 15,724.7; annual 188,696.4. D = 3,174.6012 (capped). H = 2,534.3088 (capped). Net = **33,566.39**.

**H16** man, single, S 60,130 (annual 721,560 exactly: s 121B "עלתה על" not met).
R = 12,363.5 + 47% × 13,440 = 18,680.3; no additional tax. tax/m = 18,135.8; annual 217,629.6. D 3,174.6012; H 2,534.3088. Net = **36,285.29**.

**H17** man, single, S 70,000 (additional tax).
R = 12,363.5 + 47% × 23,310 = 23,319.2; s 121B 3% × 9,870 = 296.1; total 23,615.3. tax/m = 23,070.8; annual 276,849.6. D, H capped. Net = **41,220.29**.

**H35** man, single, S 12,000 (baseline for the family cases).
R = 1,128 + 20% × 1,940 = 1,516. tax/m = 971.5; annual 11,658. D = 80.1112 + 7% × 4,297 = 380.9012. H = 248.8069 + 5.17% × 4,297 = 470.9618. Net = **10,176.637**.

**H37** woman, married (husband no income), no children, S 12,000.
P = 2¾. tax/m = 1,516 − 665.5 = 850.5; annual 10,206. Net = **10,297.637**. (Marriage alone changes nothing: s 37 needs a "יחיד מוטב".)

### Group B — one to five children; the man/woman difference in s 66(c)(4)/(5)

**H18** woman, married, 1 child born 2018-03-10 (turns 8 in 2026), S 12,000.
P = 2¾ + 2 (s 66(c)(4)(a), 6 to 17) = 4¾ → 1,149.5. tax/m = 1,516 − 1,149.5 = 366.5; annual 4,398.
D 380.9012; H 470.9618. Allowance: 1 child, counted to the father (s 67(b)), who has no additional-tax income → 173.
Net = 12,000 − 366.5 − 380.9012 − 470.9618 + 173 = **10,954.637**.

**H19** man, married, same child, S 12,000.
P = 2¼ + 1 (s 66(c)(5)(c)) = 3¼ → 786.5. tax/m = 729.5; annual 8,754. Allowance 173. Net = **10,591.637**.

**H20** woman, married, children born 2024-05-01 (turns 2) and 2019-09-01 (turns 7), S 15,000.
R = 1,128 + 20% × 4,940 = 2,116. P = 2¾ + 4½ + 2 = 9¼ → 2,238.5 > 2,116 → tax/m **0**; annual 0 (credits do not go negative).
D = 80.1112 + 7% × 7,297 = 590.9012. H = 626.0618. Allowance 173 + 219 = 392. Net = **14,175.037**.

**H21** man, married, same two children, S 15,000.
P = 2¼ + 4½ + 1 = 7¾ → 1,875.5. tax/m = 240.5; annual 2,886. Allowance 392. Net = **13,934.537**.

**H22** man, married, children born 2026-02-14 (birth year), 2023-07-01 (turns 3), 2012-01-15 (turns 14), S 20,000.
R = 2,916 + 31% × 1,000 = 3,226. P = 2¼ + 2½ + 3½ + 1 = 9¼ → 2,238.5. tax/m = 987.5; annual 11,850.
D = 80.1112 + 7% × 12,297 = 940.9012. H = 884.5618. Allowance 173 + 219 + 219 = 611. Net = **17,798.037**.

**H23** woman, married, children born 2010-04-01 (16), 2013-04-01 (13), 2016-04-01 (10), 2021-04-01 (turns 5), S 9,000.
R = 701 + 14% × 1,990 = 979.6. P = 2¾ + 2 + 2 + 2 + 2½ = 11¼ → 2,722.5 → tax/m **0**.
D = 80.1112 + 7% × 1,297 = 170.9012. H = 315.8618. Allowance 173 + 3 × 219 = 830. Net = **9,343.237**.

**H24** man, married, five children born 2009-02-01 (turns 17), 2011, 2014, 2017, 2020-02-01 (turns 6), S 30,000.
R = 4,807 + 35% × 4,900 = 6,522. P = 2¼ + 5 × 1 = 7¼ → 1,754.5. tax/m = 4,767.5; annual 57,210.
D = 80.1112 + 7% × 22,297 = 1,640.9012. H = 1,401.5618. Allowance 173 + 219 + 219 + 219 + 173 = 1,003. Net = **23,193.037**.

### Group C — a child turning 18, a child born in the month (s 72, a gap)

**H25** woman, married, children born 2008-06-10 (turns 18 on 10 June 2026) and 2015-03-01, S 12,000, **June 2026**.
P = 2¾ + ½ (year of majority, s 66(c)(4)(a)) + 2 = 5¼ → 1,270.5. tax/m = 245.5; annual 2,946.
Allowance June: entitlement for the elder ceased in June; s 72(a) "תשלום הקצבה יסתיים ביום האחרון של החודש שבו נפסקה הזכאות" → both counted → 392.
Net = 12,000 − 245.5 − 380.9012 − 470.9618 + 392 = **11,294.637**.

**H26** the same household, **July 2026**. Tax unchanged (annual). Allowance: one child → 173. Net = **11,075.637**.

**H44** man, married, one child born 2008-11-01 (turns 18 in November), S 12,000.
P = 2¼ + 0 (s 66(c)(5) gives the father nothing in the year of majority) → tax/m 971.5; annual 11,658.
June 2026: child is 17 → allowance 173 → net **10,349.637**.
**H44b** same, **December 2026**: entitlement ceased in November → allowance 0 → net **10,176.637**.

**H27** man, married, child born 2019-01-05 and a newborn born **2026-09-15**, S 12,000, **September 2026**.
P = 2¼ + 1 + 2½ (birth year) = 5¾ → 1,391.5. tax/m = 124.5; annual 1,494.
Allowance September: entitlement arose on the 15th, "עד 15 בחודש" → from 1 September → 2 children → 392. Net = **11,415.637**.

**H28** the same, newborn born **2026-09-16**, September 2026. Tax as H27. Allowance from 1 October → 173. Net = **11,196.637**.

**H29** the H28 household in **March 2026** (before the birth). Tax/m 124.5 (annual points of the birth year in every month, per the brief's one-twelfth rule). Allowance 173. Net = **11,196.637**. (Guess about design: the source fixes the annual tax, the brief fixes "one twelfth".)

### Group D — high income, and the s 66 exclusion from child allowance

**H30** man, married, children born 2016-04-01 and 2019-04-01, S 70,000.
Rates + additional tax 23,615.3 (as H17). P = 2¼ + 1 + 1 = 4¼ → 1,028.5. tax/m = 22,586.8; annual 271,041.6.
Allowance: counting parent is the father (s 67(b)), who has income subject to additional tax → s 66 excludes him → **0**.
Net = 70,000 − 22,586.8 − 3,174.6012 − 2,534.3088 = **41,704.29**.

**H31** woman, married (husband no income), same children, S 70,000.
P = 2¾ + 2 + 2 = 6¾ → 1,633.5. tax/m = 21,981.8; annual 263,781.6.
Allowance: the counting parent is the husband, who has no additional-tax income → 392 (paid to the mother, s 69(a)).
Net = 70,000 − 21,981.8 − 3,174.6012 − 2,534.3088 + 392 = **42,701.29**. (My reading of ss 66, 67(b); medium confidence.)

**H33** man, married, one child born 2016-04-01, S 60,130 (annual exactly 721,560, not "עלתה על").
R = 18,680.3. P = 3¼ → 786.5. tax/m = 17,893.8; annual 214,725.6. Allowance 173. Net = **36,700.29**.

**H34** the same, S 60,131.
R = 12,363.5 + 47% × 13,441 = 18,680.77, plus 3% × 1 = 0.03 → 18,680.8. tax/m = 17,894.3; annual 214,731.6. Allowance **0** (s 66). Net = **36,527.79**.

**H32** woman, single, one child born 2016-04-01, S 70,000.
Tax: **declined** (s 40(b) single-parent points; see §1.1). D = 3,174.6012 (answerable). Allowance: child is with the mother only → her count; she has additional-tax income → **0**.

### Group E — single parents with children (s 40 is outside the rows)

**H36** woman, single, children born 2016-04-01 and 2019-04-01, S 12,000.
Tax: **declined** (s 40(b)). D = 380.9012. Allowance 392 (counted to her). Net: declined, because the tax is.

**H36m** man, single, one child born 2016-04-01 living with him, S 12,000.
Tax: **declined** (s 40(b)). D = 380.9012. Allowance 173.

### Group F — the period, and what the capstone must decline

**H38** H35's facts in **December 2025** → the capstone **refuses** by name (brief: "refuses every other [period] by name"). Also tax year 2025 refused.
**H39** H35's facts in **January 2027** → **refuses**; tax year 2027 refused. (Note the ITO figures are frozen through 2027 by s 120B(e) and the brackets are annotated "2026–2027", so the 2027 tax is arguably answerable from the source; the refusal is the brief's scope, not the law's.)
**H40** H35's facts in **January 2026** and in **December 2026** → same as H35 (both ends of the period answer).
**H41** H35's facts with a pension contribution giving a s 45A credit / s 47 deduction → tax **declined** (brief: "that is an input and the capstone declines the tax"). NI still 380.9012.
**H42** H35's facts for a new immigrant (s 35 points) → tax **declined**. (Guess: same mechanism as H41.)
**H43** a non-resident earner → **declined** (guess; the household is pinned as resident, and s 34 / s 36 / NII s 65 all turn on residence).
**H45** man, single, S 5,000 (guess: below a full-time minimum wage). Tax: R = 500, credits 544.5 → 0. D = 1.04% × 5,000 = 52 if the capstone applies the actual salary; s 348(b) would lift it to the Schedule K minimum (the minimum wage "לגבי עובד פלוני", which the bundle does not fix, and which may be a partial minimum wage). **Guess: 52; I would accept a refusal.** H = 161.5. Net 4,786.5.
**Health**: never computed by the capstone; always an input (brief). Expect the input to pass through unchanged into the net.

## 3. Count

Decided households: **48 rows** — H01 to H47 (H46 unused) plus H36m and H44b.
40 carry full figures (H01–H31, H33–H35, H37, H40, H44, H44b, H45, H47); 8 are a decided decline or refusal (H32 and H36/H36m for the tax, H38, H39, H41, H42, H43), of which H32, H36 and H36m still carry figures for the contribution and the allowance.
Marked as guesses (the source does not decide, or the capstone's mechanism is unknown): H29 (one-twelfth design), H32/H36/H36m (decline mechanism for s 40), H41, H42, H43 (decline mechanism), H45 (minimum income) — **8 households**; and two cross-cutting guesses, that the net includes the allowance and that nothing is rounded.
Medium-confidence readings that I nonetheless assert as the source's answer: s 66(c)(1a) for the sole earner (H18–H31), s 67(b) with s 66 for H30/H31/H34, s 72 inclusive "עד 15" (H27), and the s 19(6) heading (H05, H47).

## Revised after seeing the encoding

Everything above this heading is unchanged from the version finished at 2026-10-06T23:46:05Z (a frozen copy, sha256 `c86ba4cf857df741f334b26df637b2383a61dafa453b60756d60b5a26a8d3591`, was taken at that moment).
This section only adds; it changes no expected value above.

### Added households

- **H44n** — the H44 household (man, married, one child born 2008-11-01, S 12,000) in **November 2026**, the month of the 18th birthday, which falls on the 1st.
  Added after reading the IL-06 adapter, which asks IL-06 about the family on the first day of the month and declines only a birth or 18th birthday falling *after* the 1st.
  Expected from my pre-encoding reading of s 72(a) in section 1.4 ("a child who turns 18 counts for the whole month of the 18th birthday and not after"): allowance **173**, net **10,349.637** (as H44 in June).
- **H40a / H40d** — H40 split into its two months (January and December 2026); expected values as written for H40.
- **H45b** — the H45 earner with "the full monthly minimum wage of an employee aged 18 or over applies" set FALSE, an input the capstone needs that I did not foresee; my pre-encoding note "I would accept a refusal" is asserted as a refusal of the contribution.

### Inputs the capstone needs that my households did not state

- The earner's date of birth (I gave 1990-01-01, age 36, as section 2's "aged 35" intended), and for a woman the Schedule A1 Part D age in months (I gave 840, 70 years, which cannot bind at 36).
- Whether the earner is the registered spouse (I gave TRUE: the sole earner, ITO s 64B(a)) and whether the earner claims the separate calculation (TRUE, per my s 66(c)(1A) reading).
- Whether each spouse at home is insured under Chapter 11 / a s 238 housewife: a wife at home I gave as a housewife, not insured; a husband at home as insured.

### An input I got wrong, corrected without touching any expected value

In my first run every child was named "Child".
Row IL-06 tells children apart by name, so every household with two or more children had its allowance refused ("IL-06 reports that the household's facts cannot describe a family on the day").
The deposited `tests-independent.l4` names them "Child 1", "Child 2", …; no `#ASSERT` line changed between the two runs.

### Readings I now think were wrong (the expected values above stand, and fail)

- **H45**: s 348(b) does lift the income to the Schedule K minimum when the full adult minimum wage applies, as I half-said above; the capstone's 67.01604 (1.04% × 6,443.85) is the source's answer, my 52 is not.
- **H43, the tax half**: ss 34 and 36 give a non-resident no points and s 121 still applies, so the tax is answerable (18,192 a year); only the national insurance half of my "declined" stands.
- **Column D above the threshold**: I took 7.00% from the printed total of column D and from the Institute's published rate, and did not add up the branch figures, which sum to 4.67%. I still think 7.00% is the right answer, but the deposited table is inconsistent with itself, and I did not notice that before seeing the encoding.
