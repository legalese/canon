# De novo diff — sg-succession

Produced by `etc/go/lib/denovo-diff.mjs` from `/Users/mengwong/src/legalese/l4wt/sg-family-gia/jl4/examples/legal/sg-succession/cleanroom-2026-08/surface-map.json`. Every disposition below is **UNTRIAGED**: this script measures, it does not triage. SPEC.md §8's three dispositions — `ENCODING-ERROR`, `GENUINE-AMBIGUITY`, `IMPROVEMENT-OVER-CORPUS` — are judgements and belong to the reviewer or the skill.

## Surfaces

|                      | corpus (left)                                | cleanroom (right)                                                                |
| -------------------- | -------------------------------------------- | -------------------------------------------------------------------------------- |
| module               | `jl4/examples/legal/sg-succession/sg-isa.l4` | `jl4/examples/legal/sg-succession/cleanroom-2026-08/intestate-succession-act.l4` |
| rules declared       | 27                                           | 271                                                                              |
| rules paired         | 5                                            | 5                                                                                |
| paired and `@export` | 0                                            | 0                                                                                |

## Battery

24 seed row(s), 0 single-field perturbation(s), 24 row(s) in all. Every seed is evaluated against all 5 pair(s); a perturbation is evaluated only against the pairs that take the mutated slot as an argument, because a decision is a function of its arguments and the rest are provably unchanged. That leaves **120** evaluation(s) per side.

## Agreement

| pair                   | citation        | evaluated |  agreed | diverged | leaves perturbed | of those, inert |
| ---------------------- | --------------- | --------: | ------: | -------: | ---------------: | --------------: |
| `act-applies`          | ISA 1967 s 2    |        24 |      24 |        0 |                0 |               0 |
| `movables-regulated`   | ISA 1967 s 4(1) |        24 |      24 |        0 |                0 |               0 |
| `immovables-regulated` | ISA 1967 s 4(2) |        24 |      24 |        0 |                0 |               0 |
| `commencement`         | ISA 1967 s 5    |        24 |      24 |        0 |                0 |               0 |
| `distributable-fund`   | ISA 1967 s 5    |        24 |      19 |        5 |                0 |               0 |
| **total**              |                 |   **120** | **115** |    **5** |            **0** |           **0** |

### Sensitivity — where an agreement is not evidence

An **inert** (pair, fact) leaf is one the battery perturbed without ever moving either side's answer away from its seed's. Agreement there is not agreement about anything: the decision never responded to that input over these values, so a real difference between the two encodings on that leaf would be invisible. This is measured, it does not affect the exit code, and it is not a defect in either encoding — it is a limit of the battery. The remedy is a seed case or a `slots.<n>.thresholds` entry that reaches the boundary.

Every perturbed leaf moved an answer at least once. No blind spot of this kind.

## Triage table (SPEC.md §8)

|   # | pair                 | witness                                                                                         | corpus says         | cleanroom says | also seen on | fork       | disposition   |
| --: | -------------------- | ----------------------------------------------------------------------------------------------- | ------------------- | -------------- | -----------: | ---------- | ------------- |
|   1 | `distributable-fund` | whole seed row _section 4 — domiciled abroad, both movable and immovable property in Singapore_ | `636363.6363636364` | `600000`       |            0 | `F-ISA-A7` | **UNTRIAGED** |
|   2 | `distributable-fund` | whole seed row _section 5 — an estate with substantial debts_                                   | `700000`            | `1000000`      |            0 | `F-ISA-A7` | **UNTRIAGED** |
|   3 | `distributable-fund` | whole seed row _section 5 — expenses exceeding the whole Singapore estate_                      | `-900000`           | `0`            |            0 | `F-ISA-A7` | **UNTRIAGED** |
|   4 | `distributable-fund` | whole seed row _section 5 — part of the Singapore estate held as trustee and not beneficially_  | `1000000`           | `500000`       |            0 | `F-ISA-A7` | **UNTRIAGED** |
|   5 | `distributable-fund` | whole seed row _section 5 — the whole Singapore estate held as trustee and not beneficially_    | `1000000`           | `0`            |            0 | `F-ISA-A7` | **UNTRIAGED** |

Minimality: a witness marked `one-field-from-agreeing-seed` is minimal by construction — its seed agreed and exactly one field moved. A witness marked `whole-seed-row` is not minimised: the seed itself diverged, and there is no agreeing neighbour to shrink towards.

## Limits — what this comparison cannot see

- **Only the pairs the map declares.** Coverage is `rules paired / rules declared` above. A decision present in one encoding and absent from the other is invisible here unless somebody wrote the pair down — the map is a declaration, and the oracle can only disagree with what was declared.
- **Decisions only — the deontic layer is not exercised.** The battery evaluates `DECIDE`/`MEANS` functions. Regulative rules (obligations, deadlines, reparations) have no answer this comparator reads, so two encodings could differ on who owes what, by when, and with what consequence on breach, and every row here would still agree. The BPMN/LTS legs are where that divergence would show; wiring them into the diff is not built.
- **Answer equality is equality of the compiler's rendering.** Two answers that mean the same thing but render differently (a record with reordered fields, `4/2` against `2.0`) read as a divergence, and are triaged away by a human. The `field` projection in the map exists to narrow the comparison when that noise dominates.
- **Both sides erroring identically counts as agreement.** If a fact pattern makes both encodings refuse, that is recorded as an agreement on the refusal — which is the right answer for a curated refusal (Reg CF pre-commencement dates) and the wrong one if both encodings are broken in the same way.
- **Perturbation is single-field.** Interaction defects that need two fields to move together are out of reach. The generator is a search over a neighbourhood of the seed cases, not over the input space.
- **A leaf the battery never made a decision respond to is not compared, only visited.** The generator reaches the values it can derive from the seed cases (±1, ×0/×½/×2, ×−1, cross-pollination, declared thresholds); a statutory boundary outside every one of them is never crossed, and both encodings answer identically on the near side of it whatever they say on the far side. Measured case: moving `total assets threshold` from 10,000,000 to 20,000,000 in a scratch copy of `regcf.l4` changes a live path of `reporting-may-terminate` and produces **zero** divergence, because every value the battery reaches for `status.total assets` is below both. The Sensitivity table above is that blind spot enumerated rather than described; the remedy is a seed case or a `slots.<n>.thresholds` entry at the boundary.
- **List-valued and optional-shaped facts are not perturbed.** `leavesOf` descends objects and stops at arrays.
- **An enum-typed input field cannot be fed.** `JSONDECODE` delivers a constructor name as a string, so any `CONSIDER` over an enum-valued field of a decoded record raises `NonExhaustivePatterns` — on both sides identically, which reads as agreement on an error and measures nothing. Keep such slots out of the map (the Reg CF identity fixture drops `FormCFiling` for exactly this) until the decoder learns constructors. `l4 batch` decodes rows the same way and has the same limit.
- **A `#ASSERT` in either module is not consulted.** This is a differential oracle between two encodings; it says nothing about whether either agrees with the statute. That is HG1's question and P5's.
