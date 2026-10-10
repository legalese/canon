# State Lands Protection Act 2022 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 42 of 2022, informal consolidation, "version in force from
29/5/2026", as deposited at `../../registers/source-bundle/SLPA2022.txt` (retrieved
1 October 2026). The only amendment annotated is Act 8 of 2026, with effect from
29 May 2026, which renames the Sewerage, Drainage and Coastal Protection Act in
ss 3(4)(b) and 32(1)(c).

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0070** in `subjects/sg/requirements.jsonl`: Tier 2 of
the remaining Singapore Acts, ordered by everyday-life relevance. It asks what the
Act decides for a person or business it applies to. No scenario has asked a
sharper question yet.

This row covers ss 3, 5-7, 10, 12-20, 26 and 27: what counts as State land, what
may not be done on it, the penalties and defences, the vehicle owner's duty to
name the driver, the encroachment-notice procedure, forfeiture of abandoned land,
obstructing officers and composition. Not encoded: interim injunctions (s 9),
the court's additional orders on conviction (s 8), enforcement powers in detail
(ss 21-24), disposal of seized things (s 25), administration (ss 28-31), liability
of corporations and partnerships (ss 34, 35), service (s 37), and the amendments,
repeal and transitional provisions (ss 40-46).

## What the Act turns out to say

### 1. Not knowing the land was State land is no answer for the prosecution, and only a defence if you prove it

Under s 5(3) the prosecution does not have to prove that the accused "knew or
had reason to believe" the land was State land. Under s 7(1) the accused has a
defence only by proving, on a balance of probabilities, that they did not know
**and** could not reasonably have been expected to know. The offence still requires
the act itself to be intentional and done without "lawful authority", meaning the
Authority's permission or a written law. Asserted.

### 2. Much public land is outside the Act

Under s 3(4), national parks, nature reserves, public parks, NParks green verges,
drainage reserves, railway land, public streets, street reserves and backlanes vested
in the Government are "not ... treated as State land" for this Act. Other Acts govern
them, and s 32(1) preserves those Acts. Land stops being State land once the price
is received, even before the buyer is registered (s 3(2)(a)). Land sold by tender
stops being State land once the deposit is received, and becomes State land again
if the purchaser fails to complete (s 3(3)). Land gazetted for compulsory acquisition
is State land unless the notification is cancelled before possession (s 3(1)(d)).
Asserted.

### 3. The doubled penalty for dumping catches lorries and boats but not motorcycles

The ordinary maximum is $50,000 or 6 months, plus up to $500 a day for a
continuing offence after conviction (s 6(1)). A repeat offender who dumps using a
motor vehicle or vessel faces $100,000 or 12 months (s 6(2)), where an earlier
conviction within 5 years counts, including one under the repealed 1883 Act. But
s 6(3) defines "motor vehicle" as having "4 or more wheels", so dumping from a
motorcycle can never trigger the higher tier. The encoding treats an earlier
conviction exactly 5 years before as counting (an inference). Asserted.

### 4. An encroachment notice runs on two clocks, and objecting stops the Authority's self-help

The objection period may not be longer than the compliance period (s 12(4)).
Failing to comply without reasonable excuse is an offence with a fine of up to
$10,000 (s 12(6)), but only for a person who has not objected in time (s 12(5)).
The Authority may do the work itself only when the person has neither complied
nor objected (s 13(1)). It may require a deposit with at least 7 days to pay.
Unpaid expenses become arrears one month after the certificate is given, or later
if the Authority allows (s 14(4)). Once a person objects, the officer's route is a
complaint to a Magistrate (s 16(1)). A person who claims title can have that
complaint stayed pending the High Court, and the Magistrate **must** grant the
stay if satisfied the claim is genuine (s 16(4)). Asserted.

### 5. A vehicle owner must name the driver within 14 days, and cannot plead self-incrimination

When a dumping offence from a motor vehicle or vessel is suspected, the owner must
identify the driver and passengers. Failing to do so within 14 days without
reasonable excuse carries a fine of up to $10,000 (s 10(2)). The owner "is not
excused" because the answer might incriminate them (s 10(3)). Asserted.

### 6. Abandoned land is forfeited after 3 years, compensation is capped, and State land cannot be squatted into ownership

Land abandoned for 3 years or more may be declared liable to forfeiture "even
though some person may be found in occupation" (s 17). If nobody sues to recover
possession within 3 months of the gazetted resumption notice, the land is deemed
forfeited (s 18(4)). A claimant who establishes a claim within 6 years gets
whatever the Minister directs, up to the appraised value (s 19). Under s 18(3),
failure to publish the notice does not invalidate the declaration, but the
3 months run from publication. The encoding therefore requires publication before
deemed forfeiture (an inference). Under s 20, State land cannot be "acquired by
possession or unlawful occupation", and the Limitation Act does not apply to the
Government's action to recover it. Asserted.

### 7. You may refuse an officer who will not identify themselves, but only if they fail on both counts

Obstruction is punishable by $10,000 or 12 months (s 26(1)). It is not an offence
to refuse an officer who "fails to declare his or her office **and** refuses to
produce his or her identification card on demand" (s 26(3)). Composition is capped
at the lower of half the maximum fine and $5,000 (s 27(1)). That is $5,000 for every
offence with a maximum fine of $10,000 or more, and $2,500 for removing an affixed
notice (s 26(2), maximum fine $5,000). Which offences are compoundable is left to
regulations, which were not retrieved. Asserted.

## What would need doing before this is worth anything

- The regulations prescribing compoundable offences, and any other subsidiary
  legislation, were not retrieved.
- s 7(2), the defence for subterranean structures under the State Lands Act
  easement of support, is not encoded.
- s 8, the court's power on conviction to order payment of the value taken, costs
  and compensation, and to cut off electricity, gas and water, is not encoded.
- The boundary readings ("within 5 years", "at the end of one month", "before the
  end of one year" taken as under 365 days) are the encoder's and are untested
  against any decision.
- No case law was searched.
