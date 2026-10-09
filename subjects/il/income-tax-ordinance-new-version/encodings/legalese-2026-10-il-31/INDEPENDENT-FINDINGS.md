# INDEPENDENT-FINDINGS for IL-31 (fid-il-31)

DECIDED-ANSWERS.md was written from the Hebrew page images and frozen before any encoding file was opened.
sha256 of DECIDED-ANSWERS.md: fa8af1300b4c422842e26d8a0df0f6725cfe1c2df1be20896c4f060ffa738b5b.
l4 sha256 before and after: f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8 (unchanged).
check.sh: 6 modules, 0 errors, 182 satisfied, 0 failed, 1 refused (declared); tests-independent.l4 has 69 assertions, 68 satisfied and 1 declared refusal; exit 0.
check.sh was edited only to add `expected_refused` (one declared refusal for tests-independent.l4, line D16).

## Result

- 89 decided cases; 69 assertions in tests-independent.l4 cover those the encoding's entry points can be asked.
- No OURS-WRONG finding.
- Every figure, date and quoted Hebrew phrase of the encoding that I checked against the page images agrees with the Acts (list below).

## Disagreements

| id | what | class | detail |
|---|---|---|---|
| D16 | tax year 2024, s 121B entry: I decided (a1) = 0 and the (a) charge applies, 8,353.2 on capital 1,000,000; the entry REFUSES | TESTER-WRONG | s 3(ב) reads "הכנסה שהופקה או התקבלה ביום התחילה ואילך": income produced in 2024 but received on or after 1 January 2025 is inside (a1) and the Act does not say to which tax year it belongs. I scored H; it is M at best. The refusal is the careful answer. The refusal is asserted as my value so that the declared expected refusal stays visible. |
| B07 | SH 2972, child born 2009, no reading named: I decided out (0, M); the default declines | AMBIGUITY | I flagged the same ambiguity (DECIDED flag 1). With the reading named ("counted in tax years") the encoding gives 0, as I decided. Default refusal asserted. |
| A30, A31 | the mother's (4)(a1) election to defer one birth-year point (and the father's lack of it) | SCOPE | the entry is named "before any election under (4)(a1)"; the election is not encoded, and no deposited Act enacts it. Not testable. |
| B10, B11 | the SH 2972 point for single-parent parents under s 40(c)(1),(2) | SCOPE | s 40 is out of the row's scope by its own brief; the (4)(d) and (5א) paragraphs are encoded. |
| B12 to B15 | the toddler boundary | SCOPE | the encoding takes the toddler flag from the caller (a missing input, not a refusal). I decided refusal for cohorts 2015 to 2022 when the flag is unknown; the caller-supplied design answers with the flag given, which is consistent with my B05, B06, B09, B15 (all "not a toddler"). The caller must supply the flag. |
| C01 to C13 | commencement and publication dates | SCOPE | the encoding exposes only: the first tax year 2024, SH 2972 for 2022 only, and the 121B(a1) date function; the other dates (28 Tevet 5782, 20 Tevet 5784, 1 Tevet 5785, the publication days) appear in comments only. The three exposed ones agree with me. |
| D13, D14 | timing of income produced or received; capital income greater than total | SCOPE | no input can express either; D14 inconsistency is not checked (a capital item always is part of the items). |
| D19 to D21 | tax years 2026 to 2028 | SCOPE | answered by row IL-03; the 2025 module refuses 2026 and later by name. 2028 needs the 2027 index. |

## What agreed

- The s 66(c)(4)(a) and (5) ladders for tax years 2024 to 2026 (cases A01 to A29, A32): all 30 satisfied, mother and father, both sides of every age boundary (0, 1-2, 3, 4-5, 6-17, 18, 19; no majority-year point for the father; none before birth).
- Refusals for 2021, 2022 and 2023 (B01 to B04).
- The SH 2972 increment: 2010, 2012, 2014 born +1 (woman, man); 2008 born 0; 2009 with the named reading 0; none in 2021, 2023, 2024, 2025, 2026.
- s 121B total of (a) and (a1) for 2025 at T = 721,560: D01 to D12, D23, D24, D26 all agree to the agora; the strict "עלתה על" at exactly 721,560; capital income tested alone; salary and pension excluded; a residential sale of 5,000,000 not counted; 6,000,000 counted.

## What the encoder quotes, checked against the page images

- SH 2972 s 1(2)(א),(ב),(ג): "אשר בשנת 2022 טרם מלאו לו שלוש עשרה שנים והוא אינו פעוט כהגדרתו בסעיף 40(ב)(3)" and the period 28 Tevet 5782 to 7 Tevet 5783 match p. 844.
- SH 3184 s 1(2) ladder and s 3 (1 January 2024) match p. 630 and p. 634.
- SH 3342 s 1(2)(ג) text of (a1), s 3(א) (1 Tevet 5785) and s 3(ב) match pp. 150 and 152; 5,385,285 matches p. 151 and the text layer.
- The encoder's comment says "s 120B(e)(1)" for the Hebrew (ה)(1); that is a letter convention, not an error.
- The consolidation's definition of "הכנסה חייבת" prints "המדד שפורסם ביום המדד שפורסם ביום ז׳ בשבט התשפ״ז" (the phrase is doubled); the Act has it once. The encoder quotes the consolidation line as it is; harmless.

## My own errors, for the record

- DECIDED-ANSWERS section 0.1 cites the s 40(b)(3) definitions at consolidation lines 1648-1649; they are lines 1644-1645 (the encoder's citation is right). Frozen, not edited.
- D16 as above.
