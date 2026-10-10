# Minors' Contracts Act 1987 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/4/2022"), as deposited at `../../registers/source-bundle/MCA1987.txt`. The latest
amendment annotated is Act 25 of 2021 (Courts (Civil and Criminal Justice) Reform Act
2021, s 163), in force 1 April 2022, against s 3(1) and (2). The deposit does not show
what that amendment changed.

**Checks:** one case file, 44 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for **everyday-life relevance** (Tier 1), not by citation count: it decides
what happens when a shop, lender or landlord deals with someone under age, whether
the parent who guaranteed the deal is still liable, and whether the goods can be got
back. The Act has only four operative sections, and all four are encoded (ss 1 to 4).
Who counts as a "minor", and when a minor's contract is unenforceable or may be
repudiated, are **not in this Act** and are not encoded.

## What the Act turns out to say

### 1. The Act never says who a minor is, or which contracts bind one

There is no definition of "minor" and no age. Sections 2 and 3 both start from a
contract that already "is unenforceable against" the minor "because he was a minor"
or that the minor "repudiates". Whether that is so comes from outside the Act (the
common law and other Acts, none read here). The encoding therefore takes it as an
input. Asserted: a contract that binds the minor triggers neither s 2 nor s 3.

### 2. A guarantor cannot hide behind the minor's age

s 2: where the minor's obligation is unenforceable (or repudiated) because of
minority, "the guarantee shall not for that reason alone be unenforceable against the
guarantor". A parent who guaranteed a teenager's phone plan or loan loses the
minority defence. "For that reason alone" leaves every other defence open, so the
encoding says only that the guarantor cannot rely on the minority, not that the
guarantee is enforceable. A contract void for some other reason is outside s 2.
Asserted.

### 3. Restitution is discretionary and is of property, not money

s 3(1): the court "may, if it is just and equitable to do so" order the minor to
transfer "any property acquired ... under the contract, or any property representing
it". There is no power here to order the price paid or damages; s 3(2) keeps any
other remedy the claimant has. That the minor must still hold the property (or its
substitute) is an inference from "transfer", labelled as such in the .l4; a minor's
loan already spent is outside the order. Asserted.

### 4. 9 April 1987 itself is excluded, and 1987 to 1993 contracts need a second statute

Every section speaks of contracts made "after 9 April 1987", so a contract made on
that day is outside the Act. s 4 then excludes contracts made after 9 April 1987 and
"before 12 November 1993" except so far as the Act applied through s 5 of the Civil
Law Act 1909 as then in force. A contract of 12 November 1993 is fully covered; one of
11 November 1993 is covered only through the old Civil Law Act. The content of that
s 5 is not in the deposit and is an input. Asserted.

### 5. It is an English statute, applied

The Legislative History records the Act as U.K. 1987, c. 13, declared to apply in
Singapore by the Application of English Law Act 1993 from 12 November 1993. It lists
the application as "except sections 1(b) and 4(1)", which are U.K. section numbers
that do not match the Singapore text deposited (whose s 1 and s 4 have no
subdivisions). Not asserted.

## What would need doing before this is worth anything

- The age of majority, and the rules on when a minor's contract is void, voidable or
  binding (necessaries, beneficial contracts of service, ratification), from outside
  this Act.
- The pre-1993 s 5 of the Civil Law Act 1909, for s 4.
- What Act 25 of 2021 changed in s 3.
- No case law on s 2 or s 3 was searched.
