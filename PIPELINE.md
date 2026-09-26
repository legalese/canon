# The pipeline, and where it actually lives

**This repository holds encodings. It does not hold the pipeline.** The pipeline is in
`legalese/l4-ide`: specified in `specs/todo/single-instruction-demo/SPEC.md`, driven by
`etc/go/go.sh`, and documented by two skills that are the entry points for using it:

| skill | for |
|---|---|
| `.claude/skills/running-the-l4-pipeline/` | running a subject through P0-P10, reading statuses and verdicts, granting or waiving a gate, auditing somebody else's run |
| `.claude/skills/writing-l4-rules/` | writing the L4 itself: encoding a statute, regulative rules, `IS`/`MEANS`/`IF` |

Read those before starting work. Their own references are authoritative over anything here:
`references/phases.md` (what P0-P10 are), `references/status-vocabulary.md` (the eight statuses,
five oracle classes and four run verdicts) and `references/gates.md` (HG1 and HG2).

> **Correction, 2026-09-23.** The first version of this file (commit `2d9489d`) described a
> five-stage pipeline of its own invention and stated that HG2 "was defined nowhere". Both were
> wrong: the pipeline is P0-P10 with eight statuses and four verdicts, and both gates have been
> specified in SPEC.md §7.3 all along. That version is superseded by this one. It was written
> without reading the two skills, which is the mistake worth not repeating.

## The two gates, as specified

Both use `ssh-keygen` detached signatures over a payload built **from a run's journal** by
`etc/go/gate-request.sh`, and verified by `etc/go/gate-verify.sh` against
`specs/todo/single-instruction-demo/gate-allowed-signers`. An agent may verify a signature and may
never make one.

**HG1 — fidelity.** After P5, a domain expert certifies that the inert-style L4 is isomorphic to
the source: reviewable section by section against it. Namespace `l4-go-gate`. In the driver it
blocks `p6-tests`, every projection leg and `p9-report`. It **may** be waived with a recorded
reason (`--waive HG1="…"`), because that work is often reviewed by other means.

**HG2 — anything outward-facing.** Meng agrees to a specific act other people will see: creating a
corpus-of-law repository, publishing the conversion report, any lexipedia contact. Namespace
`l4-go-gate-hg2`, so an HG1 signature cannot be replayed as an HG2 one. It blocks `p10-publish`.
**HG2 cannot be waived** — `go.sh run --waive HG2=…` exits 2, enforced by the driver rather than by
documentation.

Nothing is enrolled: `gate-allowed-signers` ships with no public key, so every gated stage refuses
with exit 3 until someone enrols one. That is the shipped state, not a fault.

A waiver is a verdict with a reason attached, never an absence: it lands on the journal and prints
in the report's Gates section. Signatures and waivers both bind to content — edit any module of the
encoding and the gate re-opens.

### Smoke test of the signing mechanics, 2026-09-23

Run in a scratch directory with a **disposable** key, never a project key, because no agent should
hold one. A good signature verified; a tampered payload, a signer absent from the allowed-signers
file, and a wrong namespace were each rejected; and the digest check failed when a covered file was
edited. The mechanism behaves as `references/gates.md` describes. Note HG2's namespace is
`l4-go-gate-hg2`, not `l4-go-gate`.

## How this repository relates to a pipeline run

A run is about a **subject sidecar** in l4-ide at `etc/go/subjects/<id>/` — its `subject.json`,
`pins.json`, `known-defects.json` and `NOTES.md`. As at 2026-09-23 the committed sidecars are
`regcf`, `sg-succession` and `dog-act-1976`.

This repository's `subjects/<jurisdiction>/<subject>/` directories are the corpus side: source
bundle, L4 modules, registers, reports. A subject here is **not** automatically a pipeline subject —
a corpus with no sidecar is never the subject of a run, the same rule that makes `bna` and
`charities-cleanroom` non-subjects in l4-ide.

To take something here through the pipeline: register a sidecar (`etc/go/go.sh new-subject …`),
declare only the projection legs that subject genuinely supports, then `doctor`, `plan`, `run`.

## The tracker's stage names are not the pipeline's

`tools/topics/encoding-progress.xlsx` and `tools/review-queue.py` use Indexed → Source text →
AI pass #1 → Human pass #1 → AI pass #2 → Human pass #2. That is a **project-management** view, for
deciding which of 700-odd Acts a human should look at next. It is not P0-P10, it produces no
receipts, and "Done" in a spreadsheet cell is not a status in the sense `status-vocabulary.md`
means. Keep the vocabularies apart: a pipeline status is a function of bytes on disk, written by
`receipt.mjs`, and nothing else may assert one.

## Legislative quality assurance

The corpus-side artifacts an LQA job produces — incident register, coverage register, conversion
report — belong in the subject directory here. The discipline is that **every finding is traceable
to a provision and reproducible by machine**: an incident that cannot be demonstrated by an
assertion or a worked scenario is an opinion, not a finding. Findings that turn out to be sound
drafting are kept and marked verified-no-defect, because knowing what was checked is part of the
result.

Releasing any of it — sending findings to a ministry, a regulator or a drafting office, or
publishing them — is an HG2 act, and HG2 has no waiver route.

**Where the authoritative text is not in the language the encoders worked in**, HG1 needs care the
shipped machinery does not supply: the payload names corpus files, not a translation chain. The
Israeli subjects are the live case — Hebrew governs, the consolidated text is unofficial, and an
English working translation is an aid only. An HG1 signer must have read the Hebrew, because
certifying an encoding against a translation certifies the translation. Put that in the subject's
`NOTES.md`, where a subject's idiosyncrasies belong.
