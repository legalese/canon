# Intestate Succession Act 1967 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/ISA1967.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021; no later amendment is annotated in the text.

**Checks:** one case file, 45 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it decides who inherits when a
non-Muslim dies in Singapore without a will, or with a will that leaves part of the
estate undisposed of. It was not chosen by citation count. The Act is ten sections
long, so this row covers all of the operative provisions, ss 2 to 10. Not encoded:
the Probate and Administration Act 1934 (administration, and the "expenses of due
administration" deducted first under s 5), Muslim law (excluded by s 2), the foreign
law that governs movables of a person domiciled abroad (s 4(1)), and the Legitimacy
Act and adoption legislation, which were not read. Shares are modelled as dollar
amounts of the net estate.

## What the Act turns out to say

### 1. A spouse with no children and no parents takes everything — the siblings get nothing

Rule 1: with a surviving spouse, "no issue and no parent, the spouse shall be
entitled to the whole of the estate". Brothers and sisters only come in under rule 6,
which needs "no surviving spouse, descendants or parents". Asserted.

### 2. Parents are shut out by any issue

With a spouse and issue, the spouse takes half (rule 2) and the issue the rest
(rule 3). Rules 4 and 5 give parents a share only where there is no issue. With no
spouse, children take the whole and a surviving parent takes nothing. Asserted.

### 3. The line stops at uncles and aunts; after that, the Government

Rule 8 reaches uncles and aunts; rule 9 gives "the Government" the whole estate "in
default of distribution under rules 1 to 8". No rule names cousins, great-uncles or
step-relatives, and rule 6 reaches only the "children of deceased brothers or
sisters", not their grandchildren. A person survived only by cousins leaves the estate
to the Government. Asserted.

### 4. "Child" means legitimate or court-adopted in Singapore, Malaysia or Brunei

s 3 defines "child" as "a legitimate child" and includes a child adopted by court
order under the law of Singapore, Malaysia or Brunei Darussalam. On the text of this
Act alone, a child adopted elsewhere, or a child who is not legitimate, is not a
"child". Whether other legislation (for example on legitimation or recognition of
foreign adoptions) changes this was not checked. Asserted on the text only.

### 5. More than one widow share the single spouse's share

s 8: where the intestate leaves "more than one wife, such wives shall share among them
equally the share" one wife would have taken. Two widows with children therefore take
a quarter each. The section speaks only of wives. Asserted.

### 6. Where the Act reaches, and where it does not

s 4: movables follow the law of the domicile; immovables follow this Act "wherever he
may have been domiciled". But s 5 distributes only (a) property situated in Singapore
of a person domiciled here and (b) immovable property in Singapore of a person
domiciled abroad. So a foreign-domiciled person's Singapore bank account is outside
it, and so (on s 5) is land abroad of a Singapore domiciliary — though s 4(2) read
alone would seem to claim it. The encoding follows s 5. Asserted.

### 7. Half blood come after whole blood; lifetime gifts are not deducted

s 6(b): relatives of the half blood "rank immediately after those of the whole blood
related to him in the same degree". This encoding reads that, as an inference, to mean
half-siblings take only when no whole-blood sibling stock exists. s 9: gifts the
intestate made in life for a child's advancement are not taken into account. s 6(a):
posthumous children and maternal relatives are treated alike (stated in comments, not
separately tested). Asserted.

## What would need doing before this is worth anything

- The s 4(2) / s 5 tension over immovables abroad needs case law.
- The meaning of "rank immediately after" in s 6(b) is inferred, and its effect on
  half-blood uncles and aunts is not modelled.
- The Legitimacy Act 1934, the Adoption of Children Act and the Probate and
  Administration Act 1934 were not read.
- Rule 3's "reversionary interest" language and the s 10 interaction with a will's
  own provisions are modelled only as a yes/no on whether a part passes.
- No case law was searched.
