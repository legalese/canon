# Jurong Town Corporation Act 1968 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit says it
"incorporates all amendments up to and including 1 December 2021"; the latest
amending Act annotated in it is 27/2019.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**8 of the 527 Singapore Acts** deposited here cite it. It is an institutional Act,
so this row takes the rules with decision content: the board's size, quorum and
conflicts (s 5), what cannot be delegated (s 8), personal immunity (s 9), what needs
the Minister's or the President's approval (ss 12(4)(l)-(n), 13(4), (5)), spending
against the budget (s 24), the offences and penalties (ss 27, 33, 35, 35A, 35C),
entry for statistics (s 35D), composition (s 67), and the Corporation's capped
liability for goods at Jurong Port (ss 57, 59-62). Appointments, budgets and
accounts procedure, investment, regulations, service of notices, the 1968 EDB
transfer, the 2018 transfer of HDB's industrial undertaking (Part 4) and the s 58
liability contract are not encoded.

The arrangement of sections at the top of the deposit is out of step with the body
(it lists, for example, "26. Power to make rules" and "32. Obstruction"); the body
numbers the rule-making power s 27 and obstruction s 33. This row follows the body.

## What the Act turns out to say

### 1. At Jurong Port the Corporation's liability stops at $2,000 a package, and at nothing if the value was misstated

For ordinary goods the Corporation is not liable at all for misdelivery, short
delivery or non-delivery (s 57(a)), and for damage or destruction not "in the sum of
more than $2,000 per package or unit" unless the nature and value were declared in
writing beforehand (s 57(b)). Transhipment goods are the exception: the Corporation
is liable for their loss from acknowledgment until delivery alongside the
on-carrying vessel (s 59(1)), with the same cap (s 59(2)). Either way it "shall not
in any event be liable" where the value was misstated. Asserted.

### 2. A long list of causes takes the loss outside liability altogether

s 60 lists thirteen causes for which ss 57 and 59 impose no liability, including an
act of God, strikes, insufficient packing and the dangerous nature of the goods.
Fire or flood is excused "unless caused by the actual fault or privity of the
Corporation". Cargo under a general or particular average declaration (s 61(2)) and
a stevedore's default (s 62, the stevedore being deemed the vessel owner's employee
even when the Corporation pays the wage) also carry no liability. Only some of the
s 60 causes are enumerated in the encoding. Asserted.

### 3. The $5,000 limb of the composition ceiling never bites on the offences in the Act

s 67 caps a composition sum at "the lower of" half the maximum fine and $5,000. Every
fine in the Act is $5,000 or $2,000 (ss 27(2)(b), 27(4), 33, 35(3), 35A(7), 35C(3)),
so half the maximum is never more than $2,500. Inference: the $5,000 limb would matter
only for an offence carrying a fine above $10,000, and none appears in the text read.
The ceilings asserted are $1,000 for symbol misuse and $2,500 for obstruction.
Asserted.

### 4. The heaviest penalty is for leaking statistics, not for obstructing the Corporation

Disclosing information gathered under ss 35A or 35B outside the six permitted routes
carries up to one year's imprisonment, or a fine of $2,000, or both (s 35C(3)).
Obstruction (s 33) carries $5,000 or six months, but the text does not add "or to
both". Even a colleague inside the Corporation may not be told unless charged with
s 35A or 35B duties (s 35C(4)). Asserted.

### 5. The guarantee needs the President; the company and the loan need only the Minister

The Corporation may form a company or joint venture (s 12(4)(l)) and lend to a
company it holds shares in (s 12(4)(m)) with the Minister's written approval. To
guarantee loans to such a company needs "the written approval of the Minister and the
President" (s 12(4)(n)). Selling or leasing land is "upon terms that the Corporation
may determine" (s 12(4)(d)). Bonds issued before 1 October 1994 are
Government-guaranteed outright; later ones only if the President concurs (s 13(4),
(5)). Asserted.

### 6. Borrowing can never be delegated, and the quorum floor is 4

s 8 lets the Corporation delegate any power to a committee, the Chairperson or an
employee "except the power to borrow money" or to raise loans. The wording differs
(committees and the Chairperson are barred from raising loans "by the issue of bonds
and debentures", employees from raising loans at all), but since borrowing money is
excluded for all, the encoding finds no case where the difference matters. The board
has a Chairperson and 4 to 14 other members (s 5(1)); the quorum is 4 or one-third of
members in office, whichever is higher (s 5(3)); an interested member's vote is not
counted and the member is not counted in the quorum (s 5(8)). Reading "members in
office" to include the Chairperson is an inference. Asserted.

### 7. Refusing to identify yourself is an offence, and self-incrimination is no excuse

A person the Corporation reasonably believes has broken its rules must furnish
evidence of identity (s 27(3)); refusing without reasonable excuse, or wilfully
misstating it, is an offence with a fine up to $5,000 (s 27(4)), and the person "is
not excused" on the ground of self-incrimination (s 27(5)). Asserted.

### 8. Spending outside the budget is allowed in four cases, two of which must be regularised

s 24(1) bars any payment not covered by a budget item with a sufficient balance.
s 24(2) allows repayable deposits, sums credited in error, land acquisition awards and
court judgments, and expenditure that "cannot be postponed"; the last two must be
provided for in a supplemental budget (s 24(3)). Asserted.

## What would need doing before this is worth anything

- The rules made under s 27 and the regulations under ss 32 and 67(3) (which say
  which offences are compoundable) were not retrieved; the rule offences are modelled
  only by their $5,000 ceiling.
- The s 58 contract by which the Corporation accepts liability for short delivery, and
  goods accepted for storage under s 63, are outside the port rule.
- Only five of the thirteen s 60 causes (fire or flood, act of God, strikes, packing, dangerous goods) are enumerated.
- No case law on ss 57-62 was searched.
