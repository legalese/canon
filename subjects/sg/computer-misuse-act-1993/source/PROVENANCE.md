# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| *(not deposited)* `Computer Misuse Act 1993.pdf` | Singapore Statutes Online PDF, footer "Current version as at 07 Oct 2026 / PDF created date on: 07 Oct 2026", 26 pages; downloaded from the SSO website by the user and copied to the working machine on 2026-10-07. Kept out of the repository, as for the other subjects the user supplied. | `1c7f57adf47c68895e070de5c63ca06222a45357cea8966566a5aaa3055e2619` |
| `CMA1993.txt` | the PDF's text layer, extracted with `pypdf` 6.19.0 in plain (non-layout) mode, 814 lines; the encoding's line references are to this file | `0c4d61728dfb517859fada7363638983c45167417241454490ddbe1defa64dde` |

- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative.
- **In force as at**: 7 Oct 2026 (the banner). 2020 Revised Edition (in operation 31 December 2021), with later amendments marked in the text: Act 16 of 2023 (Computer Misuse (Amendment) Act 2023) wef 8 Feb 2024, which added ss 8A-8B and the First Schedule; and Act 21 of 2025 (Criminal Law (Miscellaneous Amendments) Act 2025) wef 30 Dec 2025, which added scam offences (Second Schedule) and caning.
- **How it was retrieved**: downloaded by hand from SSO by the user (2026-10-07).
- **Earlier deposit**: `../registers/source-bundle/CMA1993.txt` was fetched by the bulk ingestion on an earlier date and is kept as it was; this `source/` copy is the one the encoding cites.

## Extraction notes

- Repeated page footers ("Singapore Statutes Online Current version as at …") and the Table of Contents are in the text and are not part of the Act.
- Bracketed numbers after a section (e.g. "[8A") are the pre-2020 section numbers, markers rather than text; the Comparative Table maps them.
- **Instrument it is made under**: none; a primary Act. Regulations prescribing compoundable offences (s 16(2)) and Gazette notifications under s 2(1) are not in the source.

## Extraction script

```python
import sys, pypdf
r=pypdf.PdfReader(sys.argv[1])
sys.stdout.write("\n".join(p.extract_text() for p in r.pages))
```
