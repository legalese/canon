# Central Provident Fund Act 1953, section 15 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 July 2026.

**Checks:** `l4 run cpf-cases.l4` — 27 assertions satisfied, 0 errors,
0 warnings.

## Scope — read this first

The CPF Act is about **911,000 characters**. This encodes **section 15,
subsections (1) to (6)**, plus the s 2 definition of "applicable person". That
is a few pages out of a very large statute.

Not encoded: contributions (ss 7–9D), the subsidiary accounts (s 13), housing
and investment charges, nominations (s 25), the Retirement Sum Scheme machinery
in s 15AA, the Board's discretionary power in s 15(4), section 16 (which s 15(2)
and (3) are both expressed to be subject to), and everything from Part 3A
onwards.

The prescribed retirement sum, the prescribed classes of applicable person, and
the Board's conditions are all **facts supplied**. The regulations were not
retrieved, and they carry most of the practical content.

## Three observations

**1. There are now only two routes out of the Fund, and one of them is leaving
the country.** s 15(2) once had seven paragraphs. (c) to (g) were repealed
between 2021 and 2024, and what remains is:

- **(a)** the member has attained 55; or
- **(b)** the member **is not an applicable person** — that is, is neither a
  citizen nor a permanent resident of Singapore (nor of a prescribed class).

So the Act's own structure now reads: wait until 55, or cease to be a citizen or
permanent resident. Asserted on the foreigner aged 40, who may withdraw at any
age.

**2. The retirement-sum set-aside binds the member who stays and not the one
who goes.** s 15(6) attaches the set-aside to entitlements under (2)(a), (3) and
(4). It does **not** attach to (2)(b). Two members with identical accounts
therefore come out very differently:

| | credit | retirement sum | may withdraw |
|---|---|---|---|
| citizen, aged 60, s 15(2)(a) | $200,000 | $100,000 | **$100,000** |
| non-citizen, aged 40, s 15(2)(b) | $200,000 | $100,000 | **$200,000** |

Asserted as a pair. There is an obvious policy reading — the retirement sum
exists to fund a retirement in Singapore, and someone who has ceased to be a
citizen or permanent resident is not having one — so this is recorded as a
consequence of the drafting rather than as a defect. It is worth stating because
it is invisible unless (2), (3) and (6) are read together.

**3. s 15(3) attaches to one ground and not the other.** The annual further
withdrawal is for "a member of the Fund who has withdrawn any money from the
Fund **on the ground that he or she has attained 55 years of age**". A member who
withdrew under (2)(b) is outside it — which makes sense, because they were
entitled to the whole sum and have nothing left to come back for, but the
drafting achieves it by naming the ground rather than by saying so.

## An honest limit

`the amount this member may withdraw` is the function a person would actually
want to call, and it is the one least safe to rely on. It reads s 15(1), (2),
(3) and (6), and it **does not** read s 16 (to which (2) and (3) are both
subject), s 15(4) (the Board's discretion to allow more), s 15AA, or any of the
charges that can be registered against an account. A real answer needs all of
those. The function is correct for the subsections it covers and silent about
the rest, which is not the same as being right.

## What would need doing before this is worth anything

- **Section 16**, which both entitlements are expressed to be subject to, and
  which was not read at all.
- The regulations fixing the retirement sum.
- s 15AA, s 15(4), and the charge provisions.
- No case law was searched.
