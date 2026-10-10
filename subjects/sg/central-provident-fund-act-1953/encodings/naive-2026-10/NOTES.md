# Central Provident Fund Act 1953, section 15 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 July 2026.

**Checks:** `l4 run cpf-cases.l4`, `l4 run cpf-medisave-cases.l4`, `l4 run cpf-rates-and-death-cases.l4` and
`l4 run cpf-allocation-and-exemption-cases.l4` -- 136 assertions satisfied, 0 errors. Of these, 60 predate
11 October 2026. On that day 41 were added for REQ-0001 and REQ-0012, and 35 for REQ-0002 and REQ-0003.

## Scope — read this first

The CPF Act is about **911,000 characters**. This encodes **s 7, s 15(1)–(6),
s 16 and s 25(1)**, plus the s 2 definition of "applicable person". That is a
few pages out of a very large statute.

*(The section below describes the first pass only. See "Added with sections 7,
16 and 25" at the foot of this file, which corrects it.)*

Not encoded: contributions (ss 7–9D), the subsidiary accounts (s 13), housing
and investment charges, nominations (s 25), the Retirement Sum Scheme machinery
in s 15AA, the Board's discretionary power in s 15(4), section 16 (which s 15(2)
and (3) are both expressed to be subject to), and everything from Part 3A
onwards.

The prescribed retirement sum, the prescribed classes of applicable person, and
the Board's conditions are all **facts supplied**. The regulations were not
retrieved, and they carry most of the practical content.

## Three observations

**1. There are now only two routes out of the Fund, and one of them is leaving
the country.** s 15(2) once had seven paragraphs. (c) to (g) were repealed
between 2021 and 2024, and what remains is:

- **(a)** the member has attained 55; or
- **(b)** the member **is not an applicable person** — that is, is neither a
  citizen nor a permanent resident of Singapore (nor of a prescribed class).

So the Act's own structure now reads: wait until 55, or cease to be a citizen or
permanent resident. Asserted on the foreigner aged 40, who may withdraw at any
age.

**2. The retirement-sum set-aside binds the member who stays and not the one
who goes.** s 15(6) attaches the set-aside to entitlements under (2)(a), (3) and
(4). It does **not** attach to (2)(b). Two members with identical accounts
therefore come out very differently:

| | credit | retirement sum | may withdraw |
|---|---|---|---|
| citizen, aged 60, s 15(2)(a) | $200,000 | $100,000 | **$100,000** |
| non-citizen, aged 40, s 15(2)(b) | $200,000 | $100,000 | **$200,000** |

Asserted as a pair. There is an obvious policy reading — the retirement sum
exists to fund a retirement in Singapore, and someone who has ceased to be a
citizen or permanent resident is not having one — so this is recorded as a
consequence of the drafting rather than as a defect. It is worth stating because
it is invisible unless (2), (3) and (6) are read together.

**3. s 15(3) attaches to one ground and not the other.** The annual further
withdrawal is for "a member of the Fund who has withdrawn any money from the
Fund **on the ground that he or she has attained 55 years of age**". A member who
withdrew under (2)(b) is outside it — which makes sense, because they were
entitled to the whole sum and have nothing left to come back for, but the
drafting achieves it by naming the ground rather than by saying so.

## An honest limit

`the amount this member may withdraw` is the function a person would actually
want to call, and it is the one least safe to rely on. It reads s 15(1), (2),
(3) and (6), and it **does not** read s 16 (to which (2) and (3) are both
subject), s 15(4) (the Board's discretion to allow more), s 15AA, or any of the
charges that can be registered against an account. A real answer needs all of
those. The function is correct for the subsections it covers and silent about
the rest, which is not the same as being right.

## What would need doing before this is worth anything

- The regulations fixing the retirement sum.
- s 15AA, s 15(4), and the charge provisions.
- No case law was searched.


---

# Added with sections 7, 16 and 25

## s 16 corrects the first pass, and the first pass was too generous

The earlier note said that `the amount this member may withdraw` was "the
function someone would want to call and the one least safe to rely on", because
it did not read s 16. It now does, and the difference is large.

**s 16 ring-fences the medisave account.** A member may not withdraw it under
s 15(2)(a) (reaching 55) or s 15(3) (the annual further withdrawal); the Board
must not allow it under s 15(4); and under s 15AA(1) only with the Minister's
approval.

So for a 55-year-old citizen with **$200,000** in the Fund, of which **$60,000**
is medisave, and a **$100,000** retirement sum:

| | |
|---|---|
| first pass, s 15 alone | $200,000 − $100,000 = **$100,000** |
| with s 16 | ($200,000 − $60,000) − $100,000 = **$40,000** |

Both rules are kept, and both are asserted, so the difference is visible rather
than silently corrected. The older one states what s 15 says on its own; the
newer one states what s 15 and s 16 say together.

A member whose medisave balance is large enough can reach **nothing at all**: on
$200,000 with $150,000 in medisave, the non-medisave credit is $50,000, which
will not cover the $100,000 retirement sum, so the withdrawable amount is zero
despite $200,000 in the Fund. Asserted.

## The asymmetry, sharpened

The earlier note recorded that the retirement-sum set-aside binds the member who
stays and not the one who goes. s 16 widens that gap, because **s 16(1) names
s 15(2)(a) and s 15(3) and does not name s 15(2)(b)**:

| | retirement sum set aside? | medisave reachable? | takes |
|---|---|---|---|
| citizen, 60 | yes | no | **$40,000** |
| non-citizen, 40 | no | **yes** | **$200,000** |

The member who remains a citizen or permanent resident loses both. The member
who ceases to be one loses neither. There is a coherent policy reading — the
retirement sum funds a retirement here and medisave pays for healthcare here —
but the difference is now a factor of five on identical balances, and it is
assembled from three provisions that never mention each other.

## Two more

**s 7(3) is narrower than a general failure-to-pay offence, and far heavier.**
It bites only where the employer **has already recovered** the employee's share
from their wages and then fails to pay it over. An employer who never deducted
anything and never paid anything is outside this subsection. The maximum is a
fine not exceeding $10,000 **or imprisonment for a term not exceeding seven
years** — the heaviest custodial maximum encountered anywhere in these seven
Acts, and it is for keeping money already taken from a worker's pay.

**A member who is not an applicable person may empty the Fund but may not say
who gets it.** s 25(1) allows a nomination only by "a member of the Fund (**being
an applicable person**) who is at least 16 years of age". So the same person who
may withdraw everything under s 15(2)(b) may not make a nomination at all.
Asserted as that pair.

Also encoded: s 25(1)(a)(ii)(B) splits a large nomination to a citizen or
permanent resident — the Minister's maximum is transferred into the nominee's
own CPF accounts and the excess is paid out to them in cash.

## Contribution rates and death (added 11 October 2026 for REQ-0001 and REQ-0012)

A third module, `cpf-rates-and-death.l4`, answers two requirements raised by the
`cradle-to-grave-simone` scenario.

### REQ-0001: the shares for an employee aged 23 on $4,200 in August 2026

First Schedule paragraph 1, in force from 1 January 2026. For wages over $750 the employer
pays a total of **37%** of ordinary wages, up to the Ordinary Wage Ceiling, and may recover
**20%** from the employee. The ceiling is $8,000 a month from 2026 (para 7(ea)). So $4,200
gives **$1,554** in total: **$840** deducted from the employee and **$714** borne by the
employer, exactly as the entry expected. Asserted.

The other bands are 34/18 (above 55 to 60), 25/12.5 (above 60 to 65), 16.5/7.5 (above 65 to
70) and 12.5/5 (above 70). Wages of $500 to $750 phase in the employee share. The total is
rounded to the nearest dollar with 50 cents rounding up, and the employee share drops any
fraction (para 7(b), (c)). An older band starts the month **after** the birthday month
(para 7(a)). The tables are column-shifted in the `.txt` deposit; the rates were read cell
by cell.

Not encoded: additional wages, the graduated rates for new permanent residents, foreign
and public-sector employees, and the allocation into the three accounts (REQ-0002, which
needs subsidiary legislation).

### REQ-0012: CPF moneys on death are outside the estate by statute

The entry asked this as a case-law question. The Act answers it. s 24(3A): moneys paid out
on a member's death "are deemed to be impressed with a trust in favour of" the nominee
(or, with no nomination, those entitled through the Public Trustee under s 25A), and "are
deemed not to form part of the deceased member's estate or to be subject to his or her
debts". A will leaving everything to the spouse does not reach them.

One trap is s 25(5)(a): a nomination is **revoked by the member's marriage**. A nomination
made before marrying does not survive the wedding, and the moneys then go through the
Public Trustee route. Asserted.

## Allocation and the Exemption Order (added 11 October 2026 for REQ-0002 and REQ-0003)

### Allocation into the accounts is a ministerial direction, published by the Board

Section 13(4) requires the Board to credit each contribution to the member's accounts "in such manner as the
Minister may direct". The direction is not subsidiary legislation. The ratios in `cpf-allocation.l4` therefore
come from the CPF Board's one-page **"CPF Allocation Rates from 1 January 2026"**, supplied by hand. Because
it is not legislation, it is not deposited.

The Board's method:
- Medisave is computed first, then the special account (the retirement account above 55).
- The ordinary account gets the remainder.

The examples are in cents, but the page does not say how a fraction of a cent is rounded. The encoding rounds
each of the first two credits to the nearest cent; that is the encoder's reading. Both of the page's examples
are asserted.

**REQ-0002:** $1,554 at age 23 gives medisave **$335.97**, special **$251.90** and ordinary **$966.13**.
The ledger expected 336 / 252 / 966, which is the same split rounded to whole dollars.

Not modelled: the footnote on members aged 55 and above after the special account closes. Their contributions
go to the retirement account only up to the Full Retirement Sum, and to the ordinary account after that.

### The Exemption Order: an approved internship is exempt, but this is the 2018 text

`cpf-exemption.l4` encodes the **Central Provident Fund (Exemption) Order 2018** (S 61/2018), made under s 69.
The text is deposited at `../../registers/source-bundle/CPFA1953-S61-2018.txt`. **The PDF supplied is the
version as made, in force from 1 January to 1 February 2018; later amendments have not been checked.**

What it exempts:
- Para 3: no contributions for an employee who is neither a citizen nor a PR.
- Para 2 and the Schedule: no contributions for specified employees. These include:
  - domestic workers on 14 hours a week or less;
  - UN staff;
  - certain seamen;
  - SHATEC trainees;
  - students (paras 5 to 8).

The students covered:
- Para 5: a student of a university "whose function of providing university education is determined by
  any written law", of ITE, of a polytechnic, or of certain schools, "employed for training approved by the
  institution concerned".
- Para 6: private-institution students on MOE-subsidised full-time programmes.
- Para 7: overseas students required to train here for 6 months or less, who give the employer written
  confirmation.
- Para 8: school pupils on holiday jobs, but not once they have done A levels.

**REQ-0003:** an NUS student whose internship is part of the course is exempt under para 5(a). No
contributions are payable on the $1,200. The test is whether the *institution approved the training*,
not whether she is full-time. An internship the university has not approved is not exempt. Both are asserted.

## Still a small fraction of the Act

911,000 characters, of which this encodes s 7, s 15(1)–(6), s 16 and s 25(1).
Since 11 October 2026 the First Schedule rates and s 13(4) allocation are encoded (see above). Not encoded: s 15AA, s 15(4), the housing and investment charges, the rest
of s 25, and everything from Part 3A onwards.

**A caution carried over from the Work Injury Compensation Act.** The First
Schedule contribution rates are a long table that crosses page breaks, and in
that Act every such table in the deposited text was shifted by one row against
its key. The CPF rates were *not* encoded partly for that reason: they should be
recovered from the PDF and checked before anyone relies on them.
