# Penal Code 1871 — verification of the pre-existing encoding

**Run date:** 2026-09-09
**Scope:** every rule present in the encoding before this pass (ss 2, 4, 4B, 6, 23–26, 26B–26D,
76, 79A, 82, 83, 84, 95, 107, 108, 108A, 108B, 120A, 120B, 378, 403, 405, 415, 416, 416A, 416B,
418, 420, 420A, 424A, 424B, 463, 464, 499, 503, 504, 505, 506, 511, and the Schedule classifier).
**Method:** each rule read against `registers/source-bundle/PC1871.txt` (SSO current version as at
09 Sep 2026), plus a machine run of every module through `jl4-lsp` as a batch checker.

## Machine result before any change

```
14 modules, 0 type errors, 33 of 33 #ASSERTs satisfied
```

So the pre-existing encoding was **mechanically sound**. Every defect below is a fidelity
defect — the L4 says something the statute does not, or omits something the statute says.

## Defects found

| # | Section | Severity | Finding |
| --- | --- | --- | --- |
| V1 | s 84(1) | **high** | `section 84 applies` fired on `is of unsound mind at the time of the act` alone. s 84(1) requires unsoundness of mind **and** one of (a) incapable of knowing the nature of the act, (b) incapable of knowing it is wrong, (c) completely deprived of any power to control his actions; s 84(2) further requires, for (b), incapacity on *both* the ordinary-standards and contrary-to-law limbs. As written the exception exempted every act of any person of unsound mind, and because `a general exception applies` is negated in every `the proposed act constitutes ...` wrapper, a single true flag suppressed the entire offence screen. |
| V2 | s 505 | **high** | Limb (a) — statements causing an officer or serviceman of the SAF, a visiting force, or a s 140B person to mutiny or disregard his duty — was not encoded at all. Only (b) and (c) were. |
| V3 | s 23(1), (2) | medium | "by unlawful means" was not required; wrongful gain by **avoidance of a loss** and wrongful loss by **exposure to the risk of a loss** were both missing. |
| V4 | s 4B(1)(c) | medium | "or exposure to a risk of loss" omitted from the gain-or-harm limb. |
| V5 | s 416A(3)(a) | medium | The defence to the supply limb was keyed to `purpose is supply for use in committing ... an offence` only. s 416A(3)(a) speaks of a purpose other than "for the personal information **to be used** in committing" an offence, which covers the actor's own use as well. |
| V6 | s 26D(3) | medium | "or with wilful blindness" omitted from the knowingly test. |
| V7 | s 420(1) | low | The valuable-security limb omitted "or anything which is signed or sealed, and which is capable of being converted into a valuable security". |
| V8 | s 499 Expl 4 | low | The harm test covered lowering of character, calling and credit, but omitted "moral or intellectual" character and the loathsome/disgraceful-state limb. |
| V9 | s 503 | low | "as the means of avoiding the execution of such threat" was not encoded. |
| V10 | s 108A | low | The rule conjoined `the thing would be an offence if committed by a person capable ...` twice — once inside `the person abets an offence` and once directly. Redundant, and it conflates the s 108 capable-person test with s 108A's distinct "would constitute an offence if committed in Singapore" test. |
| V11 | s 79A | low | `DECIDE mistake of law is a defence IF FALSE` is dead code: nothing references it, and s 79A(1) is a rule about what is *not* a defence, so a bare FALSE constant adds nothing. |
| V12 | s 416B(1) | low | "conducted **mainly** by way of remote communication" was reduced to "the channel is not `not remote`". |

## Correct as written (checked, no change needed)

- s 2, s 4 — faithful.
- s 6 — correctly applied as a negated conjunct in every offence wrapper.
- s 24(a) and (b) — both limbs, correctly disjunctive.
- s 25 with Explanation 1 — correct, including the de-minimis carve-out.
- s 26, s 26B, s 26C(1) — faithful.
- s 82, s 83, s 95, s 76 — faithful.
- s 107(1)(a)–(c) and s 107(2) — faithful; impossibility correctly *not* a precondition.
- s 108 — faithful.
- s 108B — faithful.
- s 120A(1)–(5) — faithful, including the two-distinct-persons requirement and both
  extraterritorial arms.
- s 415 — faithful, including the choice not to gate on "sole or main inducement" and the
  correct attachment of the damage-or-harm clause to the third limb only.
- s 416, s 418 — faithful.
- s 420A(1)(a)–(c) — faithful.
- s 378, s 403 — faithful.
- s 405 — faithful on the two dishonest limbs; the sufferer limb is a documented
  interpretive choice, retained.
- s 424A(1), (4), (5) and s 424B(1), (4) — faithful, including the goods-or-services split.
- s 463, s 464(1)(a)–(c) — faithful.
- s 499 main test, s 504, s 506 — faithful apart from V8.
- s 511(1)–(3) — faithful.
- The Schedule classifier — the eight offence families it screens all do sit in the Schedule
  (items 3, 6, 7, 9, 10, 12, 13); s 463/464 map to Schedule item 13 through the s 465
  punishment section, which is correct.

All twelve defects are fixed in this pass.

---

**Since this pass.** Three modules were added afterwards — `chapter-2-definitions.l4`
(ss 6A to 51), `chapter-2-participation.l4` (ss 32 to 38) and `chapter-3-punishments.l4`
(Chapter 3) — and Chapter 4 was completed to ss 76 to 95 with Chapter 2 completed to
ss 26A to 26H. Those rules are **not** covered by the section-by-section fidelity reading
above; they carry `@ref` citations to the deposited source but have not had a second pair
of eyes read them back against it. The whole subject, old and new, was re-run through the
machine checker: 17 modules, 0 type errors, 53 of 53 assertions satisfied. See
`report/machine-evaluation.md`.
