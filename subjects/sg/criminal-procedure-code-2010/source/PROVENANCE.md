# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| `CPC2010.pdf` | Singapore Statutes Online PDF of the Criminal Procedure Code 2010, footer "Current version as at 01 Oct 2026 / PDF created date on: 01 Oct 2026"; 480 pages; supplied from the user's folder `SG Acts/Criminal Procedure Code 2010.pdf` on 2026-10-01 | `0d61a66c6943b146071797bf7033d983768097e7b4acb08dcfe11032d7b1a2ec` |
| `CPC2010.txt` | `pdftotext -layout` of the PDF (23,233 lines), in a single-byte (Latin-1) encoding and **not UTF-8**: read it with that encoding. Line references in the modules' comments are to this file | `e848278a32ea10e20321fef9e819de0e754d122be4836d34759b26724b052597` |

- **Act**: Criminal Procedure Code 2010 (Act 15 of 2010), Singapore.
- **URL**: https://sso.agc.gov.sg/Act/CPC2010
- **Retrieved**: 2026-10-01 (the PDF's own created date). How it was fetched is not known to the encoder.
- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative. **A current (revised) version**: the "2020 Revised Edition", which "incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021", with marginal amendments after that date (the First Schedule's latest: Act 10 of 2025 wef 15/09/2026, Act 21 of 2025 wef 17/08/2026, S 42/2026 wef 30/01/2026).
- **Legislative history**: the PDF ends with SSO's Legislative History, which "is not part of the Act". The Code commenced on 2 January 2011. The First Schedule was amended by G.N. No. S 664/2011 and by the later Acts and orders listed in the marginal notes after the table.
- **Instrument it is made under**: none; it is a primary Act. Acts it points at, above all the Penal Code 1871, were **not** fetched here; the Penal Code has its own subject, `sg/penal-code-1871`.
- **The First Schedule is read from the PDF, not from the text file.** `pdftotext -layout` scrambles the table (stacked section numbers drift away from their rows). `encodings/generators/first_schedule_extract.py` reads the PDF's text spans by position and writes `first_schedule_rows.json`. NOTES.md section 7 gives the checks run.
- **Extraction artefacts**: the layout text prints the dash in "CHAPTER n -- ..." and the apostrophe in "Magistrate's Court" as a single non-UTF-8 byte (the generator maps both); the page footer is repeated on every page.
