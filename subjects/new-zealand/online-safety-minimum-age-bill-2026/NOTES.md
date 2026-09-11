# Online Safety (Minimum Age and Child Safety Risk Assessment) Bill -- encoding notes

This subject's idiosyncrasies, in prose, for humans. No script reads this file.

---

## 1. What this subject is

An L4 encoding of the **Online Safety (Minimum Age and Child Safety Risk Assessment) Bill**
(NZ), 2026 No 339-1, as introduced on 24 August 2026. The Bill bans under-16s from
age-restricted platforms, imposes child safety risk assessment duties on operators, and
creates a regulator with enforcement powers backed by three tiers of pecuniary penalty.

The purpose here is **legislative quality assurance**, not a decision service. The
deliverable is a defect list: gaps, overlaps and unreachable states in the Bill as drafted,
each demonstrated by a machine-evaluated case rather than asserted in prose.

Modules, in dependency order:

```
types.l4                         the nouns: the cl 5 and cl 6-8 fact records, the cl 34(3) act enum, tiers
part-1-preliminary.l4            cll 1-3, 5-10 encoded; cl 4 definitions taken as facts
part-2-duties.l4                 cll 11-19 encoded
part-3-subpart-1-regulator.l4    cll 20-23 encoded
part-3-subpart-2-enforcement.l4  cll 24-33 encoded
part-3-subpart-3-remedies.l4     cll 34-56 encoded in part (see section 4)
part-3-subpart-4-offences.l4     cll 57-60 encoded
part-3-subpart-5-other.l4        cll 61-64 encoded
schedule-1-transitional.l4       Sch 1         scaffold
registers/source-bundle/         LMS1592864 .xml / .txt / .pdf as retrieved 11 Sep 2026
```

## 2. Divergences from the subject-sidecar class

Recorded here rather than by forking the template, per `subjects/README.md`.

1. **The subject is a Bill, not law in force.** Every other subject in this corpus encodes
   an Act or Regulation currently in force. Consequences:
   - `subject.json` has no field for parliamentary stage, so the version identity lives in
     `citation` ("2026 No 339-1") with `bill_no` and `bill_stage` added as non-class keys.
     If Bills become a recurring subject type, these belong in the class.
   - There is no as-at date and no law-time axis. `EVAL UNDER RULES EFFECTIVE AT` is not
     used and should not be: the Bill has no dated arms, only versions -1, -2, -3.
   - The source will change. When the Bill is reported back from select committee as -2,
     the correct move is a new `registers/source-bundle` entry and a minor version bump,
     with the probes in section 3 re-run against the new text. That re-run is the point.

2. **No `cases/` directory.** Following the WA Residential Tenancies Act 1987 subject,
   `#EVAL` / `#ASSERT` directives sit inline in the module they test, and the fixtures they
   run against sit beside them. Expected values are machine-evaluated, never hand-typed.

3. **No `projections/`, `report/` or `gates/` yet.** `status` is `draft`: no claim of
   fidelity is made, and no human gate has been sought.

4. **`SOURCE-LICENSE.md` grants nothing**, because there is nothing to grant -- see that
   file. This is the corpus's first no-copyright source.

5. **`registers/incident-register.xlsx` is a spreadsheet, not markdown or JSON.** Every other
   register in the corpus is `.md` (coverage, verification) or `.json` (fork,
   external-modification, source-bundle), and the class expects registers to validate against
   the l4-ide schemas. This one is a working defect tracker, kept in the form the reviewer
   asked for so that rows can be filtered, sorted and assigned. It carries three sheets: a
   terminology and method note, the incidents themselves, and a coverage summary whose counts
   are formulas over the incidents sheet. Section 3 below remains the prose record; the
   spreadsheet is the tracked view of it, and the two must be updated together.

## 3. Open questions -- the LQA probes

These are why the subject exists.

**Terminology.** An *incident* is a defect, gap or open question in the Bill as drafted. A
*probe* is a machine-evaluated test in the encoding that demonstrates one: the probe is the
evidence, the incident is the finding. The numbered list below is the prose record, and each
entry maps to a row in `registers/incident-register.xlsx` (OS-001 to OS-010). Where an entry
is marked *Encoded*, a directive in the named module produces the stated result under
`l4 run`; where it is not, the finding follows from reading provisions together and has not
yet been reduced to a directive, usually because its module is still a scaffold.

1. **The excluded-service carve-out attaches only to limb (a) of cl 5(1).** An internet
   service that solely or primarily enables healthcare or education is an "excluded service"
   and so falls outside cl 5(1)(a). But cl 5(1)(b) -- the AI companion limb -- carries no
   carve-out and requires no specified feature. A therapy or tutoring chatbot therefore
   appears to fall out of (a) and straight back in under (b). `#ASSERT` in
   `part-1-preliminary.l4` confirms this on the drafted text: limb (a) FALSE, limb (b) TRUE.
   Whether that is intended is a question for the drafter. If intended, it is under-signposted;
   if not, it is a gap.

2. **Does cl 34(3)(a) to (i) partition cleanly across the three tiers? Yes -- no defect.**
   *Encoded and machine-evaluated in `part-3-subpart-3-remedies.l4`.* cll 45 to 47 route
   paragraphs (a)-(c) to Tier 1, (d)-(g) to Tier 2, and (h)-(i) to Tier 3. `the tier for` is
   a total function over the `specified liability act` enum, so an unrouted act is a type
   error rather than a silent gap, and nine `#ASSERT` directives pin each act to the tier the
   Bill assigns it. All nine hold. This is a negative result and is recorded as one: the
   partition is total and disjoint on the text as drafted. Its value is prospective -- if a
   select committee adds a paragraph to cl 34(3) without amending cll 45 to 47, the encoding
   fails to typecheck rather than quietly leaving the new act unpenalised.

3. **A cl 6(1) operator stops being the operator when someone else is designated.**
   *Encoded and machine-evaluated in `part-1-preliminary.l4`.* cl 6(2) makes a designated
   person "the only operator ... while the designation is in place". On the `a displaced
   controller` fixture -- a company that manages and controls the platform in New Zealand,
   with its overseas parent designated under cl 7 -- `the person is an operator under
   section 6(1)` evaluates TRUE while `the person is the operator of the platform`
   evaluates FALSE. Every Part 2 duty attaches to "an operator of an age-restricted
   platform", so the displaced controller owes none while the designation stands. Two
   questions follow, neither answered by the text: what happens to duties that accrued
   before the designation, and whether the regulator can designate a person who is neither
   a cl 6(1) operator nor an interconnected body corporate of one (cl 7(1) says it cannot,
   so a platform whose controller is outside both limbs cannot be designated at all).

4. **Three routes into scope, one route out -- no defect.** *Encoded in
   `part-3-subpart-5-other.l4`.* cl 61(1)(a) exempts "an operator of an age-restricted
   platform", and a service specified by cl 62(1)(a) regulations is an age-restricted platform
   by force of cl 5(1)(c). The exemption route therefore reaches a regulation-added platform,
   and the two do not conflict. Encoding cl 62 did surface a distinction worth keeping in
   view: each limb of cl 62(1) carries its own satisfaction test -- cl 62(4) for limbs (a) and
   (b), cl 62(6) for limb (c) -- and the tests are not interchangeable. A `#ASSERT` shows a
   limb (c) recommendation failing when only the cl 62(4) test is satisfied.

5. **cl 11(2)-(3) define what does *not* discharge the duty** (manual age entry; evidence-of-age
   documents; a digital identity service; both together) without stating what does.
   *Encoded in `part-2-duties.l4`.* The three disqualifiers are modelled as
   `the steps taken cannot satisfy the duty`, and what survives them is a single irreducible
   field, `the steps taken are otherwise reasonable`. That is the honest shape: an operator
   reading the Bill can learn with certainty only which methods will fail. The
   `identity documents only` fixture is the cl 11(3)(c) case -- an operator that does both
   formal identity checks and nothing else -- and evaluates FALSE.

6. **cl 16(5) imposes a duty with no time for performance, and Tier 2 liability for
   breaching it.** cl 15(1) gives 12 months (or an earlier notified date). cl 17(3) requires
   a copy as soon as practicable after the assessment and before the change is made. cl 16(5)
   says only that "on completion of a review, the operator must provide the regulator with a
   copy" -- no period, no notified date, no "as soon as practicable". Yet cl 34(3)(f) makes
   failure to provide "in accordance with section 15(1), 16(5), 17(3), or 19(3)(b)" a
   specified liability act, and cl 46 routes cl 34(3)(f) to Tier 2: up to $250,000 for an
   individual, or for anyone else the greater of $12 million and 3% of relevant global
   turnover. A penalty of that size for a duty whose time for performance is unstated is
   worth putting to the drafter. Contrast cl 19(3)(b), which requires the regulator's notice
   to specify the date -- the same drafting problem solved two clauses later.

7. **The only duty on the regulator carries no consequence.** cl 13(3) requires the regulator
   to notify the Privacy Commissioner before applying to the High Court for a remedy in
   respect of a cl 12(1) contravention. Every one of the nine specified liability acts in
   cl 34(3) is an operator failure, and the four offences in cll 57 to 60 do not reach it
   either, so nothing in the Act attaches to a breach of cl 13(3). Judicial review is the
   only route. This may be deliberate -- it usually is -- but it is the one asymmetry in a
   Part otherwise built on enforceable duties, and the encoding makes it visible by giving
   the regulator its own `duty actor` arm.

8. **cl 17(4) is inclusive, so the trigger for the change-related duty is open-ended.**
   "significant change ... includes a significant change to (a) the design, features, or
   functionality of the platform: (b) the terms of use". The encoding follows the text:
   the two limbs are sufficient, not necessary, so a change outside both may still be
   significant and still trigger cl 17(1). An operator cannot determine in advance whether a
   given change is caught.

9. **Breach of an enforceable undertaking is not a specified liability act.** cl 29(2)
   provides that an operator "must not breach an undertaking given by that operator that is
   in force". None of the nine acts in cl 34(3) is that breach, so no pecuniary penalty is
   available for it under cll 44 to 47. What is available is a cl 30(2) order directing the
   operator to comply with the undertaking or discharging it, plus costs under cl 30(3), and
   -- where the underlying act is still ongoing -- a service restriction order, because
   cl 35(2)(c)(i)(B) makes breach of an accepted undertaking a route to one. The gap is
   narrower than it first appears: cl 29(3)(a) bars proceedings only while the undertaking is
   in force AND unbreached, so breach lifts the bar and the underlying act can still be
   pursued. What cannot be penalised is the breach itself. On the drafted text the sanction
   for breaking a statutory promise to the regulator is an order to keep it. `#ASSERT` in
   `part-3-subpart-2-enforcement.l4` shows the bar lifting on breach.

10. **The enforcement measure with the least process is the one with immediate public
    effect.** cl 24(2) requires the regulator to give public notice of a warning as soon as
    reasonably practicable, and nothing in cl 24 requires prior notice to the operator, a
    statement of the case, or an opportunity to be heard. By contrast cl 25(3) requires at
    least 5 working days' written notice plus an opportunity to make written submissions and
    be heard before the regulator may require the operator to *republish* that same warning,
    and cl 33 requires at least 10 working days and the same hearing right before a
    corrective notice. So public naming attracts no process, republishing the naming attracts
    5 days and a hearing, and requiring remedial steps attracts 10 days and a hearing. The
    order of intrusion and the order of procedural protection do not match.

11. **The only imprisonable offence can be switched off by committing a lesser civil breach.**
    cl 57 makes it an offence to confirm the accuracy of a risk assessment knowing it to be
    false or misleading, but the offence is committed only by "an individual designated under
    section 18". If the operator never designates anyone, no individual is capable of
    committing it. Failing to designate is itself a breach -- cl 34(3)(g), routed by cl 46 to
    Tier 2 -- but it is a civil penalty, and it extinguishes the criminal exposure of every
    officer of the operator. `#ASSERT` in `part-3-subpart-4-offences.l4` runs identical
    conduct through both fixtures: designated, offence committed; undesignated, no offence.
    cl 57 is the only provision in the Bill carrying imprisonment alongside a fine on an
    individual for conduct about risk assessments.

12. **cl 61 permits exemption from any or all requirements of the Act by Order in Council.**
    cl 61(1)(a) is not limited to particular duties: an exemption may relieve a named
    operator of "any or all requirements under this Act", the cl 11 minimum age duty
    included. The controls are procedural (cl 61(2)) plus a single satisfaction test
    (cl 61(3)) that the benefits outweigh the risk to children. There is no limit on
    duration, no requirement to publish reasons beyond the secondary-legislation publication
    rules in cl 61(4), and no parliamentary confirmation requirement on the face of the Bill.
    Worth raising alongside the Regulatory Standards Act 2025 material the Department of
    Internal Affairs filed with the Bill.

13. **cl 11(4) creates a prohibition with no consequence, defined by the weakest
    regulation-making power.** cl 11(4) forbids an operator to collect personal information
    of a class specified in cl 63 regulations for the purpose of complying with the minimum
    age duty. Two observations. First, cl 34(3)(a) reaches only a failure "to take reasonable
    steps to prevent a New Zealand person under the age of 16 years from having an account
    ... in accordance with section 11" -- that is cl 11(1). Breach of the cl 11(4) prohibition
    is not a specified liability act, is not an offence under cll 57 to 60, and so attracts
    nothing. Second, the class of forbidden information is set by regulations under cl 63,
    which is the only regulation-making power in the Bill carrying no satisfaction test at
    all: cl 63(2) requires the Minister to seek the regulator's advice and consult, and
    nothing more. A substantive privacy prohibition is created by the least-constrained
    instrument and enforced by none. `part-2-duties.l4` decides the contravention; nothing
    consumes it.

## 4. What is deliberately not encoded

Within Subpart 3, the following are left out because they state no test an encoding can
decide. Each is marked in the module with a heading and a reason, so a reader can see that
the omission is a decision rather than an oversight.

| Provision | Why not encoded |
| --- | --- |
| cll 36, 39 | Interim orders, granted where the court is "of the opinion" that it is desirable |
| cll 37, 40 | Prescribe what an order must contain; no condition on the outcome |
| cl 41(1) | Requires the court to consider named persons' rights without conditioning the result on them |
| cl 41(2) | A notification duty on the regulator, owed to the Minister |
| cl 42 | Renewal procedure |
| cl 43 | Appeal to the Court of Appeal on a question of law |
| cl 48 | Matters the court must have regard to in fixing a penalty within the maximum; constrains reasoning, not outcome |
| cll 49-51 | Injunction powers turning on the court's satisfaction or opinion |
| cl 52 | Removes the requirement for an undertaking as to damages |
| cl 53 | Applies the ordinary civil rules and standard of proof |

Still to be scoped once their modules land: cll 20-23 regulator functions and
information-gathering, which are administrative rather than determinative.

## 5. Provenance

Source XML is the PCO drafting-system source, not a scrape: 134 provisions, 102,551
characters of extracted text, `bill.no="339"`, `stage="1"`, `year="2026"`. Fetched by
appending `.xml` to the document URL, which the NZ Legislation website serves without an API
key. Bulk retrieval would need a key from contact@pco.govt.nz.
