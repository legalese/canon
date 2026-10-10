# Point-to-Point Passenger Transport Industry Act 2019 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, "version in force from
4/5/2026", deposited at `../../registers/source-bundle/PPPTIA2019.txt`. The cover says
the revised edition incorporates amendments up to 1 December 2021; the latest amendment
annotated in the text is Act 5 of 2026 (wef 4 May 2026, the definition of "motor
vehicle"). Act 30 of 2024 (Platform Workers Act 2024, wef 1 January 2025) is annotated
in s 4.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It was chosen for **everyday-life relevance**: it is the Act behind the taxis and
ride-hail apps people in Singapore use, and the drivers who work through them. This row
takes what a passenger, a driver or a small would-be operator meets: what counts as a
street-hail or ride-hail service (ss 3, 4), the offences of providing one without
authority and of a driver taking bookings from an unauthorised provider (ss 9-11), false
applications (s 12(5)), the suspension limit and financial-penalty cap (s 35), notice
before regulatory action (s 36), roadside questioning and the offence of not complying
(ss 39, 41), composition (s 42) and appeals (ss 43, 44).

Not encoded: licence application and grant criteria (ss 12-13, 18-19, beyond s 12(5)),
licence conditions and their modification (ss 15-17, 21-23), the content of exempt
ride-hail operator orders (ss 24-26), accounts and records (ss 28, 29), codes of
practice, directions and emergency directives except as appealable decisions
(ss 30-34), powers of entry (s 38), corporate liability (ss 48, 49), service, Regulations,
and the savings in s 68 and the Schedule. No Regulations or Gazette orders were
retrieved.

## What the Act turns out to say

### 1. A driver can be prosecuted for taking a booking, and a passenger can be questioned

s 11 makes it an offence for a **driver** to intentionally take bookings from a ride-hail
provider that is neither licensed, an exempt operator, nor exempted under s 52, if the
driver knows or is reckless about that. Up to $1,000 or 3 months; $2,000 or 6 months on
a second or subsequent conviction. Unlike the provider's offence, it needs knowledge or
recklessness. And s 39(1)(f) lets an authorised officer require "the driver or any
passenger of the vehicle" to answer questions and provide documents; failing to comply
without reasonable excuse is an offence under s 41(1) (fine up to $10,000). Asserted.

### 2. The provider's offence is strict liability, with a daily fine after conviction

Providing a street-hail or ride-hail service without authority is "a strict liability
offence" (ss 9(2), 10(2)): up to $10,000 or 6 months, plus up to $500 for every day or
part of a day the offence continues after conviction. A suspended licence does not
authorise anything (ss 9(4), 10(4)). An exempt ride-hail operator is covered only while
it acts in accordance with the order's conditions (s 24(3)). Asserted.

### 3. One taxi is not a street-hail service; a lone driver is not a ride-hail provider

s 3 defines a street-hail service by taxis "2 or more of which at any time in a year are
taxis owned by the provider". s 4(4): a person is not providing an on-demand passenger
transport service "solely because the person drives" the vehicle. Only taxis, private
hire cars hired as a whole with a driver, and prescribed s 101 classes are "bookable
vehicles", so an ordinary private car is outside the ride-hail definitions (whether
other law catches it is not something this Act says). Asserted.

### 4. The financial penalty cap scales with turnover and with each breach

s 35(6): the maximum is the **highest** of $100,000, 10% of annual turnover from the
service, $100,000 per contravention (breach of conditions, codes or directions), or 10%
of turnover per act or omission causing inadequate service. So four service failures by
an operator with $5m turnover could attract up to $2m. Suspension is capped at 3 months
(s 35(2)(e)), and the LTA must allow at least 14 days for representations first
(s 36(1)(c)). Asserted.

### 5. Appeals go to the Minister, are short, final and do not suspend the decision

s 44(2): 28 days for a modification of licence conditions, 14 days for every other
appealable decision; the Minister's decision "is final" (s 44(5)) and the decision must
be complied with meanwhile unless the Minister directs otherwise (s 44(7)). The list in
s 43 does not include the 24-hour stop-service direction under s 31(3), nor anything
about exempt ride-hail operator orders, so an exempt operator whose order is revoked
under s 26 has no appeal under this Act. What it gets instead is a published notice
inviting representations by a date at least 14 days away, "unless [the LTA] considers it
impractical or undesirable" (s 26(2)). Refusal to renew is treated as appealable because
s 2 says "grant" includes grant on renewal; that is a reading of the definition. Asserted.

### 6. Compounding is capped at the lower of half the maximum fine and $5,000

s 42(1). Which offences are compoundable is prescribed in Regulations not retrieved; the
encoding takes that as an input. Asserted.

## What would need doing before this is worth anything

- The Regulations (fees, prescribed periods, compoundable offences, prescribed vehicle
  classes) and the exempt ride-hail operator orders were not retrieved.
- The ride-hail false-application offence in s 18 was not read in full.
- Only limb (a) of "on-demand ride booking service" is modelled; vehicle pooling and
  prescribed services are not.
- No case law or LTA guidance was searched.
