# Advance Medical Directive Act 1996 — naive encoding

**Method: naive.** Written straight from the deposited text with the
`writing-l4-rules` skill and nothing else. No pipeline, no coverage table, no
probe record, no independent test pass, no human gate. One pass, no review.
Everything below is an observation made while encoding, not a checked finding.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 May 2023 (`../../registers/source-bundle/AMDA1996.txt`).

**Checks:** `l4 run amd-cases.l4` — 41 assertions satisfied, 0 errors,
0 warnings. `l4 run` exits 0 on a failing assertion, so the diagnostics were
read rather than the exit code.

## What is encoded

ss 2–10, which is the whole of the Act's decision-making. ss 11–22 are savings,
offences, composition and the regulation power: they state consequences rather
than decide anything, and nothing in ss 2–10 depends on them.

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
