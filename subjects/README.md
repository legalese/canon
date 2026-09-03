# subjects/

One directory per body of law. **Seven are deposited as at 2026-09-04.** Four are Singapore
statutes; of the other three, one is a synthetic insurance policy and two are commercial standard
forms. Each of those three is flagged below. One subject, `contracts/investment/yc-safe-premoney`,
holds source text and no encoding at all, which the `what it encodes` column says plainly.

| subject | what it encodes | status |
| --- | --- | --- |
| [`sg/succession`](sg/succession) | Wills Act 1838, Intestate Succession Act 1967, Probate and Administration Act 1934 — three Acts against one ontology | `draft` |
| [`sg/child-support`](sg/child-support) | the SG Child Support Package announced at the National Day Rally on 23 August 2026, and childcare leave under the Child Development Co-Savings Act 2001 | `draft` |
| [`sg/pdpa-2012`](sg/pdpa-2012) | Personal Data Protection Act 2012, Part VIA (data breach notification) | `draft` |
| [`sg/penal-code-1871`](sg/penal-code-1871) | Penal Code 1871, s 301 (transferred malice), as substituted by Act 15 of 2019 | `draft` |
| [`us/chubb-hospital-cash`](us/chubb-hospital-cash) | a **synthetic** supplemental hospitalization cash policy — never law, never in force — encoded twice, independently, as evidence in a replication study | `experimental` |
| [`contracts/investment/yc-safe-postmoney`](contracts/investment/yc-safe-postmoney) | the Y Combinator post-money SAFE — six instruments plus four Pro Rata Side Letters, with their User Guide — deposited verbatim, with one encoding row | `draft` |
| [`contracts/investment/yc-safe-premoney`](contracts/investment/yc-safe-premoney) | nothing, and none planned in this repository — **sources only**: the 2013–2018 "original safe", four US variants, recovered from the Internet Archive | `draft` |

`sg/child-support` is the odd one and worth knowing about before you read it: its primary
source is an **announcement, not an enactment**. No Bill has been introduced, so its
rule-version axis carries *administered today* against *announced*, and the statute the
announcement would amend is recorded as the source bundle's `instrument`.

`sg/penal-code-1871` is the smallest row here — one section, hand-encoded in inert style,
with no `cases/`, `projections/`, `registers/`, `report/` or `gates/`. It is filed as a
subject rather than an l4-ide example because it is a body of law, and this is where bodies
of law live; its `NOTES.md` states what the sidecar does not carry. It is also the row whose
**source terms bite hardest**: inert style works by quoting the statute inline, so unlike
`sg/pdpa-2012` it reproduces its section verbatim rather than paraphrasing it. See that
row's `SOURCE-LICENSE.md`.

`us/chubb-hospital-cash` is the row that most needs its label read. It is the first `experimental`
row, and the status is not a weaker `draft` — it marks a different kind of thing. **The instrument is
synthetic: fictional parties, never issued, never in force, never construed.** It was invented by
researchers as a benchmarking target, and it is filed here because it is a body of contractual rules
that has been encoded, not because anyone is subject to it. It is also the first row whose source
terms are **determined** rather than undetermined — the policy originates in a CC BY 4.0 article, so
attribution is required and is recorded in `NOTICE`. Two independent encodings sit side by side under
`encodings/`, written blind to each other and to the benchmark's answer key, because the comparison
between them is the evidence. Read its `NOTES.md` before drawing any conclusion from it: the source
text was modified before publication in a way that removed the operative insuring clause.

The two `contracts/` rows are the first entries under a **second grammar**. Everything above them
is enacted law, filed by the authority that enacted it — `sg/`, `us/`, an ISO 3166-1 code. A
commercial instrument has no promulgating authority and often no jurisdiction at all until a
governing-law clause supplies one, so it is filed by **genre** instead:
`contracts/<genre>/<leaf>/`, with `governing_law` as a `subject.json` field rather than a
directory. The genre vocabulary is controlled — insurance, investment, leasing, lending — and
lives in [`contracts/GENRES.md`](contracts/GENRES.md), which these rows seed. See
`docs/directory-conventions.md` §3, and §8.4 of that document, which names
`yc-safe-postmoney` as its worked example of a standard form. **That document is not on this
branch**: it lives on `docs/directory-conventions` and is unlinked here for that reason, so
read it with `git show docs/directory-conventions:docs/directory-conventions.md`.

Both SAFE rows carry the publisher's text byte-exact, a Markdown rendering of it, the header and
footer strings pandoc throws away (which is where the licence and the version stamp live), digests
for everything, and a validated source bundle. **`yc-safe-premoney` stops there** — no `encodings/`
directory, and none planned in this repository; its `NOTES.md` says why. `yc-safe-postmoney` adds
one encoding row and a fork register, and neither row has `projections/`, `report/` or `gates/`, so
no human review has been sought for either. They also differ from each other in the way that matters
most for a corpus: `yc-safe-postmoney` is the second row
here whose source terms are **determined** — CC BY-ND 4.0, printed in the form's own footer, so
attribution is a condition and is recorded in `NOTICE` — while `yc-safe-premoney` carries **no
terms at all**, because the licence footer was added in 2018 and those captures are from 2014.
Read each row's `SOURCE-LICENSE.md` before deriving anything from it. `yc-safe-postmoney`'s also
records an unresolved question: whether an L4 formalisation of a form is an "adaptation" under a
NoDerivatives licence.

`regcf` (SEC Regulation Crowdfunding) and the British Nationality Act 1981 are encoded in
`legalese/l4-ide` and have not been deposited here yet.

*(This paragraph read "Empty at this writing" until 2026-08-25, by which point three
subjects had landed; a fourth landed on 2026-08-27, a fifth on 2026-08-31, and the two
`contracts/` rows on 2026-09-04. A README that describes a directory it no longer matches is
worse than none, because it is believed.)*

The directory contract (the "class" — see the repository README for the class/instance
design) is the subject-sidecar shape defined by the l4-ide orchestrator:

| file                | role                                                                                                                                                 |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subject.json`      | machine-readable descriptor: id, display name, citation, source URL, corpus modules, per-leg projection declarations, encoding version, status       |
| `NOTES.md`          | this subject's idiosyncrasies, in prose, for humans — no script reads it                                                                             |
| `SOURCE-LICENSE.md` | the terms the quoted legal text carries, and the attribution NOTICE requires                                                                         |
| `*.l4`              | the encoding, in inert style, with `@ref` citations on dated arms                                                                                    |
| `cases/`            | dated scenario cases; expected values machine-evaluated, never hand-typed                                                                            |
| `projections/`      | emitted DMN/BPMN/other artifacts + fidelity reports declaring every loss                                                                             |
| `registers/`        | fork register, external-modification register, source bundle — validated against the schemas in l4-ide `specs/todo/single-instruction-demo/schemas/` |
| `report/`           | the conversion report                                                                                                                                |
| `gates/`            | HG1/HG2 grant artifacts: payloads, signatures, waivers, `allowed_signers`                                                                            |

An instance is expected to veer from the class; its divergences are recorded in its own
`NOTES.md`, never by forking the template.

Two amendments to that table are already in force and are not yet written into it, because
`docs/directory-conventions.md` supersedes it and its own §12
owns the rewrite. First, the sidecar shape above now describes a **vendored encoding row** under
`encodings/<encoder>/`, one level below the subject, and the descriptor splits in two:
`subject.json` at the subject level carries facts about the law, `encoding.json` in each row
carries facts about the encoding (§4.2). All seven subjects already do this. Second, `source/` and
`registers/` sit at the **subject** level, because the source text is a fact about the law and is
shared by every row (§6). That one is not yet uniform, and the tree is the honest record: both
`contracts/` rows put `source/` and `registers/` at the subject level, `us/chubb-hospital-cash`
puts `registers/` there, and the `sg/` rows keep both inside the encoding row. Do not read the
table above as contradicting the conventions document.
