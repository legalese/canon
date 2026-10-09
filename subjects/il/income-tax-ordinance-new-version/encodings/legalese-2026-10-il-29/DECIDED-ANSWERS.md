# IL-29 decided answers (independent test author fid-il-29, written from the Hebrew sources alone)

Status: written before the encoding directory was opened.
Sources read: the ITO text (s 1 definitions "תושב ישראל", "תושב חוץ", "שנת מס"; s 2; s 2א; s 14) and the four regulations in registers/source-bundle/regulations/.
Hebrew is authoritative; the Wikisource text is an unofficial consolidation.
Figures that appear only in Wikisource editorial notes (`{{ח:הערה|...}}`) are not law.
Such cases are marked NPF (needs the published figure) and a refusal is expected.

Conventions.
Tax year Y is the calendar year unless a special assessment period was fixed.
2024 and 2028 are leap years (366 days); 2025 is not (365 days).
"D0" is days in Israel in tax year Y, "D1" and "D2" the days in the two preceding tax years.
A day counts if any part of it was spent in Israel (s 1 "תושב ישראל" (א)(2) last line: "יום – לרבות חלק מיום").
Confidence: H high, M medium, L low.
"AMBIG" marks a genuine ambiguity: the decided reading is stated, and a refusal is acceptable for the encoding if it chose not to pick.

## A. Individual: the day-count presumptions (s 1 "תושב ישראל" (א)(2), (3))

Text: "חזקה היא שמרכז חייו של יחיד בשנת המס הוא בישראל – (א) אם שהה בישראל בשנת המס 183 ימים או יותר; (ב) אם שהה בישראל בשנת המס 30 ימים או יותר, וסך כל תקופת שהייתו בישראל בשנת המס ובשנתיים שקדמו לה הוא 425 ימים או יותר".
Output "presumed" means the presumption of centre of life in Israel arises; it is rebuttable (A32 onwards).

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| A01 | D0=183, D1=D2=0, 2025 | presumed (limb a) | "183 ימים או יותר" | H |
| A02 | D0=182, D1=D2=0 | not presumed (limb a fails; limb b: 182 < 425) | same | H |
| A03 | D0=184, D1=D2=0 | presumed | same | H |
| A04 | D0=365 | presumed | same | H |
| A05 | D0=0, D1=D2=0 | not presumed | no limb | H |
| A06 | D0=1, D1=D2=0 | not presumed | limb b needs 30 days | H |
| A07 | D0=183 in leap 2024 (D0=183 of 366) | presumed | days threshold is absolute, not a fraction of the year | H |
| A08 | D0=182 in leap 2024 | not presumed by limb a | same | H |
| A09 | D0=30, D1+D2=395 (e.g. 200+195) | presumed (limb b: 30 >= 30 and 425 >= 425) | "30 ימים או יותר ... 425 ימים או יותר" | H |
| A10 | D0=30, D1+D2=394 | not presumed (total 424) | same | H |
| A11 | D0=29, D1=D2=365 (total 759) | not presumed (29 < 30) | the 30-day floor is separate | H |
| A12 | D0=30, D1=0, D2=0 | not presumed (total 30) | limb b | H |
| A13 | D0=100, D1=200, D2=125 (total 425) | presumed | limb b | H |
| A14 | D0=100, D1=200, D2=124 (total 424) | not presumed | limb b | H |
| A15 | D0=182, D1=182, D2=182 (total 546) | presumed by limb b although never 183 | limb b | H |
| A16 | D0=182, D1=61, D2=182 (total 425) | presumed (limb b) | limb b | H |
| A17 | D0=182, D1=61, D2=181 (total 424) | not presumed | limb b | H |
| A18 | D0=30, D1=366 (leap), D2=29 (total 425) | presumed | limb b | H |
| A19 | D0=29, D1=D2=366 | not presumed | 29 < 30 | H |
| A20 | D0=183 and D1=D2=0 and every other tie abroad | presumption arises (rebuttal question separate, A32) | (א)(2)(א) | H |
| A21 | Arrives 2025-07-02 (any hour), stays to 2025-12-31 | D0=183: presumed | part of a day counts; Jul 2-31 is 30, then 31+30+31+30+31 | H |
| A22 | Arrives 2025-07-03, stays to year end | D0=182: not presumed | same arithmetic | H |
| A23 | In Israel from 2025-01-01, leaves 2025-07-02 | D0=183 (181 days to 30 Jun, plus 1 and 2 Jul): presumed | departure day counts as part of a day | H |
| A24 | In Israel from 2025-01-01, leaves 2025-07-01 | D0=182: not presumed | same | H |
| A25 | Visit 1: 2025-01-01 to 2025-03-31 (90 days); visit 2: 2025-06-01 to 2025-09-01 (93 days) | D0=183: presumed | days are added across visits | H |
| A26 | As A25 but visit 2 ends 2025-08-31 | D0=182: not presumed | same | H |
| A27 | Lands 23:50 on 2025-12-31, nothing else that year | D0=1 | "לרבות חלק מיום" | H |
| A28 | Commutes across the border to work: 200 workdays, a few hours each | D0=200: presumed | each part day is a day | H |
| A29 | Leaves and returns the same calendar day | that day counts once | a day is a day | H |
| A30 | Overnight transit that spans two calendar days in Israel (lands 22:00 day 1, leaves 02:00 day 2) | 2 days | part of each day | H |
| A31 | Special assessment period shorter than 183 days, and the person is in Israel throughout it | limb a cannot be met (period shorter than 183 days) unless the text is read per year | s 1 "שנת מס" second limb; AMBIG: the statute counts days "בשנת המס" and does not prorate | L |
| A32 | Presumption arises; the individual proves centre of life abroad (e.g. permanent home, family, job and business abroad) | not an Israeli resident for Y | (א)(3): "ניתנת לסתירה ... על ידי היחיד" | H |
| A33 | Presumption arises, individual offers no evidence | Israeli resident | the presumption stands | H |
| A34 | Presumption arises; the assessing officer rebuts it by showing centre of life abroad | not resident | (א)(3): "והן על ידי פקיד השומה"; AMBIG: the text does not say in whose interest the officer rebuts; I read it as symmetric | M |
| A35 | No limb of the presumption is met, but centre of life is in Israel on the ties (family, home, work, economic interests, organisations all in Israel; D0=100) | Israeli resident (the presumption is one-way; (א)(1) is the primary test) | "מי שמרכז חייו בישראל" | M |
| A36 | No presumption, all five listed ties abroad, D0=40 | not resident | same | H |
| A37 | No presumption; ties split (home abroad, family in Israel, job abroad, finances split, one organisation in Israel) | the text gives no weighting; AMBIG, expect refusal or an explicit fact input "centre of life" | "יובאו בחשבון מכלול קשריו" | H (that it is undecidable from the text) |
| A38 | Same split as A37 but with the presumption met | resident unless the individual rebuts; the individual bears the practical burden | (א)(2),(3) | M |
| A39 | The listed ties are not exhaustive | other ties (e.g. children's school) may be weighed | "ובהם בין השאר" | H |
| A40 | The five listed ties | permanent home; residence of him and his family; usual or permanent occupation or place of employment; place of active and substantial economic interests; activity in organisations, unions or institutions | (א)(1)(א)-(ה) | H |

## B. Reg 2 of the 5766-2006 Regulations: deemed Israeli residents (employees)

Text: reg 2(1) "עובד מדינת ישראל – אם יחסי עובד מעביד בינו לבין מדינת ישראל החלו כאשר היה אותו יחיד תושב ישראל"; reg 2(2) other listed employers: "החלו כאשר היה היחיד תושב ישראל, ובלבד שלא חלפו חמש שנים מיום שהחל היחיד לעבוד אצל אותו מעביד מחוץ לישראל, והכל אלא אם כן הוכיח אחרת להנחת דעתו של פקיד השומה".
The reg applies to an individual who is not otherwise resident under (א)(1), (2).
The listed employers are those in (א)(4)(ב)-(ו): local authority; Jewish Agency; KKL and Keren Hayesod-UIA; government company; statutory authority or statutory corporation.

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| B01 | State employee, hired while resident, abroad 12 years, no ties, D0=0 | deemed resident | reg 2(1) has no time limit | H |
| B02 | State employee hired while a foreign resident (local hire abroad) | not deemed by reg 2 | the employment began when he was not resident | H |
| B03 | State employee, hired while resident, abroad 1 year | deemed resident | reg 2(1) | H |
| B04 | Local-authority employee, hired while resident; began working outside Israel 2020-01-01; assessed 2024-12-30 | deemed resident | not yet five years | H |
| B05 | Same, assessed 2025-01-03 | not deemed | five years have passed | H |
| B06 | Same, assessed exactly on the fifth anniversary 2025-01-01 | AMBIG: whether five years "חלפו" on the anniversary day depends on whether the start day is counted | reg 2(2) | L |
| B07 | Jewish Agency employee, hired while resident, began work abroad 2022, assessed 2026 | deemed resident | under five years | H |
| B08 | KKL employee, same facts as B07 | deemed resident | listed employer | H |
| B09 | Keren Hayesod-UIA employee, same | deemed resident | listed employer (the "קרן היסוד – המגבית המאוחדת לישראל") | H |
| B10 | Government-company employee, same | deemed resident | listed employer | H |
| B11 | Employee of a statutory authority, same | deemed resident | listed employer | H |
| B12 | Employee of a statutory corporation ("תאגיד שהוקם לפי חוק"), same | deemed resident | listed employer | H |
| B13 | Employee of a private company, hired while resident, abroad | not deemed | not a listed employer | H |
| B14 | Local-authority employee abroad 3 years, proves to the assessing officer's satisfaction that he is not a resident | not deemed | "אלא אם כן הוכיח אחרת" | H |
| B15 | State employee abroad, tries the same proof | AMBIG: the rebuttal clause sits at the end of (2); I read it as limited to (2), so a state employee cannot rebut by this clause | structure of reg 2 | L |
| B16 | Hired in Israel 2015 by Jewish Agency, sent abroad 2020-01-01; assessed 2023 | the five years run from the day he began working for that employer outside Israel, not from hire: deemed resident | "מיום שהחל היחיד לעבוד אצל אותו מעביד מחוץ לישראל" | H |
| B17 | Same, assessed 2026 | not deemed (more than five years since 2020-01-01) | same | H |
| B18 | Spouse and children of a state employee abroad, themselves not employees | not deemed under reg 2 | the reg lists employees only | H |
| B19 | Employee of a listed employer who is already resident under (א)(1) or (2) | resident anyway | reg 2 only extends | H |
| B20 | Reg 2 effect | the person is "treated as" an Israeli resident for the Ordinance | "יראו כתושב ישראל" | H |

## C. Reg 3: deemed foreign residents

Text: "יראו יחיד שאינו עולה חדש ושרואים אותו כתושב ישראל כאמור בפסקה (א)(1) ו־(2) להגדרה, כתושב חוץ, אם בחמש שנות המס הקודמות לשנת המס היה תושב חוץ והוא אחד מאלה".
Common conditions: (i) not a new immigrant (עולה חדש, s 35(ד)); (ii) would otherwise be seen as resident under (א)(1) or (2); (iii) a foreign resident in each of the five preceding tax years; (iv) one of the eight classes.
Class tests are in the rows below; "ביקש" classes (3), (4) need the request.
All rows assume (i), (ii), (iii) unless stated.

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| C01 | Diplomat in regular service in an official capacity for a foreign state, D0=300 | deemed foreign resident | reg 3(1) | H |
| C02 | Consular official in regular service, official capacity | deemed foreign resident | reg 3(1) | H |
| C03 | Spouse of such diplomat, residing with the diplomat | deemed foreign resident | "בן זוגו וילדיו ... המתגוררים עמו" | H |
| C04 | Child of such diplomat, residing with the diplomat | deemed foreign resident | same | H |
| C05 | Child of such diplomat not residing with the diplomat | not covered by (1) | residence with them is required | H |
| C06 | Parent of the diplomat | not covered | only spouse and children | H |
| C07 | Honorary consul or diplomat not in regular service | not covered | "בשירות סדיר ובתפקיד רשמי" | M |
| C08 | Soldier in a foreign state's army | deemed foreign resident | reg 3(2) | H |
| C09 | Person in UN service | deemed foreign resident | reg 3(2) "או בשירות האומות המאוחדות" | H |
| C10 | Came to Israel to serve in the IDF, in service, requested not to be treated as resident | deemed foreign resident until the end of service | reg 3(3) | H |
| C11 | Same, made no request | not deemed foreign (resident if (א)(1) or (2) apply) | "אם ביקש" | H |
| C12 | Same as C10, the day after discharge | no longer covered | "עד לסיום שירותו הצבאי" | H |
| C13 | Same as C10 but serving in the standing army (צבא הקבע) | not covered | reg 1: "שירות צבאי – למעט שירות בצבא הקבע" | M |
| C14 | Same as C10 but he is a new immigrant (עולה חדש) | not covered | the lead-in excludes new immigrants | H |
| C15 | Student at 100% of a full programme, year 2 of stay, requested | deemed foreign resident | reg 3(4) | H |
| C16 | Student at exactly 50% of a programme, year 1, requested | deemed foreign resident | "חצי תכנית לימודים לפחות" | H |
| C17 | Student at 49% of a programme | not covered | below half | H |
| C18 | Full-time student, year 3, requested | deemed foreign resident | "בשלוש השנים הראשונות" | H |
| C19 | Full-time student, year 4 (more than three years), requested | not covered | same | H |
| C20 | Full-time student, no request | not deemed foreign | "אם ביקש" | H |
| C21 | Student, exactly at the end of the third year | AMBIG: "three first years of his stay" may be 36 months from arrival or three tax years | reg 3(4) | L |
| C22 | Lecturer at a university, in role for the institution, year 2 | deemed foreign resident | reg 3(5) | H |
| C23 | Researcher at a higher-education institution, year 3 | deemed foreign resident | reg 3(5) | H |
| C24 | Teacher at "another teaching institution", year 1 | deemed foreign resident | "או במוסד הוראה אחר" | H |
| C25 | Lecturer, year 4 | not covered | three years | H |
| C26 | Visiting researcher not serving in a role for the institution | not covered | "ומשמש בתפקיד בעבור אותו מוסד" | M |
| C27 | Clergy filling a religious role at a religious institution in Israel at its invitation, year 2 | deemed foreign resident | reg 3(6) | H |
| C28 | Clergy without invitation of the institution | not covered | "על פי הזמנת אותו מוסד" | H |
| C29 | Clergy, year 4 | not covered | three years | H |
| C30 | Patient hospitalised in Israel; in Israel 200 days, of which 150 hospitalised; no other presence (so 50 non-hospital days); came for hospitalisation | deemed foreign resident | reg 3(7): without hospitalisation the (א)(2) presumption would not apply | H |
| C31 | Patient who fell ill while in Israel; 182 non-hospital days, 20 hospitalised | deemed foreign resident | without the hospital days D0=182, no presumption | H |
| C32 | Same, 183 non-hospital days, 20 hospitalised | not covered | without the hospital days the presumption still applies | H |
| C33 | Patient, non-hospital days 30, D1+D2=395 non-hospital (total 425), plus 100 hospital days | not covered | limb (b) still applies without hospital days | M |
| C34 | Foreign journalist, year 4 | deemed foreign resident | reg 3(8), "חמש השנים הראשונות" | H |
| C35 | Foreign sportsperson, year 5 | deemed foreign resident | same | H |
| C36 | Foreign journalist, year 6 | not covered | five years | H |
| C37 | Foreign journalist or sportsperson: who qualifies | defined in s 75A (outside the bundle for this row); take as an input | reg 1 | H |
| C38 | Diplomat who was a resident in one of the five preceding tax years | not deemed | the five-year foreign-resident condition | M (AMBIG: "היה תושב חוץ" read as each of the five years) |
| C39 | Diplomat who was a foreign resident in all five preceding years | deemed foreign resident | same | H |
| C40 | Diplomat, only the preceding four years as foreign resident, arrived year 5 | not deemed | five years required | M |
| C41 | Diplomat, ties to Israel strong but not presumed (D0=20) | deemed foreign resident (reg 3 covers (א)(1) as well as (2)) | "בפסקה (א)(1) ו־(2)" | M |
| C42 | Person not in any of the eight classes | reg 3 does not apply | closed list | H |
| C43 | Effect of reg 3 | he is treated as a foreign resident ("תושב חוץ") for the tax year | "כתושב חוץ" | H |
| C44 | Preceding five tax years for tax year 2026 | 2021 to 2025 | "חמש שנות המס הקודמות לשנת המס" | H |

## D. "Foreign resident" (s 1 "תושב חוץ")

Text: "מי שאינו תושב ישראל, וכן יחיד שהתקיימו בו כל אלה: (א) הוא שהה מחוץ לישראל 183 ימים לפחות, בכל שנה, בשנת המס ובשנת המס שלאחריה; (ב) מרכז חייו לא היה בישראל ... בשתי שנות המס שלאחר שנות המס האמורות בפסקת משנה (א)".
So for year Y: outside >= 183 days in Y and in Y+1, and centre of life not in Israel in Y+2 and Y+3.

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| D01 | Person who is not an Israeli resident | foreign resident | first limb | H |
| D02 | An Israeli-incorporated company | not a foreign resident | resident under (ב)(1) | H |
| D03 | Resident individual: D0=200, D(Y+1)=200, no other facts | not a foreign resident (outside days 165 < 183) | second limb (א) | H |
| D04 | Resident individual: outside 183 in 2025 (D0=182), outside 183 in 2026, centre of life abroad in 2027 and 2028 | foreign resident for 2025 | second limb | H |
| D05 | Same but D0(2025)=183 (outside 182) | not a foreign resident by the second limb | 182 < 183 | H |
| D06 | Same as D04 but D0(2026)=183 (outside 182) | not a foreign resident for 2025 | second year fails | H |
| D07 | Same as D04 but centre of life in Israel in 2027 | not a foreign resident | (ב) | H |
| D08 | Same as D04 but centre of life in Israel in 2028 | not a foreign resident | (ב) covers two years | H |
| D09 | Same as D04 but 2027 and 2028 both abroad, 2029 in Israel | foreign resident for 2025 | only two years are tested | H |
| D10 | Tax year 2024 (leap): D0=183 (outside 183), 2025 outside 183, 2026 and 2027 centre abroad | foreign resident for 2024 although (א)(2)(א) presumes residence at 183 days; AMBIG: part-day counting for "outside" days is not defined, since the "לרבות חלק מיום" rule is stated only inside paragraph (א) | second limb vs presumption | L |
| D11 | Status of 2025 asked on 2026-06-30 for a resident individual | cannot be decided yet: the test needs 2026, 2027 and 2028 | forward-looking text | M |
| D12 | Individual who is both an Israeli resident for Y and meets the second limb | AMBIG: the text makes him a foreign resident; whether s 2 then charges worldwide income (resident) or only Israeli-source (foreign) is not said; I take the foreign-resident treatment | s 1 "תושב חוץ" | L |
| D13 | Outside day count, 2025, in Israel 182 | outside 183 | 365 - 182 | H |
| D14 | Outside day count, 2024 (leap), in Israel 183 | outside 183 | 366 - 183 | H |
| D15 | A deemed foreign resident under reg 3 | foreign resident | reg 3 | H |

## E. "Tax year" (s 1 "שנת מס")

Text: "תקופה של שנים עשר חדשים רצופים, שתחילתה ב־1 בינואר, ואם נקבעה תקופת שומה מיוחדת – תקופת השומה שנקבעה כאמור".

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| E01 | Tax year 2025 | 2025-01-01 to 2025-12-31, 365 days | text | H |
| E02 | Tax year 2024 | 2024-01-01 to 2024-12-31, 366 days | twelve consecutive months | H |
| E03 | Date 2025-12-31 | in tax year 2025 | same | H |
| E04 | Date 2026-01-01 | in tax year 2026 | same | H |
| E05 | Special assessment period fixed as 2025-03-01 to 2025-09-30 | the tax year is that period | second limb | H |
| E06 | Special period not fixed | calendar year | first limb | H |
| E07 | A twelve-month period starting 1 April | not a tax year (no special period) | must start on 1 January | H |
| E08 | The three tax years preceding 2025 | 2022, 2023, 2024 | arithmetic | H |

## F. Bodies of persons (s 1 "תושב ישראל" (ב))

Text: (ב)(1) "התאגד בישראל"; (ב)(2) "השליטה על עסקיו וניהולם מופעלים בישראל" except a body whose control and management in Israel are exercised by an individual who became resident for the first time or a veteran returning resident (s 14(א)), or by his proxy, before ten years have passed since he became resident, "ובלבד שאותו חבר בני אדם לא היה תושב ישראל גם אם השליטה ... לא היו מופעלים בידי יחיד כאמור", "אלא אם כן חבר בני האדם ביקש אחרת".
Reading of the proviso: the exception applies only to a body that would not be resident on other grounds (the only other ground is incorporation in Israel); a body that asks otherwise is resident.

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| F01 | Incorporated in Israel; controlled and managed abroad | resident | (ב)(1) | H |
| F02 | Incorporated abroad; controlled and managed in Israel by an Israeli individual who is not a new immigrant | resident | (ב)(2) | H |
| F03 | Incorporated abroad; controlled and managed abroad | not resident | neither limb | H |
| F04 | Incorporated abroad; controlled and managed in Israel by an individual who became a first-time resident 3 years ago | not resident | exception | H |
| F05 | Same as F04, body asks to be otherwise | resident | "אלא אם כן חבר בני האדם ביקש אחרת" | H |
| F06 | Same as F04 but control and management is exercised by the individual's proxy | not resident | "או בידי מי מטעמו" | H |
| F07 | Same as F04 but the individual is a veteran returning resident (10 consecutive years as foreign resident) | not resident | exception | H |
| F08 | Same as F04 but the individual is a plain returning resident (6 to 9 years abroad) | resident | exception covers only first-time and veteran returning residents | H |
| F09 | Incorporated in Israel; controlled and managed in Israel by a first-time resident, year 3 | resident | (ב)(1) is not subject to the exception | H |
| F10 | Individual became first-time resident 2015-03-01; test date 2025-02-28; body foreign-incorporated, run by him | not resident (ten years not passed) | "טרם חלפו עשר שנים" | H |
| F11 | Same, test date 2025-03-02 | resident (ten years have passed) | same | H |
| F12 | Same, test date exactly 2025-03-01 | AMBIG: day-count convention on the anniversary | same | L |
| F13 | Same as F10, individual elected the adjustment year (s 14(ב)) | still not resident on 2025-02-28: the adjustment year counts toward the ten years, it does not extend them | s 14(ב)(2)(ב) | M |
| F14 | Same as F11, individual elected the adjustment year | resident on 2025-03-02 | same | M |
| F15 | Control in Israel shared between a first-time resident and another Israeli individual | resident; AMBIG: the exception speaks of control "בידי יחיד", read as exclusive | (ב)(2) | L |
| F16 | Control abroad, management in Israel (split) | AMBIG: whether "השליטה על עסקיו וניהולם" is conjunctive; expect refusal or a fact input | (ב)(2) | L |
| F17 | Body that was resident for another reason (incorporated in Israel) and is run by a first-time resident | resident | the proviso "לא היה תושב ... גם אם" | H |
| F18 | Foreign-incorporated body, control in Israel by a first-time resident whose ten years ended | resident | exception lapsed | H |

## G. Section 14(b): the adjustment year

Text: "לא יראו יחיד שהיה לתושב ישראל לראשונה או לתושב חוזר ותיק, כתושב ישראל, במשך שנה אחת מהמועד שבו עלה או שב לישראל ... ובלבד שהיחיד הודיע, בתוך 90 ימים מיום הגעתו לישראל כאמור, בטופס שקבע המנהל".
Veteran returning resident: foreign resident for ten consecutive years at least (five for someone who became resident in tax years 2007 to 2009).
Returning resident (s 14(ג)): six consecutive years; not covered by (ב).

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| G01 | First-time resident arrives 2025-03-01, notifies on the Director's form 2025-03-01 | adjustment year applies: not resident from 2025-03-01 for one year | 14(ב)(1) | H |
| G02 | Same, notifies 2025-05-30 (day 90) | applies | 90 days from arrival | M (day-count convention) |
| G03 | Same, notifies 2025-05-31 (day 91) | does not apply | late | M |
| G04 | Same, no notification | does not apply; normal residence tests | "ובלבד שהיחיד הודיע" | H |
| G05 | Same, notifies by a letter not on the Director's form | does not apply | "בטופס שקבע המנהל" | M |
| G06 | Arrival 2024-01-01 (leap), notifies 2024-03-31 | applies (day 90) | arithmetic: Jan 31 + Feb 29 + 30 | M |
| G07 | Arrival 2024-01-01, notifies 2024-04-01 | does not apply | day 91 | M |
| G08 | Veteran returning resident (foreign resident 10 consecutive years), arrives 2025-03-01, notifies in time | applies | 14(ב)(1) | H |
| G09 | Returning resident with 9 consecutive years as foreign resident | does not apply (not a veteran returning resident) | 14(ב) names first-time and veteran only | H |
| G10 | Returning resident with 6 consecutive years | does not apply | same | H |
| G11 | Previously resident, left for 3 years, returns | does not apply (none of the three categories) | same | H |
| G12 | Became resident in tax year 2008, returned after 5 consecutive foreign-resident years | veteran returning resident | note to the definition: 5 years for those who became resident in 2007 to 2009 (the parenthetical sits in the Wikisource note; AMBIG as to its force) | L |
| G13 | Adjustment year of arrival 2025-03-01: the last day | 2026-02-28; resident status can resume on 2026-03-01 | "שנה אחת מהמועד" | M |
| G14 | A day in the adjustment year, individual's centre of life is in Israel on every tie | not treated as resident | "על אף האמור בפסקה (א)" | H |
| G15 | Adjustment year and a tax year that straddles it | AMBIG: the Ordinance charges per tax year but the exemption runs from the arrival date; the text does not say whether the straddling tax year is split | 14(ב) vs s 2 | L |
| G16 | Does the adjustment year count toward the ten-year exemption of 14(a) | yes, if elected | 14(ב)(2)(א) | H |
| G17 | Does the adjustment year count toward the ten years of s 1 (ב)(2) (bodies) | yes, if elected | 14(ב)(2)(ב) | H |
| G18 | Does the adjustment year count toward s 97(ב)(1) period | yes, if elected | 14(ב)(2)(ו) | H |
| G19 | Notification made before the arrival | AMBIG: "בתוך 90 ימים מיום הגעתו" contemplates after arrival | 14(ב)(1) | L |

## H. Section 2 and the territorial charge

Text: "מס הכנסה יהא משתלם ... לכל שנת מס ... על הכנסתו של אדם תושב ישראל שהופקה או שנצמחה בישראל או מחוץ לישראל ועל הכנסתו של אדם תושב חוץ שהופקה או שנצמחה בישראל, ממקורות אלה: (1) ... (10)".
Source categories: (1) business or vocation; (2) work; (3) repealed; (4) dividend, interest, linkage differences, discount; (5) pension, annuity; (6) rent, royalties, key money and other profit from buildings, land, industrial building; (7) property that is not building or land; (8) agriculture; (9) consideration for patent or copyright sold by the inventor or creator outside his ordinary field; (10) any other source not in (1) to (9), not expressly excluded and not exempt.

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| H01 | Resident, wages from work performed abroad | chargeable | resident: Israel or abroad | H |
| H02 | Resident, wages from work in Israel | chargeable | same | H |
| H03 | Foreign resident, wages for work in Israel | chargeable | foreign resident: Israel | H |
| H04 | Foreign resident, wages for work abroad | not chargeable | same | H |
| H05 | Foreign resident, Israeli business profit | chargeable (source 1) | s 2(1) | H |
| H06 | Foreign resident, dividend from a foreign company, source outside Israel | not chargeable | territorial limit | H |
| H07 | Resident, foreign dividend | chargeable (source 4), subject to s 14(a) | s 2(4) | H |
| H08 | Resident, pension from abroad | chargeable (source 5), subject to s 14(a) | s 2(5) | H |
| H09 | Resident, rent from Israeli land | chargeable (source 6) | s 2(6) | H |
| H10 | Resident, income from a non-land asset (source 7) | chargeable | s 2(7) | H |
| H11 | Resident, farming profit | chargeable (source 8) | s 2(8) | H |
| H12 | Resident, sale of a patent by the inventor outside his ordinary field | chargeable (source 9) | s 2(9) | H |
| H13 | Resident, sale of a patent by the inventor within his ordinary field | not source 9; falls under (1) as business or other | s 2(9) restricts to outside the ordinary field | M |
| H14 | Resident, windfall in none of (1) to (9), not exempt, not expressly excluded | chargeable (source 10) | s 2(10) | H |
| H15 | Resident, income expressly exempt by the Ordinance | not chargeable under (10) | "ולא ניתן עליו פטור" | H |
| H16 | Item (3) | repealed: not a source | "(בוטלה)" | H |
| H17 | New immigrant (first-time resident) within ten years, foreign-source dividend from foreign assets | exempt under s 14(a) (overlay, outside the territorial charge itself) | s 14(a) | M |
| H18 | Same, income from a source in Israel | chargeable | s 14(a) covers only income produced outside Israel or sourced in assets outside | H |
| H19 | Same, the individual asked otherwise | chargeable | "אלא אם כן ביקשו אחרת" | H |
| H20 | Foreign resident: where an income is produced or arises (place of source) | not defined in s 2; take as input | s 2 | H |
| H21 | Tax charged per tax year | yes | "לכל שנת מס" | H |

## I. Section 2A: gambling, lotteries and prizes

Text: (א) winnings of a resident (Israel or abroad) or of a foreign resident (Israel only) from gambling, lotteries or prize-bearing activity are counted in determining profit or income and treated as income, "למעט לענין קיזוז הפסדים"; (ב) not applicable to (1) winnings that are income from another source under the Ordinance, (2) prizes given in a personal framework, (3) winnings from lotteries or prizes determined by the Finance Minister with the approval of the Finance Committee.

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| I01 | Resident wins a lottery in Israel | income | 2A(א) | H |
| I02 | Resident wins at a casino abroad | income | same | H |
| I03 | Foreign resident wins a lottery in Israel | income | same | H |
| I04 | Foreign resident wins at a casino abroad | not income under 2A | territorial limit | H |
| I05 | Resident wins a prize in a family game (prize in a personal framework) | not income under 2A | 2A(ב)(2) | H |
| I06 | Resident employee wins a prize in his employer's contest as part of the job | not under 2A: income from work under s 2(2) | 2A(ב)(1) | M |
| I07 | Winnings from a lottery on the Minister's list of exempted lotteries | not under 2A | 2A(ב)(3); NPF: the list is published by order, not in the bundle | H |
| I08 | Winnings from a lottery with no such order known | under 2A | NPF for the exemption | M |
| I09 | Winnings of a prize-bearing activity (a quiz show) | income | "פעילות נושאת פרסים" | H |
| I10 | Resident has a loss from other sources and gambling winnings | the loss cannot be set against the winnings; AMBIG: "למעט לענין קיזוז הפסדים" may mean the opposite | 2A(א) | L |
| I11 | Gambling loss | s 2A makes no provision for deducting it; take as not deductible under 2A | silent | L |
| I12 | Tax rate on 2A income | not in the sources | none | H (NPF) |

## J. Section 2(2)(b): value of the use of a vehicle (5747-1987 Regulations)

Reg 2(א): monthly value = the consumer-adjusted price (המחיר המתואם לצרכן) times the use rate, rounded to the nearest multiple of NIS 10.
Use rate tiers (reg 2(א) definition "שיעור שווי השימוש") depend on the "weighted 2010 price" W: (1) W (unindexed) <= 123,000: 2.6%; (2) W x CPI(Nov 2008)/CPI(Nov 2009) in (123,000, 124,000]: 2.58%; (3) (124,000, 125,000]: 2.56%; (4) (125,000, 126,000]: 2.54%; (5) (126,000, 127,000]: 2.52%; (6) (127,000, 135,000]: 2.50%; (7) (135,000, 136,000]: 2.48%; (8) (136,000, 137,000]: 2.46%; (9) (137,000, 138,000]: 2.44%; (10) > 138,000: 2.43%.
The actual W is a published statistic that is not in the sources: any rate other than "given W" is NPF.
For rows J01 to J20 the rate is given as an input, 2.48%, except where stated.

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| J01 | Registration year, original price 150,000, rate 2.48% | 3,720 | in the registration year the adjusted price is the original price (def. (1)): 150,000 x 0.0248 = 3,720.0 | H |
| J02 | Price 177,777, rate 2.48% | 4,410 | 4,408.87 rounds to the nearest 10 | H |
| J03 | Price 180,000, rate 2.5% | 4,500 | exact | H |
| J04 | Price 178,600, rate 2.5% (4,465 exactly, a tie) | 4,470 | AMBIG: the tie is not resolved by the text; I take half-up | L |
| J05 | Tax year 2010, price 520,000, rate 2.6% | cap 450,000 applies: 11,700 | "לא יותר מסכום של 450,000" (adjusted to 2010 per the note) | M |
| J06 | Tax year 2010, price exactly 450,000, rate 2.6% | 11,700 | at the cap | M |
| J07 | Tax year 2010, price 450,001 | capped: 11,700 | cap | M |
| J08 | Tax year 2024, price 700,000 | cap exists but its 2024 value (563,790 in the note) is NPF | cap indexed each 1 January by reg 3, index not named in reg 3 | H (NPF) |
| J09 | Year after registration: original 200,000, average 210,000, exchange ratio 1, CPI ratio 1.03, rate 2.48% | adjusted price 1.03 x (200,000 + 10,000) = 216,300; value 5,360 | def. (2): 216,300 x 0.0248 = 5,364.24 | H |
| J10 | As J09, average 201,000 | difference 1,000 = 0.5% < 1%, so use 1.03 x 200,000 = 206,000; value 5,110 | proviso "נמוך בערכו המוחלט מ־1%": 5,108.8 | H |
| J11 | As J09, average 202,000 | difference 2,000 = exactly 1%, not lower than 1%: price 1.03 x 202,000 = 208,060; value 5,160 | strictly "נמוך": 5,159.888 | H |
| J12 | As J09, average 190,000 (below original) | difference = lower of (0) and (-10,000) = -10,000; 5% in absolute value: price 1.03 x 190,000 = 195,700; value 4,850 | "הפרש ההתאמה" is the lower; "בערכו המוחלט" implies negatives | M |
| J13 | As J09, average 200,500 (difference 0.25%) | 1.03 x 200,000 = 206,000: 5,110 | proviso | H |
| J14 | Exchange ratio 1.05 (revalued 210,000), average 212,000, original 200,000, CPI ratio 1.02 | revalued 210,000; (1) = 2,000, (2) = 12,000; difference 2,000 = 1.0%, not lower; price 1.02 x 202,000 = 206,040; value 5,110 | arithmetic 5,109.79 | H |
| J15 | Exchange-rate ratio computed as 0.97 | floored to 1 ("אך לא פחות מ־1") | def. | H |
| J16 | Registration year, average price differs from original | adjusted price is the original price | def. (1) | H |
| J17 | Model registered 1 Oct, list 200,000 for the first 50 days and 210,000 for the next 42 days (to 31 Dec = 92 days) | average price = (200,000 x 50 + 210,000 x 42) / 92 = 204,565.22 | "מחולק ... במספר הימים שחלפו מיום רישום הדגם ... עד סוף שנת המס" | H |
| J18 | Model registered in an earlier year; average over the registration year | divided by 365 | "365 או במספר הימים ..." | H |
| J19 | Imported-vehicle price with no parallel commercial import | customs value + duty + purchase tax + VAT + 1% per month of use abroad | def. "מחיר הרכב לצרכן" (2) and "פחת שימוש" | H |
| J20 | Month of availability partly used | AMBIG: the reg gives a value per month and does not prorate | reg 2(א) | L |
| J21 | W = 123,000 (CPI ratio 1) | 2.6% | tier 1 "אינו עולה על" | H |
| J22 | W = 123,001 (CPI ratio 1.000) | 2.58% | tier 2 | M |
| J23 | W = 124,000 / 124,001 / 125,000 / 125,001 | 2.58 / 2.56 / 2.56 / 2.54 | tiers 2-4 (CPI ratio 1) | M |
| J24 | W = 126,000 / 126,001 / 127,000 / 127,001 | 2.54 / 2.52 / 2.52 / 2.50 | tiers 4-6 | M |
| J25 | W = 135,000 / 135,001 / 136,000 / 136,001 | 2.50 / 2.48 / 2.48 / 2.46 | tiers 6-8 | M |
| J26 | W = 137,000 / 137,001 / 138,000 / 138,001 | 2.46 / 2.44 / 2.44 / 2.43 | tiers 8-10 | M |
| J27 | W unindexed 123,500 with CPI ratio 0.99 (indexed 122,265) | no tier applies: tier 1 tests the unindexed figure, tiers 2 to 10 the indexed one; AMBIG (a gap); expect refusal | tier (1) vs (2) | M |
| J28 | W unindexed 122,900, CPI ratio 0.99 | 2.6% | tier 1 | H |
| J29 | The current rate in force today (2.48% per the Tax Authority) | NPF: W is not in the sources | needs the published figure | H |
| J30 | L3 motorcycle, 2008 | 750 per month | reg 2(ב) (amount adjusted to 2008) | M |
| J31 | L3 motorcycle, 2026 | NPF (1,070 in the note only) | reg 3 indexation, index not named | H |
| J32 | Motorcycle of another class | AMBIG: reg 2(א) excludes only the motorcycle "כאמור בתקנת משנה (ב)" | reg 2 | L |
| J33 | The maximum price and the L3 amount are adjusted each 1 January and rounded to NIS 10 | yes, but the index is not named in reg 3 | reg 3 | H |

### Hybrid, plug-in and electric provisions (5776-2015 temporary provision)

Reductions apply after rounding: reg 2(א) is read as if after "מכפלה של 10 שקלים חדשים" came "בהפחתת N שקלים חדשים".
Periods: 2015-07-01 to 2021-12-31 ((ב), (ג), (ד)); 2022-01-01 to 2028-12-31 ((ב1), (ג1), (ד1), (ד2)).
Reductions: (ג)/(ג1) hybrid registered on or after the start day of the 2009 amendment regs (1 January 2010, per a note and the parallel 1 Jan 2010 window in reg 2(א)): 500; (ד)/(ד1) plug-in (and, 2015 to 2021, electric): 1,000; (ד2) electric from 2022: 1,200.
Reductions are indexed each 1 January and rounded to NIS 10 ((ו)): the nominal figures hold for 2015 and for 2022 respectively; later-year figures appear only in notes (NPF).
Rows use base value 4,960 (price 200,000 at 2.48%) unless stated.

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| K01 | July 2015, hybrid M1, registered 2012 | 4,460 | (ג): 4,960 - 500 | H |
| K02 | July 2015, plug-in M1, registered 2012 | 3,960 | (ד): 4,960 - 1,000 | H |
| K03 | July 2015, electric M1, registered 2012 | 3,960 | (ד) covers plug-in or electric | H |
| K04 | 2022, hybrid 1M, registered 2012 | 4,460 | (ג1) | H |
| K05 | 2022, plug-in 1M, registered 2012 | 3,960 | (ד1) | H |
| K06 | 2022, electric 1M, registered 2012 | 3,760 | (ד2): 4,960 - 1,200 | H |
| K07 | 2016 plug-in | NPF: the 2016 indexed reduction is not stated | (ו) | H |
| K08 | 2023 hybrid | NPF | (ו) | H |
| K09 | 2026 electric (1,380 in the note) | NPF | (ו) | H |
| K10 | Hybrid, month 2015-06-30 | no reduction: 4,960 | period starts 2015-07-01 | H |
| K11 | Hybrid, month 2015-07-01 | 4,460 | same | H |
| K12 | Hybrid, 2028-12-31 | reduction applies (amount NPF for 2028) | period ends 2028-12-31 | H |
| K13 | Hybrid, 2029-01-01 | no reduction: 4,960 | outside the period | H |
| K14 | Plug-in at 2022: also claims the hybrid reduction | no: reductions do not stack, 3,960 not 3,460 | (ה) | H |
| K15 | Plug-in with green score 100 and battery 3.1 kWh | plug-in, 3,960 | def. "רכב פלאג־אין" | H |
| K16 | Plug-in with green score 101 | only hybrid: 4,460 | "ציון ירוק שאינו עולה על 100" | H |
| K17 | Hybrid with battery exactly 3.0 kWh, score 90 | only hybrid: 4,460 | "העולה על 3 KWH" | H |
| K18 | Diesel hybrid | not a "hybrid" (spark-ignition engine required): no reduction | def. "המוצת בניצוץ" | M |
| K19 | Vehicle class M2 (not M1/N1), hybrid | no reduction | "סיווגו M1 או N1" | H |
| K20 | Electric, price 40,000 (value 990), 2022 | 990 - 1,200 = -210; AMBIG: floor at 0 is not stated; decided 0 | (ד2) | L |
| K21 | Hybrid registered 2009-12-31, 2022 | (ב1): reduction applied to the Schedule amounts; the Schedule is repealed ("תוספת (בוטלה)"): NPF/refusal | (ב1) | H |
| K22 | Hybrid registered 2010-01-01 | (ג) applies | "ביום התחילה ... או אחריו" | M |
| K23 | Hybrid registered 2009-12-31, 2015 | (ב): reduction of 500 from the Schedule amounts; Schedule repealed: refusal | (ב) | H |
| K24 | Electric registered before 1 Jan 2010, 2022 | no provision for this combination in (ד2) (registered on or after the start day only) | (ד2) | M |

## K. Section 2(2)(b): value of use of a mobile telephone (5762-2002 Regulations)

Text: monthly value = half the monthly expense or NIS 80, whichever is lower, minus the monthly expense the employee paid for that phone; excluded: a phone from which calls can be made only to the workplace; applies to expenses from 2002-05-01; amounts indexed and rounded to NIS 5 (the 80, not the half-expense).

| ID | Facts | Decided answer | Basis | Conf |
|---|---|---|---|---|
| L01 | 2002, monthly expense 100, employee paid 0 | 50 | half is lower | H |
| L02 | 2002, expense 160 | 80 | equal | H |
| L03 | 2002, expense 161 | 80 | cap lower than 80.5 | H |
| L04 | 2002, expense 159 | 79.5 | half not rounded | M |
| L05 | 2002, expense 200, employee paid 30 | 50 | 80 - 30 | M |
| L06 | 2002, expense 300, employee paid 100 | 0 | 80 - 100 negative, floored; AMBIG | L |
| L07 | Phone only able to call the workplace | 0 | exclusion | H |
| L08 | Phone not given for personal use | not "הועמד לרשות העובד": 0 | reg 1 | H |
| L09 | Expense 0 | 0 | | H |
| L10 | 2002, expense 120 | 60 | half | H |
| L11 | 2025, expense 100 | 50 (cap is at least 80) | half is lower either way | H |
| L12 | 2025, expense 400 | the cap for 2025 (115 in the note) is NPF | indexation | H |
| L13 | Expense incurred 2002-04-30 | outside the regs | reg 4 | H |
| L14 | Expense incurred 2002-05-01 | inside | reg 4 | H |
| L15 | Employee reimburses the full expense | 0 | deduction | M |

## Count

A 40, B 20, C 44, D 15, E 8, F 18, G 19, H 21, I 12, J 33 (+ the K tier and hybrid rows, 24), L 15, tier rows J21-J29 included in J.
Total decided cases: about 270 rows; the J23 to J26 rows each decide four boundary values.
