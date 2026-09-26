# HG1 — waived, not signed

**Status: WAIVED, not reviewed.** No signature exists over `HG1.payload.txt`. Per
`docs/directory-conventions.md` §4.2, `status` in `encoding.json` states what is claimed for
this row: `draft`, not `reviewed` — `reviewed` requires a named domain expert's signature, and a
waiver is explicitly not that.

**Who waived, when, why** (quoted verbatim from the go pipeline's journal, run
`2026-09-21-430aa01d-002`, `produced_under.reason`):

> waived by Meng, 2026-09-21 — does not have time to review; corpus PASS on p6-tests
> (848/848), p7-catala PASS, p8-verify's four findings dispositioned in NOTES §6.1, no
> self-review substitute intended

`HG1.payload.txt` beside this file is the payload that was waived — its file hashes pin the
corpus at commit `1dd165f9c` in `legalese/l4-ide`, branch `miles-card` (merged to `unstable`
via PR legalese/l4-ide#439, merge commit `9c93a028a`). The payload's own digest is
`sha256:f196078d4df3e9426265e760884b3ad03b0529417daae0e1877ad8b05e5e0cbd`.

**What a waiver does and does not mean.** It means Meng, who owns this corpus, chose not to
spend his own time checking the encoding's isomorphism to the issuers' T&Cs before it landed
here, and said so on the record rather than silently skipping the step or having the encoding
session sign its own work. It does not mean the encoding is wrong, and it does not mean it is
right: the machine gates (`p6-tests`, `p7-catala`, structural `p3-check`) passed and are
independent evidence, but none of them is HG1 — HG1 is specifically the claim that a human
compared the rules against the source text and found them isomorphic, and that claim was
never made. Anyone relying on this encoding for an actual purchase decision should read
`../NOTES.md` and `../ACCEPTANCE-TRIAGE.md` rather than trust the `draft` status alone.

If HG1 is later granted, this file should be replaced by `allowed_signers` +
`HG1.payload.sig`, matching `subjects/us/regcf/`'s shape, and `encoding.json`'s `status`
should move to `reviewed`.
