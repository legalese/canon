# NOTES — sg/pdpa-2012, encoding row `legalese`

**Status: `draft`, and the sidecar is deliberately incomplete.** This row is a *rescue
deposit* on the `mengwong/drafts` branch, not a finished encoding job. It exists so the
work has a home with a path and a licence note instead of sitting untracked in a checkout
that is being retired.

## Provenance

`pdpa-dbno.l4` was found untracked (dated 2026-06-11) in `~/src/legalese-l4-ide`, an old
parallel clone of `legalese/l4-ide` being decommissioned. It was verified to exist nowhere
else — not on `unstable`, not in any `l4wt/` worktree — which is why it was rescued here
rather than dropped.

Its own header describes it as a "modern-L4 transcription of the legacy *LegalSS*
spreadsheet encoding" of PDPA Part VIA.

## What it is

A hybrid constitutive + regulative encoding of the data-breach notification regime:

- **Ontology** — the First Schedule Part 1 categories of prescribed personal data.
- **Constitutive rules** — what makes a breach a *Notifiable Data Breach* (§26A, §26B and
  its significant-harm / significant-scale limbs), and the derived duties to notify the
  PDPC and affected individuals (§26D).
- **Regulative rules** — two phases: ASSESS (§26C(2), 30 days) and NOTIFY (§26D, 3 days),
  as deontic obligations on the organisation.
- **Scenario tests** and a regulative trace of the happy path.

## What it does *not* have

Recorded plainly so no reader infers more than is there:

- **No law-time axis.** There are no dated arms and no
  `EVAL UNDER RULES EFFECTIVE AT` coverage; the encoding reads as a single vintage of the
  text and cannot answer as-at questions. Part VIA has been amended-into rather than
  amended, so this is a gap to fill, not a claim that the text never moved.
- **No `cases/`, `projections/`, `registers/`, `report/`, or `gates/`.** The scenario tests
  are inline in the `.l4`, not lifted into machine-evaluated dated case rows; nothing has
  been projected to DMN or BPMN; there is no fork register recording its interpretive
  choices, and there is no human review — HG1 has not been sought and no signature exists.

## What has been checked

`l4 check pdpa-dbno.l4` **succeeds** against the compiler at l4-ide `unstable` as of
2026-08-08 (`JL4_LIBRARY_PATH` pinned to `jl4-core/libraries`; the residual warnings are
prelude's own `WHEN EMPTY` exhaustiveness notes, not this file's). That is a statement
about typechecking only. **No claim of fidelity to the Act is made.**
