# IL-02 — Income Tax Ordinance s 66: answers decided from the Hebrew source alone

**Finished: Tue Oct  6 14:03:09 UTC 2026** (`date -u`). 101 scenarios. Nothing above the "Revised after seeing the encoding" section (if any) was changed after this time.

Written by the independent test author (fid-il-02) before opening any `.l4` file, `NOTES.md`, `encoding.json` or `check.sh` in the encoding directory.
Only `BRIEF.md` was read from that directory.

Source: `registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt`, sha256 `b87f2cf4…94b81b6` (verified), s 66 at lines 2454-2484.
Also read, for cross-references: s 1 definitions (lines 106-204, esp. 112-113 "בן זוג", "בן זוג רשום"; 170-178 "הכנסה מיגיעה אישית" (1)-(7); 202 "שנת מס"), s 33A (1561-1564), ss 34-40 (1569-1645), s 64B (2439-2445), s 65 (2447-2448).

## Conventions

- "Age in tax year Y" for a child born in calendar year b means `Y − b`: the age the child turns during tax year Y.
  A tax year is the calendar year (s 1 "שנת מס" – "תקופה של שנים עשר חדשים רצופים, שתחילתה ב־1 בינואר"); no special assessment period is assumed anywhere below.
  "Year of birth" (שנת לידה) is age 0, "year of majority" (שנת בגרות) is age 18, per s 40(b)(3): "”שנת לידה“ – שנת המס שבה נולד הילד; ”שנת בגרות“ – שנת המס שבה מלאו לילד שמונה עשרה שנים", incorporated by s 66(c)(4)(a) and the unlabelled tail of (c)(4).
- "Until the tax year in which he turned two" (ועד לשנת המס שבה מלאו לו שנתיים) is read **inclusively**: the next limb starts at "the tax year in which he turned three", so an exclusive reading would leave age 2 with nothing, which no limb supplies. Same for "until the tax year preceding the year of majority" (ages 6-17 inclusive).
- Inputs taken from outside s 66 are marked **[input]** with the section they come from. The one number I choose from the source is the value of a credit point for 2024-2027, **2,904 NIS**, from the editorial note in s 33A at line 1563 ("בשנים 2024–2027, 2,904 ש״ח"). I use it only in scenario C-CAP.
- Vintage: the brief says the text answers tax years from 2024 and refuses earlier ones; the source itself shows only the law at retrieval. I adopt that as my expectation for every pre-2024 tax year.
- Confidence: **H** = the words decide it; **M** = my reading of words that admit another; **L** = I expect a reasonable encoder to differ, and I would not call a disagreement an encoding error without more.

## V — vintage (tax-year scope)

| id | facts | expected | provision, Hebrew words | conf |
|---|---|---|---|---|
| V-1 | woman, separate calculation, tax year 2024, child born 2024 | 2½ child points | (c)(4)(a) "2½ נקודות זיכוי בעד כל אחד מילדיה בשנת לידתו" | H |
| V-2 | same facts, tax year 2023 | REFUSE | brief; source shows only the law at retrieval | H |
| V-3 | man, tax year 2027, child born 2020 (age 7) | 1 child point | (c)(5)(c) "נקודת זיכוי אחת … החל בשנת המס שבה מלאו לו שש שנים" | H |
| V-4 | non-registered spouse with employment income claims under (a)(1), tax year 2023 | REFUSE | brief | H |
| V-5 | man, tax year 2023, child born 2015 | REFUSE | brief | H |

## A1 — s 66(a)(1): who may claim, and on what income

All in tax year 2024, spouses within s 1 "בן זוג" (married, living together, joint household), no common source unless stated.

| id | facts | expected | provision, Hebrew words | conf |
|---|---|---|---|---|
| A1-1 | non-registered spouse claims; income is salary from employment by an unrelated employer | may claim: TRUE | (a)(1) "רשאי בן זוג שאיננו בן זוג רשום לתבוע כי ייעשה חישוב נפרד של המס על הכנסתו מיגיעה אישית … מעבודה" | H |
| A1-2 | non-registered spouse claims; income is self-employed business income from personal exertion | TRUE | (a)(1) "… מיגיעה אישית בעסק או משלח יד" | H |
| A1-3 | **registered** spouse claims under (a)(1) (both have employment income) | not under (a)(1): FALSE | (a)(1) the claimant is "בן זוג שאיננו בן זוג רשום" | H |
| A1-4 | non-registered spouse claims on ordinary rental income (not s 1 PE para (7)) or dividend income only | FALSE: not personal-exertion income | (a)(1) "על הכנסתו מיגיעה אישית" | H |
| A1-5 | non-registered spouse claims on rent within s 1 PE para (7) (property used ≥10 years in own business before letting) | TRUE | (a)(1) "לרבות הכנסתו מיגיעה אישית כאמור בפסקאות (1) עד (7) להגדרתה שבסעיף 1"; s 1 PE (7) | H |
| A1-6 | non-registered spouse claims on a retirement grant (s 1 PE para (5)) | TRUE (not a pension, so the proviso does not bite) | (a)(1) "(1) עד (7)"; s 1 PE (5) "מענק שנתקבל עקב פרישה" | H |
| A1-7 | non-registered spouse's income is a pension from a former employer (PE para (1)) paid in respect of employment income for which that spouse was entitled to a separate calculation | TRUE (proviso limb 1) | (a)(1) "ובלבד שלגבי הכנסה כאמור שהיא קיצבה ייעשה חישוב נפרד אם היא משולמת בשל הכנסת עבודה שלגביה היה בן הזוג שאיננו בן הזוג הרשום זכאי לחישוב נפרד" | H |
| A1-8 | pension; limb 1 false; the spouse was entitled to a separate calculation within the five years before the pension began, for the income by virtue of which it is paid | TRUE (proviso limb 2) | (a)(1) "או אם בן הזוג … היה זכאי בחמש השנים האחרונות שלפני תחילת תשלום הקיצבה לחישוב נפרד בשל ההכנסה שמכוחה משתלמת הקיצבה" | H |
| A1-9 | pension; neither limb holds | FALSE | (a)(1) proviso | H |
| A1-10 | pension; limb 1 false; last entitlement 5 years before the pension began (inside the window) | TRUE | (a)(1) "בחמש השנים האחרונות" | M (edge) |
| A1-11 | pension; limb 1 false; last entitlement 6 years before the pension began (outside) | FALSE | (a)(1) "בחמש השנים האחרונות" | H |

## D — s 66(d): common source of income

In each, the non-registered spouse claims under (a)(1) on income from the common source, tax year 2024.

| id | facts | expected | provision, Hebrew words | conf |
|---|---|---|---|---|
| D-1 | common source; both spouses' personal exertion required; each paid in direct proportion to contribution; income not produced in the home | (a) applies: TRUE | (d)(1) "רק אם התקיימו כל אלה" (a),(b); (c) not engaged ("אם ההכנסה מופקת בבית המגורים") | H |
| D-2 | as D-1 but one spouse's personal exertion is not required | FALSE | (d)(1)(a) "יגיעתו האישית של כל אחד מבני הזוג נדרשת" | H |
| D-3 | as D-1 but income does not correspond to / is not in direct proportion to contribution | FALSE | (d)(1)(b) "מקבל הכנסה התואמת את תרומתו … ועומדת ביחס ישיר לתרומתו" | H |
| D-4 | as D-1 but produced in the home; home serves the source permanently; most activity in the home | TRUE | (d)(1)(c) "בית המגורים משמש, דרך קבע, את מקור ההכנסה המשותף ומרבית פעילות … נעשית בבית המגורים" | H |
| D-5 | produced in the home; permanently; most activity NOT in the home | FALSE | (d)(1)(c) | H |
| D-6 | produced in the home; NOT permanently; most activity in the home | FALSE | (d)(1)(c) "דרך קבע" | H |
| D-7 | no common source (each employed by unrelated employers) | TRUE, (d) not engaged | (d)(2) "”מקור הכנסה משותף“ – מקור הכנסה של בן זוג התלוי במקור ההכנסה של בן הזוג השני" | H |
| D-8 | common source failing (d)(1)(a); the non-registered spouse ALSO has salary from an unrelated employer and claims (a)(1) on that salary | FALSE (literal: "subsection (a) shall apply to spouses who have a common source only if …" — the restriction attaches to the couple, not to the income) | (d)(1) "הוראות סעיף קטן (א) יחולו לגבי בני זוג שיש להם מקור הכנסה משותף, רק אם …" | L — a purposive reading confines (d) to the common-source income; s 64B(b) points that way ("למעט הכנסה ממקור הכנסה משותף לפי סעיף 66(ד) שלא מתקיימות לגביה הוראות אותו סעיף") |
| D-9 | common source failing (d); the spouse claims under (b) on income from property inherited during the marriage | TRUE: (d) restricts (a) only, and (b) is "על אף האמור בסעיף קטן (א)" | (d)(1) names "סעיף קטן (א)"; (b) | H |

## A2 — s 66(a)(2): where income not from personal exertion goes

Separate calculation in force (non-registered spouse claimed under (a)(1)), tax year 2024. "PE" = taxable income from personal exertion; "passive" = the spouses' taxable income not from personal exertion (both spouses' together).

| id | facts | expected | provision, Hebrew words | conf |
|---|---|---|---|---|
| A2-1 | registered PE 300,000; non-registered PE 200,000; passive 50,000 | passive goes to the registered spouse | (a)(2) "תיווסף ההכנסה החייבת שאינה מיגיעה אישית של בני הזוג להכנסה החייבת של בן הזוג שהכנסתו החייבת מיגיעה אישית גבוהה יותר" | H |
| A2-2 | registered PE 150,000; non-registered PE 250,000; passive 50,000 | passive goes to the **non-registered** spouse | (a)(2) "גבוהה יותר" — no preference for the registered spouse | H |
| A2-3 | registered PE 0; non-registered PE 100,000; passive 40,000 | to the non-registered spouse | (a)(2) | H |
| A2-4 | neither has PE income (separate calculation is under (b) only); passive 40,000 | to the registered spouse | (a)(2) "לא היתה לבני הזוג הכנסה חייבת מיגיעה אישית, יראו את ההכנסה שאינה מיגיעה אישית כהכנסת בן הזוג הרשום" | H |
| A2-5 | registered PE 200,000; non-registered PE 200,000 (a tie); passive 50,000 | REFUSE — "the spouse whose PE income is higher" does not exist, and the fallback limb is only for "no PE income" | (a)(2) "גבוהה יותר" | M |
| A2-6 | registered: PE 300,000, own passive 20,000; non-registered: PE 200,000, own passive 30,000 | registered spouse's taxable income for the calculation 350,000; non-registered 200,000 | (a)(2) "ההכנסה החייבת שאינה מיגיעה אישית **של בני הזוג**" (both spouses' passive pooled) | H |

## A3 — s 66(a)(3): a child's transparent-company, REIT, interest and capital-gain income

Separate calculation in force, tax year 2024.

| id | facts | expected | provision, Hebrew words | conf |
|---|---|---|---|---|
| A3-1 | child born 2007 (turns 17 in 2024), interest income 10,000 | counted as the registered spouse's income | (a)(3) "יראו את הכנסותיו של בן הזוג הרשום ככוללות גם הכנסות כאמור של ילדו שטרם מלאו לו בשנת המס 18 שנים" | H |
| A3-2 | child born 2006 (turns 18 in 2024), interest 10,000 | NOT counted: in 2024 the child did turn 18 | (a)(3) "שטרם מלאו לו בשנת המס 18 שנים" | M (edge: one could read "not yet 18 at some point in the year") |
| A3-3 | child born 2005 (turns 19), interest 10,000 | NOT counted | (a)(3) | H |
| A3-4 | child turns 10; capital gains 10,000 | counted | (a)(3) "מריווח הון" | H |
| A3-5 | child turns 10; income from a transparent company (s 64A1) | counted | (a)(3) "הכנסות מחברה שקופה כהגדרתה בסעיף 64א1" | H |
| A3-6 | child turns 10; income from a REIT (s 64A2) | counted | (a)(3) "הכנסות מקרן להשקעות במקרקעין, כהגדרתה בסעיף 64א2" | H |
| A3-7 | child turns 10; dividend income only | NOT counted under (a)(3): dividends are not listed | (a)(3) list | H |
| A3-8 | child turns 10; employment income | NOT counted under (a)(3) | (a)(3) list | H |
| A3-9 | child turns 10; linkage differentials (הפרשי הצמדה) | counted: "interest" has its s 65 meaning, which includes linkage differentials | (a)(3) "”ריבית“ – כמשמעותה בסעיף 65"; s 65 "מריבית, מדמי ניכיון או מהפרשי הצמדה (לענין סעיף זה – ריבית)" | H |
| A3-10 | non-registered spouse has the higher PE income; child (turns 10) has interest 10,000; spouses' own passive 50,000 | spouses' passive → non-registered spouse (a)(2); child's interest → **registered** spouse (a)(3) | (a)(2) vs (a)(3) "בן הזוג הרשום" | H |
| A3-11 | child turns 10; interest from assets the child inherited | counted: s 66(a)(3) imports only the *meaning* of "interest" from s 65, not s 65's exception for inherited or bodily-injury assets | (a)(3) "”ריבית“ – כמשמעותה בסעיף 65"; s 65's "אלא אם כן הנכסים … התקבלו בירושה" is not repeated in s 66 | L |

## B — s 66(b): income from pre-marriage or inherited property

Tax year 2024. Marriage date 2015-06-01 unless stated.

| id | facts | expected | provision, Hebrew words | conf |
|---|---|---|---|---|
| B-1 | non-registered spouse; property inherited in 2020 (during the marriage) | may claim: TRUE | (b) "בן זוג שהיתה לו הכנסה … מרכוש שקיבל בירושה בתקופת נישואיו, רשאי לתבוע שייעשה חישוב נפרד" | H |
| B-2 | property owned since 2013-06-01 (two years before marriage) | TRUE | (b) "מרכוש שהיה בבעלותו שנה לפני נישואיו" | H |
| B-3 | property acquired 2014-12-01 (six months before marriage) | FALSE | (b) "שנה לפני נישואיו" | H |
| B-4 | property acquired 2014-06-01 (exactly one year before marriage) | TRUE: owned on the day one year before marriage | (b) "שהיה בבעלותו שנה לפני נישואיו" | M (edge) |
| B-5 | property acquired 2014-06-02 (one day short of a year) | FALSE | (b) | M (edge) |
| B-6 | property received by gift during the marriage | FALSE: only inheritance qualifies during marriage | (b) "שקיבל בירושה" | H |
| B-7 | property bought during the marriage | FALSE | (b) | H |
| B-8 | property inherited 2015-03-01 (three months before marriage) | FALSE: not during the marriage, not owned a year before it | (b) both limbs | H |
| B-9 | **registered** spouse; property inherited during marriage | TRUE: "בן זוג", not limited to the non-registered spouse | (b) "בן זוג שהיתה לו הכנסה מרכוש" | H |
| B-10 | non-registered spouse has separately calculated salary 100,000 and claims (b) on 20,000 inherited-property income | one separate calculation on 120,000: the (b) income is added to the other separately calculated income | (b) "ובלבד שאם היתה לבן הזוג האמור הכנסה אחרת לגביה נערך חישוב מס נפרד, תיווסף ההכנסה על פי סעיף קטן זה להכנסה האחרת" | H |
| B-11 | non-registered spouse has no other separately calculated income; claims (b) on 20,000 | separate calculation on 20,000 alone | (b) | H |
| B-12 | registered PE 300,000 + other passive 10,000; non-registered PE 100,000 + (b) inherited-property income 20,000, claimed under (b) | registered 310,000; non-registered 120,000 — the (b) income does not go into the (a)(2) pool | (b) "על אף האמור בסעיף קטן (א)" | H |

## C — s 66(c): provisions applying to the separate calculation

Tax year 2024, separate calculation in force unless stated. Credit-point counts from ss 34, 35, 36, 37 are **[input]** (IL-01 and out of scope).

| id | facts | expected | provision, Hebrew words | conf |
|---|---|---|---|---|
| C1-1 | non-registered spouse, Israeli resident, separate calculation | her own s 34 (2) and s 36 (¼) points belong to her calculation [input values] | (c)(1) "הזכאות לניכויים, לזיכויים ולנקודות זיכוי לפי סעיפים 34, 35, 36 … יהיו לכל אחד מבני הזוג" | H |
| C2-1 | spouse is a "beneficiary individual" (יחיד מוטב) otherwise entitled under s 37 | ½ point, not 1 | (c)(2) "תובא בחשבון ½ נקודת זיכוי בלבד" | H |
| C2-2 | spouse otherwise entitled to s 38 (working spouse) or s 39 (helping spouse) points | 0 | (c)(2) "ולא תהא זכאות לנקודות זיכוי לפי סעיפים 38 ו־39" | H |
| C3-1 | non-registered spouse otherwise entitled to s 40(a) pension points | none | (c)(3) "זכאות לנקודות קיצבה על פי סעיף 40(א) תהא רק לבן הזוג הרשום" | H |
| C3-2 | registered spouse otherwise entitled to s 40(a) pension points | keeps them | (c)(3) | H |
| C4-0 | woman, no children | ½ point (s 36A) | (c)(4) "האשה תהא זכאית ל־½ נקודת זיכוי לפי סעיף 36א" | H |
| C-NONE | no separate calculation has been claimed or requested | s 66(c) does not apply: no s 66 child points | (c) "אלה ההוראות שיחולו לגבי החישוב הנפרד" | M |

### C4 — the woman's children's points, one child, tax year 2024

| id | child born | age in 2024 | expected points | limb |
|---|---|---|---|---|
| W0 | 2024 | 0 | 2½ | (4)(a) "2½ … בשנת לידתו" |
| W1 | 2023 | 1 | 4½ | (4)(a) "4½ … החל בשנת המס שלאחר שנת לידתו ועד לשנת המס שבה מלאו לו שנתיים" |
| W2 | 2022 | 2 | 4½ | same, inclusive |
| W3 | 2021 | 3 | 3½ | "3½ … בשנת המס שבה מלאו לו שלוש שנים" |
| W4 | 2020 | 4 | 2½ | "2½ … בשנות המס שבהן מלאו לו ארבע שנים וחמש שנים" |
| W5 | 2019 | 5 | 2½ | same |
| W6 | 2018 | 6 | 2 | "ושתי נקודות זיכוי … החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו" |
| W12 | 2012 | 12 | 2 | same |
| W17 | 2007 | 17 | 2 | same, last year |
| W18 | 2006 | 18 | ½ | "ו־½ נקודת זיכוי בעד כל אחד מילדיה בשנת בגרותו" |
| W19 | 2005 | 19 | 0 | no limb |

All H.

### C5 — the man's children's points, one child, tax year 2024

| id | child born | age in 2024 | expected points | limb |
|---|---|---|---|---|
| M0 | 2024 | 0 | 2½ | (5)(a) "2½ נקודות זיכוי בשנת לידתו של הילד" |
| M1 | 2023 | 1 | 4½ | (5)(b) "4½ … החל בשנת המס שלאחר לידתו ועד לשנת המס שבה מלאו לו שנתיים" |
| M2 | 2022 | 2 | 4½ | same, inclusive |
| M3 | 2021 | 3 | 3½ | (5)(b) "3½ … בשנת המס שבה מלאו לו שלוש שנים" |
| M4 | 2020 | 4 | 2½ | (5)(b) "2½ … בשנות המס שבהן מלאו לו ארבע שנים וחמש שנים" |
| M5 | 2019 | 5 | 2½ | same |
| M6 | 2018 | 6 | 1 | (5)(c) "נקודת זיכוי אחת … החל בשנת המס שבה מלאו לו שש שנים ועד לשנת המס שקדמה לשנת בגרותו" |
| M17 | 2007 | 17 | 1 | same, last year |
| M18 | 2006 | 18 | 0 | (5) has no year-of-majority limb |
| M19 | 2005 | 19 | 0 | no limb |
| M-36A | man, no children | 0 (no s 36A half point: (c)(4) gives it to "האשה") | (c)(4), (c)(5) |

All H.

### C4(a1) — the mother's election to move one birth-year point

| id | facts | expected | provision | conf |
|---|---|---|---|---|
| E-1 | mother, child born 2024, no election; tax year 2024 / 2025 | 2½ / 4½ | (4)(a) | H |
| E-2 | mother, child born 2024, elects to move one point; tax year 2024 / 2025 | 1½ / 5½ | (4)(a1) "אמו של ילד תהיה זכאית לבחור אם נקודת זיכוי אחת מתוך נקודות הזיכוי שלהן היא זכאית … בשנת הלידה, תובא בחשבון בשנת המס שבה נולד הילד או בשנת המס שלאחריה" | H |
| E-3 | father, child born 2024, purports to elect; tax year 2024 / 2025 | 2½ / 4½ — the election is the mother's only | (4)(a1) "אמו של ילד"; it sits under (4), not (5) | H |
| E-4 | mother, child born 2023, elected in 2023 to move one point into 2024; tax year 2024 | REFUSE: whether the 2023 point existed and could be moved is 2023 law, which the source does not show | brief; (4)(a1) | L — one could read the 2024 text as answering 4½ + 1 = 5½ |

### C4A / C6 — step-children

| id | facts | expected | provision | conf |
|---|---|---|---|---|
| S-1 | woman married to a **widower**; his child (not hers), age 7 in 2024 | 2 (woman's table) | (4A) "בחישוב המס של אישה שנישאה לאלמן יובאו בחשבון נקודות זיכוי בעד כל אחד מילדיו, כאמור בפסקה (4)" | H |
| S-2 | woman married to a **divorced** man; his child (not hers), age 7 | 0 | (4) "ילדיה"; (4A) needs "אלמן" | H |
| S-3 | man married to a **widow**; her child (not his), age 4 | 2½ (man's table) | (6) "בחישוב המס של גבר שנישא לאלמנה יובאו בחשבון נקודות זיכוי בעד כל אחד מילדיה, כאמור בפסקה (5)" | H |
| S-4 | man married to a **divorcée**; her child (not his), age 7 | 0 | (5) "ילדיו"; (6) needs "אלמנה" | H |
| S-5 | man married to a widow; her child age 7 | 1 (man's table, not 2) | (6) "כאמור בפסקה (5)" | H |

### Mixed families and the cap on children's points

| id | facts | expected | provision | conf |
|---|---|---|---|---|
| MIX-W | woman, own children aged 0, 3, 10, 18 in 2024 | children's points 2½+3½+2+½ = 8½; with s 36A ½ = 9 | (c)(4) | H |
| MIX-M | man, the same children | 2½+3½+1+0 = 7 | (c)(5) | H |
| MIX-S | woman married to a widower: her own child age 1, his child age 7 | 4½ + 2 = 6½ children's points; + ½ = 7 | (4), (4A) | H |
| C-CAP | woman, 2024, one child age 1 (4½ points × 2,904 = 13,068 NIS); tax on her income from personal exertion 10,000 NIS [input, s 121, IL-03] | the children's points offset at most 10,000 NIS; they cannot reduce tax on other income | (c)(4) "וכנגד המס החל על הכנסתה מיגיעה אישית"; (c)(5) "כנגד המס החל על הכנסתו מיגיעה אישית" | M — the ordering of other credits is not in s 66 |

### C1A — the separate calculation where the other spouse has no personal-exertion income

| id | facts | expected | provision, Hebrew words | conf |
|---|---|---|---|---|
| R1A-1 | woman (non-registered) with salary; husband (registered) has no PE income | may request; children's points per (4) | (c)(1A) "בן זוג רשאי, אף אם לבן זוגו אין הכנסה מיגיעה אישית, לבקש חישוב נפרד על הכנסתו מיגיעה אישית, ויהיה זכאי … לנקודות זיכוי כאמור בפסקאות (4) או (5)" | H |
| R1A-2 | man who is the **registered** spouse, with salary; wife has no PE income | may request; children's points per (5) | (c)(1A) "בן זוג" — not limited to the non-registered spouse | M |
| R1A-3 | requesting spouse has no PE income | cannot request: there is no "הכנסתו מיגיעה אישית" to calculate | (c)(1A) | H |
| R1A-4 | registered spouse with salary; the other spouse also has PE income; registered spouse requests under (1A) | may request — "אף אם" is "even if", not "only if" | (c)(1A) | L |

## R — where the source does not answer, and the right result is a refusal

| id | facts | expected | why | conf |
|---|---|---|---|---|
| R-1 | any s 66 question for tax year 2023 (V-2, V-4, V-5) | REFUSE | brief; the source shows only the law at retrieval | H |
| R-2 | (a)(2) tie (A2-5) | REFUSE | "גבוהה יותר" names no one on a tie; the fallback is for "no PE income" only | M |
| R-3 | a couple of two women, or two men, each with personal-exertion income and a child of both, separate calculation | REFUSE for which table applies to which spouse | (c)(4) "האשה" and (c)(5) "הגבר" presuppose one woman and one man; the text does not say what a same-sex couple gets | L |
| R-4 | deferred birth-year point from a 2023 birth (E-4) | REFUSE | depends on 2023 law | L |

## Notes on what I decided not to assert

- Survivors' pensions (s 1 PE para (3)) under the (a)(1) proviso: limb 1 speaks of employment income "for which the non-registered spouse was entitled to a separate calculation", which for a survivor's pension is the deceased's income, not the claimant's. The source does not clearly say how the proviso reads for them; I note it and do not assert it.
- Whether a commuted pension (PE para (6)) is "a pension" (קיצבה) for the proviso: not asserted.
- A child born after the tax year (negative age): not a child of the parent in that year; I would expect 0 or an invalid-input answer, and do not assert a single value.
- Same-sex couples (R-3) are asserted only if the interface can express the sex of each spouse.

## Revised after seeing the encoding

Appended after the encoding's `.l4` modules were read and `tests-independent.l4` was run; nothing above this heading was changed, and **no expected value was changed**.
These notes record only how a scenario was expressed through the encoding's interface.

- **V-2.** "Same facts, tax year 2023" literally puts a child born in 2024 into tax year 2023, before the child exists. The expectation (REFUSE) does not depend on the child, so the test asserts it twice: with the child born 2024 and with the child born 2023.
- **D-8.** The interface cannot tie an item of income to the common source (`common source of income` sits on the couple, not on an item), so D-8's inputs are identical to D-2's. It is asserted, but it cannot distinguish the two readings of (d)(1).
- **E-3.** The only election input is `the mother elects to count one birth-year credit point in the following tax year`, on the child; "the father purports to elect" is expressed by setting that flag and checking the man's points do not move.
- **R1A-1, R1A-2, R1A-3, A2-3, A2-4.** "No PE income" is expressed as a salary item of 0, which the encoding sums to 0 personal-exertion income.
- **Not expressible** (12): A1-10, A1-11 (the five-year window is a BOOLEAN input); A3-7, A3-8 (no field for a child's dividends or employment income); A3-9 (no field separating linkage differentials from interest); A3-11 (no field recording an inherited asset); B-3 to B-8 (whether property qualifies under (b) is supplied pre-sorted into the two (b) fields).
