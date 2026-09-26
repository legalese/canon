# Penal Code 1871 — verification register, pass 5

**Run date:** 2026-09-12
**Scope:** the 52 Chapter 17 sections added on 12 Sep 2026 — aggravated theft (ss 380 to
382), extortion (ss 383 to 389), robbery and gang-robbery (ss 390 to 402), misappropriation
from a deceased person (s 404), aggravated criminal breach of trust (ss 407 to 409), stolen
property (ss 410 to 414), fraudulent deeds and dispositions (ss 421 to 424), mischief
(ss 425 to 440) and criminal trespass (ss 441 to 462). With ss 378, 403, 405, 415, 416,
416A, 416B, 418, 420, 420A, 424A and 424B already encoded, Chapter 17 reaches 64 of its 76
live sections; the twelve remaining are pure punishment provisions, so the chapter is
complete in substance.
**Method:** every rule read back against the deposited source text in
`registers/source-bundle/PC1871.txt`, clause by clause, after it was written and
machine-checked. Same method as passes 1 to 4. Not an adversarial review.

**Result: no defect found in read-back. 5 traps in the Act's drafting recorded; 1 limit of
the toolchain recorded.**

---

## 1. What this pass covers, and the limit of it

The same limit as passes 3 and 4: these rules were read back on the day they were written,
so **a misreading shared by the rule and the read-back is invisible here**.

What compensates, as in Chapter 16, is that Chapter 17 is rich in Illustrations that state
outcomes. Every one that does is an assertion in `agent-cases.l4` rather than prose here:

| Illustration | what it tests | fixture |
| --- | --- | --- |
| s 382 Ill | a pistol carried in case the victim resists | `a theft with a weapon prepared` |
| s 383 Ill (c) | a threat to report a real offence is extortion | `a threat to report a real offence` |
| s 390(2) Ill (a) | holding a man down while taking his money is robbery | `holding a man down and taking his money` |
| s 390(3) Ill (b) | a pistol shown on the road, purse surrendered, is robbery | `a pistol shown on the road` |
| s 390(3) Ill (d) | a child held elsewhere by the gang is extortion and **not** robbery | `a child held by the gang elsewhere` |
| s 404 Ill | the servant who takes the dead master's money | `misappropriating a dead man's money` |
| s 412(2) Ill | keeping stolen jewels safe and reporting them promptly | `keeping stolen jewels to report them` |

## 2. Five traps in the drafting

### N13 — section 390 has two tests, not one

s 390(1) says "In all robbery there is either theft or extortion", and it is tempting to
read the rest of the section as one set of aggravating facts applied to either. It is not.
s 390(2) and s 390(3) are separate tests with different elements:

| | theft → robbery (s 390(2)) | extortion → robbery (s 390(3)) |
| --- | --- | --- |
| harm | death, hurt or wrongful restraint, or fear of instant such | fear of **instant** death, hurt or restraint only |
| timing | in order to, in committing, or in carrying away | at the time of the extortion |
| presence | not required | **required** |
| delivery | not required | **then and there** |

Illustration (d) is the case that proves the difference and it is the regression test: a
threat to kill a child held elsewhere by the offender's gang is extortion, and is not
robbery, because the offender is not present and the fear is not of instant death. A single
merged test would have called it robbery.

### N14 — three sections in this chapter reach persons who did not do the act

ss 394, 397 and 460 each extend to "any other person jointly concerned in committing" the
robbery or house-breaking. Read as a further requirement on the person who caused the hurt,
the rules would have been under-inclusive; read as an alternative route, they reach the
accomplice the sections plainly intend. Each is encoded as a disjunct.

### N15 — sections 411 to 414 are wider than section 410, and must not conjoin it

The receiving offences turn on knowing the property to be "stolen property **or property
obtained in whole or in part through an offence involving fraud or dishonesty**". That second
branch is not in s 410 at all. Conjoining `the property is stolen property` would have made
the receiving offences narrower than the Act makes them — a person can be guilty under s 411
in respect of property that is not stolen property within s 410.

s 410 is still encoded, because s 412 needs the gang-robbery provenance and because a caller
may want to ask the question directly. It is simply not a precondition of ss 411 to 414.

### N16 — the reasonable-excuse defence belongs to two sections, not four

ss 411(3) and 412(2) give a defence of reasonable excuse plus reasonable care. ss 413 and 414
have no such defence. Gathered into one "a defence applies" — the same temptation N12
recorded for the Chapter 16 image offences — the encoding would have exculpated the habitual
dealer and the person who assists in concealment on a ground the Act withholds from them. The
defence is conjoined, negated, to ss 411 and 412 only.

### N17 — three sections stand outside the group they sit in

**s 439** is under the Mischief heading and requires no mischief: intentionally running a
vessel aground, intending theft of what is in it, is complete in itself. Built on s 425 it
would have required proof of wrongful loss and of destruction or diminution in value, neither
of which the section mentions.

**s 453** is under the Criminal Trespass heading and requires no trespass: being found armed,
disguised or equipped is the whole of it.

**s 438** carries its own attempt — "commits **or attempts to commit** by fire or any
explosive substance such mischief as is described in section 437" — so it needs no separate
s 511 analysis, in the same way s 318 does in Chapter 16.

## 3. One limit of the toolchain, recorded

### T5 — the subject has outgrown the available engine's comfortable range

`agent-compliance.l4` now builds an `Offence Screen` record of **72 fields**, each a call into
a predicate chain reaching most of the subject. Checking that one module took about **20
minutes**; `agent-cases.l4`, at some 6,200 lines and 184 assertions, took about **25**. A full
run of all 29 modules is now over an hour.

Twice during this pass the harness returned **"NO DIAGNOSTICS PUBLISHED"** for
`agent-compliance.l4` — at a 180-second limit and again at 900 — and that line is
indistinguishable from a module that cannot be parsed. Both times the module was clean; it
had simply not finished. `report/machine-evaluation.md` §9.1 recorded that failure mode after
the first time it appeared, and this pass is the second and third.

This is a limit of the March 2026 binary described in `machine-evaluation.md` §3, not of the
encoding, and it is recorded rather than worked around. But it bears on how the subject
should grow: a 72-field screen record assembled in one constructor is the thing that costs,
and if the screen keeps growing section by section it will need to be split — by chapter, or
into a record of records — before the next large chapter is added.

## 4. Clause-by-clause read-back

### Aggravated theft, extortion and robbery

| s | provision | reading |
| --- | --- | --- |
| 380, 381, 382 | aggravated theft | Each is s 378 plus one circumstance. As written. |
| 383 | extortion | Two elements: the intentional putting in fear, and the delivery dishonestly induced by it. "whether such harm is to be caused legally or illegally" is inside the fear fact. |
| 385, 387, 389 | putting in fear to commit extortion | None conjoins s 383 — no delivery is required. s 389 lacks s 388's attempted-inducement limb, and the encoding follows. |
| 386, 388 | aggravated extortion | s 383 plus the kind of fear. s 388 disjoins its two accusation limbs. |
| 390(2) | theft as robbery | Three conjuncts, including "for that end". N13. |
| 390(3) | extortion as robbery | Four conjuncts: the extortion, presence, instant fear, and delivery then and there. N13. |
| 391 | gang-robbery | Robbery **or the attempt at it**, plus the count of five including those present and aiding. |
| 393, 394, 396, 397 | the aggravated robberies | Each builds on robbery or the attempt. ss 394 and 397 reach persons jointly concerned (N14). |
| 399, 400, 401, 402 | preparation, gangs, assembly | None requires a robbery. s 401 is expressly "not being gang-robbers", so it and s 400 are mutually exclusive on their face. |

### Misappropriation, trust and stolen property

| s | provision | reading |
| --- | --- | --- |
| 404 | property of a deceased person | s 403 plus the knowledge. The clerk-or-servant aggravation is punishment only. |
| 407, 408, 409 | aggravated criminal breach of trust | Each is s 405 plus the capacity. ss 408(2), 409(2) and 409(3) widen the capacities and add no limb. |
| 410 | stolen property | Two routes disjoined, with the cessation clause as a negated conjunct. The Explanation removes a burden of proof and adds no element. |
| 411, 412, 413, 414 | receiving, dealing, concealing | Wider than s 410 and do not conjoin it (N15). The reasonable-excuse defence is on ss 411 and 412 only (N16). |

### Fraudulent deeds, mischief and trespass

| s | provision | reading |
| --- | --- | --- |
| 421, 422, 423, 424 | fraudulent dispositions | Four independent offences; none builds on another. |
| 425 | mischief | Intent or knowledge, conjoined with the destruction or diminution. Explanations 1 and 2 widen what may be asserted and add no limb. |
| 427, 428, 435, 436, 437, 440 | aggravated mischief | Each is s 425 plus its circumstance. s 427's key-service and public-agency definitions are carried inside the disruption facts. |
| 438, 439 | vessel mischief by fire; running aground | s 438 carries its own attempt; s 439 requires no mischief (N17). |
| 441 | criminal trespass | A conjunction of two disjunctions: two conduct limbs, two intents. |
| 442 | house-breaking | s 441 plus the kind of building. Its Explanation makes any part of the body entering sufficient. This is the section `verification-register-pass-4.md` §T2 was waiting for. |
| 449, 450, 451, 452 | house-breaking for a purpose | Each is s 442 plus its purpose or preparation. |
| 453 | going equipped | Requires no trespass (N17). s 453(2) shifts a burden of proof and adds no limb. |
| 459, 460, 461, 462 | hurt in house-breaking; receptacles | s 460 reaches persons jointly concerned (N14). s 462 is s 461 plus the entrustment. |

## 5. Machine check

29 modules, **0 type errors, 230 of 230 assertions satisfied** — 192 pre-existing and 38
added by this pass. See §3 above on what a run now costs.
