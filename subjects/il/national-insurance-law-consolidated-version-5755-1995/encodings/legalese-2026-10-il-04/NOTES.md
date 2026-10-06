# NOTES — il/national-insurance-law-consolidated-version-5755-1995, encoding row `legalese-2026-10-il-04`

National Insurance Law [Consolidated Version], 5755-1995: **s 334** (interpretation for Chapter 15, insurance contributions), **s 337** (the rate of insurance contributions), **Schedule J** (לוח י׳, the rates), and the **s 1** definitions they use, encoded in L4 by one agent in one session (run `IL-04-20261006`, 2026-10-06), from the brief in `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought.

## 0. What `check.sh` prints

Run on 2026-10-06 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, which resolves to the cabal store entry `jl4-0.1-0ee0100b` (modified 2026-10-06 21:20 local), sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
The binary has no `--version`, and no record beside it names the commit it was built from.

```
module                                    errors satisfied  failed  refused  expected
nii-il04-nouns.l4                              0         0       0        0         0
nii-il04-published-figures.l4                  0         0       0        0         0
nii-il04-tests-expected-red.l4                14        26      14        0        14
nii-il04-tests.l4                              0       120       0        0         0
nii-s1-definitions.l4                          0         0       0        0         0
nii-s334-interpretation.l4                     0         0       0        0         0
nii-s337-rates.l4                              0         0       0        0         0
nii-schedule-j-tables.l4                       0         0       0        0         0
nii-schedule-j.l4                              0         0       0        0         0
TOTAL (9 modules)                             14       146      14        0
```

`check.sh` exit 0.
The 14 errors are the 14 failed assertions of `nii-il04-tests-expected-red.l4`, which `check.sh`'s `expected_failed` table and `encoding.json`'s `expected_red` both name with that count; there is no other error.
They were predicted before that module was first run, and the run failed exactly those 14, read line by line from the diagnostics (none is "could not be evaluated"):

- **10 of 36 totals checks.** Schedule J's printed totals row does not equal the sum of the items above it in these cells:
  - temporary version, as printed: column C above the threshold, employee (printed 14.50, items 14.39); column D upper part (7.00, items 4.67);
  - temporary version, as read in 2024-2027: the same two (14.60 against 14.49; 7.00 against 4.67);
  - permanent version, as printed: column C above, employee (14.50 against 14.39); column C not above, employee (3.85 against 4.16); column D upper part (7.00 against 4.67);
  - permanent version, as read in 2024-2027: the same three (14.60 against 14.49; 3.95 against 4.26; 7.00 against 4.67).
  The other 26 cells agree.
- **4 of 4 composites above the threshold.** The National Insurance Institute's rate pages print, for 2026, composites the items of the 2026 version do not reach: employee 14.6% (items 14.49); employee's deduction 7% (items 4.67); controlling shareholder 14.17% (items 14.12); controlling shareholder's deduction 6.79% (items 4.46).

Both families are findings about the source, not defects of the encoding (fork F4, open questions 1-2).
`nii-il04-tests.l4`: 120 assertions, 120 satisfied. The first 116 were satisfied on the first run that evaluated them; four more were added after it, when ss 341 and 343 were found to displace s 337 (three refusals, and one check that the s 343 flag leaves a case without the work-injury branch at its ordinary 306.2999), and were satisfied on their first run. No expected value was changed after any run.
(Before that run, four test helpers were renamed because they used a parameter name as a mixfix keyword, and two self-employed boundary scenarios were corrected to test the boundary their comments named: 11.9 hours became 19.9, and an income of 2,034.89 became 6,782.99.)

Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.

**The harness can fail.** In a scratch copy, two expected values in the tests module were altered (306.2999 to 306.3; 333 to 334): `check.sh` reported 2 failed and exited 1.

**Mechanical checks** (scripts in `tools/`, run with `python3 -I`):

- `tools/srcquote.py SOURCE FILE.l4…` regenerates every `-- src:N | …` comment from line N of the source; re-running it over every module changed nothing.
- `tools/schedule_j.py SOURCE OUT.l4` generates `nii-schedule-j-tables.l4` from the two tables of Schedule J; re-running it (then `srcquote.py`) reproduces the deposited module byte for byte. It stops on any cell whose shape it does not recognise.
- `tools/hebcheck.py SOURCE FILE…` checks that every run of Hebrew outside a `src:` line occurs verbatim in the source; it passes on every `.l4` module, `BRIEF.md`, this file and `encoding.json`, and fails on a planted invented string.

The convention for the first and last of these follows row `legalese-2026-10-il-03` of the Income Tax Ordinance; these copies are self-contained and also reduce the schedule templates that row did not meet.

## 1. What is encoded and what is not

**Encoded:** s 334(a), its three definitions and both update paragraphs, and s 334(b); s 337(a)(1), (a)(2), (b) and (c); Schedule J in full, both tables, all ten items, all nine figure columns and both totals rows, with the 2024-2027 figures the editors note in item 4 and the totals; and from s 1, "employee" (with "employer"), "self-employed person", "the average wage" (with "compensation", "the compensation rate" and "update day"), "the index", "tax year" and "the Minister".

**Years answered:** contribution months from **January 2026** (assumption A1).
For 2026 the encoding computes a contribution end to end, using the reduced collection threshold the Institute publishes; for 2027 and later it computes from a threshold the caller supplies, and declines by name to supply one itself.

**Not encoded:** who pays which branch (s 335); what counts as income and its maximum, minimum and exemptions (ss 344-351, s 348 and Schedule K, row IL-05); the employer's deduction (s 342, row IL-05); the special work-injury and maternity rates (s 340); the reduced rates by order (s 341) and the reduced work-injury contributions of large employers (s 343), each of which declines a case it reaches; the payment period (s 336); s 2's adjustment of the average wage; Schedule A; the Treasury allocation (s 32).
Each of these that feeds a provision in scope enters as an **input**, with its citation in the nouns module.

**Figures not in the text** come from the National Insurance Institute's own pages, fetched 2026-10-06 with sha256 recorded (section 7): the 2026 reduced collection threshold (7,703) and the 2026 average wage (13,566 under s 1; 13,769 under s 2).
The consumer price index could not be fetched; it is an input with no default.

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`.

**Totals.** s 334, s 337 and Schedule J: **24 encoded, 3 inert, 0 out-of-scope, 0 deferred** (27 rows).
s 1: **9 encoded** (of which 4 as inputs or input conventions), **60 out-of-scope**, 0 deferred (69 rows, one per definition line).
Provisions outside the slice that the slice refers to, or that displace it: **14 out-of-scope** rows, each with its reason.
Altogether **33 encoded, 3 inert, 74 out-of-scope, 0 deferred**.

### s 334, s 337 and Schedule J

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| Chapter 15 heading, Sign A heading | 3598-3599 | "Chapter 15: insurance contributions", "Sign A: general provisions" | inert | `src:` comment heading `nii-s334-interpretation.l4` |
| s 334 heading and amendment tag | 3601 | interpretation; tag תשפ״ה־7 | encoded (as the vintage boundary) | `section 334(a) as it stood before 1 January 2026 is not in the deposited text` |
| s 334(a) chapeau | 3602 | "in this Chapter –" | inert | comment; the module is the Chapter's interpretation |
| s 334(a) "תקופת תשלום" | 3603 | payment period | encoded (a carrier of words) | `s 334(a) — "payment period"` |
| s 334(a) "מועד תשלום" | 3604 | payment date | encoded (a carrier of words) | `s 334(a) — "payment date"` |
| s 334(a) "מדרגת גבייה מופחתת" | 3605 | 7,522 NIS, updated on 1 January each year | encoded | `the sum printed in section 334(a)`, `s 334(a) — the reduced collection threshold for a month in` |
| s 334(a) "מדרגת גבייה מופחתת" (1) | 3606 | 2026-2028: by the rise in the index | encoded | `s 334(a)(1) — the threshold on 1 January of` |
| s 334(a) "מדרגת גבייה מופחתת" (2) | 3607 | from 2029: by the rise in the average wage | encoded | `s 334(a)(2) — the threshold on 1 January of` |
| s 334(b) | 3608 | wage fixed by a Law or Knesset resolution: an employee; the payer the employer | encoded (the employee limb; the employer limb is a fact, F14) | `s 334(b) — the person is an employee for Chapter 15` |
| s 337 heading and tags | 3625 | rate of insurance contributions | inert | `src:` comment |
| s 337(a)(1) | 3626 | employee: monthly, Schedule J percentages of monthly income | encoded | `s 337(a)(1) — the monthly contributions for` (two arities) |
| s 337(a)(2) | 3627 | other insured: annual, of annual income divided into advance periods | encoded (monthly periods; others declined, F8) | `s 337(a)(2) — the contributions for each advance period, for`, `s 337(a)(2) — the annual contributions for` |
| s 337(b) | 3628 | the Minister's power to change the rates by order, and its conditions | encoded (as the test whether an order is within the power) | `s 337(b) — the order is within the Minister's power` |
| s 337(c) | 3629 | a change carries proportionally to the s 342(c) deduction | encoded (F9) | `s 337(c) — the deduction of` |
| Schedule J heading, references, sub-heading | 4709-4711 | "לוח י׳"; ss 28, 32, 337-342; rates for April 2011 onward | encoded (the sub-heading fixes the year axis, F1) | `nii-schedule-j.l4` heading; nouns `calendar year of the month` |
| Schedule J temporary table: tags and label | 4713-4714 | "(הוראת שעה לשנים 2025–2026)" | encoded (as the 2026 arm; 2025 declined, A1) | `Schedule J — the version for a contribution month in` |
| Schedule J temporary table: column headings | 4716-4719 | columns A-E; C: above / not above × three columns; D: above 60% of the average wage / not above the threshold; E: Treasury | encoded | nouns `A row of Schedule J`; `the column C cell for`; `where column D's upper part begins in` |
| Schedule J temporary table: items 1-10 | 4720-4729 | ten items, nine figure columns | encoded (generated) | `Schedule J (temporary version), item 1` … `item 10` |
| Schedule J temporary table: item 4 note | 4723 | 2.06 in 2024-2027 | encoded (A3) | `Schedule J (temporary version), item 4, with the figures noted for 2024-2027` |
| Schedule J temporary table: totals | 4730 | totals row, with its note | encoded (as data; compared in the red module) | `Schedule J (temporary version), totals as printed`, `… as read in 2024-2027` |
| Schedule J permanent table: label | 4732 | "(הנוסח הקבוע)" | encoded (the 2027 and 2028-on arms) | `Schedule J — the version for a contribution month in` |
| Schedule J permanent table: column headings | 4734-4737 | as the temporary table, but column D's upper part is "above the reduced collection threshold" | encoded | as above |
| Schedule J permanent table: items 1-10 | 4738-4747 | ten items | encoded (generated) | `Schedule J (permanent version), item 1` … `item 10` |
| Schedule J permanent table: item 4 notes | 4741 | 2.06 and 0.47 in 2024-2027 | encoded (A3) | `Schedule J (permanent version), item 4, with the figures noted for 2024-2027` |
| Schedule J permanent table: totals | 4748 | totals row, with its notes | encoded (as data; compared in the red module) | `Schedule J (permanent version), totals as printed`, `… as read in 2024-2027` |
| Schedule J: "–" cells | 4720-4747 | no figure printed | encoded (NOTHING; a branch paid with a dash is declined, F10) | `the percentage in column C of`, `the percentage in column D of` |
| Schedule J column D, applied | 4717-4718, 4735-4736 | what the deduction columns apply to | encoded (as the schedule's headings say; the gap in the temporary version declined, F3) | `the column D deduction under` |

### s 1, every defined term

"Used" means the term occurs in the text of s 334, s 337 or Schedule J, or inside a definition this row encodes; it was checked by searching those lines for each term.

| term | line | used by this row's provisions? | disposition | where, or why not |
| --- | --- | --- | --- | --- |
| בעל שליטה | 122 | no | out-of-scope | A status term that s 335 or the contribution rules for kibbutzim and closely-held companies use; s 335 is an input to this row and the kibbutz rules (ss 3, 3A and Chapter 15's special rules) are not in it. |
| המוסד | 123 | no | out-of-scope | The Institute's organs, the Minister's committee and the labour court: no provision in this row names them. |
| המועצה | 124 | no | out-of-scope | The Institute's organs, the Minister's committee and the labour court: no provision in this row names them. |
| המינהלה | 125 | no | out-of-scope | The Institute's organs, the Minister's committee and the labour court: no provision in this row names them. |
| השר | 126 | yes | encoded (a carrier of words) | `s 1 — "the Minister"`; s 337(b)'s order record |
| ועדת העבודה והרווחה | 127 | no | out-of-scope | The Institute's organs, the Minister's committee and the labour court: no provision in this row names them. |
| בית הדין לעבודה | 128 | no | out-of-scope | The Institute's organs, the Minister's committee and the labour court: no provision in this row names them. |
| אשתו | 129 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| גיל הפרישה | 130-132 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| גמול פרישה | 133 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| גמלה | 134 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| גמלת אזרח ותיק מיוחדת | 135 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| דמי הסתגלות מיוחדים | 136 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| הסכם בדבר מתן גמלאות אזרח ותיק ושאירים מיוחדות | 137 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| חבר קיבוץ מתחדש | 138 | no | out-of-scope | A status term that s 335 or the contribution rules for kibbutzim and closely-held companies use; s 335 is an input to this row and the kibbutz rules (ss 3, 3A and Chapter 15's special rules) are not in it. |
| חברת מעטים | 139 | no | out-of-scope | A status term that s 335 or the contribution rules for kibbutzim and closely-held companies use; s 335 is an input to this row and the kibbutz rules (ss 3, 3A and Chapter 15's special rules) are not in it. |
| חוק ביטוח בריאות | 140 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק בית הדין לעבודה | 141 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק הבטחת הכנסה | 142 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק האימוץ | 143 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק הגנת השכר | 144 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק המשטרה | 145 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק הנוער | 146 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק הנכים | 147 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק העונשין | 148 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק העמותות | 149 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק השבות | 150 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק חדלות פירעון ושיקום כלכלי | 151 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק חופשה שנתית | 152 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק חיילים משוחררים | 153 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק יישום תכנית ההתנתקות | 154 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק הכניסה לישראל | 155 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק משפחות חיילים | 156 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק נכי המלחמה בנאצים | 157 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק נכי רדיפות הנאצים | 158 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק נפגעי פעולות איבה | 159 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק עבודת נשים | 160 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק פיצויי פיטורים | 161 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירות אזרחי | 162 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירות בטחון | 163 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירות בתי הסוהר | 164 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירות המדינה | 165 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירות התעסוקה | 166 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירותי הכבאות | 167 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שכר מינימום | 168 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק תגמול לחייל | 169 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| ילד | 170 | no | out-of-scope | The word appears in this row's provisions only inside the branch name "ילדים" (children); the definition decides who is a child for the children's benefits (row IL-06), not any rate. |
| מדד | 171 | yes | encoded (as an input convention) | index readings are arguments of the s 334(a)(1) rules |
| מעביד / מעסיק | 172 | yes | encoded | `s 1 — the person is an employee` (the core limb) |
| משרת בשירות לאומי–אזרחי | 173 | no | out-of-scope | National, civic or community service: used by the provisions on volunteers and service members, none of which is in this row. |
| מתנדב בשירות לאומי או בהתנדבות קהילתית | 174 | no | out-of-scope | National, civic or community service: used by the provisions on volunteers and service members, none of which is in this row. |
| הסכום הבסיסי | 175-202 | no | out-of-scope | The basic amount: used by Schedule K's maximum income (row IL-05) and by the benefits (its paragraph (2), the child allowance, by row IL-06); not by ss 334, 337 or Schedule J. |
| עגונה | 203 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| עובד | 204 | yes | encoded | `s 1 — the person is an employee`, `s 1 — the family-member limb of "employee"` |
| עובד לשעה | 205 | no | out-of-scope | A casual employee: used by the provisions on short engagements (outside this row); ss 334, 337 and Schedule J do not distinguish one. |
| עובד עצמאי | 206-211 | yes | encoded | `s 1 — a self-employed person in the period:` and its three limbs |
| פיצוי | 212 | yes | encoded (as an input) | the compensation rate in `The data for an update of the average wage` |
| פקודת החברות | 213 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| פקודת הנזיקין | 214 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| פקודת השותפויות | 215 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| פקודת פשיטת הרגל | 216 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| קיבוץ מתחדש | 217 | no | out-of-scope | A status term that s 335 or the contribution rules for kibbutzim and closely-held companies use; s 335 is an input to this row and the kibbutz rules (ss 3, 3A and Chapter 15's special rules) are not in it. |
| קיבוץ שיתופי | 218 | no | out-of-scope | A status term that s 335 or the contribution rules for kibbutzim and closely-held companies use; s 335 is an input to this row and the kibbutz rules (ss 3, 3A and Chapter 15's special rules) are not in it. |
| קצבת התאמה | 219 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| שיעור הפיצוי | 220 | yes | encoded (as an input) | same |
| שירות לאומי / התנדבות קהילתית / שירות אזרחי | 221 | no | out-of-scope | National, civic or community service: used by the provisions on volunteers and service members, none of which is in this row. |
| השכר הממוצע | 222-226 | yes | encoded | `s 1 — the average wage on an update day, from`, its two limbs, `s 1 — the update days of the average wage in tax year` |
| שנת מס | 227 | yes | encoded (as an input convention) | a tax year is a calendar year (fork F12) |
| תקופת אכשרה | 228 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |

### Provisions outside the slice that the slice refers to, or that displace it

| provision | line | referred to by | disposition | reason, and how this row takes its result |
| --- | --- | --- | --- | --- |
| s 335 | 3610-3620 | s 337(a)(1)-(2) ("the contributions under section 335") | out-of-scope | It decides, branch by branch, for whom contributions are paid (non-resident employees maternity only; no unemployment or insolvency for a controlling shareholder in a closely-held company; and so on). Not assigned to this row. Its answer is the input `branches for which contributions are payable under section 335`; the tests state the lists they read from it and the Institute's composites confirm two of them. |
| s 336 | 3622-3623 | s 334(a) "payment period"; s 337(a)(2) by implication | out-of-scope | It makes a payment period a month unless the Minister sets otherwise. Not assigned to this row. Used only as the reason s 337(a)(2) is encoded for monthly periods (F8). |
| s 340 | 3637-3653 | Schedule J column C heading ("sections 337(a) and 340(a)"); s 340(a)(2) for work injury of one who is neither | out-of-scope | The work-injury and maternity rates for particular groups (other insured persons at rates the Minister sets, residents of the Area). Not assigned to this row. A work-injury branch in the neither column is declined with s 340(a)(2) named. |
| s 342 | 3658-3676 | Schedule J column D heading; s 337(c) | out-of-scope (row IL-05) | The employer's duty to pay and to deduct. Column D's figures are encoded as data, and what its headings say they apply to; who deducts, and for which branches, is row IL-05's, and enters here as an input list. |
| s 348 and Schedule K | 3762; 4751- | the income on which contributions are computed | out-of-scope (row IL-05) | The maximum and minimum income. The income inputs are taken after them. |
| ss 344-351 (other than 348) | 3684-3836 | "his monthly income", "his annual income" | out-of-scope | What counts as income for contributions, exemptions (the Institute's worked example removes 3,442 NIS before the rates apply), and the special cases. The income inputs are taken after them. |
| s 2 | 230-239 | s 1 "the average wage" | out-of-scope | Changes the calculation of the average wage "for benefits and contributions" for exceptional pay months. The rules take the average wage as an argument; which figure to supply is fork F5. |
| s 32 | 476-514 | Schedule J column E heading | out-of-scope | The Treasury allocation. Column E's figures are encoded as data only. |
| s 28 | 448-451 | Schedule J's reference note (line 4710) | out-of-scope | The branch accounts: s 28(a) credits every contribution to the branches' accounts "in the ratio of the rates in Schedule J". No figure in this row is applied under it; it is evidence for fork F4. |
| Schedule A | 4360-4365 | s 1 "self-employed person" (3) | out-of-scope | "15% of the average wage as at the first of the quarter's first month"; the sum is an argument of the definition, and the tests compute it from this line for 2026 as a labelled scenario value. |
| ss 66-68 | — | (none; the children branch funds them) | out-of-scope (row IL-06) | The child allowance. Not referred to by this row's provisions; listed because the lead named it. |
| the s 335(b) "insured" of s 65(a)(1) | — | through s 335(b) | out-of-scope (row IL-06 encodes s 65) | Decides who pays the children branch; enters through the s 335 branch list. |
| s 341 | 3654-3656 | displaces s 337 ("notwithstanding sections 337 and 340") | out-of-scope | The Minister's reduced rates by order (an order of 5759-1999 is noted). Neither the section nor the order is in this row. A case it reaches is declined by name, on an input flag (`reduced rates under an order made under section 341 apply to this income`). |
| s 343 | 3677-3680 | displaces the work-injury rate for an approved employer | out-of-scope | Reduced work-injury contributions for an employer of at least 500 employees. Not in this row. An employee's month with this flag and the work-injury branch is declined by name. |

## 3. Assumptions

**A1. Contribution months from January 2026 only; earlier months are declined by name.**
s 334 carries one amendment tag (תשפ״ה־7) and Schedule J's tables carry תשפ״ה־3, תשפ״ה־7 and תשפ״ה־8 (source lines 3601, 4713).
The tags count entries in the year's list of amending Laws at the head of the source (line 7).
For 5785 that list has 11 entries but the tags in the file run to ־12, so the one entry with a double page reference, "395, 395" (the Law for the 2025 budget year), counts twice: tags ־7 and ־8 are that Law, ־3 is Amendment 252 with its temporary provision.
The check: tags ־9 to ־12 then fall on Amendment 257, Amendment 258, Amendment 7 of the National-Civic Service Law and the Economic Assistance Law, and the provisions carrying ־11 (ss 1, 158, 160, 163, 238, 287, 348) include s 1, which defines a person serving in national-civic service; that is consistent with the Law being an amendment of the National-Civic Service Law.
The Law for the 2025 budget year, as Hebrew Wikisource prints it (fetched 2026-10-06, section 7), says in its s 21 that its National Insurance chapter (ss 19-20, the second amending "Amendment 252 and temporary provision") commences on 1 January 2026.
So the deposited s 334 and Schedule J are the text in force from 1 January 2026; what they said in 2025 is not in the sources, and answering 2025 from the amended text would borrow one vintage's figures for another.
The identification is by counting and by the commencement section of a Wikisource page; the Laws themselves could not be fetched from the Knesset (section 7).

**A2. The year of the contribution month is an explicit input, and the dated arms select on it.**
The skill's rule-effective-time axis (`RULES EFFECTIVE DATE`) was not used.
Schedule J's own sub-heading speaks of the month for which contributions are paid ("rates for April 2011 onward"), and s 334(a) updates the threshold "on 1 January of every year"; the year belongs to the case, and every dated arm carries its citation.
Row IL-03 made the same choice for the same kind of reason.

**A3. The editors' notes that date the temporary provisions are relied on.**
The text itself prints two tables; which governs when is said only by the editors' labels ("(הוראת שעה לשנים 2025–2026)", "(הנוסח הקבוע)") and the item-4 notes ("(הוראת שעה בשנים 2024 עד 2027: …)").
Without them there is no rule choosing a table, so they are used, as aids, and every use is cited.
The Institute's pages corroborate the 2026 selection: its published composites for the self-employed (4.47 / 12.83, and 0.26 / 0.78 for work injury alone) and for those who are neither (6.92 / 7.00), and the employee's 5.55 and 1.04 up to the threshold, are exactly the sums of the 2026 version's items.
They also date the employee's 14.6% composite "from 01.02.2025", where the note says 2024; that difference touches only months this row declines.

**A4. Published figures.**
Used: the reduced collection threshold for 2026 (7,703), and the 2026 average wage under s 1 (13,566) and under s 2 (13,769), each from the Institute's pages with URL, time and sha256 (`nii-il04-published-figures.l4`).
The consolidation's editorial notes give the same three figures (lines 3605, 226, 233).
Not used: any figure for 2027 on, which did not exist at retrieval.

**A5. Classifications outside the slice are inputs.**
Which branches a person pays (s 335); the income on which contributions are computed (with ss 344-351, s 348 and Schedule K applied); whether a relationship is one of employment; the Schedule A sum; the number of advance periods; the consumer price index; the CBS wage figures and the compensation rate; whether an order under s 341, or an approval under s 343, reaches the case.
Each is recorded somewhere a caller can read it (phrasebook 1.6, reading 1).

**A6. Nothing is rounded.**
Neither s 334 nor s 337 nor Schedule J says to round; contributions and the updated threshold are exact (F7).

**A7. Each branch is listed once, and income is not negative.**
These are input conventions stated in the nouns module, not checked.

## 4. Fork register

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | Schedule J sub-heading (4711), label (4714) | "For the years 2025-2026": years of what? | (i) the calendar year of the month for which contributions are paid; (ii) the year of payment; (iii) the tax year of the income | **(i)**: the sub-heading dates the rates by the month contributions are "for" ("בעד אפריל"). (i) and (iii) coincide for an employee's monthly contributions. |
| F2 | items 4 and totals (4723, 4741, 4730, 4748) | The 2024-2027 notes: which table do they modify in which year? | (i) each table's own notes apply while that table is in force (temporary in 2026, permanent in 2027); (ii) the notes apply to both tables in all of 2024-2027 | **(i)**, and it makes no difference: both tables note the same 2.06 above the threshold; only the permanent table notes 0.47 below it, and the permanent table governs only 2027 of those years. The temporary table's 0.60 below the threshold carries no note and stands. |
| F3 | Schedule J temporary version, column D (4718) | Column D's upper part is "the part of the wage above 60% of the average wage"; its lower part "the part not above the reduced collection threshold". In 2026 the threshold (7,703) is below 60% of either published average wage (8,139.6; 8,261.4), so the part of a wage between them has no figure. | (i) as printed: that part has no column D figure; (ii) the upper heading is stale, and the upper part begins at the threshold, as in the permanent version; (iii) the lower part runs up to 60% of the average wage | **(i), declined**: `the column D deduction under` refuses a wage that reaches the gap. The Institute applies the employee's 7% "on the part of the wage above the reduced collection threshold", which is reading (ii). The wording "60% of the average wage" is consistent with the threshold's earlier definition: 7,522 is 60% of 12,536, the Institute's s 2 average wage for contributions in 2024 and 2025. Column D's use is s 342(c), row IL-05. |
| F4 | totals rows (4730, 4748) | Ten printed totals differ from the sums of the items above them (section 0). Which governs? | (i) the items: s 335 imposes contributions branch by branch, s 337(a) applies "the rates under section 335", and s 28(a) credits contributions to the branches' accounts "in the ratio of the rates in Schedule J" (line 449); (ii) the totals: the Institute charges composites equal to them (14.6, 7.00) | **(i) for computing; the totals are data and are compared, red, in their own module.** Consequence: an employee in 2026 is charged 14.49% above the threshold here where the Institute charges 14.6%, and the deduction on the upper part sums to 4.67% where the Institute deducts 7%. The two items of evidence point in opposite directions; this is open question 1. |
| F5 | s 1 "the average wage" (222-226), s 2(b) (236) | Which figure is "the average wage" in Schedule J's column D heading, in "self-employed person" (2), and in s 334(a)(2)? | (i) the s 1 figure (13,566 for 2026); (ii) the figure as calculated under s 2, which s 2(b) applies "for benefits and contributions" (13,769) | **not decided**: every rule takes the average wage as an argument. The tests supply 13,566 (the s 1 figure, which the editors' note at line 226 also gives). The column D gap (F3) exists under either. The Institute publishes both, each "for contributions". |
| F6 | s 334(a)(1)-(2) (3606-3607) | If the index or the average wage falls, does the threshold fall? | (i) yes, the rate of rise is negative and is applied; (ii) no, "עליית" (rise) counts only rises | **(i)**: the update is a rate computed from two readings; a test shows a 1% fall lowering 8,000 to 7,920. |
| F7 | s 334(a) | Is the updated threshold rounded? | (i) no; (ii) to the shekel, as the Institute publishes it | **(i)**: the section says nothing about rounding. The published 2026 figure is a whole number; the encoding uses it as published for 2026 and computes unrounded for any later year a caller supplies readings for. |
| F8 | s 337(a)(2) (3627) | "annual income divided into the periods set for advances": equal shares? and does the threshold scale for a period longer than a month? | (i) equal shares, threshold per monthly period, other periods declined; (ii) the threshold scaled by the period's length | **(i)**: s 336 makes the payment period a month unless the Minister sets otherwise, and the Institute applies the threshold to monthly income; the text does not say how it scales. |
| F9 | s 337(c) (3629) | "in the same way and proportionally": by what? | (i) the deduction multiplied by the ratio of new rate to old; (ii) the deduction moved by the same absolute change | **(i)**: "proportionally" is a ratio. Which column C figure pairs with which column D figure is left to the caller's arguments; the natural pairing is the employee's figure on the same part of the wage. A change from a rate of 0 is declined. |
| F10 | Schedule J "–" cells | Is a dash a rate of 0? | (i) no figure: a branch paid with a dash in the person's column is declined; (ii) zero | **(i)**: where s 335 makes a person pay a branch, a dash leaves the schedule silent, and in one case the Law supplies the rate elsewhere (s 340(a)(2)); a zero would hide that. The totals check is the one place a dash adds nothing, because that is what a total of printed figures means. |
| F11 | s 1 "employer" (172), "employee" (204) | The family-member limb of "employee" expressly has no employment relationship, but "employer" is defined by one. Is the relative an employer? | — | **not decided**: no rule in this row turns on it. It matters to s 342 (row IL-05). |
| F12 | s 1 "tax year" (227) | A special assessment period under the Income Tax Ordinance. | — | **not modelled**: a tax year is a calendar year. |
| F13 | s 1 "employee" (204) | The definition "includes" a family member; what is its core? | (i) the ordinary meaning, a person employed within an employment relationship, which is also how s 1 defines the employer; (ii) open-ended | **(i)**, with the relationship itself an input. |
| F14 | s 334(b) (3608) | "and the person liable to pay the wage is regarded as his employer" | — | Encoded as a comment: no rule in this row needs to name the employer. |
| F15 | Schedule J items 1-2 | Item 2 is "maternity – an insured person who is neither employee nor self-employed". Is it a tenth branch? | (i) the same branch, the column decides which item applies; (ii) a separate branch | **(i)**: s 335 imposes maternity contributions (in (a) and (i)) as one branch; items 1 and 2 never both print a figure in one column (a test checks this for every version and column). |
| F16 | s 1 "self-employed person" (207-209) | "לפחות" (at least), "לא פחתה מ" (not less than) at the boundary | — | **inclusive** (`AT LEAST`); tests sit on each boundary. |
| F17 | Schedule J column C (4718) | Is the rate applied to the whole income according to its band, or to each part? | (i) marginal, each figure "on the part"; (ii) slab | **(i)**: the headings say "on the part above" and "on the part not above". At exactly the threshold all the income is "not above". |

**Where I looked for others and found none:** s 334(a)'s two carrier definitions; s 337(b)'s conditions (each a fact the order records); Schedule J's column E (data only).

## 5. Answer table

Composite percentages are sums of the items of the version in force, for the branch lists the tests state (all nine branches for an employee; seven for the self-employed; six for one who is neither; six deduction branches for column D).
"Declined" means a named `REFUSE`.

| | 2025 | 2026 | 2027 | 2028 on |
| --- | --- | --- | --- | --- |
| Schedule J version | declined (A1) | temporary, with item 4 at 2.06 | permanent, with item 4 at 2.06 and 0.47 | permanent as printed |
| reduced collection threshold | declined | 7,703 (published) | supplied by the caller (index-updated; declined if not) | supplied by the caller (2029 on: wage-updated) |
| employee, not above / above | declined | 5.55 / 14.49 (printed totals 5.55 / 14.60) | 4.26 / 14.49 (printed 3.95 / 14.60) | 4.16 / 14.39 (printed 3.85 / 14.50) |
| self-employed, not above / above | declined | 4.47 / 12.83 | 2.87 / 12.83 | 2.87 / 12.83 |
| neither, not above / above | declined | 6.92 / 7.00 | 4.61 / 7.00 | 4.61 / 7.00 |
| column D, not above / upper part | declined | 1.04 / 4.67 (printed 1.04 / 7.00); upper part begins at 60% of the average wage (F3) | 0.40 / 4.67 (printed 0.40 / 7.00) | 0.40 / 4.67 (printed 0.40 / 7.00) |

Worked figures the tests assert (2026 unless marked):

| facts | contributions (NIS) |
| --- | --- |
| employee, senior citizens and survivors only, 10,000 | 306.2999 |
| employee, maternity only, 7,703 / 7,704 | 18.4872 / 18.5012 |
| employee, work injury only, 10,000 | 93.5362 |
| employee, all branches, 6,000 | 333 |
| employee, work injury only, 10,000, threshold 8,000 (scenario): 2027 / 2028 | 78.8 / 68.8 |
| neither, the Institute's January 2026 example (base 8,558) | 592.8976 (with health at 5.17%: 1,035.3462; the Institute prints 931.29 + 104.05 = 1,035) |
| self-employed, 240,000 a year in 12 monthly advances | 1,922.0292 a month; 23,064.3504 a year |
| column D, permanent version, wage 10,000, threshold 8,000 (scenario) | 125.4 |
| column D, temporary version, wage 7,000 / 7,703 / 7,704 | 72.8 / 80.1112 / declined (F3) |

## 6. Nouns to reconcile at IL-07

Read from the sibling deposit `legalese-2026-10-il-06` (read-only) at the end of this session; nothing here depends on it and nothing in it was changed.

- **The person.** This row: `A person who works` (employment relationship, family-member limb, wage fixed by Law), `A person's occupation in a period` (self-employed limbs), and the two contribution cases. IL-06: `A person` (insured under Chapter 11, resident, a housewife under s 238, …). One insured-person record could carry both; s 335(i) turns on "insured under Chapter 11 other than a housewife and a widow pensioner under s 238", which IL-06 already models.
- **The children branch.** s 335(b) makes "an insured person as defined in s 65(a)(1)" pay the children branch; IL-06 encodes s 65 (`s 65 "insured" (1)`). Here the branch enters through the input list; at IL-07 the two can be joined.
- **Section 1.** Both rows have a s 1 module (`nii-s1-definitions.l4` here; `nii-s1-basic-amount.l4` there) and a published-figures module. They define different terms and should merge into one s 1 module without collision.
- **Published figures.** Both rows take figures from the Institute's pages with the same provenance convention and decline the next year by a named refusal; the refusal texts differ in wording.

## 7. Sources: what was fetched, and what was not

The deposited source was read and its sha256 verified (`78bf47ee…2a97`) on 2026-10-06 before use.
Fetched on 2026-10-06 (curl; bytes not deposited, the site reserving its rights; sha256 of what was fetched):

| what | URL | UTC | sha256 | what it says that this row uses |
| --- | --- | --- | --- | --- |
| NII rates page, employees | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9c%d7%a2%d7%95%d7%91%d7%93%d7%99%d7%9d%20%d7%a9%d7%9b%d7%99%d7%a8%d7%99%d7%9d.aspx` | 14:07:32 | `63457694f21874d7e1eee490811ec86b60c83aff49f733aae6aadb85b9129aba` | threshold 7,703 from 01.01.2026; National Insurance employer 4.51 / employee 1.04 / total 5.55 up to it, 7.6 / 7 / 14.6 above; health 3.23 / 5.17; form 102 "column 2" (controlling shareholder) totals with health 8.71 / 19.34, employee 4.25 / 11.96 |
| NII rates page, self-employed | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9c%d7%a2%d7%a6%d7%9e%d7%90%d7%99%d7%9d.aspx` | 14:07:34 | `5abe5977d369d0da10e26269ab90aec5ae216247b6018e6721ba760fc7d33f22` | 4.47 / 12.83; under 18 or receiving an old-age pension 0.26 / 0.78, "National Insurance only" |
| NII rates page, neither | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9e%d7%99%20%d7%a9%d7%90%d7%99%d7%a0%d7%9d%20%d7%a2%d7%95%d7%91%d7%93%d7%99%d7%9d%20%d7%95%d7%91%d7%a2%d7%9c%d7%99%20%d7%94%d7%9b%d7%a0%d7%a1%d7%94%20%d7%a9%d7%9c%d7%90%20%d7%9e%d7%a2%d7%91%d7%95%d7%93%d7%94.aspx` | 14:07:36 | `36c88a5e9666a9410a13dbe50ebdb0778b2653305d0a33688682029edd24d183` | 6.92 / 7; health 5.17; the worked example for January 2026 |
| NII average wage | `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%d7%a9%d7%9b%d7%a8%20%d7%9e%d7%9e%d7%95%d7%a6%d7%a2.aspx` | 14:08:43 | `fe4d43b1bc1f007839567cbee759f8135558c94c89e3a10a531b5baecaf31b1f` | from 01.01.2026: 13,566 under s 1 and 13,769 under s 2, each for benefits and for contributions; for 2025, contributions 12,379 (s 1) and 12,536 (s 2) |
| Law for the 2025 budget year, Hebrew Wikisource raw text | `https://he.wikisource.org/w/index.php?title=%D7%97%D7%95%D7%A7%20%D7%9C%D7%94%D7%A9%D7%92%D7%AA%20%D7%99%D7%A2%D7%93%D7%99%20%D7%94%D7%AA%D7%A7%D7%A6%D7%99%D7%91%20%D7%95%D7%9C%D7%99%D7%99%D7%A9%D7%95%D7%9D%20%D7%94%D7%9E%D7%93%D7%99%D7%A0%D7%99%D7%95%D7%AA%20%D7%94%D7%9B%D7%9C%D7%9B%D7%9C%D7%99%D7%AA%20%D7%9C%D7%A9%D7%A0%D7%AA%20%D7%94%D7%AA%D7%A7%D7%A6%D7%99%D7%91%202025%20%28%D7%AA%D7%99%D7%A7%D7%95%D7%A0%D7%99%20%D7%97%D7%A7%D7%99%D7%A7%D7%94%29&action=raw` | 14:10:35 | `8ca6d31272e4a29bf481ac8e3d32ce7c44cbfd43562a7401e08ccb7b93b86361` | Chapter E (National Insurance): s 19 amends the Law, s 20 amends Amendment 252 and its temporary provision, s 21 "this chapter commences on 1 January 2026" |

The Institute's pages describe themselves as general information and not the binding text of the Law; they are used as the regulator's published figures and examples, not as law.

**Attempted and failed:** the amending Laws from `fs.knesset.gov.il` (Amendment 252, `25_lsr_5482787.pdf`) returned a 131,618-byte HTML page in place of a PDF, as it did for row IL-03; the Wayback Machine availability API answered 429 (too many requests); the Central Bureau of Statistics price-index API (`api.cbs.gov.il`) timed out after 40 seconds.
Nothing was kept from those responses.
So the consumer price index is an input, and the commencement of Amendment 252's temporary provision was not read.

**Observations about the source**, for whoever maintains it:

- Ten cells of Schedule J's totals rows differ from the sums of their items (section 0). The gaps are the same in all four readings of the schedule: 2.33 in column D's upper part, 0.11 in column C above the threshold for an employee, and (permanent version only) 0.31 the other way in column C not above the threshold for an employee. Which cell, if any, is wrong cannot be told from the table.
- The temporary version's column D heading ("above 60% of the average wage") does not meet its other heading ("not above the reduced collection threshold") in 2026 (F3).
- s 342(e)(3)-(4) (lines 3669-3670) refer to "טור ה׳ בלוח י׳" (column E) for the employee's deduction rates, where the schedule's column E is the Treasury allocation and column D is the deduction (row IL-05's provision; noted for it).
- Line 3605's editorial note calls 7,522 "nominal for 2025"; the text is in force only from 1 January 2026 (A1), so the note dates the base, not a year the text governed.

## 8. Open questions for a domain expert

1. F4: does the Institute collect the employee's 14.6% (and deduct 7%) above the threshold because the totals row governs, or because the items as enacted differ from the consolidation's? If the consolidation mistranscribes an item, which?
2. F4: for a controlling shareholder in a closely-held company the Institute's composite above the threshold (14.17) exceeds the items without unemployment and insolvency (14.12); is there a rule outside s 335(e)-(f) that explains the 0.05?
3. F3: is the temporary version's column D heading "above 60% of the average wage" in the Law as amended, or a remnant of the threshold's earlier definition that the 2025 budget-year Law did not update?
4. F5: which average wage does Schedule J (temporary column D), the s 1 self-employed test and s 334(a)(2) use: the s 1 figure or the s 2 figure?
5. A3: from which month did the 2.06 work-injury rate apply: January 2024 (the editors' note) or February 2025 (the Institute's composite)?
6. F8: are the self-employed's advance periods ever other than months, and if so how does the Institute apply the threshold to them?

## 9. What was not done

- **The independent test pass** (skill step 8) was not run: the brief for this row is one session with no sub-agents. Every expected value was worked out before it was asserted, by a Python computation over the source's cells and the Institute's printed figures that does not use this encoding; no second reader has derived them.
- **HG1**, a human who knows Israeli national insurance reading the modules against the Hebrew, has not been sought.
- **Semi-cleanroom** (ruled 2026-10-06): nothing from the Axiom Foundation, any RuleSpec repository, or the paths the brief lists was read, searched or fetched in this session.
