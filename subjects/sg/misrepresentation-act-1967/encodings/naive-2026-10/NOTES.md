# Misrepresentation Act 1967 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else (the skill itself was not loaded in this session; the
finished naive rows were followed instead). No pipeline, no coverage table, no
independent test pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all amendments
up to and including 1 December 2021 and comes into operation on 31 December 2021". No
later amendment is annotated. The deposit's metadata calls it the current version as
at 1 October 2026.

**Checks:** one case file, 46 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: anyone who buys a flat, a used car, a
renovation package or a course because of what the seller said meets this Act when
the statement proves false. (An automated count found 1 of the 527 deposited
Singapore Acts citing it by its slug title; that count undercounts and is no measure
of importance.) The Act is five short sections, so the row takes all of ss 1–4.
Section 5 is the short title. What a misrepresentation is, when rescission is
available at common law, the measure of damages, the Unfair Contract Terms Act 1977
reasonableness test and the Civil Law Act 1909 s 5 are all left as inputs.

## What the Act turns out to say

### 1. An honest but careless seller is liable unless the seller proves otherwise

s 2(1): a non-fraudulent misrepresentation by the other party attracts damages as if
it were fraudulent, "unless he proves that he had reasonable ground to believe and did
believe up to the time the contract was made that the facts represented were true".
The burden is on the representor, and both limbs are needed: reasonable ground
without proof of belief, or belief without reasonable ground, still leaves the seller
liable. Asserted.

### 2. Only a statement by a party to the contract counts under s 2(1)

The misrepresentation must be made "by another party thereto". A statement by a
stranger to the contract gives no s 2(1) claim, however much loss it causes. Whether
an agent's statement is the party's is not answered by the Act. Asserted.

### 3. A clause excluding liability for misrepresentation is void unless shown reasonable

s 3: a term excluding or restricting liability, or any remedy, for a pre-contract
misrepresentation "shall be of no effect except in so far as it satisfies the
requirement of reasonableness" in the Unfair Contract Terms Act 1977 s 11(1), and "it
is for those claiming that the term satisfies that requirement to show that it does".
A damages cap and a clause removing rescission are caught as well as a total
exclusion. Whether an "entire agreement" or "non-reliance" clause is such a term is
not answered by the Act, and is not encoded. Asserted.

### 4. The court can keep the contract alive and give damages instead

s 2(2): for a non-fraudulent misrepresentation, where rescission is claimed in
proceedings, the court or arbitrator may declare the contract subsisting and award
damages in lieu, if equitable. This needs no proof of fault and is unavailable for
fraud. s 2(3): it may be awarded whether or not the representor is liable under
s 2(1), but is "taken into account" in assessing s 2(1) liability. The encoding reads
"taken into account" as a deduction, never below zero; that is an inference, not the
text. Asserted.

### 5. Performance and incorporation do not bar rescission

s 1: a representee otherwise entitled to rescind without alleging fraud keeps that
right even though the misrepresentation has become a term or the contract has been
performed, "subject to the provisions of this Act" (that is, to s 2(2)). Asserted.

### 6. The Act does not reach pre-12 November 1993 dealings

s 4: nothing in the Act applies to a misrepresentation or contract of sale made before
12 November 1993, except so far as it applied through the Civil Law Act 1909 s 5. Read
literally, the contract date matters only for a contract of sale. Asserted.

## What would need doing before this is worth anything

- No case law was searched: what counts as a misrepresentation, the measure of
  s 2(1) damages, agents' statements and non-reliance clauses all turn on it.
- The Unfair Contract Terms Act 1977 s 11(1) test and the Civil Law Act 1909 s 5
  were not read; both are inputs.
- s 3's "in so far as" (partial survival of a term) is not modelled; the term is
  treated as wholly effective or wholly ineffective.
