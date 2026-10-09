# DECIDED-ANSWERS, IL-27 (independent test author fid-il-27, written 2026-10-09 from the Hebrew alone)

Row: Income Tax Ordinance [new version] ss 35 (olim) with the 5738-1977 rules, 39, 39A, 39B, 40(b), 40A to 40E, 41, 44, 45, 46, 46A, 46B, 47, 47A with the 5740-1980 regulations; Retirement Age Law 5764-2004.
Sources read: income-tax-ordinance-new-version.he.wiki.txt (lines cited as ITO:n), the two regulations files (R5738, R5740), retirement-age-law-5764-2004.he.wiki.txt (RAL).
The encoding directory was NOT opened before this file was frozen (only its file listing was seen by `ls`).

## Conventions and global assumptions

- Tax year = calendar year. Today is 2026-10-09, so the tax year under test is 2026 unless stated.
- Credit point value for 2026 = 2,904 NIS per year (ITO:1563, note "בשנים 2024–2027, 2,904 ש״ח"). Fractions: 1/12 = 242, 1/6 = 484, 1/4 = 726, 1/2 = 1,452, 3/4 = 2,178, 1 = 2,904, 5/4 = 3,630, 3/2 = 4,356, 7/4 = 5,082, 2 = 5,808, 5/2 = 7,260, 7/2 = 10,164, 9/2 = 13,068.
- For tax years 2028 and later no point value is in the sources: answers are given in points and the NIS value is "needs the published figure".
- Events are placed on the 1st of a month so that month counts are unambiguous; partial-month counting is flagged where it matters (see AMB-1).
- The person is an Israeli resident unless stated.
- Confidence: H = the text decides; M = the text decides but a careful reader could differ on a detail; L = a genuine ambiguity or a reading I chose between two.
- "refuse" means: I expect a correct encoding to refuse or to demand the reading be named, because the text does not decide it.

## Ambiguities flagged (the cases that depend on each are marked AMB-n)

- AMB-1: s 35(a) counts in "months" from aliyah (ITO:1574 to 1578) and s 35(c) gives the credit "לפי מספר החדשים שהעולה ישב בישראל באותה שנה" (ITO:1580). The text does not say how a part-month at arrival is counted. I only decide cases with arrival on the 1st of a month.
- AMB-2: s 35 and R5738 r 3 mention 42 months for pre-2022 olim and 54 months for later olim (editorial notes in brackets). R5738 r 3 (1977) says "42 החדשים" with no 54 version. I read r 3 as applying to whichever period (42 or 54) governs the oleh (ITO:1580, R5738 r 3).
- AMB-3: s 39B temporary provision (2026, 2027) (ITO:1621 to 1628) is printed interleaved with the permanent schedule. I cannot tell whether the temporary lines replace paragraphs (1) and (2) for tax years 2026 and 2027 or add to them. Reading T (replace): 2026/2027 schedule is 30 to 39 days = 1/2, 40 to 49 = 3/4, 50+ = 1 plus 1/4 per full 5 extra days beyond 50, cap 4, and below 30 days nothing. Reading P (permanent schedule only): 20+ days = 3/4 plus 1/4 per 5 extra days beyond 20, cap 4. Reading T gives less than P at every point, so T is odd; I still take T as my decided reading (a temporary provision that is printed as a rival sub-paragraph reads as a replacement) at confidence L, and say what P gives.
- AMB-4: s 40B "מלאו לו או לבן־זוגו 16 שנים אך לא 18 שנים" (ITO:1651): the text does not say at what moment age is tested. I decide by age at the end of the tax year (31 December): 16 or 17 qualifies; 18 does not; 15 does not. Alternative: a person who is 17 for part of the year and turns 18 inside the year also qualifies.
- AMB-5: R5740 r 1 defines the deduction ceiling as the product of "השיעורים הקבועים כניכוי בסעיפים 47(ב)(1) או 47(ב)(2)" and the qualifying-income ceiling. s 47(b)(1) fixes 7% (plus up to 4% extra); s 47(b)(2) fixes 5%. Reading A: ceiling (1) = 11% (7% + 4%) of the cap, ceiling (2) = 5% of the cap. Reading B: ceiling (1) = 7% of the cap. I decide A at confidence L. Cases whose answer is the same under both readings are marked "A=B".
- AMB-6: s 47(b1)(2) "12% מהכנסתו הנוספת" (ITO:1779): whether the 12% test is applied to the sums paid or to the sums not already deducted under (1). Cases avoiding the 12% trigger are decided.
- AMB-7: s 44 and s 45 income ceilings (188,000 single / 301,000 couple, 2024 to 2027) come from the editorial note (ITO:1705, 1713). Whether the ceiling is inclusive is not stated; "תקרת ההכנסה המזכה" suggests income equal to the ceiling still qualifies. I decide inclusive at M.
- AMB-8: s 46A caps the total of the s 46 credit-base and the s 20A deduction at 50% of taxable income, but does not say which is cut first when the total exceeds the cap (ITO:1754). Over-cap cases: refuse.
- AMB-9: s 37 "הגיע לגיל פרישה" (ITO:1600) is silent on whether the age must be reached by the start of the tax year, at any time in it, or by its end. I decide "reached in or before the tax year" at M.
- AMB-10: s 40C(d)(1) third degree in medicine: "נקודת זיכוי אחת, בשלוש שנות מס, ומחצית נקודת זיכוי, בשתי שנות מס" (ITO:1662): whether the two run concurrently or one after the other. I decide concurrently from the year after completion (1.5 points in the first two years, 1 point in the third) at L.
- AMB-11: s 41(2) refers to "נקודות הזיכוי לפי סעיף 66" and s 66 mixes points of several sections; only s 41(1) is decided numerically.
- AMB-12: s 40(b)(1b) and (2) interplay in a single-parent family where the other parent also claims; only simple cases decided.

## A. Section 35, olim (new schedule, aliyah in 2022 or later) — ITO:1572 to 1584

Schedule (ITO:1574 to 1578): months 1 to 12 at 1/12 point each; months 13 to 30 at 1/4; months 31 to 42 at 1/6; months 43 to 54 at 1/12. Total 8.5 points.
Pre-2022 schedule: months 1 to 18 at 1/4; 19 to 30 at 1/6; 31 to 42 at 1/12. Total 7.5 points.
Credit for a tax year = sum over the months of that year that fall in the 54-month period (ITO:1580).

- A01 Aliyah 1 July 2026, tax year 2026: months 1 to 6 at 1/12 = 0.5 point = 1,452 NIS. (H)
- A02 Same oleh, tax year 2027: months 7 to 12 at 1/12 (0.5) plus months 13 to 18 at 1/4 (1.5) = 2.0 points = 5,808 NIS. (H)
- A03 Same oleh, tax year 2028: months 19 to 30 at 1/4 = 3.0 points; NIS needs the published figure. (H)
- A04 Same oleh, tax year 2029: months 31 to 42 at 1/6 = 2.0 points; NIS needs the published figure. (H)
- A05 Same oleh, tax year 2030: months 43 to 54 at 1/12 = 1.0 point; NIS needs the published figure. (H)
- A06 Same oleh, tax year 2031: the 54 months ended in December 2030 = 0 points. (H)
- A07 Aliyah 1 January 2026, tax year 2026: months 1 to 12 at 1/12 = 1.0 = 2,904 NIS. (H)
- A08 Aliyah 1 January 2025, tax year 2026: months 13 to 24 at 1/4 = 3.0 = 8,712 NIS. (H)
- A09 Aliyah 1 January 2024, tax year 2026: months 25 to 36: 25 to 30 at 1/4 (1.5) plus 31 to 36 at 1/6 (1.0) = 2.5 = 7,260 NIS. (H)
- A10 Aliyah 1 January 2023, tax year 2026: months 37 to 48: 37 to 42 at 1/6 (1.0) plus 43 to 48 at 1/12 (0.5) = 1.5 = 4,356 NIS. (H)
- A11 Aliyah 1 July 2022, tax year 2026: months 43 to 54 at 1/12 = 1.0 = 2,904 NIS. (H)
- A12 Aliyah 1 January 2022, tax year 2026: months 49 to 54 (January to June 2026) at 1/12 = 0.5 = 1,452 NIS; July to December are month 55 onward = 0. (H)
- A13 Aliyah 1 December 2021 (the pre-2022 schedule applies, 42 months, ended May 2025), tax year 2026 = 0. (H) Boundary against A12: one month earlier gives zero.
- A14 Aliyah 1 December 2025, tax year 2026: month 1 is December 2025; 2026 holds months 2 to 13: eleven at 1/12 (11 x 242 = 2,662) plus month 13 at 1/4 (726) = 3,388 NIS = 1.1667 points. (H)
- A15 Aliyah 1 July 2024, tax year 2026: months 19 to 30 at 1/4 = 3.0 = 8,712 NIS. (H)
- A16 Aliyah 1 July 2023, tax year 2026: months 31 to 42 at 1/6 = 2.0 = 5,808 NIS. (H)
- A17 Pre-2022 oleh, aliyah 1 July 2021, tax year 2022: months 7 to 18 at 1/4 = 3.0 points. (H)
- A18 Same pre-2022 oleh, tax year 2023: months 19 to 30 at 1/6 = 2.0 points. (H)
- A19 Same pre-2022 oleh, tax year 2024: months 31 to 42 at 1/12 = 1.0 point. (H)
- A20 Same pre-2022 oleh, tax year 2025: the 42 months ended in December 2024 = 0 points. (H)

## B. Section 35(b), (c), (d), (e) and the 5738-1977 rules — ITO:1579 to 1587, R5738

- B01 Absence exclusion: oleh 1 January 2024, abroad 1 January 2025 to 30 June 2025 (six months, continuous), requests exclusion: the six months are not counted; July 2025 is month 13; tax year 2026 = months 19 to 30 at 1/4 = 3.0 points = 8,712 NIS. (H) Without the exclusion A09 gives 2.5.
- B02 Same but absent five months (1 January to 31 May 2025): below the six-month floor, no exclusion; tax year 2026 = 2.5 = 7,260 NIS (A09). (H)
- B03 Absent exactly three years (1 January 2025 to 31 December 2027), request made, tax year 2028: the absence "אינה עולה על שלוש שנים" so it is excludable; months in Israel before absence = 12 (2024); January 2028 is month 13; tax year 2028 = months 13 to 24 at 1/4 = 3.0 points. (M: whether a period of exactly three years is "not exceeding" — the text says "איננה עולה", so equal qualifies.)
- B04 Absent three years and one month, request made: not excludable (over three years), months stay counted. (H)
- B05 Absent seven months but no request made: the period is counted; no exclusion. (H) ("לפי בקשתו")
- B06 Credit only for months he lived in Israel in the year: aliyah 1 January 2026, resident in Israel nine months (left 1 October 2026): 9 x 1/12 = 0.75 = 2,178 NIS. (M, AMB-1)
- B07 "First time only": a person who was an oleh and received the credits, left, and returned as an oleh a second time receives no new credit run. (H) ("ולא יינתן אלא בפעם הראשונה שנעשה לעולה")
- B08 R5738 r 3: an oleh who immigrated 1 July 2026 and does regular service under the Security Service Law from 1 August 2026 for 24 months, on request: the service months are not counted in the 54; tax year 2026 counts only July (month 1) = 1/12 = 242 NIS. (L, AMB-2: the rule speaks of 42 months; whether the exclusion works for the 54-month period and whether credit is given in the excluded months is not stated.)
- B09 R5738 r 3: post-secondary study months excluded the same way; no request made: nothing excluded. (M)
- B10 R5738 r 2(1): a person who was an oleh before 31 March 1977, stayed in Israel one and a half years in all, and got neither the s 9(16) exemption nor s 35 points for that income, is treated as an oleh. (H)
- B11 R5738 r 2(1): same person who stayed exactly two years in all: still treated as oleh ("שלא עלו ביחד על שנתיים"). (H)
- B12 R5738 r 2(1): stayed two years and one day: not treated as oleh. (H)
- B13 R5738 r 2(1): stayed one year but already received the s 9(16) exemption: not treated as oleh. (H)
- B14 R5738 r 2(2): an oleh who left Israel as a minor (aged 17) before 31 March 1977 and returned after five years exactly: treated as oleh. (H) ("שאיננה פחותה מחמש שנים")
- B15 R5738 r 2(2): returned after four years eleven months: not. (H)
- B16 R5738 r 2(3): left as a minor (age 17, "קטין" = under 18, r 1) and came back after six years: treated as oleh; left aged 18: not a minor, not treated as oleh. (H)
- B17 Definition of oleh, "תושב חוזר": returned to residence on 16 May 2010 after six consecutive years as a non-resident: is an oleh. (H)
- B18 Returned on 15 May 2010 (one day before the window): not a returning resident under the definition. (H)
- B19 Returned on 30 September 2012: is. (H) Returned on 1 October 2012: not. (H)
- B20 Returned 1 January 2011 after only five years eleven months abroad: not, unless holding the immigration-ministry certificate of six years or more abroad, in which case treated as six years. (H)
- B21 Oleh whose Israeli citizenship was cancelled under s 10(d) of the Citizenship Law: excluded from "oleh". (H)
- B22 s 35(b): registered spouse whose unregistered spouse is an oleh with income of 14,520 NIS (5 x 2,904 for one point): the oleh spouse's income is left out of the registered spouse's taxable income and the registered spouse gets no oleh points. (L: "פי חמישה מסכום נקודות הזיכוי" read as five times the NIS value of the points.) 14,521 NIS: included. (L)

## C. Section 39, helping spouse — ITO:1606 to 1607

- C01 Resident, spouse helped at least 24 hours in every week for nine months of the year in his business, no pension point under s 40(a): 1.5 points = 4,356 NIS. (H)
- C02 Same, but entitled to a pension point under s 40(a): 1.75 points = 5,082 NIS. (H)
- C03 Helped 24 hours every week for ten months: 1.5 points. (H)
- C04 Helped 24 hours every week for eight months: 0. (H)
- C05 Helped 23 hours a week for nine months: 0. (H)
- C06 Helped 24 hours a week, but the help was to earn income from employment (not business/profession): 0. (H)
- C07 Help given by spouse in a rental (passive) income: 0. (H)
- C08 "Yachid muetav" (s 37) and all s 39 conditions met: add the s 37 point, 1.5 + 1 = 2.5 points = 7,260 NIS. (M, AMB-9)
- C09 Entitled to both s 38 and s 39: only one section's credit, at the taxpayer's election. (H)
- C10 Non-resident: 0. (H)

## D. Section 39A, discharged soldier — ITO:1609 to 1617

Credit per month for the first 36 months after the month in which regular service ended: 1/6 point if service was 23 full months or more (man) or 22 full months or more (woman); 1/12 point otherwise. Credit is against tax on income from personal effort.

- D01 Man, 23 full months, service ended 15 July 2025: the 36 months run August 2025 to July 2028; tax year 2026 = 12 x 1/6 = 2.0 points = 5,808 NIS. (H)
- D02 Same man, tax year 2025: August to December = 5 x 1/6 = 0.8333 points = 2,420 NIS. (H)
- D03 Same man, tax year 2028: January to July = 7 x 1/6 = 1.1667 points; NIS needs the published figure. (H)
- D04 Same man, tax year 2029: 0. (H)
- D05 Man, 22 full months of service, ended 15 July 2025, tax year 2026: below 23, so 12 x 1/12 = 1.0 = 2,904 NIS. (H)
- D06 Woman, 22 full months: 1/6 rate, tax year 2026 (same dates) = 2.0 = 5,808 NIS. (H)
- D07 Woman, 21 full months: 1/12 rate = 1.0 = 2,904 NIS. (H)
- D08 Woman 22 months 29 days: counts 22 full months: 1/6 rate. (H)
- D09 Man 22 months 29 days: 22 full months, under 23: 1/12 rate. (H)
- D10 Service ended 31 December 2023: window January 2024 to December 2026; tax year 2026 = 12 months at 1/6 (man, 24 months service) = 2.0 = 5,808 NIS. (H)
- D11 Service ended 30 January 2023: window February 2023 to January 2026; tax year 2026 = 1 month at 1/6 = 484 NIS. (H)
- D12 Service ended 31 January 2023 (same month): window is the same as D11. (H)
- D13 Service ended 30 December 2022: window January 2023 to December 2025; tax year 2026 = 0. (H)
- D14 Only unearned (passive) income in 2026: credit has no personal-effort tax to offset: 0 effective. (M: "בחישוב המס על הכנסתו מיגיעה אישית")
- D15 Man with 36 months of service (a long regular service): the 1/6 rate (23 months or more has no upper bound). (H)

## E. Section 39B, combat reservist — ITO:1619 to 1629

The credit for tax year Y depends on combat reserve days in year Y-1. Commencement date of the section is not in the file: tax years before 2026 are "needs the commencement date".

Permanent schedule, tax year 2028 and later (service in 2027 or later) and, under reading P, 2026 and 2027:
points = 3/4 at 20 days plus 1/4 per full 5 further days, cap 4.

- E01 Tax year 2028, 19 days: 0. (H)
- E02 Tax year 2028, 20 days: 0.75 point. (H)
- E03 Tax year 2028, 24 days: 0.75 (only 4 further days). (H)
- E04 Tax year 2028, 25 days: 1.0. (H)
- E05 Tax year 2028, 29 days: 1.0. (H)
- E06 Tax year 2028, 30 days: 1.25. (H)
- E07 Tax year 2028, 40 days: 0.75 + 4 x 0.25 = 1.75. (H)
- E08 Tax year 2028, 84 days: 0.75 + 12 x 0.25 = 3.75. (H)
- E09 Tax year 2028, 85 days: 0.75 + 13 x 0.25 = 4.0 (cap reached). (H)
- E10 Tax year 2028, 120 days: 4.0 (capped). (H)
- E11 Tax year 2026 (service in 2025), 19 days: 0 under both readings. (H)
- E12 Tax year 2026, 29 days: reading T: 0; reading P: 1.0. Refuse (AMB-3), my reading T = 0. (L)
- E13 Tax year 2026, 30 days: T: 0.5 point = 1,452 NIS; P: 1.25. Refuse (AMB-3). (L)
- E14 Tax year 2026, 39 days: T: 0.5 = 1,452 NIS; P: 0.75 + 3 x 0.25 = 1.5. Refuse (AMB-3). (L)
- E15 Tax year 2026, 40 days: T: 0.75 = 2,178 NIS; P: 1.75. Refuse (AMB-3). (L)
- E16 Tax year 2026, 49 days: T: 0.75 = 2,178 NIS; P: 0.75 + 5 x 0.25 = 2.0. Refuse (AMB-3). (L)
- E17 Tax year 2026, 50 days: T: 1.0 = 2,904 NIS; P: 0.75 + 6 x 0.25 = 2.25. Refuse (AMB-3). (L)
- E18 Tax year 2027, 54 days: T: 1.0 (4 days beyond 50 are under a block of 5); P: 0.75 + 6 x 0.25 = 2.25. Refuse (AMB-3). (L)
- E19 Tax year 2027, 55 days: T: 1.25; P: 2.5. Refuse (AMB-3). (L)
- E20 Tax year 2027, 200 days: T: 4.0 (cap); P: 4.0 (cap). Same under both readings: 4.0 points = 11,616 NIS. (H, A=B)
- E21 "Combat" and "reserve service" are defined by reference to military law and the Reserve Service Law, so a service day is a day of reserve service as a fighter; non-combat reserve days do not count. (H)

## F. Sections 40(b), 40A, 40B, 40C, 40D, 40E (40ה)

### F1. Section 40(b), single-parent family child points — ITO:1633 to 1646

Mother (para (1)) for tax year Y and child born in year B (and the child not yet 19 in the tax year, support on the parent, child with the parent, parent not entitled to the s 37 point):
Y = B: 2.5; Y = B+1 or B+2: 4.5; Y = B+3: 3.5; Y = B+4 or B+5: 2.5; Y = B+6 up to B+17: 2.0; Y = B+18 ("שנת בגרות"): 0.5; Y >= B+19: 0.
Father (para (1a)): Y = B: 2.5; B+1, B+2: 4.5; B+3: 3.5; B+4, B+5: 2.5; B+6 up to B+17: 1.0; Y = B+18: nothing in (1a).

- F01 Mother, single-parent family, child born 2026, tax year 2026: 2.5 = 7,260 NIS. (H)
- F02 Child born 2025, tax year 2026: 4.5 = 13,068 NIS. (H)
- F03 Child born 2024, tax year 2026: 4.5 (turns two in 2026) = 13,068 NIS. (H)
- F04 Child born 2023, tax year 2026 (turns three): 3.5 = 10,164 NIS. (H)
- F05 Child born 2022, tax year 2026 (turns four): 2.5 = 7,260 NIS. (H)
- F06 Child born 2021, tax year 2026 (turns five): 2.5 = 7,260 NIS. (H)
- F07 Child born 2020, tax year 2026 (turns six): 2.0 = 5,808 NIS. (H)
- F08 Child born 2009, tax year 2026 (turns 17): 2.0 = 5,808 NIS. (H)
- F09 Child born 2008, tax year 2026 (turns 18, the year of majority): 0.5 = 1,452 NIS. (H)
- F10 Child born 2007, tax year 2026 (turns 19): 0. (H)
- F11 Father (para (1a)), child born 2020, tax year 2026: 1.0 = 2,904 NIS. (H)
- F12 Father, child born 2008, tax year 2026 (year of majority): 0; para (1a) has no majority-year point. (H)
- F13 Father, child born 2025, tax year 2026: 4.5 = 13,068 NIS. (H)
- F14 Mother entitled to the s 37 point: no (1) points at all. (H) ("אך אינו זכאי לנקודת זיכוי לפי סעיף 37")
- F15 Mother may elect to carry one point of the birth-year 2.5 into the following year (para (1a1)): child born 2026: 2026 = 1.5, 2027 = 4.5 + 1 = 5.5. (M)
- F16 Child who is "ילד להורה אחד" (other parent died in the year or earlier, or not recorded): para (1b): the parent gets one extra point: child born 2020, tax year 2026, the parent otherwise entitled to (1) (mother): 2.0 + 1 = 3.0 = 8,712 NIS. (M, AMB-12)
- F17 Parents living apart: the parent entitled under (1) gets one more point; if care is shared, the other parent gets one point or a share by expenses: child born 2020, parent entitled under (1) = 2 + 1 = 3 points. (M, AMB-12)

### F2. Section 40A — ITO:1648 to 1649

One point for a divorced person who, or whose spouse, pays alimony to a former spouse and who is married to a different spouse.

- F18 Divorced, pays alimony to ex-wife, remarried: 1 point = 2,904 NIS. (H)
- F19 Divorced, pays alimony, not remarried: 0. (H)
- F20 Divorced, remarried, but nobody in the household pays alimony: 0. (H)
- F21 Divorced person whose new spouse pays alimony to the new spouse's former spouse: 1 point (the text says "הוא או בן־זוגו"). (H)

### F3. Section 40B — ITO:1651 to 1652

One point if the person or the spouse has completed 16 years but not 18 (AMB-4: tested at year end).

- F22 Taxpayer aged 17 at 31 December 2026 (born 2009): 1 point = 2,904 NIS. (H)
- F23 Taxpayer aged 16 at year end (born 2010): 1 point. (H)
- F24 Taxpayer aged 15 at year end (born 2011): 0. (H)
- F25 Taxpayer aged 18 at year end (born 2008): 0 at year-end reading; alternative reading gives 1. Refuse or name reading (AMB-4). (L)
- F26 Spouse aged 17 at year end, taxpayer adult: 1 point. (H)

### F4. Section 40C, academic degrees — ITO:1654 to 1672

Rules for those who finished studies in 2023 or later: first degree 1 point, second degree 1/2 point, third degree (medicine or dentistry) 1 point for three tax years and 1/2 for two tax years, each degree for as many tax years as its academic study years, at most three for the first and two for the second, starting in the tax year after the year in which studies ended, on proof of completion and entitlement to the degree.
Rules for those who finished in the period from 2014 to 2022: one point (or half) in a single tax year only, the year after or the year after that, at the person's choice.

- F27 First degree, three study years, finished 2025: 1 point in each of 2026, 2027, 2028; tax year 2026 = 2,904 NIS. (H)
- F28 First degree, three study years, finished 2025, tax year 2029: 0. (H)
- F29 First degree, four study years (more than three), finished 2025: capped at three tax years: 2028 = 1 point; 2029 = 0. (H)
- F30 First degree, two study years, finished 2025: two tax years only: 2026 and 2027 = 1 point; 2028 = 0. (H)
- F31 Second degree, two study years, finished 2025: 1/2 point in 2026 and 2027; tax year 2026 = 1,452 NIS. (H)
- F32 Second degree, three study years, finished 2025: capped at two tax years: 2028 = 0. (H)
- F33 First degree finished in 2026: credit starts 2027; tax year 2026 = 0. (H)
- F34 First degree finished in 2023: credit years 2024, 2025, 2026 (three-year study); tax year 2026 = 1 point = 2,904 NIS. (H)
- F35 First degree finished in 2022 (old rule, one year only, taken in 2023 or 2024): tax year 2026 = 0. (H)
- F36 Boundary: finished 2022 gets one year only; finished 2023 gets the multi-year rule (F34). (H)
- F37 No certificate of completion provided to the assessing officer: 0. (H)
- F38 Both a first degree (finished 2023: credit 2024 to 2026) and a second degree (finished 2025: credit 2026, 2027): tax year 2026 = 1 + 0.5 = 1.5 points = 4,356 NIS (the text does not forbid cumulating the two). (M)
- F39 A second first degree (a person who already used 40C for a first degree and now studies a second first-degree): "לתואר אקדמי ראשון אחד או לתואר אקדמי שני אחד, בלבד": no second credit. (H)
- F40 Third degree in medicine or dentistry, finished 2025, concurrently reading: tax year 2026 = 1 + 0.5 = 1.5 points; 2027 = 1.5; 2028 = 1.0; 2029 = 0. (L, AMB-10)
- F41 Direct track to a third degree, first-degree portion three years finished 2023 and third degree finished 2025: 1 point 2024 to 2026 (first-degree part) and 1/2 for two years from 2026: tax year 2026 = 1.5. (L)
- F42 Degree in a profession requiring an internship: the person may choose to start the credit in the year after the end of the internship instead (para (g1)); chose the internship route, internship started 2026: credit starts the year after the internship ends. (M)
- F43 Degree from a body that is not a recognised institution of higher education: 0. (H)

### F5. Section 40D, vocational studies — ITO:1673 to 1681

One point if studies were at least 1,700 study hours (higher-education-equivalent hours) and he is entitled to a recognised certificate (recognised by a government ministry); for as many tax years as study years, at most three, starting the tax year after studies ended (finished 2023 or later; finished 2018 to 2022: one tax year only).

- F44 Study of exactly 1,700 hours, three years, finished 2025: 1 point in 2026, 2027, 2028; tax year 2026 = 2,904 NIS. (H)
- F45 Study of 1,699 hours: not "לימודי מקצוע": 0. (H)
- F46 One-year course of 1,700 hours finished 2025: 1 point in 2026 only; 2027 = 0. (H)
- F47 Finished 2022: one tax year only (2023 or 2024); tax year 2026 = 0. (H)
- F48 Finished 2018: one tax year only. (H) Finished 2017: not in the 2018 to 2022 window text; treated by the general rule (current text) = needs the pre-2018 text. (L)
- F49 Certificate not recognised by a government ministry: 0. (H)
- F50 Four-year vocational study: cap of three tax years. (H)
- F51 No proof given to the assessing officer: 0. (H)

### F6. Section 40E (the file's 40ה), no double credit — ITO:1683

- F52 A person who qualifies under both 40C and 40D chooses either the 40C amount or the 40D point: not both. Qualifying for a first degree (1 point) and a vocational certificate (1 point) in 2026: 1 point = 2,904 NIS, not 2. (H)
- F53 Qualifying under 40C for a second degree (0.5) and 40D (1): elects the larger, 1 point; or may elect the 0.5; never 1.5. (H)
- F54 Section 40F: repealed ("פקע"): 0 in all cases. (H) (ITO:1686)

## G. Section 41, spouse married for part of the year — ITO:1689 to 1692

For months when not married: 1/12 of the points under ss 34, 36, 40(b) and 40B per month; for months when married: 1/12 of the points under s 66 per month. Applies to a non-registered spouse.

- G01 Not married for 4 months (married 8), points: s 34 = 2, s 36 = 1/4: (2 + 0.25) x 4/12 = 0.75 points = 2,178 NIS for the unmarried period. (H)
- G02 Not married for 12 months (married for 0): full year: 2.25 points (and s 41 not engaged). (M)
- G03 Not married for 1 month: 2.25 / 12 = 0.1875 = 544.5 NIS. (H)
- G04 Not married 6 months and the person is 17 (s 40B 1 point): (2 + 0.25 + 1) x 6/12 = 1.625 points = 4,719 NIS. (M, AMB-4)
- G05 Not married 6 months with a single-parent child under s 40(b) child born 2020 (2 points): (2 + 0.25 + 2) x 6/12 = 2.125 points = 6,171 NIS. (M)
- G06 Section 36A (woman 1/2 point) is not in the list of sections prorated by 41(1): a woman not married for 6 months does not receive 36A's 1/2 point through s 41(1). (M)
- G07 The registered spouse (בן זוג רשום) is not covered by s 41: 0 under s 41. (H)
- G08 s 41(2) months married times 1/12 of the s 66 points: depends on which s 66 points apply. Refuse. (L, AMB-11)

## H. Sections 44 and 45 — ITO:1703 to 1712

s 44: resident taxpayer who, or whose spouse, paid in the year for keeping in a special institution a child, spouse or parent who is totally paralysed, bedridden for good, blind or of unsound mind, or a child with an intellectual-developmental disability: credit = 35% of the part of the amounts paid exceeding 12.5% of taxable income. Income ceilings per the note: 188,000 NIS single, 301,000 NIS couple (2024 to 2027).

- H01 Income 80,000, paid 20,000: threshold 10,000; excess 10,000; credit 3,500 NIS. (H)
- H02 Income 80,000, paid 10,000: excess 0; credit 0. (H)
- H03 Income 80,000, paid 10,001: credit 35% x 1 = 0.35 NIS. (H)
- H04 Income 100,000, paid 12,500: 0. (H)
- H05 Income 100,000, paid 50,000: excess 37,500; credit 13,125 NIS. (H)
- H06 Single taxpayer income 188,000, paid 60,000: threshold 23,500; excess 36,500; credit 12,775 NIS (ceiling reached but not exceeded). (M, AMB-7)
- H07 Single taxpayer income 188,001: over the ceiling: 0. (M, AMB-7)
- H08 Couple with joint income 250,000, paid 60,000: couple ceiling 301,000: qualifies; threshold 31,250; excess 28,750; credit 10,062.5 NIS. (M, AMB-7)
- H09 Couple income 301,001: 0. (M)
- H10 Same income 250,000, single person: over 188,000 ceiling: 0. (M)
- H11 Payment to keep a sibling in an institution: not a child, spouse or parent: 0. (H)
- H12 Payment for the institution of a parent who is only elderly, not paralysed, bedridden, blind or of unsound mind: 0. (H)
- H13 Payment made by the spouse counts ("הוא או בן זוגו"). (H)
- H14 Payment to a home care at the person's own home, not a special institution: 0. (M)
- H15 s 45: one blind child, no s 44 credit for the child: 2 points = 5,808 NIS. (H)
- H16 s 45: two disabled children (one paralysed, one with intellectual-developmental disability): 4 points = 11,616 NIS. (H)
- H17 s 45: child for whom the taxpayer received a s 44 credit: 0 for that child. (H) ("רק אם לא קיבל זיכוי ממס עבור אותו ילד על פי סעיף 44")
- H18 s 45: two children, one with a s 44 credit and one without: 2 points. (H)
- H19 s 45: the child of the spouse counts ("או שהיה לבן זוגו ילד כאמור"); points brought into the account of the taxpayer or the spouse. (H)
- H20 s 45: disabled adult relative (not a child): 0. (H)
- H21 s 45: non-resident taxpayer: 0. (H)
- H22 s 45: a child with deafness only: not in the list (paralysed, blind, intellectual-developmental): 0. (M)
- H23 s 45(b) repealed: no extra points beyond para (a). (H)

## I. Sections 46, 46A, 46B — ITO:1744 to 1761

s 46: donation in the year exceeding 207 NIS (2024 to 2027) to a national fund or an approved public institution: credit 35% of the donation for an individual; total donations credited in a year capped at the lower of 30% of taxable income and 10,354,816 NIS; the excess is carried forward and credited in the next three tax years in order, subject to the same cap each year.

- I01 Donation 207 NIS: does not exceed 207: 0. (H)
- I02 Donation 208 NIS: credit 35% x 208 = 72.80 NIS. (H)
- I03 Income 100,000, donation 20,000: cap 30,000; credit 7,000 NIS. (H)
- I04 Income 100,000, donation 30,000: credit 10,500 NIS. (H)
- I05 Income 100,000, donation 40,000: base capped at 30,000; credit 10,500; 10,000 carried forward to 2027 to 2029. (H)
- I06 Following year (2027) with taxable income 100,000 and no new donation: carried 10,000 credited at 35% = 3,500 NIS. (H)
- I07 Income 100,000 with a new 2027 donation of 25,000 and carried 10,000: total 35,000 vs cap 30,000: cap applied to total; the order of use is not stated in the part read. Refuse. (L)
- I08 Income 50,000,000, donation 40,000,000: cap = lower of 15,000,000 and 10,354,816 = 10,354,816; credit 35% x 10,354,816 = 3,624,185.60 NIS. (H)
- I09 Donation to a body not designated by the Minister: 0. (H)
- I10 Donation to a "national fund" named in para (c) (Jewish Agency, World Zionist Organisation, United Israel Appeal, Jewish National Fund): qualifies. (H)
- I11 Donation of exactly 207 in total over several donations: sum is the test: 207 total = no. (M)
- I12 Donation by a company: rate under s 126(a), not 35%. Refuse (company rate not in this file). (H)
- I13 s 46A: donation credit base 30,000 plus a s 20A R&D deduction of 20,000 against taxable income (before the R&D deduction) 100,000: total 50,000 = 50%: allowed. (H)
- I14 s 46A: total 50,001 against 100,000: exceeds the cap; the text does not say which is cut. Refuse. (L, AMB-8)
- I15 s 46B: tax assessed after a donation credit of 10,500 is 49,500: the advance-payments base is 49,500 + 10,500 = 60,000. (H)
- I16 Memorial note: a family member of a soldier who fell is credited 30% of memorial expenses (year 1971 onward) per the editorial note: expenses 10,000: credit 3,000 NIS. (L: it is a note on the text, not a section; family member list: spouse, son, grandson, brother, parent, brother-in-law, son-in-law.)
- I17 46(d): a public institution whose books were found inadmissible: the Director may cancel its designation from that day: donations to it afterwards not credited. (M)
- I18 46(a1): an institution that did not file two consecutive annual reports may have its designation cancelled by the Minister: until cancelled, donations qualify. (M)

## J. Sections 47 and 47A with R5740

2026 figures (ITO:1766 to 1771): qualifying income cap, employment income only: 116,400; no employment income: 164,400; "עמית מוטב" threshold 26,436 NIS paid into a pension fund in the year (16% of the average wage 13,769 x 12; AMB: exact figure 26,436.48 and note prints 26,436).

- J01 Self-employed, income 100,000, only a pension fund payment of 7,000: deduction min(7,000, 7% of 100,000 = 7,000) = 7,000. (H)
- J02 Same income, payment 10,000: deduction limited to 7% = 7,000. (H)
- J03 Same income, payment 12,000 (exactly 12%): deduction 7,000 (extra only for the part above 12%). (H)
- J04 Self-employed income 150,000, payment 20,000: 7% = 10,500; 12% = 18,000; excess 2,000 below 4% (6,000): deduction 10,500 + 2,000 = 12,500. (H)
- J05 Self-employed income 150,000, payment 25,000: 10,500 + min(7,000, 6,000) = 16,500. (H)
- J06 Self-employed income 200,000: the qualifying income is capped at 164,400; payment 15,000: 7% x 164,400 = 11,508 (a payment of 15,000 is under 12% of 164,400 = 19,728): deduction 11,508. (H)
- J07 Employee, no pension from the employer, salary 100,000, payment 6,000: lower of 5% x 100,000 = 5,000 and 5% x salary up to 291,000 less insured income (0) = 5,000: deduction 5,000. (H)
- J08 Same, payment 4,000: deduction 4,000. (H)
- J09 Employee salary 130,000, no insured income, payment 6,000: (a) 5% of qualifying income capped at 116,400 = 5,820; (b) 5% x (130,000 - 0) = 6,500; lower = 5,820; deduction 5,820. (H)
- J10 Employee with insured income (employer pays to a pension fund) of 100,000 and no other income: (a) 0 (all income is insured); deduction 0. (H)
- J11 Taxpayer who is an "עמית מוטב" (paid 26,436 or more), self-employed income 200,000: income for independent member = min(200,000, 116,400) - insured income 0 = 116,400; 11% = 12,804; payment 26,436: first limb deduction 12,804 (the (b1)(1) amount). (M)
- J12 Same payer as J11 but payment 26,435 (one below): not an "עמית מוטב" (needs not less than 16% of average wage); deduction under (b) only. (M, rounding)
- J13 Payment exactly 26,436: "שלא פחת מ־16%": qualifies as עמית מוטב on the printed figure. (M)
- J14 (b2): amounts deducted under (b) cannot be deducted again under (b1) and vice versa. (H)
- J15 (c): a sum deducted under (b) or (b1) is not counted for s 45A. (H)
- J16 R5740 r 2(a)(1): age 50 on 1 January 2026 (born on or before 1 January 1976), non-employment income 100,000, payment 10,000: deduction 10,000 (up to 10.5% = 10,500). A=B. (H)
- J17 R5740 r 2(a)(1): same, payment 12,000: deduction 10,500. A=B (ceiling is at least 11,508). (H)
- J18 Age 49 on 1 January 2026 (born 2 January 1976), same facts, payment 12,000: s 47(b)(1) rate 7% = 7,000. (H)
- J19 Born exactly 1 January 1976: aged 50 at the start of the year: enlarged rate applies. (H)
- J20 R5740 r 2(a)(2): age 50, income 100,000, pension only, payment 20,000: first 10,500; payment exceeds 10.5% + 5% = 15,500 by 4,500; extra up to 6% (6,000): extra 4,500; total 15,000; ceiling A = 11% x 164,400 = 18,084 (not binding): 15,000; under B the ceiling 7% x 164,400 = 11,508 binds: 11,508. Refuse (AMB-5); my reading A = 15,000. (L)
- J21 R5740 r 2(b): age 50 employee, salary 70,000 uninsured, payment 6,000: 7.5% x 70,000 = 5,250; ceiling 5% x 116,400 = 5,820; deduction min(6,000, 5,250, 5,820) = 5,250. A=B. (H)
- J22 R5740 r 2(b): age 50 employee, salary 116,400, payment 9,000: 7.5% x 116,400 = 8,730; ceiling 5,820: deduction 5,820. A=B. (H)
- J23 R5740 r 2(b): age 50 employee salary 77,600: 7.5% = 5,820 equals ceiling; payment 5,820: deduction 5,820. (H)
- J24 s 47A(a): self-employed paid 10,000 national insurance on non-employment income, taxable income before deduction 80,000: deduction 52% = 5,200. (H)
- J25 s 47A(a): paid 10,000, taxable income before the deduction only 3,000: deduction limited to 3,000. (H)
- J26 s 47A(a): supplement under s 179(a) of the NI law is excluded: paid 10,000 including a 500 supplement: base 9,500; deduction 4,940. (H)
- J27 s 47A(b): employee whose employer is not required to pay NI and who pays it himself on employment income: same 52%: paid 10,000: 5,200. (H)
- J28 s 47A(b1) (from 2025): paid 10,000 in 2026 and received a refund of 2,000 for a prior year's overpayment: deduction 52% x 8,000 = 4,160. (H)
- J29 s 47A(b1): refund 12,000 against payments 10,000: no deduction; 52% of the 2,000 difference (1,040) is treated as business income when received. (H)
- J30 s 47A(b1): refund of 2,000 including a supplement of 100: "סכום ההחזר" excludes the supplement: refund counted 1,900: paid 10,000: 52% x 8,100 = 4,212. (H)
- J31 s 47A(c): 52% of medical-insurance payments (not dental) to a body fixed by the Minister, up to the parallel-tax that would have applied: needs the Minister's list and the parallel-tax rates (parallel tax was repealed): refuse. (L)
- J32 s 47A(d): parallel-tax deduction only for the period ending 31 December 1996: a parallel-tax payment for 2026 is not deductible under (a). (H)
- J33 s 47(b) payers: a payment to a pension fund for a spouse's pension right counts as the taxpayer's ("הוא או בן זוגו"). (H)
- J34 s 47(b): paid to a fund other than a pension fund (for example to an education fund only): the (b) deduction does not apply. (M)

## K. Retirement Age Law 5764-2004 — RAL

- K01 s 3: a man (born May 1942 or later): retirement age 67. (H)
- K02 s 3: a woman born 1 January 1970 or later: 65. (H)
- K03 s 4: mandatory retirement age for men and women: 67. (H)
- K04 s 5: early retirement age for men and women: 60. (H)
- K05 s 6(1) + Part A: man born February 1939: 65. (H)
- K06 Man born March 1939: 65; born April 1939: 65 years 4 months. (H)
- K07 Man born August 1939: 65y4m; born September 1939: 65y8m. (H)
- K08 Man born April 1940: 65y8m; born May 1940: 66. (H)
- K09 Man born December 1940: 66; born January 1941: 66y4m. (H)
- K10 Man born August 1941: 66y4m; born September 1941: 66y8m. (H)
- K11 Man born April 1942: 66y8m; born May 1942: 67. (H)
- K12 Woman born December 1959: 62; born January 1960: 62y4m. (H)
- K13 Woman born December 1960: 62y4m; born January 1961: 62y8m. (H)
- K14 Woman born December 1961: 62y8m; January 1962: 63. (H)
- K15 Woman born December 1962: 63; January 1963: 63y3m. (H)
- K16 Woman born December 1963: 63y3m; January 1964: 63y6m. (H)
- K17 Woman born December 1964: 63y6m; January 1965: 63y9m. (H)
- K18 Woman born December 1965: 63y9m; January 1966: 64. (H)
- K19 Woman born December 1966: 64; January 1967: 64y3m. (H)
- K20 Woman born December 1967: 64y3m; January 1968: 64y6m. (H)
- K21 Woman born December 1968: 64y6m; January 1969: 64y9m. (H)
- K22 Woman born 15 December 1969: 64y9m, reached 15 September 2034. (H)
- K23 Woman born 15 January 1970: s 6(2) does not apply (born after December 1969): 65, reached 15 January 2035. (H)
- K24 Woman born before May 1947: Part B has no row for her although s 6(2) covers "עד חודש דצמבר 1969". I cannot read a figure: refuse (gap in the table). (L)
- K25 Mandatory retirement (s 7), a woman born January 1941: the Part A age: 66y4m. (H)
- K26 s 7, a man born May 1942 or later: 67. (H)
- K27 Early retirement (s 8), woman born April 1947: 56y8m; May 1947: 57. (H)
- K28 Woman born December 1949: 57; January 1950: 57y4m. (H)
- K29 Woman born August 1950: 57y4m; September 1950: 57y8m. (H)
- K30 Woman born April 1955: 59y8m; May 1955: 60. (H)
- K31 Woman born December 1951: 58; January 1952: 58y4m. (H)
- K32 Woman born December 1953: 59; January 1954: 59y4m. (H)
- K33 Man born 1950: early retirement age 60 (s 5; s 8 applies only to women). (H)
- K34 s 10(b)(1): an agreement may set the age at which a worker can be compelled to retire above 67: agreement saying 70: effective. (H)
- K35 s 10(a): an agreement setting the compulsory age at 65 does not override s 4: the law's 67 prevails. (H)
- K36 s 10(b)(2): an agreement allowing a pension from age 58 where the employer bears the whole extra cost: valid. (H)
- K37 s 10(b)(2): the same where the cost is not borne in full by the employer and the Minister has not approved another body to bear it: not valid. (M)
- K38 s 12: a woman whose agreement from before 1 April 2004 fixed a higher retirement age than the statutory one: her age for the right to retire and take a benefit from the employer is the agreement's age. (H)
- K39 Definition of "גמלה": a pension or payment paid because of retirement for age from a budgeted body, a mutual-guarantee body, or under an employer's commitment on termination because of the worker's age. (H)
- K40 Interaction with ITO s 37: "יחיד מוטב" when the taxpayer or the spouse has reached retirement age: a man born 1 March 1959 turns 67 on 1 March 2026; in tax year 2026 he is a "יחיד מוטב" under the reading "reached in or before the tax year"; under a reading "at the start of the year" he is not. (L, AMB-9)
- K41 A woman born in March 1960 (retirement age 62y4m, reached July 2022): in 2026 she is past retirement age; her spouse's dependency proved: s 37 point 1. (M)
- K42 A woman born 1962 (retirement age 63, reached 2025): yachid muetav for 2026 under any reading. (H)
