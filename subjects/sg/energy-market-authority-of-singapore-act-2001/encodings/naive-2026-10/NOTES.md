# Energy Market Authority of Singapore Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/EMASA2001.txt`. The deposit's cover says it
"incorporates all amendments up to and including 1 December 2021"; later amendments
are annotated in the body, the latest being Act 27 of 2024 (s 19B in force 1 July
2025; s 5(1) in force 31 March 2025; ss 19 and 19A in force 8 November 2024). The
arrangement of sections at the top of the deposit is out of step with the body (it
lists 19A, 19B and 20 against the wrong headings); the body's numbering is followed.

**Checks:** one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. It is an institutional Act,
so this row takes the rules with decision content: the Authority's size (s 5),
immunity from suit (s 11), borrowing (s 12), withdrawals from the Future Energy Fund
(s 19A), the cost-recovery rate for energy initiatives (s 19B), the offences and
penalties (ss 20, 27, 28, 29), composition (s 30), what needs the Minister's approval
(ss 12, 19A(3), 30(2), 31, Second Schedule), and membership, quorum, voting and
delegation (First Schedule). The functions in s 6, Ministerial directions (s 8),
staffing (s 9), financial housekeeping (ss 13 to 18), the Fund's composition (s 19)
and the 2001 transfer from the Public Utilities Board (Part 4) are not encoded.

## What the Act turns out to say

### 1. The Fund for low-carbon energy can pay for gas turbines and diesel generators

s 19A(6) defines an "energy supply security project" as one "necessitated by any
low-carbon energy project", and lists among its back-up assets "fast-response
generators (including diesel generators and gas engines)" and "combined-cycle gas
turbines". The Future Energy Fund may be withdrawn for such projects (s 19A(1)(a)).
The test is the necessity link, not the fuel. The coal-fired station in the cases is
a constructed example outside the list, not something the Act names. Asserted.

### 2. Anyone in the energy chain, consumers included, can be made to pay for an initiative they do not benefit from

s 19B (in force 1 July 2025) lets regulations impose a rate to recover the cost of an
energy initiative for security of supply, market improvement or lower carbon
emissions. It may be laid on electricity, gas and district cooling licensees, persons
exempted from those licences, and "any consumer of any energy utilities", "whether or
not the person derives any direct or immediate benefit"; s 19B(5) lets a rate for one
utility fall on payers in another. If the rate over-recovers, the Authority "may
retain the excess" for other initiatives (s 19B(8)). That a payer outside the four
classes cannot be charged is an inference from the list. Asserted.

### 3. The Fund has hard exclusions: no land reclamation, no fuel, no running costs

s 19A(4): the moneys "must not be withdrawn" for Government land reclamation, for
fuel used to generate electricity, or for the recurrent costs of a project. A project
begun before the appointed date qualifies only if its assets could not yet serve
anyone before that date (s 19A(2)), and no Fund investment may be written off without
the Minister's prior approval (s 19A(3)). Which purposes s 19A(2) reaches is an
inference (the project-related ones). Asserted.

### 4. A quorum is a third, rounded up in effect, and never fewer than 3

First Schedule para 11(1): the quorum is "one-third of the total number of members in
office or 3 members, whichever is the higher". With 10 members in office, 3 present
is not enough (a third is 3.33). Ties go to the chair's casting vote, cast in
addition to the chair's own vote (para 11(3)). Asserted.

### 5. The Authority can borrow from the Government freely; from anyone else, only with the Minister

s 12(3): loans may be raised "from the Government" or, "with the approval of the
Minister, from another source, whether in or outside Singapore"; an instrument other
than a mortgage, overdraft, charge, debenture or bond also needs the Minister's
approval (s 12(2)(c)). Borrowing and the levying of dues and rates are the two powers
the Authority may not delegate (First Schedule para 14(2), (3)). Selling immovable
property also needs the Minister (Second Schedule para 2); acquiring it does not
(para 1A). Asserted.

### 6. The offences are modest, and compounding is capped at $3,000

Using the Authority's symbol or a confusing imitation: $10,000 or 12 months, plus
$250 a day after conviction (s 20(2)). Obstructing an officer, wilfully misstating or
refusing information without lawful excuse, or ignoring a lawful demand: $5,000 or 12
months (s 27(2)). Disclosure by a present or former member, officer, employee, agent
or committee member: $5,000 or 12 months (s 28). Officers who authorise, consent or
connive share the body's guilt (s 29). Composition requires the offence to be
prescribed and the sum to be at most $3,000 (s 30). Asserted.

### 7. The Authority's statutory functions cannot be enforced in court

s 6(3): nothing in s 6 imposes "any form of duty or liability enforceable by
proceedings before any court". Not asserted.

### 8. A member serving a sentence of exactly six months is not disqualified

First Schedule para 8(b) disqualifies a person "sentenced to imprisonment for a term
exceeding 6 months" without a free pardon; six months is not enough. Missing 3
consecutive meetings vacates the office unless the Authority finds sufficient cause
(para 6(b)). Asserted.

## What would need doing before this is worth anything

- The regulations under ss 19B, 30 and 31 (which rates exist, which offences are
  compoundable) were not retrieved.
- The appointed date for s 19A(2) and any Gazette orders under s 19A(7) on
  low-carbon fuels and recurrent costs were not retrieved.
- The 5 citing Acts were not read for how they use this Act.
- No case law was searched.
