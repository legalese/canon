# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| *(not deposited)* `Work Injury Compensation Act 2019.pdf` | Singapore Statutes Online PDF, footer "Current version as at 06 Oct 2026 / PDF created date on: 06 Oct 2026", 143 pages; downloaded from the SSO website by the user and copied to the working machine on 2026-10-06. Kept out of the repository at the user's instruction. | `004f6aa01f0e3a87dbf723282a06c78662f40d29a92e7cf11e7d156d67f68364` |
| `WICA2019.txt` | the PDF's text layer, extracted with `pypdf` 6.19.0 in plain (non-layout) mode, 4,835 lines; the encoding's line references are to this file | `dcaccfd28fa35b505a0b1f45dd9b1eac1ceb41315e4b1da06706c437e771a8c3` |

- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative.
- **In force as at**: 6 Oct 2026 (the banner). 2020 Revised Edition, with later amendments marked in the text: Act 30 of 2024 (Platform Workers Act 2024) wef 15 Oct 2024 and 1 Jan 2025; G.N. No. S 694/2025 (First and Fifth Schedule amounts) wef 1 Nov 2025; G.N. No. S 751/2025 (Second Schedule) wef 1 Dec 2025; and earlier ones listed in the Legislative History.
- **How it was retrieved**: downloaded by hand from SSO by the user (2026-10-06).

## The three formulas the text layer does not carry

Three formulas are printed as images, which SSO's Terms of Use cl.6 exclude from the reproduction grant, so they are not deposited. Transcribed from the PDF:

| where | text layer | the formula as printed |
| --- | --- | --- |
| First Schedule para 6(1) | "the employee's AME is computed according to the formula  where —" | **A / P** |
| First Schedule para 6(2) | "the employee's AME is computed according to the formula  where —" | **(D × W × 52) / 12** |
| Fifth Schedule Part 3 para 6(1)(c) | "computed according to the formula  , where —" | **E / P** |

## Extraction notes

- Unlike the bulk ingestion's earlier deposit (`../registers/source-bundle/WICA2019.txt`, whose Tables A and B lost rows at page breaks), this extraction carries every row of Tables A and B in both the First and Fifth Schedules: ages "14 and below" to "66 and above", 53 rows each. Checked row by row.
- Repeated page footers ("Singapore Statutes Online Current version as at …") are in the text and are not part of the Act.
- **s 39 is printed with two subsections (2)**: the substituted text (Act 30 of 2024), with paragraphs (a) and (b) for employees and platform workers, followed by the earlier one-sentence subsection (2). This is in the SSO PDF itself, not an extraction artefact; the encoding follows the newer text, which contains the older.
- **Fifth Schedule Part 3 para 5(1)(b)** reads "per accident per employee" in a Schedule about platform workers. Encoded as per accident per platform worker; see the encoding's NOTES.md.
- **Instrument it is made under**: none; a primary Act.
