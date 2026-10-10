# Accounting and Corporate Regulatory Authority Act 2004 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 24
of 2025 (in force 6 May 2026) shown. The arrangement of sections at the top of the
deposit is out of step with the body for Part 7; this row follows the body's numbers
(36 symbol, 37 name, 38 false statements, 39 enforcement, 42 secrecy, 44
composition).

**Checks:** one case file, 112 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. Most of the Act sets up the
Authority: its constitution, finances, staff transfers and the electronic
transaction system. This row takes the parts an outsider meets:
- whether an individual's residential address is shown to the public (ss 30C, 30D,
  Sixth Schedule paras 2 to 4)
- who may use the title "Chartered Accountant of Singapore", and how registration is
  renewed, suspended and appealed (ss 35B to 35I)
- the Part 7 offences and their composition (ss 36, 37, 38, 39(6), 42, 44)

## What the Act turns out to say

### 1. A public accountant who is not a registered chartered accountant is both permitted and forbidden the title

s 35A(1) defines "accounting entity" to include "a public accountant". s 35B(1) lets
any accounting entity describe itself as "Chartered Accountant of Singapore". But
s 35B(3) says an individual "who is not registered as a chartered accountant ... must
not" use the expression. A public accountant is an individual. On the text alone, an
unregistered public accountant falls under both subsections, and nothing says which
one wins. Both are encoded as written. Asserted.

### 2. Residential addresses are hidden only for filings from 9 December 2024

s 30C(1) says a residential address "must be excluded from public disclosure". But
Sixth Schedule para 3(2) lets an address "filed or lodged ... before 9 December 2024"
be disclosed. Para 3(3) also leaves it public where the contact address is the same
as the residential address. So the protection covers only addresses filed from that
date on, and only for people who give a separate contact address. Asserted.

### 3. Ignore ACRA's letters and your home address goes public for three years

s 30D(1) lets the Registrar end the exclusion where communications to the contact
address "remain unanswered", or where service there is shown to be ineffective. Notice
and a chance to make representations must come first (s 30D(2) to (5)). Once the
exclusion has ended, s 30D(8) bars a new contact address "within 3 years" unless the
Registrar finds good cause. An appeal to the Court must be lodged within 30 days
(s 30D(7)). Asserted.

### 4. Hidden addresses still go to insolvency office-holders, AML-regulated firms and process servers

Sixth Schedule paras 3 and 4 allow a protected address to be given to an authorised
information service provider (which "must not disclose" it), to trustees in bankruptcy,
liquidators, judicial managers and receivers, and to financial institutions, licensed
moneylenders and licensed estate agents for anti-money-laundering purposes. It may also
go to a Singapore law practice, but only to serve process. Para 4A limits each
recipient to that purpose. A law practice wanting the address for any other reason is
not covered. Asserted.

### 5. Lying in an application costs five times more than misusing ACRA's name

The maximum for a false statement or intentional suppression in an application is
$50,000 or 2 years (s 38). Using ACRA's symbol or name without permission carries
$10,000 or 6 months, plus $250 a day while it continues (ss 36, 37). Obstructing an
officer carries $10,000 or 2 years (s 39(6)), and a secrecy breach $10,000 or 12 months
(s 42(4)). Composition is capped at the lower of half the maximum fine and $5,000
(s 44), so a false statement can be compounded for no more than a $10,000 offence can.
Asserted.

### 6. Chartered-accountant discipline is capped at 10 months, and the appeals are final

A designated entity may suspend a registration for up to 10 months instead of revoking
it (s 35F(4)). The Authority may extend a suspension to 10 months "in the aggregate"
(s 35G(4)). The only designated entity listed in the Third Schedule is the Institute of
Singapore Chartered Accountants. Its decisions are appealed to the Authority, whose
decision "is final" (s 35H). The Authority's own decisions under s 35G, and its refusal
to approve an entity under s 35C, go to the Minister, also final (ss 35I, 35C(5)). Every
appeal must be brought within 30 days, and does not stop the decision taking effect
unless directed (ss 35H(5), 35I(5)). A registration lasts one year. It cannot be renewed
while membership is suspended (s 35D(3) to (5)). Asserted.

### 7. "Two-thirds" has a two-member exception

For approval as a "Chartered Accountant of Singapore" entity, s 35C(2)(b) requires
two-thirds of the directors or partners to be chartered accountants. With only 2, one is
enough. For a company the requirement is what the constitution provides, and it applies
"(including the chairperson)". This row reads that phrase as requiring the chairperson to
be a chartered accountant. That is an **inference**: the phrase could instead mean only
that the chairperson counts as a director. Asserted on the inferred reading.

## What would need doing before this is worth anything

- Finding 1 needs the Accountants Act 2004 and any ACRA practice on how public
  accountants use the title. No such material was read.
- The "prescribed" accounting services, proportions and other requirements under ss 35C
  and 35D are in regulations that were not retrieved. So is the list of compoundable
  offences under s 44.
- The 3-year bar in s 30D(8) is modelled in whole months. Day counting was not attempted.
- Liability of officers and partners (s 40), enforcement powers beyond the s 39(6)
  offence, and the s 39(7) good-faith protection are not encoded.
