# Civil Aviation Authority of Singapore Act 2009 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill conventions and nothing else. No pipeline, no coverage table, no independent
test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 16
of 2025 (in force 1 October 2026) shown. The deposit's metadata calls it the
"Current version as at 01 Oct 2026". Section numbers follow the body: in Part 9 the
arrangement of sections is out of step with it (the body has the airport
development levy at s 87A, the SAF levy at s 87B, statutory liens at s 89 and the
lien offence at s 94).

**Checks:** one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**7 of the 527 Singapore Acts** deposited here cite it. Most of the Act is about
the Authority itself, the 2009 corporatisation of Changi, and economic regulation
of the airport licensee. This row takes the rules with decision content: who may
operate an airport, transfer of the licence, non-airport business, becoming a 5%
controller of a licensee, the Authority's immunities and secrecy duty, the
enforcement offences and composition, when the airport development levy attaches,
and statutory liens on aircraft (ss 13, 14, 36, 41, 42, 56B, 57, 77 to 79, 82, 85,
87A, 89, 92 to 95, 99). Licence conditions and revocation, codes of practice,
master plans, charges, designated operating entities, by-laws, slot coordination,
special administration and the levy rates (set by Gazette order) are not encoded.

## What the Act turns out to say

### 1. "Ought reasonably to have known" reaches removal of a liened aircraft, not stripping it

s 94 forbids a person who knows a statutory lien is in effect from removing the
aircraft from Singapore (subs (1)) or detaching any part or equipment (subs (2)).
But the deeming rule in subs (5), that a person is taken to have known if they
"ought reasonably to have known", is stated to apply only "for the purposes of
establishing a contravention of subsection (1)". So constructive knowledge
convicts the person who flies the aircraft out, but not the one who strips it.
The maximum is $200,000 or 12 months. Asserted.

### 2. The two notification defences in s 57 are built differently

A person who becomes a 5% controller of an airport licensee without approval has a
defence under s 57(7) if they were unaware **or** they notified within 14 days of
becoming aware and took the action the Authority directed. The licensee's own
failure to notify under s 57(5) has a defence under s 57(9) only if it was unaware
**and** notified within 5 days. Beyond these defences, lack of intent is no defence
(s 57(10)). A third defence, s 57(8), covers a breach caused by an associate's
increase with no arrangement between them. Asserted.

### 3. "5% controller" has no ceiling for a licensee but stops at 25% for a designated entity

For an airport licensee, a 5% controller is anyone holding 5% or more of the equity
or voting power (s 56B(2)), and the Minister may raise that figure by Gazette order
(s 56B(3)). For a designated entity the definition is a band, "5% or more, but less
than 25%" (s 56B(1)). Approval needs all three of fit and proper, continued prudent
conduct, and the public interest (s 57(2)). The maximum fine is $500,000 and 3 years
for an individual, $1 million otherwise, with daily fines of $50,000 or $100,000
(s 57(6)). Asserted.

### 4. Operating an airport without a licence carries a $1 million fine and no prison term

s 36(6): a fine up to $1 million plus $25,000 for every day or part of a day the
offence continues after conviction. The section provides no imprisonment. A licence
transfer without the Authority's prior written consent "is void and of no effect"
(s 41(2)). Asserted.

### 5. Composition is capped at $5,000 whatever the offence

s 85: a prescribed offence may be compounded for the lower of half the maximum fine
or $5,000. For the $200,000 lien offence that is still $5,000, if it is prescribed
as compoundable (the prescription is in regulations not retrieved). No offence may
be tried without the Public Prosecutor's consent (s 79). Asserted.

### 6. The immunity for aircraft seizures yields to negligence

s 13(1) bars suits for acts done in good faith. s 13(2) also bars actions for damage
to, or economic loss from, an aircraft seized under s 92, but s 13(3) excludes loss
"wilfully or negligently caused". Seizure and sale become available only when an
amount stays unpaid 9 months after the later of its becoming outstanding and the
lien's registration (ss 92(1), 93(1)). Asserted.

### 7. The airport development levy attaches to the ticket, not the passenger

s 87A(1): it is payable on "every air passenger ticket that covers at least one
flight" departing Changi for a place outside Singapore, on or after a date set by
order no earlier than 29 June 2018. The amount and the payer are left to the order.
Asserted.

## What would need doing before this is worth anything

- The Gazette orders fixing the levy amounts and start date, and the regulations
  prescribing compoundable offences, were not retrieved.
- s 42 states no penalty and does not say a contravention is an offence; whether the
  s 99 general penalty applies is left open (an inference either way).
- Months under ss 92 and 93 are counted as whole months elapsed, and days under s 57
  as whole days; neither counting rule is in the text.
- s 57(7)(b) and (8)(c) require action "as the Authority may direct" within a time
  it determines; the encoding takes compliance as a single yes or no.
- No case law, Authority decisions or the designated-entity provisions of Part 5
  Division 3 were read.
