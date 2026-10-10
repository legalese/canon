# Estate Agents Act 2010 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation, version in force from 1 July 2025, as deposited at
`../../registers/source-bundle/EAA2010.txt`. The latest amendment annotated is
Act 15 of 2025, in force 1 July 2025.

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: anyone who sells, buys or rents a home
through an agent in Singapore meets it, and so may anyone who helps a friend find a
buyer for a fee. (An automated count found 3 of the 527 deposited Singapore Acts
citing it by its slug title. That count misses citations by short or older titles,
so it does not measure importance.) This row takes what estate agency work is and
who is outside the Act (ss 3, 4), the licensing and registration offences and the
bar on suing for commission (ss 28, 29, 44), who may be licensed or registered
(ss 3(2), 30, 32, 32A), disciplinary penalty caps (ss 49(6), 52(12), (13)) and
whether an appeal stays a revocation (s 59(3), (4)). Not encoded: the Council
(Part 2), applications and the register (ss 33-37), key executive officers and
agent-salesperson agreements (ss 38, 39, 41), codes and reporting (ss 42-43A), the
anti-money-laundering duties of Part 4A beyond their penalty caps, inspectors,
Disciplinary Committee and Appeals Board procedure, s 64 offences, the regulations,
and Ministerial exemptions under s 5.

## What the Act turns out to say

### 1. A one-off introduction for a fee is estate agency work

s 3(1) defines estate agency work as work done "in the course of business" **or**
"for or in expectation of any fee (whether or not in the course of business)". A
friend who introduces a buyer for a finder's fee is doing estate agency work, and
none of the s 4 exclusions covers them, so s 28 (up to $75,000, 3 years, and $7,500
a day for a continuing offence after conviction) applies unless they are licensed.
The same friend introducing for nothing is outside the definition. Asserted.

### 2. An agent with no prescribed agreement, or no licence when signing, cannot sue for commission

s 44(1): a claim lies "if, and only if" a prescribed-form estate agency agreement was
entered into and properly executed **and** the agent was licensed "at the time when
the estate agency agreement was so entered into and executed". A handshake deal, or a
licence obtained after signing, leaves nothing to sue on. Outgoings need, in
addition, an express reimbursement term (s 44(2)). Separately, ss 28(3) and 29(4)
make any fee for work done in an offence irrecoverable "by any person". Asserted.

### 3. Selling your own flat, an executor, and a solicitor who only introduces are outside the Act

s 4(1) disapplies the Act to vendors and purchasers acting for themselves (f),
executors and trustees (a), mortgage work (d), pure advertisers (e), employers housing
employees (h) and the Government (i). A solicitor is excluded only if he or she does
no other estate agency work (b): once the solicitor negotiates, the exclusion goes.
The encoding treats a tenant and a statutory board as excluded, through the
definitions of "purchaser" (which includes a prospective tenant) and s 4(1)(i), but
those cases were trimmed from the tests. Asserted for the rest.

### 4. A conviction disqualifies only "unless the Council otherwise determines"

s 3(2) lists convictions for dishonesty or fraud, civil fraud judgments,
money-laundering or terrorism-financing convictions (added by Act 15 of 2025,
"whether in Singapore or elsewhere"), convictions under this Act and bankruptcy as
making a person not fit and proper, but each is subject to the Council otherwise
determining. Conversely the Council may find a person with a clean record unfit.
Both directions asserted.

### 5. Licence and registration rules diverge

Both require age 21 (or a prescribed age, not read) and no link to a moneylender's
licence holder (ss 30(d), 32(2)(b)(iii)). A licence needs no employer; registration
as a salesperson needs employment by a licensed agent (s 32(2)(b)(i)). An existing
salesperson of another agent cannot hold a licence (s 30(c)), but s 32 does not bar
registration on that ground: the bar on serving two agents at once is in s 40, which
is not encoded (an inference about how the sections fit). Asserted.

### 6. Disciplinary caps are high, and multiply for money-laundering breaches

A Disciplinary Committee may fine a licensed agent up to $200,000 and a salesperson
up to $100,000 (s 52(12)); for Part 4A anti-money-laundering contraventions the same
figure applies "for each contravention" (s 52(13)). The Council's own penalty is
capped at $5,000, per contravention for those breaches (s 49(6)). An appeal does not
suspend a decision (s 59(3)), except that a revocation or suspension is stayed on due
notice of appeal unless the Appeals Board orders otherwise (s 59(4)). Asserted.

## What would need doing before this is worth anything

- The regulations under s 72, including the prescribed form of estate agency
  agreement and any class of work excluded from s 44 (s 44(4)), were not read.
- Prescribed ages, qualifications and CPE requirements were not read; 21 is used.
- No case law was searched, including on what amounts to "holding out" under s 28.
- Section 4(2) (developers' undivided-share property) and s 5 exemptions are not
  modelled.
