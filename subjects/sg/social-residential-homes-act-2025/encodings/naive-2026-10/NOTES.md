# Social Residential Homes Act 2025 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** the Act as enacted (No. 14 of 2025), as deposited at
`../../registers/source-bundle/SRHA2025.txt`. The deposit shows the First Schedule as
amended by S 470/2026 and the Second Schedule as amended by S 471/2026, both "wef
01/07/2026"; no later amendment is annotated. The deposit's metadata says "Current
version as at 01 Oct 2026".

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it is the licensing law for adult
disability homes, homes for children and young persons, sheltered homes for the
elderly and welfare homes, and it sets the rules on restraining residents and on
naming them in public. (An automated count found 2 of the 527 deposited Singapore
Acts citing it by title; that count undercounts and is no measure of importance.)

This row takes what a resident, a family, a member of the public or a care worker
meets: what counts as a licensable home (s 2, s 5, First Schedule), unlicensed
operation (s 6), the penalties for unapproved key staff (ss 17-19), Boards of
Visitors (s 36(6)), force and mechanical restraints (s 37), identifying residents in
publications and broadcasts (ss 38, 39), the 90-day limit on interim orders (s 32(3)),
appeals not suspending decisions (s 49(7)), composition (s 47) and informants
(s 53). The s 45 obstruction maximum is written down but not asserted. Not encoded:
licence applications, grant, conditions, transfer and lapse (ss 7-16), approval of
key staff (ss 20-23), codes and directions (ss 24-26), step-in orders (Part 6),
revocation and suspension beyond s 32(3), enforcement powers, corporate liability,
consequential amendments and the saving and transitional Schedules. Whatever the
Act leaves to regulations ("prescribed") is an input.

## What the Act turns out to say

### 1. Restraining a resident in breach of s 37 is not, in itself, an offence under the Act

s 37(2) forbids anyone working in a licensable home to "use force or any mechanical
restraint" on a resident, and (3)-(5) allow it only to the person-in-charge or a
trained, authorised employee, in a prescribed type of home, for a listed purpose, in
the prescribed manner, and never "as punishment". "Mechanical restraint" expressly
includes handcuffs, leg braces and flexi cuffs (s 37(7)). But s 37 states no penalty,
and none was found elsewhere in the Act; s 37(1) leaves the Penal Code untouched,
and s 32(1)(b)(ii) treats breach of "any provision of this Act, the contravention of
which is not an offence" as a ground for regulatory action. (That s 37 is enforced
through the Penal Code and licensing is an inference from those provisions;
regulations under s 61(4)(d) may create offences.) The permission test is asserted:
an untrained carer, punishment, excessive force and absconding from an unprescribed
home all fail. Asserted.

### 2. Naming a resident online is an offence, even for a family member — unless it is the resident's own story

s 38(1) forbids publishing or broadcasting anything that identifies a resident or
former resident of a prescribed home, or the home or its location, without the
Director-General's prior approval. "Publish" includes messaging systems. The
exceptions are the licensee's own publication or website, and publication "by an
individual, or with the consent of the individual" about that individual; under 18,
only a parent's or guardian's consent counts (s 38(3)). The fine is up to $5,000, or
$10,000 on a second or subsequent conviction, with no imprisonment. A 16-year-old's
own consent to a post by someone else does not suffice. Asserted.

### 3. A court can order a takedown without hearing the poster

s 39 lets a court, "on the application of any person", order removal, deletion and
Internet takedown, even if the application was not served or the respondent did not
appear, if satisfied on a balance of probabilities that it is necessary for
residents' protection and safety, and regardless of whether anyone has been
convicted. Asserted (the case where the respondent was served and appeared is an
inference).

### 4. An elderly disabled resident's home is an adult disability home, not a sheltered home

An adult disability home needs all four services (accommodation, care,
biopsychosocial intervention and daily-living support) and a resident admitted at
18 or older with autism or a disability. A sheltered home serves persons aged 60 or
older but "does not include" premises used as an adult disability home. A home that
admits a 65-year-old with a disability and provides all four services is therefore
an adult disability home. Someone admitted at 17 is outside the definition even
once older. Nursing homes and hospitals ("healthcare premises") are excluded from
every category, and the Act does not apply to Government-run homes (s 5). Asserted.

### 5. "Young person" runs to 21, but boarding schools are carved out

A home for children and young persons gives board and care for "protection or
rehabilitation"; a young person is 14 to below 21. A registered or exempt boarding
school is excluded. Asserted at ages 20 and 21.

### 6. Running an unlicensed home doubles the fine for repeat offenders, counting the old Acts

s 6: up to $100,000 or 2 years; with a "previous qualifying conviction", up to
$200,000. Earlier convictions under the repealed Homes for the Aged Act 1988 s 4(1)
or (4) and the Children and Young Persons Act 1993 s 62(2) count. "Operate" means in
the course of business "whether or not for profit". Asserted.

### 7. Smaller points

Letting unapproved staff act as key appointment holder or person-in-charge, or
deploying them to prescribed duties, is up to $50,000 plus $1,000 a day after
conviction (ss 17-19). Keeping out a Board of Visitors is up to $20,000 or 12 months,
but hindering one is an offence only after the member's identity is reasonably
established (s 36(6)). Interim orders cannot be stated to run beyond 90 days
(s 32(3)). An appeal does not suspend the decision unless the Minister directs, and
the Minister's decision is final (s 49). Composition is capped at the lower of half
the maximum fine and $10,000 (s 47). An informant to an inspecting officer cannot be
held in breach of confidentiality, but is shielded from civil and criminal liability
only in good faith (s 53). Asserted.

## What would need doing before this is worth anything

- The regulations were not retrieved: which homes are prescribed for ss 37 and 38,
  the prescribed manner and conditions for restraint, and which offences are
  compoundable.
- "Child" (Children and Young Persons Act 1993) and "welfare home" (Destitute Persons
  Act 1989) were taken as inputs, not encoded.
- A home is examined through one resident; mixed homes are not modelled.
- The saving and transitional Schedules for existing homes were not read.
- No case law or MSF guidance was searched.
