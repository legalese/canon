# Four Acts, one ontology

A **second, independent** encoding of Singapore's death-in-the-family statutes, written
without reading the [`legalese`](../legalese/) encoding that sits beside it — so the two can
be compared as evidence rather than as one thing checked against itself.

> **DRAFT. NOT REVIEWED.** The pipeline run behind [`report/`](report/) carries **HG1 waived,
> not granted**: no human has read this against the Acts section by section. Everything the
> report asserts is machine-checkable fact — 1,907 assertions passing, a propositional
> consistency pass, a differential comparison against the encoding next door. None of that is
> a claim that the encoding says what the law says. Do not cite it as one.

| Act                                     | the question it answers here                                     |
| --------------------------------------- | ---------------------------------------------------------------- |
| **Wills Act 1838**                      | is there a valid, unrevoked will, and who may witness it?        |
| **Intestate Succession Act 1967**       | who takes what is left, and in what shares?                      |
| **Probate and Administration Act 1934** | who administers, what comes off the top, and when?               |
| **Guardianship of Infants Act 1934**    | who may act for an infant beneficiary — and receipt for a share? |

The fourth is the one the `legalese` encoding does not carry, and it is the reason this
encoding exists in the shape it does. An infant who takes on an intestacy raises a question
neither the Intestate Succession Act nor the Probate and Administration Act answers: _who can
give a good discharge for the money?_ That question only has an answer when all four Acts are
read against the same family.

## What is here

```
family-domain.l4                 the shared ontology — 37 types, no rules
wills-act.l4                     WA 1838
intestate-succession-act.l4      ISA 1967
probate-administration-act.l4    PAA 1934
guardianship-of-infants-act.l4   GIA 1934
family-cases.l4                  the case suite, and the cross-Act joins
tests/                           four goldens per module, committed beside them
registers/                       source bundle · sweep · fork register · surface map
report/                          the pipeline's own account of the run, and what it cost
source/fetch-sso.py              re-runs the fetch, reproducibly
```

## Running it

```
JL4_LIBRARY_PATH=<l4-ide>/jl4-core/libraries l4 run family-cases.l4 --json
```

Measured on this deposit, 26 Aug 2026: **1,907 assertions across six modules, none failing,
no errors** — 341 + 381 + 429 + 404 + 352, with `family-domain.l4` contributing none, being
types only.

### There is no `cases/` directory here, and that is deliberate

The sibling encodings put their case suite in `cases/`. **That layout does not run.** L4
resolves `IMPORT` by basename, in the order `JL4_LIBRARY_PATH → root → importer-relative →
embedded → XDG → bundle`, and none of those steps reaches a _parent_ directory. A case file in
`cases/` therefore cannot find the modules it imports.

Measured, 26 Aug 2026, on `../legalese/cases/sg-succession-cases.l4` as deposited:

| invocation                                   | result                                                               |
| -------------------------------------------- | -------------------------------------------------------------------- |
| `JL4_LIBRARY_PATH` unset (embedded stdlib)   | `Module not found: sg-succession-domain`, `sg-isa`; **0 assertions** |
| `JL4_LIBRARY_PATH=<repo>/jl4-core/libraries` | same, **0 assertions**                                               |
| the same file copied flat beside its modules | `ok`, **37 assertions**, none failing                                |

`JL4_LIBRARY_PATH` is a _single directory_, not a search list, so it cannot be used to add the
encoding root as a second entry.

Two consequences worth stating plainly. First, this encoding keeps its case suite flat, which
is a divergence from the class recorded here as the class's own README asks. Second — and this
is the part that matters more — **the `cases/` files already deposited under
`sg/succession/encodings/legalese/` and `sg/child-support/encodings/legalese/` do not run from
the layout they are deposited in.** The `.l4` text is intact and runs when moved; it is the
directory shape that breaks resolution. That is a defect in the deposits, not in this note, and
it is not fixed here.

## What the run found

Three things, all in [`report/`](report/) with the artifacts behind them:

**Eight decisions that nobody can satisfy, and all eight are correct.** `l4 verify`'s
propositional rung reported eight `unsat` findings. Seven are Wills Act sections that _abolish_
a ground — s 9, s 10(2), s 11, s 12, s 14, s 5(4), s 6(3) — encoded as the subsection verbatim
followed by `… FALSE`, so that a denial is distinguishable from a silence. The eighth withholds
a power from a guardian on an _expressio unius_ inference, and that inference is in the fork
register with the competing reading recorded live. The verifier cannot tell a drafting bug from
a statutory abolition; both are unsatisfiable skeletons.

**Five divergences from the encoding next door, and they are all one clause.** 115 of 120
comparison cells agreed. Every disagreement is `distributable-fund`, Intestate Succession Act
s 5, and turns on three phrases in one sentence: _possessed beneficially_, _expenses of due
administration_, and what it means to pay _thereout_. On one fact pattern the encoding next
door returns a **negative** distributable fund of −900,000 where this one floors at zero. The
dispositions are **UNTRIAGED**: the comparator measures, and triage is a reading of the law.
See [`report/denovo-diff.md`](report/denovo-diff.md) for the measurement and
[`report/TRIAGE.md`](report/TRIAGE.md) for a proposed reading of each — proposed, because HG1 is
waived and nobody with standing has ruled. Read the diff table's fork column with care: it stamps
one id on all five witnesses because `fork` is declared per _pair_, and the five actually land on
three register entries and one gap.

**Five cross-Act joins that a broken upstream Act actually breaks.** Sixteen were claimed;
eleven turned out to be _adjacency_ — two single-Act assertions side by side, each of which
would still pass if the other Act said the opposite. The test is mutation, not reading: copy
the module set, break the upstream Act, re-run. Five survived and are written as one
expression each; the other eleven are relabelled in the case suite as cross-checks, a
duplicate, or blocked-with-a-reason.

## Not legal advice

An encoding is a reading. This one has not been reviewed by a lawyer, and the Acts themselves
are at [Singapore Statutes Online](https://sso.agc.gov.sg/).
