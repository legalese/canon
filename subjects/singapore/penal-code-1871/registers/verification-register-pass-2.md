# Penal Code 1871 — verification pass 2: the rules added 09 Sep 2026

**Run date:** 2026-09-09
**Scope:** every rule that `registers/verification-register.md` did not cover — the sections
added to the encoding after that pass:

- `chapter-2-definitions.l4` in full — ss 6A, 7, 8–10, 11, 12, 17, 19, 20, 21, 22, 22A, 27,
  28, 29, 29A, 29B, 30, 31, 31A, 40, 41, 42, 43, 44, 44A, 45–48, 49, 50, 51
- `chapter-2-participation.l4` in full — ss 32–38
- `chapter-3-punishments.l4` in full — ss 53, 54, 72, 73, 74, 74A–74E
- `chapter-2-explanations.l4`, the sections added that day — ss 26A, 26E, 26F, 26G, 26H
- `chapter-4-exceptions.l4`, the sections added that day — ss 77, 78, 79, 80, 81, 85, 86, 87,
  88, 89, 90, 91, 92, 93, 94

**Method:** each rule read against `registers/source-bundle/PC1871.txt` (SSO current version
as at 09 Sep 2026), subsection by subsection, including every Explanation, proviso and
Illustration. Every rule then re-run through the `jl4-lsp` batch checker.

---

## Defects found

| # | Section | Severity | Finding |
| --- | --- | --- | --- |
| W1 | s 74B(1)(b) | **medium** | The excluded-offence test reused the flag `the offence is under section 304B 304C or 335A`, shared with ss 73 and 74A. But **s 74B's list is different**: s 304B, 304C, 377BG, 377BH, 377BI, 377BJ or 377BK. **s 335A is not in it.** The encoding therefore withheld the s 74B doubling from an offence under s 335A committed against a person below 14, which the section plainly allows. The three sections had been read as sharing an exclusion list; they do not. |
| W2 | s 89 | **medium** | s 89 covers an act done "**by** or by consent, either express or implied, of the guardian or other person having lawful charge". The encoding had the consent limb, but rendered the "by the guardian" limb as `bound by law to do it or justified by law in doing it` — which is the **s 76** test, not "done by the guardian". A guardian acting personally failed s 89 unless independently law-bound; someone law-bound but neither the guardian nor holding the guardian's consent passed it. |
| W3 | s 44A | medium | The whole content of s 44A is that "bodily injury" denotes **a series of bodily injuries as well as a single** bodily injury — the exact parallel of s 33(1) for "act" and "omission". The encoding dropped the series extension entirely and substituted an unstated definition ("an s 44 injury which is to the body"). No field for a series existed. |
| W4 | ss 45, 46 | low | Both were cited in a `DECLARE`'s `@ref` but neither had a rule. "Life" and "death" — the life or death of a human being **unless the contrary appears from the context** — were decided nowhere, and the contrary-intention proviso had no field at all. This also meant `registers/coverage-register.md` counted them as encoded on the strength of a citation carried by a record declaration. |

All four are fixed in this pass. W1 carries a regression fixture and two new assertions
(`section 335A offence against a child below 14`): the s 74B doubling now applies to it and
the s 74A doubling still does not.

## Correct as written (checked, no change needed)

**`chapter-2-participation.l4`, ss 32 to 38** — faithful throughout.

- s 32 — all three limbs, with the contrary-intention proviso correctly negated.
- s 33(1) and (2) — and note the encoding gets the hard part right: `it is not known which of
  the acts in the series caused the effect` is declared as a fact but is deliberately **not**
  a precondition, because s 33(2) says "**even if** it is not known".
- ss 34, 36, 37 — faithful.
- s 35 — faithful. `this person is one of those persons` is redundant alongside `this person
  joins in the act`, but adds no error.
- s 38 — the permissive reading is a documented interpretive choice, retained.

**`chapter-2-explanations.l4`, ss 26A and 26E to 26H** — faithful throughout.

- s 26A — both limbs of "voluntarily".
- s 26E(1), (2) and (3) — including the ladder in (3): rashness is also established by
  intention or knowledge.
- s 26F(1) and (2) — including the wider ladder in (2): intention, knowledge **or** rashness.
- s 26G — the full chain: the (1) gate with the s 301(1) carve-out, the (2) elements, the (3)
  negligence requirement, and **s 26G(5)** correctly encoded as a negated conjunct, so a
  defence measured against the intended target defeats the transfer. s 26G(4) needs no limb
  because the rule already requires all fault elements to be proven.
- s 26H(1) to (4) — including (3): an offence may be one of strict liability though not
  expressly so described, encoded by **not** requiring express description; and (4)'s defence
  correctly gated on the offence being one of strict liability.

**`chapter-3-punishments.l4`** — faithful apart from W1.

- s 53, s 54 — the five punishments, and life as a flag rather than a number of years.
- s 72 — the ordering death > life > longer maximum term.
- s 73 — including the s 73(4) definition of "excluded offence" (ss 304B, 304C, 335A, or
  punishable with death or life), checked against the definition itself.
- s 74 — ss 298 and 298A and the death-or-life exclusion, per s 74(2)(a).
- s 74A — ss 304B, 304C, 335A **and 376F**, the knowledge requirement in (2), and the (2A)
  defence.
- s 74C, s 74D — both correctly confined to Chapter 16 and excluding death-or-life offences.
- s 74E — the doubling applies once however many sections are engaged, which is s 74E(1)(a);
  and s 74E(2) is satisfied structurally, since prescribed minima pass through unchanged and
  the record carries no maximum number of strokes to enhance.

**`chapter-4-exceptions.l4`, the sections added that day** — faithful apart from W2.

- ss 77, 78 — including s 78's good-faith belief in jurisdiction.
- s 79 — and s 79(2) with Explanations 1 and 2 correctly treated as rules of proof, not as
  further conditions.
- s 80 — all four conjuncts of s 80(1); s 80(2) again a rule of proof.
- s 81 — the Explanation is treated as a conjunct, on the view that without it the section
  does not excuse. An interpretive choice, now recorded in `NOTES.md` §3.
- ss 85, 86 — including **s 85(3)**, whose unsound-mind limb correctly does **not** carry the
  "without knowledge or against the will" requirement that s 85(2) attaches to its own limbs;
  and s 86(1)'s unsound-mind disposal rather than a simple acquittal.
- ss 87, 88 — s 87's four negations and the above-18 requirement; s 88 correctly **without**
  an age requirement.
- s 89 proviso (a) to (d) — faithful, and correctly distinguished from the s 92 proviso.
- ss 90, 91 — all three limbs of s 90, with (c)'s contrary-intention proviso; s 91 correctly
  shutting out ss 87, 88 and 89.
- s 92 — and the encoding gets a trap right that is easy to miss: **the s 92 proviso is not
  the s 89 proviso.** In s 89(c) the limb is *grievous* hurt saved by preventing death or
  grievous hurt or curing a grievous disease; in s 92(c) it is *hurt* saved by preventing
  death or hurt. Both are encoded separately and correctly.
- The Explanation to s 92 — "mere pecuniary benefit is not benefit within the meaning of
  sections 88, 89 and 92" — is correctly applied to all three.
- ss 93, 94 — including s 94's proviso and its murder / offences-against-the-State carve-out.

**`chapter-2-definitions.l4`** — faithful apart from W3 and W4.

- s 6A — the ss 24 and 25 carve-out and the displacement by another written law.
- ss 11, 12, 17, 19, 20 — faithful. s 19's Illustration (c) needs no negation: a Magistrate
  who can only commit for trial fails the definitive-judgment limbs anyway.
- s 21 — all of (a) to (j), with (h) correctly **split into two limbs** ("every officer whose
  duty it is …" and "every officer in the service or pay of Government, or remunerated by
  fees or commission"); Explanation 2 as a further disjunct, not a proviso; and s 21(2)
  correctly gated on a charge under s 175, 178, 179, 180 or 228.
- s 22 — the four definitions as one record, with "movable" derived rather than asserted.
- s 22A(1) and (2) — the state-of-mind / not-a-state-of-mind partition.
- s 27 — the deeming rule. The encoding adds a first limb (`the person has the property
  physically`) that s 27 does not state; it is the ordinary case the section builds on.
  Recorded in `NOTES.md` §3 rather than removed.
- s 28 — including Explanation 1 (exactness not essential, encoded by not requiring it) and
  Explanation 2's presumption, which correctly supplies the fault element until rebutted.
- s 29(a) to (f), s 29A, s 29B — faithful.
- s 30(1) and (2) — including the "or purports to be" limb and the card list.
- s 31, s 31A — faithful.
- ss 40 and 41 — the three reference contexts of s 40, and s 41 implemented by reading the
  s 40(3) threshold against the **maximum** term. s 40(1)'s "except in the Chapters and
  sections mentioned in subsections (2) and (3)" needs no exclusion, because the (2) and (3)
  meanings are supersets of the (1) meaning.
- ss 42, 43, 44, 47, 48, 51 — faithful.
- ss 7, 8, 9, 49, 50 — rules of construction with no factual test; documented as such under
  their own headings. See `registers/coverage-register.md` §3.

## Unused declared fields

Not defects — each is a fact the statute mentions that the correct rule does not gate on —
but recorded so a later reader does not mistake them for live inputs:

| field | section | why unused |
| --- | --- | --- |
| `it is not known which of the acts in the series caused the effect` | s 33(2) | "even if" — not a precondition |
| `the imitation is exact` | s 28 Expl 1 | exactness is not essential |
| `the holder is employed only temporarily or on a particular occasion as a clerk or servant` | s 27 Expl | temporary employment still counts |
| `is empowered only to commit for trial to another court` | s 19 Illus (c) | already excluded by the definitive-judgment limbs |

## What this pass does not establish

It is a reading of the encoding against the deposited text by one pass, not an adversarial
review. It does not touch the sections `registers/coverage-register.md` records as absent —
no reading can find a defect in a rule that was never written — and it grants no human gate.
`status` stays `draft`.
