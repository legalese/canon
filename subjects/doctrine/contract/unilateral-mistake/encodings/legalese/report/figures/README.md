# Ladder figures

Four ladder diagrams of the critical logic, rendered by **l4-ide's own ladder visualizer** rather
than drawn by hand — so the picture uses the project's visual grammar and not an imitation of it.

| file | what it shows |
| --- | --- |
| `donovan-sg.screen.svg` | Singapore's equity door under *Donovan*'s facts — the current dies at `constructive knowledge` |
| `donovan-us.screen.svg` | Restatement § 153 under the **same** facts — the circuit closes through the unconscionability rung |
| `dm2-sg.screen.svg` | Singapore's equity door for *Digilandmall*'s second appellant — closes |
| `dm2-au.screen.svg` | *Taylor v Johnson* on the same facts — dies at `deliberately set out to prevent discovery` |

The two pairs are Delta 3 and Delta 1 of [the report](../../README.md), drawn on identical facts.

## How to read them

Series is **AND**, the parallel fan is **OR**, a small circle is a **NOT** inverter, and unboxed
italic prose is *inert* text — grammatical scaffolding that carries no current. Line weight is
current: thick means the contact is closed and reached, hairline means it is not. A path that
runs source to sink turns **green**; one that stops partway stays near-black and simply ends.

That green is worth trusting rather than reading off: it is the renderer's own `scene.complete`,
computed by its energize pass, and on all four figures it **agrees with the verdict the L4 modules
compute** — `complete=false, true, true, false` against `stands, voidable, voidable, stands`. The
picture and the encoding were produced by different code from the same rules.

## Regenerating

`make-ladders.ts` is the generator. It is **not runnable from this repository**: it imports
`@repo/ladder-core` and `@repo/ladder-svg`, which live in `legalese/l4-ide`. Drop it into
`ts-shared/ladder-core/demo/` in an l4-ide checkout with dependencies installed and run it with
`npx tsx`.

**Provenance, stated precisely.** These four SVGs were rendered on 2026-09-07 from the worktree
`~/src/legalese/l4wt/ladder-e1-step4`, branch `mengwong/ladder-e1-step4` at `77f527d1` — which is
**not `unstable`**. `ts-shared/ladder-core` and `ts-shared/ladder-svg` are both on `unstable` and
the generator uses only their public API (`layout`, `estimateMetrics`, `defaultViewSpec`,
`sceneToSvg`), so it is expected to run there unchanged — but that was not tested, and "expected
to" is not "does". Anyone regenerating should re-run against `unstable` and say so here.

The circuits are transcribed from the `.l4` modules by hand, the same way the artifact's
JavaScript is, and carry the same risk: if a module changes and these are not re-rendered, the
figures go stale silently. Nothing checks them.
