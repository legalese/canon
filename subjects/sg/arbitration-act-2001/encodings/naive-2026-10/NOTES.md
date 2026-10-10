# Arbitration Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 5
of 2025 (in force 9 March 2025) shown.

**Checks:** one case file, 108 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**12 of the 527 Singapore Acts** deposited here cite it. This row takes what a party
or its lawyer meets: when the Act applies (s 3), the writing requirement (s 4), the
stay of court proceedings (s 6), the default tribunal (ss 12, 13), challenges to an
arbitrator (ss 14, 15), immunity (ss 20, 59), jurisdiction pleas (s 21), reasons and
costs (ss 38, 39), correction of awards (s 43), enforcement (s 46), and the two court
routes against an award: setting aside (ss 47, 48) and appeal on a question of law
(ss 49, 50). The conduct of proceedings, extensions of time, limitation, interest,
fees, preliminary points of law, the intellectual property Part, privacy and
mediation are not encoded.

## What the Act turns out to say

### 1. Agreeing to an award without reasons quietly gives up the appeal on law

s 38(2) lets the parties agree that no reasons be stated. s 49(2) then says "an
agreement to dispense with reasons for the arbitral tribunal's award is to be treated
as an agreement to exclude the jurisdiction of the Court" on an appeal on a question of
law. A procedural choice doubles as a waiver. Asserted.

### 2. Two routes against an award, with different clocks and different starting points

Setting aside (s 48(2)): 3 months from the date the applicant **received** the award,
or from disposal of a s 43 correction request. Appeal on law (s 50(3)): 28 days from
the **date of the award**, or from notification of an arbitral review result. The
appeal also needs every other party's agreement or the Court's permission (s 49(3))
and exhaustion of arbitral review and s 43 recourse first (s 50(2)). Asserted. How the
3 months is reckoned (same day of the month, three months on) is an inference; the
Act does not say, and month-end cases are not modelled.

### 3. A wrong answer is not a ground for setting aside

The s 48(1) list is about capacity, validity, notice, scope, composition, fraud,
natural justice, arbitrability and public policy. Error of law or fact is not on it,
and s 47 removes any other jurisdiction to "confirm, vary, set aside or remit" an
award. A legal error goes by s 49 or not at all; a factual error has no route in this
Act. Arbitrability and public policy are the two grounds the Court "finds" (s
48(1)(b)) rather than ones the applicant must prove. Asserted.

### 4. Permission to appeal needs an obviously wrong decision, or public importance plus serious doubt

s 49(5): the question must substantially affect a party's rights, have been put to the
tribunal, be just and proper for the Court, and the decision must be "obviously wrong"
or, if of "general public importance", "at least open to serious doubt". A doubtful
decision of purely private importance does not qualify. Asserted.

### 5. The arbitrator's immunity has no bad-faith exception in its words; the institution's does

s 20 protects an arbitrator against negligence and any mistake of law, fact or
procedure, and says nothing of bad faith. s 59(1) protects the appointing authority
and institutions "unless the act or omission is shown to have been in bad faith", and
(2) never for merely having appointed the arbitrator. That s 20 leaves deliberate
dishonesty unprotected is an inference from its silence. Asserted.

### 6. Smaller rules a party trips over

- No number agreed means **one** arbitrator (s 12(2)); with three and no agreed
  procedure, a party's failure to appoint within 30 days of the request lets the
  appointing authority step in (s 13(4)). Asserted.
- A party who helped appoint an arbitrator may challenge only on grounds learned
  after the appointment (s 14(4)); a rejected challenge goes to the Court within 30
  days, with no appeal (s 15(4), (5)). Asserted.
- A stay must be sought after the notice of intention and before any pleading on the
  merits or other step (s 6(1)); a stayed case idle for 2 years may be discontinued (s
  6(4)). Asserted.
- A clause making a party pay its own costs "in any event" is void unless it is in a
  submission of an already-arisen dispute (s 39(2), (3)). Asserted.
- An interpretation under s 43 needs the other parties' agreement; a correction does
  not. Asserted.
- s 46(3) lets an award be enforced with permission whatever the seat, although s 3
  confines the rest of the Act to Singapore-seated arbitrations outside Part 2 of the
  International Arbitration Act 1994. Asserted.

## What would need doing before this is worth anything

- The day-counting in the 28-, 30- and 14-day periods (days elapsed after the start
  date, at most N) matches s 61(3): the period "begins immediately after that date".
  s 61 lets the parties agree another method, which is not modelled. The 3-month
  reckoning in s 48(2) is still an inference. (The arrangement in the deposit numbers
  this section 60; the body numbers it 61.)
- The Rules of Court and the International Arbitration Act 1994 (which decides when
  this Act does not apply) were not consulted.
- "May" in ss 6, 13 and 50(7) is encoded as permission only; the court's discretion
  is not modelled.
- No case law was searched, including on what counts as "taking any other step" (s 6)
  or on public policy (s 48).
