# Coverage - exceptions group (Chapter 4, ss 76-95; Chapter 4A, ss 96-106A)

Modules, all in `deposit/`:

- `pc-exceptions-general.l4` - Chapter 4 (ss 76-95).
- `pc-exceptions-private-defence.l4` - Chapter 4A (ss 96-106A).
- `pc-exceptions.l4` - the roll-up `a general exception applies` (s 6), and the s 26G(5) / s 301(2) wiring that notes/PLAN.md §5 gives this group.
- `pc-exceptions-tests.l4` - 153 assertions.

**No section in these Chapters creates an offence, so no row has an `offence under s N` or a `charge under s N`.**
BRIEF.md says so for "a general exception", and notes/PLAN.md §8 says to state it here: items 3 and 4 of the charge-generator contract do not apply to any section below.
What the charge generator gets instead is one exported BOOLEAN ladder per exception, over its own facts record, with every leaf phrased so that TRUE favours the accused (FORK E-1) - so its FALSE-fill of unknown leaves withholds the exception, which is Evidence Act 1893 s 107's "the court is to presume the absence of such circumstances".

`check.sh`-equivalent counts on the toolchain in BRIEF.md, `JL4_LIBRARY_PATH` unset, 2026-09-26:

| module | errors | warnings | satisfied | failed |
| --- | --- | --- | --- | --- |
| pc-exceptions-general.l4 | 0 | 0 | 0 | 0 |
| pc-exceptions-private-defence.l4 | 0 | 0 | 0 | 0 |
| pc-exceptions.l4 | 0 | 0 | 0 | 0 |
| pc-exceptions-tests.l4 | 0 | 0 | 153 | 0 |

Positive control: a copy of the tests with one expectation inverted (`exception under s 96` on s 98 illus (a)) reports 1 failed assertion, so the harness can fail.

| s | heading | disposition | functions (facts record) |
| --- | --- | --- | --- |
| 76 | Act done by person bound, or justified by law | encoded | `exception under s 76` (`Bound or Justified by Law Facts`) |
| 77 | Act of judge when acting judicially | encoded | `exception under s 77` (`Judicial Act Facts`) |
| 78 | Act done pursuant to the judgment or order of a court of justice | encoded | `exception under s 78` (`Court Order Facts`) - FORK E-2 |
| 79 | Act done by person by mistake of fact believing himself bound or justified by law | encoded: (1) as a ladder; (2) and Explanations 1-2 inert (declaratory - a mistake negating a fault element is answered by the offence's own fault leaf) | `exception under s 79` (`Mistake of Fact Facts`) |
| 79A | Mistake of law or ignorance of law not defence | encoded: (1) as a ladder of the one open case; (2) inert (declaratory) | `mistake of law is a defence under s 79A` (`Mistake of Law Facts`) |
| 80 | Accident in the doing of a lawful act | encoded: (1) with the Explanation in the `in the doing of a lawful act` leaf; (2) inert (declaratory) | `exception under s 80` (`Accident Facts`) |
| 81 | Act likely to cause harm but done to prevent other harm | encoded, Explanation as a limb (FORK E-3) | `exception under s 81` (`Necessity Facts`) |
| 82 | Act of a child below 10 years of age | encoded | `exception under s 82`, helper `below 10 years of age` (`Child Facts`) |
| 83 | Act of a child of or above 10 and below 12 years of age, who has not sufficient maturity of understanding | encoded | `exception under s 83`, helper `of or above 10 years and below 12 years of age` (`Child Facts`) |
| 84 | Act of person of unsound mind | encoded, (2) inside limb (1)(b) | `exception under s 84` (`Unsoundness of Mind Facts`) |
| 85 | Intoxication when a defence | encoded, (2A) inside limb (2)(b); (1) is the closure (FORK E-4) | `exception under s 85` (`Intoxication Facts`) |
| 86 | Effect of defence of intoxication when established | (1) encoded as an outcome, not exported (not a BOOLEAN ladder); (2) inert (evidence on the offence's fault leaves); (3) carried in the `@desc` of every `Intoxication Facts` leaf | `the effect under s 86(1)` returning `Effect of the defence of intoxication` |
| 87 | Act not intended and not known to be likely to cause death or grievous hurt, done by consent | encoded (FORK E-10), age helper FORK E-9 | `exception under s 87`, helper `above 18 years of age` (`Consent to Harm Facts`) |
| 88 | Act not intended to cause death done by consent in good faith for the benefit of a person | encoded | `exception under s 88` (`Consent to Harm Facts`) |
| 89 | Act done in good faith for the benefit of a child or person of unsound mind, by or by consent of guardian | encoded, provisos (a)-(d) in the defender's polarity (FORK E-1) | `exception under s 89`, helper `below 12 years of age` (`Consent to Harm Facts`) |
| 90 | Consent given under fear or misconception, by person of unsound mind, etc., and by child | encoded as a DEFINITION (FORK E-5); ss 87-89 read it as a flat leaf | `consent within section 90` (`Consent Facts`) |
| 91 | Acts which are offences independently of harm caused to the person consenting | encoded, read inside ss 87-89 | `not excluded by s 91` (`Consent to Harm Facts`) |
| 92 | Act done in good faith for the benefit of a person without consent | encoded (FORK E-6); the Explanation printed after s 92 (mere pecuniary benefit) is in the benefit leaves' `@desc` for ss 88, 89 and 92 | `exception under s 92` (`Benefit Without Consent Facts`) |
| 93 | Communication made in good faith | encoded | `exception under s 93` (`Communication Facts`) |
| 94 | Act to which a person is compelled by threats | encoded; Explanations 1-2 in the proviso leaf's `@desc`, and tested | `exception under s 94` (`Compulsion by Threats Facts`) |
| 95 | Act causing slight harm | encoded | `exception under s 95` (`Slight Harm Facts`) |
| 96 | Nothing done in private defence is an offence | encoded | `exception under s 96` (`Private Defence Facts`, one record for all of Chapter 4A) |
| 97 | Right of private defence of the body and of property | encoded, one ladder per limb | `the right of private defence of the body extends to the act`, `the right of private defence of property extends to the act`, `the act is, or is to be treated as, an offence within sections 97 and 99` (FORK E-13) |
| 98 | Extent to which right may be exercised | encoded | `within the restrictions of section 98` |
| 99 | Right of private defence against act of person of unsound mind, etc. | encoded, as the second limb of `the act is, or is to be treated as, an offence within sections 97 and 99` | (as s 97) |
| 100 | Right of private defence against deadly assault when there is risk of harm to innocent person | encoded | `the right of private defence extends to the running of the risk within section 100` |
| 101 | Start and continuance of right of private defence of body | encoded, inside the body ladder | `the right of private defence of the body extends to the act` |
| 102 | When right of private defence of body extends to causing death | encoded (FORK E-14) | `the right of private defence of the body extends to the harm caused to the assailant within sections 102 and 103` |
| 103 | When such right extends to causing any harm other than death | encoded | (as s 102) |
| 104 | Commencement and continuance of right of private defence of property | encoded: (1) in the property ladder; (2)-(5) as their own ladder (FORK E-7) | `the right of private defence of property continues within section 104` |
| 105 | When right of private defence of property extends to causing death | encoded (FORK E-15) | `the right of private defence of property extends to causing death within section 105`, `in one of the 6 ways described in section 105(2)`, helper `after 7 p.m. and before 7 a.m.` |
| 106 | When such right extends to causing any harm other than death | encoded | `the right of private defence of property extends to the harm caused to the wrongdoer within sections 105 and 106` |
| 106A | Acts against which there is no right of private defence | encoded, in the defender's polarity (FORK E-1, E-8) | `section 106A does not exclude the right` |

Not sections of these Chapters, but encoded here because notes/PLAN.md §5 assigns them to this group:

| provision | disposition | functions |
| --- | --- | --- |
| s 6 | the roll-up (s 6 itself is a convention in pc-general.l4) | `a general exception applies` (`General Exception Facts`, nesting every record above) |
| s 26G(5) | encoded | `the accused person may rely on a defence under section 26G(5)` (`Transferred Defence Facts`) |
| s 301(2) | encoded | `the accused person may rely on a defence under section 301(2)`, and `a defence or exception in law is available to the accused person` |

## Illustrations: which are tests, and which are not

Every Illustration in these Chapters is a test except these, each for the reason given:

- **s 79 illus (f)** (the look-alike watch) and **s 80 illus (b)** (the malfunctioning crane): each says the accused is not guilty because the OFFENCE's fault element (dishonesty; negligence) is not made out, "There is no need for A to rely on a defence under this section". That is a statement about the theft and s 304A ladders (property's and body-a's), not about this exception, so it cannot be expressed on these atoms. Proposed as a test for those groups: s 79 illus (f) is `NOT commits theft` with `dishonestly` FALSE.
- **s 92 illus (b)** is "[Deleted by Act 51 of 2007]".

Also asserted: s 6 illus (a) (through `exception under s 82` and through the roll-up) and s 6 illus (b) (through `exception under s 76`), which Chapter 2 prints but which are illustrations of these exceptions.
