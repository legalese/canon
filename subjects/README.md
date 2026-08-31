# subjects/

One directory per body of law. Five are deposited as at **2026-08-31**. Four are Singapore statutes;
the fifth is not a statute and not Singaporean, and is flagged below.

| subject | what it encodes | status |
| --- | --- | --- |
| [`sg/succession`](sg/succession) | Wills Act 1838, Intestate Succession Act 1967, Probate and Administration Act 1934 — three Acts against one ontology | `draft` |
| [`sg/child-support`](sg/child-support) | the SG Child Support Package announced at the National Day Rally on 23 August 2026, and childcare leave under the Child Development Co-Savings Act 2001 | `draft` |
| [`sg/pdpa-2012`](sg/pdpa-2012) | Personal Data Protection Act 2012, Part VIA (data breach notification) | `draft` |
| [`sg/penal-code-1871`](sg/penal-code-1871) | Penal Code 1871, s 301 (transferred malice), as substituted by Act 15 of 2019 | `draft` |
| [`us/chubb-hospital-cash`](us/chubb-hospital-cash) | a **synthetic** supplemental hospitalization cash policy — never law, never in force — encoded twice, independently, as evidence in a replication study | `experimental` |

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

`regcf` (SEC Regulation Crowdfunding) and the British Nationality Act 1981 are encoded in
`legalese/l4-ide` and have not been deposited here yet.

*(This paragraph read "Empty at this writing" until 2026-08-25, by which point three
subjects had landed; a fourth landed on 2026-08-27. A README that describes a directory it
no longer matches is worse than none, because it is believed.)*

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
