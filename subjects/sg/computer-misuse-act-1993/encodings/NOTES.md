# Computer Misuse Act 1993 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act, ss 1–20 and both Schedules**, as printed by SSO, "Current version as at 07 Oct 2026". That is the 2020 Revised Edition, amended by Act 16 of 2023 (in force 8 February 2024) and Act 21 of 2025 (in force 30 December 2025).

**The vintage (fork F1).** Act 21 of 2025 did several things:
- added the scam offences (Second Schedule);
- added caning to ss 8A and 8B;
- made s 8A(1) "subject to subsection (5)";
- recast s 8B(5).

The source prints only the amended text. So the top-level goal refuses conduct before 30 December 2025. The goal functions underneath take no date and answer with the current text: a caller asking about earlier conduct through them gets the 2025 text. The independent pass pointed this out, and it is recorded here rather than threaded through every rule.

**Inputs.** The court's findings are inputs:
- knowledge, purpose and intent;
- reasonable grounds and reasonable steps;
- whether a presumption is rebutted.

So are:
- which offences are prescribed as compoundable (s 16(2));
- a prescribed loss threshold or excluded device (s 2(1));
- for ss 9 and 10, whether the underlying act contravened ss 3–6 or ss 3–7.

For "damage", the caller gives the loss counted within one year after the offence; s 2(1)(a) excludes later loss.

### The goals

Top level: `the computer misuse position for` a `Case` (`cma-goal.l4`). The question is: *for this conduct involving a computer, does the Act reach it, is the alleged offence made out, and what is the most it can cost?*

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Is it a computer? Did the person secure access or modify? Was it without authority? Was there damage? | `a computer`, `secures access to a program or data`, `a modification of the contents of a computer`, `without authority`, `damage`, `a credential in relation to the national digital identity service`, `a scam offence` | s 2; First and Second Schedules | `cma-definitions.l4` |
| 2 | Are the elements of the alleged offence made out, with no exception met? | `the elements are made out`, `the s 8A(3) presumption stands`, `a dealing is an offence`, `an offence to which s 4 applies` | ss 3–10, 12 | `cma-offences.l4` |
| 3 | What are the maximum fine, imprisonment and caning? | `the maximum punishment for`, `the section's punishment for`, `a protected computer`, `the caning strokes for` | ss 3–12 | `cma-punishment.l4` |
| 4 | Does the Act reach the conduct? Can charges be amalgamated? Which courts, composition, compensation, arrest? | `the Act reaches the conduct`, `the acts may be charged as one offence`, `the most that may be collected to compound, prescribed:`, `the damages still recoverable in a civil claim…` | ss 13–20 | `cma-scope-procedure.l4` |

## 2. Coverage table

| provision | heading | disposition |
| --- | --- | --- |
| long title, 1 | Short title | inert (`provisions carried as text`) |
| 2(1) | Interpretation | Goal 1. "computer" (with exclusions (a)–(d)) and "damage" (limbs (a)–(d) with the $10,000 threshold) are encoded. "scam offence" and "credential" are encoded via the Schedules. The other definitions are read into the facts: computer output, computer service, data, device, function, intercept, program, user |
| 2(2)–(4), (6), (9) | securing access, use, output form | Goal 1 `secures access to a program or data`. Subsection (6) (removable media) and (9) (part of a program) are read into the facts |
| 2(5), (8) | without authority | Goal 1 `without authority` |
| 2(7) | modification | Goal 1 |
| 3 | Unauthorised access | Goal 2 elements; Goal 3 punishment, (1)(a)–(b) and (2). Subsection (3) (immaterial targets) adds no element |
| 4 | Access with intent | Goal 2, (1), (2) and (4); Goal 3, (3) |
| 5 | Unauthorised modification | Goals 2–3 |
| 6 | Use or interception of computer service | Goals 2–3 |
| 7 | Obstruction of use | Goals 2–3 |
| 8 | Disclosure of access code | Goals 2–3 |
| 8A | Singpass disclosure | Goal 2: (1), with the presumption in (3) and the exception in (4). Subsection (2) eases proof and adds no element. Goal 3: (1) and caning under (5); (6)–(7) are proof rules |
| 8B | Another's credential | Goal 2: (1)–(4). Goal 3: (5) and caning under (5A)–(5B); (5C)–(5D) are proof rules; (6) maps to the First Schedule |
| 9 | Personal information | Goals 2–3. Both Examples are tested. Subsection (6) is a proof rule; (7) is read into the facts |
| 10 | Items for use in offences | Goals 2–3 |
| 11 | Protected computers | Goal 3, (1)–(3) |
| 12 | Abetment and attempts | Goal 2 `is guilty of the offence itself, with its punishment`. Participation changes nothing computed. Subsection (2) (place immaterial) is noted |
| 13 | Territorial scope | Goal 4, (1)–(6); subsection (7) is read into "statutory board" |
| 14 | Amalgamation of charges | Goal 4, (1)–(3). Subsection (4) (sufficient notice) is a drafting rule, inert |
| 15 | Jurisdiction of Courts | Goal 4 |
| 16 | Composition | Goal 4. The prescription is an input |
| 17 | Compensation | Goal 4, (1)–(2). Subsection (3) (civil debt) is inert |
| 18 | Saving for investigations | Goal 4 |
| 19 | Arrest without warrant | Goal 4 |
| 20 | Amendment of Schedules | inert |
| First Schedule | NDI service definitions | Goal 1 `Credential kind` |
| Second Schedule | Scam offences | Goal 1 `a scam offence` |

Nothing is left `deferred`.

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | Act 21 of 2025 | What text governs conduct before 30 December 2025? | The top-level goal refuses that conduct | The source prints only the amended text. The goal functions themselves are undated (see §1) |
| F2 | s 14(1)(c) "a period that does not exceed 12 months" | Is the anniversary inside the period? | Yes. The last act may fall on the same day of the month twelve months after the first; the day after may not | First taken the other way (both days counted). Revised after the independent pass: "does not exceed" is an inclusive ceiling, and s 50(a) of the Interpretation Act 1965 excludes the first day |
| F3 | s 3(2), 5(2), 6(2), 7(2) "If any damage is caused" | Does the damage limb override a repeat conviction? | Yes: $50,000 / 7 years whether or not it is a repeat | Subsection (2) states its own ceiling for "a person convicted", without the (1)(a)/(b) distinction |
| F4 | s 11(1) "in lieu of the punishment prescribed in those sections" | With a protected computer and damage both present, which ceiling applies? | s 11: $100,000 / 20 years | s 11 replaces the section's punishment, the damage limb included |
| F5 | s 12 | Does an abettor or attempter face anything different? | No: "the punishment provided for the offence" | The text |

**Smaller readings:**
- **s 16 composition and s 19 arrest** turn on reasonable suspicion, not proof. The top-level goal reports them whether or not the elements are found made out (corrected after the independent pass).
- **Caning applies only to an individual** (ss 8A(5), 8B(5A)–(5B)). A body corporate gets 0 strokes.

## 4. Tests

- `cma-tests.l4` (93 assertions). Expected values are worked from the source. They include both s 9 Examples, every penalty limb, the $10,000 damage edge, the s 4(2) two-year threshold, the 30 December 2025 gate, and the s 14 anniversary edge (revised with fork F2).
- `tests-independent.l4` (134 assertions), `independent-expectations.md` and `INDEPENDENT-TEST-REPORT.md` are the independent pass. A separate session wrote its expectations from the source before reading the encoding.
  - 133 passed on the first run.
  - The one failure was s 14 at exactly 12 months. It was resolved by revising F2; that expected value was not edited.
  - The report's other observations are answered in §1 and §3: the undated goal functions, the one-year loss cut-off left to the caller, ss 9 and 10's underlying contravention as an input, s 16 and s 19 (fixed), and ss 12(2), 14(4) and 17(3) (inert).

## 5. Checks

See `encoding.json` → `checks`.
