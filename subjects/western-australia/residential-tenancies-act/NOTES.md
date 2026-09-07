# Notes: Residential Tenancies Act 1987 (WA)

Sourced directly from the official Word (.docx) export on
[legislation.wa.gov.au](https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_a693.html)
(`mrdoc_49316`), not via the Legal Data Hunter mirror used for the rest of the
`western-australia/` corpus — this was the first subject in this corpus, encoded before the
bulk pull, and deliberately pulled from the primary source to establish the extraction
method (`.docx` → `word/document.xml` → plain text) later reused for the bulk pull.

## Encoding (draft, v0.1.0)

L4 files sit next to this note. They type-check. `#EVAL` / `#ASSERT` / `#TRACE`
directives in each rules file are the golden cases.

| File | Source |
| --- | --- |
| `types.l4` | s.3 occupancy facts used by the s.5 application test |
| `part-i-preliminary.l4` | s.3 (residential premises / residential tenancy agreement), s.4, s.5 (including s.5(4) holiday deeming, s.5(5) caravan-park sites, s.5(6) residential-park carve-out), s.6 as a fact |
| `part-iv-rent-and-bonds.l4` | s.27, s.27AA, s.28, s.29(1) and s.29(4)(b) lodgement, s.30, s.31A, s.31B |

Cross-Act meanings (strata lease, residential park, approved provider, prescribed amounts) are taken as facts. This encoding does not re-state those other Acts or the regulations.

Not yet encoded: Part II, Part III, the rest of Part IV (form of agreement, standard terms, pets, modifications), Part V termination, Part 5A bond release, and later Parts.
