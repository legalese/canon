# Bills of Exchange Act 1949 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the `writing-l4-rules` skill as shown in the finished example rows (the skill
itself could not be loaded in this session). No pipeline, no coverage table, no
independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/BEA1949.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. The latest amending Act in its legislative history is Act 7 of
2009 (Civil Law (Amendment) Act 2009, annotated at s 22(3)), with the rectification
order S 30/2010 (annotated at s 76(1)). The arrangement of sections at the top of
the deposit is out of step with the body from s 23 onwards; the body's numbering is
followed.

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0034**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet.

The Act is 106 sections on bills, cheques and promissory notes. This row takes the
cheque, the instrument an ordinary person or business actually meets: what makes
an instrument a bill and a cheque (ss 3, 9(2), 11(2), 13(2), 73), days of grace and
business days (ss 14, 101), signatures by minors, forgers and agents (ss 22(3), 24,
26), the holder in due course and good faith (ss 29, 99), material alteration (s 64),
late presentment (s 74), stopping a cheque and the drawer's death (s 75), notice of
dishonour (ss 48, 49(m), 50(3)), and crossings, "not negotiable" and "account payee"
(ss 76, 79, 81, 82, 8(1)).

Not encoded: acceptance (ss 17-19, 39-44), inchoate instruments (s 20), the detailed
presentment rules (ss 41, 45, 46), noting and protest (s 51), the liabilities and
estoppels of parties (ss 53-58), discharge (ss 59-63), acceptance and payment for
honour (ss 65-68), lost bills and sets (ss 69-71), conflict of laws (s 72), the
bankers' protections for unindorsed and collected cheques (ss 83-88), cheque
truncation (ss 89-91), promissory notes (Part 4) and most of Part 5.

## What the Act turns out to say

### 1. A bank that pays a crossed cheque over the counter is liable even if it acted in good faith

s 79(2): a banker who pays a cheque "crossed generally otherwise than to a banker",
or a specially crossed cheque to anyone but the named banker or its collecting
agent, "is liable to the true owner of the cheque for any loss". Subsection (2) has
no good-faith defence. The only escape is s 79(3), where the cheque "does not at the
time of presentment appear to be crossed" (or the crossing was obliterated invisibly)
and the banker paid in good faith and without negligence. Asserted.

### 2. "Not negotiable" does not stop a cheque being transferred; it stops the transferee getting a better title

s 81: a person who takes a crossed cheque marked "not negotiable" "shall not have and
shall not be capable of giving a better title" than the person he took it from. So an
honest buyer who meets every condition of s 29 still takes it subject to a prior
defect, such as a theft. It is "account payee" on a crossed cheque that makes it not
transferable at all (s 82(1)). Asserted.

### 3. "Account payee" only works on a crossed cheque

s 82(1) applies "Where a cheque is crossed and bears across its face the words
'account payee' or 'a/c payee'". On an uncrossed cheque s 82 does not apply. Whether
the words then count as "words ... indicating an intention that it should not be
transferable" under s 8(1) is a question of construction the text does not settle;
the encoding leaves it to a separate flag. Asserted (for s 82).

### 4. Stopping a cheque costs the drawer the right to notice of dishonour

s 48(1) discharges a drawer who is not given notice of dishonour. But s 50(3)(c)(v)
dispenses with notice "where the drawer has countermanded payment". And s 75 ends
the bank's authority to pay on countermand, or on **notice** of the customer's death:
the death alone, unknown to the bank, does not end it. Asserted.

### 5. Late presentment of a cheque discharges the drawer only to the extent of his actual loss

For bills generally, failing to present duly discharges the drawer (s 45(2)). For a
cheque, s 74 discharges the drawer only if he had the right to have it paid "and
suffers actual damage through the delay", and only "to the extent of such damage"; the
holder then becomes the bank's creditor for that amount in his place. Asserted.

### 6. Smaller points

- A cheque need not be dated, and may be post-dated, without ceasing to be a cheque
  (ss 3(5)(a), 13(2)); an order to pay "out of a particular fund" (s 3(3)) or on a
  contingency (s 11(2)) is not a bill at all. Asserted.
- Where words and figures differ, the words govern (s 9(2)). Asserted.
- A cheque, payable on demand, has no days of grace; other bills have 3 unless they
  say otherwise (s 14). Saturday is a business day for a Singapore bill (one payable
  in Singapore currency) but not for other bills (s 101(2)(c)). Asserted.
- s 22(3): a bill drawn by someone under 18 still entitles the holder to enforce it
  against the other parties. Whether the minor is liable depends on capacity to
  contract under other law, which was not read. Asserted for the age line only.
- "For and on behalf of" the company excuses an agent who signs; just adding "director"
  does not (s 26(1)). Asserted.
- Good faith means honesty, "whether it is done negligently or not" (s 99), so a
  careless but honest taker can still be a holder in due course. Asserted.
- A material alteration that is not apparent does not stop a holder in due course
  enforcing the original tenor (s 64(2)). Asserted.
- Crossing needs two parallel lines, except a special crossing: the name of a bank
  written across the face is enough on its own (s 76(2)). "And company" with no lines
  is not a crossing. Asserted.

## What would need doing before this is worth anything

- No case law on cheques, crossings or "account payee" was searched, and no
  regulations under s 91 (cheque truncation) were read.
- The s 49(m) timing is counted in business days on the inference that s 101(1)
  reaches it; this has not been checked.
- The minor's own liability (s 22(1)) needs the law on capacity to contract.
- Days of grace are counted but the actual due date (rolling to the next business
  day) is not computed.
