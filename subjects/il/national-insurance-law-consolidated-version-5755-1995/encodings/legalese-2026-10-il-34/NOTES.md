# Notes: National Insurance Law, the contributions surroundings (row IL-34)

Version 0.1.1, draft (0.1.0 plus the repairs of section 13).
Run `IL-34-20261008`, encoder `enc-il-34`, 2026-10-09 (SGT); the check run below is 2026-10-09T00:00Z.
Read BRIEF.md first for the scope and the rules.
Every Markdown sentence here is on its own line, so a grep hit is a whole sentence.

## 0. What is encoded and what is not

**Encoded, in the lead's priority order.**

1. **The expiry of the National-Civic Service Law and s 348(e)'s temporary text** (IL-05's 05-Q7): the Civic Service Law's s 36(a) and (b), and the end of s 348(e)'s temporary text, in `nii-s348e-civic-expiry.l4`.
2. **s 341 and the Order of 5759-1999** (`nii-s341-order-5759-1999.l4`); **Schedule K1 and s 369(a)** (`nii-schedule-k1-s369.l4`).
3. **The several-employers regulations of 5757-1997**, which exercise s 342(e) (`nii-s342e-several-employers.l4`).
4. **Schedule A1 Parts A, B, C, E:** not re-encoded; row IL-33 holds them (section 1, coverage table).
5. **The remaining sections:** `nii-s2-average-wage-and-schedule-a.l4` (s 2, Schedule A), `nii-s28-s32-accounts-and-treasury.l4` (ss 28, 28A, 28B, 32), `nii-s336-s340-s343.l4` (ss 336, 340, 340A, 343), `nii-s344-s347-income.l4` (ss 344, 344A, 345, 345A, 345B, 346, 347), `nii-s349-s351-exemptions.l4` (ss 349, 350, 350A, 351 and Schedule K16).
6. **The Institute's charge on yeshiva students:** refused by name (`nii-il34-needs-a-source.l4`); no text was found.

**Not encoded.**
Anything the row does not name (ss 29 to 31, 33 to 36, 352, and s 369 beyond (a)); every Minister's order and regulation that is not deposited (section 8); the Income Tax Ordinance's provisions the sections cite (ss 2, 47, 47A, 60A, 87B, 102, 122, 122A, 125B, 125C, which are rows IL-01 to IL-03 or not encoded).

**The nouns module** is `nii-il34-nouns.l4` (`DECLARE` only).
It imports row IL-04's nouns for `A branch of insurance` and `A column of insured persons in Schedule J`.

**Vendored, unchanged, with sha256 in `VENDORED.sha256`:** four modules of row IL-04 (`nii-il04-nouns.l4`, `nii-s1-definitions.l4`, `nii-il04-published-figures.l4`, `nii-s334-interpretation.l4`), because the Order's amount since 2026 is s 334(a)'s threshold, which IL-04 computes.
Their last commit is 0720ea90; they are byte-identical to the originals (`cmp`) and `shasum -a 256 -c VENDORED.sha256` passes.

## 1. Coverage table

Dispositions: `encoded`; `inert` (quoted, nothing to compute: a power, a repeal, a definition that only labels); `out-of-scope` (with a reason).
No row is `deferred`.
"Rule" names the module and the main rule; source line numbers are lines of the Law's deposited text unless the tag says otherwise (`civic`, `order`, `reg`).

### Priority 1

| provision | line | disposition | where |
| --- | --- | --- | --- |
| Civic Service Law s 36(a), the Law stands until 31.8.2026 | civic 330 | encoded | `nii-s348e-civic-expiry.l4`: the expiry day, `the National-Civic Service Law is in force on` (forks C1, C2) |
| Civic Service Law s 36(b), the Law goes on applying to one who began before the expiry | civic 331 | encoded | `s 36(b) — the Law applies to one who began service on` |
| Civic Service Law s 37(f), the commencement day is on or before 30.6.2014 | civic 339 | encoded as a bound | `National-Civic Service Law — the last day on which its commencement day may fall, from s 37(f)`; a day up to it is declined (needs a source: the commencement day) |
| Civic Service Law s 1 "משרת בשירות לאומי–אזרחי" | civic 36 | inert | cited; the NII s 1 definition (line 173) is the one the rules read |
| NII s 348(e), temporary text, and s 1 "משרת בשירות לאומי–אזרחי" (line 173) | 3769, 173 | encoded | `s 348(e) — the temporary text reaches one serving in national-civic service who began on` (fork C3) |
| The Institute's charge on a yeshiva student who has not regularised his military status | none | refused by name | `nii-il34-needs-a-source.l4` |

### Priority 2

| provision | line | disposition | where |
| --- | --- | --- | --- |
| s 341, the Minister's power over reduced rates | 3654-3655 | encoded | `s 341 — the order is validly made` |
| s 341, last limb (old orders read as the threshold) | 3655 | encoded | with the Order: `Order of 5759-1999 s 1 — the amount of wage or income for the month` |
| s 341, the note naming the Order | 3656 | inert | a pointer |
| Order s 1, the amount fixed by the quarter's first month | order 15-16 | encoded | the same rule; fork O1 for a quarter |
| Order s 2, repeal of Order No. 2 of 5747-1987 | order 18-19 | inert | the repealed Order is not deposited: a day before 1.1.1999 is refused by name |
| Order s 3, in force from 1.1.1999 | order 21-22 | encoded | `Order of 5759-1999 s 3 — the Order applies to contributions payable for the day` |
| Order s 4, the temporary reach to an employee to 31.3.2000 | order 24-25 | encoded | `Order of 5759-1999 s 4 — s 1 reaches an employee, by this section alone, on the day` |
| s 342(e)(1) to (4), the Minister's powers | 3666-3670 | inert | they are exercised by the regulations below |
| s 342(e), the note naming the regulations | 3671 | inert | a pointer |
| Schedule K1, columns A and B, items 1 to 3 | 4775-4783 | encoded | `Schedule K1 — the multiple of the average wage for a breach from…`, `Schedule K1 — the most the clerk may charge…` (forks K1 to K3) |
| s 369(a), the clerk's charge and the cap by K1 | 4014-4015 | encoded | `s 369(a) — the most the Institute can charge the employer…` |
| s 369(a1) to (e) | 4016-4026 | out-of-scope | not named by the row (notice, 45 days, 30 days, interest, division, the five-year limit, collection) |

### Priority 3: the regulations of 5757-1997

| provision | line | disposition | where |
| --- | --- | --- | --- |
| reg 1, definitions | reg 14-20 | inert | "coordinated contributions", "full rate", "total income" are inputs; "half the average wage" is not gating (section 3) |
| reg 2, the full rate on the whole wage | reg 22-23 | encoded | `Regulations of 5757-1997 reg 2 — where…, the deduction from a wage of…` |
| reg 2A, the form | reg 25-26 | encoded | `…reg 2A — the employee is bound…`, `…the form was handed over in time` |
| reg 3(a), the collection clerk's certificate | reg 29 | encoded | `…reg 3(a) — the clerk may give the employee a certificate` |
| reg 3(b), the employer deducts as directed | reg 30 | inert | the clerk's directions are the input |
| reg 3A(a), the secondary employer's sum | reg 33 | encoded | fork N1 |
| reg 3A(b), (c), the months | reg 34-35 | encoded | `…reg 3A(b)-(c) — the secondary employer may deduct for month…` |
| reg 3A(d), "wage certificate", "employer" | reg 36-38 | encoded | `…reg 3A(d) — it is a wage certificate` |
| reg 3B | reg 40-41 | encoded | `…reg 3B — reg 3A applies…` |
| reg 3C | reg 43-44 | encoded | `…reg 3C — a complete request for a refund` |
| reg 4(a), the account | reg 47 | encoded | `…reg 4(a) — the employee must file an account…`, the due day |
| reg 4(b), the employer's certificate | reg 48 | inert | a duty with no figure; the mis-citation "reg 3B [should be 3C]" is the text's own note |
| reg 5, the employee pays | reg 51 | encoded | `…reg 5 — the difference the employee pays…` |
| reg 6(a), (b), the refund | reg 54-55 | encoded | `…reg 6(a)…`, `…reg 6(b)…` |
| reg 7, linkage | reg 58-60 | encoded | `…reg 7(1)…`, `…reg 7(2)…` (fork N2) |
| reg 8, from 1.3.1997 | reg 63 | encoded | `…reg 8 — regulations 2 and 3 apply to a monthly income paid for the day` |
| reg 9, the transition | reg 66 | encoded | `…reg 9…` |

### Priority 4: Schedule A1

| provision | line | disposition | where |
| --- | --- | --- | --- |
| Schedule A1 Part A (retirement age) | 4369-4396 | out-of-scope here | encoded by row IL-33 (`nii-schedule-a1-ages.l4`), which pins it in its BRIEF; two competing age tables would be worse than one |
| Part B (maximum age for unemployment insurance) | 4399-4412 | out-of-scope here | row IL-33, same file |
| Part C (not insured under Chapter 11 by age) | 4415-4428 | out-of-scope here | row IL-33, same file |
| Part D (women's old-age pension age) | 4431-4453 | out-of-scope here | row IL-08 (`nii-schedule-a1-part-d.l4`) |
| Part E (woman exempt from the qualifying period by age) | 4456-4475 | out-of-scope here | row IL-33, same file |

I told the lead of this overlap by message on 2026-10-09 and asked to be corrected if a duplicate was wanted; no reply had arrived when this was written.

### Priority 5

| provision | line | disposition | where |
| --- | --- | --- | --- |
| s 2(a), "שכר מדוד", "חודש שכר חריג", "שכר מדוד מתוקן" | 232-235 | encoded | `nii-s2-average-wage-and-schedule-a.l4`: `s 2(a) — month… is an exceptional wage month`, `s 2(a) — the corrected measured wage…` (fork W1) |
| s 2(b)(1), (2) | 236-238 | encoded | `s 2(b)(2) — the monthly difference…`, `…the average wage increased…` |
| s 2(b)(3) | 239 | inert | lapsed |
| s 28(a) | 449 | encoded | `s 28(a) — the sum credited to the account of the branch…` |
| s 28(b) | 450 | encoded | `s 28(b) — the transfer between two branch accounts is allowed` |
| s 28(c) | 451 | inert | deleted |
| s 28(d) | 452 | encoded | `s 28(d) — the rule dividing the general expenses is valid` |
| s 28A | 454-455 | encoded | the day and the branch |
| s 28B | 457-461 | encoded | the window, `s 28B(1)`, `s 28B(2)`, `s 28B(3)` |
| s 32(a) | 477-489 | encoded | `s 32(a) — the Treasury's percentage for the year…`, the allocation, the validity of a change |
| s 32(b), (c), (c3), (d), (e), and the paragraphs lettered ט, י, יא | 490-491, 498-500, 511-513 | inert | repealed or lapsed |
| s 32(c1) | 492-496 | encoded | `s 32(c1)(1) — the monthly payment…` |
| s 32(c2), (h) | 497, 510 | encoded | `s 32(c2) and (h) — the reimbursement of expenses of…` (the identity) |
| s 32(f) (lettered ו) | 501 | inert | the manner of payment is by agreement |
| s 32(g) (lettered ז), paragraphs (1), (2) | 502-509 | encoded | forks S1, S2 |
| s 336 | 3622-3623 | encoded | `s 336 — the last day of the payment period…` |
| s 340(a)(1), (b) | 3638-3639, 3641 | inert | (a)(1) points at Schedule J item 4 and s 337 (row IL-04); (b) is a power |
| s 340(a)(2) | 3640 | encoded | `s 340(a)(2) — the rate fixed for another insured person is valid…` |
| s 340(c) | 3642 | encoded | `s 340(c) — the maternity insurance rate…` |
| s 340(d), (e) | 3643-3644 | encoded | with the temporary figures of Amendment 252 |
| s 340A(a), (b) | 3647-3649 | encoded | `s 340A — the employer's contributions…`, `s 340A(a)(2) — the most the employer may deduct…` |
| s 340A(c) | 3650-3652 | inert | definitions (a household worker; "wage" is income under ITO s 2(2)) |
| s 343 | 3677-3680 | encoded | `s 343 — the employer is one the Minister may approve`; the reduced sum is the Minister's, refused by name |
| s 344(a) | 3685 | encoded | `s 344(a) — the first day of the month whose income is the monthly income…` |
| s 344(a)(1) | 3686-3693 | encoded | fork D1 |
| s 344(a)(2) | 3694 | encoded | an identity on the replaced person's income |
| s 344(b), (d) | 3695, 3697 | encoded | the validity of an order |
| s 344(c) | 3696 | inert | a power |
| s 344A(a) | 3700 | encoded | an identity on the grossed-up budget (input) |
| s 344A(b), (c) | 3701-3702 | inert | labels (income by status; income under ITO s 2(5) at column D except item 6) |
| s 344A(d), (e) | 3703-3704 | inert | the member's share of the paid surplus is the caller's; the rule gives the label |
| s 344A(f), (h) | 3705, 3707-3713 | encoded | the surplus (fork D2) and the annual income attributed from the unpaid surplus |
| s 344A(g) | 3706 | inert | s 348 applies (row IL-05) |
| s 345(a) | 3716 | inert | the sources; the assessed income is input |
| s 345(b)(1) | 3717-3719 | encoded | `s 345(b)(1) — the annual income of another insured person` |
| s 345(b)(2), (b)(3), (c)(2), (c)(3), (d), (f) | 3720-3723, 3725-3727, 3729-3734 | inert | procedure, powers and cross-references (s 364, s 362(a)(3), the regulations on advances, not deposited) |
| s 345(c)(1) | 3724 | encoded | `s 345(c)(1) — the difference the insured pays…` |
| s 345(e) | 3728 | encoded | `s 345(e) — the income on which the advance is paid…` |
| s 345A(a), (d), (e) | 3737-3740, 3743-3744 | inert | definitions, a power, a lapse |
| s 345A(b), (c) | 3741-3742 | encoded | the month of the income; the employer; the sum |
| s 345B(a), (b), (d), (f) | 3747-3748, 3751, 3754 | inert | the definition; the rate (column D except item 6, row IL-04's Schedule J); the deduction at source; a power |
| s 345B(c) | 3749-3750 | encoded | `s 345B(c) — the early pension on which contributions are paid…` |
| s 345B(e) | 3752-3753 | encoded | `s 345B(e)(2) — the part of the early pension…charged at the reduced rate…` |
| s 346 | 3757 | encoded | an input, or refused by name |
| s 347 | 3760 | encoded | `s 347 — the clerk may determine the contributions…` |
| s 349 | 3772 | encoded | the validity of an order |
| s 350(a)(1) to (9) | 3775-3795 | encoded | `s 350(a) — the receipt is not regarded as income for contributions…` (fork L1) |
| s 350(b), the orders | 3796-3799 | inert | a power; the orders are named in the notes and not deposited (their receipts are given as a kind) |
| s 350A(a), (c) | 3803, 3805 | encoded | the window, the immigrant, the exempt income, `section 348(b) does not apply` (fork L2) |
| s 350A(b), (d), (e) | 3804, 3806, 3807 | inert | (b) is a rule for the benefit rows; (d) a power; (e) a report |
| Schedule K16 | 4845-4850 | encoded | `Schedule K16 — the countries` (one country) |
| s 351(a) | 3810 | encoded | `s 351(a) — the income on which contributions are paid for an employee…` |
| s 351(b), (c), (d), (f), (g), (g1), (h), (i), (j) | 3811-3822 | encoded | `s 351 — contributions under… are not payable for him`, `s 351 — he pays no contributions at all` |
| s 351(e) | 3814 | inert | repealed |
| s 351(k)(1) to (3) | 3823-3835 | encoded | `s 351(k) — a limb applies to him` |
| Schedule A | 4360-4365 | encoded | `Schedule A — the minimum average monthly income for month…` |
| ss 29 to 31, 33 to 36, 352 | 463 ff, 3837-3841 | out-of-scope | not named by the row |

## 2. Fork register

All seventeen are **ruled by Meng 2026-10-08 (SHRUG)**: one named switch, default a refusal by name; every other reading kept by name and tested.
Each switch declines **only where the readings give different answers to the question asked**; where they agree the question is answered.
The refusal message is the fork's own sentence, quoted in the tests.

| id | provision (line) | the question the text does not decide | readings (constructor names in `nii-il34-nouns.l4`) | default |
| --- | --- | --- | --- | --- |
| C1 | Civic Service Law s 36(a) (civic 330) | whether a later Act moved the expiry after the deposited text (the consolidation of 2026-04-01, last amendment No. 9) | `the expiry stays as the deposited text states it`; `a later Act moved the expiry to` a date; declined | declined: answered when the printed day already answers TRUE (nothing falls as the day moves later), otherwise refused |
| C2 | Civic Service Law s 36(a) | is the expiry day itself a day of the Law ("stand in force until the day") | in force through the day; ends at the start of the day; declined | declined (only the day itself is affected) |
| C3 | NII s 348(e), editors' note (3769), s 1 (173) | does the temporary text end with the Civic Service Law whenever that is, or on the printed 31.8.2026 | follows the Civic Service Law; fixed at 31.8.2026; declined | declined: both ends are asked; answered if they agree |
| O1 | Order of 5759-1999 s 1 (order 15) | how a quarter's amount relates to a month's ("for each month in the quarter and for a quarter") | three times a month's; declined | declined |
| N1 | reg 3A(a) (reg 33) | what the secondary employer deducts when the others have already deducted more than the coordinated contributions | nothing; declined | declined (zero difference is answered 0) |
| N2 | reg 7(2) (reg 60) with s 362(a)(1) | the addition to a refund when the index fell | no addition; the refund is reduced by the rate of the fall; declined | declined |
| K1 | s 369(a) (4015) | to what day "the period that elapsed" runs | to the insured event; to the day the arrears were paid or the employer registered; declined | declined: both are asked |
| K2 | Schedule K1 column B (4781-4783) with s 369(a) | whether the benefits limb counts benefits in kind (column B says "cash benefits", s 369(a) charges cash and kind) | cash only; cash and kind; declined | declined: answered where they agree (kind nil, or cash already over the multiple) |
| K3 | Schedule K1 | the maximum for a breach of 30 days or less (no row) | no charge may be made; limited by the benefits limb alone; declined | declined |
| W1 | s 2(a) (235) | whether the "compensation" added to the corrected measured wage is its rate of the earlier month's wage or an amount in shekels | the rate; the amount; declined | declined (nil compensation is answered) |
| S1 | s 32(g)(1) (502-508) | what a negative product (the entitled population grew slower than the general one) reimburses | nothing; taken as it comes; declined | declined |
| S2 | s 32(g)(2) (509) | the ceiling when the index fell | stays; lowers; declined | declined |
| D1 | s 344(a)(1) (3686-3693) | whether the kibbutz figures are the year's (the monthly income a twelfth of their sum) or the month's | year; month; declined | declined |
| D2 | s 344A(h) (3709) | a negative surplus of a renewed kibbutz | nil; taken as it is; declined | declined |
| L1 | s 350(a)(7) (3793) | do the two exceptions (early pension; income the Minister of Finance determines) follow the last kind only, or all three kinds | last kind only; all three; declined | declined, and only where the Minister of Finance determined a rental income to be income |
| R1 | s 28(a) (449) with Schedule J (4720-4730) | whether the ratio of the rates is to the SUM of the rates given or to the column's PRINTED TOTAL (the cells of a column need not add to its printed total) | to the sum; to the printed total; declined | declined, for a caller that gives the printed total and where the two amounts differ; the plain list form is at the sum |
| L2 | s 350A(a) (3803) | whether five years "have not yet passed" on the fifth anniversary of the visa day | passed on the day; not passed until the day after; declined | declined, and only on the anniversary itself |

Each switch has a public rule that answers at the switch, and a form with the reading as an argument that takes any named reading; the old and new names are listed in the tests.

## 3. Not gating, and what I assumed

**Looked at and found not to change any answer.**

- **The Order's "first month of the quarter" rule.** Since 1.1.2026 the amount is s 334(a)'s threshold, which moves only on 1 January, so every month of a year has the year's figure whichever quarter month is read.
  The tests show all twelve months of 2026 at 7,703.
- **"Half the average wage" in the regulations (regs 1, 2).** The Law now says "the reduced collection threshold" (s 334(a); the 2025 Budget-year Law s 19(4) changed the Law's own wording, not the regulations').
  The regulations' amounts do not turn on which: reg 2 puts the full rate on the whole wage, and the full rate is the rate of the band above the threshold, wherever the threshold is.
- **"Column E" in reg 1 and s 342(e)(3).** Both name column E where Schedule J's deduction rates are column D (IL-05's fork F22).
  The rate is an input here, so this row takes no side; two instruments naming column E is a small fact for whoever rules F22.
- **Reg 3A(c), "the second half after 1 June".** Every day of the second half is after 1 June, so the clause adds nothing; the reference day of the first half is 1 January.
- **Reg 4(b)** cites "reg 3B" and the text's own note corrects it to 3C.
- **ss 340(d), (e), 340A:** the consolidation prints the base figures in the text and the 2025 and 2026 figures in editors' notes.
  Amendment No. 252 s 7(a) is the source of the larger figures: for contributions collected for 2025 and 2026, from 1.1.2025 to 31.12.2026 (21 Tevet 5787), the Law is read with 0.53%, 0.13%, 7.85%, 1.8% and 3.6%; s 7(b) lets the Minister of Finance extend it to 2027 and then 2028 by order.
  The year, and whether an order extended it, decide the figure.
  Before 2025 the provisions did not exist (their s 6 commencement is 1.1.2025).
- **s 32(a):** the percentages for 2025 to 2029 come from Amendment 252 s 2 (2025: 47.07%) and the 2025 Budget-year Law s 19(1) (2026: 44.57%, 2027: 55.40%, 2028: 56.47%, 2029 on: 56.52%, from 1.1.2026 by its s 21), checked against the deposited PDFs.
  If the Minister of Finance extended Amendment 252's temporary period for 2027 or 2028, the percentage is 44.26% or 45.39% (that Act's s 7(b), as the Budget-year Law s 20(2) changed it from 47.74% and 49.27%).
- **s 351(b)'s "subject to s 245(b2)"** is repealed (IL-05's fork F10 notes the same for s 342(c)(2)).
- **Order s 4** (the temporary reach to employees until 31.3.2000) and the amended s 1 (which names employees outright) agree for every day after 1.1.1999.

**Assumed, not ruled (each is in a place a revert would touch only that rule).**

- **A1.** The Civic Service Law began on or before 30.6.2014 (its s 37(f) speaks of a period "from the commencement day until 30 June 2014").
  A day up to 30.6.2014 is declined; the commencement day itself is not in the deposited text.
- **A2.** A tax year is a calendar year, as in the other rows of this subject.
- **A3.** The days elapsed in Schedule K1 are the end less the start (the first day does not count); "6 months" and "12 months" are `add months` from the start, which clamps a 31st.
  The text does not say how days are counted at the 30-day edge.
  A reviewer who counts both ends moves the edge by one day: the tests at 30 and 31 days (14 and 15 February 2026 from 15 January) are where.
- **A4.** Reg 6(a)'s "within seven years from the end of the tax year" ends on 31 December of the tax year plus seven (for tax year 2018, 31.12.2025), and that day is in time.
- **A5.** Reg 6(b)'s "within three months from the day of receipt" is `add months` 3 from the day.
- **A6.** In s 351(k) a month limit is inclusive ("up to 12 months", "the first two months"), counted to the end of the period asked about; the age limit of (2a) is 18 inclusive to 21 exclusive.
- **A7.** From 1.4.2000 the Order's s 1 reaches employees by the deposited text; the commencement of the 5760 amendment (Kovetz HaTakanot 5760 p. 778) is not deposited.
- **A8.** s 345(c)(1): a net that the benefit difference turns negative means nothing is payable (not a payment by the Institute).
- **A9.** s 345B(c)(1): when the other income already reaches the maximum, nothing of the pension counts.
- **A10.** s 340(d) and (e) are monthly amounts (the average wage is a monthly figure; the text names no period).
- **A11.** s 344(a)(1)(a): the housing value is 7.5% of the basic amount a member a month (the "times the number of members" divides out when the services value is divided by the members).
- **A12.** s 350A(a): the income exempt is the part of the income "on which he pays social insurance in the country he came from"; the caller gives that part.
- **A13.** Country names in the `A new immigrant` record are matched as strings; Schedule K16's one country is matched in the Hebrew of the Schedule.
- **A14.** The heading "s 2(b) average wage" of Schedule K1 is an input; this row does not decide whether the figure is the s 1 average wage with s 2(b)'s changes or the figure the Institute publishes for contributions (row IL-04 carries two published figures under two labels).

## 4. How this row feeds the others

**Row IL-05 (ss 342, 348, Schedule K).**

- Its constant `the expiry of the National-Civic Service Law, which ends the temporary text of section 348(e)` is 31.8.2026, which is this row's reading C1 "the expiry stays as the deposited text states it".
- This row's rule `s 348(e) — the temporary text reaches one serving in national-civic service who began on… for the span…` is IL-05's `s 348(e) — the person serves in national-civic service in a period the temporary text reaches`, with the end of the temporary text made a switch.
- **At this row's switch, two of IL-05's answers are declined and not FALSE:** a person who began on 31.8.2026 for September 2026 (IL-05's tests line 462) and one who began on 15.9.2026 for the fourth quarter of 2026 (line 466).
  Both are "the temporary text does not reach him" if the Law's expiry stands, and "it does" if a later Act moved it.
  IL-05's other civic-service answers (lines 458 to 460, 463, 465) are the same here: TRUE, TRUE, TRUE, TRUE, and the straddling quarter declined with the same message.
  Whether IL-05 should take this switch is the lead's; I did not edit IL-05.
- Its inert (e) (`the deduction is governed by regulations under section 342(e)(3) or an approval under section 342(e)(4)…`) is what the regulations of this row encode: `reg 2` (the deduction at the full rate), `reg 3` and `reg 3A` (the other approved deductions).
- Its `s 342(d) — "coordinated contributions", for…` and `…the outcome, for the deductions…` are the inputs `the coordinated contributions` and `the actual deduction` of regs 3, 3A, 5 and 6.
- Schedule K1, which it listed as out-of-scope, is `nii-schedule-k1-s369.l4`.

**Row IL-04 (ss 1, 334, 337, Schedule J).**

- The Order's amount calls IL-04's `s 334(a) — the reduced collection threshold for a month in` (vendored, unchanged), so 2027 and 2028 are refused with IL-04's own message and 2029 on likewise.
- The Order's rule for 2006 to 2025 (60% of the average wage of the quarter's first month) and for 1999 to 2005 (half) is given with the average wage as an input; IL-04 declines 2025 and earlier and this does not change that.
- Schedule A's sum, which IL-04's `s 1 — a self-employed person in the period…` takes as an argument, is `Schedule A — the minimum average monthly income for month…`.
- s 28(a) reads Schedule J's rates by branch; the rates are the caller's (IL-04 holds the table), and the tests use the printed items of the 2025-2026 table (self-employed, above the threshold: 0.94, 2.74, 0.78, 0.09, 2.12, 0.21, 5.95, which add to the printed total 12.83).

**Row IL-08 (the NII half: s 72, s 335, Part D).**

- `s 351 — contributions under… are not payable for him` is by the letters of s 335 (`A subsection of section 335`); IL-08's `nii-s335-branches.l4` maps the letters onto branches, and the two compose.
- The age of s 351(b) for a woman is Schedule A1 Part D (IL-08); the caller supplies whether it has been reached.

**Row IL-33** holds Schedule A1 Parts A, B, C, E, and s 238 (a "housewife" and "widow with a pension", which s 351(h) to (j) read as booleans here).

**The capstone (IL-44/IL-55 follow).**

- Nothing the capstone computes today changes.
- What it would need: a decision on C1 to C3 (the temporary text of s 348(e)); the readings of N1, N2 only if it computes several-employer coordination; and a choice of how it takes the exemptions of s 351 and the non-income of s 350 for its four modelled statuses.

## 5. Answer table

All amounts are shekels; rates are fractions. "Switch" is the default of section 2.

| question | answer | provision |
| --- | --- | --- |
| Is the Civic Service Law in force on 30.8.2026, 31.8.2026, 1.9.2026, 9.10.2026? | yes; declined (C2); declined (C1); declined (C1) | s 36(a) |
| The Law applies on 9.10.2026 to one serving who began on 1.7.2026; who began on 31.8.2026? | yes (all readings); declined (C1) | s 36(b) |
| Does the temporary text of s 348(e) reach a civic servant who began 1.9.2025 for September 2026; who began 31.8.2026 for August 2026; for September 2026; for the third quarter 2026? | yes; yes; declined (C1); declined (the span straddles the end, the message of IL-05) | s 348(e) |
| The Order's amount, any month of 2026 | 7,703 | Order s 1, s 334(a) |
| The same for 2025 with the average wage 12,536 | 7,521.6 (60%) | Order s 1, s 341 last limb |
| A quarter's amount, 2026 | declined (O1); 23,109 at "three times" | Order s 1 |
| The Treasury's percentage 2018 to 2029 | 57.16, 55.96, 55.74, 57.26, 53.89, 58.88, 59.81, 47.07, 44.57, 55.40 (44.26 if extended), 56.47 (45.39 if extended), 56.52 | s 32(a) |
| The monthly Treasury payment on 1,000,000 from employers and 200,000 from the self-employed | 82,300 | s 32(c1)(1) |
| Work-injury contribution for training, 2026, average wage 13,566 | 35.9499 (0.53% of 6,783); 27.132 in 2027 with no order | s 340(d) |
| Household worker, a quarter's wage of 30,000, 2026 | 2,355 (insured), 1,080 (not); the deduction at most 540 | s 340A |
| Schedule K1: the multiple for over 30 days to 6 months; to 12; over 12 | 5; 10; 20 times the average wage (not above the benefits) | Schedule K1 |
| The 4(a) account of tax year 2026 is due | 31.7.2027 | reg 4(a) |
| The last day to file an account for tax year 2018 | 31.12.2025 | reg 6(a) |
| The refund is due three months after 31.1.2026 | 30.4.2026 | reg 6(b) |
| A fall of the index from 100 to 99 on a refund of 1,000 | declined (N2); 0 or -10 at the named readings | reg 7(2) |
| An early pension of 10,000 with other income 45,000, maximum 51,910 (an input) | 6,910 counts | s 345B(c) |
| A pensioner of 500 with no other income (item 3 minimum 5% x 13,566 = 678.30) | 678.30 counts | s 345B(c)(2) |
| A new immigrant from the United States (visa 10.3.2024) on 9.3.2029; on 10.3.2029; on 11.3.2029 | yes; declined (L2); no | s 350A(a) |
| A stable-disability pensioner: which subsections of s 335 fall away | (a), (b), (d), (e), (g), (h), (i) | s 351(d) |
| An old-age pensioner (or one over 70): which fall away | (b), (e), (g), (h), (i) | s 351(b) |

The `s 351` matrix is 21 situations against the nine subsections in `nii-il34-tests-s349-s351.l4`.

## 6. What check.sh prints

Run from 2026-10-09T00:23:49Z to 00:24:09Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset.
The binary was `jl4-0.1-6df1397b`, sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` before and after the run (`shasum -a 256 "$(readlink -f "$(which l4)")"`).
No module changed during the run.

```
module                                    errors satisfied  failed  refused  expected
nii-il04-nouns.l4                              0         0       0        0         0
nii-il04-published-figures.l4                  0         0       0        0         0
nii-il34-needs-a-source.l4                     0         0       0        0         0
nii-il34-nouns.l4                              0         0       0        0         0
nii-il34-tests-civic.l4                        0        57       0        0         0
nii-il34-tests-k1.l4                           0        35       0        0         0
nii-il34-tests-needs-a-source.l4               0         2       0        0         0
nii-il34-tests-s2-schedule-a.l4                0        27       0        0         0
nii-il34-tests-s28-s32.l4                      0        82       0        0         0
nii-il34-tests-s336-s340-s343.l4               0        44       0        0         0
nii-il34-tests-s341.l4                         0        54       0        0         0
nii-il34-tests-s342e.l4                        0       102       0        0         0
nii-il34-tests-s344-s347.l4                    0        58       0        0         0
nii-il34-tests-s349-s351.l4                    0       267       0        0         0
nii-s1-definitions.l4                          0         0       0        0         0
nii-s2-average-wage-and-schedule-a.l4          0         0       0        0         0
nii-s28-s32-accounts-and-treasury.l4           0         0       0        0         0
nii-s334-interpretation.l4                     0         0       0        0         0
nii-s336-s340-s343.l4                          0         0       0        0         0
nii-s341-order-5759-1999.l4                    0         0       0        0         0
nii-s342e-several-employers.l4                 0         0       0        0         0
nii-s344-s347-income.l4                        0         0       0        0         0
nii-s348e-civic-expiry.l4                      0         0       0        0         0
nii-s349-s351-exemptions.l4                    0         0       0        0         0
nii-schedule-k1-s369.l4                        0         0       0        0         0
tests-independent.l4                           5       150       5        1       5/1
TOTAL (26 modules)                             5       878       5        1
```

`check.sh` exit 0.
The row's own modules: 728 assertions satisfied, none failed, none refused (the 718 of 0.1.0 plus 10 added in 0.1.1).
`tests-independent.l4` (fid-il-34, frozen, not edited): 150 satisfied, 5 failed and 1 refused, all declared in `check.sh` (section 13).
An `#ASSERT REFUSED … BECAUSE "…"` that is satisfied is counted as satisfied (they are the refusals the policy requires, 74 of the 728 satisfied in the row's own modules).
`python3 -I tools/srcquote.py` and `tools/extquote.py` leave the 21 modules of this row byte-identical; `tools/extquote.py --check` and `tools/hebcheck.py` pass them (exit 0).

**The harness can fail.**
A scratch copy of each rules module with one number changed, run against its tests, failed as it should (counts of failed assertions): the Civic expiry day moved to 30 September (19 failed, with the refusals that no longer refuse); the reg 6(a) years 7 to 6 (2 failed, 2 refused); the K1 six months to five (2); the s 32(a) percentage for 2026 44.57 to 44.58 (2); s 351(b) with the age limb removed (5); the Order's 60% to 61% (2); s 344(a)(1)'s 90% to 80% (4); the 2025-26 household rate 7.85% to 7.84% (2); s 2(a)'s 0.5% to 0.6% (6).
The scratch copies were not kept.

## 7. Tests: where each expected value comes from

Every expected value was worked by hand from the Hebrew text before the run; the arithmetic is in a comment beside the group.
The real figures used are the Law's own (the 2026 basic amount under paragraph (3), 10,382, printed in s 1's note; the reduced collection threshold 7,703 carried by row IL-04; the Schedule J items of the 2025-2026 table at lines 4720 to 4729; the percentages of s 32(a); the average wage 13,566 of s 1's note) and, for the Schedule K maximum 51,910, the number row IL-05 carries. The item 3 minimum is 5% of the average wage, 678.30 (5% x 13,566); the 3,442 that appears in two tests of ss 345(e) and 350A(c) is an illustrative "minimum stated for him" (it is item 2 computed with the other 2026 average wage), not the item 3 minimum.
Round figures (10,000 and the like) are illustrative and said so.
The s 351 situations and the s 351(k) persons are generated by a script so that no field is left to a slip; the generating script is not kept (the fixtures are the record).

## 8. Needs a source

1. **Any amendment of the National-Civic Service Law after 2026-04-01** (the deposited consolidation's date; its last amendment is No. 9, Sefer HaChukim 5786 p. 470).
   Today is after 31.8.2026; an Amendment 10 would continue the line 30.6.2025, 15.11.2025, 31.3.2026, 31.8.2026 that IL-05 records.
   Where: the Knesset legislation database, lawitem 2001379, or Reshumot after April 2026.
   The answer to IL-05's 05-Q7 is therefore: **the deposited text says 31.8.2026 and nothing deposited says it moved; a question whose answer turns on a later day is declined**.
2. **The commencement day of the Civic Service Law** (the Law's own commencement section is not in the Wikisource page).
3. **The Institute's charge on yeshiva students who have not regularised their military status** (IL-05's open question 3); no Law, regulation or order found.
4. **The National Insurance (Classification of Insured Persons and Determination of Employers) Order 5732-1972 s 2** (a "recognised employer"), **the Income Tax (Deduction from Salary and Wages and Payment of Employers' Tax) Regulations 5753-1993 reg 5**, and **the National Insurance (Collection of Insurance Contributions) Regulations 5714-1954 reg 2(2)** (the payment dates reg 5 names): inputs of the regulations module.
5. **The Minister's orders and regulations** under ss 336 (other limits), 343 (the reduced sums), 344(b) to (d), 345(b)(3), (c)(2), (f), 345B(f), 346, 349, 350(b) (the orders on the German and Dutch laws, the Workers' Compensation Ordinance, the Prison Service law, the Maintenance Law), 351(k)(3): none deposited.
6. **The average wage series** for 1999 to 2025 (the Order's amount by the quarter's first month): the formula is encoded with the figure as an input.
7. **The 5760 amendment of the Order** (Kovetz HaTakanot 5760 p. 778) and **the Act of 2026 that added s 350A and Schedule K16** (the consolidation, an aid, is the only source of its text and of the temporary period 1.1.2026 to 31.12.2035).
8. **s 32(a) before 2018** and the Treasury's data (receipts, pensions paid, populations): printed only in an editors' note or inputs.
9. **The Income Tax Ordinance** sections these sections cite are rows IL-01 to IL-03 or unencoded; their results are inputs.

## 9. Inputs the capstone does not supply today (so IL-55 can follow)

| input | for | source of the figure |
| --- | --- | --- |
| whether a later Act moved the Civic Service Law's expiry; the reading of the expiry day; what ends s 348(e)'s temporary text | priority 1 | the Knesset database (section 8, item 1) |
| the average wage of the quarter's first month | the Order, 1999 to 2025 | the Institute |
| the full rate; the coordinated contributions; the sums the other employers deducted; whether the employer is a "recognised employer" | regs 2 to 6 | row IL-05 and the Institute |
| the highest monthly total income in the year; the Schedule K item 1 maximum | reg 4(a) | row IL-05 |
| the two index readings | reg 7(2), s 32(g)(2) | the CBS (row IL-33 holds the series) |
| the days of the breach, the cash and in-kind benefits, the s 2(b) average wage | Schedule K1 | the Institute |
| the measured wages, the compensation | s 2(a), (b) | the CBS |
| the Schedule J rates of the payer's column | s 28(a) | row IL-04 |
| the Treasury's receipts and (c1) payments; whether an order extended Amendment 252's period for 2027 or 2028 | s 32, ss 340(d), (e), 340A | the Treasury; Reshumot |
| the assessed income and its deductions; the advances; the benefit difference | s 345 | the Tax Authority; the Institute |
| the kibbutz figures; the basic amount under paragraph (3); the grossed-up member budget | ss 344(a)(1), 344A | the kibbutz; row IL-04's s 1 |
| the early pension, other income, the Schedule K maximum and minimum, the threshold | s 345B | rows IL-04, IL-05 |
| every fact of the s 351 situation, including whether the s 351(b) age was reached (Part D for a woman) | s 351 | the Institute; row IL-08 |
| the immigrant's country, visa day and the income he pays abroad on | s 350A | the Institute |

## 10. Open questions for a domain expert

1. Did a later Act move the Civic Service Law's 31.8.2026 expiry?
   (Section 8, item 1.)
2. Is the "compensation" added by s 2(a) a rate or an amount? (W1.)
3. Is the housing value of s 344(a)(1)(a) 7.5% of the basic amount a month a member, and are the other figures of (a)(1) monthly or yearly? (D1, A11.)
4. Does s 351(k)(2b) ("a period not exceeding twelve months") count in whole months?
5. What does s 345(c)(1) say about a net that the benefit difference turns negative? (A8.)
6. Does the Institute count the days of a Schedule K1 breach with or without the first? (A3.)
7. Is the consolidation's text of s 350A (a temporary provision, 1.1.2026 to 31.12.2035) the enacted text?

## 11. For the independent tester: the doubtful readings

Decide your answers from the Hebrew before you open the encoding.
The readings I am least sure of, beside the forks of section 2:

- the end of s 36(a)'s "until the day" (C2) and the strictness of "began before" (the same reading IL-05 takes in its fork F8);
- the 30-day edge and the clamping of `add months` in Schedule K1 (A3);
- the fifth anniversary in s 350A(a) (L2) and the inclusive month limits of s 351(k) (A6);
- whether s 351(d)'s first limb exempts from all branches ("no contributions are paid") or only from the branches named in its second limb, which I read as all (the first limb names none);
- whether the exceptions of s 350(a)(1) (the four kinds that ARE income) attach as I read them: maternity and pregnancy-preservation benefit (Chapter 3), injury allowance (Chapter 5), and benefits under Chapters 8 and 12;
- s 345B(c): the floor of (c)(2) applies only if the pension is BELOW the minimum and he has no other income on which contributions are paid.

## 12. Files

`BRIEF.md`, `NOTES.md`, `SOURCE-LICENSE.md`, `check.sh`, `encoding.json`, `VENDORED.sha256`, `tools/` (`srcquote.py`, `hebcheck.py`, `extquote.py`), and the modules named in section 0 and in `encoding.json`.
`INDEPENDENT-FINDINGS.md`, `tests-independent.l4` and `DECIDED-ANSWERS.md` are fid-il-34's, frozen; not edited here.

## 13. Version 0.1.1: the independent pass (fid-il-34, 370 cases)

The tester wrote `DECIDED-ANSWERS.md` from the Hebrew before opening the encoding (sha256 `1d4a5ef8878c…`); no misread figure or date was found.
Its three disagreements and what I did:

1. **C013, OURS-WRONG (minor).** `Order of 5759-1999 s 3 — the Order applies to contributions payable for the day` refused on 31.12.1998.
   Art 3 starts the Order on 1.1.1999, so the plain answer is no.
   Fixed: the rule is now `Day d AT LEAST 1.1.1999`, and `Order of 5759-1999 — the Order's amount applies to…` is FALSE before then.
   Added by hand-worked assertions: 31.12.1998 and 1.6.1990 are outside the Order; an employee and a self-employed person on 31.12.1998 are outside it.
   The AMOUNT of a pre-1999 month stays refused (the repealed Order No. 2 of 5747-1987 would be needed).
   The tester's line 129 now passes; its refusal count in `check.sh` falls from 2 to 1.
2. **3,442 labelled as the item 3 minimum.**
   By the text item 3 is 5 percent of the average wage: 5% x 13,566 = 678.30 a month; 3,442 is item 2 computed with the other 2026 average wage.
   The rules take the minimum as an input, so no rule changed.
   The s 345B(c) fixtures now use 678.30 (a pensioner of 500 with no other income is raised to 678.30; with other income of 10,000 he stays at 500; one of exactly 678.30 stays at 678.30), and the labels are corrected.
   The tests of ss 345(e) and 350A(c) keep 3,442 as an illustrative "minimum stated for him" and say so.
3. **C143 to C147, s 28(a).**
   The tester divides each branch rate by the PRINTED total 14.60; the list form divides by the sum of the cells given (14.49).
   The consolidation's own cells do not add to its printed total (the 2025-2026 employee column above the tier: 14.39, or 14.49 with the 2024-2027 work-injury 2.06, against 14.50 or 14.60).
   Section 28(a) says "by the ratio of the rates", which both readings serve, so under SHRUG this is a named switch: **fork R1**.
   `s 28(a) — the sum credited to the account of the branch… , the rates being… and the printed total…` takes the printed total and the reading; at the switch it is declined where the amounts differ and answered where they agree (printed total equal to the sum, or a branch with no rate).
   The plain list form is unchanged and is the "sum of the cells" reading; it is what the tester's five assertions call, so they still fail, as declared in `check.sh` with a comment.
   New tests (8): 14,490 by the cells and 14,600 by the printed total both give maternity 1,400; 14,600 by the cells gives 14,600 x 1.40 / 14.49; the default declines; equal totals answer (12,830 gives 940); a printed total of 0 is refused.

**C269** (a start on 1.9.2026 for October 2026): the tester decided "not reached unless an Act extended the Law"; fork C1 declines at the switch and answers FALSE at the named reading `the deposited expiry, the day itself in force` (its line 324 passes).
The tester's refusal is declared in `check.sh`.

**The two 2026 average wages (13,566 in s 1's note, 13,769 in s 2(a)'s note).**
No rule of this row chooses: Schedule A, Schedule K1, ss 340(d), (e), the Schedule K minima and the others take the average wage as an INPUT, so no switch is needed here.
By its words 13,769 is "השכר הממוצע המדוד" (the measured wage of s 2(a), the CBS input to s 1(1)), not "the average wage", and 13,566 is the note on the definition "the average wage" itself; the text therefore points at 13,566 for every rule that says "the average wage".
Whether 13,566 already includes s 2(b)'s changes is not stated; the two labels in row IL-04's published-figures module (13,566 "under section 1", 13,769 "as calculated under section 2") are IL-04's.

**Source anomalies the tester listed (not encoding errors).**

- S1. Schedule J, 2025-2026, employee column C above the tier: the cells add to 14.39 (14.49) against the printed 14.50 (14.60): fork R1 above.
- S2. Column D (employee deduction) above the tier: the cells add to 4.67 against the printed 7.00; the rates are inputs here and nothing is affected (IL-04's fork).
- S3. The consolidation keeps "60% of the average wage" in column D's heading in the 2025-2026 table, though the 2025 Budget-year Law s 19(6) replaces it by the reduced collection threshold from 1.1.2026.
- S4. s 342(e)(3), (4) and reg 1 say column E for the deduction rate, which is column D (IL-05 fork F22).
- S5. s 369(d) says "(ג)" where (a) is evidently meant; out of scope (this row stops at s 369(a)).
- S6. The two average wages above.

**Thin coverage, stated plainly.**
The tests are light on s 32(b) to (h) beyond (e) (they are repealed or by agreement), on (c1) and (c2) (one formula and an identity), on the kibbutz formula of s 344(a)(1) (two readings at two basic amounts, no case with other member counts), and on s 369 beyond (a), which is not encoded.

**Mutation checks of 0.1.1:** not repeated; the tests added are for rules whose changes are one line each.
