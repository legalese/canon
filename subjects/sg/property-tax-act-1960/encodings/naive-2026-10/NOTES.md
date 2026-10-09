# Property Tax Act 1960 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 33 of
2022).

**Checks:** one case file, 37 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**36 of the 527 Singapore Acts** deposited here cite it, 24 of them for s 10 (the
Valuation List): other Acts measure their own charges by annual value. This row
takes what an owner pays and how to dispute it. **The rate orders under s 9(2) --
which set the owner-occupier and other progressive rates most owners actually pay
-- were not retrieved.** The statute's own rate is 36%, and the cases use it or a
stand-in.

## What the Act turns out to say

### 1. A seller who gives no notice keeps paying

s 19(1): the vendor must give notice of a sale "within one month". s 47(1): until
that notice is given, the seller "continues to be liable for the payment of all
taxes payable in respect of the property" falling due. The buyer is liable too
(s 47(2)), and the tax is a first charge on the property (s 6(4)). A seller who
forgets the notice remains liable for next January's tax on a property they no
longer own. Asserted.

### 2. A demolished building can be taxed as standing -- whoever was at fault

s 19(4): where a building is demolished "and no action has been taken to amend the
Valuation List in respect thereof **for any reason**", the owner must, "at the
option of the Comptroller", continue to pay "as if the building had not been
demolished". "For any reason" includes the Chief Assessor's own inaction after the
owner gave the 15-day notice required by s 19(3). Asserted with and without timely
notice.

### 3. Owners can pass tax up to a ground landlord, whatever the lease says

s 6(10): an owner who holds subject to a rent and has paid the tax may deduct from
that rent the tax multiplied by rent over annual value, "**despite any stipulation to
the contrary**". Not from rent payable to the Government or a public authority
(s 6(11)) -- which excludes most state leases. Asserted.

### 4. Object any time in the year; but pay first

s 20A(1): an owner may object to the annual value "at any time in that year"; an
objection to an amendment must be within 30 days. s 35A: tax is payable on the
listed value "even if" an objection or appeal is pending. s 20A(7): an appeal to the
Valuation Review Board lies only from a decision that disallowed the objection or
allowed it in part, within 30 days, with a late-appeal discretion for absence,
sickness or reasonable cause (s 29(4)). Asserted.

### 5. Smaller things worth recording

- **s 6(5):** no tax on property whose annual value is **$18 or less**.
- **s 6(6):** exemption needs **exclusive** use for worship, a grant-aided school,
  charity or social development; any commercial letting of the same part defeats it.
- **s 36:** a late-payment penalty of up to 5% of the outstanding tax, remissible for
  good cause.
- **s 6(15):** refund claims within five years.
- **s 2:** annual value is the yearly rent reasonably expected with the **landlord**
  paying repairs, insurance, upkeep and taxes other than GST.

## What would need doing before this is worth anything

- **Retrieve the Property Tax (Residential Property) orders** and other s 9(2) orders;
  without them no case here computes a real owner-occupier's tax.
- **No case law was searched.** Annual value has a large body of Valuation Review
  Board and High Court decisions.
- Recovery by agent declaration (s 38), attachment and sale are not encoded.
