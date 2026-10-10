# Lease Agreements for Retail Premises Act 2023 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 28 of 2023, informal consolidation, deposited as
`../../registers/source-bundle/LARPA2023.txt`. Every page is footed "version in
force from 1/2/2024"; no amending Act or subsidiary legislation is annotated. The
deposit's metadata says "Current version as at 01 Oct 2026". The text does not
say when Part 3 commenced (s 1 leaves it to Gazette notification), so that date
is an input, not a fact, in this encoding.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: anyone who rents a shop, salon, clinic,
food outlet or other retail unit in Singapore on a lease of a year or more is
under it, on both sides of the counter. This row takes which leases the Act
covers, what counts as non-compliance with a leasing principle, the consequence
of not declaring a permitted deviation, and the dispute route from complaint to
setting aside: ss 2, 6, 9(1), 10(4), 12(1), 14, 17, 18(1), 23(3)-(5), 24(3)-(5),
25(6), 26, 27(4), (6), 35(1) and both Schedules. The Committee, the register,
disclosure of declarations, filing formalities, immunities, stays,
admissibility, adjudication confidentiality, the adjudicator's procedural powers
and the court's powers on setting aside are not encoded.

**The substance is not in the Act.** The leasing principles live in the Code of
Conduct for Leasing of Retail Premises in Singapore (s 5), which is not in the
deposit. Which matters are mandatory, which deviations are permitted, and which
need a declaration are therefore inputs here.

## What the Act turns out to say

### 1. The Act has no offences and no penalties

Nothing in the Act makes a breach of a leasing principle an offence or attaches a
fine. The remedies are a complaint, mediation, adjudication (variation of the
lease, or compensation "provided by the leasing principle", s 25(4)), and the
Committee's power to "publish any details of non-compliance" (s 30). The word
"offence" appears only in the disclosure exceptions. Not asserted (an absence).

### 2. A landlord's missing declaration voids the deviation, except on rent

Where a principle requires it, the landlord alone must declare a permitted
deviation, in time and with the fee (s 6(2), (3)). If not, "the permitted
deviation is void (but not if the permitted deviation relates to a rental
formula)" (s 6(4)(a)). The same rule is repeated word for word for variations
made by settlement in mediation (s 23(5)) and in adjudication (s 24(5)).
Asserted.

### 3. One year, counted without the options, and old options are grandfathered

A qualifying lease needs a term of at least one year, and "any period ... for
which the lease may be extended or renewed ... is to be disregarded" (First
Schedule). A six-month lease with renewal options is outside the Act, and so is
each six-month renewal, as the Schedule's own illustration says. Each extension
or renewal is treated as a separate lease (s 2(5)), but s 35(1) exempts an
extension of a lease signed before Part 3 commenced if its terms were agreed then
and "remain unchanged". Change the rent and the Act applies. Asserted.

### 4. Only the complainant can take the dispute to adjudication

Every complaint goes first to a mediator (s 11(1)). If mediation does not settle
it, "the party that filed the complaint" may apply for an adjudicator (s 12(1));
the respondent has no such right. A person who mediated a complaint may not
adjudicate it (s 10(4)). Asserted.

### 5. Consent of everyone does not let the mediator brief the adjudicator

s 18(1) permits disclosure of mediation communications with all parties'
consent, for legal advice, under a court order and so on, but "subject to
section 17(2)", which forbids the mediator telling the adjudicator anything about
the mediation. Asserted.

### 6. Setting aside costs money up front, and respondents are held to their response

A party who wants a determination set aside in the High Court "must pay into
court as security the unpaid portion" of what it owes (s 27(4)). A respondent may
not rely on a ground it did not raise in its response unless the circumstances
arose later or it could not reasonably have known of them (s 27(6)). A
determination binds until the court refuses enforcement, a court or tribunal
finally decides, or the parties settle (s 25(6)). Asserted.

### 7. Who can complain

Only "a landlord or a tenant under a qualifying lease" may file (s 9(1)). A
guarantor is neither, on the text. "Lease" includes a licence, sub-lease and
sub-licence (s 2(1)), so a sub-tenant is a tenant under its own sub-lease (an
inference from the definition). Only the first part is asserted.

## What would need doing before this is worth anything

- The Code of Conduct and its leasing principles must be retrieved; without them
  the non-compliance rule is a frame with no content.
- The commencement date of Part 3, the Regulations (declaration periods, fees)
  and the authorised dispute resolution body's rules (complaint and adjudication
  periods) were not retrieved.
- "Used primarily" (Second Schedule) is taken as a single input; mixed-use
  premises are not modelled.
- No adjudication determinations or case law were searched.
