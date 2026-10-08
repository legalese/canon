# Penal Code 1871 (Singapore), the whole Code — row `legalese-whole-code`

A draft encoding of the whole Penal Code 1871 (443 sections encoded, 42 deferred for time), made in one 45-minute run of nine agents and built to the charge generator's contract (`legalese/l4-ide` `ts-apps/charge-generator`).
It was made to measure how compatible a whole-Code encoding would be with that consumer, not to wire it up.
It sits beside two other rows of the same Code: `legalese` (twelve modules, hand-built, with a bench of reported charges) and `legalese-aswathy` (the whole Code, 45 modules, eight verification passes).
Rows are equal; none is primary.

**Status: draft, not reviewed by a lawyer.** Revised once, on 30 September 2026 (filed here on 8 October): defects found by comparing the encoding with the ladder diagrams in Alex Woon's *Essential Criminal Law* were fixed, each checked against the Code's text. See "Revised 2026-09-30" below.

## Where things are

- `*.l4` — 27 encoding modules and 9 tests modules. `pc-domain.l4` holds the shared nouns and `pc-general.l4` holds Chapter 2, the `Punishment` and `Charge` records and the shared helpers; every other module imports both.
- `check.sh` — runs every module and counts errors, satisfied and failed assertions. `l4 run` exits 0 when an `#ASSERT` fails, so read its counts, not an exit code.
- `notes/PLAN.md` — the conventions every encoder followed.
- `notes/<group>-coverage.md` — every section in the group's chapters, with its disposition and function names.
- `notes/<group>-forks.md` — every ambiguity met, the readings, the one taken and why.
- `generators/` — several groups generated their modules or tests with scripts, kept here. Paths inside them are absolute to the machine they ran on (`/Users/mengwong/...`); a hand edit to a generated `.l4` is lost if its generator is re-run.
- The source text is the subject's `registers/source-bundle/PC1871.txt` (SSO, "Current version as at 09 Sep 2026"); this row read that file byte for byte (sha256 `066301837e6413cf…`).

Run: workflow `sg-penal-code-encode`, run `wf_16958398-5ba`, session `pipeline` (6c6da87c), 2026-09-26.
Nine Opus agents at high effort: one ontology agent, then eight chapter-group encoders in parallel.
About 45 minutes, 3.0M subagent tokens, 472 tool calls.
Toolchain: the `l4` prerelease `unstable-20260926-c76e6b0` (legalese/prereleases), `JL4_LIBRARY_PATH` unset. Canon has no CI: these counts are a point-in-time record from that build.

## Checked after the run, by the integrator rather than the encoders

Every module was run again after the workflow returned, counting `DiagnosticSeverity_Error` lines and the anchored `Message: assertion satisfied|failed` lines.
The counts are from 2026-10-08, after the revision of 30 September, on the same toolchain: `check.sh` for the last three columns, `grep -c '^#ASSERT'` for the first.
At filing the totals were 1,314 / 1,312 / 2 / 2; the revision added 78 assertions, to body-a (146 to 179), exceptions (153 to 175) and property (195 to 218).

| tests module | #ASSERT | satisfied | failed | errors |
| --- | --- | --- | --- | --- |
| pc-general-tests.l4 | 115 | 115 | 0 | 0 |
| pc-general-part-tests.l4 | 167 | 165 | 2 | 2 |
| pc-exceptions-tests.l4 | 175 | 175 | 0 | 0 |
| pc-state-public-tests.l4 | 151 | 151 | 0 | 0 |
| pc-justice-order-tests.l4 | 92 | 92 | 0 | 0 |
| pc-body-a-tests.l4 | 179 | 179 | 0 | 0 |
| pc-body-b-tests.l4 | 123 | 123 | 0 | 0 |
| pc-property-tests.l4 | 218 | 218 | 0 | 0 |
| pc-documents-defamation-tests.l4 | 172 | 172 | 0 | 0 |
| **total** | **1,392** | **1,390** | **2** | **2** |

The 27 encoding modules have 0 errors each (and had 0 warnings at filing); 36 `.l4` files and 49,519 lines in all (47,973 at filing).
At filing, every figure matched what its encoder reported.

**The two failures are findings about the Code, left red on purpose.**
Both were checked against the source text:

- **s 118's Illustration is stale** (fork GP-14). It says concealing a design to commit gang-robbery is punishable under s 118, which needs "an offence punishable with death or imprisonment for life". s 395 now punishes gang-robbery with 5 to 20 years and caning, so on the current text those facts fall under s 120.
- **s 512(4)'s Illustration treats attempted robbery under s 512** (fork GP-10). s 512(2) applies only "where no express provision is made", and s 393 makes express provision for attempted robbery.

## Coverage

Every section number in the Code's table of contents has a row in some group's coverage note: nothing is silently absent.
Taking each section's best disposition across groups:

| disposition | sections |
| --- | --- |
| encoded | 443 |
| inert (definitions and text that is not a rule) | 29 |
| repealed | 72 |
| deferred for time | 42 |

**The 42 deferred sections**, by group:

- body-a (10): 301, 304B, 304C, 308A, 310, 311, 314, 315, 316, 335A.
- body-b (32): 372, 373, 373A, 376B–376H, 377, 377B, 377BB–377BO, 377C. The body-b encoder named voyeurism (377BB), the intimate-image offences (377BD, 377BE), sexual exposure (377BF) and child abuse material (377BG–377BK) as the most charged of these.

**344 punishing provisions** have the charge generator's four items (facts record, defining predicate, `offence under s N`, `charge under s N`), every one `@export`ed with `@desc`: general-part 10, state-public 76, justice-order 85, body-a 56, body-b 19, property 67, documents-defamation 31. The exceptions group has none by design: Chapters 4 and 4A create no offence. It exports 18 `exception under s N` ladders and a roll-up instead.

**179 forks** are registered across the nine `*-forks.md` notes: 174 at filing, and five added by the revision of 30 September (F-20, E-17, P-22, P-23, P-24).

## What integration changed

**Nine helpers were defined in more than one group**, with the same name and the same body: the age tests (below 12, 14, 16, 18 and 21; above 18), `5 or more persons`, `to wit` and `the to-wit clause`.
Each module ran alone, but a module importing two groups could not call the helper: "There are multiple definitions for the identifier" (probed with `pc-body-a-life` + `pc-exceptions-general`).
The one definition of each now lives in `pc-general.l4` under "Shared helpers, hoisted at integration", and the copies are gone from ten group modules.
After the move, all 27 non-test modules import together into one file with 0 errors, the helpers evaluate, and the counts in the table above are unchanged.

**The generators were patched to match**, because four groups generate their modules and a re-run would otherwise restore the duplicates.
State-public (`generators/state-public/`), property, justice-order and body-a were each re-run after the patch, and each reproduced the integrated deposit byte for byte.
The last three had been written to a session scratchpad; the copies in `generators/` are the patched ones. `generators/other/` holds further test-fixture scripts found there; which encoder wrote each is not recorded.

**Ruled.** "above 18 years of age" (s 87; s 300 Exception 5) means 18 or over: Meng, 2026-09-26, "yes 18 or older" (forks F-10 and E-9).

## Revised 2026-09-30

Eight modules changed (`pc-body-a-hurt`, `pc-body-a-life`, `pc-body-a-tests`, `pc-exceptions-private-defence`, `pc-exceptions-tests`, `pc-property-cheating`, `pc-property-tests`, `pc-property-trust`), with their generators and the body-a, exceptions and property notes.
Each change was found by that comparison and checked against the Code's text, and each has tests; forks F-20, E-17 and P-22 to P-24 record the reasoning.

- **s 300 Exception 7.** The abnormality of mind and its listed cause are leaves of their own, required before limbs (a)(i), (a)(ii) and (b). An intoxicated accused with no abnormality of mind no longer comes within the Exception on (a)(ii) alone.
- **s 300 Exception 2 reads Chapter 4A.** `Homicide Facts` carries a `Private Defence Facts`, and the flat "exceeds the power" leaf is replaced by `the right of private defence was exceeded`, so the Exception and the private-defence rules can no longer disagree.
- **Chapter 4A is decided in two stages:** whether the right arose (the kind of act, s 99, its start, s 98(2), s 106A), and whether it extends to the act (continuance, extent, s 98(1)). The answers under s 96 are unchanged. Where continuance and s 98(2) belong is fork E-17, which wants a ruling.
- **A grievous hurt is a hurt.** `causes hurt` reads s 320, and the s 321 fault reads the leaf for aiming at grievous hurt.
- **The murder refusal names each Exception that applies.**
- **s 405's last limb** ("intentionally suffers any other person to do so") is split into leaves: the accused suffers another person, that person acts dishonestly, which of the four acts that person does, and, for use or disposal, the violation. The charge names the other person, so "to do so" always has its antecedent. Whose dishonesty the limb needs is fork P-22, open for a ruling.
- **s 409(1)(b) and (g)** take the trade, role or body as a string particular and recite it (P-23); **s 419**'s recital names the mode of personation.
- **s 415 Explanation 1:** the `deceived the victim` `@desc` carries Poh Yuan Nie v PP [2022] SGCA 74 (P-24). No logic changed.
- **New tests** include the Exception 4 proviso, which no Illustration covers.

**Consumers keyed on field names need migrating:** `CBT Facts` loses one field and gains thirteen, and `Homicide Facts` loses three and gains five (`private defence`, and four for Exception 7).

## Not done, and worth knowing before anyone relies on this

- **No independent test pass.** Every test was written by the agent that wrote the code it tests. justice-order is the thinnest: 92 tests for 85 offences.
- **Not a cleanroom.** Encoders read Meng's 12-module drafts row as the pattern for the charge generator's contract.
- **The charge generator's catalogue is not updated, by choice.** The run was to measure how compatible a whole-Code encoding would be, not to wire it up (Meng, 2026-09-26). Each coverage note proposes its `OFFENCES` rows and family slugs.
- **28 proposed shared nouns** (24 from the encoders, 4 from the ontology agent: weapon, dwelling-house, animal, age helpers and others) are listed in the reports and not merged into `pc-domain.l4`; the age helpers are the part integration has done.
