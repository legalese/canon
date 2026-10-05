# Inputs — provenance

Every quotation in this encoding is copied from the `.txt` files in this directory.
Each `.txt` was produced mechanically from the official Word (`.docx`) file by `docx2txt.py` (in this directory), which concatenates the `w:t` runs of each paragraph and keeps tabs.
Nothing was retyped.

All files were fetched from the Western Australian Parliamentary Counsel's Office site, `https://www.legislation.wa.gov.au`, on **2026-10-05 between 10:24 and 10:28 UTC**, by plain HTTPS GET (no archive fallback was needed).
The download URL for each document is `https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=<mrdoc>.<ext>`.

| file here | role | instrument | version (in-force from) | official file | sha256 of the official file |
| --- | --- | --- | --- | --- | --- |
| `cat-act-2011.txt` | **authoritative** (official consolidation) | Cat Act 2011, No. 55 of 2011 | 00-l0-01, current from **25 Sep 2025** | `mrdoc_48898.docx` (102 648 bytes) | `5321f420afaeaf66a4dd7e137a6d32993e277dcb79d532c6c362c2b97b60fb50` |
| `cat-regulations-2012.txt` | **authoritative** (official consolidation) | Cat Regulations 2012 | 02-b0-00, current from **24 Jul 2025** | `mrdoc_48735.docx` (126 366 bytes) | `ae3baa53a091d8f9633743f248e35e65163cb55e9634aa1de31faec0273da578` |
| `interpretation-act-1984-extract.txt` | authoritative extract — time computation and "Act" | Interpretation Act 1984 s 5 (five definitions), ss 61–62 | 07-k0-00, current from 18 Dec 2025 | `mrdoc_49111.docx` (99 704 bytes) | `dd0630f2444da30505b082c20300fb08f47ff163d18c9d74a0cf9ab905dc046a` |
| `local-government-act-1995-extract.txt` | authoritative extract — the only "working day" definition in the LG Act | Local Government Act 1995 Sch 4.1A cl 1 | 07-at0-01, current from 26 Jun 2026 | `mrdoc_49599.docx` (588 903 bytes) | `61f585fb776c11c406ec95db7747c4b764d4b2b97d8d1850477ffe14f88665ed` |

The Act and Regulations `.docx` files are byte-identical (same sha256) to the copies already filed at `../../registers/source-bundle/mrdoc_48898.docx` and `mrdoc_48735.docx` in this subject, fetched by another encoder on 2026-09-07; the PDF and HTML renderings of the same versions were also fetched and hashed:

| rendering | sha256 |
| --- | --- |
| Act `mrdoc_48898.pdf` | `277ce56c538aa60fd8b9c8bdf04e04feb7e5e20311fb987b1f5db2abb4c8ebf0` |
| Act `mrdoc_48898.htm` | `12de1e5628d3e909fb4c759791489a16aa109f06b3732164718a7a65faf071a4` |
| Regulations `mrdoc_48735.pdf` | `998771be09ab5d954dd32d1a7b84708f934a2b70a2b2ab9b43122f02d192cefb` |
| Regulations `mrdoc_48735.htm` | `64a618c6c2eda7c6d749d33541aac938fd41f8580cd03f6612abef75560b023b` |

## In-force statements

- **Act.** The WA site lists consolidation 00-l0-01 as "Currency start 25 Sep 2025, Currency end Current".
  Its uncommenced-provisions table names two amending instruments not yet in force: the *Dog Amendment (Stop Puppy Farming) Act 2021* ss 50–61 ("To be proclaimed"), and the *Evidence Act 2025* s 492(1) (18 Sep 2027).
  The second only replaces the words "Evidence Act 1906" with "Evidence Act 2025" in Cat Act s 75(3) — checked against the as-passed text at `../../../cat-act-2011-lqa/sources/evidence-act-2025.as-passed.mrdoc_48825.txt` lines 4741–4762 (a source file, not an encoding). It changes no computed answer.
  The first is not reproduced in the consolidation and was not fetched; see NOTES.md, open questions.
- **Regulations.** Consolidation 02-b0-00, "Currency start 24 Jul 2025, Currency end Current". The last amendment is SL 2025/138 (reg 6). There are no uncommenced amendments listed.

## Licence

Both consolidations carry: "© State of Western Australia 2025. This work is licensed under a Creative Commons Attribution 4.0 International Licence (CC BY 4.0)." See `../SOURCE-LICENSE.md`.

## What was not fetched

- Earlier versions of either instrument. This encoding states the law as in force from 25 September 2025; it does not answer for earlier dates (see NOTES.md).
- The *Public and Bank Holidays Act 1972* and the list of WA public holidays. Public holidays are an input.
- The Dog Act 1976, the Animal Welfare Act 2002 and the Veterinary Practice Act 2021, which the Cat Act refers to. A conviction under one of them, and whether a person is a veterinarian or veterinary nurse, are inputs.
- The *Cat Amendment (Local Laws) Bill 2026* — out of scope by instruction.

## Consulted, not encoded

The *Cat (Uniform Local Provisions) Regulations 2013* are out of scope, but they are also "regulations made under this Act", so they could prescribe something the Act leaves to be prescribed.
They were fetched (consolidation 00-a0-05, current from 1 Nov 2013; `mrdoc_25294.docx`, sha256 `62b13ca9c6d9b805250590fe72c9a1d977ce1c0a99649ee738c850bb01fa2a40`, 2026-10-05 10:31 UTC — byte-identical to `../../registers/source-bundle/mrdoc_25294.docx`) and read **only** to establish what they prescribe under the Act's own provisions.
They prescribe nothing under ss 18(2)(c), 23(3), 34(2)(b), 37(2)(f), 37(5) or 49(1)(c); they make one local-law offence (their reg 6(1)) a prescribed offence for s 62(1). See NOTES.md.
