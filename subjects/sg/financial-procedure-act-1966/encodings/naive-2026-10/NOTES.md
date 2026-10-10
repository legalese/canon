# Financial Procedure Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 3
of 2024 (in force 26 February 2024) shown.

**Checks:** one case file, 81 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**32 of the 527 Singapore Acts** deposited here cite it. It is a government-finance
Act, so this row takes the provisions with decision content:
- the financial year (s 2) and the Accountant-General's protected terms (s 2A(2))
- bank accounts and overdrafts (s 4)
- which Consolidated Fund account money is kept in (s 6)
- what public money may be invested in, and where the income goes (s 7)
- capital injections into statutory corporations (s 7A)
- Contingencies Fund advances (s 11)
- warrants for expenditure from the Consolidated Fund (s 12(3))
- when a guarantee or a loan binds Singapore (s 15)
- virement between subheads (s 17(4)) and transfer of functions between heads (s 17A)
- surcharge of public servants for losses, its withdrawal and recovery (ss 20 to 23)

Not encoded: the Accountant-General's duties, accounting officers' general duty, the
Minister's general powers, deposit and advance accounts and Government funds (ss 8 to
10, 13, 14), refunds, the estimates and personnel list, the yearly statement of
accounts (s 18), write-off (s 19), and regulations (s 24).

**Warning about the source.** The Schedule to which s 7(7) refers ("Moneys in deposit
account to be invested on deposit in bank") has a title and **no entries** in the
deposit. Whether it is empty in law or was lost in extraction was not checked. The
encoding takes "Schedule moneys" as an input flag.

## What the Act turns out to say

### 1. The Act has no offences and no penalties

The deposit contains no "offence" and no "penalty". Section 4 says no accounting
officer "shall open" a public account without the Minister's written authority, and no
bank "shall permit" an overdraft without authorisation, but nothing is attached to
breach. The only sanction in the Act is the **surcharge** (ss 20 to 23), which is civil
and reaches only someone who "is or was in the employment of the Government". A bank
that permits an unauthorised overdraft faces nothing under this Act. Asserted (s 4 and
the surcharge rule; that a contractor cannot be surcharged).

### 2. A surcharge survives retirement and is collected from the pension

s 20(1) reaches a person who "is or was" a Government employee, and s 23 lets the
Minister recover a surcharge not withdrawn by monthly deductions "from the salary or
pension", not exceeding **one-fourth** of the monthly salary or pension. The surcharge
may be "the whole or such proportion as it thinks fit" of the loss, so it can be the
whole loss but not more (the encoding caps it at the amount at stake). A satisfactory
explanation given within the Minister's period stops it; one given later allows
withdrawal (s 22). The appropriate Commission is the Public, Judicial or Legal Service
Commission. Asserted.

### 3. The cap on warrants binds only half of s 12(3)

The proviso "the aggregate of such sums under each head of expenditure shall not exceed
the total sum so approved" sits under s 12(3)(a): Supply laws, Article 148A(2)
resolutions and Article 148B(1) resolutions. Section 12(3)(b), annotated with Act 3 of 2024
(Article 148B(2) resolutions with the President's concurrence, and Cabinet approvals
under Article 148B(4)), carries no such proviso in this Act. Read literally, a
Cabinet approval under 148B(4) needs neither the President's concurrence nor a cap
here. Whatever limit applies would be in the Constitution, which was not read.
Asserted.

### 4. Loan money that refinances SIGLA borrowing goes into the Revenue Account

s 6(b) puts in the Consolidated Loan Account loan money "that [is] not to refinance an
earlier borrowing under the Significant Infrastructure Government Loan Act 2021";
s 6(a) puts everything else in the Revenue Account. So, literally, a refinancing loan
lands in the Revenue Account. Asserted.

### 5. The Contingencies Fund is a last resort behind virement, and needs the President

s 11(2): an advance needs an urgent **and** unforeseen need, no other provision, funds
that "cannot be provided under section 17(4)" (virement from a surplus subhead of the
same head), and the President's concurrence "in his or her discretion". Virement
itself (s 17(4)) is only within a head; moving an appropriation between heads needs a
s 17A direction, laid before Parliament within 30 days. Asserted.

### 6. Investment: anything but Singapore Government paper

s 7(3) allows bank deposits, bullion, securities of or guaranteed by any government or
international financial institution, "any of the stocks, funds, securities or
investments" (paragraph (d), unqualified as deposited), or anything authorised by law.
s 7(4) forbids investing in "any stock, bond, fund or security issued by the Government
of Singapore". Schedule moneys in a deposit account may go only on bank deposit
(s 7(7)). A guarantee binds Singapore only with the Minister's written authority **and**
the President's concurrence, or in accordance with law (s 15(1)). Asserted.

## What would need doing before this is worth anything

- The Schedule's emptiness should be checked against SSO's web version.
- s 7(3)(d) reads as though words are missing; the web version should be compared.
- The Constitution (Articles 144, 147, 148A, 148B) governs most of these rules and was
  not read.
- The Financial Regulations under s 24 were not retrieved.
- "Which year a month falls in" (s 2) and "the virement cannot exceed the surplus"
  (s 17(4)) are inferences, labelled as such in the module.
