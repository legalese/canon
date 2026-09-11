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
types.l4                         the nouns: the cl 5 fact record, the cl 34(3) act enum, tiers
part-1-preliminary.l4            cll 1, 2, 5 (encoded); cll 3, 4, 6-10 (to do)
part-2-duties.l4                 cll 11-19     scaffold
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

3. **Can a person be an operator under cl 6(1) and simultaneously not the operator under
   cl 6(2)?** cl 6(2) makes a designated person "the only operator ... while the designation
   is in place". The interaction with duties that accrued before designation is not stated.

4. **Three routes into scope, one route out.** Regulations under cl 62 add platforms
   (cl 5(1)(c)), the regulator designates operators (cl 7), and exemption orders under cl 61
   remove obligations. Whether an exemption can reach a platform brought in by regulation is
   worth testing once cll 61-62 are encoded.

5. **cl 11(2)-(3) define what does *not* discharge the duty** (manual age entry; evidence-of-age
   documents; a digital identity service; both together) without stating what does. The duty
   is "reasonable steps", so the residue is open-textured by design -- but the encoding should
   make the shape of the residue visible rather than hide it behind a boolean.

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
