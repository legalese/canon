# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| *(not deposited)* `Child Development Co-Savings Act 2001.pdf` | Singapore Statutes Online PDF, footer "Current version as at 07 Oct 2026 / PDF created date on: 07 Oct 2026", 148 pages; downloaded from the SSO website by the user and copied to the working machine on 2026-10-07. Kept out of the repository, as for the other subjects the user supplied. | `12309e52b8bbb36e44c423faf147733415d43aa0228a5b4da93bc24c5fcf83b6` |
| `CDCSA2001.txt` | the PDF's text layer, extracted with `pypdf` 6.19.0 in plain (non-layout) mode, 5,098 lines; the encoding's line references are to this file | `232d98915aedeee9e0d374f1ffc4f66dc43ad288b8ceecc1c47434b1ad54ac83` |

- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative.
- **In force as at**: 7 Oct 2026 (the banner). 2020 Revised Edition (in operation 31 December 2021), with later amendments marked in the text, the latest Act 30 of 2024 (Platform Workers Act 2024) wef 1 Jan 2025 and Act 46 of 2024 wef 1 Apr 2025 (shared parental leave for April 2025 Scheme children, ss 12DA-12DD and the Second Schedule; 4 weeks' paternity leave).
- **How it was retrieved**: downloaded by hand from SSO by the user (2026-10-07).
- **Earlier deposit**: `../registers/source-bundle/CDCSA2001.txt` was fetched by the bulk ingestion on an earlier date and is kept as it was; this `source/` copy is the one the encoding cites.

## The formulas the text layer does not carry

These are printed as images, which SSO's Terms of Use cl.6 exclude from the reproduction grant, so they are not deposited. Transcribed from the PDF:

| where | text layer | the formula as printed |
| --- | --- | --- |
| s 12DD(1)(b) | "calculated in accordance with the formula  unless that allocation is varied" (PDF page 79) | **M / 2** |
| s 12JA(2)(d)(ii)(B) | "calculated in accordance with the formula where P is $2,500 and W is the number of reimbursable days per week" (PDF page 103) | **P / W** |
| First Schedule Part 1 item 2 | "where T is the total number of work days in the fixed number of weeks ... W is the fixed number of weeks" (PDF page 129) | **T / W** |
| First Schedule Part 1 item 3 | "where T is the total number of work days in the period of 3 weeks immediately preceding the applicable date" (PDF page 130) | **T / 3** |

## Extraction notes

- Repeated page footers ("Singapore Statutes Online Current version as at …") and the Table of Contents are in the text and are not part of the Act.
- Bracketed numbers after a section (e.g. "[8A") are the pre-2020 section numbers, markers rather than text; the Comparative Table maps them.
- **Instrument it is made under**: none; a primary Act. The Child Development Co-Savings Regulations (the Scheme, prescribed periods, claims, reductions) and the Employment Act 1968 provisions it applies are not in the source.

## Extraction script

```python
import sys, pypdf
r=pypdf.PdfReader(sys.argv[1])
sys.stdout.write("\n".join(p.extract_text() for p in r.pages))
```
