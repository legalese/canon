# canon

**A corpus of L4 encodings of existing legal text.**

Every entry here is a body of law — a statute, a regulation, a contract form — encoded in
[L4](https://github.com/legalese/l4-ide), the language for law, together with the evidence
that the encoding is faithful: section-by-section citations back to the source, scenario
tests, ambiguity registers recording every interpretive choice, projections to executable
industry standards (DMN, BPMN), and a signed human review.

From the _canons of construction_ to the construction of canon: where the interpretive
tradition leaves construction implicit in a reader's judgement, an entry here carries its
construction on its face — which reading was taken at each ambiguous site, on what argument
or authority, and what turns on the difference.

**Status (2026-08-02): scaffold.** The repository shape below is ruled and fixed
(single-instruction demo spec, ruling R1); the first subjects arrive with the pipeline's G4
milestone. Nothing here yet claims to be a reviewed encoding.

## Layout: one class, many instances

```
subjects/
  <subject-id>/          one body of law
    subject.json         the descriptor: sources, corpus modules, projections, version
    NOTES.md             this subject's idiosyncrasies, in prose
    SOURCE-LICENSE.md    the terms the quoted legal text carries (see Licensing)
    *.l4                 the encoding
    cases/               dated scenario cases with expected values, machine-evaluated
    projections/         emitted DMN / BPMN / other artifacts, with fidelity reports
    registers/           fork register · external-modification register · source bundle
    report/              the conversion report
    gates/               HG1/HG2 grant artifacts — signatures and waivers (see Gates)
```

The layout is a **class/instance** design: the generic "⟨body of law⟩: go" template (the
subject-sidecar shape) is the class; each encoding job is an instance expected to veer, and
its divergences are recorded in its own `NOTES.md` — never by forking the template.

## Status vocabulary

Every subject declares exactly one of:

| status                   | meaning                                                                        |
| ------------------------ | ------------------------------------------------------------------------------ |
| `draft`                  | the encoding exists; no claim of fidelity is made                              |
| `adversarially-reviewed` | machine gates passed; independent adversarial review completed                 |
| `reviewed`               | a named domain expert has signed HG1: the encoding is isomorphic to its source |

## Versioning: two axes, deliberately separate

The **encoding version** (semver, in `subject.json`) numbers the encoding itself — it
increments when the L4 changes. The **law-time axis** is inside the encoding: L4's
`EVAL UNDER RULES EFFECTIVE AT` evaluates any entry under the rules effective at a chosen
date, so amended regimes are dated arms in one artifact, not forked files. An encoding at
version 2.1.0 can still answer questions about the law as it stood in 2016.

## Gates: human sign-off you can verify yourself

Review here is not a badge; it is a **detached SSH signature over a content digest** of the
reviewed files. Each subject's `gates/` directory carries the signed payload, the signature,
and the `allowed_signers` entry. To verify one:

```
ssh-keygen -Y verify -f gates/allowed_signers -I <signer> -n l4-go-gate \
  -s gates/HG1.payload.sig < gates/HG1.payload.txt
```

A signature binds to content — edit the encoding and the grant visibly no longer verifies.
Waivers, where used, are equally on the record: a waiver is a verdict with a reason attached,
never an absence. Agents can verify signatures; they cannot make them.

## Licensing

- **Everything authored here** — encodings, cases, schemas, harnesses, reports — is licensed
  under [Apache-2.0](LICENSE).
- **Quoted legal text carries its own terms**, recorded per subject in `SOURCE-LICENSE.md`
  and attributed in [NOTICE](NOTICE). United States federal material is in the public domain
  (17 U.S.C. § 105 and the edicts-of-government doctrine); United Kingdom legislation is
  quoted under the [Open Government Licence v3](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
  with attribution.
- **Prose artifacts** (conversion reports, commentary, comparison notes) may additionally be
  offered under CC-BY-4.0 where a subject's `SOURCE-LICENSE.md` says so, so they can flow
  into attribution-share-alike wikis without ShareAlike reaching the encodings.

## Tooling

Encodings here are produced and checked by the pipeline in
[legalese/l4-ide](https://github.com/legalese/l4-ide) — the `etc/go/` orchestrator, whose
subject sidecars mirror this repository's layout. This repository holds law; that one holds
tools.
