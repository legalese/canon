# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| *(not deposited)* `Income Tax Act 1947.pdf` | Singapore Statutes Online PDF, footer "Current version as at 06 Oct 2026 / PDF created date on: 06 Oct 2026", 1,118 pages; downloaded from the SSO website by the user and copied to the working machine on 2026-10-06. Kept out of the repository, as for the other subjects the user supplied. | `247e691a0411e3ee501652c9c98f243b98f810d0c5691b2ae4814360f13f03ab` |
| `ITA1947.txt` | the PDF's text layer, extracted with `pypdf` 6.19.0 in plain (non-layout) mode, 38,370 lines; the encoding's line references are to this file | `0af28999c0af3f49e125cd0406bcb78e24a489d6c5c9ae10de8ae15c8ebd0ef5` |

- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative.
- **In force as at**: 6 Oct 2026 (the banner). 2020 Revised Edition (in operation 31 December 2021), with later amendments marked in the text, among them Act 33 of 2022, Act 30 of 2023, Act 2 of 2024, Act 30 of 2024 (Platform Workers Act 2024), Act 35 of 2024, Act 36 of 2024 (MMT Act consequentials, wef 20 March 2025), Act 46 of 2024, Act 25 of 2025 (wef various dates to 8 December 2025) and Act 17 of 2026.
- **How it was retrieved**: downloaded by hand from SSO by the user (2026-10-06).

## Formulas the text layer does not carry

The PDF prints 135 formulas as images (from page 49 onwards), which SSO's Terms of Use cl.6 exclude from the reproduction grant, so none is deposited. Those the encoding relies on are transcribed here from the PDF; the others belong to provisions the encoding carries as text or takes as inputs.

| where | PDF page | the formula as printed |
| --- | --- | --- |
| s 14(6B)(a) | 263 | **A + B** |
| s 14(6B)(b) | 263 | **C + D** |
| s 14D(1) | 286 | **(U + V) × A%** |
| s 14D(1A) | 288 | **T × 150%** |
| s 14E(2)(b) | 299 | **A × B / C** |
| s 14EA(1) | 300 | **A × 400%** |
| s 14ZG(1) | 400 | **A × 300%** |
| s 37R(4) | 735 | **A × 20%** |

## Extraction notes

- Repeated page footers ("Singapore Statutes Online Current version as at …") are in the text and are not part of the Act.
- Section headings sometimes wrap onto a second line in the text layer (for example "Remission of tax for companies for year of assessment 2025 and" / "companies" before s 92L); the heading text is as printed.
- The Second Schedule's three tables, the Fifth Schedule (child relief), the Sixth Schedule (working lives) and the Twelfth Schedule (net tonnage) were checked row by row against the PDF text.
- **Instrument it is made under**: none; a primary Act. The Income Tax rules and regulations (prescribed rates, limits, relief caps, SRS contribution caps, compoundable offences) are not in the source.
