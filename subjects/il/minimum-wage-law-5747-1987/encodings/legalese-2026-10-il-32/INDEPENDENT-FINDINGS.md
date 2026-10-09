# Independent findings (IL-56, tester fid-il-32)

DECIDED-ANSWERS.md (83 cases) was written from the Hebrew source alone and frozen before the encoding was opened.
Its sha256 is dee0c2c8061f14382566aa8ddd7d35c80dc3fc9994899f8c9ca5e786e9b8e726.
Tests: tests-independent.l4, 68 assertions.
check.sh: 8 modules, 0 errors, tests-independent 63 satisfied and 5 refused (declared 0/5), exit 0.
l4 sha256 before and after: f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8.

## Disagreements

| # | Cases | Class | Finding |
|---|---|---|---|
| 1 | 1, 3, 4 | OURS-WRONG (scope hole) | The Law prints 525 from 1 April 1987 and 551 from 1 October 1987 (s 21(a), lines 175-176), and the encoding holds both as constants and asserts them. The dated entry point `the full monthly minimum wage ... on` DAY refuses for every date before 1 April 2025 ("no source held ... prints the full monthly minimum wage before 1 April 2025"), including 1 April 1987 to 30 September 1987 (525) and 1 October 1987 (551). A date in the window s 21 covers is answered by the Law's own text, not by a publication. The NOTES coverage table calls s 21 "encoded" but no date dispatch reaches it. Note that after 1 October 1987 s 21(a)(2) says it does not detract from s 4, so only 1 April to 30 September 1987 is certain; 1 October 1987 itself is certain at 551 unless a s 4 increase begins that day. |
| 2 | 6 | SCOPE | 1 April 2023 = 5,571.75 is printed in the Law's editorial note (line 23), not in the statutory text. The encoding declines it deliberately (header of mw-il32-published-figures.l4). I decided M confidence, so the refusal is defensible. |
| 3 | 45 | AMBIGUITY (trivial) | A 0% position: I decided 0; the encoding refuses a zero fraction. The text does not say whether a position of no fraction is a position. |
| 4 | 68 | AMBIGUITY, with a view | A combined wage (which already includes the cost-of-living supplement) plus a fixed supplement of 600, regular pay 5,000. I decided 5,600 (reading P): the wage is payable by component (1), so s 3(d) ("if the wage was not payable by components (1) and (2), or part of them") is not triggered, and s 3(b)(2) itself says the supplement counts only "if not included in the combined wage". The encoding's default declines; reading P gives 5,600 (tested and satisfied); reading L gives 5,000. I think reading L is hard to square with s 3(b)(2), because it makes the ordinary combined-wage case fall into s 3(d), but I did not rule it out: the words "או לפי חלק מהם" (or part of them) support L. Not a bug. |
| 5 | 69, 70 | AMBIGUITY | Overtime pay and employer pension contributions are not in the s 3(b) list. I decided they do not count (s 3(a) speaks of pay for a regular working day, and s 3(b) is a list). The encoding default declines (fork F3); with "it does not count" it agrees (tested and satisfied). |
| 6 | 13-15 | SCOPE | The s 4 increase (rates fixed in a general collective agreement, in force from the date the supplements start) has no entry point. The encoder says the increases arrive through the published figure; that is a reasonable choice, but a caller cannot ask "what is M after a 2% s 4 increase". My case 13 was L confidence in any event. |
| 7 | 73-83 | SCOPE | Pay on other bases (s 18(b)), supplementary daily and hourly rules (s 18(c)), penalty amounts (s 14, s 14A), the actual employer (s 6A) and the presumptions (s 7B) are not encoded. The encoder lists all of them as out of scope or refused by name. Accepted. |
| 8 | A4 | AMBIGUITY (source currency) | The deposited text says the hourly minimum is a 186th. My recollection, which I could not verify from the source, is that the official hourly rates (for example 30.61 for April 2023) correspond to a 182nd. Both the encoding and I follow the deposited Hebrew (hourly x 186 = M passes for 525, 551, 5,571.75, 6,443.85). If the 186 in the Wikisource consolidation is stale, every hourly answer and the F1 reading B (186 hours) is wrong together. Someone should check the official text or the Ministry's published hourly rates before relying on hourly figures. |

## Things that agree (tested and satisfied)

Monthly = 0.475 x average wage (13,566 to 6,443.85; 12,000 to 5,700; 11,730 to 5,571.75).
s 5: the larger of the old minimum and the updated figure, including equality.
Daily 25 and 21 2/3 divisors for 525, 551, 5,571.75, 6,443.85; five-day daily is larger than six-day daily.
Age: 18 and 40 covered, 17 and 15 refused to s 16 regulations, s 17 classes refused.
Part-time: 1/2 gives 3,221.925; 30 of 42 hours gives 4,602.75 on reading A and the default declines because 42 differs from 186.
Absence: 0, half, whole month, 2 of 22 days, and an arrangement payment.
s 3: every excluded kind adds nothing, a fixed supplement and a separate cost-of-living supplement count, case 67 totals 6,100 (shortfall 343.85), and a pay of 6,443.85 meets the minimum while 6,443.84 does not.

## The 47.5% question

The text does support the 47.5% reading of s 1 (line 23: "47.5 אחוזים מהשכר הממוצע כפי שהוא ב־1 באפריל של כל שנה וכפי שהוא מוגדל על פי חוק זה").
It supports it with three limits that the encoding mostly respects: the average wage is an input from the National Insurance Law, which is not deposited; the clause "as increased under this Law" means s 4 increases may sit on top; and s 5 means the formula figure is a floor-bounded update, which the encoding implements as a separate function but does not apply inside the dated lookup.
The consolidated text carries eight amendments to s 1, so for dates before the last amendment the 47.5% rule is not established by this text; the encoding sensibly gives no answer before 1 April 2025.

## Encoder reading of the source, checked line by line

The quoted Hebrew in the `src:N` comments matches the deposited file for the lines I compared (23, 24, 25, 28, 29, 30, 33-37, 40, 42, 147, 148, 151, 152, 174-176).
The only rendering difference is line 24, where the <sup>/<sub> markup of "21 2/3" is flattened to "21 2 ⁄ 3".
The 525 and 551 figures and the dates (1 April 1987, 1 October 1987) match lines 175 and 176.
The published 6,247.67 (from 1 April 2025) and 6,443.85 (from 1 April 2026) are not in the Hebrew source and I could not check them there.
6,443.85 = 0.475 x 13,566 holds exactly; 6,247.67 / 0.475 = 13,152.99, which the encoder notes is an implied average wage it holds no source for.
One note on my own sheet: case 7 labels the 13,566 case "1 April 2025"; the encoder pairs 13,566 with 1 April 2026. The arithmetic is unaffected; I treated the average wage as an input.
I found no misreading of the source by the encoder beyond the missing date dispatch for s 21 (finding 1).
