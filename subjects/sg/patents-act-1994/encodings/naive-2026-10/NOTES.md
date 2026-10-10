# Patents Act 1994 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit says it
incorporates "all amendments up to and including 1 December 2021"; later amendments
are annotated in the text, the latest seen being Act 5 of 2025 (wef 9 March 2025).

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes the rules an
inventor, employer, competitor or seller actually meets: what is patentable (ss 13 to
16), filing abroad by residents (s 34), term, renewal and restoration (ss 36, 39),
employees' inventions (ss 49, 50), infringement and its exceptions (s 66), the
innocent infringer (s 69), the prior user (s 71), groundless threats (s 77), and the
false-claim offences and their penalties (ss 34(3), 98 to 100). The Registry,
priority dates, the application and examination procedure, extension of term
(s 36A), amendment, the register, licences, Government use, revocation,
international applications, proceedings and patent agents are not encoded.

## What the Act turns out to say

### 1. A Singapore resident may not file abroad first

s 34(1): a person resident in Singapore must not, without the Registrar's written
authority, file a patent application outside Singapore unless the same invention was
filed in the Registry **at least 2 months** earlier and no s 33 directions (s 33 is headed
"Information prejudicial to defence of Singapore or safety of public") are in force. The penalty is $5,000 or **2 years** or
both, the heaviest imprisonment term in the Act's offences read here. "Resident"
includes anyone living in Singapore on a valid pass (s 34(4)(c)). Inventions first
filed abroad by a non-resident are exempt (s 34(2)). Asserted.

### 2. An employee's invention is the employer's only on the stated tests, and only if Part 9 applies

s 49(1) gives an invention to the employer "despite anything in any rule of law" if
made in normal or specifically assigned duties where an invention might reasonably be
expected, or in the course of duties by someone with a special obligation to further
the employer's interests. Everything else belongs to the employee (s 49(2)). But
s 50(1) switches the Part off unless the employee was mainly employed in Singapore, or
not mainly employed anywhere and attached to a Singapore place of business; for an
employee mainly employed abroad the Part says nothing either way. s 50(4) preserves
contracts about the right to an invention (not encoded). Asserted.

### 3. Your own disclosure in the 12 months before filing is forgiven

s 14(4)(e): a disclosure made to the public by the inventor (or someone who got it from
the inventor) is disregarded if it happened within the 12 months before the **filing**
date, alongside disclosures in breach of confidence, at an international exhibition,
or to a learned society. The window counts back from filing, not from priority. A
disclosure 13 months out destroys novelty. The written-evidence requirement in s 14(8)
is not encoded. Asserted.

### 4. Parallel imports are allowed, except one narrow pharmaceutical case

s 66(2)(g) makes it non-infringing to import or deal in goods put on the market by or
with the proprietor's consent, anywhere in the world. s 66(3) withdraws that only for
a patented pharmaceutical product never sold in Singapore with consent, where the
import breaches a distribution contract of the proprietor and the importer knows or
has (deemed, s 66(4)) notice. Asserted.

### 5. Private use must also be non-commercial; experiments and approval trials are free

s 66(2)(a) needs both "privately" and "not commercial". Experimental use on the
subject matter (b), extemporaneous prescription medicines (c) and acts supporting a
pharmaceutical marketing approval application (h) are also exceptions. Infringement
must be in Singapore, while the patent is in force, and without consent (s 66(1)).
Asserted.

### 6. Marking "patented" without the number does not defeat the innocent infringer

s 69(1): no damages or account of profits against a defendant who proves they did not
know and had no reasonable grounds to suppose the patent existed. s 69(2): the word
"patent" or "patented" on a product does not give reasonable grounds "unless the
number of the patent accompanied the word". s 69(1) names only damages and an account
of profits; the encoding does not decide injunctions. Asserted.

### 7. False patent claims: $10,000 or 12 months, with a grace period and a due diligence defence

s 99: falsely representing a product sold as patented, including by marking it. s 100:
"patent applied for" or "patent pending" where no application was made, or it was
refused, withdrawn or abandoned. Both excuse a reasonable period after expiry,
revocation or refusal, and both allow the accused to prove due diligence. Asserted.

### 8. Term is 20 years from filing, and lapses without renewal fees

s 36(1): the patent runs from issue of the certificate of grant to the end of 20 years
from filing (subject to s 36A). It ceases if a renewal fee is not paid in the
prescribed period (s 36(2)) but revives as if it had never expired if paid with the
additional fee in the further period (s 36(3)). After that, the Registrar **must**
restore on an application in time if the failure was unintentional (s 39(5)). The
periods are prescribed by rules not retrieved. Asserted.

### 9. Prior users keep going, and groundless threats are actionable

s 71: a person who in good faith did the act, or made effective and serious
preparations, in Singapore before the priority date may continue, but may not license
it; a business may assign it with that part of the business. s 77: anyone aggrieved
by a threat of infringement proceedings may sue unless the threatener proves
infringement and the patent is not shown invalid; a mere notification of the patent
is not a threat, and threats about making, importing or using a process are outside
the section. Asserted.

## What would need doing before this is worth anything

- The Patents Rules (prescribed periods, renewal fees, restoration periods, prescribed
  dates for the term) were not retrieved.
- Process infringement (s 66(1)(b), (c)), the vessel and aircraft exceptions
  (s 66(2)(d) to (f)), named-patient imports (s 66(2)(i)) and the health-product export
  carve-out (s 66(6)) are in comments only.
- s 36A extension of term, s 67(2) election between damages and profits, and s 68's
  reversal of the burden of proof are not encoded.
- No case law was searched; "inventive step", "state of the art" and "special
  obligation" are taken as given facts.
