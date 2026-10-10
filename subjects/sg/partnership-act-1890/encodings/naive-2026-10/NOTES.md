# Partnership Act 1890 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1/4/2022), as deposited at `../../registers/source-bundle/PA1890.txt`. The latest
amendment annotated is Act 25 of 2021 (Courts (Civil and Criminal Justice) Reform
Act 2021), commenced 1 April 2022, at s 23(1). The legislative history records that
the Act was declared to apply in Singapore on 12 November 1993 by the Application of
English Law Act 1993. The arrangement of sections at the top of the deposit is out of
step with the body (it lists "Definition of partnership" at 2); the encoding follows
the body, where the definition is s 1 and the short title s 47.

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0028** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. The row takes what two or three people running a business
together actually meet: whether they are partners at all (ss 1-3), when one binds
the firm and who pays its debts (ss 5, 7-9, 14, 17, 36), the default rules between
them (ss 19, 24, 25), how the partnership ends (ss 32-35), the outgoing partner's 5%
option (s 42) and the order in which money is paid out at the end (s 44). Not encoded:
wrongs and trust property (ss 10-13), admissions and notice (ss 15, 16), guarantees
(s 18), partnership property and charging orders (ss 20-23), ss 26-31 (notice by deed,
continuance, accounts, private profits, competition, assignees), and ss 37-41, 43.

## What the Act turns out to say

### 1. Partnership needs no registration and no agreement — only conduct

s 1(1): partnership "is the relation which subsists between persons carrying on a
business in common with a view of profit". Nothing in this Act requires writing,
registration or an intention to be partners; only a registered company or a body
incorporated under another Act is excluded (s 1(2)). Receiving a share of profits is
"prima facie evidence" of partnership (s 2(c)), though not conclusive. Asserted.
(Whether business registration is required elsewhere is a matter for other Acts, not
read.)

### 2. Every partner is liable for every firm debt incurred while he is a partner

s 9: each partner is liable "jointly with the other partners for all debts and
obligations of the firm incurred while he is a partner". Retiring does not end it
(s 17(2)); only a three-way agreement with the new firm **and** the creditor
discharges him (s 17(3)). An incoming partner is not liable for earlier debts
(s 17(1)). Someone who lets himself be held out as a partner is liable to a creditor
who gave credit on that faith (s 14). Asserted.

### 3. A Gazette notice protects a retiring partner only against strangers

s 36(1): a customer may treat apparent members of the old firm as still members
"until he has notice of the change". s 36(2): a Gazette advertisement is notice only
"as to persons who had no dealings with the firm before" the change — existing
customers must actually be told. A retiring partner who was never known to the
creditor as a partner is not liable (s 36(3)). Asserted.

### 4. Defaults: equal shares, no salary, 5% on advances, unanimity for big things

Subject to agreement, s 24 gives equal shares of capital and profits regardless of
contribution (a), no remuneration (f), 5% a year on advances beyond agreed capital
(c), majority rule for ordinary matters but all partners for a change in the business
(h) or a new partner (g). s 25: no majority can expel a partner without an express
power. Simple interest and "majority of all partners" are inferences. Asserted.

### 5. Death or bankruptcy of one partner dissolves the whole firm by default

s 33(1): "every partnership is dissolved as regards all the partners by the death or
bankruptcy of any partner" — subject to agreement. Illegality dissolves "in every
case" (s 34), agreement or not. A charge on a partner's share only gives the others
an option (s 33(2)); incapacity or loss-making needs a court decree (s 35), and
grounds (a)-(c) must concern a partner other than the applicant. Asserted.

### 6. At the end, outsiders first, then advances, then capital, then residue

s 44(b): assets go to outside creditors, then partners' advances, then capital, then
the residue in profit-sharing proportions. A deficiency, including lost capital, is
borne by partners "in the proportion in which they were entitled to share profits"
(s 44(a)) — profit ratio, not capital ratio. In the worked case (assets $80,000,
outside debts $30,000, advances $20,000, capital $60,000, profits shared equally) each
partner contributes $15,000 to the $30,000 deficiency, and the partner who advanced
$20,000 and put in $40,000 of capital nets $45,000. Asserted.

## What would need doing before this is worth anything

- No case law was read: holding out, apparent authority and "just and equitable"
  dissolution are case-driven, and none of it is here.
- s 3 is read as applying to profit-linked loans whether or not the s 2(c)(iv)
  writing proviso is met; that is an inference.
- s 8 notice of a restriction is folded into "knew he lacked authority".
- Partners who cannot pay their contribution under s 44(a) are not modelled.
- The Limited Partnerships Act and the Limited Liability Partnerships Act were not
  read.
