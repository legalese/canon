# DECIDED-ANSWERS: Encouragement of Aliyah and Return (Temporary Provision) Law 5786-2026

Author: fid-il-36, independent test author, run id IL-56-36-20261008.
Written from the Hebrew text alone, before opening any encoding.
Source of authority: Sefer HaChukim 3511 pp. 416-418 (PDF pp. 4-6 of 25_lsr_12235101.pdf), read from page images at 150 and 260 dpi; ITO definitions read from the deposited new-version ITO .he.wiki.txt (s 1, s 14, s 62A(d), s 88).
Confidence: H = the text decides; M = the text decides on its better reading, or an input I treat as given; L = a real gap, my reading is a guess.
Section numbers are those of chapter D section 9 of the amending law (the Law's own sections 1-6).

## 0. The reading I work from

Window (s 2(a)): an oleh who first became an Israeli resident, or a returning veteran resident who became an Israeli resident, in the period from 14 Cheshvan 5786 (5 Nov 2025) to the end of tax year 2026 (31 Dec 2026), both ends inclusive.
Exempt: qualifying income produced or accrued in Israel while they were Israeli residents, in tax years 2026-2030, up to a per-person per-year ceiling, "unless they asked otherwise, as to the income, all or part" (`אלא אם כן ביקשו אחרת, לעניין ההכנסות, כולן או חלקן`).
Ceilings (s 2(a)(1)-(4)): 2026 600,000; 2027 1,000,000; 2028 1,000,000; 2029 350,000; 2030 150,000; no ceiling and no exemption for any other year.
Relatives (s 2(b)): for qualifying income received from a relative (`הכנסה מזכה ... שהתקבלה מקרוב`) paragraphs (1)-(3) are replaced by "tax years 2026 to 2029, up to 140,000 per year"; paragraph (4) is not replaced, so 2030 keeps 150,000.
Both kinds in one year (s 2(c)): entitled to the exemption "under (a) or (b), as the case may be, provided the total exempt does not exceed the ceilings in (a)".
So my formula is: exempt = min( ceiling(year), Q + min(R, 140,000 in 2026-2029) ), where Q is qualifying income not from a relatives and R is qualifying income from relatives, each after removing any income the person elected to leave taxable.
2026 (s 2(d)): both the (a)(1) ceiling and the (b) ceiling are taken "proportionally to the period of their residence in Israel in that year" (`באופן יחסי לתקופת תושבותם בישראל בשנה האמורה`).
Date of first residence (s 2(e)): ITO s 14(b)(1) (the adaptation-year election) is disregarded in finding the date.
Qualifying income (s 1): taxable income (`הכנסה חייבת`) that is personal-exertion income under ITO s 2(1) or (2), that is not "other income" (ITO s 62A(d): interest, linkage, discount; dividend; rent; consideration from sale of an asset (s 88); securities sold as business inventory; consideration from real-estate rights), and that is not income attributed to the person from a "transparent corporation" (`תאגיד שקוף`, defined here as an ITO s 64(a) transparent corporation in which the person is a material shareholder, other than one wholly owned by the person), except income so attributed under ITO s 62A.
Material shareholder (s 1, via ITO s 88): 10% or more of any means of control, alone or together with another.
Relative (s 1, via ITO s 88): spouse, brother, sister, parent, grandparent, descendant, step-descendant, the spouse of any of these; descendant of a sibling; sibling of a parent; a body held 25% or more by the person or a relative; certain trustees; other than a company wholly owned by the oleh.
Oleh (s 1): holder of an oleh visa or oleh certificate under the Law of Return, or in a class entitled to an absorption basket under s 2 of the Absorption Basket Law, other than a person whose Israeli citizenship was annulled under s 11 of the Citizenship Law.
Returning veteran resident (s 1): ITO s 14(a) (returned after at least ten consecutive years as a non-resident), and holding a returning-resident certificate issued by the Ministry of Aliyah and Absorption.
Entity income (s 3): business income of a foreign-resident entity produced in Israel through the personal exertion of the oleh or veteran, years 2026-2030, is exempt (no ceiling stated), unless the entity asked otherwise, provided the entity had no Israel-produced business income that arose without his exertion; not applied (s 3(b)) if the person is a material shareholder in the entity, or, for a transparent foreign entity, as to the part attributable to an Israeli-resident rights-holder.
Departure (s 4): the Law does not apply "from its commencement" to an individual who ceases to be an Israeli resident during tax year 2028 or 2029 and stays in Israel fewer than 75 days "in one of those years".
Savings (s 5): without prejudice to s 2(e), nothing here derogates from ITO ss 14 and 97.
Commencement (s 6): 12 Tevet 5786 (1 Jan 2026), applying to qualifying income produced or accrued from the day the oleh first became resident or the veteran became resident.
Out of scope for this test pass: chapter C (the s 121 bracket changes), chapter E (the special payment on bank profits 2026-2027), and the ITO s 14 / s 97 foreign-income exemptions themselves.
Unless a case says otherwise: arrival and residence are in the window, nobody departs, no election is made, all income is qualifying, produced in Israel while resident, and not from relatives; the person has the status of oleh.

## 1. Flagged ambiguities (decided reading, and what the alternative gives)

AMB-1, the 2026 pro rata unit (s 2(d), `לתקופת תושבותם`).
Decided: days, inclusive of the arrival day, over 365 (2026 is not a leap year).
Why: a period of residence is naturally a span of days; the Ordinance counts days elsewhere (75 days here, 90 days in ITO s 14(b)(1)); the text never says months.
Alternative: whole months (arrival month excluded or included, or by half-months).
For arrival 15 Mar 2026 days give 292/365 x 600,000 = 480,000; months give 450,000 (Apr-Dec) or 500,000 (Mar-Dec).
Confidence M; the encoding should refuse or name the reading if it supports more than one.
AMB-2, the 140,000 cap in 2030 (s 2(b)).
Decided: no relative-specific cap in 2030; a relative's income in 2030 is limited only by the 150,000 ceiling of (a)(4).
Why: (b) says it replaces paragraphs (1) to (3) and its replacement text names "2026 to 2029"; paragraph (4) is untouched.
Alternative: 140,000 in 2030 as well (if one assumes a drafting slip).
Confidence H on the text.
AMB-3, the relatives' cap against the general ceiling (s 2(b), (c)).
Decided: the relatives' 140,000 is a sub-cap inside the (a) ceiling, per s 2(c) ("the total exempt shall not exceed the ceilings in (a)"): exempt = min(C, Q + min(R, 140,000)).
Alternative 1: two independent ceilings with no overall bound (excluded by s 2(c), so not arguable).
Alternative 2: the whole of a person's income is limited to 140,000 once any relative income exists (not supported by the text).
Confidence H.
AMB-4, s 4 "in one of those years" (`באחת מאותן השנים`).
Decided (literal): the person ceased to be resident in 2028 or 2029, and in at least one of the two years 2028, 2029 (whichever) was in Israel fewer than 75 days.
Alternative: the 75-day count is for the year in which he ceased.
Where they differ: ceased 1 Oct 2028 having been in Israel 275 days in 2028, then 30 days in 2029: literal = disqualified; alternative = not.
Confidence L-M; encoding default should refuse or name the reading.
AMB-5, s 4 and the entity exemption in s 3.
Decided: s 4 speaks of the individual; the entity's s 3 exemption is not removed by it.
Alternative: the entity's exemption falls away with the individual's, because s 3 derives from his exertion.
Confidence L.
AMB-6, the adaptation-year election (ITO s 14(b)(1)) and pro rata or "while resident".
Decided: s 2(e) removes the election for finding when he first became resident; I take the same for "while they were residents" and for the 2026 residence period, so the election changes nothing.
Alternative: with the election he is not a resident for a year, so income in that year is not "earned while resident" and 2026 residence days are fewer.
Confidence L-M.
AMB-7, entity income before the person's arrival date in 2026 (s 3 with s 6).
Decided: s 3 exempts only income produced from the day he became resident (s 6).
Alternative: the whole entity-year is exempt.
Confidence L.
AMB-8, rounding of 2026 pro rata amounts.
The text gives no rounding rule; I give exact rational values and the value to the agora; where possible I picked arrival dates that give whole shekels.
Confidence H that nothing is specified.
AMB-9, 2025 income of someone who arrived between 5 Nov and 31 Dec 2025.
Decided: nothing is exempt for 2025, since s 2(a) lists only tax years 2026-2030 (s 6 starts the Law on 1 Jan 2026).
Alternative: s 6's "from the day he became resident" reaches 2025 (not supported: no ceiling is given for 2025).
Confidence H-M.

## 2. Cases

Format: id | situation | decided answer | basis | confidence.
"Exempt" means the amount of qualifying income exempt from tax under s 2 (unless stated).

### A. Who is covered, and the window (s 1, s 2(a), s 2(e))

| id | situation | decided answer | basis | conf |
|---|---|---|---|---|
| A01 | Oleh (certificate), first resident 5 Nov 2025 | covered | `יום י״ד בחשוון התשפ״ו (5 בנובמבר 2025)` start of window, s 2(a) | H |
| A02 | Oleh, first resident 4 Nov 2025 | not covered, exempt 0 in every year | before the window | H |
| A03 | Oleh, first resident 31 Dec 2026 | covered (window ends `תום שנת המס 2026`) | s 2(a) | H |
| A04 | Oleh, first resident 1 Jan 2027 | not covered, 0 | after the window | H |
| A05 | Oleh, first resident 31 Dec 2025, 2026 income 700,000 | covered, 2026 exempt 600,000 (full year of 2026 residence) | s 2(a)(1), (d) | H |
| A06 | Oleh, first resident 1 Jan 2026, 2026 income 700,000 | covered, exempt 600,000 | s 2(a)(1) | H |
| A07 | Returning veteran, 10 consecutive years abroad, certificate, returned 1 Mar 2026 | covered | s 1 `תושב חוזר ותיק`, ITO s 14(a) | H |
| A08 | Returning resident, only 9 consecutive years abroad, certificate | not a veteran, not covered, 0 | ITO s 14(a) `עשר שנים רצופות לפחות` | H |
| A09 | Returning veteran (10 years) without the Ministry's certificate | not covered, 0 | s 1 `ובלבד שבידו תעודת תושב חוזר` | H |
| A10 | Oleh whose Israeli citizenship was annulled under Citizenship Law s 11 | not an oleh, 0 | s 1 `למעט מי שאזרחותו ... בוטלה` | H |
| A11 | Person in a class entitled to an absorption basket, no oleh certificate | an oleh, covered | s 1 `או מי שנמנה עם סוג בני אדם ... סל קליטה` | M |
| A12 | Person who was an Israeli resident before, abroad 4 years, now returning, oleh certificate | not first-time resident, not a veteran, not covered, 0 | s 2(a) `לראשונה` | M |
| A13 | Oleh arrived 1 Feb 2026 and elected the adaptation year (ITO s 14(b)(1)) | still covered, first residence is 1 Feb 2026 for the window | s 2(e) | H on the window, see AMB-6 for amounts |
| A14 | Person who is both oleh and returning veteran, 2027, income 1,500,000 | one exemption of 1,000,000; the ceiling is not doubled | s 2(a) is one ceiling per person-year | H |
| A15 | Same dual person, 2026 full year, income 1,300,000 | 600,000 | same | H |

### B. Ceilings by year, full-year resident (arrived on or before 1 Jan 2026), no relatives

| id | situation | decided answer | basis | conf |
|---|---|---|---|---|
| B01 | 2026, Q = 599,999 | 599,999 | (a)(1) `עד לתקרת ... 600,000` | H |
| B02 | 2026, Q = 600,000 | 600,000 | same | H |
| B03 | 2026, Q = 600,001 | 600,000 (taxable 1) | same | H |
| B04 | 2026, Q = 0 | 0 | | H |
| B05 | 2027, Q = 999,999 | 999,999 | (a)(2) `מיליון שקלים חדשים, לכל שנה` | H |
| B06 | 2027, Q = 1,000,000 | 1,000,000 | same | H |
| B07 | 2027, Q = 1,000,001 | 1,000,000 | same | H |
| B08 | 2028, Q = 1,500,000 | 1,000,000 (taxable 500,000) | (a)(2) covers 2027 and 2028 | H |
| B09 | 2028, Q = 1,000,000 | 1,000,000 | | H |
| B10 | 2029, Q = 349,999 | 349,999 | (a)(3) 350,000 | H |
| B11 | 2029, Q = 350,000 | 350,000 | | H |
| B12 | 2029, Q = 350,001 | 350,000 | | H |
| B13 | 2030, Q = 149,999 | 149,999 | (a)(4) 150,000 | H |
| B14 | 2030, Q = 150,000 | 150,000 | | H |
| B15 | 2030, Q = 150,001 | 150,000 | | H |
| B16 | 2031, Q = 100,000 | 0 | no paragraph for 2031 | H |
| B17 | 2025, arrived 5 Nov 2025, Q = 80,000 | 0 (see AMB-9) | years listed are 2026-2030 | H-M |
| B18 | 2027 Q = 0, then 2029 Q = 500,000 | 2029 exempt 350,000; nothing carries over | ceilings are per year | H |
| B19 | 2027, Q = 1,200,000 | exempt 1,000,000, taxable 200,000 | | H |
| B20 | 2026 with a 2027-style income of 1,000,000 in 2026 | 600,000 | | H |

### C. 2026 pro rata (s 2(d)); Q large unless stated; days inclusive of arrival day over 365

| id | situation | decided answer | basis | conf |
|---|---|---|---|---|
| C01 | Arrival 15 Mar 2026 (292 days), Q = 1,000,000 | 480,000 (600,000 x 292/365); months-reading alternatives 450,000 or 500,000 | (d), AMB-1 | M |
| C02 | Arrival 20 Oct 2026 (73 days), Q = 1,000,000 | 120,000; months: 100,000 or 150,000 | (d) | M |
| C03 | Arrival 8 Aug 2026 (146 days), Q = 1,000,000 | 240,000; months: 200,000 or 250,000 | (d) | M |
| C04 | Arrival 27 May 2026 (219 days), Q = 1,000,000 | 360,000; months: 350,000 or 400,000 | (d) | M |
| C05 | Arrival 1 Jul 2026 (184 days), Q = 1,000,000 | 302,465.75 (110,400,000/365 = 302,465.7534...); months: 300,000 under both month conventions that include July as a full month | (d) | M |
| C06 | Arrival 31 Dec 2026 (1 day), Q = 1,000,000 | 1,643.84 (600,000/365 = 1,643.8356...) | (d) | M |
| C07 | Arrival 2 Jan 2026 (364 days), Q = 1,000,000 | 598,356.16 (600,000 x 364/365 = 598,356.1644) | (d) | M |
| C08 | Arrival 15 Mar 2026, Q = 400,000 (below the pro rata ceiling) | 400,000 | min(480,000, 400,000) | M |
| C09 | Arrival 15 Mar 2026, Q = 480,000 | 480,000 | | M |
| C10 | Arrival 15 Mar 2026, Q = 480,001 | 480,000 | | M |
| C11 | Arrival 15 Mar 2026, R = 200,000 (relatives), Q = 0 | 112,000 (140,000 x 292/365) | (d) names `או (ב)` | M |
| C12 | Arrival 20 Oct 2026, R = 200,000, Q = 0 | 28,000 (140,000 x 73/365) | (d) | M |
| C13 | Arrival 15 Mar 2026, Q = 100,000, R = 200,000 | min(480,000, 100,000 + 112,000) = 212,000 | (c), (d) | M |
| C14 | Arrival 31 Dec 2026, 2027 Q = 1,000,000 | 1,000,000 (pro rata is for 2026 only) | (d) is limited to `בשנת המס 2026` | H |
| C15 | Arrival 5 Nov 2025, 2026 Q = 700,000 | 600,000 (full 2026 residence) | (d) | H |
| C16 | Arrival 1 Jul 2026, R = 100,000, Q = 0 | min(100,000, 140,000 x 184/365 = 70,575.34) = 70,575.34 | (d) | M |
| C17 | Arrival 8 Aug 2026, Q = 100,000, R = 100,000 | min(240,000, 100,000 + min(100,000, 56,000)) = 156,000 | (c), (d) | M |
| C18 | Arrival 27 May 2026, Q = 400,000 | 360,000 | | M |

### D. Relatives' 140,000 (s 2(b), (c)); full-year resident

| id | situation | decided answer | basis | conf |
|---|---|---|---|---|
| D01 | 2026, R = 140,000 only | 140,000 | (b) | H |
| D02 | 2026, R = 140,001 only | 140,000 | (b) | H |
| D03 | 2026, R = 139,999 only | 139,999 | (b) | H |
| D04 | 2027, R = 500,000 only | 140,000 | (b) | H |
| D05 | 2028, R = 140,000 only | 140,000 | (b) | H |
| D06 | 2029, R = 200,000 only | 140,000 | (b) `2026 עד 2029` | H |
| D07 | 2030, R = 150,000 only | 150,000 (no relatives' cap in 2030) | (a)(4) untouched, AMB-2 | H on text |
| D08 | 2030, R = 160,000 only | 150,000 | (a)(4) | H |
| D09 | 2027, Q = 800,000, R = 300,000 | min(1,000,000, 800,000 + 140,000) = 940,000 | (c) | H |
| D10 | 2027, Q = 950,000, R = 300,000 | min(1,000,000, 950,000 + 140,000) = 1,000,000 | (c) | H |
| D11 | 2026, Q = 500,000, R = 200,000 | min(600,000, 640,000) = 600,000 | (c) | H |
| D12 | 2029, Q = 300,000, R = 100,000 | min(350,000, 400,000) = 350,000 | (c) | H |
| D13 | 2029, R = 100,000 only | 100,000 | | H |
| D14 | 2030, Q = 100,000, R = 100,000 | min(150,000, 200,000) = 150,000 | (c) | H |
| D15 | 2027, 300,000 received from a company wholly owned by the oleh | not from a "relative", so Q = 300,000, exempt 300,000 (not capped at 140,000) | s 1 `קרוב ... למעט חברה שבבעלותו המלאה של העולה` | H |
| D16 | 2027, 300,000 from a company 25% held by the oleh's brother | a relative under ITO s 88 "relative" (3) (held 25% or more by a relative), so R = 300,000, exempt 140,000 | s 1, ITO s 88 | M |
| D17 | 2027, 300,000 from his spouse | relative, exempt 140,000 | ITO s 88 (1) | H |
| D18 | 2028, R = 100,000 and Q = 950,000 | min(1,000,000, 1,050,000) = 1,000,000 | (c) | H |

### E. Election "otherwise" (s 2(a), s 3(a))

| id | situation | decided answer | basis | conf |
|---|---|---|---|---|
| E01 | 2027, Q = 800,000, elects that all of it be taxed | exempt 0, taxable 800,000 | `ביקשו אחרת ... כולן` | H |
| E02 | 2027, Q = 800,000, elects on 300,000 | exempt 500,000 | `או חלקן` | H |
| E03 | 2027, Q = 1,200,000, elects on 300,000 | min(1,000,000, 900,000) = 900,000 | the elected income is outside the exempt base | H |
| E04 | 2027, Q = 1,200,000, elects on 100,000 | min(1,000,000, 1,100,000) = 1,000,000 | | H |
| E05 | 2027 elects on all; 2028 no election, Q = 500,000 | 2028 exempt 500,000 | election is per year, per income | M |
| E06 | 2027, Q = 800,000, R = 300,000, elects on all of R | exempt 800,000 | | H |
| E07 | 2027, Q = 800,000, R = 300,000, elects on 200,000 of R (so R = 100,000) | min(1,000,000, 800,000 + 100,000) = 900,000 | | H |
| E08 | Entity (s 3) asks otherwise, 2027, income 500,000 | not exempt, taxed | s 3(a) `אלא אם כן ... ביקש אחרת` | H |
| E09 | 2026 full year, Q = 700,000, elects on 100,000 | min(600,000, 600,000) = 600,000 | | H |

### F. Entity income (s 3)

| id | situation | decided answer | basis | conf |
|---|---|---|---|---|
| F01 | Foreign-resident entity, 2027, Israel business income 2,000,000 solely from the oleh's exertion; he holds no shares | exempt 2,000,000 (no ceiling in s 3) | s 3(a) | M |
| F02 | Same but he holds 10% of the entity | not exempt (material shareholder) | s 3(b)(1), ITO s 88 `10% לפחות` | H |
| F03 | Same but he holds 9.9% | exempt | s 3(b)(1) not met | H |
| F04 | Same, 2026 | exempt | `2026 עד 2030` | H |
| F05 | Same, 2030 | exempt | | H |
| F06 | Same, 2031 | not exempt | | H |
| F07 | Same, 2025 | not exempt | | H |
| F08 | Entity is an Israeli resident | s 3 does not apply (`חבר בני אדם תושב חוץ`) | s 3(a) | H |
| F09 | Foreign entity also has Israel business income that arises without his exertion | the exemption fails for the entity | proviso `ובלבד` | M |
| F10 | Foreign transparent entity, income 1,000,000 from his exertion; he holds 5%, an Israeli-resident third party holds 20%, non-residents hold 75% | exempt 750,000 (the part attributable to non-residents); the 25% attributable to Israeli residents is outside s 3 | s 3(b)(2) | M |
| F11 | Foreign transparent entity, all owners non-resident, he holds nothing | exempt in full | s 3(a), (b)(2) not engaged | M |
| F12 | The entity's exempt income and his own: 2027, personal Q = 1,000,000 and entity income 500,000 | personal exempt 1,000,000 and entity exempt 500,000; the entity amount does not use up his ceiling | s 3 is a separate exemption with no ceiling | M |
| F13 | Entity income produced before his 2026 arrival date | see AMB-7; decided: not exempt | s 6 | L |

### G. Departure (s 4)

| id | situation | decided answer | basis | conf |
|---|---|---|---|---|
| G01 | Ceases residence 30 Jun 2028; in Israel 74 days in 2028 | the Law does not apply from 1 Jan 2026: exempt 0 for every year | s 4 `פחות מ־75 ימים` | H |
| G02 | Same, 75 days in 2028 and 75 or more in 2029 | the Law still applies (75 is not fewer than 75) | s 4 | H |
| G03 | Same, 76 days in 2028 and 76 in 2029 | still applies | s 4 | H |
| G04 | Ceases 1 Mar 2029; 74 days in 2029; in 2028 he was resident throughout and in Israel 300 days | disqualified (74 < 75 in one of those years) | s 4 | H |
| G05 | Ceases 1 Mar 2029; 75 days in 2029 | not disqualified (if he also had 75+ days in 2028) | s 4 | H |
| G06 | Ceases 1 Mar 2029; 76 days in 2029, 300 in 2028 | not disqualified | s 4 | H |
| G07 | Ceases 10 Oct 2027, 10 days in 2028, 10 days in 2029 | s 4 is not engaged (he did not cease in 2028 or 2029); exemption for 2027 income earned while resident stands | s 4 limited to 2028 or 2029 | M |
| G08 | Ceases 15 Apr 2030, 20 days in 2030 | not affected (2030 is not named) | s 4 | H |
| G09 | Stays resident in 2028 (centre of life stays) though only 20 days physically in Israel | not ceased, s 4 not engaged | s 4 `חדל להיות תושב ישראל` | M |
| G10 | Departs 2028 with 74 days: what of 2026 and 2027 | retroactive: 2026 exempt 0 (taxable 600,000 if his income was 600,000), 2027 exempt 0 | s 4 `מיום תחילתן` | H |
| G11 | Departs 2028 with 74 days: 2028 income earned before leaving, 400,000 | exempt 0 | s 4 | H |
| G12 | Ceased 1 Oct 2028, 275 days in 2028, then 30 days in 2029 | literal: disqualified (30 < 75 in 2029); alternative: not | AMB-4 | L-M |
| G13 | Ceased 1 Oct 2028, 275 days in 2028, 0 days in 2029 | literal: disqualified; alternative: not | AMB-4 | L-M |
| G14 | Departure and s 3 entity (ceased 2028, 74 days): the entity's 2027 exemption | AMB-5: decided, unaffected | | L |
| G15 | A person who departs and never has a year under 75 days: exemption for earlier years | stands | s 4 | H |

### H. Income types (qualifying income, s 1)

| id | situation | decided answer | basis | conf |
|---|---|---|---|---|
| H01 | 2027 salary from Israeli employer 400,000 | qualifying; exempt 400,000 | ITO s 2(2) | H |
| H02 | 2027 business or profession income produced in Israel 400,000 | qualifying; exempt 400,000 | ITO s 2(1) | H |
| H03 | 2027 rent 100,000 | not qualifying (other income); exempt 0 | ITO s 62A(d)(3) | H |
| H04 | 2027 bank interest 50,000 | not qualifying | s 62A(d)(1) | H |
| H05 | 2027 dividend 80,000 | not qualifying | s 62A(d)(2) | H |
| H06 | 2027 consideration from selling a capital asset 300,000 | not qualifying | s 62A(d)(4) | H |
| H07 | 2027 interest earned inside a business, treated as business income | still other income (`לרבות הכנסה כאמור שנחשבת כהכנסה מעסק`), not qualifying | s 62A(d) | H |
| H08 | 2027 consideration from sale of a right in real estate 500,000 | not qualifying | s 62A(d)(6) | H |
| H09 | 2027 securities sold as business inventory 200,000 | not qualifying | s 62A(d)(5) | H |
| H10 | Foreign-source employment income | not within this Law (not produced or accrued in Israel); exempt under ITO s 14(a) if applicable | s 2(a), s 5 | H |
| H11 | 2027: salary 500,000, rent 200,000, interest 30,000 | exempt 500,000 (only the salary qualifies) | | H |
| H12 | 2027: business income 300,000 plus business interest 50,000 | exempt 300,000 | | H |
| H13 | 2027 gross salary 700,000, taxable (after deductions) 600,000 | qualifying income 600,000, exempt 600,000 | s 1 `הכנסה חייבת` | M |
| H14 | Income of 300,000 attributed to him from a transparent corporation in which he holds 40%, not under s 62A | not qualifying | s 1 `ואינה הכנסה המיוחסת ... מתאגיד שקוף` | M |
| H15 | Same 300,000 attributed to him under ITO s 62A | qualifying (the exception), exempt 300,000 | s 1 `למעט ... לפי סעיף 62א` | M |
| H16 | 300,000 attributed from a corporation wholly owned by him | that corporation is not a "transparent corporation" under this Law, so the income is qualifying if personal-exertion | s 1 `למעט תאגיד ... שבבעלותו המלאה` | M |
| H17 | Income earned in Israel before the arrival date (visit, then arrival 1 Jul 2026), 100,000 | not qualifying (not earned `בעת שהיו תושבי ישראל`) | s 2(a), s 6 | M |
| H18 | Pension or annuity income from abroad | not qualifying | not ITO s 2(1) or (2), and not Israeli-source | H |

### I. Savings, commencement and other

| id | situation | decided answer | basis | conf |
|---|---|---|---|---|
| I01 | Oleh's foreign-source income in 2027 | still exempt under ITO s 14(a); this Law neither adds to nor reduces it | s 5 | H |
| I02 | Using this Law's ceiling does not reduce the ITO s 14 foreign-income exemption | correct, separate | s 5 | M |
| I03 | A person arriving 15 Mar 2026 asks what is exempt in 2027 | 1,000,000 ceiling, not pro rated | (a)(2), (d) | H |
| I04 | A person arriving 15 Mar 2026 asks about 2031 | 0 | | H |

## 3. Count

The cases are the rows in sections A-I.
Count recorded in the closing message of the run, computed by `grep -c` over the ids.
