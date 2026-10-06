# IL-01 decided answers (independent test author, written before opening the encoding)

Finished: 2026-10-06T14:02:44Z (UTC, from `date -u`)

Written by the independent test author for row IL-01 from the Hebrew source alone, plus `BRIEF.md` for scope.
Before this file was finished I had read: the source bundle (sha256 `b87f2cf437ccfed35c3164681f4fc7ee015a111633454622751930c8894b81b6`, verified), the `second-pass.md` reference, the `writing-l4-rules` SKILL.md, and `BRIEF.md`.
I had NOT opened `NOTES.md`, `encoding.json`, `check.sh`, or any `.l4` file in the encoding directory (I saw their filenames in a directory listing only).

Line numbers below are lines of the source bundle file.

## The provisions as I read them

- **s 33A** (line 1561–1564), "בפרק זה":
  - ”נקודת זיכוי“ – "סכום של 504 שקלים חדשים ... לשנת מס, צמוד למדד כאמור בסעיף 120א, המקוזז כנגד המס לאותה שנה" (line 1563).
    A credit point is an annual amount of money per tax year, indexed; it is set off against that year's tax.
    The figures inside `{{ח:הערה|…}}` (2,820; 2,904) are Wikisource's and are not law.
    Note: s 33A points to s 120A for the index, but s 120A's ”מדד“ definition reads "(נמחקה)" (line 4329); the operative adjustment is s 120B(a) (line 4337ff), which is IL-03's. The value is therefore an input I choose.
  - ”נקודת קיצבה“ – "סכום השווה לסכום נקודת זיכוי כערכה ביום כ״א בטבת התשנ״ז (31 בדצמבר 1996), כשהוא מתואם לפי הוראות סעיף 120ב לענין נקודת קיצבה ומחולק בשנים עשר" (line 1564).
    An allowance point is (the credit point's 31-Dec-1996 value, as adjusted under s 120B for allowance-point purposes) divided by 12. The adjusted value is an input I choose; the division by twelve is the in-scope rule.
- **s 34** (line 1569–1570): "בחישוב המס של יחיד שהיה תושב ישראל בשנת המס יובאו בחשבון שתי נקודות זיכוי."
  Conditions: (i) יחיד — an individual, not a חבר בני אדם; (ii) "שהיה תושב ישראל בשנת המס". Result: 2 points.
- **s 36** (line 1593–1594): "בחישוב המס של יחיד תושב ישראל תובא בחשבון 1⁄4 נקודת זיכוי כזיכוי נסיעה."
  Conditions: יחיד, תושב ישראל. Result: 1/4 point. The heading ("זיכוי בעד נסיעה למקום ההשתכרות") speaks of travel to a place of earning, but the operative text has no work or travel condition.
- **s 36A** (line 1596–1597): "בחישוב המס של אשה תובא בחשבון 1⁄2 נקודת זיכוי."
  Condition: אשה. **No residence condition and no "יחיד"** — unlike ss 34 and 36. Result: 1/2 point.
- Read, not encoded, but they decide some answers:
  - s 1 "תושב ישראל" (line 143ff): for an individual, centre of life in Israel; a status assessed per tax year (presumptions "בשנת המס"). No notion of a part-year resident and no proration in ss 34/36.
  - s 1 "שנת מס" (line 202): twelve consecutive months from 1 January (or a special assessment period).
  - s 3A(f) (line 471): "יחולו על אזרח ישראלי שהוא תושב אזור או פועל באזור, הוראות פקודה זו כאילו היה תושב ישראל" — an Israeli citizen (s 3A(a) meaning, which includes a person entitled under the Law of Return who is an Area resident) who is an Area resident is treated as an Israeli resident for the whole Ordinance.
  - s 48 (line 1807): the Minister MAY by order apply ss 34, 36, 37 to Area residents who are not Israeli citizens "כאילו היו תושבי ישראל". Whether an order exists is outside the source (the Wikisource note on line 1808 is not law). s 48 does not mention s 36A.
  - s 48A (line 1811): the Minister MAY determine that the chapter's credit provisions "לא יחולו על עובד זר ... או שיחולו עליהם באופן חלקי ... אף אם רואים אותו כתושב". It can only remove or reduce credits, never add.
  - s 41 (line 1689–1692): a non-registered spouse married for part of the year gets, for unmarried months, 1/12 of the ss 34 and 36 points per month, and for married months 1/12 of the s 66 points per month. So ss 34/36 alone do not answer for that person.
  - s 66(c)(1),(4) (lines 2461, 2465): in a separate computation each spouse keeps ss 34/36 points and "האשה תהא זכאית ל־1⁄2 נקודת זיכוי לפי סעיף 36א". s 38 (line 1603) gives the registered spouse points for an included spouse. So for a woman whose income is in her registered spouse's joint computation, s 36A alone does not say whose computation the half-point enters.
  - s 57(a) (line 1870): a kibbutz (a cooperative society, hence a "חברה" and a body of persons) pays tax computed with "סעיפים 34 עד 46א ... בהתאם להרכב המשפחות של חברי הקיבוץ". So the bare "a body of persons gets no s 34 points" answer does not hold for a kibbutz.
  - s 134A(2) (line 4864): "סכום נקודות הזיכוי שעל פי סעיפים 34 ו־36" — the aggregate the brief names. It is 34 + 36 only; s 36A is not part of it.
  - s 120B(e)(1) (line 4344): amounts are not adjusted on 1 January of 2025–2027; they stay as on 1 January 2024 after rounding. (IL-03's; used only as a consistency check on published figures, S43.)
- Tax-year vintage: the bundle is a single "as amended" consolidation. The section headers list the amending Acts: s 34 last "תשל״ה־2" (1975); s 36 last "תשל״ז־4" (1977); s 36A last "תשנ״ו" (1995/96); s 33A last "תשס״ד־2" (2004). The text for a tax year before a section's last amendment is not in the bundle.

## Conventions for the scenarios

- Unless stated, the person is an individual; the tax year is 2026; residence is for the whole tax year; not a foreign worker; not an Area resident; separate (own) computation; not married part-year.
- V = the value of one credit point for the tax year (my chosen input, NIS per year).
- A = the credit point's value at 31 December 1996 as adjusted under s 120B for allowance-point purposes (my chosen input).
- "REFUSE" means the right result is a refusal with a reason, not 0, not FALSE.
- Confidence: H (high), M (medium), L (low). M and L are where I expect a reasonable encoder might differ.

## A. Points per section per kind of person (the answer table)

| id  | person                                                                 | s 34    | s 36    | s 36A   | total (34+36+36A) | 34+36 aggregate (s 134A(2)) | conf |
| --- | ---------------------------------------------------------------------- | ------- | ------- | ------- | ----------------- | ---------------------------- | ---- |
| S01 | resident man                                                           | 2       | 1/4     | 0       | 9/4               | 9/4                          | H    |
| S02 | resident woman                                                         | 2       | 1/4     | 1/2     | 11/4              | 9/4                          | H    |
| S03 | non-resident man                                                       | 0       | 0       | 0       | 0                 | 0                            | H    |
| S04 | non-resident woman                                                     | 0       | 0       | 1/2     | 1/2               | 0                            | H    |
| S05 | body of persons (company), resident                                    | 0       | 0       | 0       | 0                 | 0                            | H    |
| S06 | body of persons (company), non-resident                                | 0       | 0       | 0       | 0                 | 0                            | H    |
| S07 | resident man with no employment and no travel to work                 | 2       | 1/4     | 0       | 9/4               | 9/4                          | H    |
| S08 | resident girl aged 16                                                  | 2       | 1/4     | 1/2     | 11/4              | 9/4                          | M    |
| S09a| Israeli citizen, Area resident (not an Israeli resident under s 1), man | 2       | 1/4     | 0       | 9/4               | 9/4                          | M    |
| S09b| same, woman                                                            | 2       | 1/4     | 1/2     | 11/4              | 9/4                          | M    |
| S10 | Area resident, not an Israeli citizen, not an Israeli resident, man   | REFUSE  | REFUSE  | 0       | REFUSE            | REFUSE                       | H    |
| S11 | same, woman                                                            | REFUSE  | REFUSE  | 1/2     | REFUSE            | REFUSE                       | H    |
| S12 | foreign worker, regarded as Israeli resident, man                     | REFUSE  | REFUSE  | 0       | REFUSE            | REFUSE                       | H    |
| S13 | foreign worker, regarded as Israeli resident, woman                   | REFUSE  | REFUSE  | REFUSE  | REFUSE            | REFUSE                       | H    |
| S14 | foreign worker, non-resident, man                                      | 0       | 0       | 0       | 0                 | 0                            | M    |
| S15 | foreign worker, non-resident, woman                                    | 0       | 0       | REFUSE  | REFUSE            | 0                            | M    |
| S16 | individual resident for only part of the tax year (left Israel 30 June) | REFUSE  | REFUSE  | (by sex) | REFUSE           | REFUSE                       | M    |
| S17 | resident man, non-registered spouse, married for part of the year      | REFUSE  | REFUSE  | 0       | REFUSE            | REFUSE                       | M    |
| S18 | resident woman whose income is included in her registered spouse's joint computation | REFUSE  | REFUSE  | REFUSE  | REFUSE            | REFUSE                       | L    |
| S19 | resident individual whose sex is not stated                            | 2       | 1/4     | REFUSE  | REFUSE            | 9/4                          | H    |
| S20 | individual woman whose residence is not stated                         | REFUSE  | REFUSE  | 1/2     | REFUSE            | REFUSE                       | H    |
| S44 | kibbutz (cooperative society taxed under s 57)                         | REFUSE  | REFUSE  | 0       | REFUSE            | REFUSE                       | M    |

Licences and reasoning, row by row:

- **S01** s 34 "יחיד שהיה תושב ישראל בשנת המס ... שתי נקודות זיכוי"; s 36 "יחיד תושב ישראל ... 1⁄4 נקודת זיכוי"; s 36A "אשה" not met → 0, the law's own answer.
- **S02** as S01 plus s 36A "בחישוב המס של אשה תובא בחשבון 1⁄2 נקודת זיכוי". The s 134A(2) aggregate is "סעיפים 34 ו־36" only, so 9/4, not 11/4.
- **S03** s 34 and s 36 each require "תושב ישראל"; not met → 0 (the section does not apply; an ordinary value, per the brief).
- **S04** s 36A has no residence condition — "אשה" is the only condition → 1/2. ss 34/36 → 0. This is the cell I most expect an encoder to get wrong by importing a residence condition into s 36A.
- **S05/S06** ss 34 and 36 require "יחיד"; a body of persons is not one (s 1 "חבר בני אדם", "חברה"). s 36A: a company is not "אשה". All 0.
- **S07** the s 36 heading mentions travel to the place of earning; the operative words "בחישוב המס של יחיד תושב ישראל" carry no such condition → 1/4.
- **S08** no age condition in ss 34, 36, 36A (contrast s 40B, line 1652, which states an age band explicitly). I read "אשה" in s 36A as a female individual taxpayer of any age. M: a literal reader could say a 16-year-old girl is not an "אשה"; if so, REFUSE would be defensible, never 0.
- **S09** s 3A(f) applies the whole Ordinance to an Israeli citizen who is an Area resident "כאילו היה תושב ישראל" → s 34 = 2, s 36 = 1/4. M only because s 3A is outside the brief's read list; the words are plain. An encoding that REFUSEs here (lumping all Area residents under s 48) is refusing where the source answers.
- **S10/S11** s 48: whether ss 34 and 36 apply turns on a ministerial order that is outside the source; the brief also requires a named refusal. s 48 does not reach s 36A, and s 36A has no residence condition, so the woman still gets 1/2 and the man 0. The total and the aggregate refuse because they include a refusing term.
- **S12/S13** s 48A: "לא יחולו על עובד זר ... אף אם רואים אותו כתושב" — the chapter's credits for a foreign worker turn on regulations outside the source → REFUSE for ss 34, 36, and for s 36A when she is a woman. For a man s 36A is 0 whatever the regulations say, because s 48A can only disapply or partially apply, never grant.
- **S14/S15** a non-resident gets 0 under ss 34/36 before s 48A is reached, and s 48A cannot add credits → 0 is the source's answer. s 36A for a foreign-worker woman refuses (S13 reasoning). M because an encoder could reasonably refuse every foreign-worker question; that would be a refusal where the source answers, a minor finding.
- **S16** s 34 "שהיה תושב ישראל בשנת המס", s 36 "יחיד תושב ישראל": the s 1 definition makes residence a status for the year with no part-year concept, and ss 34/36 have no proration. Whether a person resident only until 30 June "was a resident in the tax year" (full 2 points), was not (0), or gets a prorated share is not answered by the source → REFUSE. M: the alternative literal reading is 2 full points (the person was a resident during the year). 0 would be wrong on either reading.
- **S17** s 41 replaces the plain ss 34/36 count with 1/12 per unmarried month plus 1/12 of the s 66 points per married month. Out of scope, but it changes the answer → REFUSE, never a bare 2.
- **S18** whose computation the s 36A half-point enters depends on ss 65/66/38 (IL-02, IL-08). L: I expect most encodings have no input for this; record as inexpressible rather than as a failure if so.
- **S19** s 36A cannot be decided without knowing whether the person is a woman → REFUSE for s 36A and for the total; s 34, s 36 and the 34+36 aggregate are answerable.
- **S20** ss 34/36 cannot be decided without residence → REFUSE; s 36A needs only "אשה" → 1/2.
- **S44** s 57(a) brings "סעיפים 34 עד 46א" into a kibbutz's computation by its members' family composition; the bare "a body of persons gets 0" is therefore not the whole answer → REFUSE for ss 34/36. s 36A: the kibbutz itself is not a woman → 0 for the kibbutz as such. M.

## B. Credit-point amounts (s 33A): points × V, no rounding stated

| id  | facts                                         | V     | expected amount                                     | conf |
| --- | --------------------------------------------- | ----- | --------------------------------------------------- | ---- |
| S21 | resident man                                  | 2,904 | total 6,534; s 34 part 5,808; s 36 part 726          | H    |
| S22 | resident woman                                | 2,904 | total 7,986; s 36A part 1,452                        | H    |
| S23 | non-resident woman                            | 2,904 | 1,452                                               | H    |
| S24 | resident man                                  | 2,903 | 6,531.75 exactly (2.25 × 2,903; no rounding in s 33A) | H    |
| S25 | resident woman                                | 3,000 | 8,250                                               | H    |
| S26 | company                                       | 2,904 | 0                                                   | H    |
| S27 | resident man, V not supplied                  | —     | amount REFUSE (or V is a required input); points 9/4 still answerable | H |
| S28 | one credit point                              | 2,904 | 2,904 (s 33A: a credit point is "סכום ... לשנת מס")  | H    |
| S29 | the statutory base sum, if exposed             | —     | 504 NIS ("סכום של 504 שקלים חדשים"), not a year's value | H |

Licence: s 33A ”נקודת זיכוי“ – "סכום של 504 שקלים חדשים ... לשנת מס ... המקוזז כנגד המס לאותה שנה". The money value of n points is n × that year's value; nothing in ss 33A–36A rounds it (rounding rules under s 120B(d) apply to the adjusted value V itself, which is my input).

## C. Set-off against the tax (s 33A "המקוזז כנגד המס לאותה שנה")

| id  | facts                                    | V     | tax before credits | expected                                                                 | conf |
| --- | ---------------------------------------- | ----- | ------------------ | ------------------------------------------------------------------------ | ---- |
| S30 | resident man                             | 2,904 | 20,000             | tax after set-off 13,466                                                  | H    |
| S31 | resident woman                           | 2,904 | 5,000              | tax after set-off 0, not −2,986; whether the unused 2,986 is refunded or carried is not answered (REFUSE if asked) | M |
| S32 | resident man                             | 2,904 | 0                  | tax after set-off 0                                                       | M    |

M on S31/S32: "מקוזז כנגד המס" (set off against the tax) cannot make the tax negative; "לאותה שנה" ties it to that year. Whether any excess is paid out is outside these words.
Only testable if the encoding exposes a set-off; otherwise record as not expressible.

## D. Allowance point (s 33A ”נקודת קיצבה“)

| id  | A (adjusted 1996 credit-point value) | expected allowance point                   | conf |
| --- | ------------------------------------ | ------------------------------------------ | ---- |
| S33 | 2,904                                | 242                                        | H    |
| S34 | 2,820                                | 235                                        | H    |
| S35 | 2,905                                | 2905/12 exactly (≈ 242.0833), no rounding  | M    |
| S36 | not supplied                         | REFUSE (or A is a required input)          | H    |

Licence: "סכום השווה לסכום נקודת זיכוי כערכה ביום ... (31 בדצמבר 1996), כשהוא מתואם לפי הוראות סעיף 120ב ... ומחולק בשנים עשר".
M on S35: s 120B(d) rounding rules might be argued to reach the result; nothing in s 33A rounds.
Note the allowance point is NOT one-twelfth of the current year's credit point value as such; it is one-twelfth of the 1996 value adjusted under s 120B "לענין נקודת קיצבה". An encoding that computes it as V/12 from the year's credit point value conflates the two (they coincide numerically only when the two adjustment paths coincide).

## E. The aggregate s 134A(2) names

| id  | facts           | V     | expected                                                                 | conf |
| --- | --------------- | ----- | ------------------------------------------------------------------------ | ---- |
| S37 | resident woman  | 2,904 | aggregate "נקודות הזיכוי שעל פי סעיפים 34 ו־36" = 9/4 points = 6,534 NIS; three times = 19,602 NIS (only if exposed) | H |

## F. Tax-year edges

| id  | facts                               | expected                                                                        | conf |
| --- | ----------------------------------- | ------------------------------------------------------------------------------- | ---- |
| S38 | resident man, tax year 2026         | 9/4                                                                             | H    |
| S39 | resident man, tax year 2024         | 9/4                                                                             | H    |
| S40 | resident man, tax year 1970         | s 34 REFUSE (last amended תשל״ה־2, 1975; earlier text not in the bundle); s 36 REFUSE (תשל״ז־4) | M |
| S41 | resident woman, tax year 1990       | s 36A REFUSE (last amended תשנ״ו); s 34 = 2 and s 36 = 1/4 (unamended since 1975/1977) | M |
| S42 | any person, tax year 1960           | REFUSE everything (before the 1961 New Version)                                 | H    |
| S43 | published figures, if a module states them per year | the values for 2025, 2026, 2027 equal the value for 2024 (s 120B(e)(1)) | M |

If the encoding takes no tax year at all, S38–S42 are not expressible; that is a finding of its own (an encoding that never asks the year cannot refuse a year the bundle does not carry).

## Where the source does not answer (the refusals, collected)

S10, S11 (s 48 order), S12, S13, S15 (s 48A regulations), S16 (part-year residence), S17 (s 41), S18 (ss 66/38), S19 (sex unknown), S20 (residence unknown), S27 (no V), S31 refund of excess, S36 (no A), S40–S42 (vintage), S44 (s 57 kibbutz).

Count: 45 scenario rows (S01–S08, S09a, S09b, S10–S44), of which 17 have a REFUSE in at least one cell.

---

## Revised after seeing the encoding (appended; nothing above this line was changed)

Everything above this section is the pre-encoding reading: the first 21,493 bytes of this file, sha256 `684306d6602ca9beb8f90b62f6977aa8c3554b716d71945f45710aeee9f75446` (check with `head -c 21493 DECIDED-ANSWERS.md | shasum -a 256`).
No expected value above has been changed. On reflection, after reading the encoding's modules and then `NOTES.md`, I now hold three of my expectations to be wrong or mis-aimed, and one to be stronger than I marked it:

- **S17 (s 41, spouse married part of the year), S18 (woman in a joint computation): my expectation was mis-aimed.**
  s 41 takes "1⁄12 מנקודות הזיכוי לפי סעיפים 34, 36" as a quantity, and s 66(c)(1),(4) applies "the points under s 34/36/36A" per spouse.
  The encoding's rules are named "the credit points under section N" and say expressly that they are not the person's total; that is the quantity ss 41 and 66 consume, and for it 2, 1/4 and 1/2 are correct.
  My REFUSE was aimed at the person's entitlement after ss 41/66/38, which this row does not claim to answer.
- **S44 (kibbutz, s 57): my expectation was wrong.**
  s 57(a) applies "סעיפים 34 עד 46א" in a hypothetical computation of the members' tax, by their family composition; it does not give the kibbutz itself, a body of persons, points under s 34.
  0 for the body of persons is right; the members' points are s 57's business.
- **S09 (Israeli citizen resident in the Area, s 3A(f)): I would now mark this H, not M.**
  s 48 itself says "'אזור', 'תושב אזור' ו'אזרח ישראלי' – כהגדרתם בסעיף 3א", so the s 48 / s 3A pairing is the statute's own: s 3A(f) carries Israeli citizens in the Area "כאילו היה תושב ישראל", and s 48 exists to let an order extend ss 34/36/37 to the non-citizens s 3A(f) leaves out.
