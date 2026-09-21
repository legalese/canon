# projections/ — robbery as pictures and as prose

Eight decisions out of `../robbery-390-392.l4`, four carriers each, plus one hand-drawn page figure
that is **not** in that set and is flagged below.

## The generated set — 32 files, single-sourced

| file | carrier | made by |
| --- | --- | --- |
| `.svg` | page/print figure, `ink` theme | `@repo/ladder-svg` `sceneToSvg(scene,"ink")` |
| `.txt` | monospace grid — pasteable and **diffable** | `@repo/ladder-core` `sceneToAscii` |
| `.mmd` | Mermaid `railroad-beta` | `@repo/ladder-core` `toMermaidRailroad` |
| `.sentences` | **readable prose** — one line per way to satisfy the rule | `@repo/ladder-core` `expandSentences` |

**One carrier is wrong for one of the eight, and it is wrong quietly.**
`robbery-392-implies.sentences` reads "0 ways this can be satisfied", which is false about the rule and true about the tool: `expandSentences` (`ts-shared/ladder-core/src/sentences.ts`) has cases for `And`, `Or` and `Not` and none for `Implies`, so an implication body falls to the `default` arm, `leafLabel` returns `""` for it, and the enumeration comes back empty.
No warning, exit 0.
The other three carriers of that figure are correct.
`robbery-392-liability.sentences` is unaffected — its body is an `Or`.

| slug | decision in the L4 | what it is for |
| --- | --- | --- |
| `robbery-390` | `commits robbery` | s 390(1), the root: a two-way OR. Meet this one first |
| `robbery-390-2` | `theft is robbery` | s 390(2) — the widest, and the one to hold against a textbook's element list |
| `robbery-390-3` | `extortion is robbery` | s 390(3) — presence, instant harms, to whom, then-and-there |
| `robbery-392` | `offence under s 392` | the punishing section: one rung over the definition |
| `robbery-393` | `offence under s 393` | the attempt: one leaf, deliberately |
| `robbery-394` | `offence under s 394` | not s 392 plus a leaf — its own first limb, and its own second question |
| `robbery-392-implies` | `whoever commits robbery shall be so punished` | the same s 392 as an `IMPLIES`: scope, seam, **consequent on the right**, two lamps. Woon's shape, and the only figure here that has one |
| `robbery-392-liability` | `liable under s 392` | what that consequent contains — the ordinary punishment and the night one, as the statute splits them |

**Nothing here is retyped.** The generator reads the corpus through `jl4-lsp`
(`textDocument/codeLens` → `l4.visualize` → `RenderAsLadderInfo.funDecl` → `fromVizFunDecl` →
`layout`), so every label, every ordering and every inert chapeau comes out of the `.l4`. A figure
a human transcribed is a second source, and this set is not one.

The cost of that is **untrimmed labels**: a leaf reads `f's \`in order to commit theft\`` because
that is what the module says, and `robbery-390-2.svg` is 2894 px wide as a result. Two of the eight
are too wide for a page; `robbery-392-implies.svg` is not one of them, at 969 px. That is the same trade the Reg CF figures in l4-ide make, and it is
recorded in their README.

**The four carriers are not interchangeable.** Read `robbery-390-2.sentences` and the size of the
rule becomes obvious in a way no diagram shows: **48 ways** to satisfy s 390(2), which is four
timing limbs × two of causes-or-attempts × six harms. That number is the section, not the encoding.
It read 36 until 2026-09-21, when the timing group went from three limbs to four — see NOTES.md,
“s 390(2) at Woon’s granularity”.

## There are no THEFT figures here, and s 380 is now the reason to want one

Every slug above is `robbery-*`.
Nothing in this directory draws `commits theft` (s 378), `offence under s 379`, or — since 2026-09-21 — `offence under s 380`.
So Woon's two theft diagrams (*Essential Criminal Law* ch. 8, R02 at p. 181 and R05 at p. 185) have no artefact of ours to be laid beside, and the s 380 ladder is the first in this row with **two OR-groups in series**, which is exactly the shape a figure shows better than prose.

**The obvious fix does not work, and the shape of the real one is worth recording before anyone files it.**
`ts-shared/ladder-svg/demo/robbery.ts` in `legalese/l4-ide` sets ONE module-level `const CORPUS = resolve(ROW, "robbery-390-392.l4")`, and its `SUBJECTS` entries carry only `{decision, slug, why}` — there is no per-subject corpus path.
The three theft decisions are declared in `theft-378-379.l4`, and the script asks `jl4-lsp` for codeLenses on a single document, so adding three slugs would hit the script's own guard: `FAILED: N decision(s) not found in robbery-390-392.l4 — has one been renamed?`.
What is needed is a `corpus` field on `SUBJECTS` (or a sibling demo keyed to the theft module), not three slug entries.

That is an l4-ide change, not a canon one, and it has not been made.
**Nothing here is stale as a result** — these eight files are generated from `robbery-390-392.l4`, which the s 380 work did not touch. This section records an absence, not a drift.

## Regenerating

```sh
cd <l4-ide>/ts-shared/ladder-svg
npx turbo build --filter=@repo/ladder-svg -C ../..      # dist/ is gitignored; build it once
JL4_LSP_CMD=<l4-ide>/dist-newstyle/.../jl4-lsp \
CANON_DIR=<this canon checkout> npx tsx demo/robbery.ts
```

The generator is `ts-shared/ladder-svg/demo/robbery.ts` in `legalese/l4-ide`, registered as
`npm run demo:robbery`. It **fails loudly** (exit 1) if a named decision is not found, so renaming
a decision in the module breaks the run rather than silently dropping a figure. It **skips cleanly**
(exit 0) when `CANON_DIR` has no checkout, because l4-ide must never depend on canon.

> **Its `SUBJECTS` list still has only six entries, and that is the one thing here that can go
> stale without saying so.** `robbery-392-implies` and `robbery-392-liability` were generated on
> 2026-09-21 by a scratch runner that is a copy of `robbery.ts` with the two slugs added and the
> workspace imports resolved by absolute path, so that no l4-ide branch had to be touched to
> produce them. The runner regenerated the other six in the same pass and they came out
> **byte-identical to what was already committed**, which is the evidence that it is equivalent
> to the real generator. But `robbery.ts` cannot fail on a subject it does not list, so running
> `npm run demo:robbery` today refreshes six of the eight and leaves the other two untouched and
> unmentioned. **Adding the two `SUBJECTS` entries in l4-ide is the fix**, and until it lands
> these two files are the only ones in this directory that a regeneration will not keep honest.

**…but only if someone runs it.** It needs a live `jl4-lsp`, so it is not in `turbo.json` and no CI
runs it. Canon has no CI at all. These files can sit stale beside an edited module indefinitely;
re-run it whenever `robbery-390-392.l4` changes.

## The one hand-drawn figure

`robbery-390-ladder.{py,svg,png}` is **drawn, not generated**, by a dependency-free Python script
after l4-ide's `paper/formal-methods-in-law/the-letter-and-the-spirit/cheating-415-ladder.py`.

It earns its place by doing the one thing the generated set cannot: it puts **both subsections on
one page** at 1180 px, with every leaf coloured by its value on the Chen Weixiong Jerriek facts, so
a reader sees the whole of s 390 and which parts of it those facts light up. The generated root
figure shows two boxes; the generated s 390(2) is too wide to print.

**It is a second source and it can drift.** Nothing checks it against the module. If the ladder in
the `.l4` changes, this drawing will keep showing the old one, silently. Where the two disagree,
**the generated files are right**. It was written before the headless generated path was known to
be available, and it is kept for the page rather than for the record.
