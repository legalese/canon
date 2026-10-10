# Unfair Contract Terms Act 1977 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/UCTA1977.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021; the only amendment annotated in the
body is [44/96] (s 7(3A), (4)).

**Checks:** one case file, 41 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes the controls
that decide whether an exemption clause survives: business liability (s 1(3)),
negligence (s 2), contract (s 3), consumer indemnities (s 4), sale of goods (s 6),
title in other supply contracts (s 7(3A), (4)), the burden of proving reasonableness
(s 11(5)), dealing as consumer (s 12), international supply contracts (s 26), choice
of law (s 27) and First Schedule paragraphs 1 and 4. Reasonableness itself is taken as
a finding: the s 11(1)-(4) test and the Second Schedule guidelines are not encoded.
Notices that are not contract terms, s 5 guarantees, ss 9, 10, 13, 28, 29, 30(2) and
the shipping paragraphs of the First Schedule are not encoded.

## What the Act turns out to say

### 1. Title to goods cannot be excluded even by a private seller

s 6(1) bars any term excluding the seller's implied undertakings as to title, and
s 6(4) says the s 6 liabilities are "not only the business liabilities defined by
section 1(3)". Everything else in ss 2 to 7 is limited to business liability, so a
private host's waiver of a guest's injury claims is untouched by the Act, while a
private seller's title exclusion is void. The First Schedule paragraph 1 exceptions
(insurance, land, IP, companies, securities) are written for "Sections 2 to 4" and do
not mention s 6. Asserted (the private-seller and private-host cases).

### 2. Negotiated business-to-business terms on contract liability escape s 3 entirely

s 3 applies only where one party "deals as consumer or on the other's written standard
terms of business". A negotiated delay exclusion between two businesses is not
controlled at all; the same clause on the supplier's standard terms is controlled
only so far as reasonable. Asserted.

### 3. The party relying on the clause must prove it reasonable

s 11(5): "It is for those claiming that a contract term or notice satisfies the
requirement of reasonableness to show that it does." Unproven, a reasonableness-
controlled clause cannot be relied on. By contrast s 12(3) puts on the other side the
burden of showing someone did not deal as consumer (noted, not modelled). Asserted for
s 11(5).

### 4. Two cross-border doors out of the Act, one door back in

An international supply contract (s 26: goods, parties in different States, and
carriage, offer and acceptance, or delivery across States) is outside the limits,
even against a consumer. Where Singapore law applies "only by choice of the parties",
ss 2 to 7 do not operate (s 27(1)). But a foreign choice of law does not oust the
Act if imposed mainly to evade it, or if a consumer habitually resident in Singapore
took the essential steps here (s 27(2)). Asserted.

### 5. Employment: the protection runs one way

First Schedule paragraph 4: s 2(1) and (2) do not extend to a contract of employment
"except in favour of the employee". An employer cannot exclude liability for injuring
the employee; an employee's exclusion of loss to the employer is outside s 2. Asserted.

### 6. Who is a consumer

s 12: the party must not act (or hold himself out as acting) in the course of a
business; the other party must; for goods contracts the goods must be of a type
ordinarily supplied for private use; and an auction or competitive-tender buyer is
never a consumer. Buying from a private seller is therefore not dealing as consumer.
Asserted.

## What would need doing before this is worth anything

- Notices (s 2 covers non-contractual notices, with the s 11(3) test) are not modelled.
- The reasonableness test and Second Schedule guidelines are a boolean finding here.
- s 13 (restrictive conditions, remedies, evidence rules treated as exclusions; the
  arbitration carve-out) would widen what counts as an exclusion and is not encoded.
- First Schedule paragraphs 2 and 3 (salvage, charterparties, carriage of goods by
  sea) and s 28 orders for sea passengers were not encoded.
- The interaction of the Sale of Goods Act 1979, Hire-Purchase Act 1969 and Supply of
  Goods Act 1982 provisions that s 6 and s 7 refer to was not read; hire-purchase is
  not modelled. No case law was searched.
