# Travel Agents Act 1975 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/TAA1975.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The latest amending Act in the legislative history and in the body
annotations is Act 47 of 2017 (Travel Agents (Amendment) Act 2017, commenced
1 January 2018).

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**, not its citation count. Anyone in
Singapore who books a flight, a package holiday or a guided tour through an agent
deals with a business this Act licenses. Anyone who sells such things, including a
small online operator, needs to know whether it must hold a licence. An automated
count found 1 of the 527 deposited Singapore Acts citing it by its slug title. That
count misses citations by short or older titles, so it says little about how
important the Act is.

This row covers who is a travel agent and must be licensed (ss 2, 3, 4, 6), the
procedural safeguards around refusal, suspension, revocation and financial penalties
(ss 7(4), 9, 10, 11), the maximum penalties for the offences an operator meets
(ss 6, 10, 13, 14, 19, 21, 28(2)), the Public Prosecutor's consent (s 25), the
composition ceiling (s 27) and s 16(4). Not encoded: the refusal and suspension
grounds themselves (except the financial-penalty ground), licence conditions
(s 7A), limits on licence numbers (s 8), publication (s 12), most enforcement powers
(ss 15–18), corporate and partnership liability (ss 20, 20A), service (s 22),
recovery of penalties (s 27A), and the regulations, which were not retrieved.

## What the Act turns out to say

### 1. Misusing customers' money carries prison only, and needs the Public Prosecutor

s 14 covers a licensee who fraudulently converts money received for a customer,
fraudulently fails to account for it or pay it over, or renders a false account. It
is punishable by "imprisonment for a term not exceeding 3 years". No fine is
provided. s 25: "No court is to try an offence under section 14 except with the
consent of the Public Prosecutor". No other offence in the Act has that bar.
Asserted.

### 2. Who counts as a travel agent turns on what you own and on whether someone guides you

s 4(1) catches selling rights to travel, travel plus accommodation, buying travel for
resale and supplying tours. Holding yourself out as doing so is enough. s 4(3) takes
out sellers of their own conveyance, sellers of regular bus, community or courtesy
bus (within Singapore) and train services, package sellers who own BOTH the
conveyance and the hotel, and tour suppliers at a place they own or operate. Owning
the hotel alone does not take a package seller out. Owning the conveyance does not
take out someone who buys travel for resale. "Tour" (s 2) needs the participants to
be accompanied by a non-participant for some part of the visit. On that definition a
self-guided visit is not a tour. Employees and agents of a licensee are not
themselves travel agents (s 4(2)). Government and public bodies are outside the Act
(s 3(5)). Unlicensed trading carries up to $25,000 or 2 years or both (s 6(2)).
Asserted.

### 3. A $2,000 financial penalty can replace suspension, but only for a contravention that is not itself an offence

s 9(2): where the licensee has contravened the Act, the regulations, a licence
condition or a code of conduct (s 9(1)(c)), the Board may impose a penalty "not
exceeding $2,000" instead of suspending or revoking. s 9(3) excludes any
contravention "prescribed to be an offence". No other s 9(1) ground allows it.
Asserted.

### 4. Nothing takes effect until the appeal window closes, and a suspended agent may still finish its existing contracts

s 9(6): a suspension, revocation or penalty takes effect only from the day after the
14-day appeal period (s 11(1)) expires or, if there is an appeal, from the day after it
is withdrawn or the decision is confirmed. s 9(7): during a suspension the licensee may
still do "what is necessary" to fulfil contracts entered into before the suspension took
effect. Before acting, the Board must give 14 days to submit reasons (s 9(4)), unless the
licensee has died, been made bankrupt or ceased to exist (s 9(5)). Asserted. That no
extension of the appeal period is granted is an assumption of the encoding.

### 5. Customers may have to be told within 2 working days

s 10: once the Board serves a s 9(4) notice, it may require the licensee to tell
existing customers with unperformed contracts within 2 working days. Anyone who gets in
touch during the specified period must be told within 2 working days of first contact,
or before a contract is made, whichever is earlier. Failing to do so carries a fine of
up to $4,000. Asserted. The s 10 order is not an "appealable decision" under s 11(11).
Neither is publication under s 12 nor the s 8 limit on licence numbers. Asserted for
s 10 and s 12.

### 6. Notice is owed before refusing a renewal, not a first licence

s 7(4) requires written notice and a chance to submit reasons "before refusing an
application to renew a licence". s 7 says nothing similar about a first application.
Asserted. The composition ceiling is the lower of half the maximum fine and $5,000
(s 27(1)). An arrested woman may be searched only by a woman (s 16(4)). Asserted.

## What would need doing before this is worth anything

- The Travel Agents Regulations (licence classes, minimum financial requirements, the
  code of conduct, compoundable offences, any prescribed s 4(1)(e) activities or
  longer suspension maximum) were not retrieved, and each of these changes results.
- The s 7(3) and s 9(1) grounds are not encoded beyond the financial-penalty ground.
- "3 months" (s 3(2)) and "working days" (s 10) are taken as numbers supplied by
  the caller. No calendar is modelled.
- No Board decisions, Ministerial appeals or case law were searched.
