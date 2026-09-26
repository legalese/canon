# singapore/

Singapore Acts, one subject-id per body of law, following the subject-sidecar shape described
in [`subjects/README.md`](../README.md).

- `penal-code-1871` is encoded (v0.9.0, draft).
- Twenty subjects were laid out on 2026-09-22 for the Acts that govern twelve everyday topics
  -- payroll, leave, termination, pensions, government benefits, personal tax, insurance
  claims, utility billing, passenger compensation, consumer matters, customs and duties, and
  work permits. The mapping and the check of each Act against Singapore Statutes Online are in
  `tools/topics/`. They hold metadata only.

Source text is fetched by `tools/fetch-sso-corpus.py`, which uses the same directory names and
`subject.json` shape, and which runs only in the 03:00 to 07:00 SGT window that SSO's Terms of
Use (cl.13(d)(i)) set for automated extraction.
