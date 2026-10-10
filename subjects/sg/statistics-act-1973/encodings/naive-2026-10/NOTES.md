# Statistics Act 1973 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/SA1973.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021; the latest annotation in it is
S 439/2026 (wef 30 June 2026) to the Second Schedule. The arrangement of sections
at the top of the deposit is numbered one ahead of the body (it lists "2. Short
title"); the encoding follows the body.

**Checks:** one case file, 49 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**7 of the 527 Singapore Acts** deposited here cite it. This row takes what a
respondent or a public agency meets: the requisition and the duty to answer it
(s 5 and the First Schedule), the Chief Statistician's directions to agencies
(s 6), secrecy and its exceptions (s 7 and the Third Schedule), impersonation
(s 8), the requisition offences (s 9), composition (s 10) and service (s 11).
The coordinator's duties and the refusal procedure for research and statistics
units (s 4), the s 6(4) immunities, the s 9(2) certificate, rules (s 12) and
amendment of the Schedules (s 13) are not encoded.

## What the Act turns out to say

### 1. Refusing to answer a survey costs at most $1,000; leaking the answers costs $10,000 or a year

s 9(1): failing to answer a requisition, or wilfully giving false particulars, is
punishable by a fine not exceeding $1,000, plus up to $100 a day while it continues
after conviction. No imprisonment is provided. s 7(4): disclosure contrary to s 7
is punishable by up to $10,000, 12 months, or both. And s 10 lets the Chief
Statistician or a director compound any s 9(1) offence for a sum not exceeding
$200, but no other offence. Asserted.

### 2. Impersonating a statistical officer carries prison only

s 8(1) provides imprisonment not exceeding 6 months and no fine at all. A
"statistical officer" is an officer of the Department of Statistics or of a
research and statistics unit (s 8(2)). Asserted (maximum fine encoded as 0).

### 3. The Chief Statistician's direction overrides confidentiality, but not MAS data or a Minister's exemption

s 6(1)(b), (2): a public agency must hand over what it holds "despite ... any
other written law", whether or not it or its data source is under an obligation
not to disclose. The only outs are an exemption by the Minister responsible for the
agency or for the data source, and those apply only to (1)(b) directions, not to a
direction to a research and statistics unit director. s 6(5) takes information
obtained under any law the Monetary Authority of Singapore administers outside
s 6(1) entirely, although the MAS Statistics Unit is itself listed in the Second
Schedule. Asserted.

### 4. The secrecy exceptions belong to the Chief Statistician and directors alone

s 7(1) forbids anyone to disclose s 5 or 6 information in a form that may identify
a person without that person's prior written consent. The s 7(2) exceptions
(non-identifying statistics, anonymised microdata to a public agency or a Third
Schedule class, offence proceedings, general information about an establishment,
the public domain) are available only to "the Chief Statistician or the director of
a research and statistics unit". So an establishment's address may be released by
the Chief Statistician but not by a junior officer, and microdata received by a
consultant may not be passed on. Breaching a condition imposed under s 7(3) is
itself an offence. Asserted. INFERENCE: anonymised microdata is treated as a form
that "may identify" a person, since s 7(2)(b) would otherwise be pointless; the
text does not say so.

### 5. Only listed subjects, only from the listed people, only what you know

A requisition is valid only from the Chief Statistician or the director of a
Second Schedule unit, for a First Schedule subject (s 2 "statistical purposes"),
in writing, served under s 11 and specifying what is required (s 5(1), (2)). Even
then, s 5(4): no one is bound to give anything not accessible to them or derived
from their own business, occupation or work. For s 9(1)(a), the lawful-excuse
defence (burden on the person) attaches to neglect, not to wilful refusal.
Asserted. INFERENCE: information outside s 5(4) is not "required by a
requisition", so not giving it is no s 9 offence.

### 6. Fax works on a company but not on an individual; affixing is the reverse

s 11(1): an individual may be served by affixing a copy at their address but not by
fax; a partnership or body corporate by fax but not by affixing. An occupier may be
served by affixing only if no adult can with reasonable diligence be found on the
premises (s 11(2)). Any of them may be served through an agent in Singapore
(s 11(4)). Asserted.

## What would need doing before this is worth anything

- s 11(1) is "subject to any rules made under section 12", and s 12(1)(c) allows
  rules exempting people from the duty to furnish; no rules were retrieved.
- The First Schedule subjects are represented by six samples and one "not listed"
  placeholder, not the full list of 55.
- s 4 (coordination, the refusal procedure), the s 6(4) immunities and the s 9(2)
  certificate are not encoded.
- No case law or Department of Statistics practice was consulted.
