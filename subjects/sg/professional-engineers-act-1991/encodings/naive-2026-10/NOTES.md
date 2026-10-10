# Professional Engineers Act 1991 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 15
of 2026 (s 21(2A), (2B), in force 1 January 2026) and Act 25 of 2024 (in force
1 October 2025) shown.

**Checks:** one case file, 138 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. This row takes what an
engineer, a firm, a builder or a client meets: who may do, sign, offer and supply
professional engineering work and who may use the title (ss 15, 17, 18, 19, 20 and
the Schedule), compulsory voting (s 5), removal and re-registration (ss 26, 27),
practising certificate deadlines (s 28), disciplinary sanctions and when they take
effect (ss 50, 51), offence penalties (ss 15(10), 17, 54(6), 58) and the Board's
immunity (s 63). The Board's constitution, registration qualifications, specialist
registration, Part 6 corporate licensing, the complaint machinery and ss 59-62 are
not encoded.

The case file is larger than the usual naive row (138 assertions) because thirteen
kinds of actor are run through each of the s 15 permissions.

## What the Act turns out to say

### 1. Doing the work, signing it, supplying it and offering it are four different permissions

s 15(1) lets five kinds of person do the work: a certificated engineer, someone under
such an engineer's supervision, a Board-authorised foreign engineer working in
collaboration, a licensed practice, and a partnership wholly of certificated engineers.
s 15(3) lets only the certificated engineer **sign and submit** to a building
authority, and a document signed in contravention "is invalid". s 15(8)(a) lets only
a licensed practice, or a certificated engineer acting on own account, for a licensed
practice or as partner in an all-engineer partnership, **supply** services. s 15(8)(b)
adds two who may **offer** but are not listed as able to supply: the authorised
foreign engineer and an allied professional (architect or land surveyor) who is a
partner in a licensed partnership or LLP. Read literally, the all-engineer
partnership itself may do the work and hold itself out (s 15(1)(e), (6)(c)) but is not
named in s 15(8)(a) as a supplier; its partners are. That last point is a literal
reading, not a settled one. Asserted.

### 2. The title follows registration, not a practising certificate

s 15(4) forbids "professional engineer", "Er.", "Engr." or "engineer" as a title before
the name "unless the person is a registered professional engineer". A registered
engineer with no current practising certificate, or one suspended, may still use the
title, though he or she may do none of the work. An engineering graduate who is not
registered may not call himself "Engineer Tan". A Board-authorised foreign engineer may
use only a Board-approved derivative of "professional engineer" (s 15(5)). Asserted.

### 3. Engineers must vote, or pay to practise

s 5: every engineer holding a practising certificate on election day "must vote" for
the elected Board members; one who does not "is not entitled to apply for a practising
certificate" unless he or she satisfies the Registrar of a good reason or pays a
penalty prescribed by the Board. Asserted.

### 4. Illegal practice is fine-only the first time; lying to the register is not

Contravening s 15 carries a fine of up to $5,000, with imprisonment up to 6 months only
for a repeat natural-person offender (s 15(10)); a body corporate faces fines only.
Employing an unregistered person "as a professional engineer" is $2,000, then $5,000
(s 17). But obstructing an investigator (s 54(6)) and falsifying a register or
procuring registration or a certificate by false representation (s 58) carry up to six
months' imprisonment from the first offence. Asserted.

### 5. A client who paid an unlawful practitioner can get the money back; the practitioner cannot sue

s 18(1) bars anyone not authorised to supply the services from suing for any fee.
s 18(2) lets a person who paid for conduct contravening s 15 recover the money, unless
he or she knew or had reason to believe the conduct contravened s 15. Asserted.

### 6. Removal for not renewing is forgiven at once; removal at your own request is not

s 27(2) makes a removed person wait "at least 3 years" before the Board may consider a
fresh application. s 27(3) excepts only removal under s 26(1): no Singapore contact
address, or not renewing a certificate for a continuous 10 years. Read literally, an
engineer who asked to be taken off the register (s 26(5)) waits the three years. A
removal under s 50(2)(a) reversed on appeal means immediate reinstatement with no fee
(s 27(1)). Asserted.

### 7. Disciplinary orders wait 30 days, or the appeal, unless made immediate

A Disciplinary Committee may remove, suspend for up to 2 years, fine up to $50,000 and
order costs up to a further $50,000 (s 50(2), (3)). Its order waits 30 days (s 50(7));
an appeal stops it taking effect until confirmed, dismissed or withdrawn (s 51(4));
but removal or suspension may be ordered to take effect immediately to protect the
public or the engineer (s 50(8), (9)). How s 51(4) ("Despite anything in section 50")
treats an immediate order under s 50(8) that is appealed is not stated; the encoding
treats the immediate order as in effect, an inference. Asserted.

### 8. Practising certificate deadlines

An engineer must apply by 1 December for the next year's certificate (s 28(1)); a
December application after that, or an application during the year, is accepted only
with an additional prescribed fee (s 28(5)), except a first application after
registration, which may be made at any time (s 28(2)). A change of practice address
must be notified within 2 weeks (s 28(7)). Asserted.

### 9. A deposit oddity

s 58 in the deposit has two paragraphs labelled "(b)": the second ("by making or
producing ... any false or fraudulent representation") reads as the means by which the
first (b) is done, not a separate limb. The encoding only uses the penalty.

## What would need doing before this is worth anything

- The Professional Engineers Rules and the Board's prescribed fees, examinations,
  experience and voting penalty were not retrieved; every "prescribed" item is an
  input or is left out.
- Part 6 (licensing of corporations, partnerships and LLPs) was not encoded, although
  "licensed practice" is an input everywhere in s 15.
- The s 20(1) saving for architects ("not ... a substantial part of services within
  the practice of professional engineering") and the s 15(4)(c) catch-all ("any word
  ... that will lead to the belief") are judgement calls and are not modelled.
- The interaction of s 51(4) with an immediate order under s 50(8), and whether an
  all-engineer partnership itself "supplies" under s 15(8), need a lawyer's reading.
- No case law was searched.
