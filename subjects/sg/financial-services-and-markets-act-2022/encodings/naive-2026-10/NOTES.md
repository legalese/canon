# Financial Services and Markets Act 2022 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 18 of 2022 (not a 2020 Revised Edition Act), current version as at
1 October 2026, informal consolidation, with amendments to Act 5 of 2025 (wef
9 March 2025) annotated.

**Checks:** one case file, 76 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**20 of the 527 Singapore Acts** deposited here cite it. Most of the Act is MAS's
toolkit for supervising, rescuing and resolving financial institutions (Parts 2, 4,
4A, 5, 7, 8, 10, 10A), which an ordinary person never meets. This row takes the two
places where a person or business meets it directly: being barred by a **prohibition
order** (ss 7, 8), and running a **digital token** business out of Singapore (Part 9:
ss 136(1), 137, 138(3), 139, 141(1), 147, 149, 153, 154, 163). The First Schedule
(what a "digital token service" is) and the Second Schedule (exempt providers) were
not read; whether a service is one, and whether s 137(5) excludes the provider, are
inputs.

## What the Act turns out to say

### 1. The digital token licence is about serving customers *outside* Singapore

s 137(1) bars an individual or partnership from carrying on, "from a place of business
in Singapore", a business of providing a digital token service "outside Singapore"
without a licence; s 137(3) bars a Singapore corporation from doing so "whether from
Singapore or elsewhere". A provider serving only customers in Singapore is not caught
by s 137 at all (the encoding does not say whether some other Act catches it). A
foreign corporation is named in neither subsection; the encoding treats it as outside
s 137, which is an inference from silence. Asserted.

### 2. "It's only a side-line" is expressly no answer

s 137(2) and (4): a person providing the service while carrying on any other business is
presumed to carry on a business of providing it, and the presumption "is not rebutted by
proof that the provision ... is related or incidental" to the primary business. The
encoding takes the incidental flag and ignores it. Asserted.

### 3. Being exempt from licensing does not let you call yourself a licensee

s 139(4) disapplies the holding-out offences in (2) and (3) to a person excluded by
s 137(5), but not (1): anyone who holds itself out "as a licensee" without a licence
commits an offence, whatever its exemption. Asserted.

### 4. A prohibition order reaches the employer too, and the defence is only for indirect use

s 8(2): a financial institution must not employ, contract with or use the services of a
prohibited person, "whether directly or indirectly", to the extent of the prohibition
($100,000, s 8(4)). The s 8(5) defence of reasonable steps and reasonable belief is
available only to an institution charged for **indirect** use; direct use has no
statutory defence. The prohibited person faces $150,000 or 2 years (s 8(3)). The order
does not avoid the person's own contracts (s 8(9)). Asserted.

### 5. Two different 5% tests

s 7(7)-(8) makes a person a "substantial shareholder" (for prohibition orders) at 5% of
the votes, or 5% of the votes in any one class. Part 9 instead bands controllers of a
licensee at 5%, 12% and 20% of shares **or** votes (s 136(1)), and only the 20% band
needs MAS approval in advance (s 149(1)). Crossing 20% unawares is defensible only by
notifying MAS within 14 days and taking the action MAS directs (s 153(3)); a family
associate's increase is a defence even if aware, on the same terms (s 153(4)).
Asserted.

### 6. Licensees may not lend to individuals in Singapore

s 147(1): a licensee "must not carry on a business of granting any credit facility to
any individual in Singapore" ($100,000 plus $10,000 a day). Corporate customers and
individuals outside Singapore are not mentioned. Asserted.

### 7. Penalties

Unlicensed business, holding out and controller offences: individual $125,000 or 3 years
or both, plus $12,500 a day; any other person $250,000, plus $25,000 a day (ss 137(6),
139(5), 153(2)). The Part 9 default is $50,000 / $100,000 (s 163). Appeals to the
Minister on prohibition orders and controller decisions run 30 days (ss 7(5), 154).
Asserted.

## What would need doing before this is worth anything

- The First and Second Schedules, and regulations under s 192 that can switch the
  s 137(5)(a) exclusions off, were not read.
- The commencement of Part 9 was not checked. The deposit annotates the s 6 definition of
  "digital payment token instrument" as inserted by Act 18 of 2022 wef 30 June 2025,
  which suggests (inference) the Act commenced in stages.
- s 138(3)'s conditions are collapsed into five flags; the "prescribed class" routes
  for a non-resident director are folded into one.
- Revocation (s 141(2)) was read in part, and s 36 (dispute resolution membership,
  $50,000) was read; neither is encoded. Officer approval (s 155) was not read.
- No MAS guidance, notice or case law was searched.
