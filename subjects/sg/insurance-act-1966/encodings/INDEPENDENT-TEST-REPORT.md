# Independent test report: Insurance Act 1966 (Singapore)

## How this was done

1. I read `BRIEF.md` and `../source/IA1966.txt` and nothing else. I wrote 221 expectations (E001-E221), each with the provision it rests on, to `independent-expectations.md` before opening any `.l4` file. They have not been changed since.
2. I then read `ia-types`, `ia-penalties`, `ia-permission`, `ia-supervision`, `ia-policies` and `ia-goal` for their names and inputs. I opened `ia-tests.l4` only to copy syntax (how record constructors and `JUST`/`YMD` are written), never for its values. Then I wrote `tests-independent.l4`.
3. I ran `l4 check`, `l4 run` and `check.sh` with `~/.local/bin/l4`. Two fixes were needed, both plumbing only:
   - parentheses around `(...)'s \`fine\``;
   - one helper used the wrong way round (E146: "constituted on 5 April is late" is now asserted as "the deadline is on or before 4 April").

   No expected value was changed.

## Counts

| | |
|---|---|
| Expectations written | 221 |
| Expectations expressed as assertions | 201, in 213 `#ASSERT` directives |
| Expectations not expressible against the encoding | 20 (listed below) |
| Assertions passing | **212** |
| Assertions failing | **1** |
| Assertions refusing instead of answering | **0** (`l4 run ... \| grep -i warning` finds nothing) |

`check.sh` output for this file: `errors 1, satisfied 212, failed 0`. The single error is the failed `#ASSERT REFUSED`. In the `l4 run` output, the "assertion failed: expected a refusal ..." text sits on the line after `Message:`. `check.sh` looks for it on the same line, so it does not count this as a failed assertion. It only shows up as an error. **That is a gap in `check.sh`**: a failing `#ASSERT REFUSED` is counted as an error but never as a failure.

## The disagreement

### E188: capacity of a child under 10 (s 147(1))

- **Scenario.** An 8-year-old enters a contract of insurance with written parental consent.
- **My expectation.** The Act gives no answer, so the encoding should REFUSE. s 147(1) says only that "a person over the age of 10 years does not, by reason only of his or her age, lack the capacity". It then limits under-16s to contracting with consent. It says nothing about anyone aged 10 or under, so the common law of minors' contracts governs them, outside the Act.
- **What the encoding gives.** `has capacity to insure, aged 8, with consent: TRUE` returns **FALSE**. The rule is `age GREATER THAN 10 AND (age AT LEAST 16 OR consent)`.
- **Which reading is right.** Mine. The section is a "despite any law to the contrary" relaxation for over-10s. It does not take capacity away from younger children. Returning FALSE turns the Act's silence into a negative answer, which the brief forbids ("Where the source does not answer, `REFUSE`, never `FALSE`"). The fix is to `REFUSE` when age is 10 or under.

There were no other disagreements. Every penalty figure, threshold, period and ranking I derived from the text matched the encoding. That includes the trickier points:
- s 27(7) gives an individual no imprisonment.
- s 89(1)(a) allows a broker's non-employee director no unsecured loan at all.
- s 143 doubles the fine for single-penalty offences (ss 64, 70, 75, 87, 124) but not for split penalties or for duties that fall only on corporations (s 88(8)).
- Under s 142(5), an officer convicted of the s 88(8) offence faces 2 years.
- Composition under s 142(7) is half the maximum fine.
- The A/B × C formulas in ss 133(5)(c) and 150(11) work out.
- s 123 ranks the classes and abates claims within a class.
- The First Schedule residence tests at 183, 90 and 5 years, and the treaty test at "more than 25%", are right.

## Expectations that could not be expressed (20)

| # | Why |
|---|---|
| E016, E017 | s 5(1)(b): no rule makes the directors, partners or officers of a firm that holds itself out liable unless they prove lack of knowledge or consent. s 142(4) is encoded only through the penalty for an officer who did not prove due diligence. |
| E020 | s 6(3): there is no input for a registered representative office using "insurance". |
| E031 | s 8(4): the advertising publisher's defence is not encoded. |
| E033 | s 9(3): registration criteria (applicant must be a company) are not encoded. |
| E044 | s 66(4)-(5): agreements contrary to s 66 being void, and the premium set-off exception, are not encoded. |
| E076 | s 34(2): no input separates foreign-incorporated insurers or insurance-fund assets. s 34(1)'s test is applied to every licensed insurer. |
| E081 | s 35(8): reappointment on expiry without fresh approval is not encoded. |
| E082, E086 | ss 35(5), 36(1)(b): the director and chairperson limbs apply only to Singapore-incorporated insurers. The encoding has no incorporation input, so a foreign-incorporated insurer appointing a director is treated as needing approval or consent. |
| E087 | s 36(1)(c): the kind of conviction is decided by the caller, inside one "disqualification" boolean. |
| E154 | s 123(2): preferential debts are handled by asking the caller for the assets left after them. They are not computed. |
| E174, E175 | First Schedule para 9(2)-(3): a term that is short only because of the insured's age, and an extension option, are both folded into one input boolean. |
| E201 | s 132(7): "a parent or legal guardian, not being the policy owner" is folded into one consent boolean. |
| E208 | s 133(6): the rule that the younger is deemed to survive the elder exists only as text. |
| E211 | s 133(7)(b)(ii): whether a later will specifies the policy's particulars is folded into one boolean. |
| E219, E220, E221 | s 150(8)(f), (12): who counts as a "proper claimant" (nephew yes, cousin no), and payment to the personal representatives of a nominee who outlives the owner, appear only inside strings. Nothing returns a value that can be tested. |

Some expectations could be asserted, but only by setting the caller's boolean to the conclusion. They prove little about the encoding:
- E011, E012: s 4(2)(b)(iii) notification, and the (a)-(f) versus (g) exempt-broker split, are one "unsolicited" boolean.
- E038, E039, E040: the life-policy and non-reinsurance limits in s 64(4)-(5) are one boolean.
- E090: s 37(2) relatives are one boolean.
- E164: the "longer than 90 days" pass duration is part of the residence status.
- E165: owner or insured residence is one input.

## Parts of the Act the encoding misses or simplifies

1. **s 147 below age 10.** It answers FALSE instead of refusing (the failure above).
2. **s 132(7) revocation.**
   - (c), "such requirements ... as may be prescribed", is not an input.
   - Where there is no outside trustee and a nominee has died, the text of (b) imposes no consent requirement ("so long as no nominee has died"). The encoding then answers that the nomination *cannot* be revoked. I did not fix an expectation on this before reading the code, so it is an observation, not a counted failure. I think the literal text points the other way, and at minimum it is a fork worth recording.
3. **Incorporation.** There is no input for whether an insurer is incorporated in Singapore. That loses:
   - the director and chairperson limbs of s 35(2), (5), (9) and s 36(1)(b);
   - s 34(1) versus (2);
   - s 26/27, which apply only to insurers incorporated in Singapore.
4. **s 35.** These limbs are not encoded: (1) and (2), the duty to *have* a chief executive, actuary and chairperson; (8), reappointment; and (9), term limits. The offence for an appointment that is both unapproved and disqualified maps to s 35(16), not s 36(2).
5. **s 5 and s 142(4) officer liability.** s 5(1)(b)'s separate liability for partners and LLP managers, which comes with a burden of proof, is absent.
6. **Defences and exceptions.** These are not encoded:
   - s 8(4), the publisher's defence;
   - s 30's defences, of which only the 14-day timing is encoded;
   - s 66(4)-(5);
   - s 89(2), increasing a loan made before 2002;
   - s 34(3), the transitional period.
7. **s 145(3).** Regulations disapplying s 145(2) are not an input.
8. **First Schedule.**
   - Paragraph 2(1)(a)(ii), the non-individual address and insured tests, and 2(1)(b)(ii), residence and permanent establishment, are collapsed into one boolean.
   - Facultative reinsurance, paras 2(5)-(6), is absent.
   - Para 9(2)-(3) are folded into one boolean.
9. **s 150.** Who may be paid is returned as text, so the s 150(12) "proper claimant" test, s 150(8)(f) and s 150(1)'s living benefits cannot be computed or tested.
10. **s 111.** (b) purpose and (g)-(i) are merged into one "assessment" input, and (d)-(f) into one "undertakings" input. That is acceptable, since they are the Authority's satisfaction.
11. **Forks I took no position on before reading, but note.**
    - F2: the encoding doubles the *daily* continuing fine for corporations, e.g. s 75 gives $15,000 a day.
    - F3: composition uses the undoubled fine, e.g. s 75 corporate gives $37,500.

    Both are defensible readings of ss 142(7) and 143(1), but neither is beyond argument.

## Files

- `independent-expectations.md`: the 221 expectations, fixed before any code was read.
- `tests-independent.l4`: 213 assertions, each tagged with its E-number.
- this report.
