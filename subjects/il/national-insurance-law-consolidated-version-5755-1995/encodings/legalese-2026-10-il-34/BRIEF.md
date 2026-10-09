# Encoding brief: National Insurance Law, the contributions surroundings, in L4 (row IL-34)

Row IL-34, run id `IL-34-20261008`, encoder `enc-il-34` (one session, no sub-agents).
This brief restates the lead's task (message of 2026-10-09 and `enc-brief.txt`) in the template of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`.
It was pinned from the row and the lead's message; it was written down after the priority 1 to 3 modules had landed, and NOTES.md says what each provision came to.

## The subject

**חוק הביטוח הלאומי [נוסח משולב], התשנ״ה–1995**, the National Insurance Law [Consolidated Version], 5755-1995, as consolidated on Hebrew Wikisource (unofficial; the Hebrew is authoritative), deposited at `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`, sha256 `78bf47ee29a300d51c5c7646cf85992d7de78aa1380bd8460a4a18265f552a97`.
Read with it, each deposited:

| instrument | file | sha256 |
| --- | --- | --- |
| National-Civic Service Law, 5774-2014 (Wikisource revision 3002360, 2026-04-01) | `../../../national-civic-service-law-5774-2014/registers/source-bundle/national-civic-service-law-5774-2014.he.wiki.txt` | `ed0a31aeae4474a9cd97d4f940e6406070cff5f72a0db1f1c88257605a06546f` |
| National Insurance (Reduced Rates of Insurance Contributions) Order, 5759-1999 | `../../registers/source-bundle/regulations/national-insurance-reduced-rates-of-insurance-contributions-order-5759-1999.he.wiki.txt` | `f91c3b20909bdd67e3c6135554449a0f9f393e4db732470ece542c2a72f0f007` |
| National Insurance (Payment and Deduction of Contributions from an Insured Person Working for Different Employers) Regulations, 5757-1997 | `../../registers/source-bundle/regulations/national-insurance-payment-and-deduction-from-employee-of-several-employers-regulations-5757-1997.he.wiki.txt` | `8c25330765dc4e7c58476dd77440f5d62e5163a8b69f3e68bb2f171580b77103` |
| National Insurance Law (Amendment No. 252 and temporary provision), Sefer HaChukim 3347 p. 176 | `../../registers/source-bundle/amending-laws/25_lsr_5482787.pdf` | `d6c450ca0b869d1edb036b0f96bffbd79be6670336d9b5aa888da6cf2ecc8904` |
| 2025 Budget-year Law, Sefer HaChukim 3384 p. 386 ff. (ss 19 to 21: National Insurance) | `../../registers/source-bundle/amending-laws/25_lsr_6133485.pdf` | `eba7e1fa570a3ece265d87f379543024da038ee51af3f959d4c74162f5edecfa` |

## Why this row exists

Rows IL-04, IL-05 and IL-08 (the NII half) record, as gaps, the provisions around the ones they encode.
The capstone `employed-parent-monthly-net` takes their results as inputs (its `GAPS.md` items on the contributions surroundings).
The lead released the gaps on 2026-10-08 (SHRUG: "do IL-25 to IL-36").
This row encodes the ones that are contributions law, in the lead's priority order, and never edits another row.

## Scope, in priority order (pinned)

1. **s 348(e)'s expiry and the National-Civic Service Law** (IL-05's fork 05-Q7): whether the 31.8.2026 expiry that s 348(e)'s temporary text follows was moved.
2. **s 341 and the Order of 5759-1999; s 342(e) and Schedule K1.**
3. **The several-employers regulations of 5757-1997** (the regulations made under s 342(e)).
4. **Schedule A1 Parts A, B, C, E.** Encoded by row IL-33 (its `nii-schedule-a1-ages.l4`, which its own BRIEF pins); not duplicated here (NOTES.md, coverage table).
5. **The remaining sections:** ss 2, 28 (with 28A and 28B), 32, 336, 340 (with 340A), 343, 344 (with 344A), 345 (with 345A and 345B), 346, 347, 349, 350 (with 350A), 351, and Schedules A and K16 (the schedule s 350A reads).
6. **The Institute's charge on yeshiva students** (IL-05's open question 3): no text found; refused by name.

Not in scope, and not touched: ss 334, 337, 342, 348, 335 and Schedule J, K and A1 Part D (rows IL-04, IL-05, IL-08); ss 29 to 31 and 33 to 36 (not named by the row); s 352 (not named); s 369 beyond (a) (Schedule K1 is read through s 369(a) only).

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, each starting `@lang en`: one nouns module (`DECLARE` only), one rules module per section or instrument, tests modules, and four modules of row IL-04 vendored unchanged with their sha256 (`VENDORED.sha256`).
2. `NOTES.md`: scope, coverage table (no row left `deferred`), fork register (each fork "ruled by Meng 2026-10-08 (SHRUG)"), answer table, `check.sh` output, open questions, inputs the capstone does not supply today, needs-a-source list.
3. `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`, `tools/` (`srcquote.py` and `hebcheck.py` from row IL-06, `hebcheck.py` changed to skip the `ext:` lines this row writes; `extquote.py`, new, for quotations of the instruments other than the Law).

## Rules that matter

- **Policy for every ambiguity (Meng, SHRUG, 2026-10-08):** where the text is silent or two readings are arguable and give different answers to a question someone would ask, one named switch, default DECLINE (a refusal by name saying the text does not decide), the other readings kept by name and tested; the default declines only where the readings give different answers to the question asked.
- **Never invent a number.** A figure that is only published elsewhere is an input with its source, or a marked module; this row publishes none of its own.
- **Where the sources do not answer, `REFUSE "…"`,** never `FALSE`, `0` or a plausible default.
- **A provision that needs a text not deposited** is refused by name and recorded as "needs a source" (the 1972 Order on recognised employers; the Income Tax deduction regulations; the Collection Regulations; the Minister's orders; any amendment of the Civic Service Law after 2026-04-01).
- **Tests:** every expected value worked by hand from the Hebrew before the run, the arithmetic beside it; both sides of every threshold and date; a failing assertion is a finding.
- **Semi-cleanroom against the Axiom Foundation:** no RuleSpec, tests, ENCODING-GAPS, manifests or "Comparison with Axiom" section was read.
- **Git is read-only;** the lead commits.

## Toolchain

`/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset; `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
The binary's sha256 is recorded before and after each check run (NOTES.md, "What check.sh prints").
