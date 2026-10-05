# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| `AA1928.pdf` | Singapore Statutes Online PDF of the Apportionment Act 1928, footer "Current version as at 05 Oct 2026 / PDF created date on: 05 Oct 2026"; supplied by the user as an upload on 2026-10-05 | `eef6774eb6014ce0702c0fa6ceec52797ecca7d6858b9bfe1887091b5c978eaf` |
| `AA1928.txt` | the PDF's text layer, extracted with `pypdf` 6.19.0 in layout mode (the script reproduced below; 250 lines). The encoding's line references are to this file | `9b3ce6a5798009dc58be9c187dce6b7cd1df668ae0a48f1bf69fe3fd26b03898` |

- **Status**: unofficial consolidation (SSO Terms of Use cl.8). Not authoritative.
- **In force as at**: 5 Oct 2026 (the banner). The text states itself as the 2020 Revised Edition, which "incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021".
- **History**: Legislative History lists no amending Act: Ordinance 25 of 1928 and six revised editions (1936, 1955, 1970, 1985, 1998, 2020). The Legislative History "is not part of the Act".
- **How it was retrieved**: uploaded to the session by the user on 2026-10-05. How the PDF was obtained from SSO was not stated.
- **Extraction artefacts**: repeated page footers and the Table of Contents are in the text, which is not part of the Act.
- **Instrument it is made under**: none; it is a primary Act.
- **Earlier deposit**: `../registers/source-bundle/AA1928.txt` was fetched by the bulk ingestion on an earlier date and is kept as it was; this `source/` copy is the one the encoding cites.

## Extraction script

```python
import sys, pypdf
r=pypdf.PdfReader(sys.argv[1])
out=[]
for i,p in enumerate(r.pages):
    out.append(p.extract_text(extraction_mode="layout"))
sys.stdout.write("\n\f\n".join(out))
```
