# Notes — blind-guarded-2026-08

**Status: `experimental`.** Read
[`../blind-inert-2026-08/NOTES.md`](../blind-inert-2026-08/NOTES.md) first — it carries everything
about the subject: that the instrument is synthetic and was never law, that the source text was
modified (the benefits section excised, the age threshold moved), that there is no insuring clause,
and how the blind protocol worked. None of that is repeated here.

## Why this row exists

It is the **second, independent encoding** of the same policy — a different agent, a different house
style (guarded rows rather than inert quotation), blind both to the benchmark answer key and to the
inert encoding beside it. Canon's `encodings/<encoder>/` structure treats rows as equal with none
primary, which is exactly right here: the two were produced to be *compared*, not ranked.

The comparison is mechanised. l4-ide's §8 diff oracle pairs this module against the inert one and
evaluates both sides over a shared battery, reporting divergences rather than a winner.

## What you must know before quoting anything from it

**It carries no `#ASSERT` at all.** Every assertion for this subject lives in the inert row. So:

- any test count for this file is **zero**, and
- the l4-ide pipeline reports its test stage **DEGRADED** for precisely that reason — "no failed
  assertion" over an empty result set is vacuous, and the stage refuses to call it a pass.

Do not read the absence of failures here as evidence of anything.

**It was ranked third of three** on isomorphism by the reviewing auditors. It is deposited because
an independent second encoding is evidence, not because it is the better artifact. If you want the
reference encoding, take the inert row.

**It reaches the same nine answers** as the other two arms — including the same unanimous
disagreement with the published key on Q4.

## Goldens

Point-in-time, as with the sibling row: canon has no CI and these modules sit outside l4-ide's corpus
globs, so nothing regenerates or re-checks them here.
