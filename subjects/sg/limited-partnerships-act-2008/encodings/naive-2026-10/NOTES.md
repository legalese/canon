# Limited Partnerships Act 2008 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 21 of
2024, in force 9 December 2024).

**Checks:** one case file, 34 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**18 of the 527 Singapore Acts** deposited here cite it. This row covers nearly the whole
of Part 2 (rules of law) and the registration provisions that change a partner's
liability. The Registrar's procedures, name reservation, changes in particulars,
records and inspection are not encoded.

## What the Act turns out to say

### 1. An unregistered limited partner is a general partner

s 10(1): a limited partner "is deemed to be a general partner of the firm unless the
limited partner is registered as a limited partner". The agreement alone gives no
protection. And s 10(3)-(6): a creditor who dealt with the firm **before** registration
may treat it as a general partnership until they have notice. Registration is notice
only to those with no prior dealings. Asserted.

### 2. Meddling costs only the debts incurred while meddling

s 6(2): a limited partner who takes part in management is liable as a general partner
"for all debts and obligations ... incurred while so taking part". Debts from before
or after are still limited. Asserted.

### 3. The safe harbours are wide

The First Schedule (non-exhaustive) lets a limited partner do the following without
counting as management:
- guarantee the firm's debts
- be a director of the corporate general partner
- advise on strategy
- vote on any transaction, including investments and removing a general partner
- sue when the general partners refuse without good cause
- have their name in the firm's name

What is left is the day-to-day running: negotiating contracts and signing cheques.
Asserted.

### 4. Clawback of distributions needs three things at once

s 7(2): a limited partner refunds a distribution only if **every** general partner was
or became insolvent, the limited partner knew or ought to have known, **and** every
general partner is made bankrupt or wound up within **one year**. If one general partner
stays solvent, or bankruptcy comes at month 13, there is no clawback. Asserted.

### 5. A limited partner's death or bankruptcy does not dissolve the firm

s 8 reverses Partnership Act 1890 ss 32 and 33 for limited partners: no dissolution by
their notice, death, bankruptcy or a charge on their share, unless the agreement says
otherwise. **Simplified:** general partners' events are encoded as always dissolving.
Under the 1890 Act that too is subject to agreement. Asserted.

### 6. Smaller things worth recording

- **s 5(b):** new partners may be admitted without the limited partners' consent, unless
  agreed otherwise.
- **s 16:** the name must contain "limited partnership" or "LP".
- **s 28:** a local manager may be required only where **every** general partner lives
  abroad.
- **s 29:** an undischarged bankrupt may not take part in management without permission.

## What would need doing before this is worth anything

- The Partnership Act 1890, which s 4 applies to everything not displaced, has no row
  here.
- "Taking part in the management" beyond the First Schedule is for the courts. No case
  law was searched.
