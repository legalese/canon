# Business Names Registration Act 2014 — encoding notes

Status `draft`. **No domain expert has read this against the source.** An independent test pass was run on 2026-09-30 (section 6).

## 1. What is encoded and what is not

The whole Act as printed in Singapore Statutes Online's PDF, "Current version as at 30 Sep 2026": ss 1 to 45. The Act has no Schedules. Five rule modules and five test modules over one nouns module, `bnra-types.l4` (DECLARE only), which every other module imports.

| module | covers |
| --- | --- |
| `bnra-types.l4` | every noun: the fact records, enumerations and the deontic party and act types |
| `bnra-part1.l4` | ss 2 to 4: the definitions, carrying on business in Singapore, the exemptions |
| `bnra-part2-registration.l4` | ss 5 to 14: the requirement, the application, the decision, authorised representatives, cancellation, expiry |
| `bnra-part2-names.l4` | ss 15 to 24: use, reservation and restriction of names, changes, cessation, cancellation, restoration |
| `bnra-part2-register.l4` | ss 25 to 31: rectification, copies, the electronic system, contact address, disability of defaulters |
| `bnra-part3.l4` | ss 32 to 45: inspection, offences, composition, records, enforcement, bodies corporate, service, transitional |

**Shape.** The Act is a registry statute: definitions, tests for who must register and what the Registrar may or must do, and a set of notice duties with 14- and 30-day deadlines. Each test is a `BOOLEAN` rule over a record of facts a witness could testify to. Where the Registrar, a court or the Minister "may", the rule answers whether the power is *available*, never whether it will be exercised. The notice duties are regulative rules (ss 11(4), 11(7), 11(9), 11(11), 17(4), 19(1), 20(1), 20(3), 22(1)), with the deadline as `WITHIN`, and most also as a date rule (`the last day for ...`) so a case can be checked against a calendar.

**Not encoded, and why** (section 2 has the row-by-row account):

- the other Acts the Act points at (Companies Act 1967, Limited Liability Partnerships Act 2005, Limited Partnerships Act 2008, National Registration Act 1965, Charities Act 1994, Central Provident Fund Act 1953, Trade Marks Act 1998, and others). Their answers are facts in the records.
- every regulation and order the Act lets the Minister make. None is an input. Each is either an input fact or a named `REFUSE` (section 3.3).
- the Legislative History, Abbreviations and Comparative Table, which are not part of the Act.

## 2. Coverage table

Disposition: `encoded` (a rule in the module named), `inert` (quoted, adds no condition or answer; the reason is given), `refuse` (the Act delegates and nothing supplies the answer: a named `REFUSE`). No row is `deferred`.

| provision | heading | disposition | where |
| --- | --- | --- | --- |
| 1 | Short title | inert: names the Act | — |
| 2(1) "business", "individual", "corporation", "firm" | | encoded | part1 |
| 2(1) "contact address", "full name" | | encoded | part1 |
| 2(1) "authorised representative", "Authority", "certificate of confirmation of registration", "company", "document", "electronic transaction system", "foreign company", "identification", "individual proprietor", "inspector", "notice of registration", "register", "registered", "registered business name", "Registrar", "residential address", "ACRA administered Act", "business name" | | inert: pointers to another Act or section, or plain-word terms; each is a fact or is decided in the section it names | types |
| 2(2), 2(3) | Carrying on business in Singapore | encoded (fork F3) | part1 |
| 2(4), 2(5), 2(6) | | inert: a pointer to the Companies Act, the manner of lodging, who "the Minister" includes | — |
| 3(1) to (5) | Administration; the Registrar | inert: allocations of office and power that no fact of a case can satisfy or fail | — |
| 4(1)(a) to (q), (ja) | Persons not required to be registered | encoded | part1 |
| 4(2) | | encoded with 4(1)(c) | part1 |
| 4(3) | | encoded (fork F8) | part1 |
| 4(4) | | encoded | part1 |
| 4(5) | | inert: a rule of construction | — |
| 5(1), 5(2) | Requirement to register | encoded | part2-registration |
| 6(1) | Application and particulars | encoded | part2-registration |
| 6(2) | | inert: a power to require verification | — |
| 6(3) | "appropriate person", "identification", "registered corporate service provider" | encoded | part2-registration |
| 7(1), 7(2) | Nominee or trustee | encoded | part2-registration |
| 8(1), 8(5) | Registration | encoded (the outcome rule) | part2-registration |
| 8(2) | certificate of confirmation | encoded | part2-registration |
| 8(3) | validity and renewal | inert as to the period (the Registrar's to specify); renewal encoded with 8(4), 8(5) | part2-registration |
| 8(4), 8(5) | renewal | encoded | part2-registration |
| 8(6) | | encoded as a constant FALSE | part2-registration |
| 8(7) | appeal | encoded | part2-registration |
| 9(a), (b), (c) | When registration must be refused | encoded | part2-registration |
| 10(1), 10(2) | Registration does not confer ownership | encoded as constants FALSE | part2-registration |
| 11(1) to (4), (11) | Authorised representative: when, who, deadlines | encoded, regulative for (4) and (11) | part2-registration |
| 11(5), (6) | personal responsibility | encoded | part2-registration |
| 11(7), (8), (9), (10) | notices | encoded, regulative for (7) and (9) | part2-registration |
| 11(12) | offence | encoded | part2-registration |
| 11(13), (14), (15), (16) | definitions | (14) and (16) encoded; (13), (15) inert | part2-registration |
| 12(1) to (4) | General power to cancel | encoded | part2-registration |
| 13(1), (2), (3) | Supplemental provision | encoded | part2-registration |
| 14(1) to (4) | Failure to renew | encoded | part2-registration |
| 15(1), (2), (3) | Use of business names | encoded | part2-names |
| 16(1) to (5) | Reservation | encoded (forks F1, F6) | part2-names |
| 17(1), (2), (3) | Restrictions on registration | encoded (forks F2, F12) | part2-names |
| 17(4), (6), (7), (8) | direction to change | encoded, regulative for (4) | part2-names |
| 17(5), (10) | | inert: applies regardless of inadvertence or date; accept the High Court's injunction as correct, "to avoid doubt" | — |
| 17(9) | appeal | encoded (with 8(7)) | part2-registration |
| 18(1), (2), (3) | Change of registered business name | encoded | part2-names |
| 19(1), (2) | Change of residential address | encoded, regulative for (1) | part2-names |
| 20(1) to (4) | Change in particulars | encoded, regulative for (1) and (3) | part2-names |
| 20(5) | | inert: a power to require verification | — |
| 21(1), (2) | Deceased registrants | encoded | part2-names |
| 22(1) to (4) | Cessation of business | encoded, regulative for (1) | part2-names |
| 23(1) to (3) | Cancellation of registration | encoded (fork F18) | part2-names |
| 24(1) to (5) | Restoration | encoded (fork F7) | part2-names |
| 25(1), (2), (3) | Rectification by the High Court | encoded | part2-register |
| 26(1) to (3) | Rectification on application | encoded | part2-register |
| 26(4) | | inert: the decision is final | — |
| 27(1) to (5), (7) | Rectification on the Registrar's initiative | encoded | part2-register |
| 27(6) | | inert: a power to add a notation | — |
| 28(1) to (3), (5), (6) | Copies | encoded | part2-register |
| 28(4) | | encoded within 28(1) (the excluded-document limb) | part2-register |
| 29(1), (4) | Electronic transaction system | inert: a power and a definition | — |
| 29(2), (3) | | encoded | part2-register |
| 30(1), (2), (3) | Transitional contact address | encoded | part2-register |
| 30(4) | | inert: definition | — |
| 31(1) to (7) | Disability of persons in default | encoded | part2-register |
| 31(8) | | inert: definition | — |
| 32(1) to (5) | Inspection | encoded | part3 |
| 33(1) | Power to obtain information | encoded | part3 |
| 33(2) | | inert: a power to require further particulars | — |
| 34(1), (3) | Undischarged bankrupt | encoded | part3 |
| 34(2) | | inert: a discretion to refuse or approve on conditions | — |
| 35(1), (2), (3) | Offences and penalties | encoded | part3 |
| 36 | Evidence of carrying on business | encoded | part3 |
| 37(1), (2) | Composition | encoded | part3 |
| 37(1) which offences | | refuse (s 43(2)(j)) | part3 |
| 38 | Destruction or transfer of old records | encoded | part3 |
| 39(1), (4) | Enforcement of duty to make returns | encoded | part3 |
| 39(2), (3) | | inert: costs may be ordered; a saving | — |
| 40(1) to (4) | Offences by bodies corporate | encoded | part3 |
| 40(5) | | inert: definitions, fixed in `Role in Body` | — |
| 40(6) | | refuse | part3 |
| 41 | Authority and its employees not liable | encoded | part3 |
| 42(1), (2), (3), (4), (5) | Service of documents | encoded | part3 |
| 43(1), (2) | Regulations | refuse | part3 |
| 43(3) | | encoded in the penalty table | part3 |
| 44 | Saving for other written law | inert: a rule of construction | — |
| 45(2), (4), (5), (8), (9) | Transitional | encoded | part3 |
| 45(1), (3), (6), (7), (10) to (14) | | inert: allocation of office, administrative transfer, savings and continuations, definition | — |

## 3. Answer tables

### 3.1 Every number, period and date in the Act

| provision | quantity | value | rule |
| --- | --- | --- | --- |
| 2(3)(h) | isolated foreign transaction | completed within 31 days | `the foreign company does any of the activities ...` |
| 8(7), 16(5), 17(9) | appeal | within 30 days after notice | `the person may appeal to the Minister within 30 days` |
| 12(4) | appeal | 30 days or a further period the Minister allows | `... or a further period the Minister allows` |
| 11(2) | authorised representative | age 18 or over | `the person qualifies as an authorised representative` |
| 11(4), (11) | appoint an authorised representative | within 30 days | `the duty to appoint ...` |
| 11(7), (9) | notices about the representative | within 14 days | `the duty to lodge notice ...` |
| 11(12), 45(5)(b) | fine | not exceeding $1,000 | `the maximum penalty for the offence` |
| 12(3)(b) | time for representations | at least 30 days | `the procedure of section 12(3) has been followed` |
| 14(2) | renewal notice | at least 30 days after the date of the notice | `the period stated in the notice is long enough` |
| 16(4) | reservation | 60 days after notice of approval, or a further 60 | `the last day of the reservation` |
| 17(2)(a), (e) | waiting period | one year | `the waiting period in years after an earlier use of the name` |
| 17(2)(b)(i), (c), (d)(i) | waiting period | 2 years | same |
| 17(2)(b)(ii), (d)(ii) | waiting period | 6 years | same |
| 17(3)(a)(i) | foreign company that ceased | 3 months | `section 17(3) permits registration of the name` |
| 17(3)(a)(ii) | foreign company struck off | 6 years | same |
| 17(3)(b) | limited partnership that ceased | one year | same |
| 17(4) | change of name | 6 weeks (42 days), or longer if allowed | `the last day for complying with the Registrar's direction` |
| 17(7) | resemblance application | within 12 months | `the Registrar may consider the application for a direction` |
| 19(1), 20(1), 20(3), 22(1) | notices | within 14 days | the `the duty to lodge ...` rules |
| 22(3), 35(3), 43(3) | fine | not exceeding $5,000 (35(3), 43(3) also 12 months) | `the maximum penalty for the offence` |
| 23(1)(b), (2)(b) | objection | at least 30 days; cancellation if none within 30 days | `the Registrar may cancel the registration under section 23` |
| 24(2)(a) | restoration | within 12 months | `the application to restore is made in time` |
| 27(2)(b) | objection | at least 30 days | `the notice requirement of section 27(2) is met` |
| 32(4), 34(1), 35(1) | penalty | fine not exceeding $10,000 or imprisonment not exceeding 2 years or both | `the maximum penalty for the offence` |
| 37(1) | composition | not more than the lower of one half of the maximum fine and $5,000 | `the most that may be collected in composition` |
| 39(1)(a), (b) | make good | within 14 days after service | `the non-compliance was not made good ...` |
| 42(2) | deemed service | personal: date delivered; ordinary post: day after; registered post: 2 days after; fax: day sent; email: when retrievable | `the date the document is deemed served` |
| 45 | commencement | 3 January 2016; 30 days after it is 2 February 2016 | `the last day for appointing ... under section 45(5)` |

### 3.2 What the Act delegates, and what this encoding does about it

| section | delegation | treatment |
| --- | --- | --- |
| 2(3)(l) | other prescribed activities | input fact in `Business Presence Facts` |
| 4(1)(p), 43(2)(e) | persons exempted by the Minister | input fact in `Exemption Facts` |
| 4(2) | professions the exemption does not apply to | input fact |
| 6(1)(b)(ix) | other prescribed particulars | input fact in `Application Facts` |
| 7(1) | prescribed nominee particulars | input fact in `Nominee Facts` |
| 8(2), 8(3), 24(3), 28(1) | fees, late penalty | input facts (paid or not); the amounts are not encoded |
| 17(1)(d) | kinds of name the Minister directs not to accept | input fact in `Name Restriction Facts` |
| 27(2), 28(4), 28(5)(c) | prescribed circumstances, excluded documents, prescribed information | input facts |
| 37, 43(2)(j) | compoundable offences | `REFUSE`; the composition ceiling is encoded |
| 40(6) | modification of s 40 for foreign bodies | `REFUSE` |
| 43 | regulations | `REFUSE`; the s 43(3) penalty is in the penalty table |

## 4. Fork register

Each reading below is a choice where the text survives more than one. None is materialised as a switch: each is resolved at encode time and recorded here.

| id | provision | readings | taken | why |
| --- | --- | --- | --- | --- |
| F1 | 16(4)(a) | "60 days after ... approved, or such further period of 60 days as the Registrar may ... extend": one extension, or repeated | the number of extensions is a fact; each adds 60 days | the text does not cap them |
| F2 | 17(3)(a) | (i) and (ii) are joined by "and": both, or alternatives | alternatives | (i) and (ii) describe different events (a foreign company that ceased business; one whose name was struck off) |
| F3 | 2(3) | "for the reason only that" it does one of (a) to (l) | not treated as carrying on business if it does any of them and has no other reason | the words "for the reason only" |
| F4 | 2(1) "individual" | "where appropriate, includes" an administrator etc "having direct control or management" | an administrator, executor, liquidator, trustee, nominee, guardian, donee or deputy counts only with direct control | the words follow the whole list |
| F5 | 9(b), 12(1)(a)(ii), 13(1) | the certificate is "conclusive evidence of the matters so stated" | it makes the Registrar's satisfaction established | that is what conclusive evidence does |
| F6 | 16(3)(b) | whether the certificate applies to reservation | no: s 13(1) names ss 9(b) and 12(1)(a)(ii) only | the text |
| F7 | 24(1) | it lists cancellation under ss 12(2), 14, 23 and cessation under s 22, and omits s 12(1) | encoded as printed: a registration cancelled under s 12(1) cannot be restored under s 24 | the text; the 2024 amendment changed the reference from s 12 to s 12(2), which looks deliberate |
| F8 | 4(3) | "(e) to (o)" and where (ja) sits | (ja) is inside the range, as its letter places it | alphabetical order |
| F9 | 17(2) | "a period of at least N years has passed after the date" | the anniversary date counts as passed | ordinary reading; `add months` |
| F10 | 17(4) | "6 weeks" | 42 days | 6 x 7 |
| F11 | 14(3) | "if the registration is not renewed within the period stated" | the Registrar may cancel from the day after the last day of the period | the period has then run |
| F12 | 23(2)(b) | "within 30 days after sending the notice" | measured from the date of the notice | the date of sending is the date of the notice |
| F13 | 39(1)(a), (b) | a person who never made good the default: when is the 14th day tested | at the date the court considers the Registrar's application | the court's application is when the failure is in question |
| F14 | 8(7), 12(4), 13(2), (3) | the person "aggrieved" may appeal against a refusal or cancellation; whether the Minister's certificate excludes appeal | s 13(2) and (3) exclude it only for a refusal under s 9(b) or a cancellation under s 12(1)(a)(ii) resting on the certificate | the text |
| F15 | 42(2)(e) | "at the time the email becomes capable of being retrieved" | the date is used; the time of day is not modelled | the rules are date-based |

**Where I looked and found no fork**: ss 5, 7, 8(1) and (5) (the order of refusal and non-satisfaction is unambiguous), 10, 18, 19, 20(1) to (4), 22, 25 to 27, 30, 31, 32 to 38, 40, 41, 45. A reviewer should not treat that as proof there are none.

## 5. What `check.sh` prints, and #TRACE

Run on `l4` from `legalese/prereleases` tag `unstable-20260926-c76e6b0`, 2026-09-30:

```
module                                    errors satisfied  failed
bnra-part1.l4                                  0         0       0
bnra-part2-names.l4                            0         0       0
bnra-part2-register.l4                         0         0       0
bnra-part2-registration.l4                     0         0       0
bnra-part3.l4                                  0         0       0
bnra-tests-part1.l4                            0        78       0
bnra-tests-part2-names.l4                      0       154       0
bnra-tests-part2-register.l4                   0        60       0
bnra-tests-part2-registration.l4               0       164       0
bnra-tests-part3.l4                            0       163       0
bnra-types.l4                                  0         0       0
TOTAL (11 modules)                             0       619       0
```

No test is meant to fail. The harness can fail (a scratch file with `#ASSERT 1 EQUALS 2` prints `errors 1, failed 1` and exits 1), so the 0 is not vacuous. The assertions were written from the text on both sides of each threshold in 3.1; they were written by the same session that wrote the rules; the independent pass is `tests-independent.l4` (599 assertions, all satisfied; report in `INDEPENDENT-TEST-REPORT.md`).

`#TRACE` results are printed, not asserted (L4 cannot assert them). Read on 2026-09-30, for each of the nine regulative rules: an act on the last day (day 14, day 30 or day 42 as the rule says) gives `FULFILLED`; waiting one day longer gives `DEONTIC BREACHED ... BY` the named party with the section's reason.

## 6. Open questions, and what has not been done

1. **Independent test pass run, 2026-09-30.** A fresh agent fixed its expected answers from the source before opening the encoding, then wrote `tests-independent.l4` (599 assertions, 0 failed). It read the modules for names and signatures, so it was not blind to the logic. Gaps it found: the s 11(12) offence has no field for a failure under s 11(11); s 40(5) counts a partner as an officer but the role list has no partner; s 2(1) "business" for a trade not carried on for gain is ambiguous and untested. Untested: leap-day anniversaries, the regulative deadlines in ss 11(9), 11(11), 19(1), 20(1), 20(3), and the inert provisions. Original note:
2. **HG1 (fidelity) has not been sought.** A Singapore company-law reader should go section by section, especially ss 4, 11, 17 and 24, and F1 to F15.
3. **The pipeline has not been run** on this encoding.
4. **The source is an unofficial SSO consolidation.** No authoritative text was compared. The PDF was downloaded by hand (SOURCE-LICENSE.md).
5. **Regulations.** None is an input. The Business Names Registration Regulations, if any, should be fetched and the input facts in 3.2 retired one at a time.
6. **s 24(1) and s 12(1).** Is the omission of a cancellation under s 12(1) from the restoration provision deliberate (fork F7)?
7. **Time of day.** s 42(2)(e) turns on the time an email becomes retrievable; the encoding works in dates.
