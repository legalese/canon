# Independent findings, row IL-28 (fid-il-28, IL-56)

DECIDED-ANSWERS.md (72 cases, sha256 `93c38b1feaad58af0894a9f84bff8b92a5c6e1509adedf2602aca4aea59ec2d8`) was written from the Hebrew sources alone and frozen before any file of this directory other than the listing was opened.
The tests are `ito-il28-tests-independent.l4`: 89 assertions, 84 satisfied, 5 refused, 0 failed.
`check.sh` exits 0 with the five refusals declared (`expected_refused`, lines named in its comment).
l4 sha256 before and after: `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8`.

## Agreement

Every whole-year and part-year figure agrees with the encoding: caring man 2.25, caring woman 2.75, other legal man 1, other legal woman 1.5, one twelfth per month (11/48, 121/48, 1/12, 7/12 checked exactly), the money at 2,820 (2023) and 2,904 (2024-2027), the disapplication of s 37 and s 36 for foreign workers, income outside s 2(1)/(2) giving 0, every reg 2 failure (unlawful stay, unlawful work, expert, no B/1) giving 0, the 2015-2018 and 2014 refusals, the OV refusal, the Area man's 2.25, s 37 adding 1 only with all facts, the citizen and Law of Return exclusions.
Where I decided a reading the encoding declines by default (F1 for an Area woman, F4, FW1), the test names the reading and agrees.

## Disagreements

| id | my case | encoding | class | note |
| --- | --- | --- | --- | --- |
| D1 | A18, A18b: Area man, tax years 1995 and 2016, 2.25 | refuses (s 3A held only from 2017; the Order's start within 1995 not held) | AMBIGUITY | The Order (ORD line 15) has no commencement clause and s 48 does not condition on s 3A's later amendments. I took 1995 on, flagged L. The encoder gates on the last amendment of s 3A (תשע״ו־22). Both are defensible; the text does not decide. |
| D2 | A19 (2022), A15 (2022 money): Area man, tax year 2022 | refuses, because s 37 is held only from 2023 and the total includes s 37 | SCOPE | The encoding offers the 34+36+36A alone function for 2017-2022, so the answer exists there (2.25); only the total refuses. A taxpayer with no s 37 facts could still be answered; that is an over-refusal but not a wrong figure. |
| D3 | A11: Area resident who is also an Israeli resident, 2.25 | refuses: neither instrument reaches him | SCOPE | He is an "אזרח ישראלי" (s 3A(a)(2)), so the Order does not reach him; ss 34+36 apply by their own words, which is IL-01's row. My 2.25 was an out-of-scope baseline. |
| D4 | A12: company with Area residence | refuses (neither instrument reaches) | SCOPE | I wrote 0 in DECIDED-ANSWERS and asserted the refusal in the test; no disagreement in substance (a body of persons gets no point). |

No OURS-WRONG and no TESTER-WRONG finding.

## What the deposited text cannot answer (agreed)

- Regulations, tax years 2015-2018: the consolidation lists amendments of 5777 and 5778 whose commencement is not deposited (both of us refuse).
- Tax years before 2015 for a foreign worker: reg 4 (both refuse; the encoding adds fork FW2).
- Money in any year other than 2023-2027: the value is an input here, and the text states it only for those years.

## Reading of the source by the encoder

I checked the quoted Hebrew (`hebcheck.py` reports 37 quotations verified), the Order's date (1 March 1995), the regulation amendments cited (K.T. 5777 p. 472, 5778 p. 2656), the credit-point values (2,820 for 2023; 2,904 for 2024-2027) and reg 3(א)-(ד) against the source files line by line.
I found nothing misread.
One point worth a domain expert: the encoder's note that reg 3(ג) multiplies the whole sum including s 36A (N6) is right on the words, and agrees with my 11/48 and 121/48 figures.
