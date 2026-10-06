# NOTES — il/national-insurance-law-consolidated-version-5755-1995, encoding row `legalese-2026-10-il-05`

National Insurance Law [Consolidated Version], 5755-1995: **s 342** (who is liable to pay insurance contributions, and the employer's deduction), **s 348** (the maximum, the minimum and the disregarded amount) and **Schedule K** (לוח י״א, the maximum and minimum income for contributions), encoded in L4 by one agent in one session (run `IL-05-20261006`, 2026-10-06), from the brief in `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought.
The row depends on row IL-04 (s 1, s 334, s 337, Schedule J), whose modules it could not import (section 8).

## 0. What `check.sh` prints

Run on 2026-10-06 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, which resolves to the cabal store entry `jl4-0.1-0ee0100b`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118` (the binary row IL-04 used).
The binary has no `--version`, and no record beside it names the commit it was built from.

```
module                                    errors satisfied  failed  refused  expected
nii-il05-nouns.l4                              0         0       0        0         0
nii-il05-published-figures.l4                  0         0       0        0         0
nii-il05-tests-expected-red.l4                 3         2       3        0         3
nii-il05-tests.l4                              0       170       0        0         0
nii-s342-liability-and-deduction.l4            0         0       0        0         0
nii-s348-maximum-minimum.l4                    0         0       0        0         0
nii-schedule-k.l4                              0         0       0        0         0
TOTAL (7 modules)                              3       172       3        0
```

`check.sh` exit 0.
The 3 errors are the 3 failed assertions of `nii-il05-tests-expected-red.l4`, which `check.sh`'s `expected_failed` table and `encoding.json`'s `expected_red` both name with that count; there is no other error, and no warning in any module.
They were predicted before that module was first run, and the run failed exactly those three, read from the diagnostics by line (45, 46, 61; none "could not be evaluated"):

- **2: s 342(e)(3) and (e)(4) name "column E of Schedule J" for the rates of the employer's deduction** (lines 3669-3670), where Schedule J's column E is "the State Treasury's allocation under s 32(c1)" and the deduction is column D, "the deduction from the employee's wage for s 342(c)" (line 4717). Fork F22.
- **1: s 342(c)(2) is made "subject to s 245(b2)"** (line 3662), and s 245(b2) reads "(בוטל)", repealed (line 2474). Fork F10.

Neither changes an answer the rules give: (e) is a power whose regulations are not in the sources, and a repealed provision qualifies nothing.

`nii-il05-tests.l4`: 170 assertions, 170 satisfied, on the first run that evaluated them.
Before that run, nine fixture names were changed so that no helper shared a name with a record field, a parameter, a global, or another helper's head and arity (made by reading the module, not in answer to a diagnostic); no expected value was changed at any point.
Every expected value was computed before the run, from the source's cells and the Institute's printed figures, without the encoding: by a Python script over exact fractions (`expected.py`, in the session scratchpad, not deposited), or, for a few one-step figures (557.75, 700, 2,100, and the 200 + 18.8 that equals 218.8), by hand.

**The harness can fail.** In a scratch copy, two expected values were altered (51,910 to 51,911; 2,065.35 to 2,065.36): `check.sh` reported 2 failed in the tests module and exited 1.

**Mechanical checks**, using row IL-04's scripts by path (read-only; not copied):

- `../legalese-2026-10-il-04/tools/srcquote.py SOURCE FILE.l4…` generates every `-- src:N | …` comment from line N of the source; re-running it over every module of this row changed nothing.
- `../legalese-2026-10-il-04/tools/hebcheck.py SOURCE FILE…` checks that every run of Hebrew outside a `src:` line occurs verbatim in the source; it passes on every `.l4` module, `BRIEF.md`, this file, `encoding.json` and `SOURCE-LICENSE.md`, and fails on a planted invented string.

## 1. What is encoded and what is not

**Encoded:** s 342(a), (b), (c)(1), (c)(2) in all its limbs, (d) with its two definitions, (e1) and (f)(1)-(2); s 348(a), (a1), (b), (c) (as the test whether an order is within the power, and a decline where one reaches), (d) (where its two readings agree) and (e) in both its permanent and its temporary text; Schedule K in full: all four items, maximum and minimum, per month, quarter and year, with its three definitions.
**Inert:** headings; s 342(e)(1)-(4) and (f)(3), powers to make rules whose regulations are not in the sources (a deduction such a regulation governs is declined by name).
**Out of scope:** Schedule K1 (referred to only by s 369); and every provision outside the slice, each listed in section 2 with how this row takes its result.

**Periods answered:** contribution periods from **January 2026** (assumption A1).
For 2026 the Institute's published figures are used; for 2027 and later a caller supplies the figures, and the rules that would look them up decline by name.

**Figures not in the text** are the Institute's (section 7): the basic amount under paragraph (3) for 2026 (10,382), the average wage for contributions for 2026 (13,769 under s 2, used; 13,566 under s 1, recorded), the monthly minimum wage (6,247.67 from 1.4.2025, 6,443.85 from 1.4.2026), and the reduced collection threshold for 2026 (7,703).

**Composition with IL-04.** IL-04's s 337 takes as an input "the monthly income on which contributions are computed … (s 348 and Schedule K, row IL-05)"; that is this row's `s 348 — the income on which contributions are computed, for`.
This row's s 342(c) takes as an input the column D amount of each branch on the wage, which is IL-04's `the column D deduction under`, per branch.

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`.

**Totals.** s 342, s 348 and Schedule K: **32 encoded, 8 inert, 1 out-of-scope, 0 deferred** (41 rows).
s 1 terms the slice uses: **9 encoded** (of which 8 as inputs or input conventions), **1 inert**, **3 out-of-scope** (13 rows).
Provisions outside the slice that it refers to, or that displace it: **21 out-of-scope** rows, each with its reason.
Altogether **41 encoded, 9 inert, 25 out-of-scope, 0 deferred**.

### s 342

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| s 342 heading and tags | 3658 | who is liable to pay contributions; tag תשפ״ה־7 | inert (the tag dates the text, A1) | `src:` heading, `nii-s342-liability-and-deduction.l4` |
| s 342(a) | 3659 | the self-employed and those who are neither pay for themselves; a wife insured only under Chapter C does not | encoded | `s 342(a)-(b) — the person liable to pay the contributions for` |
| s 342(b) | 3660 | the employer pays for the employee; several employers each as if the only one; (d) and (e) apply | encoded | same rule; "as if the only one" is how each employer's (c) is computed; (d) below |
| s 342(c)(1) | 3661 | the employer deducts the Schedule J percentages for s 335(a), (d), (e), (g), (h), (i) | encoded (F12, F13) | `the branches of the subsections of section 335 that section 342(c)(1) names`, `s 342(c)(1) — the deduction it requires, for` |
| s 342(c)(2) | 3662 | no deduction while a senior citizen pension is payable, or after 70 (a man) or the Part D age (a woman); police and prison officers: not item 6; the employer may reduce | encoded (F9, F10, F19, F21) | `s 342(c)(2) — no deduction is made for the month, for`, `s 342(c) — the amount the employer deducts from the wage, for`, `s 342(c)(2) — the amount by which the employer may reduce …` |
| s 342(d) chapeau | 3663 | several employers | encoded | `section 342(d) does not apply: the insured person works for one employer` |
| s 342(d)(1) | 3664 | actual deduction below the coordinated contributions: the employee pays the difference; the two definitions | encoded (F14) | `s 342(d) — "the actual deduction", of`, `s 342(d) — "coordinated contributions", for`, `s 342(d) — the outcome, …` |
| s 342(d)(2) | 3665 | above them: the employee is refunded | encoded | `s 342(d) — the outcome, …` |
| s 342(e) chapeau | 3666 | the Minister may set conditions, rules and dates | inert (a power) | `src:` comment |
| s 342(e)(1)-(4) | 3667-3670 | reporting; payment or refund of the (d) difference; deduction at the full rate where there is another employer; the Institute's approval | inert (powers; the regulations are not in the sources; a deduction they govern is declined; F22) | `the deduction is governed by regulations under section 342(e)(3) or an approval under section 342(e)(4), which are not encoded here` |
| s 342(e) note | 3671 | regulations of 5757-1997 published | inert | `src:` comment |
| s 342(e1) | 3672 | a renewed kibbutz member: the kibbutz pays the coordinated contributions less what the other employer deducted | encoded (F15) | `s 342(e1) — the contributions the renewed kibbutz pays for the member, for` |
| s 342(f)(1) | 3673 | an employee who is also self-employed: no reduced rate on the s 2(1) and (8) income | encoded | `s 342(f)(1) — the part of the self-employed income not at the reduced rate, for` |
| s 342(f)(2) | 3674 | unless the wage is below the threshold: the reduced rate on the difference | encoded (F16) | `s 342(f)(2) — the part of the self-employed income at the reduced rate, for` (two arities) |
| s 342(f)(3) | 3675 | regulations power | inert (a power) | `src:` comment |

### s 348

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| s 348 heading and tags | 3762 | maximum, minimum and disregarded amounts; tags into תשפ״ו־7 | inert (the tags dated, section 7) | `src:` heading, `nii-s348-maximum-minimum.l4` |
| s 348(a) | 3763 | income above the Schedule K maximum is not taken into account | encoded | `s 348(a) — the income taken into account, of`, `the Schedule K maximum for` |
| s 348(a1) | 3764 | non-work income not exempt under s 350 and not above 25% of the average wage is not taken into account | encoded (F3, F4; the other reading also encoded, for comparison) | `s 348(a1) — the income not from work that is not taken into account, for`, `s 348(a1), read as all or nothing — …` |
| s 348(b) | 3765 | no income or below the Schedule K minimum: as if the minimum | encoded (F6, F11, F18) | `s 348(b) — no income, or an income that does not reach the minimum: of`, `s 348(a) and (b) — …` |
| s 348(c) | 3766 | the Minister may change the minimum amounts by order | encoded (the power's test; an order that reaches a period is declined) | `s 348(c) — the order is within the Minister's power`, `an order under section 348(c) changed a minimum amount …` |
| s 348(d) | 3767 | unemployment benefit for a full month: as if the item 3 minimum | encoded where its readings agree (F5, F7) | `s 348(d) — the income on which contributions are computed, for` |
| s 348(e), permanent text | 3768 | volunteers, yeshiva students, civil service: as if the item 3 minimum | encoded (F6, F7) | `s 348(e) — the person is of a class both texts name`, `s 348(e) — the income regarded as the item 3 minimum, for` |
| s 348(e), temporary text | 3769 | the same with national-civic service, until 31.8.2026, and after it for those who began before | encoded (a dated arm, F8; A3) | `the expiry of the National-Civic Service Law, which ends the temporary text of section 348(e)`, `s 348(e) — the person serves in national-civic service in a period the temporary text reaches` |

### Schedule K

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| heading, references, sub-heading, tags | 4751-4755 | "maximum and minimum income for contributions"; ss 345(e), 348, 349; tags to תשע״ב־2 | inert | `src:` heading, `nii-schedule-k.l4` |
| table header | 4757 | item, for whom, maximum income, minimum income | encoded (the four items) | nouns `An item of Schedule K` |
| item 1, employee, month | 4758 | max the basic amount × 5; min the minimum wage of the quarter's first month | encoded | `Schedule K item 1 — the maximum income for a month, under`, `… the minimum income for a month in` |
| item 1, employee, quarter | 4759 | max month × 3; min month × 3 | encoded | `Schedule K item 1 — the maximum income for a quarter, under`, `… the minimum income for` |
| item 1, employee, year | 4760 | the totals over the quarters | encoded | `Schedule K item 1 — … for a year, under` |
| item 2, self-employed, quarter | 4761 | max 5 × the basic amount × 3; min 25% of the average wage of the quarter's first month × 3 | encoded | `Schedule K item 2 — …` |
| item 2, self-employed, year | 4762 | the totals over the quarters | encoded | `Schedule K item 2 — … for a year, under` |
| item 3, maximum | 4763 | as item 1, for a quarter or a year | encoded | `Schedule K item 3 — the maximum income …` |
| item 3, minimum, quarter | 4763 | 5% of the average wage of January (of October for the fourth quarter) × 3 | encoded | `the average wage items 3 and 4 read for`, `Schedule K item 3 — the minimum income for` |
| item 3, minimum, year | 4764 | the total over the quarters | encoded | `Schedule K item 3 — the minimum income for a year, under` |
| item 4, maximum | 4765 | as item 2 | encoded | `Schedule K item 4 — the maximum income …` |
| item 4, minimum, quarter | 4765 | 15%, the same months as item 3 | encoded | `Schedule K item 4 — the minimum income for` |
| item 4, minimum, year | 4766 | the total over the quarters | encoded | `Schedule K item 4 — the minimum income for a year, under` |
| (no monthly cell for items 2-4) | 4761-4766 | — | encoded as a third of the quarter (F2) | `a month's share of the quarter's figure` |
| definitions chapeau and tag | 4769-4770 | "in this Schedule" | inert | `src:` comment |
| "quarter" | 4771 | three months from 1 January, April, July or October of a tax year | encoded | `the quarter that contains month`, `the first month of`, `the four quarters of a tax year` |
| "minimum wage" | 4772 | the minimum wage applicable to the particular employee under the Minimum Wage Law | encoded (as the employee's input, F11) | nouns `The minimum wage applicable to the employee in the first month of each quarter` |
| "basic amount" | 4773 | as in paragraph (3) of the s 1 definition | encoded (as an input) | `the basic amount, under` |
| Schedule K1 | 4775-4784 | breach periods and maximum charges, referred to by s 369 | out-of-scope | Neither s 342 nor s 348 refers to it; its only reference is s 369 (line 4776), a provision on charging an employer who did not register or pay, which is not in this row. |

(The "no monthly cell" row records a reading, not a provision, and is not counted in the totals.)

### s 1 terms the slice uses

| term | line | disposition | where, or why not |
| --- | --- | --- | --- |
| הסכום הבסיסי, paragraph (3), with its update clause (2) | 191, 192, 196 | encoded (as an input, constant in a tax year) | `The figures Schedule K reads for a tax year`; the 2026 figure published; the update by the index is s 1's and not encoded |
| השכר הממוצע | 222-226 | encoded (as an input) | `the average wage as updated on 1 January`; which figure is fork F1 |
| יום העדכון | 225 | encoded | `the average wage in force in month`: 1 January, and any later update day |
| שנת מס | 227 | encoded (input convention: a calendar year) | nouns |
| משרת בשירות לאומי–אזרחי | 173 | encoded (as an input: the day service began) | s 348(e) temporary text |
| מתנדב בשירות לאומי או בהתנדבות קהילתית | 174 | encoded (as an input) | s 348(e) |
| גמלת אזרח ותיק מיוחדת | 135 | encoded (folded into the pension input, as s 342(c)(2) itself folds it) | `The senior citizen pension in the month` |
| חוק המשטרה / חוק שירות בתי הסוהר | 145, 164 | encoded (as an input: a police or prison officer) | s 342(c)(2) |
| קיבוץ מתחדש / חבר קיבוץ מתחדש | 217, 138 | encoded (as inputs: s 3A met) | s 342(e1) |
| השר | 126 | inert | the Minister of ss 342(e) and 348(c); row IL-04 encodes the definition |
| מעביד / עובד / עובד עצמאי | 172, 204, 206 | out-of-scope (row IL-04 encodes them) | The column of insured person is an input; IL-04's s 1 rules decide it. |
| שירות לאומי / התנדבות קהילתית / שירות אזרחי | 221 | out-of-scope | s 348(e) uses "civil service as defined in s 6(a) of the Deferral of Service for Yeshiva Students Law", not the s 1 definition (which points to the Civil Service Law); "national service" and "community volunteering" reach (e) through the s 1 definition of the volunteer, line 174. |
| מדד | 171 | out-of-scope | Used by the basic amount's update, which this row takes as a published figure. |

### Provisions outside the slice that it refers to, or that displace it

| provision | line | referred to by | disposition | reason, and how this row takes its result |
| --- | --- | --- | --- | --- |
| s 335 | 3610-3620 | s 342(c)(1); s 348(a) | out-of-scope | Which branches a person pays. Its answer is the input `branches for which contributions are payable under section 335` (IL-04's name); its subsections are mapped to branches for (c)(1) (F12). |
| s 337 and Schedule J | 3625-3629, 4709-4749 | s 342(c)(1), (c)(2) item 6, (e), (f) | out-of-scope (row IL-04) | The rates. s 342(c) takes the column D amount per branch as an input; s 342(f) returns the parts of the income each rate applies to. |
| s 334(a) | 3605-3607 | s 342(e)(3), (f) | out-of-scope (row IL-04) | The reduced collection threshold: an argument of (f), with the Institute's 2026 figure for 2026. |
| s 344 | 3684-3697 | s 348 ("his income") | out-of-scope | An employee's monthly income: the input `income from work in the period`. |
| s 345 | 3715-3734 | s 348; Schedule K's heading cites s 345(e) | out-of-scope | The annual income of the self-employed and others; (e) charges advances on the Schedule K minimum when nothing else is known. The income is an input. |
| s 349 | 3771-3772 | (Schedule K's heading) | out-of-scope | The Minister's power to change or replace Schedule K; not exercised in the sources since the 5759 change the consolidation already includes (tag ק״ת תשנ״ט, line 4755). |
| s 350, with (c) | 3774-, 3805 | s 348(a1); s 350(c) disapplies s 348(b) | out-of-scope | What is exempt is subtracted before the input; s 350(c) enters as a flag (F18). |
| s 3A | — | s 342(e1) | out-of-scope | Whether a renewed kibbutz member meets 3A(a) and (b): inputs. |
| s 245(b2) | 2474 | s 342(c)(2) | out-of-scope (repealed) | "(בוטל)". The cross-reference is checked, red (F10). |
| Schedule A1 Part D | 4431-4453 | s 342(c)(2) | out-of-scope | A woman's age by month of birth: an input in months. The tests use its last row (70, for a woman born in May 1950 or later, line 4453). |
| Chapter C | — | s 342(a) | out-of-scope | On what footing a woman is insured: an input. |
| Chapter G | — | s 348(d) | out-of-scope | Whether unemployment benefit was received for a full month: an input. |
| Chapter 15's collection provisions (ss 352-364 and on) | — | (what follows non-payment) | out-of-scope | Why ss 342(a)-(d) are encoded as who and how much, not as obligations (module header). |
| s 2 | 230-239 | s 1 "the average wage" | out-of-scope | Its (b) changes the average wage "for benefits and contributions"; the reason for fork F1. |
| the regulations of 5757-1997 under s 342(e) | 3671 | s 342(e)(3)-(4) | out-of-scope | Not in the sources; a deduction they govern is declined. |
| Income Tax Ordinance s 2 | — | ss 342(f), 348(a1) | out-of-scope | The sources of income: the inputs are split by source. |
| Minimum Wage Law | — | Schedule K "minimum wage" | out-of-scope | The employee's minimum wage is an input; the Institute's 2026 figures for an employee aged 18 or over are published figures. |
| Deferral of Service for Yeshiva Students Law s 6(a) | — | s 348(e) | out-of-scope | Who serves in civil service as it defines: an input. |
| National-Civic Service Law s 36(a) | — | s 348(e) temporary text | out-of-scope | Its expiry date ends the temporary text; read from Amendments 7-9 (section 7). |
| Police Law (Disabled and Fallen), Prison Service Law (Disabled and Fallen) | — | s 342(c)(2) | out-of-scope | Who is a police or prison officer within them: an input. |
| s 369 | — | Schedule K1 | out-of-scope | See Schedule K1 above. |

## 3. Assumptions

**A1. Contribution periods from January 2026 only; earlier periods are declined by name.**
s 342's last tag, תשפ״ה־7, counts to the Law for the 2025 budget year (row IL-04's identification, A1 there).
That Law, read from the Knesset's PDF (section 7), says in its s 19(4) that in s 342 "everywhere, instead of '60% of the average wage' shall come 'the reduced collection threshold', and instead of 'from 60% of the average wage', 'from the reduced collection threshold'", and in its s 21 that its National Insurance chapter commences on 1 January 2026.
So the deposited s 342 is the text from 1 January 2026, and before it (e)(3) and (f) read "60% of the average wage"; that earlier wording is known but not encoded, because its Schedule J is not (IL-04 declines 2025 too).
s 348 and Schedule K were probably the same in 2025 apart from the date in (e)'s editors' note (section 7), but this row answers from 2026 only, with IL-04 and with s 342.

**A2. The year and month of the period are explicit inputs; the dated arms select on them.**
The rule-effective-time axis was not used, as in rows IL-03 and IL-04: Schedule K speaks of "the first month of the quarter" and s 348(e)'s temporary text of a date, both facts of the case.

**A3. The editors' notes are relied on for s 348(e)'s two texts and their date.**
The deposited text prints (e) twice, labelled by the editors "(the permanent text)" and "(temporary provision until the expiry of the National-Civic Service Law … on 31.8.2026 …)".
Without the labels there is no rule choosing between them, so they are used as aids, cited where used.
The date was checked against the National-Civic Service Law's own amendments (section 7); whether a later amendment moved it again was not searched for.

**A4. Published figures.**
Used by the rules: the 2026 basic amount under paragraph (3) (10,382), the 2026 average wage for contributions under s 2 (13,769; fork F1), the monthly minimum wage of an employee aged 18 or over (6,247.67 from 1.4.2025; 6,443.85 from 1.4.2026), and the 2026 threshold (7,703), each with URL, time and sha256 (`nii-il05-published-figures.l4`).
The consolidation's editorial notes give the same basic amount and average wages (lines 191, 226, 233).
No figure for 2027 was published at retrieval.

**A5. Classifications outside the slice are inputs**, each listed in section 2 with its citation: the column of insured person, the branches payable, the income by source and after exemptions, the column D amounts, the employee's minimum wage, receipt of unemployment benefit, the s 348(e) statuses, s 350(c), an order under s 348(c), the senior citizen pension, the Part D age, police or prison service, s 3A, the regulations under s 342(e).

**A6. Nothing is rounded.**
Neither s 342 nor s 348 nor Schedule K says to round; the Institute publishes whole shekels, and the tests compare with `ROUND` where they compare with a printed figure.

**A7. Input conventions not checked:** incomes are not negative; each branch appears once in a list; updates of the average wage are listed in order of month.

## 4. Fork register

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | Schedule K items 2-4 (4761-4765); s 348(a1) (3764) | Which "average wage": the s 1 figure (13,566 for 2026) or the figure calculated under s 2 (13,769)? | (i) s 1; (ii) s 2 | **(ii)**: s 2(b) says that "in calculating the average wage, for benefits and contributions, these changes apply" (line 236); and every Institute figure this row checked fits (ii) and not (i): 3,442 (25% of 13,769), 143 (6.92% of 15% of 13,769), 171 (48 + 123), the 2025 table's 3,134, 627 and 1,880 (25%, 5%, 15% of 12,536, the 2025 s 2 figure for contributions). The rules take the figure in the figures record; the 2026 record uses (ii); tests show (i) does not reproduce the Institute's figures. Bears on row IL-04's open fork F5. |
| F2 | Schedule K items 2-4 | They print no figure for a month; what is a month's? | (i) a third of the quarter's; (ii) none (decline monthly periods) | **(i)**: every quarterly figure is written as a monthly amount "× 3"; s 337(a)(2) divides annual income into monthly advance periods (s 336); s 348(d) speaks of a month; the Institute prints monthly figures that are exactly a third (51,910, 3,442). |
| F3 | s 348(a1) (3764) | "the income … which does not exceed 25% of the average wage shall not be taken into account": all of it if it does not exceed, none if it does; or the part up to 25%? | (i) all or nothing; (ii) a deduction of up to the 25% sum | **(ii)**: (a)'s "the amount of the income exceeding the maximum" is read as the part above it, and (a1) is the same construction from below; the Institute's January 2026 example deducts 3,442 from rent of 12,000. (i) is encoded beside it; the readings agree up to the sum and part above it (tests). |
| F4 | s 348(a1) | The 25% sum has no period. | (i) a month's; (ii) scaled to the period | **(i), and other periods declined**: the average wage is a monthly figure, and the Institute applies the sum "per month". A quarter or year with income not from work is declined by name. |
| F5 | s 348(d) (3767) | (d) has no condition "who has no income or whose income does not reach". A deeming (the item 3 minimum whatever the income), or a floor like (e)? | (i) deeming; (ii) floor | **neither; answered only where they agree**: income not above the item 3 minimum gives the minimum under both; above it, declined by name. No source settles it. |
| F6 | Schedule K item 3 (4763) | "an insured person as stated in s 348(d) and (e)": the classes (d) and (e) name, or only those meeting (e)'s income condition? | (i) the classes; (ii) the classes with the condition | **(i)**: (ii) puts a yeshiva student with a little income on item 4's 15% minimum, above the 5% minimum of one with none (a cliff the schedule's own grading does not suggest). A test shows (i)'s answer (1,557.75, not 2,065.35). |
| F7 | items 1-3; s 348(d), (e) | An employee or a self-employed person who is also in a class (d) or (e) names: which item? | (i) item 1 or 2 by the column; (ii) item 3 | **(i), with declines**: items 1 and 2 are named by status. Where it matters, declined: (d) for an employee or self-employed person; (e) for one whose income is below the item 3 minimum (then (e) says the item 3 minimum and (b) says item 1's or 2's). The Institute's yeshiva page charges "one who works … according to the wage". |
| F8 | s 348(e) temporary text (3769) | The date and its edges. | — | The expiry is 31.8.2026 (the editors' note, matching Amendment 9). A month ending by then is within the temporary text; "began before" is strict (one who began on 31.8.2026 is not reached in September); a quarter or year across the date, for one who began on or after it, is declined. |
| F9 | s 342(c)(2) (3662) | "for the time …": a month in which the age is reached after its first day, or the pension is payable for part of it. | (i) apportion the month; (ii) whole month one way | **declined**: the text speaks of time and the wage is monthly; how it is divided is not said. A month whose first day is on or after the day the age is reached is wholly "after". |
| F10 | s 342(c)(2) | "subject to s 245(b2)", which is repealed | — | **no effect**; checked red. |
| F11 | Schedule K "minimum wage" (4772) | Whose minimum wage? | — | **the particular employee's**, as the definition says (partial, daily or hourly as applicable): an input. The tests use the Institute's full monthly figure for an adult, and a scenario partial figure. For an employee with none given, item 1's minimum declines by name. |
| F12 | s 342(c)(1) (3661); s 335 (3611-3619) | Which branches are "contributions payable under s 335(a), (d), (e), (g), (h) or (i)"? | — | maternity ((a), (i)), accident injury ((d)), unemployment ((e)), disability ((g)), long-term care ((h)), senior citizens and survivors ((i)); read from s 335's text. Column D prints figures for exactly these (row IL-04's test). |
| F13 | s 342(c)(1) | A deduction branch with no column D amount in the case | — | **declined by name**, not taken as 0. An amount given for a branch (c)(1) does not name is ignored. |
| F14 | s 342(d) "coordinated contributions" (3664) | Does (c)(2) apply to what one employer "would have had to deduct"? | — | **yes**: one employer would have had to deduct under (c) as a whole. |
| F15 | s 342(e1) (3672) | The other employer deducted more than the coordinated contributions. | — | **declined**: (e1) speaks only of the kibbutz paying the difference. |
| F16 | s 342(f)(2) (3674) | "lower than" the threshold | — | **strict**; at the threshold the difference is nil anyway, so nothing turns on it. |
| F17 | s 342(b) and s 348(b) | With several employers, is (b)'s minimum applied to each employer's wage ("as if he alone were his employer") or to the total? | — | **not modelled**: the caller supplies the income the floor applies to. |
| F18 | s 350(c) (3805) | It disapplies s 348(b); does it reach (d) and (e)? | (i) (b) only; (ii) all minimums | **(i)**: it names (b) alone. A test shows a yeshiva student under s 350(c) still at the item 3 minimum. |
| F19 | s 342(c)(2) | The day a person "reaches" an age | — | the date of birth plus the age in months, keeping the day of the month or the month's last day when it is shorter (`add months`). |
| F20 | Schedule K "for a year" | A person in a category for part of a year | — | **not modelled**: the yearly figures are for the whole tax year. |
| F21 | s 342(c)(2) "the deduction in item 6 of Schedule J" | — | — | item 6 is unemployment (line 4725); only that branch's column D amount is left out for a police or prison officer. |
| F22 | s 342(e)(3)-(4) (3669-3670) | "column E of Schedule J" for deduction rates | (i) column D intended; (ii) as written | **not resolved**: (e) is a power and decides nothing here; checked red. |

**Where I looked for others and found none:** s 342(a)'s exception (one class, one limb); s 348(c)'s conditions (two facts of the order); Schedule K's yearly sums (the total of four quarters, read as written).

## 5. Answer table

Schedule K for 2026, with the basic amount 10,382, the average wage 13,769 (F1) in every month, and the full monthly minimum wage of an adult employee (6,247.67 in January; 6,443.85 in April, July and October).
"(F2)" marks a monthly figure the schedule does not print.

| item | max, month | max, quarter | max, year | min, month | min, quarter | min, year |
| --- | --- | --- | --- | --- | --- | --- |
| 1, employee | 51,910 | 155,730 | 622,920 | 6,247.67 (first quarter), 6,443.85 (others) | 18,743.01; 19,331.55 | 76,737.66 |
| 2, self-employed | 51,910 (F2) | 155,730 | 622,920 | 3,442.25 (F2) | 10,326.75 | 41,307 |
| 3, s 348(d) and (e) | 51,910 (F2) | 155,730 | 622,920 | 688.45 (F2) | 2,065.35 | 8,261.40 |
| 4, another insured | 51,910 (F2) | 155,730 | 622,920 | 2,065.35 (F2) | 6,196.05 | 24,784.20 |

With the s 1 average wage (13,566) the minimums would be 3,391.50, 678.30 and 2,034.90 a month; the Institute prints figures matching the table above, not these.

Worked figures the tests assert (2026 unless marked):

| facts | answer |
| --- | --- |
| employee, wage 60,000, March | income 51,910 (s 348(a)) |
| employee, wage 5,000, February / May | 6,247.67 / 6,443.85 (s 348(b)) |
| one who is neither, rent 12,000, January | 8,557.75 (the Institute: 8,558; with its composite rates, 1,035 a month) |
| one who is neither, rent 3,000 / no income | 2,065.35 |
| one who is neither, rent 4,000, under s 350(c) | 557.75 |
| unemployment benefit for a full month, income up to 688.45 / above it | 688.45 / declined (F5) |
| yeshiva student, no income / rent 5,000 | 688.45 / 1,557.75 (F6) |
| national-civic service begun 30.8.2026 / 31.8.2026, September 2026 | 688.45 / 2,065.35 (F8) |
| employer's deduction, wage 7,000, all branches (column D, temporary version) | 72.80; police officer 71.40; pension payable all month 0 (employer may reduce by 72.80) |
| man born 15.3.1956: February / March / April 2026 | 72.80 / declined (F9) / 0 |
| two employers at 6,000 each, permanent version, threshold 8,000 (scenario 2027) | each deducts 24; coordinated 218.80; the employee pays 170.80 |
| renewed kibbutz member, same, other employer deducted 24 | the kibbutz pays 194.80 |
| employee also self-employed, wage 5,000, self-employed income 6,000 | 2,703 at the reduced rate, 3,297 above |

## 6. Nouns to reconcile at IL-07

Read from the sibling deposits `legalese-2026-10-il-04` and `legalese-2026-10-il-06` (read-only); nothing here depends on IL-06 and nothing in either was changed.

- **Declared twice because IMPORT failed (section 8).** `A branch of insurance` and `A column of insured persons in Schedule J` are IL-04's, constructor for constructor; delete this row's copies at IL-07. The same for the three published figures whose names are IL-04's: `the reduced collection threshold for 2026, as published by the National Insurance Institute` and the two `the average wage from 1 January 2026 …` (same figures, different fetches).
- **Schedule J's column D.** This row's input `A branch's column D amount` (a branch and an amount) is IL-04's `the column D deduction under v on a wage of … in the branches …`, taken per branch. At IL-07, compute it there.
- **The case records.** IL-04's `An employee's month of contributions` (`calendar year of the month`, the branches, the monthly income, s 341 and s 343 flags) and this row's `An employee's month under section 342(c)` (`tax year`, `month`, the branches, the column D amounts, pension, age, police) and `An insured person's period under section 348` describe overlapping facts. The year field is `calendar year of the month` there and `tax year` here; a tax year is a calendar year in both (IL-04 F12). IL-04's `monthly income on which contributions are computed` is this row's output.
- **The person.** IL-04 `A person who works`; IL-06 `A person` (insured under Chapter 11, resident, a housewife under s 238 …); this row `An insured person, for section 342(a)-(b)` (column; insured under Chapter C only as a wife) and the age record `The insured person, for the age limb of section 342(c)(2)` (`a man` / `a woman` with her Part D age). IL-06 has `Father or mother`, a second sex distinction. `date of birth` is a field name here and in IL-06's `A child`.
- **The basic amount.** IL-06 `The basic amounts for the child allowance` (paragraph (2), fields `under paragraph (2)(a)` …); this row the paragraph (3) figure as a field of `The figures Schedule K reads for a tax year` and as `the basic amount under paragraph (3) from 1 January 2026, as published by the National Insurance Institute`.
- **Refusal wording.** For the year boundary: IL-04 per provision ("section 334(a) as it stood before 1 January 2026 is not in the deposited text"); this row once for the row ("this row answers contribution periods from January 2026 only"). For unpublished figures: IL-04 and this row "had not been published when this encoding was made"; IL-06 "had not been published when this model's sources were fetched".

## 7. Sources: what was fetched, and what was not

The deposited source was read and its sha256 verified (`78bf47ee…2a97`) on 2026-10-06 before use.

**National Insurance Institute pages**, fetched 2026-10-06 with curl directly (not through the proxy); bytes not deposited, the site reserving its rights:

| what | URL | UTC | sha256 | what it says that this row uses |
| --- | --- | --- | --- | --- |
| rates, self-employed | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9c%d7%a2%d7%a6%d7%9e%d7%90%d7%99%d7%9d.aspx` | 14:49:42 | `5d1e1a490b11bb63f1430677185a977045a173d32cde6fca5317836a34827567` | threshold 7,703; maximum income 51,910 a month; "one whose income is below 3,442 a month pays on the minimum income"; from 01.01.2026 |
| rates, employees | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9c%d7%a2%d7%95%d7%91%d7%93%d7%99%d7%9d%20%d7%a9%d7%9b%d7%99%d7%a8%d7%99%d7%9d.aspx` | 14:49:54 | `34ade94d9f315ad684979636e7b3d1e166cb09bf676b1ea1a20f4d82fa242c7b` | threshold 7,703 and maximum 51,910 from 01.01.2026 |
| rates, neither | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9e%d7%99%20%d7%a9%d7%90%d7%99%d7%a0%d7%9d%20%d7%a2%d7%95%d7%91%d7%93%d7%99%d7%9d%20%d7%95%d7%91%d7%a2%d7%9c%d7%99%20%d7%94%d7%9b%d7%a0%d7%a1%d7%94%20%d7%a9%d7%9c%d7%90%20%d7%9e%d7%a2%d7%91%d7%95%d7%93%d7%94.aspx` | 14:49:55 | `1c86c85f9a1fe65f5a95a6e0e1e9aa4fdc350aff2b518f75f6e0d633e12c8e92` | no income: 143 National Insurance and 123 health, 266 a month; rent of 12,000 in January 2026: "income up to 3,442 a month is exempt", charged on 8,558, 931.29 + 104.05 = 1,035 |
| yeshiva student, amount | `https://www.btl.gov.il/Insurance/National%20Insurance/type_list/yesivatalmid/Pages/SecomTlmidYesiva.aspx` | 14:51:01 | `39720f8c5ecbcec9ce267cb4a54905a6a9d07520b798e7c8c4c52a0e5da2125a` | 171 a month at the minimum from 01.01.2026; and (open question 3) a student who has not regularised his military status is charged from 1.1.26 "full National Insurance (without discount)", 95 more a month |
| not working, amount | `https://www.btl.gov.il/Insurance/National%20Insurance/type_list/NotWorking/Pages/ScomNotWorking.aspx` | 14:51:08 | `c2692a7d08e18b81a64c9a566e42a0e5727ad36a06b6c737af65aaec9e325efa` | 266 a month at the minimum "except a woman married to an insured resident" (cf. s 342(a)) |
| minimum income, self-employed (table) | `https://www.btl.gov.il/Mediniyut/GeneralData/rates_1954_2007/Hachnasa/Pages/ovedAtzmaii.aspx` | 14:49:44 | `c8f8edf3dfdc58db79ad61f6d32d3ef73dc6bfd1ec35a620a980acdb69d10a16` | from 01/01/2025: minimum 3,134, threshold 7,522, maximum 50,695 a month (no 2026 row) |
| minimum income, neither (table) | `https://www.btl.gov.il/Mediniyut/GeneralData/rates_1954_2007/Hachnasa/Pages/%d7%9c%d7%90%20%d7%a2%d7%95%d7%91%d7%93%20%d7%95%d7%9c%d7%90%20%d7%a2%d7%95%d7%91%d7%93%20%d7%a2%d7%a6%d7%9e%d7%90%d7%99.aspx` | 14:53:32 | `8bc34ff3f3fd636835d14ce7db26a4d904abf826afba1ce8bdce4f787df069be` | from 01/01/2025: 5% 627, 15% 1,880, maximum 50,695 a month |
| minimum income, employee (table) | `https://www.btl.gov.il/Mediniyut/GeneralData/rates_1954_2007/Hachnasa/Pages/Sahir_Maasik.aspx` | 14:53:30 | `3135d61d26977f6c1a4bfc5957f1752af65e266079eae90b40501db56965b9ca` | the employee's minimum is the minimum wage (not used for a figure: its 2025 rows date 6,247.67 from 01/02/2025, where the minimum wage page dates it from 01.04.2025) |
| average wage | `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%d7%a9%d7%9b%d7%a8%20%d7%9e%d7%9e%d7%95%d7%a6%d7%a2.aspx` | 14:49:57 | `0afd95b65113a99dfc9bb9cd277090a927d26fa0c39b49a75be4ec1931829532` | from 01.01.2026: 13,566 (s 1) and 13,769 (s 2), each for benefits and for contributions; 2025 for contributions 12,379 and 12,536 (0.0% change), for benefits 13,153 and 13,316 |
| basic amount | `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%d7%94%d7%a1%d7%9b%d7%95%d7%9d%20%d7%94%d7%91%d7%a1%d7%99%d7%a1%d7%99%20%d7%9c%d7%97%d7%99%d7%a9%d7%95%d7%91%20%d7%a7%d7%a6%d7%91%d7%90%d7%95%d7%aa.aspx` | 14:52:50 | `c585c6469d5c358d0230523208b54b6501ad624b06775eed2235f52bdc0a13d9` | basic amount 3, "for … computing the maximum income for collecting contributions": 10,382 from 1.01.2026, 10,139 from 1.01.2025 |
| minimum wage | `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%d7%a9%d7%9b%d7%a8%20%d7%9e%d7%99%d7%a0%d7%99%d7%9e%d7%95%d7%9d.aspx` | 14:52:49 | `0c7ff9205881f9b13396791c2b058bb511b1ec2e51bd6a9cb9ae20effa5ac743` | age 18 and over, monthly 6,443.85 from 01.04.2026, 6,247.67 from 01.04.2025 |

Also fetched and read, nothing taken: the category pages for self-employed, employees, the not-working, income not from work (with its tab pages), yeshiva students, national service (its amount tab printed no figure), the rates index, the General Data index and the 1954-on rates index. None is cited by a rule or test, and their sha256s are not recorded here (the session's fetch log was deleted with the fetched bytes at the end of the session).
The Institute's pages describe themselves as general information and not the binding text of the Law; they are used as the regulator's published figures and examples, not as law.

**Amending Laws from the Knesset**, fetched 2026-10-06 **through the Israeli-IP proxy** (an ssh tunnel to an EC2 instance; `curl --socks5-hostname localhost:1080`), PDFs, not deposited, text extracted with `pdftotext -raw`:

| Law | URL | UTC | sha256 | what it says that this row uses |
| --- | --- | --- | --- | --- |
| Law for the 2025 budget year (legislative amendments), Sefer HaChukim 3384, p. 395 | `https://fs.knesset.gov.il/25/law/25_lsr_6133485.pdf` | 14:54:06 | `eba7e1fa570a3ece265d87f379543024da038ee51af3f959d4c74162f5edecfa` | Chapter E, s 19(4): in s 342 "60% of the average wage" becomes "the reduced collection threshold"; s 19(6): the same "everywhere" in Schedule J, "as defined in s 334(a)"; s 20: amends s 7 of Amendment 252 (column C 0.17 to 0.16); s 21: the chapter commences 1 January 2026 |
| National Insurance Law (Amendment 252 and temporary provision), 5785-2025 | `https://fs.knesset.gov.il/25/law/25_lsr_5482787.pdf` | 14:55:34 | `d6c450ca0b869d1edb036b0f96bffbd79be6670336d9b5aa888da6cf2ecc8904` | s 6: commences 1 January 2025; s 7 (temporary provision, for contributions for 2025 and 2026, until 31 December 2026): in Schedule J, replaces the sub-column of column C headed "on the part not exceeding 60% of the average wage", and the sub-column of column D headed "on the part of the wage not exceeding 60% of the average wage", with new figures under the same headings |
| National-Civic Service Law (Amendment 7), 5785-2025 | `https://fs.knesset.gov.il/25/law/25_lsr_7458944.pdf` | 14:54:08 | `b0d30c46949e5aac77ae1d87cfb30bdd62a20fa2825a42bbc9e6feb53ee4716f` | s 36(a) expiry: 30.6.2025 becomes 15.11.2025 |
| National-Civic Service Law (Amendment 8), 5786-2025 | `https://fs.knesset.gov.il/25/law/25_lsr_9833371.pdf` | 14:54:10 | `2482417b87a0e0af223e0cbc9bd43fb90bfc1a798d22955dc735a6ce24e795c4` | 15.11.2025 becomes 31.3.2026; commences 16.11.2025 |
| National-Civic Service Law (Amendment 9), 5786-2026 | `https://fs.knesset.gov.il/25/law/25_lsr_12223999.pdf` | 14:54:12 | `cb19f7be69ae6b1b49057171cd00fda46c50e4997e37f51a2f240f7881888100` | 31.3.2026 becomes 31.8.2026 |

**Tags on s 348.** Counting the 5786 list at the head of the source (line 7) as row IL-04 counted 5785's: bare תשפ״ו is Amendment 8 of the National-Civic Service Law (p. 18) and תשפ״ו־7 is its Amendment 9 (p. 470); with IL-04's count, תשפ״ה־11 is its Amendment 7.
Each only moves that Law's expiry date, so these tags record the date in the editors' note on s 348(e)'s temporary text, not a change of s 348's words.

**Attempted and failed:** nothing.
**Not attempted:** the Central Bureau of Statistics (the average wage and the index are taken as published by the Institute); a search for an amendment of the National-Civic Service Law after Amendment 9.

## 8. The cross-directory IMPORT, and what was done instead

The brief asked for IL-04's modules to be imported by relative path.
With this binary, `IMPORT \`../legalese-2026-10-il-04/nii-il04-nouns\`` (and the same for `nii-s334-interpretation` and `nii-schedule-j`) fails with "I could not find a module with this name: nii-il04-nouns": the resolver reduces the path to its bare module name and tries the importing file's own directory, the embedded library, `~/.local/share/jl4/libraries/` and the VS Code bundle (tested 2026-10-06; the probe file was deleted).
The library-resolution reference in l4-ide (`doc/reference/libraries/resolution.md`) says the CLI's project root is the importing file's own directory.
The only other route, `JL4_LIBRARY_PATH`, the brief forbids.

A symlink was also tried, in the scratchpad only: a symlink to IL-04's `nii-schedule-j.l4` resolves, but that module's own imports (`nii-il04-nouns`, `nii-s1-definitions`, `nii-il04-published-figures`) are then looked for beside the symlink and not found, so the whole import closure would have to be linked.
Nothing was linked in the deposit.

So, as the brief directs, this row declares again the IL-04 types it needs with the same names and constructors, takes IL-04's computed results (the column D amounts, the threshold) as inputs, and uses IL-04's published-figure names for the three figures both rows need.
Section 6 lists what to delete or join at IL-07.

## 9. Observations about the source, for whoever maintains it

- **s 342(e)(3)-(4) say "column E" of Schedule J for deduction rates**; the deduction is column D (F22; red).
- **s 342(c)(2) is subject to s 245(b2)**, which is repealed (F10; red).
- **Schedule J's temporary table, column D (row IL-04's fork F3).** The consolidation prints the temporary table's column D upper heading as "above 60% of the average wage" and the lower one as "not above the reduced collection threshold" (line 4718). The enacted texts, as read here: Amendment 252 s 7(a)(3)(b) replaces only column D's lower sub-column, under its own heading "not exceeding 60% of the average wage"; the upper sub-column is the main Law's, whose "60% of the average wage" the 2025 budget-year Law s 19(6) replaced "everywhere" in Schedule J with "the reduced collection threshold" from 1 January 2026, and s 20 of that Law amended s 7's figures but not its headings. On that reading the 2026 upper heading is "above the reduced collection threshold", as in the permanent table, and the "60%" survives in the enacted text only in s 7's lower heading. This is this row's reading of three texts, offered as evidence on IL-04's F3; nothing in this row turns on it, because its s 342(c) takes the column D amounts as inputs.
- **The editors' note dates s 348(e)'s temporary text to 31.8.2026**, which matches Amendment 9; the National-Civic Service Law's expiry was moved three times in 2025-2026, the second time (Amendment 8, passed 18.11.2025) after the date it replaced (15.11.2025), with commencement on 16.11.2025.

## 10. Open questions for a domain expert

1. F1 (and IL-04's F5): is "the average wage" in Schedule K and s 348(a1) the figure calculated under s 2 (the Institute's practice), for every provision of Chapter 15?
2. F3 and F5: does the Institute read s 348(a1) as a deduction because of the text, or by practice; and does it read s 348(d) as a deeming or a floor?
3. The Institute's yeshiva page says a yeshiva student who has not regularised his military status is charged from 1 January 2026 the full contributions, "95 NIS more each month" (the difference between the item 4 and item 3 minimums). Nothing in the deposited s 348(e) or Schedule K turns on military status. Where is that rule?
4. F6 and F7: which Schedule K item applies to a yeshiva student or a volunteer who also works, and below what income?
5. F9: how does the Institute apportion a month in which an employee reaches 70 (or her Part D age), or in which a pension begins?
6. F22: is "column E" in s 342(e)(3)-(4) a remnant of an earlier numbering of Schedule J's columns?
7. Was the National-Civic Service Law's expiry moved again after 31.8.2026, and if not, does s 348(e)'s temporary text now reach only those who began before?

## 11. What was not done

- **The independent test pass** (skill step 8) was not run: the brief for this row is one session with no sub-agents. Every expected value was worked out before it was asserted, by a computation that does not use this encoding; no second reader has derived them.
- **HG1**, a human who knows Israeli national insurance reading the modules against the Hebrew, has not been sought.
- **Semi-cleanroom** (ruled 2026-10-06): nothing from the Axiom Foundation, any RuleSpec repository, or the paths the brief lists was read, searched or fetched in this session. IL-04's and IL-06's deposits were read for names only, read-only; IL-04's `tests-independent.l4`, `DECIDED-ANSWERS.md` and `INDEPENDENT-FINDINGS.md` were not opened.
