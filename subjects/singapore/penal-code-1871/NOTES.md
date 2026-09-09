# Penal Code 1871 -- encoding notes

This subject's idiosyncrasies, in prose, for humans. No script reads this file.

---

## 1. What this subject is

An L4 encoding of **Penal Code 1871** (2020 Revised Edition, SSO current version as at 09 Sep 2026) built so an AI agent can screen a proposed act against the constitutive tests of selected offences and ask whether a Chapter 4 general exception takes the act outside "offence".

The agent-facing entry points are in `agent-compliance.l4`:

| question | answered by |
| --- | --- |
| Which encoded offences are indicated on these facts? | `the offence screen of` |
| Is any encoded offence indicated? | `any screened offence is indicated` |

Modules, in dependency order:

```
types.l4                      the nouns: records and enums, no rules
chapter-1-preliminary.l4      ss 2, 4, 4B location facts
chapter-2-explanations.l4     ss 23-26, 26B-26D (dishonestly, fraudulently, ...)
chapter-4-exceptions.l4       ss 6, 76, 79A, 82, 83, 84, 95
chapter-5-abetment.l4         ss 107, 108, 108A, 108B
chapter-5a-conspiracy.l4      ss 120A, 120B
chapter-17-cheating.l4        ss 415, 416, 416B, 418, 420, 420A
chapter-17-property.l4        ss 378, 403, 405
chapter-17-fraud.l4           ss 416A, 424A, 424B
chapter-18-forgery.l4         ss 463, 464
chapter-21-22-speech.l4       ss 499, 503, 504, 505
chapter-23-attempts.l4        s 511
agent-compliance.l4           the screen and the Schedule-to-4B classifier
agent-cases.l4                scenario fixtures, machine-asserted
registers/source-bundle/      PC1871.txt / .pdf as retrieved 09 Sep 2026
```

## 2. What is deliberately not encoded

The Code has 500+ operative sections. This draft encodes the chapters an AI agent is most likely to walk into when checking its own output or a user's requested act:

- **Not encoded:** Chapters 6-16 (State, armed forces, unlawful assembly, public servants, false evidence, public health, religion, offences affecting the human body including hurt, sexual offences, wrongful confinement), most of Chapter 17 (extortion, robbery, stolen property, criminal trespass), currency offences, and the ten exceptions to s 499 as individual tests.
- **s 84** is encoded only on the opening "unsoundness of mind at the time" fact. The remaining capacity tests of s 84(1) are not encoded.
- **s 499 exceptions** are a single caller-asserted flag `a section 499 exception applies`.
- **Punishment** is not computed. The encoding answers whether the constitutive test is met, not what sentence a court would pass.
- **Computer Misuse Act 1993** is a different Act and is not in the source bundle.

## 3. Interpretive choices

- **s 415** "whether or not such deception was the sole or main inducement" is encoded by not treating that flag as a precondition.
- **s 415 Explanation 4 and 5** (a company can be deceived / induced even if no individual officer is personally deceived) are encoded as facts the caller may assert; they do not change the boolean test, which still requires `deceives a person` (s 11: "person" includes a company).
- **s 4B(1)(a)** is encoded as either relevant act in Singapore and another outside, or the reverse.
- **s 416A(3)** defence to the supply limb is encoded as: the supply limb fires unless both (purpose is not supply for an offence) and (no knowledge it will be so used).
- **s 424A / 424B** split on `is directly connected with a written or oral contract for the supply of goods or services`. Materiality is ignored (s 424A(2), s 424B(2)).
- **s 405** "intentionally suffers any other person to do so" is treated as sufficient without a separate dishonesty check on the sufferer limb, matching the disjunctive last clause of s 405.
- **s 6** is applied in every `the proposed act constitutes ...` wrapper: if a general exception encoded here applies, the wrapper is FALSE.

## 4. Status

`draft`. No claim of fidelity. No HG1/HG2 grant.

