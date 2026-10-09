# Pensions Act 1956 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 33 of
2021). Includes the First Schedule Pensions Regulations.

**Checks:** one case file, 65 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**29 of the 527 Singapore Acts** deposited here cite it. This row covers nearly the whole
Act and the rate and option rules in the First Schedule regulations. Not encoded: the
Pension Authority machinery, the injury and killed-on-duty regulations (20 to 23), the
Gurkha regulation, and Tables A and B.

## What the Act turns out to say

### 1. If you don't choose, you lose the pension

Reg 15(4): "An officer who has not exercised an option ... is deemed to have opted to
receive a commuted pension gratuity ... without any pension." An officer who forgets to
elect receives a lump sum and no monthly pension. Asserted.

### 2. The commutation factor does not say what it multiplies

Reg 16(2) and s 20(4): the lump sum is "the commutation factor" (175.14) times "the amount
of such pension". Neither says annual or monthly. Times the annual pension, it would be
175 years' worth; times the monthly pension, about 14.6 years'. **The encoding takes the
monthly figure. That is an inference; the text does not state it.**

### 3. The rate, and where it stops

Reg 4: at least 10 years' service, then 1/600 of annual pensionable emoluments per
complete month. s 14 caps the pension at two-thirds of the highest emoluments, so **400
months (33 years 4 months) reaches the cap** and later service adds nothing. Under 10
years, reg 26 gives a gratuity of up to 5/600 per month instead. On abolition of office,
reg 18 accrues faster: 1/500 per month for the first 240 months. Asserted.

### 4. Sex-specific rules that remain on the face of the Act

- **s 11(2)(a):** pension age 55 for a man, 45 for a woman (for those in service before
  1 March 1962 who opted).
- **s 16:** call-back liability runs to 50 for a man and 45 for a woman.
- **s 15:** a pension can be attached only for a Government debt or a maintenance order for
  the officer's "wife or former wife or minor child". A husband's maintenance order cannot
  reach a female officer's pension.
- **s 17(3):** on bankruptcy, the Authority may apply the pension to "any wife, child or
  children"; a husband is not mentioned.

Asserted.

### 5. Smaller things worth recording

- **s 3(4):** the Act does not apply to officers appointed on or after 1 April 1986, except
  in designated schemes. Most civil servants since then are on the CPF.
- **s 19:** taking private work without permission can end the pension, but only within 5
  years of retirement.
- **s 20:** a death-in-service gratuity is never less than one year's emoluments. Death
  within a year of retirement brings a top-up to one year's emoluments.
- **Reg 16:** the reduced pension is cut by 2/25 of the gratuity, which is a 12.5-year
  payback, matching the restoration in reg 15(5).

## What would need doing before this is worth anything

- **Confirm the commutation factor's base** (finding 2) against the Pension Authority's
  practice or any amending order.
- Reg 12 (which emoluments to use, including the three-year averaging) is reduced to a
  single input.
- No case law, and no orders varying the commutation factor or discount rate, were
  retrieved.
