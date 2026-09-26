# Penal Code 1871 (Singapore), the whole Code — row `legalese-whole-code`

A draft encoding of the whole Penal Code 1871 (443 sections encoded, 42 deferred for time), made in one 45-minute run of nine agents and built to the charge generator's contract (`legalese/l4-ide` `ts-apps/charge-generator`).
It was made to measure how compatible a whole-Code encoding would be with that consumer, not to wire it up.
It sits beside two other rows of the same Code: `legalese` (twelve modules, hand-built, with a bench of reported charges) and `legalese-aswathy` (the whole Code, 45 modules, eight verification passes).
Rows are equal; none is primary.

**Status: draft, not reviewed by a lawyer.** Refinement is planned from the ladder diagrams in Alex Woon's *Essential Criminal Law*.

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

| tests module | #ASSERT | satisfied | failed | errors |
| --- | --- | --- | --- | --- |
| pc-general-tests.l4 | 115 | 115 | 0 | 0 |
| pc-general-part-tests.l4 | 167 | 165 | 2 | 2 |
| pc-exceptions-tests.l4 | 153 | 153 | 0 | 0 |
| pc-state-public-tests.l4 | 151 | 151 | 0 | 0 |
| pc-justice-order-tests.l4 | 92 | 92 | 0 | 0 |
| pc-body-a-tests.l4 | 146 | 146 | 0 | 0 |
| pc-body-b-tests.l4 | 123 | 123 | 0 | 0 |
| pc-property-tests.l4 | 195 | 195 | 0 | 0 |
| pc-documents-defamation-tests.l4 | 172 | 172 | 0 | 0 |
| **total** | **1,314** | **1,312** | **2** | **2** |

The 27 encoding modules have 0 errors and 0 warnings each; 36 `.l4` files and 47,973 lines in all.
Every figure matches what its encoder reported.

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

**174 forks** are registered across the nine `*-forks.md` notes.

## What integration changed

**Nine helpers were defined in more than one group**, with the same name and the same body: the age tests (below 12, 14, 16, 18 and 21; above 18), `5 or more persons`, `to wit` and `the to-wit clause`.
Each module ran alone, but a module importing two groups could not call the helper: "There are multiple definitions for the identifier" (probed with `pc-body-a-life` + `pc-exceptions-general`).
The one definition of each now lives in `pc-general.l4` under "Shared helpers, hoisted at integration", and the copies are gone from ten group modules.
After the move, all 27 non-test modules import together into one file with 0 errors, the helpers evaluate, and the counts in the table above are unchanged.

**The generators were patched to match**, because four groups generate their modules and a re-run would otherwise restore the duplicates.
State-public (`generators/state-public/`), property, justice-order and body-a were each re-run after the patch, and each reproduced the integrated deposit byte for byte.
The last three had been written to a session scratchpad; the copies in `generators/` are the patched ones. `generators/other/` holds further test-fixture scripts found there; which encoder wrote each is not recorded.

**Ruled.** "above 18 years of age" (s 87; s 300 Exception 5) means 18 or over: Meng, 2026-09-26, "yes 18 or older" (forks F-10 and E-9).

## Not done, and worth knowing before anyone relies on this

- **No independent test pass.** Every test was written by the agent that wrote the code it tests. justice-order is the thinnest: 92 tests for 85 offences.
- **Not a cleanroom.** Encoders read Meng's 12-module drafts row as the pattern for the charge generator's contract.
- **The charge generator's catalogue is not updated, by choice.** The run was to measure how compatible a whole-Code encoding would be, not to wire it up (Meng, 2026-09-26). Each coverage note proposes its `OFFENCES` rows and family slugs.
- **28 proposed shared nouns** (24 from the encoders, 4 from the ontology agent: weapon, dwelling-house, animal, age helpers and others) are listed in the reports and not merged into `pc-domain.l4`; the age helpers are the part integration has done.
