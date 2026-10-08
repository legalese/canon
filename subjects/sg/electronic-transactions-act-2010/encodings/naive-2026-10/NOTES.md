# Electronic Transactions Act 2010 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, incorporating Act 38
of 2022 (s 26(3A)) and S 10/2025 (public certification authorities in the Third
Schedule).

**Checks:** three case files, 273 assertions satisfied, 0 errors, 0 warnings.

## Why this Act

**33 of the 527 Singapore Acts** deposited in this repository cite it. It decides
whether an email, a click-through or an electronic signature counts as writing or
a signature, when an email is "received", and when an internet intermediary is
liable for what it carries.

## Scope

The operative Act, without the purposes clause (s 3), the regulation-making,
appointment and exemption powers, the investigation powers (encoded only through
the offences that back them), and the Third Schedule's duties of certification
authorities and subscribers except where a rule here turns on them. **No
regulations or exemption orders were retrieved.**

## What the Act turns out to say

### 1. "Network service provider" is never defined

s 26 shields a "network service provider" from liability for third-party material
to which it "merely provides access". The phrase occurs **eleven times** in the
deposited text. Neither s 2 nor s 26(4), which defines "provides access" and
"third-party", defines it. The only definition in the 527 deposited Acts is in the
**Copyright Act 2021**, the one regime s 26(3)(d) carves out. Five other deposited Acts use the phrase
without defining it (the Broadcasting Act 1994, the Food Safety and Security Act
2025, the Online Safety (Relief and Accountability) Act 2025, and both elections
Acts). Who counts is taken
here as a supplied fact. Asserted as that absence.

### 2. What the s 26 shield covers, and what it does not

The shield covers liability "founded on" publishing the material or infringing
rights in it (s 26(1)), and liability under the PDPA (s 26(2)). It does not touch
contract, a licence condition, an obligation to remove or block material,
copyright (s 26(3)), or the Broadcasting Act's online-safety provisions in
ss 45E, 45F and 45N (s 26(3A)). And "third-party" means a person "over whom the
provider has no effective control", so a provider gets no shield for its own
employees' posts. Asserted across four providers and eight bases of liability.

### 3. A tenancy agreement probably cannot be signed electronically

The First Schedule takes Part 2 (writing, signature and contract formation) away
from any rule of law requiring writing or signature for "any contract for the sale
**or other disposition** of immovable property, or any interest in such property".
A lease is a disposition of an interest in immovable property, and the Schedule
has no carve-out for short tenancies. Read literally, where a rule of law requires
a tenancy to be in writing or signed, s 7 and s 8 cannot satisfy it. This is a
reading; it is the finding here most worth checking against practice and case
law. Wills, express trusts, ordinary powers of attorney, indentures and
conveyances are excluded too; implied, constructive and resulting trusts and the
**lasting** power of attorney are not. Asserted.

### 4. An unreliable signature counts if it in fact worked

s 8(b) has two limbs: a method "as reliable as appropriate", **or** one "proven in
fact to have fulfilled the functions" of identifying the person and showing
intention. A typed name at the foot of an email, proved by the correspondence
around it, satisfies a signature requirement however unreliable the method.
Asserted.

### 5. The parties can contract out of contract formation but not of writing and signature

s 5(3) lets the parties exclude or vary ss 6 and 11 to 16, and leaves out ss 7 to
10. Those decide what satisfies a rule of law, which a contract cannot change.
s 5(2)(a) still lets the parties refuse electronic dealing altogether. Part 2A is
different again: s 16D(3) lets parties derogate from **all** of it or none, never
**some**. Asserted.

### 6. An email to an address the recipient did not designate is received only when they know of it

s 13(2): receipt at a designated address is when the email "becomes capable of
being retrieved" (presumed on arrival, s 13(4)). s 13(3): at an undesignated
address it is when it is retrievable **and** "the addressee becomes aware that the
electronic communication has been sent to that address". An email to an old
address the recipient never notices is never received. If a message never leaves
the originator's system, its despatch time is its receipt time (s 13(1)(b)).
Asserted, with times as numbers.

### 7. A website is an invitation to treat, so a pricing error does not bind on the click

s 14: a proposal "generally accessible" and not addressed to specific parties,
including one with "interactive applications for the placement of orders", is an
invitation to make offers "unless it clearly indicates the intention ... to be
bound in case of acceptance". The customer's order is the offer. Asserted.

### 8. The input-error right is narrow

s 16: a **natural person** who makes an input error dealing with **another party's
automated system**, which gave **no opportunity to correct** it, may withdraw **the
portion** containing the error, if they notify **as soon as possible** and have not
used or received a material benefit. A confirmation screen, whether read or not,
defeats it. An error made to a human on the other side is not covered, nor one
made by a bot. It is not a right to rescind the whole contract. Asserted.

### 9. Assaulting the Controller carries half the prison term of not helping the Controller

s 31 makes it an offence to obstruct, impede, **assault** or interfere with the
Controller, with no penalty stated, so s 33's general penalty applies: $20,000 or
**six months**. s 29(3) makes it an offence to obstruct access to a computer or
fail to give "reasonable technical and other assistance": $20,000 or **twelve
months**. (Assault is also a Penal Code offence, and the Controller is a public
servant under s 27(6); this row does not follow the Penal Code.) Asserted.

### 10. A certification authority's liability is capped exactly where it was at fault

Third Schedule para 11(b): unless it waives the paragraph, an accredited, public or
recognised CA is not liable "in excess of" the recommended reliance limit for a
misrepresentation in a certificate, or for **failing to comply** with paras 14
and 15 (the issuance rules). A CA that issued a certificate without checking
identity, contrary to para 14, owes at most the limit it chose to write in the
certificate. For a forged signature where the CA complied with the Act, it owes
nothing (para 11(a)). Asserted at $500,000 losses against a $10,000 limit.

### 11. Anyone acting for an "unavailable" subscriber can have a certificate suspended

Para 16(c): the CA must suspend on request by a person it reasonably believes to be
"acting on behalf of that subscriber, who is unavailable". No authority is
required. Para 18(2): a revocation for falsity, a failed issuance requirement or
compromise must be notified to the subscriber; one for death or dissolution need
not be. Asserted.

### 12. Smaller things worth recording

- **s 2(3)(d):** a ".sg" domain or Singapore email address raises no presumption
  that the business is in Singapore.
- **s 9(2):** routing data "necessarily and automatically generated solely" to
  send or receive need not be kept.
- **s 16N(3):** going from electronic to paper, metadata and dynamic data (a
  vessel's position) need not be reproduced. Once a change of medium takes effect,
  the replaced document "ceases to have any effect or validity".
- **s 16O(2), (3):** reliability is presumed only if the record was issued,
  transferred, controlled, presented **and** stored on an accredited system while
  the provider was registered. A record issued elsewhere and moved on gets no
  presumption.
- **Third Schedule para 3(b)(iv):** a self-issued certificate gives a secure
  electronic signature if sender and recipient expressly agreed to use digital
  signatures. Para 23(2) speaks of a certificate "issued by himself, herself or a
  certification authority".
- **s 25(4):** "Subject to sections 9 and 10, nothing in this Act by itself compels
  any public agency to accept" electronic documents, which implies ss 9 and 10
  do compel an agency where their conditions are met.
- **s 36:** composition is capped at the lower of half the maximum fine or $5,000,
  so $5,000 for every offence here except the two $10,000 ones.

## What would need doing before this is worth anything

- **Retrieve the regulations** (Electronic Transactions (Certification Authority)
  Regulations, any ETR provider regulations, any exemption orders). The accredited
  and recognised CAs, and the compoundable offences, are defined there.
- **No case law was searched.** Findings 3, 4 and 7 in particular have Singapore
  case law (on electronic signatures and on website pricing errors) that this row
  has not read.
- "Commercially reasonable", "reliable", "material benefit" and "as soon as
  possible" are taken as supplied facts.
- Times are plain numbers; dates are yyyymmdd numbers. No calendar arithmetic.
