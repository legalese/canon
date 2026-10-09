# Building Maintenance and Strata Management Act 2004 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 15
of 2026 shown (some in force 1 July and 1 October 2026). The deposit's arrangement of
sections is out of step with the body; the encoding follows the body.

**Checks:** one case file, 40 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**17 of the 527 Singapore Acts** deposited here cite it. It pairs with the Land Titles
(Strata) Act row, which covers collective sale. This row takes what an owner faces:
renovating, paying contributions, arrears and their consequences, guaranteeing the
management corporation's debts, and the duties owed to neighbours. Meetings,
by-laws, insurance, managing agents, the Strata Titles Boards and the Schedules
(including the voting rules) are not encoded.

## What the Act turns out to say

### 1. Unpaid maintenance fees can cost you the flat

s 43: contributions still unpaid 30 days after a written demand become a registered
**charge** with a **power of sale**, as if the management corporation were a mortgagee.
Before selling it needs all of:
- a special resolution
- a newspaper notice
- 6 weeks with no payment
- no pending court action to restrain the sale

Asserted.

### 2. Non-payment after a demand is a crime

s 40(10): an owner who has not paid within 14 days after a written demand commits an
offence. The fine is up to $10,000, plus $100 a day after conviction. Asserted.

### 3. A buyer inherits the seller's arrears

s 40(3): a new owner is jointly and severally liable for contributions unpaid when they
became owner. Under s 40(4) the seller stays liable only for what was unpaid at the
sale. Under s 37(4A), the current owner can also be made to undo an unauthorised
renovation "whether or not" they were responsible. Asserted.

### 4. Window grilles and cat mesh override the by-laws

s 37A lets an owner install window grilles, railings, window restrictors, insect and
animal screens, intruder alarms and locks "despite ... any by-law" that prohibits them,
provided they are fitted competently and in keeping with the building's appearance.
Adding floor area needs a 90% resolution (s 37(2)). A change to the appearance needs
the management corporation's approval (s 37(4)). Asserted.

### 5. Owners guarantee the management corporation's debts

s 44: every lawful expense is "guaranteed" by the owners, each up to their share-value
proportion. Asserted.

### 6. Smaller things worth recording

- **s 41(1):** contributions are cut by 75% until the TOP is issued.
- **s 53(7):** any arrears on the 3rd day before an election disqualify a council
  candidate.
- **s 54(2):** a council member more than 3 months in arrears can be removed without a
  general meeting.
- **s 63:** the duties not to cause nuisance or interfere with services bind tenants
  directly, not only owners.

## What would need doing before this is worth anything

- The Second Schedule (meetings and voting, including any arrears bar on voting) and the
  prescribed by-laws were not encoded.
- The Strata Titles Board's powers to vary contributions (s 108) are not encoded.
- No case law or Board decisions were searched.
