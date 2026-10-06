# IL-03 decided answers (independent test author, fid-il-03)

Finished (UTC, from `date -u`): Tue Oct  6 14:02:44 UTC 2026

Written from the Hebrew source alone, before any file in the encoding directory other than `BRIEF.md` was opened.
Source: `registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` (sha256 `b87f2cf4…b81b6`), lines cited as `L<n>`.
I read: s 1 definitions (L106–L204), s 8(c) (L534–L537, only to know what s 121B(d) points at), s 120A (L4327–L4335), s 120B (L4337–L4345), s 121 (L4349–L4450, including the editorial tables, which I treat as aids, not law), s 121B (L4455–L4465).

Money is NIS, annual; tax amounts are unrounded (no rounding rule for the tax itself is in scope).
"Input I choose" marks a figure the source does not state; I say where it came from.
Confidence: **H** = the words leave no room; **M** = my best reading, a reasonable reader could differ; **L** = a guess I would not defend hard.

## 0. Readings that every scenario below depends on

R0.1 **Which tax years carry the s 121 figures.**
The s 121 body prints 301,200 / 560,280 and 84,120 / 120,720 / 228,000 / 301,200, with the editorial note `{{ח:הערה|(הסכומים מתואמים לשנים 2026–2027)}}` (L4350).
s 120B(e)(1) (L4344) freezes "הסכומים" for tax years 2025 to 2027: `ב־1 בינואר של שנות המס 2025 עד 2027 לא יתואמו הסכומים`.
s 121's amendment list ends `תשפ״ו־6` (L4349), a 5786 amendment that s 120B does not carry (its list ends `תשפ״ה־2`, L4337).
My reading: the body figures are the figures for tax years **2026 and 2027** (the amended text, held by the freeze through 2027).
For **2025 and earlier** the source does not show the text in force (the 228,000 and 301,200 limbs are 5786 text; the 2024–2025 editorial table is not law), so the answer is a refusal.
For **2028 and later** s 120B(e)(2) requires the 1 January 2024 amounts *before rounding* and the 2027 index, neither of which is in the source, and for the two limbs the 5786 amendment changed there is no "amount as it was on 1 January 2024" at all; so without supplied adjusted amounts, a refusal.
Confidence M (the year scope rests partly on an editorial note).

R0.2 **The s 121B threshold is never 640,000 in any year the source carries.**
s 120A defines "תקרות הכנסה" to include `הכנסה החייבת במס נוסף, כמשמעותה בסעיף 121ב` (L4335), so the 640,000 of s 121B(a) (L4456) is an income ceiling indexed every 1 January under s 120B(a).
The adjusted figure appears only in an editorial note (`בשנים 2024–2027, 721,560 ש״ח`), which is not law.
So the threshold for any tax year is an input (a published adjusted amount), and with no input the answer is a refusal.
Where I need a threshold below I choose **721,560** as an input; I took the number from the editorial note purely as a convenient value, not as law.
Confidence H that 640,000 must not be applied as-is to 2025–2027; M on the remainder.

R0.3 **Brackets are continuous.** `על כל שקל חדש מ־301,200 השקלים החדשים הראשונים` then `מ־301,201 שקלים חדשים עד 560,280` (L4351–L4352): I read the 301,201st shekel as the interval (301,200, 301,201], so a fractional amount above 301,200 is at 35%. Confidence M.

R0.4 **s 121(b)(1) replaces only (a)(1).** `על אף האמור בסעיף קטן (א)(1)` (L4354): the reduced table runs to 301,200 and (a)(2) and (a)(3) still apply above it. Confidence H.

R0.5 **Age 60.** `יחיד שמלאו לו 60 שנים` (L4354) does not say at what date in the tax year the age is tested.
Reached 60 on or before 1 January of the tax year: reduced rates (every reading agrees).
Not 60 by 31 December of the tax year: no reduced rates by the age limb.
Turns 60 on any day from 2 January to 31 December of the tax year: the source does not answer; refusal. Confidence M.

R0.6 **Mixed income under 60.** (b)(1) gives reduced rates `לגבי הכנסה חייבת בשנת המס מיגיעה אישית` but does not say which shekels of the (a) scale the personal-exertion income occupies when the individual also has other taxable income. Refusal. Confidence M.

R0.7 **Indexation arithmetic.** s 1 `”שיעור עליית המדד“, בתקופה פלונית – ההפרש בין המדד שפורסם לאחרונה לפני סוף התקופה לבין המדד שפורסם לאחרונה לפני תחילת התקופה, מחולק במדד שפורסם לאחרונה לפני תחילת התקופה` (L180): r = (I_end − I_start) / I_start, divisor the **start** index.
s 1 `”סכום מתואם“ – סכום כלשהו בתוספת אותו סכום כשהוא מוכפל בשיעור עליית המדד` (L142): adjusted = A + A × r.
s 120B(a) (L4338): on 1 January of year Y the amounts as on 1 January of Y−1 are adjusted by r over tax year Y−1.
Direction: the definition is a signed difference with no floor, so a fall in the index **reduces** the amount. Confidence M (the term says "rise"; no floor is written).
Rounding: s 120B(d) (L4341) empowers rules; the Order is out of scope, so a rounded amount is supplied or refused. Confidence H.

R0.8 **Restart in 2028.** s 120B(e)(2) (L4345): on 1 January 2028 the amounts `כפי שהיו ביום כ׳ בטבת התשפ״ד (1 בינואר 2024) טרם עיגולם` are adjusted, `ולעניין זה המדד בשנת המס הקודמת שיובא בחשבון לצורך תיאומם יהיה המדד של שנת המס 2027`.
My reading: 2028 amount (before rounding) = A(1 Jan 2024, unrounded) × (1 + r over tax year 2027) — **no catch-up** for 2024, 2025, 2026.
The rival reading (cumulative index rise from 2024 to end-2027) I reject because the clause names only "the index of tax year 2027" as the previous-year index. Confidence M.

R0.9 **s 121B(a1) tests capital income alone.** `יחיד אשר הכנסתו החייבת ממקורות הוניים בשנת המס עלתה על הסכום הקבוע באותו סעיף קטן ... על חלק הכנסתו החייבת ממקורות הוניים העולה על הסכום האמור, בשיעור של 2%` (L4457): the capital-source income, by itself, must exceed the (a) threshold; the 2% is on its own excess. Confidence M (a "capital income on top of the stack" reading is conceivable, but the words do not say it).

R0.10 **"עלתה על" / "עולה על" is strict.** Equal to the threshold is not above it. Confidence H.

## 1. s 121 — the individual's scale, tax years 2026 and 2027 (R0.1)

Each scenario holds for tax year 2026 **and** tax year 2027 with identical answers.
"Standard" = s 121(a) only; "Reduced" = s 121(b)(1) for the first 301,200 and s 121(a)(2)–(3) above it.

### 1A. Standard scale (s 121(a)(1)–(3), L4351–L4353: 31% / 35% / 47%)
Facts: individual under 60 all year, all taxable income NOT from personal exertion (e.g. taxable rent or interest on the s 121 scale).

| id | taxable income | tax | reason |
|---|---|---|---|
| A01 | 0 | 0 | |
| A02 | 1 | 0.31 | (a)(1) 31% |
| A03 | 100,000 | 31,000 | (a)(1) |
| A04 | 301,199 | 93,371.69 | (a)(1) |
| A05 | 301,200 | 93,372 | top of (a)(1) `301,200 השקלים החדשים הראשונים` |
| A06 | 301,201 | 93,372.35 | first shekel of (a)(2) `מ־301,201 ... – 35%` |
| A07 | 400,000 | 127,952 | 93,372 + 35% × 98,800 |
| A08 | 560,279 | 184,049.65 | |
| A09 | 560,280 | 184,050 | top of (a)(2) `עד 560,280` |
| A10 | 560,281 | 184,050.47 | (a)(3) `על כל שקל חדש נוסף – 47%` |
| A11 | 1,000,000 | 390,718.40 | 184,050 + 47% × 439,720 |
| A12 | 301,200.50 | 93,372.175 | R0.3, confidence M |

All H except A12.

### 1B. Reduced scale (s 121(b)(1)(a)–(d), L4355–L4358: 10% / 14% / 20% / 31%, then (a)(2)–(3))
Facts: individual under 60 all year, all taxable income from personal exertion (`הכנסה חייבת ... מיגיעה אישית`), books not required (so (b)(2) does not bite).

| id | taxable income | tax | reason |
|---|---|---|---|
| B01 | 0 | 0 | |
| B02 | 84,119 | 8,411.90 | (b)(1)(a) 10% |
| B03 | 84,120 | 8,412 | top of (a) `84,120 השקלים החדשים הראשונים` |
| B04 | 84,121 | 8,412.14 | (b)(1)(b) `מ־84,121 ... – 14%` |
| B05 | 100,000 | 10,635.20 | 8,412 + 14% × 15,880 |
| B06 | 120,719 | 13,535.86 | |
| B07 | 120,720 | 13,536 | top of (b) `עד 120,720` |
| B08 | 120,721 | 13,536.20 | (b)(1)(c) `מ־120,721 ... – 20%` |
| B09 | 227,999 | 34,991.80 | |
| B10 | 228,000 | 34,992 | top of (c) `עד 228,000` |
| B11 | 228,001 | 34,992.31 | (b)(1)(d) `מ־228,001 ... – 31%` |
| B12 | 301,199 | 57,683.69 | |
| B13 | 301,200 | 57,684 | top of (d) `עד 301,200` |
| B14 | 301,201 | 57,684.35 | (a)(2) 35% (R0.4) |
| B15 | 400,000 | 92,264 | 57,684 + 35% × 98,800 |
| B16 | 560,280 | 148,362 | 57,684 + 35% × 259,080 |
| B17 | 560,281 | 148,362.47 | (a)(3) 47% |
| B18 | 1,000,000 | 355,030.40 | 148,362 + 47% × 439,720 |

All H.

### 1C. Routes into and out of the reduced scale
Taxable income 100,000 throughout (standard 31,000; reduced 10,635.20).

| id | facts | tax | provision |
|---|---|---|---|
| C01 | under 60, personal exertion, books required, admissible books kept | 10,635.20 | (b)(1); (b)(2) does not bite because `נוהלו ... פנקסים קבילים` |
| C02 | under 60, personal exertion, books required, admissible books NOT kept | 31,000 | (b)(2) `השיעורים המופחתים ... לא יחולו על הכנסה שחייבים לגביה בניהול פנקסי חשבונות ולא נוהלו לגביה פנקסים קבילים` |
| C03 | under 60, NOT personal exertion | 31,000 | (a)(1) only |
| C04 | reached 60 before the tax year, NOT personal exertion, books not required | 10,635.20 | (b)(1) second limb `ולגבי הכנסה חייבת בשנת המס של יחיד שמלאו לו 60 שנים` |
| C05 | reached 60 before the tax year, business income, books required, admissible books NOT kept | 31,000 | (b)(2) bites on the age limb too: `השיעורים המופחתים הקבועים בפסקה (1)` |
| C06 | reached 60 before the tax year, personal exertion | 10,635.20 | either limb |

All H.

### 1D. The age-60 date edge (R0.5), tax year 2026, NOT personal exertion, 100,000

| id | date of birth | 60th birthday | tax | confidence |
|---|---|---|---|---|
| D01 | 1965-12-31 | 2025-12-31 | 10,635.20 | H |
| D02 | 1966-01-01 | 2026-01-01 (first day of the tax year) | 10,635.20 | M (age attained on the birthday) |
| D03 | 1966-01-02 | 2026-01-02 | REFUSE (date of the age test not stated) | M |
| D04 | 1966-06-15 | 2026-06-15 | REFUSE | M |
| D05 | 1966-12-31 | 2026-12-31 | REFUSE | M |
| D06 | 1967-01-01 | 2027-01-01 | 31,000 (not 60 at any point in 2026) | H |

### 1E. Years the source does not carry (R0.1)

| id | facts | answer | confidence |
|---|---|---|---|
| E01 | tax year 2025, standard, 100,000 | REFUSE | M |
| E02 | tax year 2025, reduced, 200,000 (the 20% limb the 5786 text widened) | REFUSE | M |
| E03 | tax year 2024, standard, 100,000 | REFUSE | M |
| E04 | tax year 2028, no adjusted amounts supplied | REFUSE | H |
| E05 | tax year 2023 | REFUSE | H |

### 1F. Other cases the source does not answer

| id | facts | answer | provision | confidence |
|---|---|---|---|---|
| F01 | tax year 2026, under 60, 60,000 personal-exertion income plus 60,000 non-exertion income | REFUSE | R0.6 | M |
| F02 | tax year 2026, under 60, personal exertion 60,000 of which a part requires books not kept, part salary | REFUSE (same allocation gap through (b)(2)) | R0.6 | M |
| F03 | taxable income −1,000 | REFUSE (s 121 prices only income) | L |

## 2. s 120B — indexation arithmetic (R0.7, R0.8)

All index readings and starting amounts are inputs I choose; none is a CBS figure.
Results are before rounding under s 120B(d).

| id | facts | answer | provision | confidence |
|---|---|---|---|---|
| I01 | A = 100,000 on 1 Jan Y−1; index published last before start of Y−1 = 100.0; last before end of Y−1 = 103.0; adjustment on 1 Jan Y for an ordinary year Y | 103,000 | s 1 L142, L180; s 120B(a) | H |
| I02 | A = 50,000; I_start 100; I_end 110 | 55,000 (divisor is the start index, not 54,545.45) | s 1 L180 `מחולק במדד שפורסם לאחרונה לפני תחילת התקופה` | H |
| I03 | A = 84,120; I_start 100; I_end 102.5 | 86,223 | | H |
| I04 | A = 75,960; I_start 100; I_end 99.4 (index fell) | 75,504.24 (amount falls) | R0.7 direction | M |
| I05 | A = 75,960; I_start = I_end = 100 | 75,960 | | H |
| I06 | rate of rise alone: I_start 104.0, I_end 106.08 | 0.02 | L180 | H |
| I07 | target year 2025; amount as at 1 Jan 2024 after rounding = 193,800 (input); any index readings, e.g. I_start 100, I_end 104 | 193,800 (no adjustment) | s 120B(e)(1) `לא יתואמו ... והסכומים באותן שנות מס יהיו כפי שהיו ביום ... (1 בינואר 2024) לאחר עיגולם` | H |
| I08 | target year 2026, same | 193,800 | (e)(1) | H |
| I09 | target year 2027, same | 193,800 | (e)(1) | H |
| I10 | target year 2028; amount as at 1 Jan 2024 BEFORE rounding = 84,000 (input); index last published before 1 Jan 2027 = 105.0, before end of 2027 = 107.1 | 85,680 | (e)(2), R0.8 | M |
| I11 | target year 2028; as I10 but the caller supplies only the ROUNDED 1 Jan 2024 amount | REFUSE (the base is `טרם עיגולם`) | (e)(2) | M |
| I12 | target year 2029; amount on 1 Jan 2028 = 85,680 (input); I_start 107.1, I_end 109.242 | 87,393.60 | (a), r = 0.02 | H |
| I13 | any year; a rounded adjusted amount asked for | REFUSE (rounding Order not encoded) | (d), brief | H |
| I14 | target year 2024 (adjustment on 1 Jan 2024 by 2023's rise) | REFUSE — the text in force on 1 Jan 2024 is not in the source | brief "what they do not show" | L |
| I15 | s 120B(b): pension-point amount P = 1,000 on 1 Jan of an ordinary year; COLA agreed for work from month M; index last before start of year 100, last before end of month M 101.5 | 1,015 in month M | (b) `לפי שיעור עליית המדד מתחילת שנת המס עד תום החודש האמור` | H |
| I16 | s 120B(b) COLA in tax year 2026 | no adjustment (P unchanged) | (e)(1) names (b) too | H |

## 3. s 121B — the additional tax (R0.2, R0.9, R0.10)

Threshold T is an input I choose: 721,560, tax year 2026 unless stated.
"Income" below is taxable income as defined for s 121B by s 121B(e) (L4462).
Answers are the additional tax only, split (a) / (a1).

| id | facts | (a) 3% | (a1) 2% | total | confidence |
|---|---|---|---|---|---|
| S01 | income 721,559, none capital | 0 | 0 | 0 | H |
| S02 | income 721,560, none capital | 0 | 0 | 0 | H (`עלתה על`) |
| S03 | income 721,561, none capital | 0.03 | 0 | 0.03 | H |
| S04 | income 1,000,000, all salary (s 2(2)) | 8,353.20 | 0 | 8,353.20 | H |
| S05 | salary 100,000 + capital 721,560 (= T) | 3,000 | 0 | 3,000 | H for (a); M for (a1) |
| S06 | capital 721,561, nothing else | 0.03 | 0.02 | 0.05 | M |
| S07 | capital 900,000, nothing else | 5,353.20 | 3,568.80 | 8,922 | M |
| S08 | income 1,000,000 of which capital 500,000 | 8,353.20 | 0 | 8,353.20 | M (R0.9) |
| S09 | pension (personal exertion, not s 2(1)/(2)) 900,000 | 5,353.20 | 0 (excluded by (e) "הכנסה חייבת ממקור הוני" (2)) | 5,353.20 | H |
| S10 | business income (s 2(1)) 900,000 | 5,353.20 | 0 (excluded by (e)(1)) | 5,353.20 | H |
| S11 | tax year 2026, income 1,000,000, no threshold supplied | REFUSE | | | H (R0.2) |
| S12 | tax year 2026, threshold taken as 640,000 by the encoding without input | an encoding that does this is wrong | | | H |
| S13 | tax year 2025, T = 721,560 (input), capital 900,000 | 5,353.20 | 3,568.80 | 8,922 | M ((a1) is 5785 text; 2025 is the first year I read it to apply) |
| S14 | tax year 2024 | REFUSE (text in force not shown; (a1) did not exist in the form shown) | | | M |

### 3A. The s 121B(e) definition of taxable income (tax year 2026, T = 721,560)

| id | facts | s 121B income | (a) 3% | confidence |
|---|---|---|---|---|
| S20 | s 1/s 89 taxable income 800,000 including a s 88 inflationary amount of 50,000 | 750,000 | 853.20 | H (`למעט סכום אינפלציוני כהגדרתו בסעיף 88`) |
| S21 | other income 600,000 + betterment (שבח) 200,000 on non-residential land | 800,000 | 2,353.20 | H (`ולרבות שבח`) |
| S22 | other 600,000 + betterment 200,000 on a residential apartment, sale value 5,385,285, not exempt | 600,000 | 0 | H (`רק אם שווי מכירתה עולה על 5,385,285`) |
| S23 | as S22 but sale value 5,385,286, not exempt | 800,000 | 2,353.20 | H |
| S24 | as S22 but sale value 6,000,000 and the sale exempt | 600,000 | 0 | H (`והמכירה אינה פטורה ממס לפי כל דין`) |
| S25 | as S23 but tax year 2025 | 800,000 | 2,353.20 (with T input) | M (note: `נקוב לשנת 2025`) |
| S26 | residential sale in tax year 2027 or later, sale value 5,385,286, no adjusted figure supplied | REFUSE (adjustment under Land Taxation Law s 9(c2), base index published 15 Jan 2027; outside the sources) | | M |
| S27 | betterment counts as capital-source income for (a1): capital other 600,000 + non-residential betterment 200,000 | 800,000 capital | (a) 2,353.20, (a1) 1,568.80 | M |

### 3B. Provisions with no number

| id | facts | answer | provision |
|---|---|---|---|
| S30 | is s 91(d) (advance payments) applied to income chargeable under (a) or (a1)? | no | (b) `לא יחולו הוראות סעיף 91(ד) לעניין מקדמות` |
| S31 | does another enactment displace s 121B? | no | (c) `יחולו על אף האמור בכל חיקוק` |
| S32 | s 8(c) spreading | applies in computing s 121B income; its result is an input | (d) |

## 4. Count

Scenarios decided: section 1: A 12 + B 18 + C 6 + D 6 + E 5 + F 3 = 50; section 2: 16; section 3: 14 + 8 + 3 = 25. **Total 91.**
Section 1 scenarios hold for both 2026 and 2027, so the boundary rows are asserted twice where the interface takes a year.

Stamp (`date -u` at close): Tue Oct  6 14:02:44 UTC 2026

---

## Revised after seeing the encoding

Appended after the encoding was opened and `tests-independent.l4` was run.
Lines 1-223 above are byte-identical to the file as stamped at 14:02:44 UTC (sha256 of those lines `ad2c0b050043787a6a4c769e3bbc11cd64935131cfe64b0d5340894d980ddc00`); no expected value above was changed.
The assertions in `tests-independent.l4` assert the values above, not the ones below.

- **F02, my error on reflection.** The stacking gap of R0.6 is real but immaterial here: wages of 30,000 and unbooked trade income of 30,000 put the eligible 30,000 inside the 10% band under every placement (bottom, top, pro rata), so the source does answer: 12,300. My REFUSE was over-broad.
- **F03, my error on reflection, of mechanism only.** I meant "does not price negative income"; the encoding declines with `LEFT an amount of income is negative`, a typed rejection of invalid input, which is that answer by another route.
- **S13 and S25 (tax year 2025 for s 121B), held, but weakly.** My answer rests on the note `(נקוב לשנת 2025)` at L4462 and on 2025 being the freeze's first year; neither is text that says from which tax year the 5785 amendment applies. The encoder's refusal is the reading the brief asks for ("what they do not show, you do not know"); I keep my expectation visible and classify it as a recorded ambiguity.
