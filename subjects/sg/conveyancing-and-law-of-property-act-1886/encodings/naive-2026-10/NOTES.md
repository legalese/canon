# Conveyancing and Law of Property Act 1886 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table,
no independent test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, informal consolidation, "version in force from
1/4/2022", deposited at `../../registers/source-bundle/CLPA1886.txt` (retrieved
1 October 2026). The latest amendment annotated in the text is Act 25 of 2021, with
effect from 1 April 2022.

**Checks:** one case file, 60 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0029**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet.

The Act runs to 75 sections and a Schedule, much of it 1886 conveyancing machinery.
This row takes what a home buyer, landlord, tenant, borrower, lender or co-owner
meets: how far back a buyer may demand title (s 3(3), (4)), consent to assign (s 17),
forfeiture and relief (ss 18, 18A), redemption, leasing, sale, insurance and
receivers (ss 21-26, 28, 29(1), (6)), deeds in English (s 53), joint tenancy and
severance (s 66A), co-owners' rents (s 73A), service of notices (s 72), voluntary
dispositions (s 73C) and the offence ceiling for the conveyancing-money rules
(s 73D(2)(h)). Not encoded: implied covenants for title, the rest of Part 3,
ss 19, 20, 27, 30, statutory mortgage forms, court-made easements, Parts 6-10, most
of Part 11, Parts 12-14, life policies (s 73), the rules and adjudication scheme
themselves (ss 73D, 73E) and Part 16.

## What the Act turns out to say

### 1. A buyer at a mortgagee's sale is safe even if the sale was wrongful

s 26(2): the purchaser's title "shall not be impeachable" because no case had arisen
for the sale or due notice was not given. The owner's only remedy is "in damages
against the person exercising the power". Asserted.

### 2. A lender can sell after one month's unpaid interest, without notice

s 25 gives three alternative triggers: (a) a notice demanding payment followed by
3 months' default; (b) interest "in arrears and unpaid for one month after becoming
due"; or (c) a breach of another term of the deed. Only (a) needs a notice. A receiver
may be appointed only once the power of sale is exercisable (s 29(1)). Asserted.

### 3. A landlord must give notice before forfeiting for most breaches, but not for unlawful assignment, bankruptcy or rent

s 18(1) bars forfeiture unless a notice specifies the breach and the tenant fails to
remedy it (where remediable) and to compensate within a reasonable time, "notwithstanding
any stipulation to the contrary" (s 18(10)). Subsections (8) and (9) take out covenants
against assigning or under-letting, forfeiture on bankruptcy or execution, and non-payment
of rent. For rent, s 18A lets the tenant stop the action by paying all arrears and costs
into court in time, and a possession order may not take effect in less than 4 weeks.
Asserted.

### 4. A landlord may not charge for consent to assign, only for expenses

s 17(1) reads into every covenant against assigning without consent a proviso that no
fine is payable for the consent, unless the lease expressly says otherwise; a reasonable
sum for legal or other expenses may still be required. Asserted.

### 5. A severance deed counts as served even if it comes back, but other notices do not

s 66A(6): a severance deed sent by registered post is deemed served 2 days after posting
"notwithstanding it is returned undelivered". Under s 72(4), other notices under the Act
sent by registered letter are served only "if that letter is not returned". The severing
joint tenant takes an equal share (s 66A(4)). Asserted.

### 6. Fixed figures

A mortgagee insuring under the Act may insure for the amount in the deed or, if none,
two-thirds of the cost of restoring the property after total destruction (s 28(1)). A
receiver's commission is the rate in his appointment, not exceeding 5%, or 5% where none
is specified (s 29(6)). A buyer may not demand title for more than 15 years or past a
State grant, whichever is shorter (s 3(4)); recitals 12 years old are sufficient evidence
unless proved inaccurate (s 3(3)). Offences under the conveyancing-money rules carry up to
$50,000 or 3 years (s 73D(2)(h)). Asserted.

## Inferences, labelled

- s 22: "3 months' interest" is computed as simple interest at the mortgage rate for a
  quarter of a year. The Act does not say how.
- s 29(6): a specified rate above 5% is capped at 5%, reading "not exceeding".
- s 73A: the amount to account for is taken as the excess over the co-owner's share.
- s 26(3): a shortfall is not dealt with; the residue floors at nil.
- s 18(1): "reasonable time" is not modelled; flags record whether the tenant acted.

## What would need doing before this is worth anything

- No rules made under s 73D (to regulate "the receipt, holding and distribution of
  conveyancing money") were retrieved.
- Contrary intention in the mortgage deed (ss 21(2), 23(11), 24(3)) is reduced to a flag.
- The Land Titles Act 1993 was not read alongside. (Inference, not from the deposit: it
  is likely to govern much of what Part 4 covers for registered land.)
- No case law (for instance on s 18 relief or a mortgagee's duty on sale) was searched.
