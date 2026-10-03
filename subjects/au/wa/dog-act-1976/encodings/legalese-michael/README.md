# Dog Act 1976 (Western Australia)

This corpus formalises the **whole** Dog Act 1976 (WA) (No. 58 of 1976) as 18 L4 modules: one
shared domain module, and 17 Part/Division modules covering every operative section of the Act.

**Status: draft, not yet reviewed.** No human gate (HG1 domain-expert review, HG2 publish
sign-off) has been granted over this encoding. It is deposited here as a working copy mirrored
from the `legalese/l4-ide` development repo's `etc/go/subjects/dog-act-1976/` pipeline sidecar
and `jl4/examples/legal/dog-act-1976/`, where the same files, plus the pipeline's own machine
checks, live under version control. Treat this copy as a snapshot, not the record of truth for
the encoding's own history.

**The law is stated as at the compilation dated 28 Nov 2024** (version `08-b0-00`), re-verified
current on 2026-09-09. The verbatim extract the first module encodes from, with full provenance,
is [`source-s33.txt`](source-s33.txt) in this directory. The original bulk-ingest deposit of the
full Act's text (retrieved 2026-09-07, before any encoding existed) is preserved at
[`registers/source-bundle/`](registers/source-bundle/).

## History and methodology

- **2026-09-09, first pass**: `dog-act-1976.l4` was hand-encoded, covering s. 3 (extract) and Part
  VI Division 1 s. 33D ("Dog attacks etc.") plus the whole of Division 2 ("Dangerous dogs", ss
  33E-33M) — a deliberately bounded first slice, on the BNA smoke-test corpus's precedent. Its s.
  3 building blocks were then factored out into `dog-act-domain.l4`, the shared domain module
  every other module imports.
- **2026-09-09, same day, extended to the whole Act**: the remaining ~110 sections were encoded by
  a 16-way parallel Workflow run in the `l4-ide` development repo (`wf_9ecfc05c-79c`): one agent
  per Part/Division drafted, self-checked and iterated a module; a second, independent agent then
  re-verified each module against the source text line-by-line and fixed what it found. 14 of 16
  modules had real issues caught and fixed at that independent-review stage. The orchestrating
  session then independently re-ran `l4 check`/`l4 run` over all 18 modules itself before mirroring
  them here.
- Every one of the 17 non-domain modules is mutually independent: none imports another, and each
  treats a cross-reference outside its own assigned text (including into another module) as a
  scoped-out, fact-supplied input.

## Modules

| Module | Parts/Divisions | Sections | Assertions |
| --- | --- | --- | --- |
| `dog-act-domain.l4` | s. 3 (extract, shared) | — | 0 (types only) |
| `dog-act-1976.l4` | Part VI Div 1 s. 33D, Div 2 | 33D, 33E-33M | 16 |
| `dog-act-part1-preliminary.l4` | Part I (remainder) | 6, 7, 8 | 28 |
| `dog-act-part2-administration.l4` | Part II | 9-13B | 61 |
| `dog-act-part3-div1-registration.l4` | Part III Div 1 | 14-20 | 78 |
| `dog-act-part3-div2-microchipping.l4` | Part III Div 2-3 | 21-26D | 23 |
| `dog-act-part5-keeping-of-dogs.l4` | Part V | 26 (limitation), 27 | 31 |
| `dog-act-part6-div1-control-of-dogs.l4` | Part VI Div 1 (remainder) | 28-33C | 45 |
| `dog-act-part6-div3-4-livestock-nuisance.l4` | Part VI Div 3-4 | 34, 35, 38 | 24 |
| `dog-act-part6a-div1-2-pet-shop-approval.l4` | Part VIA Div 1-2 | 38A-38F | 28 |
| `dog-act-part6a-div3-pet-shop-obligations.l4` | Part VIA Div 3 | 38G-38M | 36 |
| `dog-act-part6a-div4-5-dog-supply-approval.l4` | Part VIA Div 4-5 | 38N-38Y | 50 |
| `dog-act-part7a-destruction-of-dogs.l4` | Part VII (early) | 39-41 | 30 |
| `dog-act-part7b-enforcement-offences.l4` | Part VII (remainder) | 43-46A | 51 |
| `dog-act-part8-civil-remedies.l4` | Part VIII | 46, 47 | 29 |
| `dog-act-part9-local-laws.l4` | Part IX | 48-52 | 35 |
| `dog-act-part10-miscellaneous.l4` | Part X | 54-54I | 59 |
| `dog-act-part11-transitional.l4` | Part XI | 55-65 | 30 |
| **Total** | | | **654** |

Independently re-measured 2026-09-09: 654 assertions, 0 failed, 0 errors across all 18 modules.
`l4 check` succeeds with no warnings on every module.

## `dog-act-domain.l4`'s shared building blocks

`LiableParty` + `` `the party is a person liable for the control of the dog` `` (s. 3), `DogProfile`
+ `` `the dog is a dangerous dog` `` (s. 3), `AttackFacts` + `` `the behaviour is an attack` `` (s.
3), and the bare `Penalty` record shape. Every other module imports this one; none redeclares
these. Dollar-amount `Penalty` presets are declared locally per module.

## Scoped out (inputs, not stubs)

Every module treats a cross-reference outside its own assigned text as a fact-supplied input,
never expanded: s. 15, s. 22, s. 29, s. 30(3), s. 31(2B), the Interpretation Act 1984 s. 71, the
Local Government Act 1995, the Criminal Code, the Public Health Act 2016, the Racing and Wagering
Western Australia Act 2003, the State Administrative Tribunal Act 2004, the Veterinary Practice
Act 2021, and more — see each module's own header comment (66 scoped-out references in total).

## Ambiguity register (full detail in [`registers/fork-register.json`](registers/fork-register.json))

22 entries. Two are **materialised** as `Interpretation` record fields with observable divergence:
**F-DANGEROUS-DOG-STATUS-TIMING** (`dog-act-1976.l4`, s. 33D penalty timing) and
**F-S47-REPRESENTATIVE-QUALIFIER-SCOPE** (`dog-act-part8-civil-remedies.l4`, s. 47(1) qualifier
scope). The rest are `resolved-at-encode` or `delegated-to-fact`.

## Tests

654 `#ASSERT`/`#TRACE` directives across 18 modules, verified green against `l4` prerelease
`unstable-20260907-9d6536a` or later:

```bash
for f in *.l4; do l4 check "$f"; done
for f in *.l4; do l4 run "$f"; done
```

## Projection artifacts

None yet.
