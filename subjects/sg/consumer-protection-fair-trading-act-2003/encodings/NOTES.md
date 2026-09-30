# Consumer Protection (Fair Trading) Act 2003 — encoding notes

Row `legalese-aswathy`. Status `draft`. **No domain expert has read this against the source, and no independent test pass has been run** (section 6).

## 1. What is encoded and what is not

The whole Act as printed in Singapore Statutes Online's PDF, "Current version as at 30 Sep 2026": ss 1 to 44 and the First, Second, Fourth and Fifth Schedules (the Third is repealed). Eight modules and seven test modules; the shared nouns are in `cpfta-types.l4` (DECLARE only), which every other module imports.

| module | covers |
| --- | --- |
| `cpfta-types.l4` | every noun: the fact records, enumerations and the deontic party/action types |
| `cpfta-part1.l4` | s 2 definitions, First Schedule |
| `cpfta-part2-practices.l4` | ss 3 to 5, the whole Second Schedule (Parts 1 and 2) |
| `cpfta-part2-redress.l4` | ss 6 to 12, Fourth and Fifth Schedules |
| `cpfta-part3-goods.l4` | ss 13 to 18 |
| `cpfta-part3a-investigation.l4` | ss 19 to 26 |
| `cpfta-part3b-offences.l4` | ss 27 to 34 |
| `cpfta-part4-general.l4` | ss 35 to 44 |

**Shape of the encoding.** The Act is a statute of definitions, tests and powers. Each test is a `BOOLEAN` rule over a record of facts a witness could testify to. Where a court, the Commission or the Minister "may", the rule says whether the power is *available* on the facts, never whether it will be exercised. Two things are regulative: the 14-day duties to notify or inform the Commission (ss 9(4)(d), 10(6)(c)) and, without a deadline, ss 9(4)(e)/(f). Nothing else in the Act is a duty with a deadline that the text states.

**Not encoded, and why** (section 2 has the row-by-row account):

- the other Acts the Act points at (Sale of Goods Act 1979, Supply of Goods Act 1982, Hire-Purchase Act 1969, Unfair Contract Terms Act 1977, Small Claims Tribunals Act 1984, Limitation Act 1959, and others). Their answers are facts in the records.
- every regulation or order the Act lets the Minister make. None is an input. Each is a named `REFUSE` (section 4).
- the Legislative History, Abbreviations and Comparative Table, which are not part of the Act.

## 2. Coverage table

Disposition: `encoded` (a rule in the module named), `inert` (quoted, but adds no condition or answer; the reason is given), `refuse` (the Act delegates and nothing supplies the answer: a named `REFUSE`). No row is `deferred`.

| provision | heading | disposition | where |
| --- | --- | --- | --- |
| 1 | Short title | inert: names the Act | — |
| 2(1) "supplier" | | encoded | part1 |
| 2(1) "consumer", 2(2) | | encoded | part1 |
| 2(1) "consumer transaction"; First Schedule para 1(a),(b) | | encoded | part1 |
| 2(1) "financial product", "financial services", 2(3) | | encoded | part1 |
| 2(1) "goods", "voucher", "residential property" | | encoded | part1 |
| 2(1) "services", "time share contract", "time share rights" | | encoded | part1 |
| 2(1) "material fact"; "motor vehicle sale contract" ("motor vehicle", "motor vehicle dealer") | | encoded | part1 |
| 2(1) "specified dispute resolution scheme" | | refuse (s 43(2)(k)) | part1 |
| 2(1) "specified body" | | encoded (s 8) | part2-redress |
| 2(1) "chief executive", "Commission", "flat", "hire-purchase agreement", "Small Claims Tribunal", "unfair practice", "time share related contract" | | inert: a role, a physical description or a pointer to another Act; each is a fact in a record | types |
| 3 | Application of Part | encoded | part2-practices |
| 4(a) to (d) | Meaning of unfair practice | encoded | part2-practices |
| 5(1), 5(2), 5(3)(a) | Circumstances surrounding unfair practice | inert: they widen what counts or direct the fact-finder; the rule for s 4 takes no timing or repetition fact | part2-practices |
| 5(3)(b) | | encoded | part2-practices |
| 6(1) to (3), (5), (6) | Consumer's right to sue | encoded | part2-redress |
| 6(4) | value of residential property | encoded (fork F1) | part2-redress |
| 6(7) to (9) | stay and discontinuance | encoded | part2-redress |
| 7(1), (2), (4) | Jurisdiction | encoded | part2-redress |
| 7(3), (6) | | inert: point into the Small Claims Tribunals Act 1984 | — |
| 7(5), (7), (8), (9) | Powers of courts | encoded | part2-redress |
| 7(10), (11) | | encoded | part2-redress |
| 8(1) to (5) | Voluntary compliance agreement | encoded | part2-redress |
| 8(6) to (9) | civil debts and bar | encoded | part2-redress |
| 8(10), (11) | specified body | encoded | part2-redress |
| 9(1) to (4) | Declaration or injunction | encoded | part2-redress |
| 9(4)(d) | 14-day notification | encoded, regulative | part2-redress |
| 9(4)(e), (f) | | encoded, regulative, no deadline stated (fork F13) | part2-redress |
| 9(5), 9(13) | | inert: what "details" include; effect despite contempt proceedings | — |
| 9(6) to (11) | periods and extensions | encoded | part2-redress |
| 9(12) | cancellation within 6 months | encoded; mechanics refuse (s 43(2)(m)) | part2-redress |
| 9(14), 9(15) | conclusive proof; notifiable event | encoded | part2-redress |
| 10(1), (4) | Injunction against abettors | encoded | part2-redress |
| 10(2), (3), (5) | | inert: "whether or not" clauses; the rule takes none of those facts | — |
| 10(6)(c), (8), (9), (10) | | encoded | part2-redress |
| 10(6)(a), (b), (7), (11) | | inert: available whenever an injunction is granted; no separate condition | — |
| 11 | Right to cancel certain contracts | refuse (no class, no period) | part2-redress |
| 12(1) to (5) | Limitation | encoded (forks F4, F7, F8) | part2-redress |
| 12(6) | | inert: the knowledge date is a fact about the facts, not the law | types |
| 12(7), (8), (9) | | encoded (knowledge, Fourth Schedule); Limitation Act 1959 otherwise not encoded | part2-redress |
| 13(1) | Part 3 definitions | inert: pointers to other Acts; facts in `Non-conforming Goods Facts` | types |
| 13(2) to (5) | | encoded | part3-goods |
| 14(1) to (4) | Application of Part | encoded (fork F3) | part3-goods |
| 15(1) to (4) | Repair or replacement | encoded | part3-goods |
| 15(5) | | inert: guides the finding of reasonable time and inconvenience | — |
| 16 | Reduction or rescission | encoded | part3-goods |
| 17 | Relation to other remedies | encoded (fork F2) | part3-goods |
| 18(1) to (5), (7) | Powers of court | encoded | part3-goods |
| 18(6) | | inert: discretion to make orders on terms, no condition | — |
| 19(1) to (4) | Power to investigate | encoded | part3a |
| 19(5) | | inert: definition | — |
| 20(1), (2) | Documents, articles, information | encoded | part3a |
| 20(3), (4), (5) | | inert: extend the power, add no condition | — |
| 21(1) to (4) | Entry without warrant | encoded | part3a |
| 21(5) | | encoded as availability of entry | part3a |
| 22(1), (2), (4), (6) to (10) | Entry under warrant | encoded (fork F5) | part3a |
| 22(3), (5), (11) | | inert: list of what a warrant authorises; equipment may stay on site; definitions | — |
| 23 | Post-seizure procedure | encoded | part3a |
| 24, 25 | Identity; examination | encoded | part3a |
| 26 | Self-incrimination | encoded | part3a |
| 27 to 30 | Offences | encoded | part3b |
| 31 | No relief after seizure | encoded | part3b |
| 32, 33(1) to (2), (5) | Corporations, associations, partnerships | encoded (fork F6) | part3b |
| 32(3), (4), (6); 33(3), (4), (6) | | inert: defence and burden, savings, definitions | — |
| 34(1), (2) | Composition | encoded | part3b |
| 34(1) which offences | | refuse (s 43(2)(n)) | part3b |
| 34(3), (4) | | inert: administrative | — |
| 35 to 40 | No contracting out; rights transferred; other remedies; publishers; parol evidence; interpretation | encoded | part4 |
| 37(2) | | input: whether regulations provide to the contrary | part4 |
| 41(1), (2) | Burden of proof | encoded; which requirements are specified is an input | part4 |
| 41(3) | | inert: saving | — |
| 42, 43 | Amendment of Schedules; Regulations | refuse | part4 |
| 44 | Saving and transitional | encoded | part4 |
| First Schedule | Excluded transactions | encoded | part1 |
| Second Schedule Part 1, paras 1 to 27 | Specific unfair practices | encoded, one `WHEN` arm each | part2-practices |
| Second Schedule Part 2, paras 1 to 3 | Interpretation | encoded | part2-practices |
| Third Schedule | Repealed | inert: no content | — |
| Fourth Schedule, paras 1 to 3 | Limitation Act modifications | encoded | part2-redress |
| Fourth Schedule, para 4 | | inert: negative saving | — |
| Fifth Schedule, paras 1 to 4 | Events to be notified | encoded | part2-redress |

## 3. Answer tables

### 3.1 Every number, period and date in the Act

| provision | quantity | value | rule |
| --- | --- | --- | --- |
| 2(1) "time share contract" | period of rights | not less than 3 years | `the contract is a time share contract` |
| 6(6) | prescribed limit | $30,000, or the Minister's amount | `the prescribed limit` |
| 6(9) | discontinuance after a stay | 2 or more years with no step | `the court may of its own motion discontinue the stayed proceedings` |
| 6(4)(c) | value of residential property, last resort | one-tenth of the last transacted price | `the value of residential property` |
| 9(4)(d) | notify the Commission | within 14 days | `the supplier's duty to notify ...` |
| 9(7), 10(8) | specified period | not exceeding 5 years, or the Minister's | `the specified period is within the ceiling ...` |
| 9(10), 10(9) | aggregate with extensions | not exceeding 10 years after the order, or the Minister's | `the court may extend the specified period` |
| 9(12) | cancellation | within 6 months after the contract | `the consumer may cancel the contract` |
| 10(6)(c) | inform the Commission | within 14 days | `the injuncted individual's duty ...` |
| 12(1) | action under s 6 | 2 years after the later of the last material event and the consumer's knowledge | `the last day for commencing the action` |
| 12(2) | action under s 8(6) to (8) | 1 year after the failure | same |
| 12(3) | action under s 9 | 2 years after the later of the last material event and, if alleged, the consumer's knowledge | same |
| 12(4) | action under s 10 | 2 years after the last material event | same |
| 12(5) | action under regulations under s 11 | 1 year after cancellation | same |
| Fourth Schedule 1 to 3 | disability | 1 year after ceasing to be under a disability or dying | `the Fourth Schedule extends the time ...` |
| 14(1)(c) | contract made | on or after 1 September 2012 | `this Part applies` |
| 14(3) | presumption | non-conformity within the 6 months starting after delivery | `the lack of conformity appeared within 6 months after delivery` |
| 21(2)(a) | notice of entry | at least 2 working days | `the notice requirements of section 21(2) are met` |
| 22(6) | warrant | in force for one month beginning on the day issued | `the warrant is valid in form and in force when exercised` |
| 27(1), 28, 29(3), 30 | penalty | fine not exceeding $10,000 or imprisonment not exceeding 12 months or both | `the maximum penalty for the offence` |
| 34(1) | composition | not more than the lower of one half of the maximum fine and $5,000 | `the most that may be collected in composition` |
| Fifth Schedule 4 | interest in a supplier company | at least 15% of voting power or issued shares | `the event is a notifiable event` |
| 44 | Board's matters | commenced before 2 April 2018 and pending on that date | `the Commission may continue the matter ...` |

### 3.2 The Second Schedule, Part 1: what makes each paragraph a specified practice

The constructor is `Paragraph N` in `Second Schedule Practice`. "Untrue" means a representation was made and is not accurate.

| para | practice is specified when | | para | practice is specified when |
| --- | --- | --- | --- | --- |
| 1 | representation untrue | | 15 | supplier represents a voucher will be honoured **and** knows or ought to know it will not |
| 2 | representation untrue | | 16 | objective-form representation, primarily to sell, **not** stating it is an advertisement |
| 3 | representation made and false or misleading | | 17 | represents a person has offered or agreed **and** the person has not |
| 4 | representation untrue | | 18 | representation untrue |
| 5 | represents goods new or unused **and** (untrue **or** deteriorated or altered) | | 19 | offers gifts or prizes **and** knows or ought to know they will not be given as offered |
| 6 | untrue **and** supplier knows | | 20 | represents a discount for a stated period **and** knows or ought to know it will last substantially longer |
| 7 | untrue **and** knows or can be expected to know **and** no limitation clearly stated | | 21 | representation untrue |
| 8 | representation untrue | | 22 | invitation or offer **and** intent to promote other goods **and** any of refusing to show, refusing an order, refusing to supply in time, showing a defective sample |
| 9 | representation untrue | | 23 | omits, hides in small print or misleads, as to a material fact, in connection with supply |
| 10 | estimate given **and** price substantially higher **and** no express prior agreement | | 24 | accepts payment **and** (period specified: knows it cannot meet it; none specified: knows it cannot supply in a reasonable period) |
| 11 | representation made **and** deceptive or misleading | | 25 | asserts a right to payment for unsolicited goods or services |
| 12 | representation untrue | | 26 | invoice for unsolicited goods **without** the prominent "not a bill" text **and** no express written acknowledgement |
| 13 | includes terms **and** harsh **and** unconscionable | | 27 | written applicable agreement, no copy given, copy requested, supplier refuses |
| 14 | undue pressure or influence | | | |

### 3.3 What the Act delegates, and what this encoding does about it

| section | delegation | treatment |
| --- | --- | --- |
| 6(6) | Minister may prescribe a different limit than $30,000 | **default is the law**: input `Consumer Action Facts` field, `NOTHING` gives $30,000 |
| 9(7), 10(8) | different maximum than 5 years | input, default 5 |
| 9(10), 10(9) | different maximum than 10 years | input, default 10 |
| 9(11), 10(10) | prescribed periods apply from the date of prescription | encoded |
| 2(1) "specified dispute resolution scheme", 43(2)(k) | schemes specified by regulation | `REFUSE`; s 7(11) takes availability as a fact |
| 9(12), 43(2)(m) | how a contract is cancelled | `REFUSE`; the 6-month right itself is encoded |
| 11 | classes of cancellable contract and periods | `REFUSE` (no fallback in the section) |
| 34, 43(2)(n) | compoundable offences | `REFUSE`; the composition ceiling is encoded |
| 37(2) | regulations restricting other remedies | input boolean |
| 41(2) | requirements to which the burden rule applies | input boolean |
| 42 | orders amending the Schedules | `REFUSE`; the Schedules are encoded as printed |
| 43 | regulations | `REFUSE` |

## 4. Fork register

Every reading below is a choice where the text survives more than one. None is materialised as a switch: each is resolved at encode time and recorded here. F1 to F13 are the ones found. Where I looked and found none, I say so.

| id | provision | readings | taken | why |
| --- | --- | --- | --- | --- |
| F1 | 6(4)(c) | (c) applies "if the annual value, annual rent or monthly rent cannot be ascertained": **(i)** when none of the three can be ascertained; **(ii)** when any one cannot | (i) | On (ii) a dwelling with an annual value but no tenant would be valued at one-tenth of its last price instead of its annual value, which (a) plainly gives. On (i), if the annual value is missing and a rent is known the rule takes the rent although (b) compares it with a value "in paragraph (a)"; that case is not answered by the text and the encoding takes the rent. |
| F2 | 17(1)-(2) | 17(2)(b) is "the transferee requires the goods to be repaired or replaced, as the case may be". Read literally it is the very act 17(1) presupposes, so 17(1) would forbid what triggers it. **(i)** literal; **(ii)** it means a further requirement of the other remedy | (ii) | (i) makes the section self-contradictory. The field is `..., having required repair or replacement, further requires the goods to be repaired or replaced by the other remedy`. |
| F3 | 14(3) | "within the period of 6 months starting after the date on which the goods were delivered": is the last day the 6-month anniversary of delivery, and does non-conformity on the delivery day itself count? | last day is the anniversary (`add months`); the day itself is **not** in the period ("starting after") | the delivery-day non-conformity is not lost: it is s 14(1)(b) directly, needing no presumption |
| F4 | 12, 9(12), 6(9), 14(3) | how "N years/months after" a date lands when the date is 29, 30 or 31 | the library's `add months`, which clamps to the last day of the shorter month (29 Feb 2024 + 24 months = 28 Feb 2026); an action on the corresponding date is in time | tests assert both sides; a court could differ by a day |
| F5 | 22(6) | "one month beginning on the day on which the warrant is issued": last day | the day before the corresponding date one month later, clamped (issued 31 Jan: through 27 Feb) | ordinary reading of "beginning on" |
| F6 | 32(1), 33(1) | s 32(1) names an officer, employee or agent of a corporation; s 33(1) names only an employee or agent of an association or partnership | encoded as printed: an **officer** of an unincorporated association or partnership does not, by 33(1), supply the body's state of mind | the difference is drafting, but it is the text; s 33(2) still reaches officers and partners personally |
| F7 | 12(1) | "whichever occurs later" when the consumer has no date of knowledge | the last material event alone governs | there is no later date to be "later" |
| F8 | 12(3)(b) | the Commission alleges an unfair practice "in respect of any consumer": which consumer's knowledge date | the single date the facts record | the Act does not say what to do with several consumers |
| F9 | 2(1) "supplier" | "includes any employee or agent of the person": the person is one within (a) to (d), or any person | one within (a) to (d) in the course of business | the words follow the definition of the person |
| F10 | 26(2) | protection applies only if the person "claims, before disclosing"; without the claim | no protection from this subsection | the text ties the protection to the claim |
| F11 | 19(3)(b) | "on demand, produce": is compliance vacuous where no demand was made | the field is TRUE if the card was produced whenever demanded, including where it was never demanded | the duty arises only on demand |
| F12 | Second Schedule para 26 | the printed quotation ends `money.,` | the encoding takes the intended words, "This is not a bill. You are not required to pay any money." | the trailing comma is an extraction artefact in the PDF text; para 26 says "or words to that effect" |
| F13 | 9(4)(e), (f) | the individual "must inform the Commission in writing if a notifiable event occurs in a specified period": no time is stated (contrast (d), 14 days) | encoded without a `WITHIN` | adding one would invent it |
| F14 | 22(1), 22(6) | whether a warrant that names no officer is "valid in form": 22(6) lists only the subject-matter and offences-copy requirements, but 22(1) has the court authorise "by name an investigation officer and one or more authorised assistants" | it is not valid in form; `the warrant is valid in form and in force when exercised` now requires the naming as well | found by the independent test pass (section 6, item 1): an unnamed warrant is not a 22(1) warrant, and nobody could exercise it. Before 2026-09-30 the rule built validity from 22(6) alone. |

**Where I looked and found no fork**: the ss 19 to 25 powers and duties; ss 27 to 30 elements (checked each against "knowing or reckless", "reasonable excuse" and the burden words); s 34(1) (the "lower of" is unambiguous); Part 3's transferee and transferor; s 7(1) and (2). A reviewer should not treat that as proof there are none: fork completeness cannot be established (SKILL step 9).

## 5. What `check.sh` prints, and #TRACE

Run on `l4` from `legalese/prereleases` tag `unstable-20260926-c76e6b0`, 2026-09-30:

```
module                                    errors satisfied  failed
cpfta-part1.l4                                 0         0       0
cpfta-part2-practices.l4                       0         0       0
cpfta-part2-redress.l4                         0         0       0
cpfta-part3a-investigation.l4                  0         0       0
cpfta-part3b-offences.l4                       0         0       0
cpfta-part3-goods.l4                           0         0       0
cpfta-part4-general.l4                         0         0       0
cpfta-tests-part1.l4                           0        61       0
cpfta-tests-part2-practices.l4                 0       127       0
cpfta-tests-part2-redress.l4                   0       166       0
cpfta-tests-part3a-investigation.l4            0        94       0
cpfta-tests-part3b-offences.l4                 0        67       0
cpfta-tests-part3-goods.l4                     0        70       0
cpfta-tests-part4-general.l4                   0        41       0
cpfta-types.l4                                 0         0       0
tests-independent.l4                           0       651       0
TOTAL (16 modules)                             0      1277       0
```

(The first 15 modules, without `tests-independent.l4`, total 626 assertions.) No test is meant to fail. The harness can fail (a scratch file with `#ASSERT 1 EQUALS 2` prints `errors 1, failed 1` and exits 1), so the 0 is not vacuous. The 626 were written from the text of each provision, on both sides of each threshold in 3.1 and both polarities of each Second Schedule paragraph, by the same session that wrote the rules. `tests-independent.l4` is the independent pass (section 6).

`#TRACE` results are printed, not asserted (L4 cannot assert them). Read by eye on 2026-09-30:

- `the supplier's duty to notify the Commission of a business change event`, act at day 14: `FULFILLED`; waiting to day 15: `DEONTIC BREACHED ... BY The supplier BECAUSE "... within 14 days ..."`.
- `the injuncted individual's duty ...`, act at day 14: `FULFILLED`; day 15: breached, BY The individual.

## 6. Open questions, and what has not been done

1. **Independent test pass run, 2026-09-30.** A fresh agent that had not seen the encoding fixed its expected answers from the source, then wrote `tests-independent.l4` (651 assertions; report in `INDEPENDENT-TEST-REPORT.md`). It disagreed once: an unnamed warrant was valid in form under 22(6) alone. The rule now also requires the naming (F14) and all 651 pass. The agent read the modules for names and signatures, so it was not blind to the logic. Not tested by it: the 14-day duties in 9(4)(d) to (f) and 10(6)(c), F1's partial cases, several edge days (14(3), the warrant's last day, the Fourth Schedule year, leap days in s 12), 8(10) and (11), and the inert provisions.
2. **HG1 (fidelity) has not been sought.** A Singapore consumer-law reader should go section by section, especially Part 2's records (the Second Schedule constructors have a long field per fact), s 12 (limitation), and F1 to F14.
3. **The source is an unofficial SSO consolidation.** No authoritative text (the printed 2020 Revised Edition, the Gazette) was compared.
4. **Is the modelling of "whether the court will" versus "whether the court may" the right level for s 7(5), s 9 and s 10?** The encoding answers availability only.
5. **s 12 knowledge.** Would a reviewer prefer the three dates (actual, observable, expert-advice) as separate rules per s 12(1)(b)(i) and (ii) (knowledge that a representation is false, versus knowledge that advantage was taken)? They are one date here.
6. **Regulations under ss 6, 9, 11, 41, 43.** Have any been made? None was an input; if the Consumer Protection (Fair Trading) Regulations or an order under s 6(6) exists, it should be fetched and encoded, and the `REFUSE`s in 3.3 retired one at a time.
7. **s 8 "specified body"** is per Act 5 of 2025 (the marginal note `[Act 5 of 2025 wef 09/03/2025]`). Its earlier text, if a reviewer needs it, is not an input.

## 7. The pipeline run

The l4-ide pipeline was run over this encoding on 2026-09-30 (run `2026-09-30-0ee01ac6-006`): verdict **PROVISIONAL**. p0-preflight, p3-check, p6-tests (626 assertions, 0 failed), p8-verify (0 findings) and p9 PASS; no projection leg is declared, HG1 is provisional, and P1, P2, P4, P5 were not run. `pipeline/README.md` has the stage table, what the run did not do, and how to reproduce it: **the driver does not run natively on Windows** and the run used a patched scratch copy, with nothing changed in `legalese/l4-ide`.

`projections/` holds DMN for the seven rule modules and BPMN for the three duties, from `l4 export` run directly. They are not pipeline artefacts and were not executed on an engine; the DMN exports carry 1 to 19 blocking findings each (`.fidelity.txt`).
