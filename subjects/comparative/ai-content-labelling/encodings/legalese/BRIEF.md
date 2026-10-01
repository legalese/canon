# Encoding brief: AI-content labelling across three authorities, in L4

You are producing an L4 encoding of the rules that require AI-generated or AI-altered media to be marked or disclosed, in three jurisdictions, from their sources.
This brief is the whole specification.
Read it fully before opening any source.

## The subject

Three bodies of enacted law, plus one voluntary code, answering one question about one piece of content: **must it be marked or disclosed, by whom, and is the marking it carries enough?**

- **European Union.** Regulation (EU) 2024/1689 (the Artificial Intelligence Act), Article 50, as amended by Regulation (EU) 2026/1744 (the "digital omnibus"), which replaced Article 50(7) and added Article 111(4).
  Beside it, the **Code of Practice on Transparency of AI-Generated Content** (final, 10 June 2026), a voluntary code under Article 50(7) that the Commission and the AI Board have confirmed is "an adequate voluntary tool".
  The Commission's **Guidelines** of 20 July 2026, C(2026) 5054, are an interpretive aid only.
- **Washington.** Engrossed Second Substitute House Bill 1170, Chapter 167, Laws of 2026, which takes effect on 1 February 2027.
- **California.** Business and Professions Code, Division 8, Chapter 25 (the California AI Transparency Act), ss. 22757.1–22757.6, **as amended by SB 1000**, approved on 30 September 2026 as an urgency statute in effect on approval.
  Section 22757.3.1 (large online platforms) is AB 853's text, which SB 1000 does not amend.

| instrument | source file under `INPUTS_DIR` | plain text under `INPUTS_DIR/text/` |
| --- | --- | --- |
| AI Act as published | `eu-ai-act-2024-1689-oj.xhtml` | `eu-ai-act-2024-1689.txt` |
| Regulation 2026/1744 | `eu-omnibus-2026-1744-oj.xhtml` | `eu-omnibus-2026-1744.txt` |
| Code of Practice | `eu-code-of-practice-transparency-2026-06-10.pdf` | `eu-code-of-practice-2026-06-10.txt` |
| Commission Guidelines (aid) | `eu-guidelines-art50-2026-07-20.pdf` | `eu-guidelines-art50-2026-07-20.txt` |
| Washington E2SHB 1170 | `wa-e2shb-1170-session-law-2026.pdf` | `wa-e2shb-1170-2026.txt` |
| California SB 1000 (enrolled = as approved) | `ca-sb1000-2026-enrolled.html` | `ca-sb1000-2026-enrolled.txt` |
| California AB 853 | `ca-ab853-2025-chaptered.html` | `ca-ab853-2025-chaptered.txt` |

The `.xhtml`, `.html` and `.pdf` files are authoritative; the `.txt` files are mechanical extractions for searching and quoting, and where they disagree the original wins.
`INPUTS_DIR/sources.json` records the URL, fetch date and sha256 of each.
The Guidelines are **not law**; use them only to name the judgement a fact-supplier must make, never to make it.

### Vintages

| instrument | vintage | in force | status in this encoding |
| --- | --- | --- | --- |
| California ss. 22757.1, 22757.3, 22757.5 | SB 942 as amended by AB 853 | 2 August 2026 to 29 September 2026 | **not encoded**: a question about a date in that window must `REFUSE` with a reason naming the window |
| California ss. 22757.1, 22757.3, 22757.5 | as amended by SB 1000 | from 30 September 2026 | encoded |
| EU Article 50(7) | as published, then as replaced by 2026/1744 | replacement in force 27 July 2026 | only the replacement matters to the questions here, and only as context |

The date of the question is an input to every rule, never `TODAY`.

## Scope — pinned, do not widen or narrow

**EU.** AI Act Art. 3(3) "provider", 3(4) "deployer", 3(60) "deep fake"; Art. 50(2); Art. 50(4), both subparagraphs; Art. 111(4) as added by 2026/1744; Art. 113 (application from 2 August 2026).
Code of Practice Section 1, **Measure 1.1** only (its two layers, Sub-measures 1.1.1 and 1.1.2, and its two single-layer cases).
Out of scope: Art. 50(1), 50(3), 50(5), 50(6); the rest of the Code (Measures 1.2–1.4, Commitments 2–4, and all of Section 2, the deployers' icon); penalties.

**Washington.** Sections 1, 2, 3(2), 5 and 9.
Out of scope: s.3(1) (trade secrets), s.4 (enforcement), s.6 (government agencies' chatbot disclosure, a different duty), ss.7–8 (codification).

**California, as amended by SB 1000.** Section 22757.1 (the definitions the other sections use), 22757.3(a), 22757.3.1, 22757.5, 22757.6.
Out of scope: 22757.2 (the verification tool), 22757.3(b)–(d) (licensees, assistive-technology misrepresentation), 22757.3.2 (hosting platforms), 22757.3.3 (capture devices), 22757.4 and 22757.4.1 (penalties).

## The questions the encoding must answer

For a single piece of content, on a given date:

1. **EU 50(2):** must the provider of the AI system that generated or manipulated it ensure it is marked; and, where the provider adheres to the Code, does the marking it carries meet Measure 1.1?
2. **EU 50(4):** must a deployer disclose that it is artificially generated or manipulated, and if so, fully or in the limited form for artistic, creative, satirical, fictional or analogous works?
3. **Washington s.2:** must the covered provider include provenance data; and is the provenance data it carries deemed to meet s.2(2)?
4. **California 22757.3(a):** must the covered provider include a latent disclosure; and does the disclosure the content carries convey the five items in 22757.3(a)(1)(A)–(E)?
5. **California 22757.3.1:** for a large online platform distributing it, what must the interface disclose under (a)(2)(B)(i)–(iii)?

Then a **census**: run a set of scenarios through all five and report where the jurisdictions give different answers for the same content.

## Deliverables, all under `DEPOSIT`

1. `.l4` modules with ASCII filenames:
   - one **domain** module of nouns only, imported by everything else;
   - one module per instrument (EU Article 50, the Code's Measure 1.1, Washington, California);
   - a **census** module that imports all of them;
   - tests modules.
2. Tests whose expected values come from the source: every limb of every exception, both sides of every date, each item on each minor-modification list. Assert refusals with `#ASSERT REFUSED … BECAUSE "…"`.
3. **Fixtures** from real signed C2PA files: the facts each file's manifest states, extracted mechanically by a script from `c2patool`'s JSON output, with every non-manifest fact of each scenario written beside it by hand and labelled as such.
4. `NOTES.md` with a coverage table (every provision above, with its disposition), a fork register, the census table, and the numbers `check.sh` prints.
5. `check.sh`, from the `encoding-a-subject` skill.

## Rules that matter

- **Encode isomorphically**, and cite the provision on every rule (`@ref` or a comment).
- **An evaluative standard is an input, never a computation.** These are judgements, and each is a `BOOLEAN` field named in the statute's own words, supplied by the caller:
  - EU 50(2): whether the AI system "perform[s] an assistive function for standard editing", and whether it "do[es] not substantially alter the input data provided by the deployer or the semantics thereof". The Guidelines (paras 90–92) say the second "requires a case-specific assessment".
  - EU 3(60): whether the content "would falsely appear to a person to be authentic or truthful".
  - EU 50(4): whether the content "forms part of an evidently artistic, creative, satirical, fictional or analogous work or programme".
  - Washington s.2(4): whether an alteration is "a significant change that substantially alters the data in content", where it is not on the list of minor modifications.
  - Washington s.2(1) and (2): "to the extent commercially and technically reasonable".
  - California 22757.3(a): "to the extent it is technically feasible", and whether the disclosure "is permanent or extraordinarily difficult to remove or tamper with".
- **The two minor-modification lists are not the same, and the difference is the point.** California's 22757.1(l) is a closed list of eight ("means any of the following"). Washington's s.2(4) is open ("Minor modifications include:") and adds "applying filters" and "resampling". Encode each as its source wrote it. Never share one list between them.
- **What a C2PA manifest says is evidence about the content, not a judgement.** Do not infer any of the judgements above from manifest fields.
- **Where the sources do not answer, `REFUSE "…"`**: never `FALSE`, `0` or a plausible default.
- **A failing assertion is a finding.** Never edit an expected value to match what the code computed.
- **Read the diagnostics, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails.
- Dates: `IMPORT daydate`; write literals as `YMD year month day`.

## Toolchain

The binary is `~/.local/bin/l4`, built from l4-ide `unstable` on 30 September 2026, after the last change to the language on 28 September.
Leave `JL4_LIBRARY_PATH` unset.
`l4 check FILE` typechecks; `l4 run FILE` also evaluates every `#EVAL` and `#ASSERT`.
`c2patool` 0.27.22 (from the `contentauth/c2pa-rs` release `c2patool-v0.27.22`) reads manifests.
