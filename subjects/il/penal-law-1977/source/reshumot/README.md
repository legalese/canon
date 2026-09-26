# Reshumot deposits — the Penal Law's gazette trail

The 241 gazette issues that the Open Book of Laws cites as the Penal Law's amendment trail,
fetched from `reshumot.justice.gov.il` on 2026-09-16. **The PDFs are not in this repository**
(64.7 MB); they are in Meng's `~/Dropbox/Documents/papers/israel-reshumot/penal-law-1977/`,
named `<series>-<issue>-<date>.pdf`. What is here is the record that lets them be re-fetched
and checked:

| file | what it is |
| --- | --- |
| `reshumot-issues.json` | one entry per issue: AKN expression path, date, the instruments the Open Book cites in it, SHA-256 and size of the PDF, and `unwrapped_from` on the 165 that arrived inside a multipart upload envelope (see below) |
| `citation-lookup.json` | the 284 Open Book citations (year, page, label, Knesset PDF link) and how each resolved to an issue: 230 by year+page filter, 51 by title fallback, 3 unresolved |
| `envelope-defect-repro.sh`, `envelope-defect-transcript.txt` | reproduction of the site defect found on the way: every OCR-processed issue (165/165 ABBYY outputs, 0/76 born-digital) is served as the raw `multipart/form-data` request body around the PDF, +186 bytes. Report: <https://claude.ai/artifact/4gRFbzM8yDTwoU8KGZRm1D> |

The site is geo-blocked outside Israel (Radware, country rule); the fetch ran through an EC2
instance in `il-central-1`. The Reshumot API is documented in the l4-ide session memory
`reshumot-akn-api.md`; there is no AKN XML for gazette issues, only PDF.
