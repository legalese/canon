# Variable Capital Companies Act 2018 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 24
of 2025).

**Checks:** one case file, 47 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**37 of the 527 Singapore Acts** deposited here cite it, mostly s 2 (20) and s 58
(8). Most of the Act's 388,000 characters apply the Companies Act with
modifications. This row takes what makes a VCC different -- one object, sub-fund
ring-fencing, a mandatory licensed manager, a board tied to the manager -- and
what a director or member can be liable for.

## What the Act turns out to say

### 1. Investors -- not directors -- lose limited liability when the board is incomplete

s 48(11): if a VCC carries on business for more than six months without a director
ordinarily resident in Singapore and a director linked to the manager, a person who
"is a **member** of the VCC" and "**knows**" it is trading that way "is liable for the
payment of **all the debts** of the VCC contracted during the period". The liability
lands on members, the fund's investors, not on its directors. Asserted at months 5
and 8.

### 2. Sub-fund ring-fencing cannot be contracted out of

s 29(1): a sub-fund's assets must not be used for any other sub-fund's or the VCC's
liabilities, "despite any written law or rule of law to the contrary". s 29(2): a term
of the constitution, "an agreement, a contract or otherwise" inconsistent with that
"is void". A cross-guarantee from sub-fund B for sub-fund A's lender is void however
it is drafted. Asserted.

### 3. A director cannot leave the board short

s 48(5), (6): a director "must not resign or vacate his or her office" unless the
required resident and manager-linked directors remain, and a resignation in breach
"is invalid". Only disqualification or removal lets the last such director go (s
48(7)). Asserted.

### 4. Disqualification turns on the offence's maximum, not the sentence

s 58(1)(a)(i): a conviction, in Singapore or elsewhere, for an offence "involving fraud
or dishonesty and **punishable** with imprisonment for a term of 3 months or more"
disqualifies for five years -- from conviction if not imprisoned, from **release** if
imprisoned (s 58(4)). A fine for a fraud offence carrying a 3-year maximum
disqualifies as surely as a prison term. Asserted.

### 5. Smaller things worth recording

- **s 15:** a VCC's "sole object" is to be one or more collective investment schemes;
  carrying on other business exposes each officer in default to $150,000 or 2 years.
- **s 46:** the manager must be a fund-management licensee (not a suspended one) or an
  exempt person such as a bank; "A VCC cannot be its own manager".
- **s 18(2):** the Registrar **must** refuse registration if no director is a director or
  representative of the manager; the Minister's decision on appeal is final.
- **s 35(2):** only fully paid shares may be redeemed.
- **s 53(8):** a direction to remove an unfit director has effect while the appeal is
  pending.

## What would need doing before this is worth anything

- **The Companies Act and IRDA as applied** (ss 5 to 6A) govern most of a VCC's life
  and are not encoded; the `companies-act-1967` row covers only its definitions core.
- The VCC Regulations (prescribed managers, fit-and-proper factors) were not retrieved.
- **No case law was searched.**

## Source refreshed after encoding (10 Oct 2026)

This row was encoded against the deposit as it stood before the source refresh: the SSO consolidation current at the
earlier retrieval, still in git at commit da331074. The deposit has since been replaced by the consolidation current as at
9 October 2026, whose text differs. **The row has not been re-checked against the refreshed text.** Its assertions do not
read the source, so they still pass; whether the encoded provisions changed is an open question.
