# Trade Unions Act 1940 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/TUA1940.txt`. The deposit's cover says it incorporates
amendments up to 1 December 2021; the latest amendment annotated in the body is Act 30
of 2024 (in force 1 January 2025), which introduced "combined federations" of trade
unions and platform work associations.

**Checks:** one case file, 57 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**8 of the 527 Singapore Acts** deposited here cite it. This row takes what a union,
its members and its officers actually meet: the deadline to register and what follows
from missing it (ss 8, 17, 19), immunity from suit in trade disputes (s 22), strikes
(s 27, with s 39(2)), membership (s 28), officers and trustees (ss 30, 43), the use and
investment of funds (ss 47-49), and a few deadlines and penalties (ss 37, 51(4), 59).
Grounds for refusing or cancelling registration, account freezing, winding up, liability
in tort and contract, amalgamation, rules, notifications, property, returns and the
residual offences are not encoded.

## What the Act turns out to say

### 1. A strike needs a majority of the members affected, not of those who vote

s 27(1) forbids a union to call a strike "without obtaining the consent, by secret
ballot, of the majority of the members so affected". Every other union decision uses
"requisite consent" (s 2), which is a majority of the members *voting*. So 40 yes votes
out of 45 cast carries an ordinary decision but does not carry a strike among 100
affected members, and exactly half in favour fails. Asserted.

### 2. A union that ignores its own rules can still strike; its members cannot

s 27(1) asks the union only for the ballot. But s 27(4)(b) makes it an offence for a
*member* to take part in a strike "taken in contravention of the rules or by-laws of
the trade union". On the text, a balloted strike against the rules is lawful for the
union and an offence for each member who joins it. Asserted.

### 3. Represented executives are shut out of strikes entirely

Where most members are non-executive employees, executives represented under s 30A of
the Industrial Relations Act 1960 do not vote and are not counted (ss 27(16), 39(2)): 41
yes votes out of 100 affected, 20 of them such executives, carries the ballot (41 of 80);
the same vote in a mostly executive union fails. A represented executive may not take
part in *any* strike the union takes (s 27(5)), and s 27(7) lifts only the bars in
(2) and (6), not (5). The union may not strike over a dispute between those executives
and their employer (s 27(2)) unless it is recognised by the employer under Part 3 of that
Act (s 27(7)). How (7) is meant to work is not clear on its face; this row reads it as
lifting the (2) bar. Asserted (the ballot arithmetic as the number of members whose consent counts).

### 4. Combined federations cannot strike, and lose the trade-dispute immunity

Since Act 30 of 2024, a combined federation "shall not commence, promote, organise or
finance any strike" (s 27(2A)), however its members vote, and s 22's immunity from civil
suit for inducing breach of contract or interfering with trade "does not apply" to it
(s 22(2)). Read literally, no member offence in s 27(4) or (9) is tied to (2A): a member
taking part in a balloted combined-federation strike commits none of the s 27 member
offences. That is a literal reading, not a conclusion. Asserted.

### 5. One month to register, and missing it makes the union unlawful

A union must apply within one month of being established (s 8(1)), the date "any
workmen or employers agree" to form it (s 8(3)). The Registrar may extend, but not
"so as to exceed a period of 6 months in the aggregate" (s 8(2)); this row reads that
as a 6-month outside limit, an inference. A union that does not apply in due time, or
whose registration is refused or cancelled, "shall be deemed to be an unlawful
association" and "shall be dissolved" (s 19). Appeal to the Minister lies within 30 days
(s 17), and his decision "shall not be called in question in any court" (s 18(3)).
Asserted.

### 6. A reformed convict can be an officer; a bankrupt cannot, ever

s 30(1) bars undischarged bankrupts and anyone convicted of criminal breach of trust,
extortion or criminal intimidation from acting as an officer; s 30(2) restores a person
"so convicted" whom the Minister thinks reformed, but offers the bankrupt nothing.
Trustees have a different list: bankrupts (no exception), fraud or dishonesty
convictions (unless the Minister approves), and, without prior approval, a president,
chairman, treasurer or secretary, or a non-citizen (s 43). So the union's treasurer may
be an officer but not, without approval, a trustee. The fixture treats a criminal breach
of trust conviction as also one "involving fraud or dishonesty"; that is an inference.
One approval flag stands in for the Minister's separate approvals in ss 30(3), 43(3) and
43(4). Asserted.

### 7. Sixteen-year-olds may join; the executive age rule skips 17-year-olds

A person "above the age of 16 years" may be a member unless the rules say otherwise
(s 28(1)); Government employees may not join any union unless the President exempts them
(s 28(3), (4)). A member "under the age of 21 years, but above the age of 18 years" needs
the Minister's written approval to sit on the executive or be a trustee (s 28(2)). Read
literally, that leaves a 17-year-old member uncaught by (2). Whether a minor can hold
such office is not answered by this section. Asserted.

### 8. Union money cannot pay fines or politics

Funds may be spent "only" on the seven objects in s 47(1); never on "any fine or
penalty imposed upon any person" by a court (s 48) or on a political party or purpose
(s 49(1)(a)). Investment is limited to trustee investments, bank deposits, shares in
union-established co-operatives and Minister-approved Singapore Labour Foundation
schemes (s 49(1)(b)): listed shares are out. Asserted.

### 9. Small numbers

Two-thirds of a union's officers must be engaged in its trade (s 30(4)). The same
auditor for more than 5 continuous years needs the Minister's approval (s 51(4)).
Operating without a notified registered office costs up to $50 a day, and every officer
is liable to the same (s 37). Strike fines top out at $3,000 for the union, its executive
and inciters and $2,000 for members (s 27); no imprisonment is provided. The Registrar may
compound prescribed offences for no more than $200 (s 59), and every prosecution needs the
Public Prosecutor (s 60). Asserted in part: the union's own $3,000 maximum and s 60 are not.

## What would need doing before this is worth anything

- The Trade Unions Regulations (forms, fees, the prescribed date for annual returns and
  which offences are compoundable) were not retrieved.
- s 27(7)'s interaction with (2), (5) and (6), and the Industrial Relations Act 1960
  provisions it relies on (s 30A, Part 3), were not read.
- Minors aged 16 to 18 in office, and whether "above the age of 18" means past the 18th
  birthday, need a reading from case law or practice.
- The grounds for refusing and cancelling registration (ss 10, 14, 15) and the Platform
  Workers Act 2024 definitions they now depend on are not encoded.
