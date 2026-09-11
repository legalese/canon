# Online Safety Bill — conversion report

**Date:** 2026-09-11
**Subject:** `new-zealand/online-safety-minimum-age-bill-2026`
**Source:** New Zealand Legislation, `LMS1592864`, Online Safety (Minimum Age and Child Safety
Risk Assessment) Bill, 2026 No 339-1, as introduced 24 August 2026. Deposited at
`registers/source-bundle/` as `.xml`, `.txt` and `.pdf`.
**Encoding version:** 0.9.0
**Status declared:** `draft` — the encoding exists and is machine-checked; no claim of fidelity
is made and no human gate has been granted.

---

## 1. What was asked for, and what this is

Every other subject in this corpus encodes law in force, and the deliverable is a decision
service: a model that answers what the law requires of a given set of facts. This subject is a
**Bill**, and the deliverable is different. It is a **legislative quality assurance** pass:
the encoding exists to find gaps, overlaps and unreachable states in the text as drafted, and
the machine-evaluated cases are the product rather than the evidence.

That difference shapes everything below. The `#ASSERT` directives are not regression tests
protecting a service; they are the demonstrations that a finding is real. Where an ordinary
subject would model around an oddity to keep the service useful, this one encodes the oddity
faithfully and then points at it.

The Bill was chosen from the 102 Bills before the House on 11 September 2026 on two grounds:
it is the most heavily covered in the media, including international coverage, and its
operative content has hard edges — a Boolean scope test with a carve-out list, three penalty
tiers over a nine-member partition, explicit consistency constraints in cll 54 to 56 — which
is the shape L4 can actually check. The RMA replacement Bills have more coverage domestically
but are purposive and evaluative, and an encoding of them would mostly restate discretion.

## 2. Method

Nine modules, named after the Bill's own Parts and subparts, following the Residential
Tenancies Act 1987 (WA) subject:

```
types.l4                         the nouns: cl 5 and cl 6-8 fact records, the cl 34(3) enum, tiers
part-1-preliminary.l4            cll 1-10
part-2-duties.l4                 cll 11-19
part-3-subpart-1-regulator.l4    cll 20-23
part-3-subpart-2-enforcement.l4  cll 24-33
part-3-subpart-3-remedies.l4     cll 34-56
part-3-subpart-4-offences.l4     cll 57-60
part-3-subpart-5-other.l4        cll 61-64
schedule-1-transitional.l4       Sch 1
```

Each clause is encoded isomorphically to the sentence it states, with the provision quoted in a
comment above the rule so a reviewer can audit rule against text. `@export` marks only
top-level goals — the questions an operator, the regulator or a court actually asks — and every
other `DECIDE` is an intermediary reachable from one. Dated duties use the `DEONTIC` form
(`PARTY` / `MUST` / `WITHIN` / `HENCE` / `LEST`).

Findings are recorded twice: in prose in `NOTES.md` section 3, and as rows OS-001 to OS-016 in
`registers/incident-register.xlsx`. The two must be updated together.

## 3. Coverage

64 clauses in the body, 3 in Schedule 1. **51 encoded, 13 deliberately not encoded, 0
unaccounted for.** The full clause-by-clause table is in `registers/coverage-register.md`.

The 13 exclusions are all in Subpart 3 and all of one kind: provisions that confer or describe
discretion without conditioning it — interim orders on the court's "opinion", the content an
order must have, the cl 48 matters the court must have regard to in fixing a penalty, the
injunction powers, and civil procedure. Each is marked in the module with a heading and its
reason, so the omission reads as a decision rather than an oversight.

## 4. Interpretation calls

Recorded here and in the modules, for the reviewer to accept or reject.

1. **Months as days.** `WITHIN` takes days; cll 15, 16 and Schedule 1 express periods in
   months. `days in 12 months` is 365 and `days in 6 months` is 183, named rather than inlined.
   Nothing currently turns on the rounding, but a rule comparing two such periods would inherit
   it.
2. **cl 17(4) read as inclusive.** "significant change ... includes" — the two named limbs are
   encoded as sufficient, not necessary, following the text. This is also incident OS-009.
3. **Evaluative standards left irreducible.** "reasonable steps" (cl 11), "adequately assesses"
   (cll 14, 19), "appropriate and proportionate" (cl 38(2)(e)) are single fields rather than
   decomposed tests. Decomposing them would invent law.
4. **cl 4 definitions taken as facts** except where they bear on a determination in the module
   that uses them. The encoding does not restate the Privacy Act 2020, the Sale and Supply of
   Alcohol Act 2012, the Digital Identity Services Trust Framework Act 2023 or the Legislation
   Act 2019.
5. **cl 8 operator location not modelled.** cl 8(a) makes the operator's location irrelevant,
   so it is not a condition and carries no field.

## 5. Findings

16 incidents, 8 of them machine-evaluated. Two were investigated and closed as **no defect**
(OS-002, the tier partition; OS-005, the exemption route reaching regulation-added platforms),
and both are retained in the register as evidence of coverage rather than deleted.

The five marked High:

| ID | Clauses | Finding |
| --- | --- | --- |
| OS-001 | cl 5(1)(b), 5(2) | The excluded-service carve-out attaches only to limb (a), so a healthcare or education service that is also an AI companion falls out of scope and back in under limb (b) |
| OS-003 | cl 6(1), 6(2) | A cl 7 designation makes the designated person the only operator, so the company that actually runs the platform in New Zealand owes no Part 2 duty while it stands |
| OS-007 | cl 16(5), 34(3)(f), 46 | A duty with no stated time for performance carries Tier 2 liability — up to $12m or 3% of relevant global turnover |
| OS-013 | cl 57, 18, 34(3)(g) | The only imprisonable offence is committed only by an individual designated under cl 18, so an operator that never designates extinguishes the criminal exposure of every officer by committing a Tier 2 civil breach |
| OS-014 | cl 61(1)(a) | Exemption from any or all requirements of the Act by Order in Council, with no subject-matter limit, no duration limit and no confirmation requirement on the face of the Bill |

Three of the five were found by encoding rather than by reading. OS-007 surfaced because the
`DEONTIC` form demanded a `WITHIN` value and cl 16(5) had none to give, where cll 15 and 17
both did. OS-013 surfaced from running identical conduct through a designated and an
undesignated fixture. OS-016 surfaced from the Schedule 1 rule that carries the account
creation date and then never consults it.

## 6. Limitations

- **No fidelity review.** Nothing here has been read back against the source by a second party.
  A rule can typecheck, evaluate and satisfy every assertion while saying something the Bill
  does not.
- **The source will change.** The Bill is at introduction (—1). When it is reported back from
  select committee as —2, the correct move is a new `registers/source-bundle` entry, a version
  bump, and a re-run of every probe against the new text. That re-run is the point of the
  exercise, and until it happens the findings speak only to —1.
- **Severity is an analyst's judgement**, not a product of the encoding, and is labelled as
  such in the register.
- **This is not legal advice** and makes no claim that any reading recorded here is the correct
  one. Each finding is a question for the drafter.

## 7. What would take this to `adversarially-reviewed`

1. An independent pass reading every rule against the clause it cites, in the manner of the
   Penal Code verification registers, recording fidelity defects separately from the drafting
   findings.
2. HG1 signed by a named reviewer over the payload in `gates/`.
3. Optionally, DMN projections for the cl 5 scope test and the cll 45 to 47 penalty table, with
   a fidelity report declaring every loss.
