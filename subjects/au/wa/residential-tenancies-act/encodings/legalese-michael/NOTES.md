# Notes: Residential Tenancies Act 1987 (WA)

Sourced directly from the official Word (.docx) export on
[legislation.wa.gov.au](https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_a693.html)
(`mrdoc_49316`), not via the Legal Data Hunter mirror used for the rest of the
`western-australia/` corpus — this was the first subject in this corpus, encoded before the
bulk pull, and deliberately pulled from the primary source to establish the extraction
method (`.docx` → `word/document.xml` → plain text) later reused for the bulk pull.

## Encoding (draft, v0.6.0)

L4 files sit next to this note. They type-check. `#EVAL` / `#ASSERT` / `#TRACE`
directives in each rules file are the golden cases.

| File | Source |
| --- | --- |
| `types.l4` | s.3 occupancy facts used by the s.5 application test |
| `part-i-preliminary.l4` | s.3 (residential premises / residential tenancy agreement), s.4, s.5 (including s.5(4) holiday deeming, s.5(5) caravan-park sites, s.5(6) residential-park carve-out), s.6 as a fact |
| `part-iv-rent-and-bonds.l4` | s.27, s.27AA, s.28, s.29(1) and s.29(4)(b) lodgement, s.30, s.31A, s.31B |
| `part-v-termination-notices.l4` | s.60 (exhaustive termination list; interest vs agreement), s.61-70A notices |
| `part-v-division-2a-family-violence.l4` | s.71AA-71AE family-violence interest termination |
| `part-iv-quiet-enjoyment-and-entry.l4` | s.44 quiet enjoyment; s.46 lessor's right of entry |
| `part-iv-pets-and-modifications.l4` | s.50A-50E, 50J-50R pets and modifications |
| `part-v-division-4-court-orders.l4` | s.71-75, 73A court termination and possession (s.71(2)(c)/(3A)/(3B) social-housing gates included) |
| `part-v-division-3-social-housing.l4` | s.71A-71J social housing termination notices |
| `part-iv-form-and-standard-terms.l4` | s.27A-27C; s.38-43, 45(2), 48, 49A, 49, 50 |
| `part-v-abandonment.l4` | s.76A-76B abandonment notices |
| `part-5a-security-bond-release.l4` | s.81C-81K bond release (application, partial, entitlements, notice, agree, dispute, refer, pay) |
| `part-iii-retaliatory.l4` | s.26A-26B retaliatory action |
| `part-v-holding-over-and-possession.l4` | s.76C, 76, 80 |
| `part-vi-contracting-out.l4` | s.82 |
| `part-via-databases.l4` | s.82E listing |

Cross-Act meanings (strata lease, residential park, approved provider, prescribed amounts) are taken as facts. This encoding does not re-state those other Acts or the regulations.

The operational core of the Act is encoded. Left unencoded on purpose: Part II administration, Part III Divisions 1-2 court procedure, remaining Commissioner pet/modification machinery (s.50F-50H, 50S-50ZE), Part IV Division 3 general offences (s.51-59F), abandoned goods/documents and mortgagee/superior title (s.77-81), Part 5A payment-after-referral (s.81L-81T), remaining database quality rules (s.82F-82K), and Part 7 transitional.
