# Triage of the §8 divergences — **PROPOSED, NOT DECIDED**

> **Status, 26 August 2026: none of this is settled.** `denovo-diff.md` emits every witness
> `UNTRIAGED` by design — the comparator measures, and SPEC.md §8's three dispositions
> (`ENCODING-ERROR`, `GENUINE-AMBIGUITY`, `IMPROVEMENT-OVER-CORPUS`) are readings of the law.
> HG1 is **waived, not granted**, and no signer is enrolled, so nobody with standing has ruled.
> What follows is one reader's proposal with its statutory hook, written so that a domain expert
> can disagree with something specific instead of starting over. Accepting one means editing
> `denovo-diff.md`'s disposition column and saying so in the fork register entry it belongs to.

## The clause the whole disagreement is about

Four of the five comparison pairs agreed 24/24. The fifth, `distributable-fund`, diverged five
times, and every witness turns on one sentence:

> If a person dies intestate after 2 June 1967, he being at the time of his death — (a) domiciled
> in Singapore and **possessed beneficially** of property, whether movable or immovable, or both,
> situated in Singapore; or (b) domiciled outside Singapore and **possessed beneficially** of
> immovable property situated in Singapore, that property or the proceeds thereof, **after payment
> thereout of the expenses of due administration** as prescribed by the Probate and Administration
> Act 1934, shall be distributed among the persons entitled to succeed beneficially to that
> property or the proceeds thereof.
>
> — Intestate Succession Act 1967 (2020 Rev Ed) s 5

Three phrases do the work: _possessed beneficially_, _expenses of due administration_, and what it
means to pay _thereout_.

## Read the fork column in `denovo-diff.md` with care

That table stamps **`F-ISA-A7` on all five witnesses. That is the PAIR's declared fork**, read
from `surface-map.json`, where `fork` is a field of the pair and not of the row. Taking it as five
witnesses of one ambiguity would be wrong. They land on three different register entries, and one
of them lands on none:

|   # | witness                                                      |     corpus | cleanroom | register entry |
| --: | ------------------------------------------------------------ | ---------: | --------: | -------------- |
|   1 | s 4 — domiciled abroad, movables and immovables in Singapore | 636,363.64 |   600,000 | `F-ISA-A4`     |
|   2 | s 5 — an estate with substantial debts                       |    700,000 | 1,000,000 | **none**       |
|   3 | s 5 — expenses exceeding the whole Singapore estate          |   −900,000 |         0 | `F-ISA-A7`     |
|   4 | s 5 — part of the Singapore estate held as trustee           |  1,000,000 |   500,000 | `F-ISA-A6`     |
|   5 | s 5 — the whole Singapore estate held as trustee             |  1,000,000 |         0 | `F-ISA-A6`     |

---

## 1 · Apportioning administration expenses — `F-ISA-A4`

**corpus 636,363.64 · cleanroom 600,000 · proposed `GENUINE-AMBIGUITY`**

A deceased domiciled abroad with both movable and immovable property in Singapore. s 4(2) reaches
the Singapore land whatever the domicile; s 4(1) sends the movables to the law of the domicile.
The Act supplies **no rule** for apportioning the expenses of administration across that split, and
the two encodings chose different conventions. The repeating decimal on the corpus side is the tell
that a proportional convention was picked rather than found.

`F-ISA-A4` is the only entry in this register still marked **open**, and deliberately: it records
two live readings of s 4's reach and encodes _both_, kept apart. This divergence is downstream of
that choice rather than a new question.

_What would settle it:_ nothing in the four Acts. Either authority on the situs rule for
administration expenses, or a ruling that the convention is arbitrary and must be declared rather
than computed.

## 2 · Debts are not expenses — no register entry

**corpus 700,000 · cleanroom 1,000,000 · proposed `GENUINE-AMBIGUITY`, leaning cleanroom**

The committed corpus deducts the deceased's debts from the fund. The cleanroom deducts only the
expenses of due administration and says in terms why the debts are not deducted: s 5 names
_administration expenses_, and debts are the Probate and Administration Act's business under its
First Schedule.

The letter favours the cleanroom. Practice favours the corpus, since an administrator distributes
what is left once creditors are paid, and a fund that ignores debts is not money anyone receives.
**This is the one worth ruling first**: both readings are defensible and they differ by 300,000 on
a 1,000,000 estate.

**It has no fork-register entry, and that is itself the finding.** `F-ISA-A7` sits on the same
clause but its recorded readings are about a _nil versus negative_ fund, not about debts. So the
cleanroom encoder did not perceive the debts question as an ambiguity at all — they read s 5,
took the narrow meaning, and moved on. A fork register records what its author noticed; register
completeness is unfalsifiable by construction and is exactly what HG1 carries. This is a worked
example of the gap, produced by the differential rather than by review.

_What would settle it:_ PAA 1934 First Schedule read against ISA s 5, and whether any Singapore
authority treats the s 5 fund as net of debts.

## 3 · A fund below zero — `F-ISA-A7`

**corpus −900,000 · cleanroom 0 · proposed `IMPROVEMENT-OVER-CORPUS`** — the clearest of the five.

Where expenses exceed the whole Singapore estate, the committed corpus produces a **negative**
distributable fund and hands every taker a negative share. The cleanroom floors it at zero with a
`max 0`.

"Payment **thereout**" contemplates a payment out of a fund, not a fund below zero, and s 7
distributes portions of an estate rather than liabilities. `F-ISA-A7` records exactly this and
records the losing reading too: R2 — _"the fund is NEGATIVE, and every share is a negative quantity
that the takers owe"_ — **rejected**, because a share of a negative estate is not a thing the Act
creates; the creditors' shortfall is the Probate Act's business under its First Schedule.

Note what the cleanroom is careful **not** to do, and the register flags it as a repair to its own
earlier wording: the s 5 gate still opens, the persons entitled are still identified, and their
fractions still sum to 1. What is nil is the thing the fractions are fractions of. An earlier draft
said "the fund is nil and nobody takes", and the second half of that was wrong.

_What would settle it:_ very little. If HG1 agrees a negative fund is not a thing the Act creates,
this is an encoding error in the committed corpus and should be fixed there.

## 4 and 5 · "Possessed beneficially" and property held on trust — `F-ISA-A6`

**corpus 1,000,000 → 1,000,000 · cleanroom 500,000 → 0 · proposed `IMPROVEMENT-OVER-CORPUS`,
with a stated assumption that could reverse it**

Where part of the Singapore estate is held as trustee, the cleanroom nets it out of the fund; where
the _whole_ estate is held as trustee, s 5's gate closes on the cleanroom side — neither limb is
made out — and the fund is nil. The committed ontology has **no cell for trust property at all**,
so its figures are gross either way.

The phrase appears in both limbs of s 5 and again in its operative words, and property held as
trustee is not held beneficially. `F-ISA-A6` takes exactly that reading: _"A positive NET value in
the relevant cell — gross less the property held as trustee — IS the evidence of beneficial
possession."_

**The assumption that could reverse this, stated by the surface map itself.** The committed
`immovable property in Singapore` and `movable property in Singapore` cells are treated as **gross**
in these rows, because with no trustee cell there is nowhere else for the trust property to go. A
reader who takes those committed cells to mean the beneficial value _already_ would say the rows
should carry a zero trustee figure on the cleanroom side too — and then the two encodings agree and
there is no divergence here at all. That choice **is** the divergence.

So the honest disposition may be narrower than `IMPROVEMENT-OVER-CORPUS`: the cleanroom models a
distinction the committed ontology cannot express, and whether that is an improvement or a
difference in what the fact layer is asked to supply depends on how the committed cells are meant
to be populated — which is a question for whoever wrote them.

_What would settle it:_ a ruling on what the committed `*-property-in-Singapore` cells mean. If
they are gross, the cleanroom is an improvement. If they are net, the surface map's rows are wrong
and should carry zeros on both sides.

---

## What this file is not

It is not a change to `denovo-diff.md`, which still reads `UNTRIAGED` for all five and should
until somebody rules. It is not evidence: the evidence is `denovo-diff.json`, its 120 evaluations,
and the run journal. And it is not a review of the encoding — reading 27,515 lines against four
Acts is what HG1 waived, and five divergences in one clause is not that.
