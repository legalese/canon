# Foreign Interference (Countermeasures) Act 2021 — naive encoding

**Method: naive.** Written straight from the deposited text, using the `writing-l4-rules`
skill and nothing else. There was no pipeline, no coverage table, no independent test
pass and no human gate. NOT for public use.

**Edition:** Act No. 28 of 2021, informal consolidation, version in force from
8/12/2025, deposited at `../../registers/source-bundle/FICA2021.txt`. It was retrieved
on 1 October 2026 and is marked "Current version as at 01 Oct 2026". The latest
amendment annotated in the body is Act 30 of 2024 wef 01/11/2024. The arrangement of
sections at the top of the deposit does not match the body, so this row uses the body's
section numbers.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0059** in `subjects/sg/requirements.jsonl`. That requirement is
Tier 2 of the remaining Singapore Acts, ordered by everyday-life relevance. It asks what
the Act decides for a person or business it applies to. No scenario has asked a sharper
question yet.

The Act runs to about 186 pages in the deposit, and most of it is ministerial machinery. This row
takes the parts an ordinary person, donor or small organisation meets:

- s 4: foreigners and foreign principals
- s 14: politically significant persons
- ss 17 to 19: the interference offences
- s 45: penalties for ignoring a direction
- ss 53, 55 to 58, 60, 70, 72 and 75(5): political donations
- ss 79 and 86(2): a citizen's foreign political membership

The following are not encoded:

- the Minister's authorisations and the content of each Part 3 direction
- proscribed online locations
- designation of Part 4 persons
- the detailed meaning of "political donation" (ss 51, 52)
- the contents and timing of donation reports
- the stepped-up directives
- foreign-affiliation reports by politically significant persons
- false-report offences
- appeals
- enforcement

Amounts that the Act allows Regulations to raise are encoded at the figure in the Act.
No Regulations were retrieved.

## What the Act turns out to say

### 1. A permanent resident is a "foreigner" and a "foreign principal"

s 4 defines "foreigner" as "an individual who is not a citizen of Singapore", and lists
a foreigner first among foreign principals. The Act has no category for permanent
residents, so a PR falls on the foreign side. s 55(1)(a) also limits permissible
individual donors to citizens aged at least 21. A party must therefore refuse a donation
from a 45-year-old PR, and a 20-year-old citizen cannot donate either. Asserted.

### 2. Taking part in a foreign party is a declarable act for every citizen

s 79 binds "an individual who is a citizen of Singapore (and whether or not resident in
Singapore)", not only politicians. A citizen who becomes a member of a foreign
legislature or foreign political organisation must declare it. Honorary membership
counts. Being only an employee, a regular participant, a regular donor or a lobbyist does
not. Under s 86(2), a late declaration is liable to a fine of up to $5,000 and $200 a day
while it continues. Asserted.

### 3. The covert element is what makes it a crime, not falsity

s 17 requires four things:

- publishing in Singapore
- on behalf of a foreign principal
- knowledge or reason to believe that the material is harmful, or "directed towards a
  political end in Singapore"
- some part that "is covert or involves deception"

None of these requires the material to be false. Openly disclosed foreign-backed
publishing falls outside the offence. The maximum for an individual is $50,000 or 7 years.
Under s 18, where the foreign link is hidden from a person the conduct is meant to
influence, the maximum rises to $100,000 or 14 years, or $1 million for a body. Asserted.

### 4. The continuing fine for an individual can dwarf the base fine

s 45(3) sets the penalty for an individual who ignores an account restriction, disabling
or similar direction. The base is $20,000 or 12 months, but a continuing offence adds a
further fine of up to **$100,000 for every day**. An access blocking direction costs
$20,000 a day, capped at $500,000 in total (s 45(5)). Neither a conflicting contract nor
a pending appeal is a defence (s 45(6)). Asserted.

### 5. The anonymous cap is "less than" $5,000, and one office holder has no cap at all

s 58 allows anonymous donations "which in total are less than" the $5,000 cap. A party
holding $3,000 may therefore take $1,000 but not $2,000. s 57(a) bars every politically
significant person other than a Part 4 person from anonymous donations. The caps in
s 58(2), however, cover parties, candidates, election agents, office holders, MPs and
directed Part 4 persons, and leave out the senior political party official.

**Inference:** read literally, a senior party official may accept no anonymous donation.
The Act does not say this expressly. A designated Part 4 person without an anonymous
donations directive is not bound by s 57 at all. Asserted.

### 6. The major political donor report only covers giving to parties

s 70 makes a donor who is not a politically significant person report donations in a year
totalling at least $10,000. That applies only where the donations went to "any one of" a
political party, or a Part 4 person with a prohibited donor directive. A $50,000 donation
to a candidate does not trigger it. The recipient's own reporting threshold is $10,000,
aggregating earlier donations from the same donor in the same period (s 53(2)). Asserted.

### 7. Thirty days to give it back

Under s 60(3), a prohibited or refused donation must be returned within "a period of 30
days starting the date when the donation is so received". **Inference:** this row reads
the day of receipt as day 1, so the last day is the day of receipt plus 29.

Keeping a prohibited donation past that point is an offence under s 60(4) only where the
recipient "knows or is reckless" about the prohibition. The fine is up to $5,000 or 12
months, plus $500 a day for a party or Part 4 entity and $200 for others. The encoding
gives every designated Part 4 person the entity figure of $500, which is wrong for a
designated individual. Asserted.

## What would need doing before this is worth anything

- **Regulations:** the FICA Regulations were not retrieved. They set the prescribed time
  for s 79 declarations and may raise any threshold.
- **Grace-period counting:** the day count under s 60(3) should be checked against the
  Interpretation Act.
- **Part 4 persons:** designated entities and designated individuals need separating.
- **Unread provisions:** "political donation" (ss 51, 52) and the exempt activities in
  s 120 were not modelled.
- **Case law:** no prosecutions or Reviewing Tribunal decisions were searched.
