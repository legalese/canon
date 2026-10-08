Finished (pre-encoding reading): Tue Oct  6 21:49:13 UTC 2026

# IL-05 decided answers: National Insurance Law ss 342, 348 and Schedule K

Written by the independent test author (fid-il-05) **before opening any `.l4` file, `NOTES.md`, `encoding.json` or `check.sh` in the encoding directory.**
The only file read in the encoding directory before this was finished is `BRIEF.md`, plus a plain `ls`.

Sources read:

- `SRC` = `registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt` (Wikisource consolidation, sha256 `78bf47ee…2a97`); line numbers below are into it.
  Read: s 1 (120-228), s 2 (230-239), s 334 (3601-3608), s 335-337 (3610-3629, for context), s 342 (3658-3675), s 344-345 (3684-3734, context), s 348 (3762-3769), Schedule J (4709-4749), Schedule K (4751-4773).
- `A252` = Amendment No. 252 and temporary provision, Sefer HaChukim 5785 p 176 (`25_lsr_5482787.pdf`), read as page images.
- `B2025` = 2025 Budget-year Law, Sefer HaChukim 3384 p 386ff (`25_lsr_6133485.pdf`), Part E (פרק ה׳) s 19-21 on PDF pages 11-12 (printed pp 395-396), read as page images.
  Note: `SOURCES.json` says this PDF has 5 pages; `pdfinfo` reports 40, and Part E is on PDF pages 11-12.
- `BTL` = National Insurance Institute pages, fetched 2026-10-06 21:41-21:43 UTC through the Israeli proxy (saved under this scratch directory, `btl-dl/`):
  - average wage: `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%d7%a9%d7%9b%d7%a8%20%d7%9e%d7%9e%d7%95%d7%a6%d7%a2.aspx` (sha256 `9d993deb…bb9d82`): "השכר הממוצע החל מ- 01.01.2026: לפי סעיף 1 בחוק - קצבאות: 13,566 ש"ח לפי סעיף 1 בחוק - דמי ביטוח: 13,566 ש"ח / לפי סעיף 2 בחוק - קצבאות: 13,769 ש"ח / לפי סעיף 2 בחוק - דמי ביטוח: 13,769 ש"ח"; row 1.01.2025: §1 13,153 / 12,379, §2 13,316 / 12,536; row 1.01.2024: §1 12,379 / 12,379, §2 12,536 / 12,536.
  - salaried rates: `https://www.btl.gov.il/Insurance/Rates/Pages/%D7%9C%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D%20%D7%A9%D7%9B%D7%99%D7%A8%D7%99%D7%9D.aspx`: "מדרגת גביה מופחתת … 7,703 ש"ח (החל ב- 01.01.2026) … ההכנסה המרבית … 51,910 ש"ח (החל ב- 01.01.2026)"; employee NI 1.04% below.
  - self-employed rates: `…/Insurance/Rates/Pages/%d7%9c%d7%a2%d7%a6%d7%9e%d7%90%d7%99%d7%9d.aspx` (sha256 `2af8d88c…dd85499`): "מי שהכנסתו נמוכה מ- 3,442 ש"ח לחודש, ישלם דמי ביטוח מהכנסה מזערית".
  - non-working: `…/Insurance/Rates/Pages/%d7%9e%d7%99%20%d7%a9%d7%90%d7%99%d7%a0%d7%9d…aspx` (sha256 `996733f5…2c2ade`): "הכנסה עד 3,442 ש"ח בחודש פטורה … 8,558 ש"ח (3,442 - 12,000)"; no-income non-working pays 143 NIS/month NI.
  - minimum wage: `…/Mediniyut/GeneralData/Pages/%d7%a9%d7%9b%d7%a8%20%d7%9e%d7%99%d7%a0%d7%99%d7%9e%d7%95%d7%9d.aspx` (sha256 `85dfbb83…a39c2a3f39`): monthly 6,443.85 from 01.04.2026; 6,247.67 from 01.04.2025.

## 0. What the amending Laws change, and what the consolidation already carries

- `B2025` s 19(2) inserts into s 334(a) "מדרגת גבייה מופחתת – סכום של 7,522 שקלים חדשים, כשהוא מעודכן ב־1 בינואר של כל שנה": 2026-2028 by CPI, 2029 on by the average wage. `SRC` 3605 carries this, with the editor's note "בשנת 2026, 7,703 ש״ח".
- `B2025` s 19(4): "בסעיף 342, בכל מקום, במקום "60% מהשכר הממוצע" יבוא "מדרגת הגבייה המופחתת", ובמקום "מ־60% מהשכר הממוצע" יבוא "ממדרגת הגבייה המופחתת"". `SRC` 3669, 3673-3674 carry the new wording.
- `B2025` s 19(6): "בלוח י׳, בכל מקום, במקום "60% מהשכר הממוצע" יבוא "מדרגת הגבייה המופחתת כהגדרתה בסעיף 334(א)"".
- `B2025` s 20: in `A252` s 7(a)(3)(A), column C of Schedule J, "0.17" becomes "0.16"; in s 7(b) the Treasury percentages change.
- `B2025` s 21: "תחילתו של פרק זה ביום י״ב בטבת התשפ״ו (1 בינואר 2026)".
- `A252` s 7(a): temporary provision "לעניין דמי ביטוח לאומי שייגבו בעד השנים 2025 ו־2026 … בתקופה שמיום התחילה עד יום כ״א בטבת התשפ״ז (31 בדצמבר 2026)": Schedule J col C sub-column "על החלק שאינו עולה על 60% מהשכר הממוצע" and col D sub-column "על חלק השכר שאינו עולה על 60% מהשכר הממוצע" are replaced. New col D (not-exceeding) column: 0.10, –, –, –, 0.03, 0.02, –, 0.29, 0.03, 0.57, total 1.04. `A252` s 6: commencement 1 January 2025. `A252` s 7(b): the Finance Minister may extend by order for 2027 and 2028.
- `A252` does **not** amend s 342, s 348 or Schedule K.
- Consolidation discrepancy found: in the **temporary** Schedule J table (`SRC` 4718), col D's first sub-heading still reads "על חלק השכר העולה על 60% מהשכר הממוצע", while the permanent table (`SRC` 4736) reads "…העולה על מדרגת הגבייה המופחתת…". `B2025` s 19(6) ("בכל מקום") replaced it from 1 Jan 2026; the consolidation's temporary table is stale in that one heading. See J2.

## 1. Inputs I chose (figures the Law does not print)

| name | value | source |
|---|---|---|
| basic amount, s 1 para (3), 2026 | 10,382 | `SRC` 191 editor's note "בשנת 2026, 10,382 ש״ח"; corroborated by BTL max 51,910 = 5 × 10,382 |
| average wage for contributions (s 1 as modified by s 2(b)), from 1 Jan 2026 | 13,769 | BTL average-wage page, "לפי סעיף 2 בחוק - דמי ביטוח" |
| average wage per s 1 unmodified, from 1 Jan 2026 | 13,566 | BTL; `SRC` 226 note. Used only to detect the wrong one |
| average wage for contributions, 2025 | 12,536 | BTL row 1.01.2025, s 2 contributions |
| reduced collection bracket, 2026 | 7,703 | BTL; `SRC` 3605 editor's note. The Law prints 7,522 plus a CPI update |
| monthly minimum wage, Jan-Mar 2026 (in force from 1 Apr 2025) | 6,247.67 | BTL minimum-wage page |
| monthly minimum wage, from 1 Apr 2026 | 6,443.85 | BTL minimum-wage page |
| hypothetical average wage after a compensation update on 1 Apr 2026 | 14,000 | invented input, for F8 only |

Schedule J figures used (`SRC` 4715-4730, temporary text for 2025-2026, as amended by `A252` and `B2025` s 20):
col D (employee deduction) total 7.00 above the bracket, 1.04 below; item 6 (unemployment) col D 0.21 above, 0.02 below.
Col C self-employed: 12.83 above, 4.47 below.
Permanent col D (`SRC` 4748): 7.00 above, 0.40 below.

## 2. Which average wage each provision uses, and why

- **s 348(a1)** (25% of the average wage), **Schedule K items 2, 3, 4** (25%, 5%, 15% of the average wage): the s 1 definition **as modified by s 2(b)**, because s 2(b) says "בחישוב השכר הממוצע, לצורך גמלאות ודמי ביטוח, יחולו שינויים אלה" — these are contribution provisions. 2026: 13,769, not 13,566.
  Supporting: Schedule K1 (`SRC` 4781-4783), which is about a penalty charge and not about benefits or contributions, has to say "השכר הממוצע כמשמעותו בסעיף 2(ב)" explicitly; s 2(b) reaches contributions without being named. BTL's own figures agree (3,442 = 25% × 13,769).
- **The pre-2026 s 342 threshold, "60% מהשכר הממוצע"**: same, s 2(b)-modified; 2025: 60% × 12,536 = 7,521.60.
- **Schedule K item 1 maximum, items 2-4 maximum**: no average wage at all; the basic amount of s 1 para (3) (`SRC` 4773: "”הסכום הבסיסי“ – כהגדרתו בפסקה (3) שבהגדרה … שבסעיף 1"), × 5.
- **Schedule K item 1 minimum**: no average wage; the minimum wage of the first month of the quarter.

## 3. Scenarios and decided answers

Unless stated, the period is a month or quarter in 2026 and the inputs of section 1 apply.
"Counted income" means the income on which contributions are charged after s 348.

### A. Who is liable, s 342(a)-(b)

| id | facts | expected | licence |
|---|---|---|---|
| A1 | insured, self-employed | liable to pay for himself: TRUE | 342(a) "מבוטח שהוא עובד עצמאי … חייבים בתשלום דמי ביטוח בעד עצמם" |
| A2 | insured, neither employee nor self-employed | liable for himself: TRUE | 342(a) "ומבוטח שאינו עובד ואינו עובד עצמאי" |
| A3 | woman insured under Chapter C (maternity) **only** because she is the wife of an insured | not liable: FALSE | 342(a) "ואולם מבוטחת לפי פרק ג׳ בלבד מכוח היותה אשת מבוטח אינה חייבת" |
| A4 | woman insured under Chapter C as a wife **and** insured on another footing (e.g. herself a non-working insured under Chapter K) | proviso does not reach her ("בלבד"): liable, TRUE | 342(a) "בלבד" |
| A5 | employee | the employer is liable for the employee: TRUE; the employee is not liable for himself under (a) | 342(b) "המעביד חייב בתשלום דמי ביטוח בעד עובדו" |
| A6 | employee of two employers | each employer pays as if it alone were the employer; (d) and (e) apply to the employee | 342(b) "ישלם כל אחד מהם את דמי הביטוח כאילו הוא בלבד היה מעבידו" |
| A7 | employee who is also self-employed | employer liable for the wage; the person liable for himself on the self-employed income | 342(a)+(b), (f) |

### B. The employee deduction, s 342(c) with Schedule J column D (temporary text 2025-2026), February 2026, bracket 7,703

The deduction is "אחוזים מההכנסה שלפיה משתלמים דמי הביטוח כאמור בלוח י׳" (342(c)(1)), i.e. column D, whose heading is "הניכוי משכר העובד לענין סעיף 342(ג)".
The income is capped by s 348(a) because 342(c)(1) charges on "ההכנסה שלפיה משתלמים דמי הביטוח".
All wages below are at or above the employee's applicable minimum wage, so s 348(b) does not move them.

| id | wage (month) | expected deduction | working |
|---|---|---|---|
| B1 | 7,000 | 72.80 | 7,000 × 1.04% |
| B2 | 7,702 (bracket − 1) | 80.1008 | 7,702 × 1.04% |
| B3 | 7,703 (at bracket) | 80.1112 | 7,703 × 1.04% |
| B4 | 7,704 (bracket + 1) | 80.1812 | 80.1112 + 1 × 7% |
| B5 | 8,000 | 100.9012 | 80.1112 + 297 × 7%; see J2 |
| B6 | 10,000 | 240.9012 | 80.1112 + 2,297 × 7% |
| B7 | 51,910 (at max) | 3,174.6012 | 80.1112 + 44,207 × 7% |
| B8 | 60,000 (above max) | 3,174.6012 | capped at 51,910 by 348(a) |
| B9 | police officer (or prison guard), 10,000 | 234.5369 | item 6 excluded: 7,703 × 1.02% + 2,297 × 6.79%; 342(c)(2) "לא ינוכה משכרם הניכוי כאמור בפרט 6 ללוח י׳" |
| B10 | man aged 70, no old-age pension, 10,000 | 0 | 342(c)(2) "ובעד הזמן שלאחר הגיע המבוטח לגיל 70 שנים בגבר … אף אם לא מגיעה למבוטח קצבת אזרח ותיק" |
| B11 | man aged 69, receiving old-age pension, 10,000 | 0 | 342(c)(2) "בעד הזמן שבעדו מגיעה למבוטח קצבת אזרח ותיק" |
| B12 | man aged 69, no pension, 10,000 | 240.9012 | (c)(1) applies |
| B13 | woman aged 68, no pension | **REFUSE** unless the Part D Schedule A1 age is supplied as an input: the age is "הגיל הקבוע לגביה, בהתאם לחודש לידתה, בחלק ד׳ בלוח א׳1", which is outside the sources | 342(c)(2) |
| B14 | man aged 70: may the employer reduce its own contributions by what it would have deducted? | TRUE | 342(c)(2) "ואולם המעביד רשאי להפחית מדמי הביטוח שהוא חייב בהם את הסכומים שהיה מנכה" |

### C. Several employers, s 342(d), February 2026

"Coordinated contributions" are the deduction that would have been made from the total monthly income had one employer paid it (so 348(a) caps it).

| id | facts | expected |
|---|---|---|
| C1 | two employers, 7,000 each | actual deduction 145.60 (72.80 × 2); coordinated on 14,000 = 520.9012; employee **owes** 375.3012 (342(d)(1) "יהיה העובד חייב בתשלום ההפרש") |
| C2 | two employers, 40,000 each | actual 4,681.8024 (2,340.9012 × 2); coordinated on 80,000 capped to 51,910 = 3,174.6012; employee **refunded** 1,507.2012 (342(d)(2) "יהיה העובד זכאי להחזר ההפרש") |
| C3 | two employers whose wages sum to ≤ the bracket, each at or above its applicable (partial) minimum | difference 0 |

### D. Employee who is also self-employed, s 342(f), a month in 2026, bracket 7,703

342(f)(1): the self-employed reduced rate does not apply to the s 2(1)/(8) income. 342(f)(2): "היתה ההכנסה … מהמקורות המפורטים בסעיף 2(2) … נמוכה ממדרגת הגבייה המופחתת יחול השיעור המופחת, על סכום הכנסתו מהמקורות … 2(1) ו־(8) … השווה לסכום ההפרש שבין הכנסתו מהמקורות … 2(2) … לבין מדרגת הגבייה המופחתת".

| id | wage | self-employed income | expected reduced-rate portion | full-rate portion |
|---|---|---|---|---|
| D1 | 5,000 | 6,000 | 2,703 | 3,297 (contribution at 4.47% / 12.83% = 543.8292) |
| D2 | 7,703 (at bracket; not "נמוכה") | 6,000 | 0 | 6,000 |
| D3 | 7,702 | 6,000 | 1 | 5,999 |
| D4 | 2,000 | 3,000 | 3,000 (the income is smaller than the 5,703 difference) | 0 |
| D5 | 9,000 | 1,000 | 0 | 1,000 |

### E. Maximum, s 348(a) with Schedule K, 2026

348(a): "לא יבוא בחשבון סכום ההכנסה של המבוטח העולה על הסכום המרבי".
Item 1 (employee): "לחודש – הסכום הבסיסי, כפול 5; לרבעון – … כפול 3; לשנה – … סך ההכנסות המרביות בכל רבעון".
Item 2 (self-employed): "לרבעון – … חמש פעמים הסכום הבסיסי, כפול 3; לשנה – סך …" (no monthly row).
Items 3 and 4: "לרבעון או לשנה" equal to item 1 / item 2 respectively (no monthly row).

| id | item / period | bound | income → counted |
|---|---|---|---|
| E1 | item 1, month | 51,910 | 51,909 → 51,909; 51,910 → 51,910; 51,911 → 51,910 |
| E2 | item 1, quarter | 155,730 | 155,729 → 155,729; 155,730 → 155,730; 155,731 → 155,730 |
| E3 | item 1, year 2026 | 622,920 | 622,919 → 622,919; 622,921 → 622,920 |
| E4 | item 2, quarter | 155,730 | same pattern as E2 |
| E5 | item 2, year | 622,920 | same pattern as E3 |
| E6 | item 3, quarter / year | 155,730 / 622,920 | same as item 1 |
| E7 | item 4, quarter / year | 155,730 / 622,920 | same as item 2 |
| E8 | item 2, 3 or 4, **month** | **REFUSE**: Schedule K prints no monthly maximum for them | — |

### F. Minimum, s 348(b) with Schedule K, 2026, average wage 13,769

348(b): "מבוטח שאין לו הכנסה או שהכנסתו אינה מגיעה לסכום המזערי … ישתלמו בעדו דמי הביטוח כאילו הכנסתו היתה הסכום המזערי".

| id | item / period | bound | income → counted |
|---|---|---|---|
| F1 | item 1, month in Q1 (Jan, Feb or Mar 2026): minimum wage of January 2026 | 6,247.67 | 0 → 6,247.67; 6,247.66 → 6,247.67; 6,247.67 → 6,247.67; 6,247.68 → 6,247.68 |
| F2 | item 1, month in Q2 (April or May 2026): minimum wage of April 2026 | 6,443.85 | 6,443.84 → 6,443.85 |
| F3 | item 1, quarter Q1 / Q2 2026 | 18,743.01 / 19,331.55 | 18,743.00 → 18,743.01; 18,743.02 → 18,743.02 |
| F4 | item 1, year 2026 (Q1 at 6,247.67, Q2-Q4 at 6,443.85) | 76,737.66 | 76,737.65 → 76,737.66 |
| F5 | item 2, quarter: "25% מהשכר הממוצע של החודש הראשון ברבעון, כפול 3" | 10,326.75 | 0 → 10,326.75; 10,326.74 → 10,326.75; 10,326.76 → 10,326.76 |
| F6 | item 2, year | 41,307.00 | 41,306.99 → 41,307.00 |
| F7 | item 3, quarter: 5% × 13,769 × 3 | 2,065.35 | 2,065.34 → 2,065.35; 2,065.36 → 2,065.36 |
| F8 | item 3, year | 8,261.40 | |
| F9 | item 4, quarter: 15% × 13,769 × 3 | 6,196.05 | 6,196.04 → 6,196.05; 6,196.06 → 6,196.06 |
| F10 | item 4, year | 24,784.20 | (BTL's 143 NIS/month = 2,065.35 × 6.92% corroborates item 4 at 15%) |
| F11 | wrong-average-wage detector: items 2/3/4 computed on 13,566 would give 10,174.50 / 2,034.90 / 6,104.70 | must **not** be these | s 2(b) |

**F12: an average wage that moves mid-year.** Input: the average wage is 13,769 in January and becomes 14,000 from 1 April 2026 (a compensation update, s 1 "ואם חל פיצוי לאחר מכן – 1 בחודש שבו חל הפיצוי") and stays 14,000 through October.

| id | expected | licence |
|---|---|---|
| F12a | item 2, Q2 minimum = 10,500.00 (uses April's 14,000) | item 2 "של החודש הראשון ברבעון" |
| F12b | item 4, Q2 minimum = 6,196.05 (uses **January's** 13,769) | item 4 "לרבעון שתחילתו ב־1 בינואר, ב־1 באפריל וב־1 ביולי … 15% מהשכר הממוצע של החודש הראשון ברבעון שתחילתו ב־1 בינואר" |
| F12c | item 3, Q3 minimum = 2,065.35 (January's) | item 3, same words with 5% |
| F12d | item 4, Q4 minimum = 6,300.00 (October's 14,000) | "ולרבעון שתחילתו ב־1 באוקטובר … של החודש הראשון שבאותו רבעון" |
| F12e | item 3, Q4 minimum = 2,100.00 | same |
| F12f | annual minima: item 2 = 41,826.75; item 3 = 8,296.05; item 4 = 24,888.15 | "סך ההכנסות המזעריות שבכל רבעון" |

### G. Disregarded non-work income, s 348(a1), 2026, 25% × 13,769 = 3,442.25

348(a1): "לא תובא בחשבון ההכנסה של מבוטח מהמקורות המפורטים בסעיף 2 לפקודת מס הכנסה, שאינה הכנסה מעבודתו כעובד או כעובד עצמאי, אשר אינה פטורה מתשלום דמי ביטוח לפי סעיף 350 ואינה עולה על סכום השווה ל־25% מהשכר הממוצע".

My reading: **the first 25% of the average wage of such income is disregarded (a deduction, not a cliff).**
Why: the same construction in 348(a), "סכום ההכנסה … העולה על הסכום המרבי", is a portion; a cliff would make 3,442.26 of rent cost contributions on all of it while 3,442.25 costs nothing.
This is a **genuine ambiguity**: "ההכנסה … אשר … אינה עולה על" can also be read as a condition on the whole income (a cliff). BTL applies the deduction reading ("8,558 ש"ח (3,442 - 12,000)").

| id | monthly non-work income | expected counted (deduction reading) | cliff reading |
|---|---|---|---|
| G1 | 3,000 | 0 | 0 |
| G2 | 3,442.25 (at) | 0 | 0 |
| G3 | 3,442.26 (just above) | 0.01 | 3,442.26 |
| G4 | 3,400 (between 25% of 13,566 and of 13,769) | 0 (proves s 2(b) wage) | 0 |
| G5 | 12,000 | 8,557.75 | 12,000 |
| G6 | 3,000 of **wages** (income from work as an employee) | 3,000: (a1) does not apply ("שאינה הכנסה מעבודתו כעובד או כעובד עצמאי") | |
| G7 | 3,000 that is exempt under s 350 | (a1) does not apply (it is exempt already); s 350 is out of scope, so REFUSE or take exemption as input | |
| G8 | non-working insured, non-work income 3,000 in each month of Q1 2026 | counted 0 by (a1), then 348(b) raises to the item 4 quarterly minimum 6,196.05 | 348(a1) then (b) |
| G9 | (a1) applied to a **quarterly or annual** income | the text gives a monthly-sized amount and does not say how it scales to a quarter or a year: preferred **REFUSE**, acceptable: monthly × 3 / × 12 with a recorded fork | 348(a1) |

### H. Deeming rules, s 348(d) and (e)

| id | facts | expected | licence |
|---|---|---|---|
| H1 | received unemployment benefit for a full month; asked for the deemed **monthly** income | **REFUSE**: (d) speaks of a month ("לחודש מלא") but item 3 prints only "לרבעון … ולשנה"; internal inconsistency | 348(d), Schedule K item 3 |
| H2 | received unemployment benefit for full months throughout Q1 2026, quarterly figure | deemed quarterly income 2,065.35 | 348(d) "ישלם דמי ביטוח כאילו היתה הכנסתו הסכום המזערי הקבוע בפרט 3" |
| H3 | as H2 but with other income 5,000 in the quarter | literal (d) is unconditional (no "אינה מגיעה" limb, unlike (e)): deemed 2,065.35; flagged as an odd literal result | 348(d) |
| H4 | yeshiva student, no income, Q1 2026 | deemed 2,065.35 (both the permanent and the temporary text) | 348(e) "תלמיד במוסד תורני או בישיבה … שאין לו הכנסה" |
| H5 | yeshiva student, quarterly income 2,065.34 | 2,065.35 | 348(e) "שהכנסתו אינה מגיעה לסכום המזערי" |
| H6 | yeshiva student, quarterly income 3,000 | 3,000; item 3, not item 4, governs him. **Genuine ambiguity**: if the class in (e) includes its income limb, he is "מבוטח אחר" and 348(b) would raise him to 6,196.05 | 348(e), Schedule K items 3-4 |
| H7 | national-civic service participant ("משרת בשירות לאומי–אזרחי"), no income, Q1 2026 | within the temporary text of (e): deemed 2,065.35 | `SRC` 3769 temporary text |
| H8 | same participant, service began 1 March 2026 and continues, Q4 2026 | still within (e): "חלה גם על מי שהתחיל את שירותו לפני המועד האמור גם אחרי המועד האמור עד שייסים את שירותו": 2,065.35 | `SRC` 3769 |
| H9 | participant whose service began 1 September 2026, Q4 2026 | **not** within (e): the permanent text (`SRC` 3768) does not list "משרת בשירות לאומי–אזרחי" and the service did not begin before 31.8.2026; as a no-income non-working insured, the item 4 minimum 6,196.05 applies | `SRC` 3768-3769 |
| H10 | participant whose service began on 31 August 2026 itself, Q4 2026 | not "לפני המועד האמור": not within (e) after the date | `SRC` 3769 |
| H11 | national-service volunteer (permanent text), no income, Q4 2026 | deemed 2,065.35 | `SRC` 3768 "מתנדב בשירות לאומי או בהתנדבות קהילתית" |

### I. Dated arms and commencement

| id | facts | expected | licence |
|---|---|---|---|
| I1 | s 342(f)(2) or the deduction bands for a period in **December 2025** | the text then in force said "60% מהשכר הממוצע" (= 7,521.60 on 12,536), not the bracket. Preferred: **REFUSE** (outside the row's vintage, which starts January 2026). Acceptable: 7,521.60. **Wrong**: 7,703 or 7,522 | `B2025` s 19(4), s 21 |
| I2 | the same on 1 January 2026 | bracket 7,703 | `B2025` s 21 |
| I3 | the employee deduction for 2027 | temporary Schedule J ends 31.12.2026 (`A252` s 7(a)) unless extended by order (s 7(b)); whether an order was made is not in the sources. Preferred: **REFUSE**. If the encoding uses the permanent text: 0.40% below / 7.00% above | `A252` s 7 |
| I4 | s 348(e) national-civic service: in force until 31.8.2026 with the tail in H8 | dated arm: H7-H10 | `SRC` 3769 |
| I5 | the bracket itself | 7,522 updated 1 Jan 2026-2028 by CPI, from 2029 by the average wage; 2026 value is a published input (7,703) | `SRC` 3605-3607, `B2025` s 19(2) |

### J. Internal inconsistencies

| id | what | expected |
|---|---|---|
| J1 | 342(e)(3)-(4) refer to "טור ה׳ בלוח י׳" for the rate on an employee's income above the bracket; column E (`SRC` 4717) is "הקצבת אוצר המדינה לפי סעיף 32(ג1)" (the Treasury allocation), and the employee deduction is column D | asking "what rate does column E give for employee income above the bracket" must **REFUSE** (or be flagged); it must not silently use column D or column E figures |
| J2 | consolidated temporary Schedule J col D: "העולה על 60% מהשכר הממוצע" above, "שאינו עולה על מדרגת הגבייה המופחתת" below; on 2026 figures that leaves 7,703-8,261.40 in neither band | per `B2025` s 19(6) "בכל מקום", both bands meet at the bracket from 1 Jan 2026: wage 8,000 → 100.9012 (B5). Residual: `A252` s 7(a)(3)'s replacement sub-column headings literally still say "60% מהשכר הממוצע" and `B2025` s 20 did not change them |
| J3 | 348(d) "לחודש מלא" vs item 3 quarterly/annual only | H1: REFUSE for a monthly figure |
| J4 | items 2-4 have no monthly row, but 337(a)(1) and 342(f) work monthly | E8: REFUSE for a monthly max/min for items 2-4 |
| J5 | `A252`'s col C item 2 non-working "0.17" did not add up to its own total 6.92; `B2025` s 20 fixed it to 0.16 from 1 Jan 2026 | not used by s 342; noted only |

### K. Refusals (collected)

| id | question | why the source does not answer |
|---|---|---|
| K1 | monthly maximum or minimum for a self-employed person, item 3 or item 4 insured | Schedule K items 2-4 print only quarter and year (E8, J4) |
| K2 | deemed monthly income under 348(d) | J3 / H1 |
| K3 | no-deduction age for a woman under 342(c)(2) | Schedule A1 Part D is out of the sources (B13) |
| K4 | rate under "טור ה׳" per 342(e)(3) | J1 |
| K5 | a contribution period before 1 January 2026 | I1 |
| K6 | a "quarter" beginning on 1 February | Schedule K "”רבעון“ – תקופה של שלושה חודשים רצופים המתחילה ב־1 בינואר, ב־1 באפריל, ב־1 ביולי או ב־1 באוקטובר" |
| K7 | the minimum wage of a part-time, daily or hourly employee | Schedule K "”שכר מינימום“ – שכר מינימום, שכר מינימום חלקי, שכר מינימום יומי, או שכר מינימום לשעה … לפי הוראות חוק שכר מינימום": an input, or REFUSE, never a default |
| K8 | (a1) on a quarterly or annual income | G9 |
| K9 | the 2027 deduction | I3 |
| K10 | any figure when the basic amount, the average wage or the minimum wage is not supplied | the Law does not print them; no default |

---

## Revised after seeing the encoding (appended Tue Oct  6 21:58:26 UTC 2026; nothing above this line was changed after 21:49:13 UTC, sha256 of the file at that time `31be53f7…a9de`)

1. **Schedule J column D does not add up, and my B/C answers assumed its printed total.**
   Found at step 5 while turning column D into the per-branch inputs the encoding takes, not by reading the encoding's code.
   Column D "above" in the temporary table (`SRC` 4720-4729): maternity 0.87, accident 0.07, unemployment 0.21, disability 1.86, long-term care 0.14, senior citizens 1.52 = **4.67**, against the printed total **7.00** (`SRC` 4730); the permanent table (4738-4748) is the same.
   Column C employee "above" rows sum to 14.39 against the printed 14.50 (14.49 against 14.60 with the temporary 2.06).
   Column D "below" rows do sum to 1.04.
   BTL's salaried page prints the employee's share above the bracket as "7% (החל ב- 01.01.2006)", which agrees with the printed total.
   My B4-B9, B12, C1 and C2 were computed on 7.00 without checking the rows.
   I keep them as decided, because they agree with the printed total and with BTL, but the source itself supports 4.67 if read row by row. This is a source inconsistency.
2. **Monthly figures for items 2-4 (E8, H1/J3/K1/K2).** Item 2 builds its quarterly figure as "חמש פעמים הסכום הבסיסי, כפול 3", and items 3-4 as "5% / 15% מהשכר הממוצע … כפול 3", so a monthly amount can be read off the text.
   On reflection I find the encoder's reading (a third of the quarter, its fork F2) better than my refusal. I leave the assertions as decided, and they fail.
3. No other expectation is revised.
