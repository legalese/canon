# Defect categories: what each covers and how to probe for it

The procedures step 7A (Probe) runs. [`LQA-PIPELINE.md`](LQA-PIPELINE.md) defines the steps; this
file defines the thirteen categories well enough that two legal engineers probing the same Part
would look for the same things.

Every procedure has the same parts:

- **Looks for**: what a defect in this category is.
- **Procedure**: what to do, over each encoded Part. Steps that need the L4 say so.
- **Usual method**: the `found_by` value findings in this category most often carry. It is a
  guide, not a rule: record how this finding was actually found.
- **Demonstrate**: what evidence suits it at 8A.
- **Usual answers**: what most often kills a candidate at 9A. Check these before recording one.
- **Not this**: the neighbouring category it is most often confused with.

A probe of one category over one Part is recorded in `registers/probe-record.json` whether or not
it found anything. "Ran T over Part 2, found nothing" is a result.

**Always first, for every category:** read the jurisdiction's Interpretation Act provisions in the
0H set that bear on the Part. In WA, three findings in one subject were answered by the
Interpretation Act after they had been written up.

---

## D — Definition

**Looks for.** A defined term used in a sense its definition does not bear; a term the operative
provisions depend on that is not defined and has no settled ordinary meaning; definitions that are
circular, overlap, or contradict each other; a definition that captures cases the operative
provision plainly does not intend (or misses ones it does).

**Procedure.**
1. List every defined term in the instrument and every term imported from the Interpretation Act or
   a parent Act.
2. For each use of each term, check that the definition fits the use. In the L4, every defined term
   should be one predicate or type; a use that needs a different predicate is a candidate.
3. For each operative condition, ask what facts make it true, and whether a case can satisfy the
   definition while defeating the provision's evident purpose. Write that case as a test.
4. Check definitions against each other for overlap and circularity.

**Usual method.** `ENC`: a term that will not encode as one predicate.
**Demonstrate.** A test case that satisfies the definition and produces the wrong result.
**Usual answers.** The Interpretation Act's general definitions; "unless the contrary intention
appears"; a definition in the parent Act that applies to the subsidiary instrument.
**Not this.** A term used consistently but capable of two meanings is U.

## R — Reference

**Looks for.** A cross-reference to a provision that does not exist, the wrong provision, or a
repealed one; a reference whose target does not do what the citing provision assumes; a pronoun,
"the person", "that notice" or similar with no antecedent, or more than one.

**Procedure.**
1. Every cross-reference is already in the reference register (2A). For each: does the target exist
   at the pinned print, and is it the provision meant?
2. For each reference marked *encoded*, call the target's encoding with the facts the citing
   provision supplies. Does it answer the question the citing provision asks?
3. For every anaphoric expression ("the person", "the notice", "such a cat"), identify its
   antecedent. In the L4, each must bind to exactly one variable.

**Usual method.** `ENC` for antecedents; `RD` for a reference to a non-existent provision; `CMP`
for a target that has since been amended.
**Demonstrate.** For a target mismatch, a test calling the encoded target with the citing
provision's facts. For an antecedent, the binding choice and a case where the choices diverge.
**Usual answers.** The Interpretation Act's rules on references to amended or renumbered
provisions; an obvious drafting slip that a court would read past (still record it, at low
severity).
**Not this.** Two Acts that each work alone but conflict is I.

## L — Logic

**Looks for.** Contradiction (two provisions require incompatible things); a gap (a case no rule
decides); an overlap where two rules give different answers to the same case; an unreachable
condition or branch; a fact the instrument reads that no provision can make true.

**Procedure.**
1. Run `l4 verify` over every module and treat each `unsat`, `dead-branch`, `vacuous-guard` and
   `unreachable-outcome` as a candidate.
2. Run the console checker over the scheme. A conferred fact with no act that confers it is a
   candidate: the instrument reads something it gives no way to bring about.
3. For each decision the instrument requires (grant or refuse, liable or not), enumerate the
   combinations of its conditions and check every combination is decided exactly once.

**Usual method.** `CHK`.
**Demonstrate.** The tool's report, plus a test or scenario showing the case.
**Usual answers.** A provision outside the encoded Parts, or in another Act, that supplies the
missing rule. Check the reference register and coverage record before recording a gap.
**Not this.** A gap in time (a period no rule governs) is T.

## T — Time

**Looks for.** Commencement that leaves provisions inoperable or out of order; deadlines without a
start point, or with an ambiguous one; computation of time (clear days, business days, "within",
"after"); calendar arithmetic (month ends, leap years, ages); a duty that arises before it can be
complied with; expiry, renewal and transition between periods.

**Procedure.**
1. List every period, date, age and deadline. For each, identify the event that starts it and the
   rule that computes it, including the Interpretation Act's.
2. Encode ages and periods against a real calendar, never as day counts. Test each at month ends,
   29 February, and the boundary day itself.
3. For each duty, ask when it can first be complied with and when it first applies. A duty that
   applies first is a candidate.
4. In the console, run a generated year and look for clustering: registrations that lapse days
   after grant, duties that fall due on a weekend.

**Usual method.** `TST` or `SIM`.
**Demonstrate.** A dated test case; a simulation run with its seed.
**Usual answers.** The Interpretation Act's rules on computing time and on "all convenient speed"
where no time is fixed; a fee or transitional rule that softens the effect.
**Not this.** Uncertainty about which event starts a period, where both readings are arguable, is
U with the readings in the fork register.

## U — Uncertainty

**Looks for.** Ambiguity or vagueness that changes outcomes: words that bear two readings, both
arguable, where the drafter could have chosen and did not.

**Procedure.**
1. Every fork in the register (5A) is a candidate. Ask: does the choice change an outcome in a
   realistic case? If not, it stays a fork and is not a finding.
2. Where it does, assert both readings and show the case where they part.

**Usual method.** `ENC`: the encoding had to choose.
**Demonstrate.** Assertions both ways on the fork, and the case that divides them.
**Usual answers.** A canon of construction or a settled authority that resolves it; a purpose
clause that makes one reading untenable. If resolved, the fork is closed and the candidate is
VERIFIED-NO-DEFECT.
**Not this.** A fork is not a defect. U is the finding that the drafter left a consequential choice
open, and it always points to a fork.

## P — Power

**Looks for.** Delegated legislation beyond the power it is made under; a power with no holder, or
the wrong holder; a discretion without criteria; a decision with no procedure, notice, reasons or
review where the scheme needs them.

**Procedure.**
1. For delegated legislation: for each provision, identify the empowering provision and test the
   provision against its terms (subject matter, class versus individual, purpose).
2. For every power the instrument confers: who holds it, on what conditions, with what procedure,
   and with what review. Encode each decision's inputs; a decision with no encodable criteria is a
   candidate.
3. Look for options the instrument opens but does not close: a power to "refuse to consider", a
   decision that may simply never be made.

**Usual method.** `CMP` for delegated legislation against its power; `ENC` for undefined
discretions.
**Demonstrate.** For excess of power, the empowering words set against the provision; for an open
discretion, a scenario where the decision is never made and nothing follows.
**Usual answers.** General provisions of the Interpretation Act on delegated legislation and on
powers; administrative-law review that supplies what the instrument omits.
**Not this.** A power whose exercise has no consequence for breach is E.

## E — Enforcement

**Looks for.** An obligation with no consequence for breach; an offence with no penalty, or a
penalty inconsistent with the scheme; nobody empowered to enforce; a defence or exemption that
defeats the offence in ordinary cases; an infringement regime that does not reach the offence.

**Procedure.**
1. For every duty ("must", "must not"), find the consequence. Encode duty and consequence as a
   pair; an unpaired duty is a candidate.
2. For every offence, check the penalty, who may prosecute or issue an infringement notice, and
   the limitation period (from the 0H set).
3. For every defence and exemption, test whether it covers the ordinary case.

**Usual method.** `ENC`.
**Demonstrate.** A scenario in which the duty is breached and nothing follows, or the defence
always applies.
**Usual answers.** A general offence provision in the instrument or in the 0H meta-legislation that
attaches a penalty to any contravention.
**Not this.** An offence that cannot practically be complied with is W.

## M — Amendment

**Looks for.** An amending instruction that fails to apply (the words to be replaced are not
there, or appear twice); a repair that stops short (related provisions left unchanged); a missed
consequential amendment; missing savings, transitional or validating provisions; retrospective
effect left unresolved.

**Procedure.** Applies to Bills and amending instruments.
1. Apply every instruction to the pinned print of the amended Act. Each must apply exactly once.
2. For each provision amended, search the amended Act for provisions that depend on it, and check
   each still works.
3. Ask what happens to things done under the old law: applications in progress, instruments
   already made, offences already committed. Is each dealt with?
4. Read the extrinsic material for what the amendment is meant to achieve, and test whether it
   does, from commencement.

**Usual method.** `CMP`.
**Demonstrate.** The amended text as it would read, and a test across the commencement date.
**Usual answers.** The Interpretation Act's savings provisions on repeal and amendment.
**Not this.** A conflict between the amended Act and a third Act is I.

## I — Interaction

**Looks for.** Conflict between Parts of the instrument; between the instrument and its parent Act;
between it and other Acts; between levels of government.

**Procedure.**
1. For each pair of provisions that govern the same actor or act, check that they can both be
   complied with.
2. For each referenced provision encoded at 4A, run the citing and cited provisions together on
   shared facts.
3. Where a local law, regulation or other subordinate instrument may be made, ask whether it can
   forbid what the instrument requires.

**Usual method.** `TST`.
**Demonstrate.** A scenario where an actor cannot comply with both.
**Usual answers.** The Interpretation Act's rule that subordinate legislation inconsistent with an
Act is invalid to the extent of the inconsistency; express priority provisions.
**Not this.** A wrong cross-reference is R.

## X — Extrinsic

**Looks for.** An explanatory memorandum, second-reading speech, heading, note or example at odds
with the enacted words.

**Procedure.**
1. For each clause note in the explanatory memorandum, set it against the clause it describes and
   check the modality (may, must, must not), the actor, the conditions and the consequence.
2. For each heading, note and example, check it against the operative words.
3. Record every mismatch, then ask whether it matters: could a court or an official be led by the
   extrinsic material into the wrong reading?

**Usual method.** `CMP`.
**Demonstrate.** The two texts side by side, and a case where acting on the extrinsic material gives
a different result from the Act.
**Usual answers.** The Interpretation Act's rules on the status of headings, notes and examples and
on the use of extrinsic material.
**Not this.** A mismatch between the instrument and its own drafting manual is S.

## W — Workability

**Looks for.** A duty that cannot practically be complied with; a scheme that depends on a body, a
register, a form or a service that does not exist; deadlines that cannot be met at realistic
volumes.

**Procedure.**
1. For each duty, identify what compliance requires in the world: who must act, what must exist.
2. Check each requirement against the 3H set: does the body, register or form exist?
3. Where volumes matter, run a simulation at stated parameters.

**Usual method.** `SIM` or `ENC`.
**Demonstrate.** Reported only where the impossibility is demonstrated: a scenario, or a simulation
whose parameters are stated and defended.
**Usual answers.** A body or form established by another instrument not yet in the set (record the
gap at 3H); a power to extend time.
**Not this.** A duty that applies before it can be complied with, as a matter of dates, is T.

## F — Form

**Looks for.** Mechanical errors: typographical errors, wrong numbering, broken lists, grammar that
changes nothing, formatting defects in the print.

**Procedure.**
1. Read the instrument once for form alone.
2. Check numbering sequences and list structures mechanically.

**Usual method.** `RD`.
**Demonstrate.** The text itself, quoted with its location.
**Usual answers.** None needed beyond confirming the print.
**Not this.** A departure from a rule in the drafting manual is S. Reported after the substantive
categories.

## S — Style

**Looks for.** Non-compliance with the jurisdiction's drafting manual, style guide or plain-language
guidelines.

**Procedure.**
1. Take the manual from the 0H set, at its pinned version.
2. For each rule in the manual that can be checked against a text (definitions placement, use of
   "shall", sentence length, structure of offences, numbering conventions), check every provision.
3. Every finding cites the manual's paragraph. A style objection with no paragraph behind it is
   not an S finding.

**Usual method.** `CMP`.
**Demonstrate.** The provision and the manual paragraph side by side.
**Usual answers.** A later version of the manual; an exception the manual itself allows.
**Not this.** A mechanical slip with no rule behind it is F. Reported after the substantive
categories.
