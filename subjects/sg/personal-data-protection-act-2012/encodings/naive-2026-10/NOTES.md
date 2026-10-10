# Personal Data Protection Act 2012 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/PDPA2012.txt`, with amendments to Act 19 of 2025
(wef 5 December 2025) shown. The Act 40 of 2020 penalty ceilings in s 48J are
annotated wef 1 October 2022.

**Checks:** one case file, 110 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. This row takes the duties an
organisation, a telemarketer or an employee actually meets, and what follows when
they are broken: who Parts 3 to 6A bind (s 4), consent, deemed consent and withdrawal
(ss 13 to 16), retention (s 25), data breach notification (ss 26B to 26D), the Do Not
Call duties (ss 43, 44, 48), the individual offences in Part 9B (ss 48C to 48F), the
ceiling on financial penalties (s 48J) and the right of private action (s 48O).

Not encoded: the Commission (Part 2), policies and practices (s 12), purpose
limitation and notification (ss 18 to 20), access and correction and the Fifth and
Sixth Schedules, accuracy, protection and overseas transfer (ss 23, 24, 26), the
First and Second Schedule exceptions to consent (one flag stands for all of them),
the register and checkers (ss 39 to 43A), calling line identity (s 45), review,
directions, undertakings and appeals, investigation powers, and the s 51 offences.

## What the Act turns out to say

### 1. A scale-only breach goes to the Commission, not to the people affected

s 26B(1) makes a breach notifiable for (a) likely significant harm **or** (b)
significant scale. But s 26D(2) requires notice to each affected individual only for
"a notifiable data breach mentioned in section 26B(1)(a)", the harm limb. A breach of
600 email addresses with no likely harm must be reported to the Commission within 3
calendar days of the assessment, and need not be told to anyone whose address leaked.
Asserted.

### 2. The internal-only carve-out does not cover disposal or a lost device

s 26B(4) deems not notifiable a breach relating to "unauthorised access, collection,
use, disclosure, copying or modification of personal data only within an
organisation". "Disposal" (in the s 26A definition) and loss of a storage medium are
not in that list. Staff browsing medical files internally is never notifiable;
staff shredding them is, if harm is likely. Asserted.

### 3. The scale threshold is not in the Act

s 26B(3) deems a breach of significant scale if it affects "not fewer than the
prescribed number" of individuals. The number is left to regulations, which were not
read; the encoding takes it as a parameter and the cases use 500 only as an example.
Asserted with that parameter.

### 4. Leaking data is an offence even with no gain; misusing it is not

ss 48D (disclosure) and 48F (re-identification) need only unauthorised conduct done
knowingly or recklessly. s 48E (use) adds that the individual "obtains a gain",
"causes harm to another individual" or "causes a loss". An employee who browses a
customer's address out of curiosity commits no Part 9B offence; one who uses it to
harass commits one. All three carry $5,000 or 2 years, and none applies to a
"relevant public official in a Singapore public sector agency" (s 48C(2)). Asserted.

### 5. The penalty ceiling scales with turnover for data protection, not for Do Not Call

s 48J(3): for an organisation, Parts 3 to 6B, 10% of annual turnover in Singapore
where that exceeds $10 million, otherwise $1 million. s 48J(4): for Part 9 (Do Not
Call) the ceiling is $1 million (or $200,000 for an individual) however large the
sender. s 48J(4A): for dictionary attacks (s 48B), 5% over $20 million turnover. These
are ceilings on the prescribed maximum ("in no case may be more than"), and a penalty
is not available where the breach is itself an offence (s 48J(2)). Asserted.

### 6. A private action lies for Parts 4 to 6B, but not for Part 3

s 48O(1) gives a right of action to a person who "suffers loss or damage directly"
from a contravention of "Part 4, 5, 6, 6A or 6B", or Division 3 of Part 9 or s 48B(1).
Part 3 (compliance, policies and practices) is absent. An action must wait until any
Commission decision on the contravention is final (s 48O(2)). Asserted.

### 7. Employees are outside the data protection duties, and largely outside Do Not Call

s 4(1)(b): Parts 3 to 6B impose no obligation on "any employee acting in the course of
his or her employment". s 48(2) lifts ss 43(1) and 44 from an employee who sends a
telemarketing message in good faith for the employer, but s 48(4) takes the shield
away from an officer or partner who knew the number was registered and consented,
connived or was neglectful. Asserted.

### 8. A data intermediary under a written contract keeps only three duties

s 4(2): a data intermediary processing for another organisation under a contract
"evidenced or made in writing" is bound only by s 24 (protection), s 25 (retention),
s 26C(3)(a) (tell the principal of a breach) and s 26E. Without a written contract,
the encoding treats it as bound by everything; that is an inference from s 4(2), not
a line of text. Asserted.

### 9. Part 6B is everywhere and nowhere

ss 4, 48I, 48J, 48O and 51(1)(c) refer to Part 6B and to data porting requests under
s 26H, but the deposited text contains no Part 6B. The encoding names it only where a
provision lists it.

## What would need doing before this is worth anything

- The Personal Data Protection Regulations (prescribed data, the prescribed number of
  affected individuals, prescribed purposes for s 15A, prescribed periods for the
  register and checkers) were not read.
- The date from which the turnover-based ceilings apply (20221001) is read from the
  annotation under s 48J(3), not from a commencement notification.
- The First and Second Schedules (collection, use and disclosure without consent) are
  a single flag; the substance of most day-to-day compliance lives there.
- No Commission decisions or case law were searched.
