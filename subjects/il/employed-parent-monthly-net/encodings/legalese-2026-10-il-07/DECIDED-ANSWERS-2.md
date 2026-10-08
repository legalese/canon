# Decided answers, second independent pass (IL-13), for the IL-07 capstone v0.2.2

Independent test author `fid-il-13`, one session, no sub-agents, working in a detached worktree of commons at `79f0a29`.
Every figure below was decided from the deposited law and from official pages I fetched myself, **before any `.l4` file was opened**.
I have not read any encoding's `NOTES.md`, `RECONCILE.md`, `GAPS.md`, `check.sh`, `vendor.sh`, `encoding.json` or `VENDORED.sha256`, any row directory, the earlier tester's `DECIDED-ANSWERS.md`, `INDEPENDENT-FINDINGS.md` or `tests-independent.l4`, or anything of the Axiom Foundation.

## What I read

- The capstone's `BRIEF.md` and `../../subject.json`.
- ITO Hebrew text `income-tax-ordinance-new-version.he.wiki.txt` (sha256 `b87f2cf4…94b81b6`, matches its meta file); line numbers below are that file's.
- NII Hebrew text `national-insurance-law-consolidated-version-5755-1995.he.wiki.txt` (sha256 `78bf47ee…65f552a97`, matches); "NII line" numbers are that file's.
- Amending Laws, each sha256 checked against `SOURCES.json` before reading (all four match): ITO `25_lsr_12235101.pdf` (Economic Efficiency Law 5786-2026, SH 3511); NII `25_lsr_5482787.pdf` (Amendment 252 and temporary provision, SH 3347), `25_lsr_6133485.pdf` (2025 Budget-year Law, SH 3384), `25_lsr_2572039.pdf` (Economic Efficiency Law 5783-2023, SH 3045).
  `pdftotext` drops the digits 0 and 2 in these PDFs, so every figure I took from them I read off a page rendered with `pdftoppm` (scratch `img/`).
- Official pages fetched by me (saved in my scratch dir `fetched/`, with the `.meta` files giving time and hash):

| page | retrieved (UTC) | sha256 | used for |
| --- | --- | --- | --- |
| BTL, rates for salaried employees (`btl.gov.il/Insurance/Rates/Pages/לעובדים שכירים.aspx`) | 2026-10-08T06:29:00Z | `74fc3652d8912f23004b6e2d1d3d7fc39e0fbe928c0b71948ff89e8b71827cf1` | reduced collection threshold 7,703 and maximum 51,910 from 1.1.2026; employee NI 1.04% / 7%; health 3.23% / 5.17%; controlling shareholder 1.02% / 6.79% (4.25−3.23, 11.96−5.17); ages 67-70 without old-age pension 0.70% / 4.86% (3.93−3.23, 10.03−5.17); over 70: no NI deduction |
| BTL, child allowance amounts (`btl.gov.il/benefits/children/Pages/שיעורי הקצבה.aspx`) | 2026-10-08T06:29:41Z | `1d9d28981e33740fefe1bb4d76be11ff87e9605fab1f4ff83939e643456e052e` | from 1.1.2026: first 173, second to fourth 219, fifth onward 173 |
| BTL, minimum wage (`btl.gov.il/Mediniyut/GeneralData/Pages/שכר מינימום.aspx`) | 2026-10-08T06:30:20Z | `cdf3944101c0cfc1fc01cfbc1074d32026e034a953b3f3e76379f59f3d28f611` | monthly minimum wage 6,247.67 from 1.4.2025 and 6,443.85 from 1.4.2026 |
| Tax Authority 2026 monthly-deductions booklet (the `SOURCES.json` pointer, Internet Archive capture) | 2026-10-08T06:30:42Z | `282bb886ccae1cc718840127af378fce88ca37ee3b2b9f00ed2cd44467e86285` (matches `SOURCES.json`) | p. 9: credit point 242 a month; s 47(a)(1)(1) ceiling 9,700 a month; s 45A(d) 189 a month; 16% of the average wage 26,436 a year |

## Rulings taken as given

1. **Schedule J, column D:** where a printed «סך הכל» differs from the sum of the printed items, the printed total governs; the sum of items is the named alternative.
   It matters only above the threshold: the upper column's items (Sch. J lines 4720-4729: 0.87, 0.07, 0.21, 1.86, 0.14, 1.52) sum to 4.67 against the printed 7.00 (line 4730); the lower column of the 2025-2026 temporary table sums exactly to its printed 1.04 (Amendment 252 s 7(a)(3)(b), SH 3347 p. 178: 0.10, 0.03, 0.02, 0.29, 0.03, 0.57).
2. **s 334(a), a fall of the index:** decline by default; "apply the fall" and "no update on a fall" are named alternatives.

## The figures for 2026, and where each comes from

| figure | value | provision and Hebrew |
| --- | --- | --- |
| credit point | 2,904 a year, 242 a month | ITO s 33A, line 1563, «”נקודת זיכוי“ – סכום של 504 שקלים חדשים (... בשנים 2024–2027, 2,904 ש״ח) לשנת מס»; s 120B(e)(1), line 4344, «ב־1 בינואר של שנות המס 2025 עד 2027 לא יתואמו הסכומים»; booklet p. 9 |
| brackets, personal exertion | 10% to 84,120; 14% to 120,720; 20% to 228,000; 31% to 301,200; 35% to 560,280; 47% above | ITO s 121(b)(1), lines 4354-4358, and s 121(a), lines 4350-4353; enacted from 1 Jan 2026 by the 5786-2026 Law ch C s 5 («במקום הסכום הנקוב בה יבוא "301,200"», «עד 228,000 שקלים חדשים», «מ־228,001 ... עד 301,200 ... 31%»), s 6 (commencement 1.1.2026), SH 3511 p. 416 |
| additional tax | 3% of annual taxable income above 721,560 | ITO s 121B(a), line 4456, «עלתה על 640,000 ... (בשנים 2024–2027, 721,560 ש״ח) ... בשיעור של 3%» |
| s 47 qualifying income ceiling | 116,400 a year | ITO s 47(a)(1)(1), line 1766 note «בשנים 2024–2027, 116,400 ש״ח»; booklet 9,700 a month |
| s 45A(d)(1) floor | 2,268 a year | line 1726 note «בשנים 2024–2027, 2,268 ש״ח» |
| beneficiary member | 16% of the average wage = 26,436 a year | ITO s 47(a)(7), line 1776 and note |
| reduced collection threshold | 7,703 a month | NII s 334(a), line 3605, «סכום של 7,522 שקלים חדשים (... בשנת 2026, 7,703 ש״ח), כשהוא מעודכן ב־1 בינואר של כל שנה ... (1) בשנים 2026 עד 2028 – לפי שיעור עליית המדד»; enacted by the 2025 Budget Law s 19(2), SH 3384 p. 396, in force 1.1.2026 (s 21); BTL page |
| employee deduction rates | 1.04% up to the threshold, 7.00% above | Sch. J column D (heading «הניכוי משכר העובד לענין סעיף 342(ג) באחוזים», line 4717): upper total 7.00 (line 4730; the temporary table replaces only the lower sub-column, Amendment 252 s 7(a)(3)(b)); lower 1.04 for 2025-2026 (Amendment 252 s 7(a), «בתקופה שמיום התחילה עד יום כ״א בטבת התשפ״ז (31 בדצמבר 2026)»); «60% מהשכר הממוצע» replaced throughout Sch. J by «מדרגת הגבייה המופחתת כהגדרתה בסעיף 334(א)» (2025 Budget Law s 19(6)); the Wikisource temporary table still prints «העולה על 60% מהשכר הממוצע» over the upper sub-column (line 4718), which I treat as a consolidation lag, not law |
| maximum income | 51,910 a month | NII s 348(a), line 3763; Sch. K item 1, line 4758, «לחודש – הסכום הבסיסי, כפול 5», and line 4773 (para (3) of the basic amount); s 1 para (3), line 191, «בשנת 2026, 10,382 ש״ח»; BTL page |
| minimum income (employee) | the minimum wage of the first month of the quarter | NII s 348(b), line 3765, «ישתלמו בעדו דמי הביטוח כאילו הכנסתו היתה הסכום המזערי»; Sch. K item 1, line 4758; «שכר מינימום» includes «שכר מינימום חלקי ... לגבי עובד פלוני», line 4772; BTL minimum-wage page |
| child allowance | 173 for the first and the fifth onward, 219 for the second to fourth | NII s 68(a), line 821; s 1 «הסכום הבסיסי» para (2)(a)-(b), lines 187-188, «בשנת 2026, 173 ש״ח», «בשנת 2026, 219 ש״ח»; BTL page |
| health insurance | an input | the National Health Insurance Law is not in the bundle (BRIEF line 37, «the health insurance contribution (an input)»); I supply it at BTL's 3.23% up to 7,703 and 5.17% above, to 51,910, and expect it passed through unchanged |

## Readings I decided before opening the encoding

- **D1, annual tax and a month.** The Ordinance taxes a tax year (s 121(a), line 4350, «המס על הכנסתו החייבת של יחיד בשנת המס»; credits «לשנת מס», line 1563); the BRIEF asks for "the income tax for tax year 2026 and one twelfth of it". Monthly tax = annual tax ÷ 12, the same in every month of 2026, with every credit point for the tax year counted (so a child born in November 2026 counts for January's twelfth).
- **D2, a married earner whose spouse has no income** requests a separate calculation under s 66(c)(1א) (line 2462), which is never worse for the household, and so receives the child points of s 66(c)(4) (a woman, line 2466) or s 66(c)(5) (a man, lines 2474-2476). Where the household says no separate calculation was requested, the joint computation of s 65 (line 2448) applies and there are no child points, because the Ordinance gives them only in s 66(c) (and s 40(b) for single parents); s 40(a) (line 1632) gives «נקודות קיצבה» paid by the NII, not tax credits.
- **D3, ages for credit points** run by tax year: a child "turns n" in 2026 if born in 2026 − n («שנת לידה» and «שנת בגרות», s 40(b)(3), lines 1644-1645).
- **D4, credits** are set against the s 121 tax and cannot make it negative («המקוזז כנגד המס», line 1563); the s 121B additional tax is added after them.
- **D5, Schedule J for a subset of branches.** s 342(c)(1) (line 3661) deducts for the branches in s 335(a), (d), (e), (g), (h), (i) that are paid for the employee. Where all are paid, ruling 1 gives 1.04 and 7.00. Where only some are paid, no total is printed; I take **the printed total less the printed items of the branches not paid** as the default, because it is the only extension of ruling 1 that uses the printed total, and the sum of the applicable items as the named alternative. BTL's published rates follow the default for the controlling shareholder (1.02 / 6.79) and for ages 67-70 (0.70 / 4.86). For a non-resident (maternity alone) the default gives 0.10 / 3.20 and the alternative 0.10 / 0.87; I flag that as a **genuine ambiguity** above the threshold, since the items printed in the deposited text cannot all be right (they sum to 4.67, not 7.00).
- **D6, s 342(c)(2):** no deduction for the time after a man reaches 70, or a woman the age in Sch. A1 Part D (70 for anyone born from May 1950, line 4453), or while an old-age pension is paid. I test months strictly after the birthday; the month of the 70th birthday itself is not decided by the text and I do not test it.
- **D7, ages 67-70:** unemployment (s 158(1), line 1444), accidents (s 150, line 1405) and disability (s 195, line 1929) insure only to retirement age (67 for a man, s 1 «גיל הפרישה», line 130), so those branches are not paid.
- **D8, the allowance:** a child is counted from the first of the month of birth if born on or before the 15th, otherwise from the first of the next month (s 72(a), line 854); entitlement ends on the 18th birthday (s 65(a), line 807, «ולא מלאו לו 18 שנים»), but payment runs to the end of that month (s 72(a)), whether the birthday falls on the 1st or later. The s 66 exclusion tests «הורה מבוטח», the parent in whose count the child is, which for a child of two parents living with both is the father (s 67(b), line 818). (A common-law reading under which a person attains an age on the day before the anniversary would move a 1st-of-month birthday into the previous month; I do not adopt it, and the Israeli texts in the bundle do not say so.)
- **D9, which tax year's additional tax** excludes a parent from the allowance in a month of 2026: tax year 2026's (s 66 speaks in the present, «שיש לו הכנסה החייבת במס נוסף»; the household's salary is the same all year, so 2026 taxable income is twelve months' salary).
- **D10, non-residents:** no s 34 or s 36 points (both «תושב ישראל»); a woman keeps s 36A (no residence condition, line 1597); s 121(b) rates apply to personal-exertion income regardless of residence; NII as D5; no allowance (not «מבוטח» under s 65(a), child not «נמצא בישראל»); health input 0.
- **D11, the 5786-2026 temporary Aliyah Law** (ch D of the deposited 5786-2026 Law, s 9 enacting the Encouragement of Aliyah and Return (Temporary Provision) Law, SH 3511 pp. 416-418): an immigrant first resident from 5 November 2025 to the end of 2026 is exempt on personal-exertion income in 2026 up to 600,000, pro rata to residence in 2026 (its s 2(a)(1), (d)). It is in the bundle, so a capstone that ignores it is wrong for such a household unless it declines by name.
- **D12, net** = salary − monthly tax − NI deduction − health deduction + allowance, as the question is put; pension contributions and premiums move the tax only.
- **D13, s 45A and s 47 for an employee all of whose salary is insured** (employer pays to a pension fund, s 47(a)(4), line 1771): credit 35% of the employee's own pension contributions (and 25% of life-insurance premiums), up to the higher of 2,268 and the lower of the sums paid and 7% of qualifying income (salary up to 116,400); no s 47 deduction (nothing is «שאינה הכנסה מבוטחת», and «הכנסה לעמית עצמאי» and «הכנסה נוספת» are nil). I chose households whose beneficiary-member status does not change the answer, and avoided any case where the cap would have to be split between the 25% and 35% items.
- **D14, out of period:** a month outside 2026 is refused in every component (BRIEF "refuses every other by name"; Amendment 252's 1.04 lower rate ends 31 December 2026).
- **D15, credits no row encodes** (s 40C, s 39B and the like): the tax and the net decline; the NI deduction, health and allowance are still answered (BRIEF line 35).
- **D16, representation.** Values are exact (Fraction arithmetic in my scratch `calc.py`); NI and health carry up to four decimals because 1.04% × 7,703 = 80.1112. Every monthly tax figure here terminates. I give the exact value and the value to the agora; which one I assert depends only on whether the capstone rounds, which I will learn from its exported types, not from its answers.

## Function-level cases (s 334(a), the threshold update)

Asserted only if the capstone exports the update; decided from line 3605 and ruling 2.

| case | 2025 base | index ratio (new / old) | expected 2026 threshold |
| --- | --- | --- | --- |
| U1 rise | 7,522 | 1.024 | 7,522 × 1.024 = 7,702.528 (7,703 if rounded to the shekel, as published) |
| U2 no change | 7,522 | 1 | 7,522 (a rise of 0%) |
| U3 fall | 7,522 | 0.99 | **REFUSE** (ruling 2 default); alternatives: apply the fall 7,446.78, or no update 7,522 |

## Summary of expected values

All households are resident (except H39, H40), employed by one employer at the same monthly salary all year, with no other income, receiving no Income Support or maintenance; children are unmarried and in Israel; a spouse has no income; separate calculation requested unless stated; health is the input shown.

| id | household | tax | NI | health (input) | allowance | net |
| --- | --- | --- | --- | --- | --- | --- |
| H01 | married man, 1 child, below the NI threshold | 0 | 62.4 | 193.8 | 173 | 5916.8 |
| H02 | married man, 2 children, salary exactly at the NI threshold | 0 | 80.1112 | 248.8069 | 392 | 7766.0819 |
| H03 | married man, 2 children, one shekel above the NI threshold | 0 | 80.1812 | 248.8586 | 392 | 7766.9602 |
| H04 | married man, 3 children | 840.5 | 800.9012 | 781.1618 | 611 | 16188.437 |
| H05 | married man, 4 children | 866.5 | 940.9012 | 884.5618 | 830 | 18138.037 |
| H06 | married man, 5 children, salary exactly at the NI maximum | 11852.4 | 3174.6012 | 2534.3088 | 1003 | 35351.69 |
| H07 | married man, 5 children, one shekel above the NI maximum | 11852.87 | 3174.6012 | 2534.3088 | 1003 | 35352.22 |
| H08 | married man, 2 children, annual salary exactly at the s 121B threshold | 17651.8 | 3174.6012 | 2534.3088 | 392 | 37161.29 |
| H09 | married man, 2 children, one shekel a month above the s 121B threshold (allowance excluded) | 17652.3 | 3174.6012 | 2534.3088 | 0 | 36769.79 |
| H10 | married man, part-time, low salary | 0 | 31.2 | 96.9 | 173 | 3044.9 |
| H11 | married woman, husband without income, 2 children | 561.5 | 660.9012 | 677.7618 | 392 | 14491.837 |
| H12 | married woman, 3 children, eldest turns 18 on 15 September 2026 | 1486.5 | 1080.9012 | 987.9618 | 611 | 19055.637 |
| H13 | married woman liable to additional tax, husband without income | 21981.8 | 3174.6012 | 2534.3088 | 392 | 42701.29 |
| H14 | married woman, no separate calculation (joint, ss 64B, 65) | 314.1 | 170.9012 | 315.8618 | 392 | 8591.137 |
| H15 | divorced single mother, 2 children | 319.5 | 660.9012 | 677.7618 | 392 | 14733.837 |
| H16 | divorced single father, child living with him | 645.5 | 520.9012 | 574.3618 | 173 | 12432.237 |
| H17 | widowed mother, 2 children (s 40(b)(1ב)) | 518.5 | 1080.9012 | 987.9618 | 392 | 19804.637 |
| H18 | single mother, newborn born 10 March 2026, month of birth | 0 | 72.8 | 226.1 | 392 | 7093.1 |
| H19 | single mother, newborn born 20 March 2026, month of birth | 0 | 72.8 | 226.1 | 173 | 6874.1 |
| H20 | as H19, the month after birth | 0 | 72.8 | 226.1 | 392 | 7093.1 |
| H21 | married man, newborn born 15 May 2026, month of birth | 724.5 | 590.9012 | 626.0618 | 392 | 13450.537 |
| H22 | married man, newborn born 16 May 2026, month of birth | 724.5 | 590.9012 | 626.0618 | 173 | 13231.537 |
| H23 | as H22, the month after birth | 724.5 | 590.9012 | 626.0618 | 392 | 13450.537 |
| H24 | married man, child turns 18 on 1 June 2026, June | 333.1 | 240.9012 | 367.5618 | 392 | 9450.437 |
| H25 | as H24, July | 333.1 | 240.9012 | 367.5618 | 173 | 9231.437 |
| H26 | married man, child turns 18 on 20 June 2026, June | 333.1 | 240.9012 | 367.5618 | 392 | 9450.437 |
| H27 | as H24, May | 333.1 | 240.9012 | 367.5618 | 392 | 9450.437 |
| H28 | married man, blind wife (s 37), separate calculation | 808.5 | 450.9012 | 522.6618 | 173 | 11390.937 |
| H29 | married man, blind wife (s 37), joint computation | 929.5 | 450.9012 | 522.6618 | 173 | 11269.937 |
| H30 | married man, joint computation, 2 children | 1171.5 | 450.9012 | 522.6618 | 392 | 11246.937 |
| H31 | immigrant (arrived 1 July 2024), s 35 | 403.5 | 520.9012 | 574.3618 | 173 | 12674.237 |
| H32 | immigrant (arrived 1 January 2023), s 35 tapering bands | 766.5 | 520.9012 | 574.3618 | 173 | 12311.237 |
| H33 | immigrant arrived 1 December 2025: 5786-2026 temporary exemption | 0 | 940.9012 | 884.5618 | 173 | 18347.537 |
| H34 | married man, pension contributions, not a beneficiary member (s 45A(d)) | 0 | 62.4 | 193.8 | 173 | 5916.8 |
| H35 | married man, pension contributions, beneficiary member, cap binds (s 45A(e)) | 1959.85 | 940.9012 | 884.5618 | 392 | 16606.687 |
| H36 | married man, pension and life insurance (s 45A(a),(b)) | 10.6 | 170.9012 | 315.8618 | 173 | 8675.637 |
| H37 | controlling shareholder below the NI threshold (NII s 335) | 0 | 71.4 | 226.1 | 173 | 6875.5 |
| H38 | controlling shareholder above the NI threshold | 5735.5 | 1592.5369 | 1401.5618 | 173 | 21443.4013 |
| H39 | non-resident man | 1119.6 | 81.207 | 0 | 0 | 8799.193 |
| H40 | non-resident woman, below the NI threshold | 479 | 6 | 0 | 0 | 5515 |
| H41 | married man aged 71 (s 342(c)(2)) | 608.5 | 0 | 470.9618 | 173 | 11093.5382 |
| H42 | married man aged 68, no old-age pension | 608.5 | 262.7552 | 470.9618 | 173 | 10830.783 |
| H43 | married man who turned 70 on 20 May 2026, month of June | 608.5 | 0 | 470.9618 | 173 | 11093.5382 |
| H44 | full-time employee below minimum wage, first quarter (s 348(b)) | 0 | 8121971/125000 (= 64.975768) | 161.5 | 173 | 618315529/125000 (= 4946.524232) |
| H45 | as H44, second quarter | 0 | 1675401/25000 (= 67.016040) | 161.5 | 173 | 123612099/25000 (= 4944.483960) |
| H46 | half-time employee above the partial minimum wage | 0 | 36.4 | 113.05 | 173 | 3523.55 |
| H47 | December 2025 (outside the period) | REFUSE | REFUSE | REFUSE | REFUSE | REFUSE |
| H48 | January 2027 (outside the period) | REFUSE | REFUSE | REFUSE | REFUSE | REFUSE |
| H49 | s 40C academic-degree credit (not encoded) | REFUSE | 240.9012 | 367.5618 | 173 | REFUSE |
| H50 | s 39B reservist credit (not encoded) | REFUSE | 240.9012 | 367.5618 | 173 | REFUSE |
| H52 | top of the 10% bracket (84,120 a year) | 0 | 72.904 | 226.423 | 173 | 6883.673 |
| H53 | top of the 14% bracket (120,720) | 341.5 | 245.1012 | 370.6638 | 173 | 9275.735 |
| H54 | top of the 20% bracket (228,000) | 2129.5 | 870.9012 | 832.8618 | 173 | 15339.737 |
| H55 | top of the 31% bracket (301,200) | 4020.5 | 1297.9012 | 1148.2318 | 173 | 18806.367 |
| H56 | top of the 35% bracket (560,280) | 11577 | 2809.2012 | 2264.4348 | 173 | 30212.364 |
| H57 | one shekel a month into the 47% bracket | 11577.47 | 2809.2712 | 2264.4865 | 173 | 30212.7723 |
| H58 | married woman, 6 children, newborn on 1 November 2026 | 0 | 660.9012 | 677.7618 | 1176 | 15837.337 |
| H59 | divorced single father, eldest turns 18 on 31 December 2026, December | 840.5 | 800.9012 | 781.1618 | 611 | 16188.437 |
| H60 | one shekel a month into the 14% bracket | 0 | 72.9144 | 226.4553 | 173 | 6884.6303 |
| H61 | one shekel a month into the 20% bracket | 341.7 | 245.1712 | 370.7155 | 173 | 9276.4133 |
| H62 | one shekel a month into the 31% bracket | 2129.81 | 870.9712 | 832.9135 | 173 | 15340.3053 |
| H63 | one shekel a month into the 35% bracket | 4020.85 | 1297.9712 | 1148.2835 | 173 | 18806.8953 |

## Households, with citations and arithmetic

Each block gives the facts, the credit points with their provisions, the tax arithmetic, the NI deduction, the health input, the allowance, and the net.
"Exact" values are the law's arithmetic; "to the agora" rounds half up.

### H01: married man, 1 child, below the NI threshold

Facts: month 2026-02; salary 6,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 72,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 72,000 = 7,200
- gross 7,200; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 6,000 = 62.4; total **62.4**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 6,000 = **193.8**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 6,000 − 0 − 62.4 − 193.8 + 173 = **5,916.8**.

**Expected:** tax 0 | NI 62.4 | health 193.8 (input) | allowance 173 | net 5916.8.
To the agora: tax 0.00 | NI 62.40 | health 193.80 | allowance 173.00 | net 5916.80.

### H02: married man, 2 children, salary exactly at the NI threshold

Facts: month 2026-03; salary 7,703 a month (the same in every month of 2026); earner man; status married; children born 2016-03-01, 2020-07-07.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2016-03-01: turns 10 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2020-07-07: turns 6 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 4.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 12,342
Tax on annual taxable income 92,436 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 8,316 = 1,164.24
- gross 9,576.24; less credits 12,342; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; total **80.1112**.
Alternative reading `full_R1`: 80.1112.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 = **248.8069**; expected = the input.

Child allowance for 2026-03: 2016-03-01: counted; 2020-07-07: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 7,703 − 0 − 80.1112 − 248.8069 + 392 = **7,766.0819**.

**Expected:** tax 0 | NI 80.1112 | health 248.8069 (input) | allowance 392 | net 7766.0819.
To the agora: tax 0.00 | NI 80.11 | health 248.81 | allowance 392.00 | net 7766.08.

### H03: married man, 2 children, one shekel above the NI threshold

Facts: month 2026-03; salary 7,704 a month (the same in every month of 2026); earner man; status married; children born 2016-03-01, 2020-07-07.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2016-03-01: turns 10 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2020-07-07: turns 6 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 4.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 12,342
Tax on annual taxable income 92,448 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 8,328 = 1,165.92
- gross 9,577.92; less credits 12,342; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 1 = 0.07; total **80.1812**.
Alternative reading `full_R1`: 80.1579.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 1 = **248.8586**; expected = the input.

Child allowance for 2026-03: 2016-03-01: counted; 2020-07-07: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 7,704 − 0 − 80.1812 − 248.8586 + 392 = **7,766.9602**.

**Expected:** tax 0 | NI 80.1812 | health 248.8586 (input) | allowance 392 | net 7766.9602.
To the agora: tax 0.00 | NI 80.18 | health 248.86 | allowance 392.00 | net 7766.96.

### H04: married man, 3 children

Facts: month 2026-05; salary 18,000 a month (the same in every month of 2026); earner man; status married; children born 2012-01-20, 2015-09-09, 2023-04-04.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2012-01-20: turns 14 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2015-09-09: turns 11 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2023-04-04: turns 3 («בשנת המס שבה מלאו לו שלוש שנים» 3½) -> 3.5 [ITO s 66(c)(5)(ב) (lines 2474-2476)]
- total 7.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 22,506
Tax on annual taxable income 216,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 95,280 = 19,056
- gross 32,592; less credits 22,506; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 10,086
- annual tax 10,086; monthly = annual ÷ 12 = **840.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 10,297 = 720.79; total **800.9012**.
Alternative reading `full_R1`: 560.9811.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 10,297 = **781.1618**; expected = the input.

Child allowance for 2026-05: 2012-01-20: counted; 2015-09-09: counted; 2023-04-04: counted. 3 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 + 219 = **611**.

Net = 18,000 − 840.5 − 800.9012 − 781.1618 + 611 = **16,188.437**.

**Expected:** tax 840.5 | NI 800.9012 | health 781.1618 (input) | allowance 611 | net 16188.437.
To the agora: tax 840.50 | NI 800.90 | health 781.16 | allowance 611.00 | net 16188.44.

### H05: married man, 4 children

Facts: month 2026-06; salary 20,000 a month (the same in every month of 2026); earner man; status married; children born 2010-02-02, 2013-06-06, 2019-10-10, 2024-12-12.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2010-02-02: turns 16 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2013-06-06: turns 13 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2019-10-10: turns 7 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2024-12-12: turns 2 (same band, 4½) -> 4.5 [ITO s 66(c)(5)(ב) (lines 2474-2476)]
- total 9.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 28,314
Tax on annual taxable income 240,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 12,000 = 3,720
- gross 38,712; less credits 28,314; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 10,398
- annual tax 10,398; monthly = annual ÷ 12 = **866.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 12,297 = 860.79; total **940.9012**.
Alternative reading `full_R1`: 654.3811.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 12,297 = **884.5618**; expected = the input.

Child allowance for 2026-06: 2010-02-02: counted; 2013-06-06: counted; 2019-10-10: counted; 2024-12-12: counted. 4 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 + 219 + 219 = **830**.

Net = 20,000 − 866.5 − 940.9012 − 884.5618 + 830 = **18,138.037**.

**Expected:** tax 866.5 | NI 940.9012 | health 884.5618 (input) | allowance 830 | net 18138.037.
To the agora: tax 866.50 | NI 940.90 | health 884.56 | allowance 830.00 | net 18138.04.

### H06: married man, 5 children, salary exactly at the NI maximum

Facts: month 2026-07; salary 51,910 a month (the same in every month of 2026); earner man; status married; children born 2009-08-01, 2011-01-01, 2014-03-03, 2021-05-05, 2025-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2009-08-01: turns 17 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2011-01-01: turns 15 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2014-03-03: turns 12 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2021-05-05: turns 5 (same band, 2½) -> 2.5 [ITO s 66(c)(5)(ב) (lines 2474-2476)]
- child born 2025-02-02: turns 1 («החל בשנת המס שלאחר לידתו ועד לשנת המס שבה מלאו לו שנתיים» 4½) -> 4.5 [ITO s 66(c)(5)(ב) (lines 2474-2476)]
- total 12.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 35,574
Tax on annual taxable income 622,920 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 73,200 = 22,692
- 35% (s 121(a)(2), line 4352) × 259,080 = 90,678
- 47% (s 121(a)(3), line 4353) × 62,640 = 29,440.8
- gross 177,802.8; less credits 35,574; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 142,228.8
- annual tax 142,228.8; monthly = annual ÷ 12 = **11,852.4**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 44,207 = 3,094.49; total **3,174.6012**.
Alternative reading `full_R1`: 2,144.5781.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 44,207 = **2,534.3088**; expected = the input.

Child allowance for 2026-07: 2009-08-01: counted; 2011-01-01: counted; 2014-03-03: counted; 2021-05-05: counted; 2025-02-02: counted. 5 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 + 219 + 219 + 173 = **1,003**.

Net = 51,910 − 11,852.4 − 3,174.6012 − 2,534.3088 + 1,003 = **35,351.69**.

**Expected:** tax 11852.4 | NI 3174.6012 | health 2534.3088 (input) | allowance 1003 | net 35351.69.
To the agora: tax 11852.40 | NI 3174.60 | health 2534.31 | allowance 1003.00 | net 35351.69.

### H07: married man, 5 children, one shekel above the NI maximum

Facts: month 2026-07; salary 51,911 a month (the same in every month of 2026); earner man; status married; children born 2009-08-01, 2011-01-01, 2014-03-03, 2021-05-05, 2025-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2009-08-01: turns 17 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2011-01-01: turns 15 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2014-03-03: turns 12 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2021-05-05: turns 5 (same band, 2½) -> 2.5 [ITO s 66(c)(5)(ב) (lines 2474-2476)]
- child born 2025-02-02: turns 1 («החל בשנת המס שלאחר לידתו ועד לשנת המס שבה מלאו לו שנתיים» 4½) -> 4.5 [ITO s 66(c)(5)(ב) (lines 2474-2476)]
- total 12.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 35,574
Tax on annual taxable income 622,932 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 73,200 = 22,692
- 35% (s 121(a)(2), line 4352) × 259,080 = 90,678
- 47% (s 121(a)(3), line 4353) × 62,652 = 29,446.44
- gross 177,808.44; less credits 35,574; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 142,234.44
- annual tax 142,234.44; monthly = annual ÷ 12 = **11,852.87**

NI deduction: maximum (s 348(a), line 3763; Sch. K item 1, line 4758, «הסכום הבסיסי, כפול 5»; basic amount s 1 para (3), line 191, 2026: 10,382): base capped at 51,910; all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 44,207 = 3,094.49; total **3,174.6012**.
Alternative reading `full_R1`: 2,144.5781.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 44,207 = **2,534.3088**; expected = the input.

Child allowance for 2026-07: 2009-08-01: counted; 2011-01-01: counted; 2014-03-03: counted; 2021-05-05: counted; 2025-02-02: counted. 5 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 + 219 + 219 + 173 = **1,003**.

Net = 51,911 − 11,852.87 − 3,174.6012 − 2,534.3088 + 1,003 = **35,352.22**.

**Expected:** tax 11852.87 | NI 3174.6012 | health 2534.3088 (input) | allowance 1003 | net 35352.22.
To the agora: tax 11852.87 | NI 3174.60 | health 2534.31 | allowance 1003.00 | net 35352.22.

### H08: married man, 2 children, annual salary exactly at the s 121B threshold

Facts: month 2026-08; salary 60,130 a month (the same in every month of 2026); earner man; status married; children born 2016-03-01, 2020-07-07.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2016-03-01: turns 10 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2020-07-07: turns 6 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 4.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 12,342
Tax on annual taxable income 721,560 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 73,200 = 22,692
- 35% (s 121(a)(2), line 4352) × 259,080 = 90,678
- 47% (s 121(a)(3), line 4353) × 161,280 = 75,801.6
- gross 224,163.6; less credits 12,342; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 211,821.6
- annual tax 211,821.6; monthly = annual ÷ 12 = **17,651.8**

NI deduction: maximum (s 348(a), line 3763; Sch. K item 1, line 4758, «הסכום הבסיסי, כפול 5»; basic amount s 1 para (3), line 191, 2026: 10,382): base capped at 51,910; all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 44,207 = 3,094.49; total **3,174.6012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 44,207 = **2,534.3088**; expected = the input.

Child allowance for 2026-08: 2016-03-01: counted; 2020-07-07: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 60,130 − 17,651.8 − 3,174.6012 − 2,534.3088 + 392 = **37,161.29**.

**Expected:** tax 17651.8 | NI 3174.6012 | health 2534.3088 (input) | allowance 392 | net 37161.29.
To the agora: tax 17651.80 | NI 3174.60 | health 2534.31 | allowance 392.00 | net 37161.29.

### H09: married man, 2 children, one shekel a month above the s 121B threshold (allowance excluded)

Facts: month 2026-08; salary 60,131 a month (the same in every month of 2026); earner man; status married; children born 2016-03-01, 2020-07-07.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2016-03-01: turns 10 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2020-07-07: turns 6 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 4.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 12,342
Tax on annual taxable income 721,572 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 73,200 = 22,692
- 35% (s 121(a)(2), line 4352) × 259,080 = 90,678
- 47% (s 121(a)(3), line 4353) × 161,292 = 75,807.24
- gross 224,169.24; less credits 12,342; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 211,827.24
- s 121B(a) (line 4456, «הכנסתו החייבת בשנת המס עלתה על ... 721,560 ... בשיעור של 3%»): 3% × (721,572 − 721,560) = 0.36
- annual tax 211,827.6; monthly = annual ÷ 12 = **17,652.3**

NI deduction: maximum (s 348(a), line 3763; Sch. K item 1, line 4758, «הסכום הבסיסי, כפול 5»; basic amount s 1 para (3), line 191, 2026: 10,382): base capped at 51,910; all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 44,207 = 3,094.49; total **3,174.6012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 44,207 = **2,534.3088**; expected = the input.

Child allowance: **0**: NII s 66 (line 814, «למעט הורה מבוטח שיש לו הכנסה החייבת במס נוסף כמשמעותה בסעיף 121ב») excludes the father, in whose count the children are (s 67(b), line 818), because his 2026 taxable income 721,572 exceeds 721,560 (reading D9).

Net = 60,131 − 17,652.3 − 3,174.6012 − 2,534.3088 + 0 = **36,769.79**.

**Expected:** tax 17652.3 | NI 3174.6012 | health 2534.3088 (input) | allowance 0 | net 36769.79.
To the agora: tax 17652.30 | NI 3174.60 | health 2534.31 | allowance 0.00 | net 36769.79.

### H10: married man, part-time, low salary

Facts: month 2026-01; salary 3,000 a month (the same in every month of 2026); earner man; status married; children born 2017-01-01; minwage_applies=True; job_fraction=0.4; note=40% part-time employee.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2017-01-01: turns 9 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 36,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 36,000 = 3,600
- gross 3,600; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: minimum income (s 348(b), line 3765; Sch. K item 1, line 4758, «סכום השווה לשכר מינימום של החודש הראשון ברבעון», where «שכר מינימום» includes «שכר מינימום חלקי ... לגבי עובד פלוני», line 4772): first month of the quarter January (6,247.67 from 1.4.2025) × job fraction 0.4 = 2,499.068; salary 3,000 is not below it, so the actual salary is the base; all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 3,000 = 31.2; total **31.2**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 3,000 = **96.9**; expected = the input.

Child allowance for 2026-01: 2017-01-01: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 3,000 − 0 − 31.2 − 96.9 + 173 = **3,044.9**.

**Expected:** tax 0 | NI 31.2 | health 96.9 (input) | allowance 173 | net 3044.9.
To the agora: tax 0.00 | NI 31.20 | health 96.90 | allowance 173.00 | net 3044.90.

### H11: married woman, husband without income, 2 children

Facts: month 2026-04; salary 16,000 a month (the same in every month of 2026); earner woman; status married; children born 2018-05-10, 2022-11-11.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 2) -> 2 [ITO s 66(c)(4)(a) (line 2466)]
- child born 2022-11-11: turns 4 («ארבע שנים וחמש שנים» 2½) -> 2.5 [ITO s 66(c)(4)(a) (line 2466)]
- total 7.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 21,054
Tax on annual taxable income 192,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 71,280 = 14,256
- gross 27,792; less credits 21,054; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 6,738
- annual tax 6,738; monthly = annual ÷ 12 = **561.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 8,297 = 580.79; total **660.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 8,297 = **677.7618**; expected = the input.

Child allowance for 2026-04: 2018-05-10: counted; 2022-11-11: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 16,000 − 561.5 − 660.9012 − 677.7618 + 392 = **14,491.837**.

**Expected:** tax 561.5 | NI 660.9012 | health 677.7618 (input) | allowance 392 | net 14491.837.
To the agora: tax 561.50 | NI 660.90 | health 677.76 | allowance 392.00 | net 14491.84.

### H12: married woman, 3 children, eldest turns 18 on 15 September 2026

Facts: month 2026-09; salary 22,000 a month (the same in every month of 2026); earner woman; status married; children born 2008-09-15, 2014-01-01, 2025-06-06.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2008-09-15: turns 18, «שנת בגרות» (s 40(b)(3), line 1645): ½ («ו־½ נקודת זיכוי בעד כל אחד מילדיה בשנת בגרותו») -> 0.5 [ITO s 66(c)(4)(a) (line 2466)]
- child born 2014-01-01: turns 12 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 2) -> 2 [ITO s 66(c)(4)(a) (line 2466)]
- child born 2025-06-06: turns 1 («החל בשנת המס שלאחר לידתו ועד לשנת המס שבה מלאו לו שנתיים» 4½) -> 4.5 [ITO s 66(c)(4)(a) (line 2466)]
- total 9.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 28,314
Tax on annual taxable income 264,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 36,000 = 11,160
- gross 46,152; less credits 28,314; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 17,838
- annual tax 17,838; monthly = annual ÷ 12 = **1,486.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 14,297 = 1,000.79; total **1,080.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 14,297 = **987.9618**; expected = the input.

Child allowance for 2026-09: 2008-09-15: counted (turns 18 this month on day 15: entitlement ends on the birthday, s 65(a) «ולא מלאו לו 18 שנים», line 807, but «תשלום הקצבה יסתיים ביום האחרון של החודש שבו נפסקה הזכאות», s 72(a), line 854); 2014-01-01: counted; 2025-06-06: counted. 3 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 + 219 = **611**.

Net = 22,000 − 1,486.5 − 1,080.9012 − 987.9618 + 611 = **19,055.637**.

**Expected:** tax 1486.5 | NI 1080.9012 | health 987.9618 (input) | allowance 611 | net 19055.637.
To the agora: tax 1486.50 | NI 1080.90 | health 987.96 | allowance 611.00 | net 19055.64.

### H13: married woman liable to additional tax, husband without income

Facts: month 2026-10; salary 70,000 a month (the same in every month of 2026); earner woman; status married; children born 2016-03-01, 2020-07-07; note=husband has no income; children live with both parents.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2016-03-01: turns 10 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 2) -> 2 [ITO s 66(c)(4)(a) (line 2466)]
- child born 2020-07-07: turns 6 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 2) -> 2 [ITO s 66(c)(4)(a) (line 2466)]
- total 6.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 19,602
Tax on annual taxable income 840,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 73,200 = 22,692
- 35% (s 121(a)(2), line 4352) × 259,080 = 90,678
- 47% (s 121(a)(3), line 4353) × 279,720 = 131,468.4
- gross 279,830.4; less credits 19,602; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 260,228.4
- s 121B(a) (line 4456, «הכנסתו החייבת בשנת המס עלתה על ... 721,560 ... בשיעור של 3%»): 3% × (840,000 − 721,560) = 3,553.2
- annual tax 263,781.6; monthly = annual ÷ 12 = **21,981.8**

NI deduction: maximum (s 348(a), line 3763; Sch. K item 1, line 4758, «הסכום הבסיסי, כפול 5»; basic amount s 1 para (3), line 191, 2026: 10,382): base capped at 51,910; all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 44,207 = 3,094.49; total **3,174.6012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 44,207 = **2,534.3088**; expected = the input.

Child allowance for 2026-10: 2016-03-01: counted; 2020-07-07: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**. The earner, the mother, is liable to additional tax; but the children, who have two parents and live with both, are in the count of «האב המבוטח» (s 67(b), line 818), and it is that insured parent whom s 66 (line 814) tests; the father has no income, so the exclusion does not reach the allowance (reading D8; payment goes to the mother, s 69(a), line 837).

Net = 70,000 − 21,981.8 − 3,174.6012 − 2,534.3088 + 392 = **42,701.29**.

**Expected:** tax 21981.8 | NI 3174.6012 | health 2534.3088 (input) | allowance 392 | net 42701.29.
To the agora: tax 21981.80 | NI 3174.60 | health 2534.31 | allowance 392.00 | net 42701.29.

### H14: married woman, no separate calculation (joint, ss 64B, 65)

Facts: month 2026-04; salary 9,000 a month (the same in every month of 2026); earner woman; status married; children born 2018-05-10, 2022-11-11; separate=False.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- no separate calculation: joint computation in the registered spouse's name (ITO s 65, line 2448, «הכנסת בני זוג יראוה ... כהכנסת בן הזוג הרשום»; s 64B(a), line 2440); child points exist only in s 66(c)(4)-(5) for a separate calculation, so none
- total 2.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 7,986
Tax on annual taxable income 108,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 23,880 = 3,343.2
- gross 11,755.2; less credits 7,986; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 3,769.2
- annual tax 3,769.2; monthly = annual ÷ 12 = **314.1**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 1,297 = 90.79; total **170.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 1,297 = **315.8618**; expected = the input.

Child allowance for 2026-04: 2018-05-10: counted; 2022-11-11: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 9,000 − 314.1 − 170.9012 − 315.8618 + 392 = **8,591.137**.

**Expected:** tax 314.1 | NI 170.9012 | health 315.8618 (input) | allowance 392 | net 8591.137.
To the agora: tax 314.10 | NI 170.90 | health 315.86 | allowance 392.00 | net 8591.14.

### H15: divorced single mother, 2 children

Facts: month 2026-01; salary 16,000 a month (the same in every month of 2026); earner woman; status divorced; children born 2017-04-04, 2021-08-08.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- child born 2017-04-04 (turns 9), living with the parent: ITO s 40(b)(1) (line 1633): 2
- child born 2021-08-08 (turns 5), living with the parent: ITO s 40(b)(1) (line 1633): 2.5
- ITO s 40(b)(2) (line 1640, «הורים החיים בנפרד יקבל ההורה הזכאי לנקודת זיכוי לפי פסקה (1), נקודת זיכוי אחת נוספת»): 1
- total 8.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 23,958
Tax on annual taxable income 192,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 71,280 = 14,256
- gross 27,792; less credits 23,958; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 3,834
- annual tax 3,834; monthly = annual ÷ 12 = **319.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 8,297 = 580.79; total **660.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 8,297 = **677.7618**; expected = the input.

Child allowance for 2026-01: 2017-04-04: counted; 2021-08-08: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 16,000 − 319.5 − 660.9012 − 677.7618 + 392 = **14,733.837**.

**Expected:** tax 319.5 | NI 660.9012 | health 677.7618 (input) | allowance 392 | net 14733.837.
To the agora: tax 319.50 | NI 660.90 | health 677.76 | allowance 392.00 | net 14733.84.

### H16: divorced single father, child living with him

Facts: month 2026-02; salary 14,000 a month (the same in every month of 2026); earner man; status divorced; children born 2015-05-05.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- child born 2015-05-05 (turns 11), living with the parent: ITO s 40(b)(1) (line 1633): 2
- ITO s 40(b)(2) (line 1640, «הורים החיים בנפרד יקבל ההורה הזכאי לנקודת זיכוי לפי פסקה (1), נקודת זיכוי אחת נוספת»): 1
- total 5.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 15,246
Tax on annual taxable income 168,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 47,280 = 9,456
- gross 22,992; less credits 15,246; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 7,746
- annual tax 7,746; monthly = annual ÷ 12 = **645.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 6,297 = 440.79; total **520.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 6,297 = **574.3618**; expected = the input.

Child allowance for 2026-02: 2015-05-05: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**. The child lives with the father only, so is in his count (s 67(b)) and is paid to him (s 69(a), line 837).

Net = 14,000 − 645.5 − 520.9012 − 574.3618 + 173 = **12,432.237**.

**Expected:** tax 645.5 | NI 520.9012 | health 574.3618 (input) | allowance 173 | net 12432.237.
To the agora: tax 645.50 | NI 520.90 | health 574.36 | allowance 173.00 | net 12432.24.

### H17: widowed mother, 2 children (s 40(b)(1ב))

Facts: month 2026-03; salary 22,000 a month (the same in every month of 2026); earner woman; status widowed; children born 2019-01-01, 2023-03-03.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- child born 2019-01-01 (turns 7), living with the parent: ITO s 40(b)(1) (line 1633): 2
- child born 2023-03-03 (turns 3), living with the parent: ITO s 40(b)(1) (line 1633): 3.5
- ITO s 40(b)(1ב) (line 1639): the other parent is deceased, so each child is «ילד להורה אחד» (line 1642): «נקודת זיכוי אחת נוספת»: 1
- and, by the same paragraph, the s 40(b)(1א) points (lines 1635-1637) for the child born 2019-01-01 (turns 7): 1
- and, by the same paragraph, the s 40(b)(1א) points (lines 1635-1637) for the child born 2023-03-03 (turns 3): 3.5
- total 13.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 39,930
Tax on annual taxable income 264,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 36,000 = 11,160
- gross 46,152; less credits 39,930; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 6,222
- annual tax 6,222; monthly = annual ÷ 12 = **518.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 14,297 = 1,000.79; total **1,080.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 14,297 = **987.9618**; expected = the input.

Child allowance for 2026-03: 2019-01-01: counted; 2023-03-03: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 22,000 − 518.5 − 1,080.9012 − 987.9618 + 392 = **19,804.637**.

**Expected:** tax 518.5 | NI 1080.9012 | health 987.9618 (input) | allowance 392 | net 19804.637.
To the agora: tax 518.50 | NI 1080.90 | health 987.96 | allowance 392.00 | net 19804.64.

### H18: single mother, newborn born 10 March 2026, month of birth

Facts: month 2026-03; salary 7,000 a month (the same in every month of 2026); earner woman; status divorced; children born 2026-03-10, 2020-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- child born 2026-03-10 (turns 0), living with the parent: ITO s 40(b)(1) (line 1633): 2.5
- child born 2020-02-02 (turns 6), living with the parent: ITO s 40(b)(1) (line 1633): 2
- ITO s 40(b)(2) (line 1640, «הורים החיים בנפרד יקבל ההורה הזכאי לנקודת זיכוי לפי פסקה (1), נקודת זיכוי אחת נוספת»): 1
- total 8.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 23,958
Tax on annual taxable income 84,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,000 = 8,400
- gross 8,400; less credits 23,958; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,000 = 72.8; total **72.8**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,000 = **226.1**; expected = the input.

Child allowance for 2026-03: 2026-03-10: counted (born this month on day 10: «נוצרה זכאות ... עד 15 בחודש פלוני, תשולם הקצבה החל ב־1 באותו חודש», s 72(a), line 854); 2020-02-02: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 7,000 − 0 − 72.8 − 226.1 + 392 = **7,093.1**.

**Expected:** tax 0 | NI 72.8 | health 226.1 (input) | allowance 392 | net 7093.1.
To the agora: tax 0.00 | NI 72.80 | health 226.10 | allowance 392.00 | net 7093.10.

### H19: single mother, newborn born 20 March 2026, month of birth

Facts: month 2026-03; salary 7,000 a month (the same in every month of 2026); earner woman; status divorced; children born 2026-03-20, 2020-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- child born 2026-03-20 (turns 0), living with the parent: ITO s 40(b)(1) (line 1633): 2.5
- child born 2020-02-02 (turns 6), living with the parent: ITO s 40(b)(1) (line 1633): 2
- ITO s 40(b)(2) (line 1640, «הורים החיים בנפרד יקבל ההורה הזכאי לנקודת זיכוי לפי פסקה (1), נקודת זיכוי אחת נוספת»): 1
- total 8.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 23,958
Tax on annual taxable income 84,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,000 = 8,400
- gross 8,400; less credits 23,958; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,000 = 72.8; total **72.8**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,000 = **226.1**; expected = the input.

Child allowance for 2026-03: 2026-03-20: not counted (born this month on day 20: «נוצרה הזכאות אחרי 15 בחודש פלוני, תשולם הקצבה החל ב־1 בחודש שלאחריו», s 72(a)); 2020-02-02: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 7,000 − 0 − 72.8 − 226.1 + 173 = **6,874.1**.

**Expected:** tax 0 | NI 72.8 | health 226.1 (input) | allowance 173 | net 6874.1.
To the agora: tax 0.00 | NI 72.80 | health 226.10 | allowance 173.00 | net 6874.10.

### H20: as H19, the month after birth

Facts: month 2026-04; salary 7,000 a month (the same in every month of 2026); earner woman; status divorced; children born 2026-03-20, 2020-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- child born 2026-03-20 (turns 0), living with the parent: ITO s 40(b)(1) (line 1633): 2.5
- child born 2020-02-02 (turns 6), living with the parent: ITO s 40(b)(1) (line 1633): 2
- ITO s 40(b)(2) (line 1640, «הורים החיים בנפרד יקבל ההורה הזכאי לנקודת זיכוי לפי פסקה (1), נקודת זיכוי אחת נוספת»): 1
- total 8.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 23,958
Tax on annual taxable income 84,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,000 = 8,400
- gross 8,400; less credits 23,958; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,000 = 72.8; total **72.8**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,000 = **226.1**; expected = the input.

Child allowance for 2026-04: 2026-03-20: counted (born after the 15th of last month: first month of payment, s 72(a)); 2020-02-02: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 7,000 − 0 − 72.8 − 226.1 + 392 = **7,093.1**.

**Expected:** tax 0 | NI 72.8 | health 226.1 (input) | allowance 392 | net 7093.1.
To the agora: tax 0.00 | NI 72.80 | health 226.10 | allowance 392.00 | net 7093.10.

### H21: married man, newborn born 15 May 2026, month of birth

Facts: month 2026-05; salary 15,000 a month (the same in every month of 2026); earner man; status married; children born 2026-05-15, 2014-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2026-05-15: year of birth («בשנת לידתו» 2½) -> 2.5 [ITO s 66(c)(5)(א) (lines 2474-2476)]
- child born 2014-02-02: turns 12 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 5.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 16,698
Tax on annual taxable income 180,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 59,280 = 11,856
- gross 25,392; less credits 16,698; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 8,694
- annual tax 8,694; monthly = annual ÷ 12 = **724.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 7,297 = 510.79; total **590.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 7,297 = **626.0618**; expected = the input.

Child allowance for 2026-05: 2026-05-15: counted (born this month on day 15: «נוצרה זכאות ... עד 15 בחודש פלוני, תשולם הקצבה החל ב־1 באותו חודש», s 72(a), line 854); 2014-02-02: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 15,000 − 724.5 − 590.9012 − 626.0618 + 392 = **13,450.537**.

**Expected:** tax 724.5 | NI 590.9012 | health 626.0618 (input) | allowance 392 | net 13450.537.
To the agora: tax 724.50 | NI 590.90 | health 626.06 | allowance 392.00 | net 13450.54.

### H22: married man, newborn born 16 May 2026, month of birth

Facts: month 2026-05; salary 15,000 a month (the same in every month of 2026); earner man; status married; children born 2026-05-16, 2014-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2026-05-16: year of birth («בשנת לידתו» 2½) -> 2.5 [ITO s 66(c)(5)(א) (lines 2474-2476)]
- child born 2014-02-02: turns 12 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 5.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 16,698
Tax on annual taxable income 180,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 59,280 = 11,856
- gross 25,392; less credits 16,698; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 8,694
- annual tax 8,694; monthly = annual ÷ 12 = **724.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 7,297 = 510.79; total **590.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 7,297 = **626.0618**; expected = the input.

Child allowance for 2026-05: 2026-05-16: not counted (born this month on day 16: «נוצרה הזכאות אחרי 15 בחודש פלוני, תשולם הקצבה החל ב־1 בחודש שלאחריו», s 72(a)); 2014-02-02: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 15,000 − 724.5 − 590.9012 − 626.0618 + 173 = **13,231.537**.

**Expected:** tax 724.5 | NI 590.9012 | health 626.0618 (input) | allowance 173 | net 13231.537.
To the agora: tax 724.50 | NI 590.90 | health 626.06 | allowance 173.00 | net 13231.54.

### H23: as H22, the month after birth

Facts: month 2026-06; salary 15,000 a month (the same in every month of 2026); earner man; status married; children born 2026-05-16, 2014-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2026-05-16: year of birth («בשנת לידתו» 2½) -> 2.5 [ITO s 66(c)(5)(א) (lines 2474-2476)]
- child born 2014-02-02: turns 12 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 5.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 16,698
Tax on annual taxable income 180,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 59,280 = 11,856
- gross 25,392; less credits 16,698; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 8,694
- annual tax 8,694; monthly = annual ÷ 12 = **724.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 7,297 = 510.79; total **590.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 7,297 = **626.0618**; expected = the input.

Child allowance for 2026-06: 2026-05-16: counted (born after the 15th of last month: first month of payment, s 72(a)); 2014-02-02: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 15,000 − 724.5 − 590.9012 − 626.0618 + 392 = **13,450.537**.

**Expected:** tax 724.5 | NI 590.9012 | health 626.0618 (input) | allowance 392 | net 13450.537.
To the agora: tax 724.50 | NI 590.90 | health 626.06 | allowance 392.00 | net 13450.54.

### H24: married man, child turns 18 on 1 June 2026, June

Facts: month 2026-06; salary 10,000 a month (the same in every month of 2026); earner man; status married; children born 2008-06-01, 2012-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2008-06-01: turns 18, «שנת בגרות» (s 40(b)(3), line 1645): 0 -> 0 [ITO s 66(c)(5) (lines 2474-2476): nothing in the year of majority]
- child born 2012-02-02: turns 14 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 120,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 35,880 = 5,023.2
- gross 13,435.2; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 3,997.2
- annual tax 3,997.2; monthly = annual ÷ 12 = **333.1**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 2,297 = 160.79; total **240.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 2,297 = **367.5618**; expected = the input.

Child allowance for 2026-06: 2008-06-01: counted (turns 18 this month on day 1: entitlement ends on the birthday, s 65(a) «ולא מלאו לו 18 שנים», line 807, but «תשלום הקצבה יסתיים ביום האחרון של החודש שבו נפסקה הזכאות», s 72(a), line 854); 2012-02-02: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 10,000 − 333.1 − 240.9012 − 367.5618 + 392 = **9,450.437**.

**Expected:** tax 333.1 | NI 240.9012 | health 367.5618 (input) | allowance 392 | net 9450.437.
To the agora: tax 333.10 | NI 240.90 | health 367.56 | allowance 392.00 | net 9450.44.

### H25: as H24, July

Facts: month 2026-07; salary 10,000 a month (the same in every month of 2026); earner man; status married; children born 2008-06-01, 2012-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2008-06-01: turns 18, «שנת בגרות» (s 40(b)(3), line 1645): 0 -> 0 [ITO s 66(c)(5) (lines 2474-2476): nothing in the year of majority]
- child born 2012-02-02: turns 14 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 120,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 35,880 = 5,023.2
- gross 13,435.2; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 3,997.2
- annual tax 3,997.2; monthly = annual ÷ 12 = **333.1**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 2,297 = 160.79; total **240.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 2,297 = **367.5618**; expected = the input.

Child allowance for 2026-07: 2008-06-01: not counted (turned 18 in an earlier month); 2012-02-02: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 10,000 − 333.1 − 240.9012 − 367.5618 + 173 = **9,231.437**.

**Expected:** tax 333.1 | NI 240.9012 | health 367.5618 (input) | allowance 173 | net 9231.437.
To the agora: tax 333.10 | NI 240.90 | health 367.56 | allowance 173.00 | net 9231.44.

### H26: married man, child turns 18 on 20 June 2026, June

Facts: month 2026-06; salary 10,000 a month (the same in every month of 2026); earner man; status married; children born 2008-06-20, 2012-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2008-06-20: turns 18, «שנת בגרות» (s 40(b)(3), line 1645): 0 -> 0 [ITO s 66(c)(5) (lines 2474-2476): nothing in the year of majority]
- child born 2012-02-02: turns 14 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 120,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 35,880 = 5,023.2
- gross 13,435.2; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 3,997.2
- annual tax 3,997.2; monthly = annual ÷ 12 = **333.1**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 2,297 = 160.79; total **240.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 2,297 = **367.5618**; expected = the input.

Child allowance for 2026-06: 2008-06-20: counted (turns 18 this month on day 20: entitlement ends on the birthday, s 65(a) «ולא מלאו לו 18 שנים», line 807, but «תשלום הקצבה יסתיים ביום האחרון של החודש שבו נפסקה הזכאות», s 72(a), line 854); 2012-02-02: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 10,000 − 333.1 − 240.9012 − 367.5618 + 392 = **9,450.437**.

**Expected:** tax 333.1 | NI 240.9012 | health 367.5618 (input) | allowance 392 | net 9450.437.
To the agora: tax 333.10 | NI 240.90 | health 367.56 | allowance 392.00 | net 9450.44.

### H27: as H24, May

Facts: month 2026-05; salary 10,000 a month (the same in every month of 2026); earner man; status married; children born 2008-06-01, 2012-02-02.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2008-06-01: turns 18, «שנת בגרות» (s 40(b)(3), line 1645): 0 -> 0 [ITO s 66(c)(5) (lines 2474-2476): nothing in the year of majority]
- child born 2012-02-02: turns 14 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 120,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 35,880 = 5,023.2
- gross 13,435.2; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 3,997.2
- annual tax 3,997.2; monthly = annual ÷ 12 = **333.1**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 2,297 = 160.79; total **240.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 2,297 = **367.5618**; expected = the input.

Child allowance for 2026-05: 2008-06-01: counted; 2012-02-02: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 10,000 − 333.1 − 240.9012 − 367.5618 + 392 = **9,450.437**.

**Expected:** tax 333.1 | NI 240.9012 | health 367.5618 (input) | allowance 392 | net 9450.437.
To the agora: tax 333.10 | NI 240.90 | health 367.56 | allowance 392.00 | net 9450.44.

### H28: married man, blind wife (s 37), separate calculation

Facts: month 2026-02; salary 13,000 a month (the same in every month of 2026); earner man; status married; children born 2016-03-01; spouse_beneficiary=True; note=wife blind within s 9(5), no income, supported by the earner.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- s 37 beneficiary individual (line 1600) in a separate calculation: ITO s 66(c)(2) (line 2463, «תובא בחשבון 1/2 נקודת זיכוי בלבד»): 1/2
- child born 2016-03-01: turns 10 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 10,890
Tax on annual taxable income 156,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 35,280 = 7,056
- gross 20,592; less credits 10,890; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 9,702
- annual tax 9,702; monthly = annual ÷ 12 = **808.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 5,297 = 370.79; total **450.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 5,297 = **522.6618**; expected = the input.

Child allowance for 2026-02: 2016-03-01: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 13,000 − 808.5 − 450.9012 − 522.6618 + 173 = **11,390.937**.

**Expected:** tax 808.5 | NI 450.9012 | health 522.6618 (input) | allowance 173 | net 11390.937.
To the agora: tax 808.50 | NI 450.90 | health 522.66 | allowance 173.00 | net 11390.94.

### H29: married man, blind wife (s 37), joint computation

Facts: month 2026-02; salary 13,000 a month (the same in every month of 2026); earner man; status married; children born 2016-03-01; separate=False; spouse_beneficiary=True; note=as H28 but no separate calculation.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- no separate calculation: joint computation in the registered spouse's name (ITO s 65, line 2448, «הכנסת בני זוג יראוה ... כהכנסת בן הזוג הרשום»; s 64B(a), line 2440); child points exist only in s 66(c)(4)-(5) for a separate calculation, so none
- ITO s 37 (line 1600, «יחיד מוטב ... שכלכלת בן זוגו היתה עליו, תובא בחשבון נקודת זיכוי אחת»): 1
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 156,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 35,280 = 7,056
- gross 20,592; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 11,154
- annual tax 11,154; monthly = annual ÷ 12 = **929.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 5,297 = 370.79; total **450.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 5,297 = **522.6618**; expected = the input.

Child allowance for 2026-02: 2016-03-01: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 13,000 − 929.5 − 450.9012 − 522.6618 + 173 = **11,269.937**.

**Expected:** tax 929.5 | NI 450.9012 | health 522.6618 (input) | allowance 173 | net 11269.937.
To the agora: tax 929.50 | NI 450.90 | health 522.66 | allowance 173.00 | net 11269.94.

### H30: married man, joint computation, 2 children

Facts: month 2026-02; salary 13,000 a month (the same in every month of 2026); earner man; status married; children born 2016-03-01, 2020-07-07; separate=False.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- no separate calculation: joint computation in the registered spouse's name (ITO s 65, line 2448, «הכנסת בני זוג יראוה ... כהכנסת בן הזוג הרשום»; s 64B(a), line 2440); child points exist only in s 66(c)(4)-(5) for a separate calculation, so none
- total 2.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 6,534
Tax on annual taxable income 156,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 35,280 = 7,056
- gross 20,592; less credits 6,534; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 14,058
- annual tax 14,058; monthly = annual ÷ 12 = **1,171.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 5,297 = 370.79; total **450.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 5,297 = **522.6618**; expected = the input.

Child allowance for 2026-02: 2016-03-01: counted; 2020-07-07: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 13,000 − 1,171.5 − 450.9012 − 522.6618 + 392 = **11,246.937**.

**Expected:** tax 1171.5 | NI 450.9012 | health 522.6618 (input) | allowance 392 | net 11246.937.
To the agora: tax 1171.50 | NI 450.90 | health 522.66 | allowance 392.00 | net 11246.94.

### H31: immigrant (arrived 1 July 2024), s 35

Facts: month 2026-03; salary 14,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; immigrant=2024-07-01.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 35(a) as for an immigrant from 2022 (lines 1575-1578), counted by the months of the 54 that fall in 2026 (s 35(c), line 1580), arrival 2024-07-01: 3
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 6.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 18,150
Tax on annual taxable income 168,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 47,280 = 9,456
- gross 22,992; less credits 18,150; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 4,842
- annual tax 4,842; monthly = annual ÷ 12 = **403.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 6,297 = 440.79; total **520.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 6,297 = **574.3618**; expected = the input.

Child allowance for 2026-03: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 14,000 − 403.5 − 520.9012 − 574.3618 + 173 = **12,674.237**.

**Expected:** tax 403.5 | NI 520.9012 | health 574.3618 (input) | allowance 173 | net 12674.237.
To the agora: tax 403.50 | NI 520.90 | health 574.36 | allowance 173.00 | net 12674.24.

### H32: immigrant (arrived 1 January 2023), s 35 tapering bands

Facts: month 2026-03; salary 14,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; immigrant=2023-01-01.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 35(a) as for an immigrant from 2022 (lines 1575-1578), counted by the months of the 54 that fall in 2026 (s 35(c), line 1580), arrival 2023-01-01: 1.5
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 4.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 13,794
Tax on annual taxable income 168,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 47,280 = 9,456
- gross 22,992; less credits 13,794; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 9,198
- annual tax 9,198; monthly = annual ÷ 12 = **766.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 6,297 = 440.79; total **520.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 6,297 = **574.3618**; expected = the input.

Child allowance for 2026-03: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 14,000 − 766.5 − 520.9012 − 574.3618 + 173 = **12,311.237**.

**Expected:** tax 766.5 | NI 520.9012 | health 574.3618 (input) | allowance 173 | net 12311.237.
To the agora: tax 766.50 | NI 520.90 | health 574.36 | allowance 173.00 | net 12311.24.

### H33: immigrant arrived 1 December 2025: 5786-2026 temporary exemption

Facts: month 2026-03; salary 20,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; immigrant=2025-12-01.

Tax: the earner first became resident on 2025-12-01, inside «מיום י״ד בחשוון התשפ״ו (5 בנובמבר 2025) ועד תום שנת המס 2026», so the Encouragement of Aliyah (Temporary Provision) Law 5786-2026 s 2(a)(1) (enacted by the 5786-2026 Economic Efficiency Law ch D s 9, SH 3511 p. 417; deposited PDF `25_lsr_12235101.pdf` p. 5) exempts personal-exertion income in 2026 «עד לתקרת הכנסה של 600,000 שקלים חדשים», pro rata to the period of residence in 2026 (s 2(d)); resident all of 2026, annual salary 240,000 ≤ 600,000, so annual tax 0, monthly **0**. (A capstone that does not compose this temporary Law should decline by name; a positive figure under s 35 alone is wrong.)

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 12,297 = 860.79; total **940.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 12,297 = **884.5618**; expected = the input.

Child allowance for 2026-03: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 20,000 − 0 − 940.9012 − 884.5618 + 173 = **18,347.537**.

**Expected:** tax 0 | NI 940.9012 | health 884.5618 (input) | allowance 173 | net 18347.537.
To the agora: tax 0.00 | NI 940.90 | health 884.56 | allowance 173.00 | net 18347.54.

### H34: married man, pension contributions, not a beneficiary member (s 45A(d))

Facts: month 2026-04; salary 6,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; pension_emp=360.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
- s 45A credit: employee pension contributions 4,320 a year to a «קופת גמל לקצבה» at 35% (s 45A(b), line 1718); the amount credited is capped at the higher of 2,268 (s 45A(d)(1), line 1726 note) and the lower of the sums paid and 7% of the qualifying income (s 45A(d)(2)(b)(2) or (e)(2)(b)(2)(a), lines 1730, 1737; qualifying income = annual salary up to 116,400, s 47(a)(1)(1), line 1766 note) = 4,320; credit 1,512; no s 47 deduction, because the whole salary is insured income (s 47(a)(4), line 1771) and so neither s 47(b)(2) (line 1781, «שאינה הכנסה מבוטחת») nor s 47(b1) (lines 1784-1785, «ההכנסה לעמית עצמאי», «ההכנסה הנוספת», both nil) reaches it
Tax on annual taxable income 72,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 72,000 = 7,200
- gross 7,200; less credits 10,950; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 6,000 = 62.4; total **62.4**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 6,000 = **193.8**; expected = the input.

Child allowance for 2026-04: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 6,000 − 0 − 62.4 − 193.8 + 173 = **5,916.8**.

**Expected:** tax 0 | NI 62.4 | health 193.8 (input) | allowance 173 | net 5916.8.
To the agora: tax 0.00 | NI 62.40 | health 193.80 | allowance 173.00 | net 5916.80.

### H35: married man, pension contributions, beneficiary member, cap binds (s 45A(e))

Facts: month 2026-04; salary 20,000 a month (the same in every month of 2026); earner man; status married; children born 2016-03-01, 2020-07-07; pension_emp=1400.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2016-03-01: turns 10 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- child born 2020-07-07: turns 6 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 4.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 12,342
- s 45A credit: employee pension contributions 16,800 a year to a «קופת גמל לקצבה» at 35% (s 45A(b), line 1718); the amount credited is capped at the higher of 2,268 (s 45A(d)(1), line 1726 note) and the lower of the sums paid and 7% of the qualifying income (s 45A(d)(2)(b)(2) or (e)(2)(b)(2)(a), lines 1730, 1737; qualifying income = annual salary up to 116,400, s 47(a)(1)(1), line 1766 note) = 8,148; credit 2,851.8; no s 47 deduction, because the whole salary is insured income (s 47(a)(4), line 1771) and so neither s 47(b)(2) (line 1781, «שאינה הכנסה מבוטחת») nor s 47(b1) (lines 1784-1785, «ההכנסה לעמית עצמאי», «ההכנסה הנוספת», both nil) reaches it
Tax on annual taxable income 240,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 12,000 = 3,720
- gross 38,712; less credits 15,193.8; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 23,518.2
- annual tax 23,518.2; monthly = annual ÷ 12 = **1,959.85**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 12,297 = 860.79; total **940.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 12,297 = **884.5618**; expected = the input.

Child allowance for 2026-04: 2016-03-01: counted; 2020-07-07: counted. 2 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 = **392**.

Net = 20,000 − 1,959.85 − 940.9012 − 884.5618 + 392 = **16,606.687**.

**Expected:** tax 1959.85 | NI 940.9012 | health 884.5618 (input) | allowance 392 | net 16606.687.
To the agora: tax 1959.85 | NI 940.90 | health 884.56 | allowance 392.00 | net 16606.69.

### H36: married man, pension and life insurance (s 45A(a),(b))

Facts: month 2026-04; salary 9,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; pension_emp=450; life=100.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
- s 45A credit: employee pension contributions 5,400 a year to a «קופת גמל לקצבה» at 35% (s 45A(b), line 1718), life-insurance premiums 1,200 at 25% (s 45A(a)(1), line 1716); the amount credited is capped at the higher of 2,268 (s 45A(d)(1), line 1726 note) and the lower of the sums paid and 7% of the qualifying income (s 45A(d)(2)(b)(2) or (e)(2)(b)(2)(a), lines 1730, 1737; qualifying income = annual salary up to 116,400, s 47(a)(1)(1), line 1766 note) = 6,600; credit 2,190; no s 47 deduction, because the whole salary is insured income (s 47(a)(4), line 1771) and so neither s 47(b)(2) (line 1781, «שאינה הכנסה מבוטחת») nor s 47(b1) (lines 1784-1785, «ההכנסה לעמית עצמאי», «ההכנסה הנוספת», both nil) reaches it
Tax on annual taxable income 108,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 23,880 = 3,343.2
- gross 11,755.2; less credits 11,628; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 127.2
- annual tax 127.2; monthly = annual ÷ 12 = **10.6**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 1,297 = 90.79; total **170.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 1,297 = **315.8618**; expected = the input.

Child allowance for 2026-04: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 9,000 − 10.6 − 170.9012 − 315.8618 + 173 = **8,675.637**.

**Expected:** tax 10.6 | NI 170.9012 | health 315.8618 (input) | allowance 173 | net 8675.637.
To the agora: tax 10.60 | NI 170.90 | health 315.86 | allowance 173.00 | net 8675.64.

### H37: controlling shareholder below the NI threshold (NII s 335)

Facts: month 2026-05; salary 7,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; branches=controlling.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 84,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,000 = 8,400
- gross 8,400; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: controlling shareholder: s 335(e) (line 3615, «למעט בעל שליטה בחברת מעטים») takes the unemployment branch out of s 342(c)(1); reading D5: printed totals less the unemployment items (Sch. J line 4725: 0.21 above; Amendment 252 s 7(a)(3)(b): 0.02 below): 1.02% and 6.79% (alternative sum-of-items reading: 1.02% and 4.46%). 1.02% × 7,000 = 71.4; total **71.4**.
Alternative reading `controlling_R1`: 71.4.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,000 = **226.1**; expected = the input.

Child allowance for 2026-05: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 7,000 − 0 − 71.4 − 226.1 + 173 = **6,875.5**.

**Expected:** tax 0 | NI 71.4 | health 226.1 (input) | allowance 173 | net 6875.5.
To the agora: tax 0.00 | NI 71.40 | health 226.10 | allowance 173.00 | net 6875.50.

### H38: controlling shareholder above the NI threshold

Facts: month 2026-05; salary 30,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; branches=controlling.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 360,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 73,200 = 22,692
- 35% (s 121(a)(2), line 4352) × 58,800 = 20,580
- gross 78,264; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 68,826
- annual tax 68,826; monthly = annual ÷ 12 = **5,735.5**

NI deduction: controlling shareholder: s 335(e) (line 3615, «למעט בעל שליטה בחברת מעטים») takes the unemployment branch out of s 342(c)(1); reading D5: printed totals less the unemployment items (Sch. J line 4725: 0.21 above; Amendment 252 s 7(a)(3)(b): 0.02 below): 1.02% and 6.79% (alternative sum-of-items reading: 1.02% and 4.46%). 1.02% × 7,703 = 78.5706; 6.79% × 22,297 = 1,513.9663; total **1,592.5369**.
Alternative reading `controlling_R1`: 1,073.0168.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 22,297 = **1,401.5618**; expected = the input.

Child allowance for 2026-05: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 30,000 − 5,735.5 − 1,592.5369 − 1,401.5618 + 173 = **21,443.4013**.

**Expected:** tax 5735.5 | NI 1592.5369 | health 1401.5618 (input) | allowance 173 | net 21443.4013.
To the agora: tax 5735.50 | NI 1592.54 | health 1401.56 | allowance 173.00 | net 21443.40.

### H39: non-resident man

Facts: month 2026-06; salary 10,000 a month (the same in every month of 2026); earner man; status single; children born 2018-05-10; branches=nonresident_R2; resident=False; note=non-resident; never married; one child, living abroad with its mother.

Credit points, tax year 2026:
- non-resident: no s 34 or s 36 points (both say «יחיד ... תושב ישראל», lines 1570, 1594)
- never married; children abroad with their other parent: no s 40(b) or s 66(c) points
- total 0 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 0
Tax on annual taxable income 120,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 35,880 = 5,023.2
- gross 13,435.2; less credits 0; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 13,435.2
- annual tax 13,435.2; monthly = annual ÷ 12 = **1,119.6**

NI deduction: non-resident: only s 335(a) (line 3611, «עובד ... שאינו תושב ישראל ישתלמו בעדו דמי ביטוח אימהות») among the branches listed in s 342(c)(1); reading D5 (totals less the items of branches (d), (e), (g), (h), (i): 0.07+0.21+1.86+0.14+1.52 = 3.80 above; 0.03+0.02+0.29+0.03+0.57 = 0.94 below): 0.10% and 3.20%; alternative (maternity item alone, Sch. J line 4720 and Amendment 252: 0.87 above, 0.10 below): 0.10% and 0.87%. 0.1% × 7,703 = 7.703; 3.2% × 2,297 = 73.504; total **81.207**.
Alternative reading `nonresident_R1`: 27.6869.

Health deduction: an input; a non-resident is not insured under the National Health Insurance Law, so supplied as **0**; expected = the input.

Child allowance: **0**: the parent is not «מבוטח» (NII s 65(a), lines 801-803: insured under ch 11, or «יחיד היושב בישראל») and the child is not «נמצא בישראל» (line 807).

Net = 10,000 − 1,119.6 − 81.207 − 0 + 0 = **8,799.193**.

**Expected:** tax 1119.6 | NI 81.207 | health 0 (input) | allowance 0 | net 8799.193.
To the agora: tax 1119.60 | NI 81.21 | health 0.00 | allowance 0.00 | net 8799.19.

### H40: non-resident woman, below the NI threshold

Facts: month 2026-06; salary 6,000 a month (the same in every month of 2026); earner woman; status single; children born 2018-05-10; branches=nonresident_R2; resident=False; note=non-resident; never married; one child, living abroad with its father.

Credit points, tax year 2026:
- non-resident: no s 34 or s 36 points (both say «יחיד ... תושב ישראל», lines 1570, 1594)
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- never married; children abroad with their other parent: no s 40(b) or s 66(c) points
- total 0.5 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 1,452
Tax on annual taxable income 72,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 72,000 = 7,200
- gross 7,200; less credits 1,452; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 5,748
- annual tax 5,748; monthly = annual ÷ 12 = **479**

NI deduction: non-resident: only s 335(a) (line 3611, «עובד ... שאינו תושב ישראל ישתלמו בעדו דמי ביטוח אימהות») among the branches listed in s 342(c)(1); reading D5 (totals less the items of branches (d), (e), (g), (h), (i): 0.07+0.21+1.86+0.14+1.52 = 3.80 above; 0.03+0.02+0.29+0.03+0.57 = 0.94 below): 0.10% and 3.20%; alternative (maternity item alone, Sch. J line 4720 and Amendment 252: 0.87 above, 0.10 below): 0.10% and 0.87%. 0.1% × 6,000 = 6; total **6**.
Alternative reading `nonresident_R1`: 6.

Health deduction: an input; a non-resident is not insured under the National Health Insurance Law, so supplied as **0**; expected = the input.

Child allowance: **0**: the parent is not «מבוטח» (NII s 65(a), lines 801-803: insured under ch 11, or «יחיד היושב בישראל») and the child is not «נמצא בישראל» (line 807).

Net = 6,000 − 479 − 6 − 0 + 0 = **5,515**.

**Expected:** tax 479 | NI 6 | health 0 (input) | allowance 0 | net 5515.
To the agora: tax 479.00 | NI 6.00 | health 0.00 | allowance 0.00 | net 5515.00.

### H41: married man aged 71 (s 342(c)(2))

Facts: month 2026-06; salary 12,000 a month (the same in every month of 2026); earner man; status married; children born 2012-02-02; earner_beneficiary=True; branches=none; note=born 1955-01-10, aged 71.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- s 37 beneficiary individual (line 1600) in a separate calculation: ITO s 66(c)(2) (line 2463, «תובא בחשבון 1/2 נקודת זיכוי בלבד»): 1/2
- child born 2012-02-02: turns 14 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 10,890
Tax on annual taxable income 144,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 23,280 = 4,656
- gross 18,192; less credits 10,890; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 7,302
- annual tax 7,302; monthly = annual ÷ 12 = **608.5**

NI deduction: s 342(c)(2) (line 3662, «המעביד לא ינכה משכר עובדו את האחוזים האמורים ... בעד הזמן שלאחר הגיע המבוטח לגיל 70 שנים בגבר»; for a woman the age in Sch. A1 Part D, line 4453, «מאי 1950 ואילך: 70»): no deduction. 0% × 7,703 = 0; 0% × 4,297 = 0; total **0**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 4,297 = **470.9618**; expected = the input.

Child allowance for 2026-06: 2012-02-02: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 12,000 − 608.5 − 0 − 470.9618 + 173 = **11,093.5382**.

**Expected:** tax 608.5 | NI 0 | health 470.9618 (input) | allowance 173 | net 11093.5382.
To the agora: tax 608.50 | NI 0.00 | health 470.96 | allowance 173.00 | net 11093.54.

### H42: married man aged 68, no old-age pension

Facts: month 2026-06; salary 12,000 a month (the same in every month of 2026); earner man; status married; children born 2012-02-02; earner_beneficiary=True; branches=age67to70; note=born 1958-03-03, aged 68, no old-age pension.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- s 37 beneficiary individual (line 1600) in a separate calculation: ITO s 66(c)(2) (line 2463, «תובא בחשבון 1/2 נקודת זיכוי בלבד»): 1/2
- child born 2012-02-02: turns 14 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 10,890
Tax on annual taxable income 144,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 23,280 = 4,656
- gross 18,192; less credits 10,890; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 7,302
- annual tax 7,302; monthly = annual ÷ 12 = **608.5**

NI deduction: aged 68, past retirement age, no old-age pension: the unemployment branch (s 158(1), line 1444, «וטרם הגיע לגיל הקבוע לגביו ... בחלק ב׳ בלוח א׳1»), accidents (s 150, line 1405, «וטרם הגיע לגיל פרישה») and disability (s 195, line 1929, «וטרם הגיע לגיל הפרישה») are not paid; reading D5: totals less those items (0.07, 0.21, 1.86 above; 0.03, 0.02, 0.29 below): 0.70% and 4.86%. 0.7% × 7,703 = 53.921; 4.86% × 4,297 = 208.8342; total **262.7552**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 4,297 = **470.9618**; expected = the input.

Child allowance for 2026-06: 2012-02-02: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 12,000 − 608.5 − 262.7552 − 470.9618 + 173 = **10,830.783**.

**Expected:** tax 608.5 | NI 262.7552 | health 470.9618 (input) | allowance 173 | net 10830.783.
To the agora: tax 608.50 | NI 262.76 | health 470.96 | allowance 173.00 | net 10830.78.

### H43: married man who turned 70 on 20 May 2026, month of June

Facts: month 2026-06; salary 12,000 a month (the same in every month of 2026); earner man; status married; children born 2012-02-02; earner_beneficiary=True; branches=none; note=born 1956-05-20, reached 70 in May 2026.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- s 37 beneficiary individual (line 1600) in a separate calculation: ITO s 66(c)(2) (line 2463, «תובא בחשבון 1/2 נקודת זיכוי בלבד»): 1/2
- child born 2012-02-02: turns 14 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 10,890
Tax on annual taxable income 144,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 23,280 = 4,656
- gross 18,192; less credits 10,890; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 7,302
- annual tax 7,302; monthly = annual ÷ 12 = **608.5**

NI deduction: s 342(c)(2) (line 3662, «המעביד לא ינכה משכר עובדו את האחוזים האמורים ... בעד הזמן שלאחר הגיע המבוטח לגיל 70 שנים בגבר»; for a woman the age in Sch. A1 Part D, line 4453, «מאי 1950 ואילך: 70»): no deduction. 0% × 7,703 = 0; 0% × 4,297 = 0; total **0**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 4,297 = **470.9618**; expected = the input.

Child allowance for 2026-06: 2012-02-02: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 12,000 − 608.5 − 0 − 470.9618 + 173 = **11,093.5382**.

**Expected:** tax 608.5 | NI 0 | health 470.9618 (input) | allowance 173 | net 11093.5382.
To the agora: tax 608.50 | NI 0.00 | health 470.96 | allowance 173.00 | net 11093.54.

### H44: full-time employee below minimum wage, first quarter (s 348(b))

Facts: month 2026-02; salary 5,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; minwage_applies=True; note=full-time employee paid below the minimum wage.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 60,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 60,000 = 6,000
- gross 6,000; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: minimum income (s 348(b), line 3765; Sch. K item 1, line 4758, «סכום השווה לשכר מינימום של החודש הראשון ברבעון», where «שכר מינימום» includes «שכר מינימום חלקי ... לגבי עובד פלוני», line 4772): first month of the quarter January (6,247.67 from 1.4.2025) = 6,247.67; salary 5,000 is below it, so contributions run on 6,247.67 and the employer deducts the percentages «מההכנסה שלפיה משתלמים דמי הביטוח» (s 342(c)(1), line 3661); all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 6,247.67 = 64.975768; total **64.975768**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 5,000 = **161.5**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 5,000 − 0 − 64.975768 − 161.5 + 173 = **4,946.524232**.

**Expected:** tax 0 | NI 64.975768 | health 161.5 (input) | allowance 173 | net 4946.524232.
To the agora: tax 0.00 | NI 64.98 | health 161.50 | allowance 173.00 | net 4946.52.

### H45: as H44, second quarter

Facts: month 2026-05; salary 5,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; minwage_applies=True; note=as H44, second quarter.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 60,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 60,000 = 6,000
- gross 6,000; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: minimum income (s 348(b), line 3765; Sch. K item 1, line 4758, «סכום השווה לשכר מינימום של החודש הראשון ברבעון», where «שכר מינימום» includes «שכר מינימום חלקי ... לגבי עובד פלוני», line 4772): first month of the quarter April (6,443.85 from 1.4.2026) = 6,443.85; salary 5,000 is below it, so contributions run on 6,443.85 and the employer deducts the percentages «מההכנסה שלפיה משתלמים דמי הביטוח» (s 342(c)(1), line 3661); all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 6,443.85 = 67.01604; total **67.01604**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 5,000 = **161.5**; expected = the input.

Child allowance for 2026-05: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 5,000 − 0 − 67.01604 − 161.5 + 173 = **4,944.48396**.

**Expected:** tax 0 | NI 67.01604 | health 161.5 (input) | allowance 173 | net 4944.48396.
To the agora: tax 0.00 | NI 67.02 | health 161.50 | allowance 173.00 | net 4944.48.

### H46: half-time employee above the partial minimum wage

Facts: month 2026-02; salary 3,500 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; minwage_applies=True; job_fraction=0.5; note=half-time employee.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 42,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 42,000 = 4,200
- gross 4,200; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: minimum income (s 348(b), line 3765; Sch. K item 1, line 4758, «סכום השווה לשכר מינימום של החודש הראשון ברבעון», where «שכר מינימום» includes «שכר מינימום חלקי ... לגבי עובד פלוני», line 4772): first month of the quarter January (6,247.67 from 1.4.2025) × job fraction 0.5 = 3,123.835; salary 3,500 is not below it, so the actual salary is the base; all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 3,500 = 36.4; total **36.4**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 3,500 = **113.05**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 3,500 − 0 − 36.4 − 113.05 + 173 = **3,523.55**.

**Expected:** tax 0 | NI 36.4 | health 113.05 (input) | allowance 173 | net 3523.55.
To the agora: tax 0.00 | NI 36.40 | health 113.05 | allowance 173.00 | net 3523.55.

### H47: December 2025 (outside the period)

Facts: month 2025-12; salary 10,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

**Expected: REFUSE** every component (tax, NI, health pass-through, allowance, net): the month is outside 2026, the only period for which the deposited figures (s 120B(e) freeze to 2027 aside) and the temporary Schedule J of Amendment 252 s 7 (2025-2026 only, SH 3347 p. 177) are known; the BRIEF scopes months of 2026.

### H48: January 2027 (outside the period)

Facts: month 2027-01; salary 10,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

**Expected: REFUSE** every component (tax, NI, health pass-through, allowance, net): the month is outside 2026, the only period for which the deposited figures (s 120B(e) freeze to 2027 aside) and the temporary Schedule J of Amendment 252 s 7 (2025-2026 only, SH 3347 p. 177) are known; the BRIEF scopes months of 2026.

### H49: s 40C academic-degree credit (not encoded)

Facts: month 2026-03; salary 10,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; note=completed a first academic degree in 2025 and is entitled to the s 40C point in 2026.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 120,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 35,880 = 5,023.2
- gross 13,435.2; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 3,997.2
- annual tax 3,997.2; monthly = annual ÷ 12 = **333.1**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 2,297 = 160.79; total **240.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 2,297 = **367.5618**; expected = the input.

Child allowance for 2026-03: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 10,000 − 333.1 − 240.9012 − 367.5618 + 173 = **9,231.437**.

**Expected: tax REFUSE** (and so net REFUSE), because the earner is entitled to the s 40C academic-degree point (line 1655, «תובא בחשבון נקודת זיכוי אחת אם הוא זכאי לקבל תואר אקדמי ראשון»), a credit no row encodes (BRIEF line 35). NI 240.90 (exact 240.9012), health = input 367.5618, allowance 173 are still expected. (The figures above omit that credit and are not the answer for tax or net.)

### H50: s 39B reservist credit (not encoded)

Facts: month 2026-03; salary 10,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10; note=served 30 days of reserve duty as a combatant in 2025 (s 39B).

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 120,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 35,880 = 5,023.2
- gross 13,435.2; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 3,997.2
- annual tax 3,997.2; monthly = annual ÷ 12 = **333.1**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 2,297 = 160.79; total **240.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 2,297 = **367.5618**; expected = the input.

Child allowance for 2026-03: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 10,000 − 333.1 − 240.9012 − 367.5618 + 173 = **9,231.437**.

**Expected: tax REFUSE** (and so net REFUSE), because the earner served 30 days as a combat reservist in 2025, which earns s 39B points (lines 1620-1626), a credit no row encodes (BRIEF line 35). NI 240.90 (exact 240.9012), health = input 367.5618, allowance 173 are still expected. (The figures above omit that credit and are not the answer for tax or net.)

### H52: top of the 10% bracket (84,120 a year)

Facts: month 2026-02; salary 7,010 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 84,120 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- gross 8,412; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,010 = 72.904; total **72.904**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,010 = **226.423**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 7,010 − 0 − 72.904 − 226.423 + 173 = **6,883.673**.

**Expected:** tax 0 | NI 72.904 | health 226.423 (input) | allowance 173 | net 6883.673.
To the agora: tax 0.00 | NI 72.90 | health 226.42 | allowance 173.00 | net 6883.67.

### H53: top of the 14% bracket (120,720)

Facts: month 2026-02; salary 10,060 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 120,720 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- gross 13,536; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 4,098
- annual tax 4,098; monthly = annual ÷ 12 = **341.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 2,357 = 164.99; total **245.1012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 2,357 = **370.6638**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 10,060 − 341.5 − 245.1012 − 370.6638 + 173 = **9,275.735**.

**Expected:** tax 341.5 | NI 245.1012 | health 370.6638 (input) | allowance 173 | net 9275.735.
To the agora: tax 341.50 | NI 245.10 | health 370.66 | allowance 173.00 | net 9275.74.

### H54: top of the 20% bracket (228,000)

Facts: month 2026-02; salary 19,000 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 228,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- gross 34,992; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 25,554
- annual tax 25,554; monthly = annual ÷ 12 = **2,129.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 11,297 = 790.79; total **870.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 11,297 = **832.8618**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 19,000 − 2,129.5 − 870.9012 − 832.8618 + 173 = **15,339.737**.

**Expected:** tax 2129.5 | NI 870.9012 | health 832.8618 (input) | allowance 173 | net 15339.737.
To the agora: tax 2129.50 | NI 870.90 | health 832.86 | allowance 173.00 | net 15339.74.

### H55: top of the 31% bracket (301,200)

Facts: month 2026-02; salary 25,100 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 301,200 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 73,200 = 22,692
- gross 57,684; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 48,246
- annual tax 48,246; monthly = annual ÷ 12 = **4,020.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 17,397 = 1,217.79; total **1,297.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 17,397 = **1,148.2318**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 25,100 − 4,020.5 − 1,297.9012 − 1,148.2318 + 173 = **18,806.367**.

**Expected:** tax 4020.5 | NI 1297.9012 | health 1148.2318 (input) | allowance 173 | net 18806.367.
To the agora: tax 4020.50 | NI 1297.90 | health 1148.23 | allowance 173.00 | net 18806.37.

### H56: top of the 35% bracket (560,280)

Facts: month 2026-02; salary 46,690 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 560,280 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 73,200 = 22,692
- 35% (s 121(a)(2), line 4352) × 259,080 = 90,678
- gross 148,362; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 138,924
- annual tax 138,924; monthly = annual ÷ 12 = **11,577**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 38,987 = 2,729.09; total **2,809.2012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 38,987 = **2,264.4348**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 46,690 − 11,577 − 2,809.2012 − 2,264.4348 + 173 = **30,212.364**.

**Expected:** tax 11577 | NI 2809.2012 | health 2264.4348 (input) | allowance 173 | net 30212.364.
To the agora: tax 11577.00 | NI 2809.20 | health 2264.43 | allowance 173.00 | net 30212.36.

### H57: one shekel a month into the 47% bracket

Facts: month 2026-02; salary 46,691 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 560,292 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 73,200 = 22,692
- 35% (s 121(a)(2), line 4352) × 259,080 = 90,678
- 47% (s 121(a)(3), line 4353) × 12 = 5.64
- gross 148,367.64; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 138,929.64
- annual tax 138,929.64; monthly = annual ÷ 12 = **11,577.47**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 38,988 = 2,729.16; total **2,809.2712**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 38,988 = **2,264.4865**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 46,691 − 11,577.47 − 2,809.2712 − 2,264.4865 + 173 = **30,212.7723**.

**Expected:** tax 11577.47 | NI 2809.2712 | health 2264.4865 (input) | allowance 173 | net 30212.7723.
To the agora: tax 11577.47 | NI 2809.27 | health 2264.49 | allowance 173.00 | net 30212.77.

### H58: married woman, 6 children, newborn on 1 November 2026

Facts: month 2026-11; salary 16,000 a month (the same in every month of 2026); earner woman; status married; children born 2026-11-01, 2024-01-15, 2021-06-30, 2019-09-09, 2015-12-31, 2010-10-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- ITO s 36A (line 1597, «בחישוב המס של אשה תובא בחשבון 1/2 נקודת זיכוי»): 1/2
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2026-11-01: year of birth («בשנת לידתו» 2½) -> 2.5 [ITO s 66(c)(4)(a) (line 2466)]
- child born 2024-01-15: turns 2 (same band, 4½) -> 4.5 [ITO s 66(c)(4)(a) (line 2466)]
- child born 2021-06-30: turns 5 (same band, 2½) -> 2.5 [ITO s 66(c)(4)(a) (line 2466)]
- child born 2019-09-09: turns 7 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 2) -> 2 [ITO s 66(c)(4)(a) (line 2466)]
- child born 2015-12-31: turns 11 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 2) -> 2 [ITO s 66(c)(4)(a) (line 2466)]
- child born 2010-10-10: turns 16 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 2) -> 2 [ITO s 66(c)(4)(a) (line 2466)]
- total 18.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 52,998
Tax on annual taxable income 192,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 71,280 = 14,256
- gross 27,792; less credits 52,998; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 8,297 = 580.79; total **660.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 8,297 = **677.7618**; expected = the input.

Child allowance for 2026-11: 2026-11-01: counted (born this month on day 1: «נוצרה זכאות ... עד 15 בחודש פלוני, תשולם הקצבה החל ב־1 באותו חודש», s 72(a), line 854); 2024-01-15: counted; 2021-06-30: counted; 2019-09-09: counted; 2015-12-31: counted; 2010-10-10: counted. 6 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 + 219 + 219 + 173 + 173 = **1,176**.

Net = 16,000 − 0 − 660.9012 − 677.7618 + 1,176 = **15,837.337**.

**Expected:** tax 0 | NI 660.9012 | health 677.7618 (input) | allowance 1176 | net 15837.337.
To the agora: tax 0.00 | NI 660.90 | health 677.76 | allowance 1176.00 | net 15837.34.

### H59: divorced single father, eldest turns 18 on 31 December 2026, December

Facts: month 2026-12; salary 18,000 a month (the same in every month of 2026); earner man; status divorced; children born 2008-12-31, 2013-04-04, 2016-08-08.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- child born 2008-12-31 (turns 18), living with the parent: ITO s 40(b)(1) (line 1633): 0.5
- child born 2013-04-04 (turns 13), living with the parent: ITO s 40(b)(1) (line 1633): 2
- child born 2016-08-08 (turns 10), living with the parent: ITO s 40(b)(1) (line 1633): 2
- ITO s 40(b)(2) (line 1640, «הורים החיים בנפרד יקבל ההורה הזכאי לנקודת זיכוי לפי פסקה (1), נקודת זיכוי אחת נוספת»): 1
- total 7.75 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 22,506
Tax on annual taxable income 216,000 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 95,280 = 19,056
- gross 32,592; less credits 22,506; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 10,086
- annual tax 10,086; monthly = annual ÷ 12 = **840.5**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 10,297 = 720.79; total **800.9012**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 10,297 = **781.1618**; expected = the input.

Child allowance for 2026-12: 2008-12-31: counted (turns 18 this month on day 31: entitlement ends on the birthday, s 65(a) «ולא מלאו לו 18 שנים», line 807, but «תשלום הקצבה יסתיים ביום האחרון של החודש שבו נפסקה הזכאות», s 72(a), line 854); 2013-04-04: counted; 2016-08-08: counted. 3 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 + 219 + 219 = **611**. The child lives with the father only, so is in his count (s 67(b)) and is paid to him (s 69(a), line 837).

Net = 18,000 − 840.5 − 800.9012 − 781.1618 + 611 = **16,188.437**.

**Expected:** tax 840.5 | NI 800.9012 | health 781.1618 (input) | allowance 611 | net 16188.437.
To the agora: tax 840.50 | NI 800.90 | health 781.16 | allowance 611.00 | net 16188.44.

### H60: one shekel a month into the 14% bracket

Facts: month 2026-02; salary 7,011 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 84,132 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 12 = 1.68
- gross 8,413.68; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 0
- annual tax 0; monthly = annual ÷ 12 = **0**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,011 = 72.9144; total **72.9144**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,011 = **226.4553**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 7,011 − 0 − 72.9144 − 226.4553 + 173 = **6,884.6303**.

**Expected:** tax 0 | NI 72.9144 | health 226.4553 (input) | allowance 173 | net 6884.6303.
To the agora: tax 0.00 | NI 72.91 | health 226.46 | allowance 173.00 | net 6884.63.

### H61: one shekel a month into the 20% bracket

Facts: month 2026-02; salary 10,061 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 120,732 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 12 = 2.4
- gross 13,538.4; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 4,100.4
- annual tax 4,100.4; monthly = annual ÷ 12 = **341.7**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 2,358 = 165.06; total **245.1712**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 2,358 = **370.7155**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 10,061 − 341.7 − 245.1712 − 370.7155 + 173 = **9,276.4133**.

**Expected:** tax 341.7 | NI 245.1712 | health 370.7155 (input) | allowance 173 | net 9276.4133.
To the agora: tax 341.70 | NI 245.17 | health 370.72 | allowance 173.00 | net 9276.41.

### H62: one shekel a month into the 31% bracket

Facts: month 2026-02; salary 19,001 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 228,012 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 12 = 3.72
- gross 34,995.72; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 25,557.72
- annual tax 25,557.72; monthly = annual ÷ 12 = **2,129.81**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 11,298 = 790.86; total **870.9712**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 11,298 = **832.9135**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 19,001 − 2,129.81 − 870.9712 − 832.9135 + 173 = **15,340.3053**.

**Expected:** tax 2129.81 | NI 870.9712 | health 832.9135 (input) | allowance 173 | net 15340.3053.
To the agora: tax 2129.81 | NI 870.97 | health 832.91 | allowance 173.00 | net 15340.31.

### H63: one shekel a month into the 35% bracket

Facts: month 2026-02; salary 25,101 a month (the same in every month of 2026); earner man; status married; children born 2018-05-10.

Credit points, tax year 2026:
- ITO s 34 (line 1570, «יובאו בחשבון שתי נקודות זיכוי»): 2
- ITO s 36 (line 1594, «תובא בחשבון 1/4 נקודת זיכוי כזיכוי נסיעה»): 1/4
- separate calculation requested under ITO s 66(c)(1א) (line 2462, «בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד ... לנקודות זיכוי כאמור בפסקאות (4) או (5)»)
- child born 2018-05-10: turns 8 («החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו»: 1) -> 1 [ITO s 66(c)(5)(ג) (lines 2474-2476)]
- total 3.25 points × 2,904 (s 33A, line 1563 note «בשנים 2024–2027, 2,904 ש״ח»; frozen by s 120B(e)(1), line 4344) = 9,438
Tax on annual taxable income 301,212 (salary × 12; personal-exertion rates, s 121(b)(1), as enacted from 1 Jan 2026 by the 5786-2026 Law ch C ss 5-6, SH 3511 p. 416):
- 10% (s 121(b)(1)(א), line 4355) × 84,120 = 8,412
- 14% ((ב), line 4356) × 36,600 = 5,124
- 20% ((ג), line 4357) × 107,280 = 21,456
- 31% ((ד), line 4358) × 73,200 = 22,692
- 35% (s 121(a)(2), line 4352) × 12 = 4.2
- gross 57,688.2; less credits 9,438; floored at 0 (a credit point is «המקוזז כנגד המס», line 1563): 48,250.2
- annual tax 48,250.2; monthly = annual ÷ 12 = **4,020.85**

NI deduction: all branches of s 342(c)(1) (line 3661) are paid: Schedule J column D printed totals (ruling 1): 1.04% on the part up to the reduced collection threshold 7,703 (Amendment 252 s 7(a)(3)(b), SH 3347 pp. 177-178, «"על חלק השכר שאינו עולה על 60% מהשכר הממוצע" ... 1.04»; the words replaced by «מדרגת הגבייה המופחתת» by the 2025 Budget Law s 19(6), SH 3384 p. 396) and 7.00% above it (Sch. J line 4730, «סך הכל» column D: 7.00). 1.04% × 7,703 = 80.1112; 7% × 17,398 = 1,217.86; total **1,297.9712**.

Health deduction: an input (the National Health Insurance Law is not in the bundle; BRIEF «the health insurance contribution (an input)»); supplied at the BTL rates (3.23% up to 7,703, 5.17% above, to 51,910): 3.23% × 7,703 + 5.17% × 17,398 = **1,148.2835**; expected = the input.

Child allowance for 2026-02: 2018-05-10: counted. 1 in the count; s 68(a) (line 821) with the 2026 basic amounts of s 1 para (2) (lines 187-188: 173 for the first and fifth onward, 219 for the second to fourth): 173 = **173**.

Net = 25,101 − 4,020.85 − 1,297.9712 − 1,148.2835 + 173 = **18,806.8953**.

**Expected:** tax 4020.85 | NI 1297.9712 | health 1148.2835 (input) | allowance 173 | net 18806.8953.
To the agora: tax 4020.85 | NI 1297.97 | health 1148.28 | allowance 173.00 | net 18806.90.

Finished 2026-10-08T06:42:48Z (UTC), before any .l4 file was opened.
