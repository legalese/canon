# Medical and Elderly Care Endowment Schemes Act 2000 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
5/12/2025), as deposited at `../../registers/source-bundle/MECESA2000.txt`. The
revised edition incorporates amendments to 1 December 2021; the latest amendment
annotated in the body is Act 19 of 2025 (deleting s 25(1)(c), wef 05/12/2025).

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0074**: Tier 2 of the remaining Singapore Acts, ordered
by everyday-life relevance. The requirement asks what the Act decides for a person
or business it applies to; no scenario has asked a sharper question yet.

Most of the Act sets up two Government funds (Medifund and the ElderCare Fund),
their investment, accounts and audit. This row takes what a patient and a
step-down care provider meet: Medifund eligibility, applying on a patient's
behalf and the committee's discretion (ss 15-17); protection of Medifund Account
moneys (s 12) and its accounting calendar (s 13); what step-down care is (s 2);
when an ElderCare subvention may be paid (ss 22, 24, 25(6)); revocation,
suspension and sanctions with their 7-day timetable (ss 25, 29); providers'
records (s 31); disclosure of medical information (s 43(2)); and the offences
(ss 31, 38, 40, 41, 45). Not encoded: fund constitution and investment
(ss 3-5, 18-21), the Advisory Council and the Schedule, approval of institutions
and grants to committees (ss 8-11), the amount and conditions of subventions
(ss 26-28, left to the Minister), monitoring powers (s 32), the general financial
provisions (ss 33-39) beyond the s 38 offence, service, regulations and
transitional provisions (ss 44, 46, 47). No regulations were retrieved, so the
prescribed means test in s 15(1)(d) is a single yes/no fact.

## What the Act turns out to say

### 1. Being eligible for Medifund gives no right to it

s 15 lists who may *apply*: a Singapore citizen, treated (or needing treatment) at
an approved institution, unable to pay, and meeting prescribed requirements. But
s 17(1) lets the committee approve only "if it thinks fit and subject to the
availability of moneys", and s 17(5) says nothing requires it to approve "every
patient who satisfies the requirements under section 15". A permanent resident is
not eligible at all. Payment goes to the institution, not the patient. Asserted.

### 2. Only the family or the medical social worker may apply for a patient, and only if the patient cannot

s 16 lets "any member of the patient's immediate family or the medical social
worker in charge of the patient's case" apply, and only where the patient is
unable to apply by reason of incapacity. A friend is not named; nor is anyone for a
capable patient. Asserted.

### 3. A Medifund Account is out of reach of the hospital's creditors

s 12(1): the moneys are deemed not to be the property of the committee or
institution on dissolution or liquidation, and are not available for its debts or
to any court enforcement process. On a committee's dissolution the balance, less
payments already authorised under s 17, goes back into the Medifund (s 12(2)).
Asserted.

### 4. A provider has 7 days to answer a revocation or sanction notice

ss 25(2)-(4) and 29(2)-(4) share one timetable: written submissions within 7 days
of receiving the notice (or longer if allowed); the decision notified within 7
days after that period; effect on the day after the last day for submissions if
nothing was submitted, otherwise 7 days after the decision notice. A suspension may
not exceed 6 months, and while it runs the provider is not an approved provider
and no subvention may be paid (s 25(6), s 22). Day arithmetic ("within 7 days
after day D" read as ending on D + 7) is an inference. Asserted.

### 5. Failing to file audited accounts is a crime but not a sanction trigger

s 29(1) sanctions (revoke, restrict, reduce, claw back) apply to breaches of
s 31(1) (records) and subvention conditions. s 31(2) (audited annual statements)
is not listed, although failing it carries a fine up to $2,000 under s 31(3), and a
conviction under s 31(3) is itself a revocation ground (s 25(1)(d)). Asserted.

### 6. Penalties are modest except for obstruction and false information

$2,000 for records failures (s 31(3)), $3,000 for a false record (s 31(5)), $1,000
for failing an auditor (s 38(2)), $2,000 for failing to answer an authorised officer
(s 40(2)); $5,000 or 12 months or both for obstruction (s 40(1)) or knowingly or
recklessly giving false information (s 41). Officers of an offending body are also
guilty unless they prove both absence of consent and due diligence (s 45). Asserted.

## What would need doing before this is worth anything

- The Medifund regulations (prescribed requirements, criteria for approval) and
  any Minister's directives under s 7(2) were not retrieved; eligibility in
  practice turns on them.
- How the Interpretation Act counts "within 7 days after" was not checked.
- The amount of a subvention (s 26) is entirely ministerial and is not modelled.
- No case law was searched.
