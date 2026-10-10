# Protection from Scams Act 2025 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act No. 1 of 2025, informal consolidation, footed "version in force
from 1/7/2025" on every page. The deposit annotates no amending Act or subsidiary
legislation; its metadata records it as the current version as at 1 October 2026.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** to ordinary people in Singapore: it lets
the police stop a person's own bank from letting that person pay a scammer. The Act
has eleven sections, so nearly all of it is encoded: ss 2 to 7, 9 and the Schedule.
Not encoded: commencement (s 1), the Minister's powers over the Schedule and
regulations (ss 10, 11) and over what counts as "remote communication", the
notification rules (left to regulations), and the prescribed form and period for an
appeal, which the Act leaves to be prescribed. Section 8 (a Deputy Commissioner may
hear appeals in the Commissioner's place) is noted, not modelled.

## What the Act turns out to say

### 1. The order freezes the victim's own money, to protect the victim from themselves

A restriction order is issued to banks "in relation to a scam victim" and blocks
transfers and withdrawals from *the victim's* accounts and any grant or drawdown of
credit to the victim (s 3). The trigger is the officer's "reason to believe" that
the victim *will* pay, withdraw for, or borrow for a scammer (s 4(1)(a)). Section 4
states no requirement for the victim's consent, a court order or a hearing; the
encoding gives the victim's consent no effect on whether an order may issue.
Asserted.

### 2. It can last up to 180 days

An order lasts 30 days or a shorter period it specifies (s 5(1)). While in force it
may be extended by up to 30 days at a time (s 5(5)), but "not more than 5 times"
(s 5(6)): 30 + 5 × 30 = 180 days. The 180-day figure is arithmetic on the text, not
a number the Act states. Asserted.

### 3. Parents are not "relatives"

The time that relatives need to intervene is one factor in deciding whether an order
is necessary (s 4(1)(b)(i)). Section 4(2) defines "relative" as the spouse, siblings
and stepsiblings, children (including adopted) and stepchildren, grandchildren and
step-grandchildren, nephews and nieces and their step- forms. Parents, grandparents,
aunts, uncles and cousins are not listed (though "other persons" are also counted in
s 4(1)(b)(i), so they are not shut out of the factor). Asserted.

### 4. Only the victim and joint holders may ask for relief, and appealing changes nothing meanwhile

Only the scam victim or a joint account holder may apply to vary the order to allow a
transfer or withdrawal (s 5(4)), or appeal to the Commissioner (s 7(1)); a relative
or the bank may not. The appeal does not suspend the order: unless the Commissioner
directs otherwise, it "must be complied with until the determination of the appeal"
(s 7(8)); it may be decided on documents without a hearing (s 7(4)), and the
decision "is final" (s 7(6)). Asserted.

### 5. Money in is not blocked, and a scammer must have reached the victim remotely

Section 3 lists only transfers and withdrawals *from* the account and credit, so a
deposit into the account is not restricted (a reading of what s 3 lists). A
"scammer" must have "interacted with the scam victim via remote communication"
(s 2); someone who only dealt with the victim face to face is not one, wherever the
offence was committed. A "scam victim" must be an individual. The Schedule's scam
offences are Penal Code ss 416A, 417, 418, 419, 420, 420A, 424A and 424B and their
abetment, conspiracy or attempt; the Act gives only the numbers. Asserted.

### 6. A bank that ignores an order risks $3,000 at most

The bank's offence (contravention without reasonable excuse) carries "a fine not
exceeding $3,000" (s 6(1)), compoundable for up to $1,500 (s 6(2)). A bank and its
officers, employees and agents are immune from criminal and civil liability for
complying with "reasonable care **and** in good faith" (s 9); good faith alone is
not enough. Asserted.

## What would need doing before this is worth anything

- The regulations under s 11 (notification, the appeal form and period) were not
  retrieved; who is told of an order, and when, is not in the Act.
- Whether any order has been made under s 10 amending the Schedule, or under s 2
  excluding a communication system, was not checked.
- The Banking Act 1970 definition of "bank" and the Police Force Act 2004 definitions
  of the officers were not read.
- No case law, police guidance or parliamentary material was searched.
