# Trade Disputes Act 1941 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
15/9/2026"), deposited as `TDA1941.txt`. The cover says it incorporates amendments up
to 1 December 2021; the text annotates later amendments by Act 30 of 2021 (wef
2 November 2022), Act 30 of 2024 (the platform-worker changes, wef 1 January 2025) and
Act 10 of 2025 (s 15(4A), wef 15 September 2026).

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**, not by citation count: it decides when an
employee, or since 1 January 2025 a platform worker such as a delivery rider, may
lawfully strike, picket or refuse to strike, and what happens if they do. The Act is
short (15 sections), so the row covers ss 2 to 15. Not encoded: the Platform Workers
Act 2024 definitions that s 2 borrows (not read), and the Industrial Relations Act 1960
machinery that decides when an Industrial Arbitration Court "has cognizance" of a
dispute — that is taken as a given fact.

## What the Act turns out to say

### 1. A strike over a dispute already before the Industrial Arbitration Court is illegal

s 3(1)(b): industrial action is illegal if "it is in furtherance of a trade dispute or
work dispute of which an Industrial Arbitration Court has cognizance". A genuine
dispute in the workers' own trade is no defence once the Court has it. The same rule
binds employers' lockouts (s 3(2)(b)). Asserted.

### 2. Any other object makes the action illegal, even alongside a genuine dispute

s 3(1)(a) makes it illegal if "it has **any object other than** the furtherance of" a
dispute in the participants' own trade or platform service. A sympathy strike, or one
with a political aim, fails; so does one "designed or calculated to coerce the
Government either directly or by inflicting hardship on the community" (s 3(1)(c)).
Asserted.

### 3. A go-slow is industrial action; a lone worker is not

s 2 defines industrial action to include any combined act or omission causing "any
limitation or restriction on, or delay in" the performance of duties — a go-slow or
work-to-rule counts, not only a walk-out. It must be by "a body of persons ... acting
in combination or under a common understanding", so one person stopping work alone is
not industrial action. Asserted.

### 4. Inciting someone bound by an award to strike is an offence even if the strike is legal

s 6 has two limbs: inciting others into an **illegal** action or lockout, or inciting
"a person bound by an award to take part in ... **any** industrial action". The second
limb does not require illegality. Maximum $5,000 or 12 months or both. Asserted.

### 5. Retaliation against a member who refused an illegal strike is a union offence

s 8(1) bars expulsion, fines, loss of benefits or any disadvantage for refusing to take
part in an illegal industrial action or lockout. Under s 8(2) a **registered** trade
union or registered platform work association that even "declares that it ... intends
to expel" such a member commits an offence (fine up to $5,000, no imprisonment). The
protection is for refusing an illegal action; the Act says nothing about refusing a
lawful one. Asserted.

### 6. Peaceful picketing is lawful, even at a person's home

s 10 protects attendance "at or near a house or place where a person resides or works"
in contemplation or furtherance of a trade or work dispute, merely to inform or
peacefully persuade. Attendance in numbers or manner calculated to intimidate, obstruct
the approach or exit, or lead to a breach of the peace is "deemed to constitute an
offence under section 9(d)" ($2,000 or 3 months). Asserted.

### 7. Penalties are modest, but every offence is arrestable and non-bailable

Maximums: illegal industrial action $2,000 / 6 months (s 5(1)); illegal lockout $5,000 /
6 months (s 5(2)); instigation and funding $5,000 / 12 months (ss 6, 7); intimidation
and dangerous breach of contract $2,000 / 3 months (ss 9, 11). Yet s 12 makes **every**
offence "arrestable and non-bailable". Once charged under s 5, 6 or 7, further
proceedings need the Public Prosecutor's consent unless the Public Prosecutor brought
them (s 13), and those offences may go to the High Court (s 14). Asserted.

### 8. The criminal conspiracy shield is narrower than the civil one

s 15(1) shields a combination from criminal conspiracy only for a trade dispute
"**between employers and employees**" (or platform operators and workers), and only if
the act done by one person would not be imprisonable (s 15(5)). s 15(2), the civil
shield, covers any "trade dispute or work dispute" — which s 2 extends to disputes
among employees and among employers. So a combination in an employee-versus-employee
dispute gets the civil shield but not the criminal one, on a literal reading. Asserted.

### 9. Intimidation of family is limited to "wife or children"

s 9(a) covers violence or intimidation of the person "or his wife or children", though
the s 2 definition of "intimidate" reaches "any member of his family or ... any of his
dependants". Following someone once, or with others in an orderly way, is not a listed
means; "persistently" following, or following "with 2 or more persons in a disorderly
manner", is. Asserted for the listed means; the wife/children point is a reading, not
tested separately.

## What would need doing before this is worth anything

- The Platform Workers Act 2024 definitions (platform service, operator, worker,
  registered platform work association, platform lockout) were not read.
- When an Industrial Arbitration Court "has cognizance" under the Industrial Relations
  Act 1960 is taken as an input; it decides finding 1 in practice.
- No case law was searched on "any object other than", "calculated to", or the s 15
  shields.
- Other legislation restricting strikes (for example in essential services) was not
  looked at; this row says nothing about it.
