# Layout-Designs of Integrated Circuits Act 1999 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1/4/2022), as deposited at `../../registers/source-bundle/LDICA1999.txt`. The
edition incorporates amendments up to 1 December 2021; the latest amendment
annotated in the text is Act 25 of 2021 (wef 01/04/2022), in ss 14, 15, 16 and 21.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0083** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The row takes what a chip designer, a chip importer or reseller, or someone who
receives a threatening letter would meet: who qualifies (s 2), ownership (s 6),
protection and its length (ss 5, 7), infringement and its exceptions (ss 8 to 11,
23, 24), groundless threats (s 17), assignments and licences (s 18), and the
Government's duty to tell the owner (s 25). Not encoded: the remedies themselves
(ss 12 to 14), the evidential presumptions (ss 15, 16), prospective ownership
(s 19), exclusive licensees and concurrent actions (ss 20 to 22), Government
remuneration (s 26), the anti-competitive-practice licence (ss 27 to 29) beyond its
effect on infringement, and rules and designations (ss 30, 31).

## What the Act turns out to say

### 1. Selling early shortens protection

s 7: a design first commercially exploited within 5 calendar years after the year
of creation is protected to the end of the 10th calendar year after first
exploitation; "in any other case", to the end of the 15th calendar year after
creation. So a design created in 2010 and never sold is protected to the end of
2025, while one sold in 2010 is protected only to the end of 2020. A design first
sold in 2015 or in 2016 runs to 2025 either way. Reading the year of creation itself
as "within 5 calendar years after" it is an inference. Asserted.

### 2. Genuine chips can be resold and imported freely, wherever first sold

s 10(g): commercially exploiting a copy, chip or article after it "has been
commercially exploited, whether in Singapore or elsewhere, by, or with the consent
of, the qualified owner" is not an infringement. Parallel imports of genuine chips
do not infringe. Asserted.

### 3. An innocent reseller keeps selling only by paying, once they find out

s 11: commercially exploiting an unauthorised chip is not an infringement if, on
acquiring it, the person did not know and could not reasonably have known. Once
aware, the shelter continues "if and only if" the person pays remuneration (agreed,
or set by the Court). Asserted.

### 4. Private and research copying is free; selling the copies is not

s 10(b), (c) protect only the copying, "for a private purpose and not for the
purpose of commercial exploitation" or "for the sole purpose of evaluation,
analysis, research or teaching". A lab that sells its research copies infringes.
A reverse engineer who uses the analysis to make a different original design may
copy and sell that design (s 10(d), (e)), and an independently created identical
design is protected in its own right (ss 5(2), 10(f)). Asserted.

### 5. No registration, and almost anyone qualifies

Protection arises when the design is recorded in documentary form or incorporated
into a chip, whichever is earlier (s 5(4)); no registration step appears in the Act.
"Qualifying country" includes every WTO member other than Singapore (s 2), and a
non-qualifying owner still qualifies if the design was first commercially exploited
in Singapore or a qualifying country. Designs created before 15 February 1999 are
not protected (s 5(3)). Asserted.

### 6. Threats over selling can be challenged; threats over making or importing cannot

s 17: a person aggrieved by a threat of infringement proceedings may seek a
declaration, injunction or compensation, "whether or not the person making the
threat is a qualified owner". But not over a mere notice that the right exists
(s 17(3)), not where the alleged infringement is "making or importing anything"
(s 17(4)), not if the threatener shows the acts infringe (s 17(2)), and not against
an advocate and solicitor acting for a client (s 17(5)). Asserted.

### 7. The Government may use a design, but not sell it to the public

s 23: Government use (or use authorised in writing, even after the event) for a
public non-commercial purpose is not an infringement, but s 24(1)(d) does not permit
sale to the public. The Government must tell the owner "promptly", or in an
emergency "as soon as reasonably practicable", unless that would prejudice defence or
security (s 25), and must pay remuneration (s 26, not encoded). Asserted (except s 26).

### 8. An assignment must be written and signed; a licence survives a sale

s 18(3): an assignment "is ineffective unless it is in writing and signed by or on
behalf of the assignor". s 18(4): a licence binds successors in title except a
purchaser in good faith for value without notice, and those deriving title from one.
Asserted.

## What would need doing before this is worth anything

- No Minister's designation under s 31 and no rules under s 30 were retrieved.
- s 24(1)(e) (Government use "predominantly in Singapore") and s 24(1)(c) (the terms
  of the authorisation) are not modelled.
- The effect of a s 27 Court licence on infringement is taken to be that of consent;
  the Act says only that the licence is granted and is non-exclusive and
  non-assignable (s 28).
- "Original" and "commonplace" (s 5(1)) are taken as given facts, not decided.
- No case law was searched.
