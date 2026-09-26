**Title:** `prettyLayout` breaks a cross-module mixfix call: unparenthesised `OF a, b` does not re-parse against an imported interior-keyword definition

`L4.Print.prettyLayout` re-emits a mixfix application in the uncurried `f OF a, b, c` form and drops the interior keywords. **Within one module that is consistent** — the printer strips the keywords from the *definition* too, so the printed module re-parses and the `prettyLayout round-trip` property (jl4/tests/Main.hs, #932) is green:

```
-- sg-isa.l4, printed by prettyLayout — definition and call agree
DECIDE `per stirpes under` i portion people basis IS ...
    ... (`per stirpes under` OF i, portion, (p's issue), basis)
```

**Across a module boundary it is not.** The round-trip prints only the module under test; the imported definition keeps its interior keywords, so the printed call no longer matches it:

```
-- sg-child-support.l4, printed
`today's cost` MEANS `the employer's cost under the Act for` OF parent, `rule date`
```

```
Expected keyword `on` but found `rule date`
In expression involving: `the employer's cost under the Act for`
```

where `sg-childcare-leave.l4` defines

```
GIVEN parent IS A Parent, day IS A DATE
`the employer's cost under the Act for` parent `on` day MEANS ...
```

### Why it is intermittent, which is the part worth fixing

A cross-module interior-keyword call **survives when the printer happens to parenthesise it** — as a sub-expression it comes out `(`the year` OF child, 1)`, which re-parses. It fails only where the call is the whole right-hand side of a binding or a record field, where the printer emits it bare and the commas are then ambiguous. So the same construct round-trips or not depending on where it sits, which is why no existing corpus file caught it: `regcf` and `sg-succession` keep their interior-keyword definitions and uses in the same module.

### Repro

`jl4/examples/legal/sg-child-support` at the parent commit of the fix; `jl4-test -m 'legal/sg-child-support/sg-child-support.l4'` (6 examples, 1 failure). `JL4_PRETTY_DUMP_DIR` shows the emitted text.

### Suggested fix, in preference order

1. **Parenthesise every multi-argument `OF` application** the printer emits. Cheapest, and it makes the construct's round-trip independent of position — which is the actual defect.
2. Re-emit the mixfix keywords, which needs `L4.Mixfix.MixfixRegistry` threaded into the printer (already noted in `CLAUDE.md` §3.2.2 as the real fix for the sibling defect).

### Workaround taken meanwhile

`sg-child-support` renames its cross-module surface to head-keyword-only (`` `days of leave under the Act` parent day `` rather than `` `days of leave under the Act for` parent `on` day ``) and records the constraint in its `NOTES.md`. Interior keywords are kept for module-internal functions, where the printer is self-consistent. This costs some of the prose readability the house style is for, so it is a workaround and not a preference.
