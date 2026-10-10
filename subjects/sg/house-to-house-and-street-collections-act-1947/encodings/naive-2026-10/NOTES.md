# House to House and Street Collections Act 1947 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table,
no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says incorporates all amendments
up to and including 1 December 2021 and came into operation on 31 December 2021. The
Legislative History lists no amending Act after the 1959 Transfer of Powers
Ordinances and Modification of Laws Order; the later entries are revised editions.

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is **REQ-0060** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Act has ten sections, so the row covers almost all of it: ss 2, 3,
4(4) to (7), 6, 7, 8, 9(2) and 10. Not encoded: the regulation-making power (s 5)
beyond the offence of breaching a regulation, any regulations themselves (none were
retrieved), the application procedure and licence conditions (s 4(1) to (3)), the
Minister's handling of an appeal (s 4(8)), court jurisdiction (s 9(1)), and the content
of a Gazette exemption (s 10), which is modelled only as a flag.

## What the Act turns out to say

### 1. A "collection" is not limited to charity, nor to gifts

s 2(1) defines a collection as an appeal to the public, by house-to-house visits or
by soliciting in streets or public places, to give money or property "whether for
consideration or not". No purpose is named, so selling something door to door for a
cause falls inside it as much as a flag day. "House" includes a place of business, so
a shop-to-shop appeal is a house-to-house one. What falls outside is an appeal by
neither means (the encoding treats an online appeal as outside; that is an inference
from the two named means) and a demand for money legally due, such as a debt or a
charge. Asserted.

### 2. The collector commits an offence too, and the text gives no excuse for ignorance

s 3(3): anyone who "acts as a collector" commits an offence unless a licence covering
him, or the promoter he acts under, is in force "at all times when he so acts". The
words state no mental element, so a volunteer who believed the promoter was licensed
is not excused by them. The penalty is the general one in s 8(1): up to $1,000 or 6
months or both. Promoting without a licence (s 3(2)) carries up to $5,000 or 2 years
or both. Asserted.

### 3. The Commissioner must grant, but may refuse for "the public interest" and need not say why

s 4(1) says the Commissioner "shall ... grant" a licence, subject to s 4. s 4(4) then
lists seven grounds for refusal or revocation, the sixth of which ends "or that the
refusal or revocation of a licence is otherwise desirable in the public interest". When
that ground (f) is relied on, s 4(6) lets the Commissioner decline to state his reasons
or disclose his information. Appeal is to the Minister within 14 days of the notice,
and the Minister's decision "shall be final" (s 4(5), (7)). Asserted; the treatment of
the 14th day as in time is an inference about counting.

### 4. Refusing your name to the police costs at most $100

s 7: a police officer who believes someone is collecting may require their name and
address "immediately"; failing to comply is an offence with a fine of up to $100 and
no imprisonment mentioned. Asserted.

### 5. Managers of a body are deemed guilty unless they prove otherwise

s 8(2): where a corporation, society or association commits an offence, everyone in
its control or management is deemed guilty unless he proves he was unaware through no
neglect of his, or took all reasonable steps to prevent it. Asserted.

### 6. The money collected can be returned or forfeited

s 9(2): on a conviction the court may order money or property obtained by the offence
returned to its owner, if known, or forfeited or confiscated. Asserted.

## What would need doing before this is worth anything

- The regulations made under s 5 (badges, certificates, receipts, accounts, minimum
  age, annoyance) were not retrieved; they are where most of the day-to-day duties of
  collectors would sit, and they may set their own penalties.
- No Gazette exemptions under s 10 were searched; if registered charities or other
  classes are exempted, the offences in s 3 reach far fewer people than the text alone
  suggests.
- No case law was searched.
