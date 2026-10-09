# Limited Liability Partnerships Act 2005 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 21
of 2024 and Act 30 of 2024).

**Checks:** two case files, 117 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**115 of the 527 Singapore Acts** deposited here cite it, second only to the
Companies Act. Most of those citations go to s 2 (92 Acts) and s 4 (19): other
Acts pull LLPs into "body corporate". The Act is 478,000 characters. This row
takes the part that decides what a partner owes and can do: Part 2, the
two-partner and manager rules, the First Schedule's default terms, and the
Second Schedule's rule on partners' liability after a firm converts.

**Not encoded:** registration and names, conversion of a company, annual
declarations and accounts, receivership and winding up, the register of
controllers, disqualification, striking off, and the offences machinery.

## What the Act turns out to say

### 1. The carve-out from limited liability is for tort only

s 12(1) makes every obligation of the LLP, "whether arising in contract, tort or
otherwise", solely the LLP's. s 12(3) preserves a partner's personal liability
"**in tort** for the partner's own wrongful act". A partner who personally
breaches a contract the LLP made is not liable on it. A partner is never liable
for another partner's wrong. Asserted.

### 2. The LLP's vicarious liability does not run to fellow partners

s 12(4): where a partner is liable "to any person (**other than another partner**)"
for a wrongful act in the course of the business, the LLP is liable to the same
extent. A partner injured by a co-partner's negligence at work cannot use (4).
Asserted.

### 3. An unauthorised partner binds the LLP unless the other side knew, or did not think them a partner

s 13(2): the LLP escapes only if the partner had no authority **and** the person
either knew that or did not know or believe them to be a partner. A supplier who
believes they are dealing with a partner, and does not know of a limit on
authority, binds the LLP. s 13(3): a former partner still binds the LLP until the
person dealing has notice **or notice is delivered to the Registrar**; filing is
enough even if the supplier never looked. Asserted.

### 4. A bankrupt partner's default right to manage is an offence to exercise

s 16(a): bankruptcy does not end the partnership (unless the agreement says so),
"but the restriction ... under section 58 applies". First Schedule para 4: "Every
partner may take part in the management". s 2(1): a "manager" is anyone "concerned
in or takes part in the management", partner or not. s 58: an undischarged bankrupt
who acts as manager without the court's or the Official Assignee's permission
commits an offence ($10,000 or 2 years). Under the default terms the right and the
offence collide. Asserted.

### 5. Equal shares in capital, not just profits

First Schedule para 2: absent agreement, partners "share equally in the **capital**
and profits". A partner who contributed $900,000 and one who contributed $100,000
each take $500,000 of capital. Voting is one vote per head (para 7); admitting a
partner needs everyone (para 6); no expulsion without an express power (para 11);
no remuneration (para 5). Asserted with a two- and three-partner list.

### 6. Converting a firm keeps the partners on the hook for old contracts, including future liabilities under them

Second Schedule para 15(1): every partner of a converted firm "continues to be
personally liable" for the firm's liabilities incurred before conversion "**or which
arose from any contract entered into prior to the conversion**". Rent under a lease
the firm signed falls on the former partners personally for its whole term, with an
indemnity from the LLP (para 15(2)). Para 2: conversion is possible only if the
LLP's partners are exactly the firm's partners. Asserted.

### 7. The one-partner LLP: liability turns on knowledge

s 28(2): if the LLP trades with fewer than two partners for more than two years, a
partner becomes personally liable for obligations incurred **after** the two years,
but only if they **knew** the two years had passed. The text says "knew", not
"ought to have known". Asserted at 24 and 30 months.

### 8. Smaller things worth recording

- **s 15:** absent agreement, a partner can leave on 30 days' notice and is paid
  capital plus share of accumulated profits net of losses, as at the date of
  leaving: nothing for goodwill.
- **s 17:** an assignee of a partner's interest gets distributions only, never a
  vote, management or partnership.
- **s 29:** the required manager must be a natural person, at least 18 and
  ordinarily resident in Singapore. Breach is an offence by the LLP **and every
  partner**.
- **s 7:** a deed needs two partners' signatures, or one witnessed; a person signing
  for two LLPs must sign separately in each capacity.
- **s 11:** a trade union, a platform work association or an unincorporated firm
  cannot be a partner.

## What would need doing before this is worth anything

- **No case law was searched.** The interaction in finding 4 and the reach of
  para 15 in finding 6 may have been decided.
- The rest of the Act, above all the register of controllers (Part 6A) and striking
  off, which are where most compliance questions arise.
- The LLP Regulations were not retrieved.
