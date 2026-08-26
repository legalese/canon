# NOTES — `cleanroom-2026-08`

This encoding's idiosyncrasies, and the traps it paid for. No script reads this file.

Where a claim here is a measurement, it says when it was measured. Where it is a reading of
the law, it is a reading and not a holding.

## Why four Acts are one subject, and one ontology

They are four views of one event — a death in a family — and they share their nouns. The same
person is the Probate Act's _deceased_, the Wills Act's _testator_ and the Intestate Succession
Act's _intestate_. The same human being is a beneficiary under a will, a next-of-kin under ISA
rule 3, a person interested in the estate with standing under PAA s 18(2), and — if under 21 —
an _infant_ whose share nobody may receipt for without the Guardianship Act's say-so.

So `family-domain.l4` owns the nouns (37 types, no rules), each Act module owns its own verbs
and imports the ontology, and `family-cases.l4` is where they meet.

## The cleanroom condition

This encoding was written **without reading** `../legalese/`. That is not a stylistic
preference: `report/denovo-diff.md` compares the two, and a comparison between an encoding and
a thing it was copied from measures nothing. Reading the other side destroys the measurement
silently and unrecoverably — there is no way to un-read it and no way for a reviewer to detect
that it happened. The only artifact licensed to read both is `registers/surface-map.json`,
which has to, because it declares which rule on one side corresponds to which on the other.

## L4 traps this corpus paid for

**Module basenames are globally unique.** L4 resolves `IMPORT` by basename, so two modules with
the same name collide no matter where they sit. Four Acts written independently produced 19
pairwise name collisions; all 19 were renamed, and the rename was proved behaviour-preserving
by byte-identical evaluation output before and after.

**A file cannot `IMPORT` a library sharing its own basename.** The failure is a silent
`GraphException`, not a "not found".

**A case suite in a `cases/` subdirectory cannot find its own modules.** Resolution order is
`JL4_LIBRARY_PATH → root → importer-relative → embedded → XDG → bundle`, and no step reaches a
parent directory; `JL4_LIBRARY_PATH` is a single directory, not a search list. Measured against
both sibling encodings on 26 Aug 2026 — see this encoding's README for the table. That is why
`family-cases.l4` is flat.

**`JSONDECODE` returns `EITHER STRING T`, not `MAYBE T`.** The explicit `GIVETH` is
load-bearing; getting it wrong is a type error that reads like a syntax error.

**`JSONDECODE` ignores fields it was not told about**, and the diff oracle's `applyRename` is
top-level only. Measured: `{"x":{"a":1,"b":2},"y":9}` decodes to `Outer OF (Inner OF 1)`. Those
two facts together are what made the §8 comparison possible at all across two encodings with
different record shapes — a battery row carries the _union_ of both encodings' field names at
every level of nesting, and each side decodes what it declares. Without it there is no shared
fact battery and no comparison.

**`#ASSERT`, not `#EVAL`.** An `#EVAL` prints; only an `#ASSERT` can fail. An early draft of
this corpus carried 524 evaluations and zero assertions, which would have counted as zero tests.
Converting them forced every expected answer to be re-derived from the statute rather than
blessed from whatever the code printed — and that pass is where several of the defects below
were found.

## The abolition idiom, and why it looks like a bug

Where a section abolishes a ground, the encoding states the subsection verbatim and then
`… FALSE`:

```
`s 14 — the will is revoked by a presumption of an intention on the ground of an
 alteration in circumstances` MEANS
    "No will shall be revoked by any presumption of an intention on the ground of an
     alteration in circumstances."
    ... FALSE
```

The `FALSE` is not dead code and must not be tidied away: it _is_ the section. A reader can see
which fact the section is about and that the fact has no effect, and an `#ASSERT NOT` makes the
denial observable. Leaving the antecedent out of the file entirely would make a **denial
indistinguishable from a silence**.

The cost is that `l4 verify`'s propositional rung reports each one as `unsat` — "TRUE for no
assignment of its atoms: as drafting, a requirement nobody can meet." Seven of the eight
findings in `report/` are exactly this. The verifier is right and the encoding is right; the
layer simply cannot tell a drafting bug from a statutory abolition. If an encoding could
_declare_ an intended `unsat`, only the eighth would surface — and the eighth is the one that
deserves to, because it rests on an inference rather than express words.

## What the adversarial passes found, and what was done

Every one below was a defect in _this_ encoding, found before deposit and repaired. They are
recorded because the shape of the mistake is more useful than the fix.

- **ISA s 3 defines "child" relationally.** A child adopted _away_ by strangers read TRUE and
  qualified as the intestate's child.
- **ISA rule 6 was conditioned on NOT TAKING where the Act conditions it on DEATH.** One case
  moved from a niece taking the estate to the Government taking all of it.
- **A wife who predeceased her husband was still a "widow"** for PAA s 18(4)(a), s 19,
  s 13(2)(c) and s 56(2).
- **PAA s 13(2), the Act's only ranked class, was unranked in effect** — three of four
  adjacent-rung swaps left all 306 assertions green. Found by mutation, not by reading.
- **WA s 27(3) counted a will appointing a guardian of a _stranger's_ child.**
- **Vacuity.** A mutation harness replaced each conjunct with the identity element of its chain
  and re-ran the suite; a conjunct whose deletion leaves the suite green has no test. On the
  Probate Act: 162 mutants, 79 survivors before (33 of them real untested rule fragments — 8×
  what a human reviewer had found), 3 after, each documented as a fact about the Act.
- **Adjacency masquerading as composition.** Eleven of sixteen claimed cross-Act joins were two
  single-Act assertions side by side. See the README.

## Open, and deliberately so

**GIA s 6(1) against ss 15–18.** s 6(1) says the survivor shall "be guardian of the infant",
unqualified; ss 15–18 speak of the "guardian of the **property**". The field that decides
whether s 17 bites is an unfixed input, and nothing in this encoding computes it. The same
unfixed member decides both whether a mother may take the grant under PAA s 21(2) and whether
she may give a good discharge under the Guardianship Act — **and it decides them in opposite
directions**. Left open, in the register, rather than resolved by fiat.

**No single statutory age of majority in Singapore.** The Interpretation Act 1965 supplies none,
and Civil Law Act 1909 s 35(3)(b) preserves other statutes' age requirements. Each Act's own
threshold is encoded where it appears.

**No rule-version axis.** The law is stated as at 26 August 2026 and there are zero dated arms,
so `p3-check` reports temporal closure NOT CHECKED rather than printing a vacuous green over an
empty matched set. This corpus cannot answer a question about an earlier version.

**The money join is an expression, not a field.** `family-domain.l4` declares an `Entitlement`
type and no record carries one, so nothing a downstream consumer builds carries a share from one
module to another. Inside the case suite the join is computed; outside it, the hand-off does not
exist yet.
