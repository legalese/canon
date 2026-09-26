# Penal Code 1871 — verification register, pass 6

**Run date:** 2026-09-14
**Scope:** the 25 Chapter 18 sections added on 14 Sep 2026 — aggravated forgery (ss 466 to
469), the forged-document designation (s 470), using and possessing a forged document
(ss 471, 474), counterfeit seals and authenticating marks (ss 472, 473, 475, 476), equipment
for making a false instrument and the meaning of prejudice (ss 473A to 473C), fraudulent
cancellation of a will (s 477), falsification of accounts (s 477A), and the currency and bank
note offences (ss 489A to 489I). With ss 463 and 464 already encoded and read back in
`verification-register.md`, Chapter 18 reaches 27 of its 28 live sections; the one remaining,
s 465, is the punishment for forgery, so the chapter is complete in substance.
**Method:** every rule read back against the deposited source text in
`registers/source-bundle/PC1871.txt`, clause by clause, after it was written and
machine-checked. Same method as passes 1 to 5. Not an adversarial review.

**Result: no defect found in read-back. 5 traps in the Act's drafting recorded; 1
observation on the toolchain recorded.**

---

## 1. What this pass covers, and the limit of it

The same limit as passes 3 to 5: these rules were read back on the day they were written,
so **a misreading shared by the rule and the read-back is invisible here**.

Chapter 18 is poorer in outcome-stating Illustrations than Chapters 16 and 17 — the seventeen
under s 464 all illustrate the one definition, and the aggravated and derivative sections
carry none. One is a fixture, and it is the base every ss 466 to 469 assertion stands on:

| Illustration | what it tests | fixture |
| --- | --- | --- |
| s 464 Ill (a) | adding a cypher to Z's letter of credit on B, to defraud B, is forgery | `altering a letter of credit` |

The other 46 assertions in `agent-cases.l4` for this chapter are constructed pairs — one
fixture that satisfies a section and one that fails it on the element that distinguishes it
from its neighbour (s 471 from s 474, s 472 from s 473, s 473A from s 473B, s 475 from
s 476, s 489B from s 489C, s 489H from s 489I). They test that the sections are told apart,
which is where the drafting traps below would have shown.

## 2. Five traps in the drafting

### N18 — the section 473C(2) disregard reaches the machine case in section 473C(4)

s 473C(1) says an act or omission is to a person's prejudice "if, and only if" it will
produce one of six results, "subject to subsections (2) and (4)". s 473C(4) adds a seventh
case — an act induced by a machine responding to the instrument "shall be treated as an act
or omission to a person's prejudice". s 473C(2) then says that "for the purpose of this
section" an act the person has an enforceable duty to do, and an omission of an act he is not
entitled to do, are disregarded.

The trap is to read (4) as standing outside (2), because (1) is expressed to be subject to
both and (4) looks like a deeming that (2) cannot touch. It is not: (2) is "for the purpose of
this section", and (4) is in the section. So the disregard is encoded as a negated conjunct
over the whole disjunction — the six results **and** the machine case — not over the six
alone. A payment the machine is induced to make that the person already had an enforceable
duty to make is no prejudice, and the fixture `a card printer to induce a payment already
owed` is the regression test.

### N19 — a coin is currency, but the encoding does not compute it

s 489A(2) defines three terms for ss 489A to 489I. "Currency" *includes* any currency note or
coin which is legal tender in the country of issue; "coin" is metal used as money stamped and
issued by or under a government's authority; "bank note" is the promissory note described.
A legal-tender coin is therefore currency. But a coin need not be legal tender to be a "coin"
— a withdrawn issue is still stamped and issued by a government — so the two are not the
same set, and the encoding carries them as separate facts rather than deriving one from the
other.

The consequence for a caller: s 489F tests the **coin** fact alone, because it speaks of
"any coin"; ss 489G, 489H and 489I test the **currency** fact, because they speak of "any
currency". A caller whose facts concern a legal-tender coin under ss 489G to 489I must assert
the currency fact, and asserting the coin fact alone will return FALSE. This is a caller trap
of the kind pass 3 recorded, and it is stated in the module.

### N20 — fault sits in three different places across the chapter

The chapter uses "fraudulently or dishonestly" and its cousins in ways that do not all belong
in the `Fault` record, and the encoding follows the grammar of each section:

| section | where the fault lives | why |
| --- | --- | --- |
| 466, 467, 468, 469 | inherited through s 464, via `constitutes forgery` | "whoever forges" / "whoever commits forgery" — the fault is s 464's |
| 471, 477, 489F | the `Fault` record (s 24, s 25) | the section makes the **act** fraudulent or dishonest |
| 474 | inside the intention fact | "intending that the same shall fraudulently or dishonestly be used" qualifies the intended future use, not the possessing |
| 477A | inside each conduct fact | "with intent to defraud" is not the s 25 term, which requires an intended advantage or detriment |
| 489G | its own intention fact | "with the intention that that currency will pass as currency of a different description" — no s 24 or s 25 at all |

s 477 is the one that would have been mis-encoded by routing everything through `Fault`: its
third route, "with intent to cause damage or injury to the public or to any person", needs no
s 24 or s 25 fault, and the fixture `burning a rival will` asserts it with `blank fault`.

### N21 — the thing being forged, counterfeit or altered is asserted, never computed

Seven sections attach to a document or currency that someone else may have made false:
s 470 designates a forged document; ss 471 and 474 punish using and possessing one; ss 489B
and 489C punish dealing in and possessing counterfeit currency; ss 489H and 489I punish
delivering and possessing altered currency. In each, whether the thing *is* forged,
counterfeit or altered is a fact the caller asserts, and is not derived from `constitutes
forgery`, `constitutes forging or counterfeiting currency`, or the s 489F and s 489G rules.

The reason is the one s 410 gave in pass 5: the maker is usually not the accused, and the
`Proposed Act` bundle carries one actor's facts. Computing "the note is counterfeit" from the
accused's own s 489A facts would make every s 489B case require the accused to have been
the forger, which the section does not.

ss 489H and 489I differ in a way that is preserved rather than merged: s 489H asks whether an
**operation** mentioned in s 489F or s 489G has been performed on the currency; s 489I asks
whether an **offence** under those sections has been committed with respect to it. The first
is satisfied by an innocent alteration; the second is not. They are two facts.

### N22 — sections 466 and 467 differ in scope, and sections 474 to 476 follow them word for word

s 466 reaches "a document or an electronic record" purporting to be a court record, a public
register and the rest. s 467 reaches "a document" only — a valuable security, a will, an
authority to adopt, the receipts. The Act carries that difference into the derivative
sections: s 474 says "if the document **or electronic record** is one of the descriptions
mentioned in section 466" and "if the **document** is one of the descriptions mentioned in
section 467"; s 475 authenticates "any document described in section 467"; s 476
authenticates "any document or electronic record other than the documents described in
section 467".

The two description facts are worded to match, and are shared by ss 466, 467 and 474 rather
than re-declared, so that a caller who asserts a forged will under s 467 has already asserted
what s 474 needs. ss 475 and 476 split on one fact — whether the device or mark authenticates
a s 467 document — with s 476 taking its negation, so no document can fall under both.

## 3. One observation on the toolchain, recorded

### T6 — the run cost recorded in T5 did not recur

Pass 5 §T5 recorded `agent-cases.l4` at about 25 minutes on the language-server harness, and
`report/machine-evaluation.md` §12 recorded about 35 minutes and ~1.9 GB on the `l4` CLI.
This pass, with the same CLI binary, the file 1,000 lines longer and 47 assertions more, ran
`l4 run agent-cases.l4` in **about one minute**. Nothing in this subject changed that could
account for it; the screen record is now 79 fields and is assembled the same way.

It is recorded because T5 drew a conclusion from the cost — that the screen would need to be
split before the next large chapter — and this run does not bear it out. The conclusion is
not withdrawn, since one fast run is not an explanation, but the next reader should measure
before splitting anything.

## 4. Clause-by-clause read-back

### Aggravated forgery and the forged document

| s | provision | reading |
| --- | --- | --- |
| 466, 467 | forgery of a court record; of a valuable security or will | Each is `constitutes forgery` plus one description fact. s 466 is "document or electronic record"; s 467 is "document" (N22). |
| 468, 469 | forgery for cheating; to harm reputation | Each is `constitutes forgery` plus one purpose. s 469 is satisfied by intention **or** knowledge of likely use, one disjunctive fact. |
| 470 | a forged document | A designation. Caller-asserted, not computed (N21). |
| 471 | using as genuine | Fraud or dishonesty from the `Fault` record; knowledge or reason to believe; use as genuine. "Punished in the same manner" is punishment only. |
| 474 | possession | Knowledge, the intention of fraudulent or dishonest use (inside the fact, N20), and one of the s 466 or s 467 descriptions as an element. Which of the two is punishment only. |

### Seals, marks and instruments

| s | provision | reading |
| --- | --- | --- |
| 472, 473 | counterfeit seal, plate or instrument | Two conduct limbs shared and disjoined — making or counterfeiting, or possession knowing it counterfeit — plus the intent. They split on whether the intended forgery would be punishable under s 467 or under another section of the chapter. |
| 473A | equipment for a false instrument | Complete on the conduct plus knowledge that the equipment is designed or adapted for making a **false** instrument. No further intent. |
| 473B | equipment with intent to induce prejudice | Conduct; designed or adapted for making **any** instrument; the two-part intent in (b)(i) and (ii); and the s 473C prejudice test conjoined. s 473C(3)'s machine extension is written into the (b)(i) fact. |
| 473C | prejudice | Six results and the (4) machine case disjoined; the (2) disregard a negated conjunct over the whole (N18); (5)'s wider "loss" written into the (a) fact. |
| 475, 476 | counterfeit authenticating mark | Two conduct limbs shared and disjoined, plus the intent; they split on one fact, s 476 taking its negation (N22). |

### Cancellation, accounts

| s | provision | reading |
| --- | --- | --- |
| 477 | cancelling, destroying or secreting a will | Three routes to fault, two from `Fault` and one inside the record (N20). The conduct fact carries the attempts and the mischief limb, so no s 511 analysis is needed. The document must be, or purport to be, a will, an adoption authority or a valuable security. |
| 477A | falsification of accounts | The capacity, then two conduct limbs disjoined, each carrying "intentionally and with intent to defraud" (N20). Explanation 1 removes a pleading burden; Explanation 2 defines a set. Neither adds a limb. |

### Currency and bank notes

| s | provision | reading |
| --- | --- | --- |
| 489A(2) | currency, bank note, coin | Three caller-asserted facts with the definitions in the field names; currency and bank note gathered for ss 489A to 489C. Coin stands alone (N19). |
| 489A | forging or counterfeiting | The thing is currency or a bank note, and the accused forges, counterfeits or knowingly performs part of the process. |
| 489B, 489C | dealing in; possessing | Each needs the thing to **be** forged or counterfeit (N21) and the knowledge. s 489C adds possession and the intent to use as genuine; s 489B the dealing verbs. |
| 489D | instruments and materials | Conduct over any die, machinery, instrument or material; then the purpose-or-knowledge disjunction as one fact. No counterfeit need exist. |
| 489E | abetting counterfeiting abroad | s 107 abetment conduct from the `Abetment` record, conjoined with presence in Singapore and the thing abetted. s 108 is not conjoined, as in s 111. |
| 489F | diminishing or adulterating a coin | Fraud or dishonesty from `Fault`; the coin fact; the operation. The Explanation illustrates the operation. |
| 489G | altering appearance | The currency fact; the operation; the intention that it pass as a different description (N20). |
| 489H, 489I | delivering; possessing altered currency | s 489H on an **operation** having been performed, s 489I on an **offence** having been committed (N21). s 489I adds the intent to use as genuine. |

## 5. Machine check

31 modules, **0 type errors, 277 of 277 assertions satisfied** — 230 pre-existing and 47
added by this pass. See §3 above on what the run cost this time.
