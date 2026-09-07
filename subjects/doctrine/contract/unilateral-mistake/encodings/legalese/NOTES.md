# NOTES — what this row is, what it is not, and what to attack first

Read [README.md](README.md) for the doctrine and the findings. This file is the row's
idiosyncrasies: the decisions taken, the ones that are contestable, and the things a reviewer
should go after. No script reads it.

---

## 1. Why this row is under `doctrine/`, and not under `sg/`

`docs/directory-conventions.md` gives two grammars. §2 files **enacted law by the authority that
enacted it**, because for a statute the authority is constitutive of the work. §3 files
**commercial instruments by genre**, because a contract has no promulgating authority and its
governing law is a term, changeable by drafting.

A doctrine of judge-made law compared **across** authorities fits neither, and the misfit is not
cosmetic:

- Filing it at `sg/unilateral-mistake` would make three of the four modules trespassers in a
  Singapore directory, and would misdescribe the subject: the subject is the *question*, and
  Singapore's answer is one of four.
- Filing four sibling subjects — `sg/…`, `uk/…`, `au/…`, `us/…` — would put the comparison
  nowhere. The comparison is the deliverable, and a delta has no home in either operand.

So this row seeds a third grammar, `subjects/doctrine/<area>/<leaf>/`, on the same shape as §3's
`contracts/<genre>/<leaf>/` and with the same device: a controlled vocabulary for the middle
component, in [`subjects/doctrine/AREAS.md`](../../../AREAS.md), extended by PR to that file.

**The principle, stated so it can be disagreed with.** For enacted law the *authority* is
constitutive; for a commercial instrument the *genre* is what a reader browses by; for a doctrine
under comparison the *question* is constitutive and the authorities are its variants. `extent` in
`subject.json` carries the list of authorities, exactly as §2.1 puts extent in the descriptor
rather than in the path.

**This is a proposal, not a ruling.** `docs/directory-conventions.md` §12 owns the rewrite and this
row has not amended it. A reviewer who thinks the doctrine tree is wrong should move the row and
say why in that document — the argument above is here precisely so it does not have to be
reconstructed.

## 2. What has no counterpart in the statute rows

- **No in-force date, no revised edition, no rule-version axis, no dated arms.** A judgment has no
  commencement. The corpus states the law as at the latest decision it reaches (*Quoine*,
  24 February 2020) and cannot answer about the law before *Chwee Kin Keong* in 2005 — when, on
  the High Court's view, the equitable jurisdiction did not exist at all.
- **No `@ref` to a provision.** The `@ref` annotations cite paragraph numbers of judgments, which
  is the nearest equivalent and is not the same thing: a paragraph is a court's reasoning, not an
  enacted text, and the operative words are chosen by the reader.
- **`source/` vendors the captures, and that was a decision.** 948KB across six files: the two
  eLitigation pages and the Wayback capture of *Donovan*, each as captured HTML, plus the
  tag-stripped text derived from each. The alternative — cite and do not vendor — was rejected
  because it would make this row unauditable: `registers/source-bundle.json` records a sha256 for
  every document, and `report/verify-quotations.py` re-derives all 51 quotations from the text
  files. Both are worthless without the bytes they name, and "trust the encoding's quotations"
  is precisely what this corpus refuses to ask of a reader.

  The exposure is real and is not hidden: the Singapore judgments' terms are **UNDETERMINED**
  (`SOURCE-LICENSE.md` §1), and this row now reproduces them in full rather than only in the
  passages the modules quote. `NOTICE` records it. If the open question is ever settled against
  reproduction, this directory is the first thing to delete, and deleting it costs the digests
  and the quotation check but not the encoding.

## 3. Three of the four modules are read through a Singapore lens

This is the largest single limitation and it is stated on the face of each module, not only here.

The English and Australian authorities were **not retrieved from their own reports**. Every
quotation of them is a quotation of *Chwee Kin Keong*'s account, taken from the retrieved Singapore
judgment. That is a legitimate basis for the comparison this row is making — the question is what
Singapore departed from, and a Singapore court's statement of what it was departing from is
directly on point — but it is **not** a survey of English or Australian law, and it will not have
caught later authority in either place.

The American module is different in kind again: the Restatement is not the law of any jurisdiction
until a State adopts it, and it is quoted from a Californian judgment rather than from the
Institute. Fork **F-US1** records the point.

**A reviewer with access to the CLR, the Law Reports and the ALI text should treat §3 as the first
thing to check.** The most likely defect in this corpus is a foreign rule that has moved since 2005
and that nothing here would notice.

## 4. Modelling decisions worth knowing before you read the code

- **`the mistake was fundamental` is an input.** *Chwee Kin Keong* at [34] expressly declined to
  define what makes a mistake serious enough. A model that computed it would be inventing the one
  thing the court refused to state.
- **`the mistake was fundamental` is set `FALSE` on the two non-term fixtures** (*Smith v Hughes*,
  *Quoine*). Fundamentality in the Singapore sense is defined *by reference to a term*, so on a
  non-term mistake the predicate is not engaged rather than false. `FALSE` is the encoding of "not
  engaged" and it is safe only because the term test already fails ahead of it. If a future reading
  lets equity reach beyond a term — the question *Quoine* at [80] left open, fork **F3** — this
  choice becomes load-bearing and must be revisited.
- **The record admits combinations no court would find.** Nothing stops a fixture from carrying
  `neither knowledge nor reason to suspect` together with `a conscious omission to disabuse`, which
  is incoherent — you cannot consciously omit to correct a mistake you do not suspect. No fixture
  does it, and no rule can reach the conduct arms without the knowledge condition beside them
  (which is what *Chwee Kin Keong* at [78] requires), so the incoherence is unreachable in practice.
  It is not prevented by the type, and a stricter ontology would prevent it.
- **There is deliberately no record collecting all four verdicts.** England refuses on a whole class
  of facts, and a four-verdict record would propagate that refusal and hide the three answers that
  do exist. The comparison is made one jurisdiction at a time, which is also how the battery
  asserts it.
- **The one `REFUSE` is narrow on purpose.** It fires only on the class *Chwee Kin Keong* at [80]
  decided — a fundamental mistake as to a term, constructive but not actual knowledge, plus
  impropriety. An earlier draft refused whenever the common law limb failed and the other party had
  suspected anything, which made the model refuse on *Smith v Hughes* — a case decided in 1871.
  Reporting doubt about settled law is a worse failure than reporting a wrong answer, because it is
  harder to spot.

## 5. Goldens, CI, and what stands behind the numbers

**Nothing regenerates anything here.** canon has no CI, and these modules are outside `l4-ide`'s
corpus globs, so `jl4-test` never sees them. `tests/run-transcript.txt` is a **point-in-time
record** of one `l4 run`, not a golden that anything checks.

Measured 2026-09-07 on a binary built from `l4-ide` at the tip of `props/refuse`, run with
`JL4_LIBRARY_PATH` **unset** so the binary resolves its own embedded prelude. That matters: the
`REFUSE` construct postdates the installed `l4` on this machine, and pointing an older binary at a
newer prelude produces cascading "could not find a definition" errors that read as a broken
encoding. If you cannot reproduce the 69 assertions, check the binary before you check the code.

`report/comparison-table.md` and `report/comparison-table.json` are **derived**, by
`report/make-table.py`, from `l4 run` output — not typed by hand. The table in `README.md` is a
transcription of them, and is the one thing in this row that can silently drift. Re-derive it after
any change to a jurisdiction module.

## 6. What a reviewer should attack first, in order

1. **F-AU1 — that Australia has no "void" outcome.** This single characterisation produces three
   `stands` cells where Singapore and England both void, and it rests on one hedged sentence of a
   Singapore judgment about an Australian one (*"seems to suggest"*, at [73]). If it is wrong, the
   Australian column changes on three fixtures and Delta 2 loses half its force. It is the highest
   ratio of consequence to evidence anywhere in this row.
2. **F-C1 — that *Digilandmall*'s third appellant made only a conscious omission**, rather than
   taking deliberate steps to prevent discovery. The stronger reading makes Australia relieve and
   erases the divergence the fixture exists to show. The court described haste, and at [98] warned
   that haste is not itself knowledge — but "pounced on the opportunity to make more money before
   the mistake was discovered" (at [93]) can be read either way.
3. **The Smith v Hughes risk characterisation (F-US2).** The § 154(b) reading is this model's, not a
   holding, and it is the only thing keeping the American column from diverging on that fixture.
4. **Every quotation, character by character.** The module comments reproduce long passages, and a
   quotation that has drifted is worse than a paraphrase because it invites no checking. The source
   is `https://www.elitigation.sg/gd/s/2005_SGCA_2`.
5. **The five deltas in README.md against the assertions in `mistake-cases.l4` §`The deltas`.** The
   prose and the code are meant to say the same thing; the assertions exist so that they cannot
   quietly stop doing so.

## 7. What is not here

No projections (`l4 export` to DMN/BPMN was not run), no wizard, no `gates/`, no pipeline receipts.
There is no `etc/go` sidecar for this subject in `l4-ide`, so no run journal, no HG1 waiver and no
`verify` — the same posture as `us/chubb-hospital-cash` and the two `contracts/` rows, and unlike
`sg/succession`. The registers under `registers/` were written by hand and validated with
`l4-ide`'s `etc/go/lib/register-validate.mjs`; that validation is recorded in
`report/register-validation.txt` and is the only mechanical check any of them has had.
