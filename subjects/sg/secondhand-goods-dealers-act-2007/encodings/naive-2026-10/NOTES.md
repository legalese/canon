# Secondhand Goods Dealers Act 2007 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, "version in force from
9/3/2025", as deposited at `../../registers/source-bundle/SGDA2007.txt`. The latest
amendment annotated in the text is Act 5 of 2025 (wef 9 March 2025, to ss 2 and 3);
Schedule item 11 is marked deleted by S 519/2023 (wef 31 July 2023). The arrangement
of sections at the top of the deposit is numbered one out of step with the body; the
encoding follows the body.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: anyone who sells a used phone, laptop,
watch or gold jewellery to a shop, or has such a thing stolen, meets this Act. This row
takes what counts as secondhand goods and who is a dealer (s 2, Schedule), the licence
requirement and exemption (ss 4, 20), appeals and when a revocation bites (ss 5(5), 8,
9), records (s 10), reporting goods on a police list (s 11), the court's powers over
stolen goods sold to a dealer (s 14), and employees, penalties and composition (ss
16(2), 18, 19). Not encoded: appointments (s 3), the application process and licence
form (ss 5(1)-(4), (6), 6), licence transfer (s 7), police entry, search and arrest (ss
12, 13), bodies corporate (s 15), court jurisdiction (s 17) and the Minister's powers
to amend the Schedule and make rules (ss 21, 22). No rules under s 22 were retrieved.

## What the Act turns out to say

### 1. The Act covers only the goods in its Schedule — not "secondhand goods" generally

s 2(1): "goods" means "any of the goods specified in the Schedule". The list is
cameras, computers, phones, CD/MP3/MP4 players, jewellery with precious stones,
platinum and gold jewellery without stones, pawn tickets, watches, copper cable, and
metal fittings of buildings and roads (drain covers, manhole covers, railings, taps,
even bicycle racks). Used clothes, furniture, books, televisions and bicycles fall
outside it. Plain silver jewellery is outside item 6, but a silver ring set with a
sapphire is inside item 5. Asserted.

### 2. Failing to keep records at all is not itself an offence under s 10

s 10(5) makes it an offence to contravene "subsection (2), (3) or (4)" — submitting,
retaining for 5 years from the end of the financial year, and producing on demand — or
to produce a record known to be false. The duty in s 10(1) to keep the records in the
shop is not on the list. (It can still ground revocation under s 8(1)(a)(vii), which
covers contravening "any of the provisions of this Act"; and failing to keep a record
may make it impossible to produce one under s 10(4) — that second point is an
inference.) Asserted.

### 3. A dealer who buys stolen goods carelessly can lose them and pay a penalty

s 14: when someone is convicted under Penal Code Chapter 17 for property sold to a
dealer, the court may order it returned to the proven owner, with or without repaying
the dealer's purchase price, "according to the conduct of the owner". If the dealer
ought reasonably to have suspected theft and did not use due care and diligence, the
court may add a financial penalty of up to $2,000. Asserted.

### 4. A person can be deemed a dealer — online too — until they prove otherwise

s 2(3): anyone in whose "shop" (which includes a house or flat, "whether electronically
or otherwise") secondhand goods are apparently exposed for sale, or who holds an
"unusual quantity", is deemed a dealer "until the contrary is proved". s 2(2) brings in
a person in Singapore who deals through the Internet. The Act does not define "deal",
so whether a private person selling their own old phone deals is left open; the
encoding takes it as a fact. Asserted.

### 5. A revocation waits 14 days, and longer if appealed

s 8(2): the show-cause notice must name a date at least 14 days away. s 8(5): the
revocation or suspension does not take effect until 14 days after the licensee is
informed, and if an appeal is notified in that time, not until the Minister confirms
it or dismisses the appeal. Only then must the licensee stop trading (s 9(1)). Appeals
are within 14 days (ss 5(5), 8(4)); for revocation the Minister may extend. Asserted.

### 6. Dealers must report goods matching a police list; detaining the seller is optional

s 11(2): a dealer holding, offered or shown property fitting a circulated list "must,
without unnecessary delay" report it to police, and "may" detain the person offering
it. Only the failure to report is an offence (s 11(3)). Offences carry up to $20,000
and/or 12 months (s 18); prescribed offences may be compounded for up to $2,000
(s 19). Asserted.

## What would need doing before this is worth anything

- The Secondhand Goods Dealers rules (fees, prescribed record particulars, which
  offences are compoundable) and any Gazette exemption orders were not retrieved.
- The content of the deleted Schedule item 11 was not read.
- No case law on what "deals" means, or on s 14, was searched.
