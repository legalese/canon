# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| `MDA1973.pdf` | Singapore Statutes Online PDF of the Misuse of Drugs Act 1973, footer "Current version as at 01 Oct 2026 / PDF created date on: 01 Oct 2026"; 160 pages; supplied from the user's folder `SG Acts/Misuse of Drugs Act 1973.pdf` on 2026-10-01 | `2585dbce58874ed46f7f1a4929a642f5a917bf0413e32d2e603f3ca9d923d248` |
| `MDA1973.txt` | a layout-preserving text extraction of the PDF (7,951 lines, ASCII only). The extraction tool is not recorded; the file is a reading aid and the PDF governs. Line references in the modules' comments are to this file | `2031d1c83a8cb0c474f5edf43a6928ffc48e025132c8d27fe0b0875ffb091508` |

- **Act**: Misuse of Drugs Act 1973, Singapore.
- **URL**: https://sso.agc.gov.sg/Act/MDA1973
- **Retrieved**: 2026-10-01 (the PDF's own created date). How it was fetched is not known to the encoder.
- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative. **A current (revised) version**: the "2020 Revised Edition", which "incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021", with marginal amendments after that date (the latest in the text: Act 9 of 2026 wef 01/05/2026 and G.N. S 321/2026 wef 1 June 2026).
- **Legislative history**: the PDF ends with SSO's Legislative History, which "is not part of the Act". It is not encoded.
- **Instrument it is made under**: none; it is a primary Act. Regulations made under it, and the Acts it points at (the Criminal Procedure Code 2010, the Penal Code 1871, the Evidence Act 1893), were **not** fetched here; those three have their own subjects, `sg/criminal-procedure-code-2010`, `sg/penal-code-1871` and `sg/evidence-act-1893`.
- **The First Schedule's substances are not read.** The Schedule names about 140 Class A substances, about 20 Class B and about 20 Class C (and further chemical families by structure); the encoding takes the CLASS of a drug as an input and does not carry the lists. The Second Schedule's table is read from the text and generated into `mda-second-schedule.l4` by `encodings/generators/mda_schedule.py`; NOTES.md section 7 says how it was checked.
