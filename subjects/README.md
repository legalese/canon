# subjects/

One directory per jurisdiction, then one directory per body of law inside it.

| jurisdiction | contents |
| ------------ | -------- |
| [`western-australia/`](western-australia/) | Western Australian Acts |
| [`european-union/`](european-union/) | European Union Regulations and Directives |
| [`singapore/`](singapore/) | Singapore Acts |
| [`commonwealth-of-australia/`](commonwealth-of-australia/) | Commonwealth of Australia Acts |
| [`new-south-wales/`](new-south-wales/) | New South Wales Acts |
| [`victoria/`](victoria/) | Victorian Acts -- **not openly licensed; metadata only** until permission is obtained |
| [`queensland/`](queensland/) | Queensland Acts |
| [`south-australia/`](south-australia/) | South Australian Acts |
| [`tasmania/`](tasmania/) | Tasmanian Acts |
| [`new-zealand/`](new-zealand/) | New Zealand Acts and Bills |
| [`united-kingdom/`](united-kingdom/) | United Kingdom Acts (Westminster) |
| [`australian-capital-territory/`](australian-capital-territory/) | Australian Capital Territory Acts |
| [`northern-territory/`](northern-territory/) | Northern Territory Acts -- conditional permission; confirm before quoting text |
| [`united-states/`](united-states/) | United States federal Acts (public domain) |
| [`california/`](california/) | California code divisions (public domain) |
| [`new-york/`](new-york/) | New York Consolidated Laws articles |
| [`texas/`](texas/) | Texas code chapters |
| [`canada/`](canada/) | Canadian federal Acts -- English and French equally authoritative; conditional permission |
| [`ontario/`](ontario/) | Ontario statutes -- English and French equally authoritative; conditional permission |
| [`british-columbia/`](british-columbia/) | British Columbia statutes (King's Printer Licence) |
| [`india/`](india/) | Indian central Acts -- no reuse licence; not independently spot-checked |
| [`ireland/`](ireland/) | Irish Acts (Oireachtas PSI Licence, CC BY 4.0) |
| [`south-africa/`](south-africa/) | South African Acts -- **licence unclear; metadata only** until resolved |
| [`hong-kong/`](hong-kong/) | Hong Kong ordinances -- **not openly licensed; metadata only**; English and Chinese equally authentic |

`regcf` (SEC Regulation Crowdfunding, 17 CFR Part 227) arrives with the pipeline's G4
milestone, with the British Nationality Act 1981 to follow.

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
