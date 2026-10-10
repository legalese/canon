# Finance Companies Act 1967 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 18
of 2022 (in force 31 July 2024) shown. The arrangement of sections at the top of the
deposit does not line up with the body from Part 3 onwards. This row follows the
body's numbering: s 18 reserve fund, s 18A bad debts, s 19 dividends, s 20 balance sheet.

**Checks:** one case file, 121 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**15 of the 527 Singapore Acts** deposited here cite it. This row covers the rules
that a finance company, its directors, someone seeking control, a depositor or a
competitor actually meets:

- who may carry on financing business, and who may use the name (ss 3, 4, 51, 53)
- the appeal against a refused licence (s 6(8))
- capital (ss 7, 7A)
- effective control and associates (s 10)
- the reserve fund and dividends (ss 18, 19)
- acknowledging a deposit (s 22)
- credit, investment and property limits (ss 23, 26, 27)
- the liquid-asset penalty charge (s 32(5))
- public holidays (s 43)
- priority in a winding up (ss 44, 44A)
- directors' liability (s 49)
- the maximum penalties for these offences

Not encoded: licence conditions and revocation, branches, mergers, ss 11 to 13,
returns and statements, own shares and trade, Authority orders, inspection and
assumption of control, Part 6A transfers, s 47, composition and winding up. The
liquid-asset ratio is left to the Authority by s 32(2), so it is not encoded either.

## What the Act turns out to say

### 1. The unsecured-lending cap reads two ways

s 23(1)(f) says a finance company must not grant unsecured facilities "(i) to any
person ... which in the aggregate ... exceeds $5,000; **and** (ii) which in the
aggregate ... exceeds 10% of the capital funds". Read literally, both limbs must be
met. A $6,000 unsecured loan to one borrower would then be lawful unless the company's
total unsecured book were also above 10% of capital funds. Read as two separate
ceilings, either limb alone is a breach. The text does not choose between them, so
both readings are encoded, and the cases show where they part. Asserted.

### 2. A director's brother is outside the indemnity

s 23(5) makes **all** the directors jointly and severally liable to indemnify the
company for losses on unsecured credit to a director, a director's firm, a company the
director owns more than 50% of, or a related corporation. s 23(6)(b) extends
"director" to "the wife, husband, father, mother, son or daughter". A brother or
sister is not on that list. A company listed on SGX is excluded even when a director
owns 60% of it. Compare s 10(3)(f), where brothers and sisters *are* associates for
the purposes of control. Asserted.

### 3. Breaking a credit limit carries a fine of up to $50,000, but no prison term

s 23(7) sets a fine of up to $50,000 for any breach of s 23 and provides no
imprisonment. Unlicensed financing business (s 3) can bring 3 years, holding out (s 51)
2 years, and falsifying books (s 50) 3 years. A breach with no penalty of its own,
such as s 22 or s 43, falls under s 48: $20,000 or 3 years. Asserted.

### 4. 20% of the votes or of the shares needs the Authority's approval first

s 10 requires notice to the Authority and its approval *before* anyone agrees to
acquire effective control: at least 20% of the voting power or of the issued shares,
counting associates. The section applies "whether resident in Singapore or not".
Associates include spouses, lineal relatives, brothers and sisters, partners,
employers and employees, and corporations in which the person controls 20% of the
votes. They do not include cousins or uncles. Asserted.

### 5. How much of each year's profit goes to the reserve fund depends on the fund's size

s 18 requires 50% of net profits after tax while the reserve fund is below half of
paid-up capital, 25% until it equals paid-up capital, and 5% after that. Under s 19 no
dividend may be paid until all capitalised expenditure, including losses, has been
written off. Asserted.

### 6. Insured deposits rank second, after the deposit insurance premiums

s 44A ranks deposit insurance premium contributions first and insured deposits
second, "up to the amount of compensation paid or payable out of the DI Fund". A
resolution fund trustee's claim ranks third. Under s 44(2), all three rank ahead of
other unsecured liabilities, though not ahead of the preferential debts under the
IRDA 2018. The uninsured part of a deposit is not listed, and this row treats it as an
ordinary unsecured liability. That is an inference. Asserted.

### 7. Smaller points

- A private company cannot be licensed at all (ss 3, 6), which is an inference from
  the two sections.
- Banks, licensed pawnbrokers and credit co-operatives are outside s 3 (s 53).
- An appeal against a refused licence must be made within 30 days, and the Minister's
  decision is final (s 6(8)).
- The capital adequacy ratio is 12% unless the Authority sets another figure (s 7A).
- Each deposit must be acknowledged in writing within 2 months (s 22).
- No business may be done on a public holiday or a declared bank holiday without
  approval (s 43).
- Under s 49(3), a director may be imprisoned only if the offence was wilful.

All asserted.

## What would need doing before this is worth anything

- In s 7(1)(b), "its capital funds are not less than that amount" is read as
  $50 million. It could instead mean the paid-up capital.
- "Substantial shareholding" (s 12) and "preferential debts" (s 44(2)) are defined in
  the Companies Act 1967 and the IRDA 2018, which were not read.
- None of the Authority's notices were retrieved: the capital adequacy figure, the
  liquid-asset ratio, approved percentages, exemptions under s 53(3), or the offences
  prescribed as compoundable.
- The Part 6 control provisions and the Part 6A transfer provisions were not read.
- The two readings of s 23(1)(f) need settling from MAS practice or case law, and none
  was searched.
