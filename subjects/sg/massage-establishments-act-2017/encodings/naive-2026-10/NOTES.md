# Massage Establishments Act 2017 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example naive rows (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.
Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MEA2017.txt`. The cover says it "incorporates all
amendments up to and including 1 December 2021"; the page furniture reads
"Informal Consolidation – version in force from 17/8/2026". Later amendments are
annotated in the text, the latest being G.N. No. S 557/2026 (amending the
Schedule's Penal Code part, commencement 17 August 2026), the last entry in the
deposited legislative history. SSO's metadata calls it the "Current version as at
01 Oct 2026".

**Checks:** one module, one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** to ordinary people in Singapore: it
governs every business that provides massage in an establishment, the people
employed there, and the owners and occupiers who let premises to them. This row
takes what an operator, a worker, a landlord or a member of the public meets: the
three licensing offences and the repeat-offender rule (ss 2, 5), whom a licensee may
employ and the penalty (s 13), renewal (ss 8(3), 16(2)(b)), suspension and
revocation with the Schedule of specified offences (ss 11, 12(1)), the time for
representations (ss 10, 12, 17), terminating a worker after cancellation (s 17(6)),
appeals and their deadlines (ss 7(9), 10(7), 12(7), 15(6), 17(8), 22, 31), the
premises closure order (ss 19, 21), and the landlord after a conviction (ss 28(6),
29(1)).

Not encoded: application procedure and the matters weighed on grant (ss 6, 7(1)-(7),
14, 15(1)-(3)); licence conditions (s 9); entry, inspection and investigation
(ss 23-26); false statements, obstruction and breach of condition (s 27); passing
an owner's notice up the chain of tenancies (s 28(1)-(5)); the lock offence (s 20);
the liquor deeming provision (s 34); rules and transitional provisions (ss 35, 36).
No rules made under s 35 were retrieved, so no fee, qualification or prescribed
criterion is known.

## What the Act turns out to say

### 1. A licence cannot be renewed, but a worker's approval can

s 8(3): "A licence is not renewable." It runs for the period it specifies unless
revoked (s 8(2)). An approval to employ an individual, by contrast, "may be renewed
upon its expiry" (s 16(2)(b)). The text does not say what an operator does when a
licence expires; a fresh application under s 6 is an inference. Asserted.

### 2. Suspension is immediate, needs no notice, and has no appeal

s 11 lets the Licensing Officer "immediately suspend" a licence while proceedings for
a Schedule offence are pending against the licensee, a responsible officer, or anyone
with substantial interest in or control of the business. Revocation, cancellation and
modification each require a notice and at least 14 days for representations (ss 10(3),
12(3), 17(3)), unless the public interest or a contravention justifies less. s 31
lists the appeals to the Minister: ss 7(9), 10(7), 12(7), 15(6), 17(8) and 22(1).
None is against a suspension. A charge against an ordinary employee does not engage
s 11. Asserted.

### 3. The landlord is a repeat offender never; the operator and advertiser are

s 5(4) doubles the fine (to $20,000) and raises imprisonment from 2 to 5 years for a
"repeat offender". s 5(5) defines that only for contraventions of s 5(1) (carrying
on unlicensed) and s 5(2) (advertising), each counting only earlier convictions for
the same subsection or its repealed-Act counterpart (s 9(a) or s 9(e)). An owner or
occupier convicted again under s 5(3) stays on the first-offender maximum. An earlier
advertising conviction does not make an unlicensed operator a repeat offender.
Asserted.

### 4. Running an unlicensed parlour is not itself a "specified offence"

The Schedule lists sexual, trafficking, prostitution, immigration, foreign-manpower,
employment-agency, criminal-benefits, organised-crime and unlawful-society offences under ten Acts, but not the Act's own s 5
offence, and not theft. So a s 5 conviction does not ground suspension or revocation
under ss 11 or 12(1)(c); revocation would need another ground, such as s 12(1)(f)
(contravention of any requirement of the Act). The PDF's tables are column-shifted,
and section numbers were matched to descriptions by order. Asserted.

### 5. A landlord who does not evict is presumed to have known

After a conviction under s 5(1) or (3), the owner or occupier from whom the offender
rents "must, within one month after the date of conviction, require the offender to
deliver up possession" (s 29(1)); an advertising conviction does not trigger it. If a
s 28(1) notice was served on that landlord and they fail to comply, they are presumed
to have known of the unlicensed business when prosecuted under s 5(3), "until the
contrary is proved" (s 28(6)). Asserted.

### 6. A worker must be approved, at least 18, and possibly screened

s 13(1), (2): no employment without the Licensing Officer's approval, nor of anyone
below 18, anyone the licensee "knows or has reason to believe is likely to engage in"
sexual services, or anyone who has not passed a medical screening "if required". A
first conviction is a fine of up to $5,000 with no imprisonment; a second or later,
$10,000 or 2 years or both (s 13(3)). After an approval is cancelled the licensee has
7 days to terminate the employment (s 17(6)). Asserted.

### 7. A closure order needs only a charge

s 19(1): the Commissioner may close premises of a person charged with carrying on
unlicensed (or with the repealed s 9(a) offence) whom the Commissioner reasonably suspects is
continuing to provide massage while proceedings are pending. A conviction is not
needed; a charge for advertising is not enough. The key must reach the Licensing
Officer within 24 hours of securing the premises (s 19(2)(b)). Entering without the
Commissioner's permission, or without meeting its conditions, carries up to $15,000 or
3 years (s 21). The order takes effect despite an appeal (s 22(2)). Asserted.

### 8. Appeal deadlines have two routes for some decisions, one for others

Refusal of a licence, revocation, and refusal or cancellation of an employment
approval: 14 days after notification, or, if grounds are requested within that time,
14 days after receiving them. A direction under s 10(6) and a closure order: 14 days
from the date of the direction or order, with no grounds route. Reading "within 14
days" as including day 14 is an inference. Asserted.

## What would need doing before this is worth anything

- The Massage Establishments Rules (or whatever rules are now made under s 35) were not
  retrieved: fees, qualifications, prescribed fitness criteria, and any operating
  conditions are unknown.
- The Licensing Officer's published fit-and-proper criteria (s 7(4)) were not read.
- The Schedule's column-shifted tables should be checked against the PDF.
- "Within one month" (s 29(1)) is not computed; neither is the s 29(5) date of
  conviction.
- No case law was searched.
