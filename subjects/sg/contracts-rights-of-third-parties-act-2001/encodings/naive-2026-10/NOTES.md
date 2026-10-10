# Contracts (Rights of Third Parties) Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CRTPA2001.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021. The latest amendments annotated in the body are [40/2019]
(s 3(7)) and [5/2021] (s 7(6), (7)).

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It was chosen for its **everyday-life relevance** to ordinary people in Singapore,
not by citation count. It decides whether someone named in another person's
contract can sue on it: a relative named on a booking, a person goods are bought
for, a subcontractor protected by an exclusion clause. The Act has nine sections,
so this row covers most of it: ss 1, 2, 3, 6, 7 and 9(1). Not encoded: the
promisor's defences, set-off and counterclaim (s 4, summarised in a comment only),
the promisee's own rights (s 5, a saving), the savings and cross-references in s 8,
the Minister's orders naming rail and road conventions, and s 9(2).

## What the Act turns out to say

### 1. A posted acceptance does not lock the contract until it arrives

Once the third party "has communicated" assent to the promisor, the parties cannot
rescind or vary the term without consent (s 3(1)(a)). But an assent sent by post
"or other means" is not communicated "until the assent is received by the promisor"
(s 3(2)(b)). So a third party whose letter is in the post is not yet protected on
that ground. This is the reverse of the postal rule for accepting an offer, though
that comparison is general law, not something the deposit says. Asserted.

### 2. The contract can rewrite the consent rules entirely

s 3(3) makes s 3(1) subject to an express term that lets the parties vary
without consent, or that requires consent "in circumstances specified in the
contract instead of" the statutory ones. Under the substituted circumstances,
a third party the promisor knows has relied on the term can still lose it
if the contract's own circumstances are not met. Asserted.

### 3. Excluded contracts still let a third party shelter behind a limitation clause

s 7 removes the s 2 right for negotiable instruments, company and LLP constitutions,
employment contracts enforced against the employee, and carriage of goods by sea or
under an international convention. For carriage alone, a third party may still
"avail the third party of an exclusion or limitation of liability" (s 7(5)). The
employment exception runs one way only: it bars enforcement "against an employee",
so on this reading a dependant could still enforce a benefit against the employer
(an inference from the wording). Asserted.

### 4. Saying so in the contract beats a contrary construction

The "did not intend" carve-out in s 2(2) applies only to s 2(1)(b), the
benefit limb. A contract that expressly says the third party may enforce
(s 2(1)(a)) is not subject to it. Either way the third party must be "expressly
identified" by name, class or description, and need not exist yet (s 2(3)).
Asserted.

### 5. Consent can be dispensed with, but the uncertain-reliance ground is narrow

A court or arbitral tribunal may dispense with consent where the third party's
whereabouts cannot reasonably be ascertained or the third party is mentally
incapable (s 3(4)), and may attach conditions including compensation (s 3(6)). The
further ground, that reliance "cannot reasonably be ascertained", is tied to
consent required under s 3(1)(c) (s 3(5)). A District Court has the power as well
as the General Division of the High Court (s 3(7), [40/2019]). Asserted.

### 6. The Act did not reach contracts of its first six months unless they opted in

s 1(2) excludes contracts entered into before the end of 6 months from
1 January 2002, unless the contract was made on or after 1 January 2002 and
"expressly provides for the application of this Act" (s 1(3)). The encoding reads
the period as ending on 30 June 2002; that end date is an inference. Asserted.

### 7. The court must reduce the award, but chooses the amount

Where the promisee has already recovered for the third party's loss, or for the
cost of making good the promisor's default, the court "must reduce" the third
party's award "to such extent as it thinks appropriate" (s 6). Only the duty is
encoded. Asserted.

## What would need doing before this is worth anything

- s 4 (defences, set-off, counterclaim) needs encoding; it is where most disputes
  under the Act would turn.
- The cross-references in s 8 (Unfair Contract Terms Act s 2(2), Limitation Act s 6)
  were not followed into those Acts.
- Whether the Minister has made orders under s 7(6)(b), (c) was not checked.
- No case law was searched, including on the meaning of "purports to confer a
  benefit" and "proper construction".
