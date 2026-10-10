# Maintenance Orders (Reciprocal Enforcement) Act 1975 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example naive rows (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.
NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MOREA1975.txt`. The cover says it "incorporates all
amendments up to and including 1 December 2021"; every page is headed "Informal
Consolidation – version in force from 16/1/2025". The latest amendment annotated is
Act 18 of 2023 (Family Justice Reform Act 2023, commencement 16 January 2025), which
deleted s 8(2) and (3). The arrangement of sections at the top of the deposit omits
"Appeals" as s 12 and is out of step with the body; the body's numbering is used.

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its everyday-life relevance (Tier 1), not by citation count: it is the
route by which a wife, former wife or child in Singapore has a maintenance order
enforced against a payer who has moved to a reciprocating country, and by which a
foreign order is enforced against a payer living here. This row takes what a payer
or payee meets: which orders count (s 2, s 17(2)), sending an order abroad (s 3),
the provisional order against a payer abroad (ss 4, 5(3)), registration and
confirmation of foreign orders (ss 6, 7), the change-of-address offence and the
start date of payments (s 8), variation, revocation and arrears (ss 9, 10), witness
compensation (s 14(3)) and currency conversion (s 16). Not encoded: the document
lists the officer and the Minister send, confirmation of foreign provisional
variation and revocation orders (ss 5(5)-(9), 9(6), (7)), appeals (s 12), evidence
and proof of foreign documents (ss 13-15), the manner of payment, the list of
reciprocating countries (Gazette notifications, none retrieved), rules and
transitional provisions (ss 18-19).

## What the Act turns out to say

### 1. Only a man's spousal maintenance travels

s 2 "maintenance order" reaches payments "by a man towards the maintenance of his
wife or former wife" and "by a person towards the maintenance of the person's child".
An order for a woman to maintain her husband is outside the definition; so is an
order for an adult child to maintain a parent, and a bare paternity finding with no
payment. Child maintenance is covered whichever parent pays. Asserted.

### 2. A payee can have a registered order varied outright; a payer usually cannot

s 9(2): the Singapore court registering a foreign order may vary it otherwise than
provisionally only if both parties live in Singapore, **or the payee applies**, or the
variation is a reduction made solely on a change in the payer's finances and the
foreign courts cannot confirm provisional variations. A payer living in Singapore who
seeks a reduction, where the foreign courts can confirm, gets only a provisional order
needing confirmation abroad. Revocation is never outright unless both live in
Singapore (s 9(3)), and the court then applies the foreign country's law (s 9(4)),
though it may make a provisional revocation on mere "reason to believe". Asserted.

### 3. An order against a payer abroad has no effect until a foreign court confirms it

s 4 lets a Family Court hear a complaint against a person in a reciprocating country
as if they were resident and served, but the order "is a provisional order" (s 4(2)),
which by s 2 "has no effect unless confirmed" abroad. Likewise s 5(3): increasing a
Singapore order that has gone abroad is only provisional unless both parties appear,
or the applicant appears and the other party was duly served. Asserted.

### 4. Confirming a foreign provisional order: the payer must prove a listed ground

s 7(2): the Singapore court must refuse confirmation only if the payer "establishes"
a ground on which the order might have been opposed; otherwise it must confirm, with
or without alterations. The foreign court's list of grounds is conclusive that they
were available (s 7(3)). If the summons cannot be served, the papers simply go back to
the Minister (s 7(6)). Asserted.

### 5. Sums run from the foreign order's date, unless the confirming court says later

s 8(7): sums under a registered order are payable "as from the date on which the
order was made" — which may be well before registration. Only a court confirming a
provisional order under s 7 may direct a later start (s 8(8)). Asserted, with dates as
day numbers.

### 6. Arrears survive revocation and cancellation

s 9(9) and s 10(1): a revoked order ceases to have effect "except as respects any
arrears due" at the date revocation takes effect, and those arrears remain recoverable
after registration is cancelled. That an instalment falling due on that very date
counts as "due at that date" is an inference. Asserted.

### 7. The only offence is not telling the court of a new address

s 8(4): a payer under a registered order who fails "without reasonable excuse" to
notify the clerk of a change of address is liable to a fine not exceeding $500; no
imprisonment is provided. Asserted.

### 8. Currency is fixed once, at the earlier of registration and confirmation

s 16(2), (5): a foreign-currency order is converted at the exchange rate on "the
relevant date" — the earlier of first registration and confirmation, or for a varied
order the earlier of the last variation's registration and confirmation — and is
thereafter a Singapore-dollar order. Asserted.

## What would need doing before this is worth anything

- The Gazette notifications under s 17 listing reciprocating countries, and the class
  limits in each, were not retrieved; every "reciprocating country" input is assumed.
- The Family Justice Rules prescribing the manner of application, the officers and
  the manner of payment were not read.
- Confirmation of foreign provisional variations and revocations (ss 5(5)-(9), 9(6),
  (7)) and appeals (s 12) are not encoded.
- No case law was searched.
