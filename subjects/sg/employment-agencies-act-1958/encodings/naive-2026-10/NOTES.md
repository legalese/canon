# Employment Agencies Act 1958 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/EAA1958.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021". The only amending Act annotated in
the body is 5/2015, at s 36. From s 33 on, the arrangement of sections at the top of
the deposit is one number out of step with the body. This row follows the body.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row covers the rules an
agency, its staff, an employer who uses an agency, and the Commissioner actually meet:

- who needs a licence (ss 2, 4(1), 6)
- when a suspension or revocation takes effect and what it stops (ss 10(4), (5), 11(1), (2))
- registering and deregistering personnel (s 12)
- appeals (s 14)
- benefits offered to employers (s 16)
- engaging an unlicensed person (s 30)
- disqualification (s 32)
- the maximum penalties for the main offences, and the cap on composition (s 41)

Not encoded:

- exemption orders beyond a flag (s 4(2)-(4))
- licence applications and security (ss 7, 8)
- late renewal (s 9(3), (4))
- inspectors' investigation and arrest powers (ss 17-27)
- vicarious and corporate liability (ss 28, 39)
- abetment (s 40)
- registers (s 44)
- rules (s 45)

## What the Act turns out to say

### 1. An employer who uses an unlicensed recruiter is fined per worker, and not knowing is no defence unless they checked

s 30(1) fines anyone who engages or uses an unlicensed person in connection with
employment up to "$5,000 for each employee engaged through that person". Under
s 30(2), ignorance is a defence only if the defendant "further proves" due diligence.
Under s 30(3), due diligence means having verified the licence "in such manner as may
be prescribed". The prescribed manner is in rules that were not retrieved. Asserted.

### 2. A suspension or revocation does not bite for 14 days, and an appeal stops it altogether

Under s 10(4), the order takes effect only after 14 days from service. Under s 10(5),
if the licensee appeals to the Minister within that time, the order "does not take
effect unless the order is confirmed by the Minister or the appeal is withdrawn".
Once a suspension is in effect, the agency may keep serving existing clients but must
not enter into new recruitment or placement agreements (s 11(1)). Once a revocation is
in effect, it must cease at once (s 11(2)). Reading "until the expiration of 14 days"
as "after day 14" is an inference about how the days are counted. Asserted.

### 3. Disqualification is wider for key appointment holders than for other staff

Under s 32(1), four things bar a person from acting as a key appointment holder
(director, CEO, partner, sole proprietor and so on) without the Commissioner's written
consent: being an undischarged bankrupt, a dishonesty conviction, a human-trafficking
conviction, or having managed an agency whose licence was revoked. Under s 32(2), only
the last two bar ordinary personnel. A bankrupt or someone with a dishonesty
conviction can therefore work as agency staff but cannot run the agency. Asserted.

### 4. Some of the Commissioner's decisions cannot be appealed

s 14(1) lists five appealable decisions: refusing to grant or renew a licence,
debarment, suspension or revocation, refusing to register personnel, and
deregistering personnel on the Commissioner's own motion. The appeal must be made
within 14 days of receiving notice, and the Minister's decision "is final". These are
not on the list: varying or adding licence conditions (s 7(4)), forfeiting security
(s 8(2)), refusing a deregistration application that lacks the worker's consent
(s 12(9)(b)), and directions after suspension or revocation (s 11(4)). Asserted.

### 5. Offences by staff under s 33 make the licensee guilty too, and some repeat penalties add only prison

For overcharging (s 33(1)), the fine stays at $5,000 on a second or subsequent offence.
What changes is that up to 6 months' imprisonment becomes available. For s 33(3)
(inducing an employer not to engage someone who did not come through the agency), the
fine rises from $2,000 to $5,000. Under s 13(3), failing to issue a registration card
carries $1,000, or $2,000 with up to 6 months on repeat. The unlicensed-agency offence
(s 6(4)) and its kin (ss 9(2), 11(5), 31) carry $80,000 or 2 years, doubling to
$160,000 or 4 years on repeat. Under s 33(1)-(3), "the licensee and the employment
agency personnel shall each be guilty". The encoding asserts the penalty figures, not
the dual liability.

### 6. The licence exemptions are narrow and specific

s 6(3) lifts the s 6(2) ban for three groups: licensees; registered personnel acting
as such; and a person recruiting "for the sole purpose of recruiting persons for
employment on that person's own behalf". An unregistered staff member or the local
representative of an overseas agency contravenes s 6(2). Under s 4(1), the Act does
not apply at all to an agency "wholly maintained or wholly managed by any department
of the Government". Asserted.

### 7. Composition is capped at the lower of half the maximum fine and $5,000

s 41(1). For a $1,000 offence the cap is $500. For an $80,000 offence it is $5,000.
Asserted.

### 8. Deregistration with the worker's consent is mandatory

Under s 12(9)(a), the Commissioner "must grant" a deregistration application that
comes with the worker's written consent. Without that consent, the Commissioner has a
discretion. Under s 12(12), a licensee remains liable for a departed worker who is
still registered to it, unless it has applied to deregister that worker. Asserted.

## What would need doing before this is worth anything

- The Employment Agencies Rules (prescribed fees, the prescribed manner of verifying a
  licence, the prescribed periods for late renewal and deregistration) were not
  retrieved. s 15 (only prescribed fees may be charged) and s 33(1) (overcharging)
  depend on them.
- The arrangement-versus-body numbering mismatch should be checked against the SSO
  current version. This row uses the body.
- Exemption orders under s 4(2) were not looked for.
- No case law was searched.
