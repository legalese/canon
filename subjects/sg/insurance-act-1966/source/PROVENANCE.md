# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| *(not deposited)* `Insurance Act 1966.pdf` | Singapore Statutes Online PDF, footer "Current version as at 07 Oct 2026 / PDF created date on: 07 Oct 2026", 233 pages; downloaded from the SSO website by the user and copied to the working machine on 2026-10-07. Kept out of the repository, as for the other subjects the user supplied. | `48dc5a767c905cad6842f0590002622783989cf96e4a68715255aa7d15356f17` |
| `IA1966.txt` | the PDF's text layer, extracted with `pypdf` 6.19.0 in plain (non-layout) mode, 7,820 lines; the encoding's line references are to this file | `640acbffb6f2531a868bc587a8008155ad61758287ddad1579731d609bed3d97` |

- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative.
- **In force as at**: 7 Oct 2026 (the banner). 2020 Revised Edition (in operation 31 December 2021), with later amendments marked in the text, among them Act 18 of 2022 (Financial Services and Markets Act 2022, in stages to 31 July 2024), Act 12 of 2024 (investigation powers, Part 3 Division 2A, wef 24 Jan 2025), Act 37 of 2024 (s 33A, wef 18 Nov 2024) and Act 5 of 2025 (s 137(2A), wef 9 Mar 2025).
- **How it was retrieved**: downloaded by hand from SSO by the user (2026-10-07).
- **Earlier deposit**: `../registers/source-bundle/IA1966.txt` was fetched by the bulk ingestion on an earlier date and is kept as it was; this `source/` copy is the one the encoding cites.

## The formulas the text layer does not carry

Printed as images, which SSO's Terms of Use cl.6 exclude from the reproduction grant, so not deposited. Transcribed from the PDF:

| where | text layer | the formula as printed |
| --- | --- | --- |
| s 133(5)(c) | "such share to be calculated as follows: where A is that surviving nominee's original portion ..." (PDF page 174) | **A / B × C** |
| s 150(11)(b) | "must be calculated as follows: where A is the amount which would have been payable in respect of that claim had it been paid in full ..." (PDF page 194) | **A / B × C** |

## Extraction notes

- Repeated page footers ("Singapore Statutes Online Current version as at …", "Informal Consolidation") and the Table of Contents are in the text and are not part of the Act.
- Bracketed numbers after a section (e.g. "[35ZN") are the pre-2020 section numbers, markers rather than text; the Comparative Table maps them.
- **Instrument it is made under**: none; a primary Act. The Insurance Regulations (financial requirements, fund solvency, capital adequacy, fees, prescribed amounts under s 150, compoundable offences) are not in the source.

## Extraction script

```python
import sys, pypdf
r=pypdf.PdfReader(sys.argv[1])
sys.stdout.write("\n".join(p.extract_text() for p in r.pages))
```
