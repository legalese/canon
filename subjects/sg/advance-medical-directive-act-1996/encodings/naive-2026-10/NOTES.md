# Advance Medical Directive Act 1996 — naive encoding

**Method: naive.** Written straight from the deposited text with the
`writing-l4-rules` skill and nothing else. No pipeline, no coverage table, no
probe record, no independent test pass, no human gate. One pass, no review.
Everything below is an observation made while encoding, not a checked finding.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 May 2023 (`../../registers/source-bundle/AMDA1996.txt`).

**Checks:** `l4 run amd-cases.l4` and `l4 run amd-offences-cases.l4` — 93
assertions satisfied, 0 errors, 0 warnings. `l4 run` exits 0 on a failing assertion, so the diagnostics were
read rather than the exit code.

## What is encoded

**ss 2–21 — the whole Act** except s 22, the regulation power, which confers a
power and decides nothing. `amd-act.l4` has the decision procedures;
`amd-offences.l4` has the savings, the offences, the protections and the
causation rule.

The register, the prescribed forms, whether a person is in fact terminally ill,
and whether a witness took "reasonable steps" are all facts supplied. The Act
does not decide them, and neither does this encoding. What s 9 decides is *who
gets to say* the patient is terminally ill, and that is what is modelled.

## Three things worth a second look

**1. The same interest is treated three different ways.** The disqualifying
interests are listed three times, and the lists do not match:

| limb | s 3(3) witness | s 9(9) certifying | s 10(4) acting |
|---|---|---|---|
| beneficiary under will or insurance | ✓ | ✓ | ✓ |
| interest under an instrument | ✓ | ✓ | ✓ |
| **entitled on intestacy** | ✓ | — | — |
| entitled to provident fund moneys | ✓ | ✓ | ✓ |
| has registered an objection | ✓ | ✓ | — |

So a person who would take on the patient's intestacy **cannot witness** the
directive, but may certify the patient terminally ill and may act on the
directive. Whether that is deliberate is not something the text settles. It may
well be: a witness is chosen by the patient and a treating practitioner is not,
so the Act may be guarding the making of the directive more tightly than its
execution. Recorded because the asymmetry is invisible unless the three lists
are put side by side. Asserted in `amd-cases.l4` § `10 — the duty to act`.

**2. A duty and a prohibition can land on the same practitioner at once.**
s 10(2) imposes a *duty* to act on the directive. s 10(4) *forbids* acting where
the practitioner takes under the patient's will. Both can be true of the same
person at the same time: the Act does not disapply the duty, it adds a
prohibition beside it. s 10(5) is what resolves it, by requiring transfer of the
patient's care — but it is a separate subsection, and reading s 10(2) alone
would leave a practitioner with a duty they are forbidden to perform.

Note the contrast: s 10(2)'s own parenthesis *does* lift the duty for a
practitioner who has registered an objection. So the Act knows how to disapply
the duty when it wants to, and did not do so for s 10(4). Asserted as the pair
on `the practitioner takes under the will`.

**3. s 9(6) and s 9(7) say the same thing twice.** s 9(6): the patient is
determined terminally ill "only on the unanimous decision of the committee".
s 9(7): if the committee cannot reach a unanimous decision, the patient "is
presumed not to be terminally ill". Given (6), (7) adds nothing to the outcome —
anything short of unanimity already fails. (7) may be doing evidential work that
(6) does not, by making it a *presumption* rather than a bare absence of
determination, which would matter to anyone trying to displace it later. The
encoding implements (6), and (7) is consistent with it.

## What would need doing before this is worth anything

- The prescribed forms, and the Advance Medical Directive Regulations, are not
  held. s 3(1) requires "the prescribed form" and the whole of s 9 runs on
  prescribed forms; none of that was retrieved.
- s 2's definition of "terminal illness" has two limbs of its own and is not
  encoded — it is taken as a fact, because applying it is a medical judgment.
- No case law was searched.
- The three observations above are observations. None has been checked against
  any authority, and the first two would need someone who knows the Act's
  purpose to say whether they are drafting defects or deliberate.


---

# Added with sections 11 to 21

## The interest list is stated FOUR times, with four different contents

The first version of this note set out three lists. s 14(2) is a fourth, and it
differs from all of them:

| limb | s 3(3) witness | s 9(9) certifying | s 10(4) acting | **s 14(2) forfeiture** |
|---|---|---|---|---|
| beneficiary under will or insurance | yes | yes | yes | **yes** |
| interest under an instrument | yes | yes | yes | **yes** |
| entitled on intestacy | yes | — | — | **yes** |
| entitled to provident fund moneys | yes | yes | yes | **yes** |
| has registered an objection | yes | yes | — | **—** |

So the Act describes the same family of conflicts of interest four times and
never the same way twice. The intestacy limb is the clearest case: it bars you
from witnessing a directive and forfeits your inheritance if you procure one by
fraud, but does not stop you certifying the patient terminally ill or acting on
the directive. Asserted across both case files.

Three of the four lists could have been one defined term. They are not, and
nothing in the Act explains the differences.

## Other observations

**A charge freezes the directive; a conviction revokes it.** s 14(3) stops
anyone acting on a directive once a person is *charged* under s 14(1), until the
directive's validity is ascertained. s 14(4) then deems it revoked on
*conviction*. The freeze does not wait for proof.

**Forfeiture under s 14(2) does not wait for a conviction either** — it bites on
a person who "is guilty of an offence under subsection (1) (**whether or not he
or she has been convicted** of that offence)". So a civil court deciding a
succession dispute must decide the criminal question for itself.

**Only limb (c) of s 14(1) has a mental element.** Procuring a directive by
"deception, fraud, misstatement, unconscionable conduct or undue influence" and
forging one are described by their conduct alone; concealing a revocation must
be **wilful**. "Misstatement" in limb (a) is notably wide — on its face it
reaches an innocent one.

**s 15 makes it an offence to ask.** A person who has or will likely have the
medical care of a patient must not ask whether they have made a directive. The
exception is narrow and cumulative: it must be the *responsible* practitioner,
the discussion must be consistent with good medical practice, held within that
relationship, **and** in furtherance of public education. A ward nurse asking
out of ordinary concern commits the offence.

**s 19(1) needs good faith AND absence of negligence**, and s 20(2) confirms it
from the other side: the causation rule "does not relieve a medical practitioner
from the consequences of a negligent decision". A negligent practitioner loses
both protections on the same fact. Asserted as that pair.

**s 16 catches both directions.** An insurer may not require a directive as a
condition, and may not prohibit one either. s 16(2) severs the offending
condition rather than voiding the policy — contrast s 54 of the Employment Act,
which destroys the whole contract.

## Still not encoded

- s 22, the regulation power.
- The prescribed forms and the Advance Medical Directive Regulations, which
  s 3(1) and the whole of s 9 run on.
- No case law was searched, and no human gate has been sought.
