# subjects/

One directory per body of law. Three are deposited as at **2026-08-25**, all Singapore:

| subject | what it encodes | status |
| --- | --- | --- |
| [`sg/succession`](sg/succession) | Wills Act 1838, Intestate Succession Act 1967, Probate and Administration Act 1934 — three Acts against one ontology | `draft` |
| [`sg/child-support`](sg/child-support) | the SG Child Support Package announced at the National Day Rally on 23 August 2026, and childcare leave under the Child Development Co-Savings Act 2001 | `draft` |
| [`sg/pdpa-2012`](sg/pdpa-2012) | Personal Data Protection Act 2012, Part VIA (data breach notification) | `draft` |

`sg/child-support` is the odd one and worth knowing about before you read it: its primary
source is an **announcement, not an enactment**. No Bill has been introduced, so its
rule-version axis carries *administered today* against *announced*, and the statute the
announcement would amend is recorded as the source bundle's `instrument`.

`regcf` (SEC Regulation Crowdfunding) and the British Nationality Act 1981 are encoded in
`legalese/l4-ide` and have not been deposited here yet.

*(This paragraph read "Empty at this writing" until 2026-08-25, by which point three
subjects had landed. A README that describes a directory it no longer matches is worse
than none, because it is believed.)*

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
