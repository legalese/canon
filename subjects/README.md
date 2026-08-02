# subjects/

One directory per body of law. Empty at this writing — the first subject (`regcf`,
SEC Regulation Crowdfunding, 17 CFR Part 227) arrives with the pipeline's G4 milestone,
with the British Nationality Act 1981 to follow.

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
