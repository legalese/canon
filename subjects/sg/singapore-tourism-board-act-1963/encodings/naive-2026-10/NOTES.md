# Singapore Tourism Board Act 1963 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, incorporating amendments
up to 1 December 2021, with later amendments annotated in the text; the latest seen
is Act 28 of 2022 (in force 1 April 2023). The deposit's metadata calls it the
"Current version as at 01 Oct 2026". The arrangement of sections at the top of the
deposit is out of step with the body for Part 3A; the encoding follows the body.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. Most of the Act sets up the
Board, its staff and the Tourism Fund, which carry little decision content. This row
takes the parts an outsider meets: the tourist guide licence and its offences
(ss 20-22, 25(4)), the Board's sanctions on a guide (s 28), the cruise terminal
licence and the 5% / 25% / 50% controller rules (ss 29A, 29R, 29W), the Merlion
(s 39), personal immunity (s 37), composition (s 41) and the appeal deadline
(s 42A(1)). Codes of practice, directions, licence conditions, the rest of Part 3AA,
enforcement powers and secrecy are not encoded.

## What the Act turns out to say

### 1. Only short-stay visitors count as tourists, so guiding residents needs no licence

The s 20(1) definition of "tourist" leaves out citizens, permanent residents, work
pass, dependant's, student's and special pass holders, and anyone on "a visit pass
valid for more than 90 days". The licence requirement in s 21 bites only on guiding
services given to a "tourist". So a guided tour for local residents alone falls
outside it. That last point is an inference from the definitions; the Act does not
say it in terms. Asserted (the definition).

### 2. Eight people in a coach puts the onus on the guide

s 22: someone who guides "8 or more tourists" is presumed to be paid, "unless the
contrary is proved", if they travel together in a motor vehicle that is not an omnibus.
Seven tourists, a scheduled omnibus, or no vehicle, and the presumption does not
arise. Payment counts "regardless of who makes" it (s 20(2)). Asserted.

### 3. The attraction's own staff are exempt; a suspended licence is no licence

s 21(2) exempts the owner or operator of a place of interest guiding at that place,
and anyone they employ or engage to guide there. s 20(3) deems a suspended licensee
not to hold a valid licence. The fine is up to $5,000, or $10,000 for a second
offence. Asserted.

### 4. Hiring an unlicensed guide is an offence too, on a "ought to know" standard

s 21(4) catches anyone who "directly or indirectly" uses an unlicensed guide whom
they know or ought reasonably to know is unlicensed, or with reckless disregard. The
fines are the same as for the guide. Asserted.

### 5. Crossing 5% means a notice; crossing 25% means the Controller's approval first

s 29R(1): becoming a 5% controller of a cruise terminal licensee requires written
notice to the Controller within 7 days. Becoming a 25% or 50% controller, or an
indirect controller, requires prior written approval. The test is equity or voting
power, alone or with associates (s 29W). The penalty is up to $100,000 or 3 years.
Unawareness is a defence only with notice within 14 days of finding out (s 29R(9)).
Otherwise, s 29R(11) says lack of intent or knowledge "is not a defence". Asserted.

### 6. Operating an unlicensed cruise terminal carries a $500,000 fine

s 29A, plus $5,000 a day for a continuing offence after conviction. Asserted.

### 7. Lesser sanctions are capped and cannot double up on offences

Instead of suspending or revoking, the Board may impose a financial penalty of up to
$1,000 (s 28(2)(f)). It may not do so for a contravention that is prescribed to be an
offence (s 28(3)). Any offence punishable with more than one month's imprisonment is
a ground to suspend or revoke (s 28(1)(e)). A suspension is capped at 6 months unless
a longer period is prescribed. Asserted.

### 8. Composition is the lower of half the maximum fine and $2,000

s 41(1); the Controller may compound Part 3AA offences for up to $5,000 (s 41(1A)).
Using the Merlion, or something confusingly like it, without the Board's permission
is an offence under s 39 (up to $2,000 or 6 months). Asserted.

## What would need doing before this is worth anything

- The meanings of "associate", "indirect controller" and "voting power"
  (ss 29W-29ZA) were not encoded; the controller rule takes percentages as given.
- The regulations prescribing compoundable offences, a longer suspension period and
  the licensing criteria were not retrieved.
- No s 43 exemption orders or Minister's orders under s 20(1)(e) were searched.
- No case law was searched.
