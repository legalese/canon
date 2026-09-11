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
part-3-subpart-1-regulator.l4    cll 20-23     scaffold
part-3-subpart-2-enforcement.l4  cll 24-33     scaffold
part-3-subpart-3-remedies.l4     cll 34-56     scaffold
part-3-subpart-4-offences.l4     cll 57-60     scaffold
part-3-subpart-5-other.l4        cll 61-64     scaffold
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

## 3. Open questions -- the LQA probes

These are why the subject exists. Probe 1 is encoded and machine-evaluated in
`part-1-preliminary.l4`; the rest are stated here and become cases as their modules land.

1. **The excluded-service carve-out attaches only to limb (a) of cl 5(1).** An internet
   service that solely or primarily enables healthcare or education is an "excluded service"
   and so falls outside cl 5(1)(a). But cl 5(1)(b) -- the AI companion limb -- carries no
   carve-out and requires no specified feature. A therapy or tutoring chatbot therefore
   appears to fall out of (a) and straight back in under (b). `#ASSERT` in
   `part-1-preliminary.l4` confirms this on the drafted text: limb (a) FALSE, limb (b) TRUE.
   Whether that is intended is a question for the drafter. If intended, it is under-signposted;
   if not, it is a gap.

2. **Does cl 34(3)(a) to (i) partition cleanly across the three tiers?** cll 45 to 47 route
   paragraphs (a)-(c) to Tier 1, (d)-(g) to Tier 2, and (h)-(i) to Tier 3. The partition
   looks total and disjoint on its face; encoding it makes that checkable, and keeps it
   checkable after amendment, which is when such partitions break.

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

4. **Three routes into scope, one route out.** Regulations under cl 62 add platforms
   (cl 5(1)(c)), the regulator designates operators (cl 7), and exemption orders under cl 61
   remove obligations. Whether an exemption can reach a platform brought in by regulation is
   worth testing once cll 61-62 are encoded.

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

## 4. What is deliberately not encoded

Nothing yet, beyond the scaffold boundary. Candidates for exclusion once the operative
modules land: cll 20-23 regulator functions and information-gathering (administrative rather
than determinative), cll 41-43 procedural requirements for restriction orders, and cll 49-53
injunction machinery and civil procedure.

## 5. Provenance

Source XML is the PCO drafting-system source, not a scrape: 134 provisions, 102,551
characters of extracted text, `bill.no="339"`, `stage="1"`, `year="2026"`. Fetched by
appending `.xml` to the document URL, which the NZ Legislation website serves without an API
key. Bulk retrieval would need a key from contact@pco.govt.nz.
