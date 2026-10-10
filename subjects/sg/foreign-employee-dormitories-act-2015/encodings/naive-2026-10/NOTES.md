# Foreign Employee Dormitories Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/FEDA2015.txt`. The deposit says the revised edition
incorporates amendments up to 1 December 2021, and each page is headed "Informal
Consolidation – version in force from 1/12/2025". The latest amendment annotated is
Act 31 of 2023 (Immigration (Amendment) Act 2023), which touches the s 2(1)
definitions of "foreigner" (wef 31/12/2024) and "permanent resident of Singapore"
(wef 01/12/2025).

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it governs the large dormitories where
many foreign workers in Singapore live, and what the Commissioner may order their
operators to do. This row takes who is a foreign employee and which premises are a
dormitory (ss 2, 3), the licence requirement (s 7), licence term and renewal (s 10),
the Commissioner's powers as they reach residents (ss 12–15), stopping operation
(s 20), questioning and arrest (ss 24(6), 25(4)), false information and obstruction
(s 26) and composition (s 28). Not encoded: application contents and inspection
(s 8), grant criteria (s 9), licence conditions (s 11), disqualification, transfer,
annual returns, codes of practice, the Register (ss 16–19, 21), appeals (ss 22–23),
the entry and search powers in s 24(1)–(5), officers' liability (s 27) and service
(s 30). No regulations, codes or Gazette notifications were retrieved.

## What the Act turns out to say

### 1. The Commissioner can lock residents in, with no hearing first

s 13(4)(d): where s 13(1)(c) applies — a "serious and imminent threat" to residents'
safety and health, or civil unrest, hostilities, war, "election or other event" that
"may occasion disorder" — a compliance directive may order the operator "to check or
control the movement of residents ..., including restricting entry to and exit from
those premises". s 13(9): there is no need to give the operator a reasonable
opportunity to be heard first. The residents themselves are not parties to the
directive at all. A stoppage of the premises as a dormitory is capped at 3 months
(s 13(4)(c)); the movement power carries no stated time limit. Asserted (the trigger
and the 3-month cap).

### 2. The Act's own threshold is 1,000 beds or residents — or whatever lower number is gazetted

s 3(1), (3): boarding premises are a foreign employee dormitory if they provide the
"threshold number" of beds for, or house that number of, foreign employees, or have
the "prescribed occupancy load" and house "substantially" foreign employees. The
threshold is 1,000 "or any lower number that the Minister may, by notification in
the Gazette, prescribe". No notification was retrieved, so the encoding takes the
threshold as an input; whether a lower number is in force is not known from the
deposit. Houses, flats, hotels, hostels, student halls, nursing homes, prisons, crew
vessels and crisis accommodation are outside the Act whatever their size (s 3(2)).
Asserted.

### 3. A dismissed worker is still a "foreign employee"

s 2(1): a foreign employee includes a foreigner "whose employment in Singapore has
expired or has been terminated (whether or not for justified reasons)" and who is
authorised under the Immigration Act 1959 to remain. Citizens and permanent
residents never are, and a self-employed foreigner is excluded — though that
exclusion sits only in paragraph (a), so this row reads it as not reaching a worker
whose employment has ended (an inference). Asserted.

### 4. A tenancy signed against a business restriction directive is void

s 15(2): "Any purported entry, renewal or extension of an occupancy agreement in
contravention of a business restriction directive is void and of no effect." The
directive is given to the operator (s 14(2)(b)(iii)); the Act does not say what
becomes of a resident whose renewal is void. Asserted.

### 5. Unlicensed operation is the heaviest offence; composition never exceeds $5,000

s 7(3): up to $500,000 or 2 years, and $1 million or 4 years on a repeat conviction,
for the operator and for a proprietor who lets the premises be used without a
licensed operator — unless the proprietor proves it "did not know, and could not
reasonably have been expected to know" (s 7(4)). A compliance-directive breach adds
up to $10,000 "for every day or part of a day" after conviction (s 13(6)). s 28 caps
composition at the lower of half the maximum fine and $5,000; since every offence in
the Act itself has a maximum fine of at least $10,000, the cap for those is always
$5,000 (an inference from reading the penalty provisions; which offences are
compoundable is prescribed and was not retrieved). Asserted.

### 6. Residents questioned by an inspector have a privilege and a right to interpretation

s 24(6): a person asked must "state truly", but "need not say anything that might
expose that person to a criminal charge, penalty or forfeiture". s 24(7): the
statement is written down, read over, interpreted if the person "does not
understand English", and signed. s 26(4): refusing an inspector who will not declare
office or produce the identification card on demand is not obstruction. s 25(4): an
inspector may hold an arrested person no more than 48 hours, excluding the journey to
the Magistrate's Court. Asserted (the privilege, s 26(4) and s 25(4)).

### 7. Closing a dormitory needs 28 days' notice and may require rehousing help

s 20: an operator may not wholly and permanently cease, or surrender the licence,
without the Commissioner's prior approval, sought at least 28 days ahead; approval
may require "assistance to foreign employees who are residents ... to find
alternative accommodation in Singapore". Ceasing without approval: up to $200,000 or
2 years. Asserted.

## What would need doing before this is worth anything

- The Foreign Employee Dormitories regulations, any Gazette notification lowering the
  s 3(3) threshold, the prescribed occupancy load and the list of compoundable
  offences were not retrieved.
- "3 months before" expiry (s 10(4)) and the day counts in ss 12, 13 and 20 are
  modelled as whole numbers of months or days; the computation of time was not read.
- The interaction of s 13 directives with residents' rights under other Acts was not
  examined; no case law or MOM guidance was searched.
