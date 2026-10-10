# Companies Act 1967, the definitional core — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation carrying amendments to
Act 24 of 2025 in force from 6 May 2026.

**Checks:** four case files, 335 assertions satisfied, 0 errors, 0 warnings.

## Why this part of this Act

A citation count across the 527 Singapore Acts deposited in this repository found
**154 Acts that cite the Companies Act**, three times as many as any other
unencoded Act. The citations concentrate: **section 4(1) alone is cited 235
times**, the most-cited single provision in the corpus, followed by s 5, s 6 and
s 7. Most of the citations are bare ("a subsidiary within the meaning of the
Companies Act 1967"), which is a request for the definitions in this row.

The Act is about 1.35 million characters. This encodes about 60,000 of them, and
nothing here should be read as covering the other 1.29 million.

## Scope

| provision | what it settles |
|---|---|
| s 4(1) | 13 of its roughly 75 defined terms: corporation, foreign company, company, private and public company, exempt private company, director, officer, voting share, debenture, listed, constitution |
| s 4(2)–(5A), (8)–(11), (13) | shadow-director carve-out, statements in lieu of prospectus, deemed debentures, "affairs", single-director rules, memorandum and articles become the constitution |
| s 5, 5A, 5B | subsidiary, holding company, ultimate holding company, wholly owned subsidiary |
| s 6 | related corporations |
| s 7 | interests in shares |
| s 7A | the solvency statement, its form, and the offence |
| s 10 | who may be a company's auditor, and who is appointed when an entity is |

**Not encoded:** the other 62 or so defined terms in s 4(1); incorporation, share
capital, directors' duties, meetings, accounts, charges, and the offences; ss 8 to
8H (administration and inspection); and winding up, which now lives in the
Insolvency, Restructuring and Dissolution Act 2018. **ss 9 and 11 are repealed**
(Act 40 of 2018), so the 15 citations of "section 11" found in other Acts are
citations of those Acts' own s 11.

Cross-references to other Acts are taken as facts supplied: the Securities and
Futures Act 2001, the Accountants Act 2004, the Limited Liability Partnerships
Act 2005, the Insolvency, Restructuring and Dissolution Act 2018 and the
Platform Workers Act 2024.

## How the group provisions are modelled

A group is a **list of direct control links**, each saying whether one named
corporation controls another by the board route or the voting-power route in
s 5(1)(a), with the s 5(3) counting rules carried on each holding. s 5(1)(b)
makes "subsidiary" transitive, which the encoding follows by recursion over the
list, bounded by the number of links so that a cyclic group terminates. **The
list is taken as complete**: a relationship not in it does not exist, which is
what lets s 5A(b), "not itself a subsidiary of any corporation", be decided.

## What the Act turns out to say

### 1. "Wholly owned subsidiary" is not transitive, and a three-tier chain fails it

s 5B: a corporation is a wholly owned subsidiary of another if none of its members
is a person other than (a) that other corporation, (b) its nominee, (c) "**a
subsidiary of that other corporation being a subsidiary none of the members of
which is a person other than that other corporation or a nominee of that other
corporation**", or (d) a nominee of such a subsidiary.

Take the chain **P → S2 → S1 → C**, every share held inside the one group. C has
one member, S1. S1 is a subsidiary of P, but S1's only member is S2, a person
other than P or P's nominee. So S1 fails limb (c) and **C is not a wholly owned
subsidiary of P**, although C is a wholly owned subsidiary of S1, S1 of S2, and S2
of P.

Unlike s 5(1)(b), which carries "subsidiary" up a chain, s 5B contains nothing to
carry "wholly owned" up one. Two tiers work (P → S → C); three do not.

The evident intention was almost certainly otherwise, and the encoding follows the
words and asserts the four-level chain as the case where they part from it. The
same chain is a subsidiary of P under s 5(1)(b), asserted beside it.

### 2. A private company owned by six kinds of body is still an "exempt private company"

s 4(1): an exempt private company is a private company "in the shares of which **no
beneficial interest is held directly or indirectly by any corporation**" with not
more than 20 members.

"Corporation" has six exclusions: a Minister-declared public authority, a
corporation sole, a cooperative society, a registered trade union, a platform work
association and a limited liability partnership. So a private company wholly owned
by **any of them** still qualifies, provided it has no more than 20 members.
Asserted for each.

The other direction is stranger. **"Foreign company" limb (b) takes in an
unincorporated foreign association that can sue through its secretary**, and
"corporation" includes any foreign company. So such an association *is* a
"corporation" for the whole Act although it is not a body corporate, and a private
company it owns beneficially is **not** exempt. Asserted.

### 3. A foreign cooperative society is both in and out of "corporation"

"Foreign company" limb (a) includes any "society" incorporated outside Singapore.
"Corporation" "includes any foreign company but **does not include** … (c) any
cooperative society" — unqualified as to where the society was formed. A foreign
cooperative society is therefore included (as a foreign company) and excluded (as
a cooperative society).

The words "but does not include" give the exclusion the last word, and the
encoding reads it that way. The Act does not say which prevails. Of the six
exclusions only (a), the Minister's declaration, is expressly confined to bodies
"incorporated in Singapore"; exclusion (e) means a limited liability partnership
under the 2005 Act, so one formed abroad is not excluded. Asserted.

### 4. Section 5(3)(b)(ii) is circular

s 5(3)(b)(ii) counts shares held by "a subsidiary of that other corporation" as the
parent's own. Whether a corporation is a subsidiary of the parent is the very
question s 5(1) is answering. So deciding whether C is a subsidiary of P can depend
on whether S is a subsidiary of P, which can depend on whether C is. The Act gives
no order of determination.

The encoding avoids the loop by taking the holder's status as a supplied fact (the
holder kind on each holding). That is a way round the problem and not a solution to
it.

### 5. Cousins at different depths are "related", but two parents of a joint venture are not

s 6(c): two corporations are related where one "is a subsidiary of the holding
company of" the other. "Holding company" is transitive by s 5(4). So any two
corporations that share a holding company **anywhere above them** are related: an
uncle and his nephew, cousins at different depths of the one group. Asserted.

And a **50:50 joint venture** has no holding company at all, since "more than half"
excludes exactly 50%. Neither parent is a holding company, and the two parents are
not related to each other. Where both parents control the board of the venture they
are both its holding companies — so the venture has **two ultimate holding
companies** — and still not related to each other, because s 6(c) relates two
*subsidiaries* of a common holding company and neither parent is a subsidiary.
All asserted.

### 6. The 20% rule in section 7 is applied tier by tier, so a 0.8% stake is an interest

s 7(4A): where a body corporate has an interest in a share and a person (alone or
with associates) is entitled to exercise or control not less than 20% of the voting
power in that body corporate, the person is deemed to have an interest in the
share. s 7(4A) itself counts a *deemed* interest as the base ("has, or is by the
provisions of this section (apart from this subsection) deemed to have").

Each step is tested against the voting power in the **immediate** body corporate
only. So a person holding 20% of A, which holds 20% of B, which holds 20% of C,
which holds the shares, is deemed to have an interest in them, although their
economic stake is 0.8%. The threshold is not compounded. Asserted at three tiers
and with each tier in turn made 19.9%, which breaks the chain.

"Not less than 20%": exactly 20 is in, 19.9 is out. Asserted.

### 7. Section 244 gets only the book-entry rule from section 7

s 7(1): the section has effect for Division 4 of Part 4 and ss 163 to 165, "and
subsection (6A), in addition, also has effect for the purposes of section 244". So
for s 244 the only part of s 7 that applies is the rule that a book-entry security is
treated as an interest in a share; the deeming rules, the 20% rule and the
disregards do not. Asserted.

### 8. The solvency statement is harder to give for a small company

s 7A(2): a company **exempt from audit** must give its solvency statement as a
written declaration signed by **every director**. A company that is **not** exempt
may do that **or** attach an auditor's report that the statement is not
unreasonable. With two of three directors signing and an auditor's report, the
audited company is in and the audit-exempt one is out. The company with the least
machinery has fewer ways to comply. Asserted as that pair.

The wording of (b) also leaves open whether, on the auditor's-report route, anyone
must still sign a declaration. The encoding reads the report as a substitute for
unanimity, the only reading under which it is an alternative.

**The offence turns on the grounds when the statement was made.** s 7A(6): a
director who makes a solvency statement "without having reasonable grounds" is liable
to a fine of up to $100,000 or three years or both. Later insolvency is not an
element: a director with good grounds is not convicted because the company failed,
and a director with none is not acquitted because it survived. Asserted both ways.

### 9. Section 10(5) and (6) treat later joiners differently, and omit accounting LLPs

s 10(5): when an **accounting firm** is appointed in its own name, the appointment
operates as if "the partners of the firm **at the time of the appointment**, who are
public accountants **at that time**," are appointed. A partner admitted later is not
an auditor, and neither is a partner who qualifies as a public accountant later.

s 10(6): when an **accounting corporation** is appointed, the appointment operates
as if its directors and employees practising as public accountants are appointed,
"**whether directors at the time … or later**" and "whether employed at the time … or
later".

So someone who joins the **corporation** after the appointment is an auditor of the
company, and someone who joins the **firm** is not. Asserted as that pair.

**And there is a gap.** s 4(1) makes an *accounting limited liability partnership*
an accounting entity, and s 10(4)(b) treats it like a firm for consent. But neither
s 10(5) nor s 10(6) mentions it. If one is appointed in its own name, no provision
says which individuals are appointed. Asserted as
`NOT section 10 says who is appointed when …`.

### 10. Smaller things worth recording

**s 4(1) "company limited by guarantee" and its siblings, "listed", and
"constitution" are plain.** The one that matters is `4(13)`: a reference in any
written law **or in any contract** to the memorandum or articles is deemed to refer
to the constitution from 3 January 2016.

**"Includes" in s 4(8).** The list of what the "affairs of a corporation" covers is
introduced by "includes" and so is not exhaustive. Absence from the list shows
nothing. And the definition applies only to eight named provisions; elsewhere the
word has its ordinary meaning. Asserted.

**The promissory-note carve-out needs both limbs.** s 4(1) "debenture" excludes a
note of face value not less than $100,000 *and* maturity not more than 12 months.
$100,000 over 12 months is out; $99,999 over 12 months and $100,000 over 13 months
are both debentures. Asserted at each edge.

**A professional adviser is not a shadow director — "by reason only".** s 4(2)
protects advice given in a professional capacity, but only where that is the sole
reason the directors follow it. An adviser who also directs in practice beyond
advice is a director. Asserted.

**s 5(5) and the Depository.** The Depository is not a holding company "by reason
only of the shares it holds … as a bare trustee". Asserted.

## What was read into the text, and should be checked

- **Board control of "a majority".** s 5(2) deems the parent to have the *power to
  appoint* where (a) a person cannot be appointed without the parent exercising a
  power in their favour, or (b) their appointment follows necessarily from being the
  parent's director or officer. The control test is "all or a majority" and those
  limbs speak of "a person". The encoding reads them as applying to a majority of
  the directors, the only reading under which they bear on the test. A single
  nominee would not make a parent.
- **Foreign cooperative society:** exclusion prevails (finding 3).
- **A disregarded interest under s 7(9) passes nothing up** under s 7(4) and (4A).
  The Act does not address the point; the natural reading of "to be disregarded"
  was taken.
- **"Controlling interest"** in s 7(4)(b) is not defined in s 7 and is a supplied
  fact.

## What would need doing before this is worth anything

- **No case law was searched.** Findings 1, 3, 4 and 9 are readings of the words;
  the Companies Act is the most-litigated statute in the corpus and several of
  these points may have been decided.
- **The other 1.29 million characters.** A user asking whether directors owe a duty,
  how a meeting is called, or what a charge needs is outside this row entirely.
- The cross-referenced Acts are not followed, in particular the Securities and
  Futures Act 2001 ss 2 and 283 (collective investment schemes) and the Accountants
  Act 2004 (who is a public accountant and what an accounting entity is).
- The group model requires the full list of control links, which a real corporate
  group's register would have to supply; the encoding cannot discover them.
- No regulations were retrieved, including those that prescribe offices disregarded
  under s 7(9)(c), the regulations under s 4(1) "debenture", and the prescribed
  entity under s 4(5).

## Source refreshed after encoding (10 Oct 2026)

This row was encoded against the deposit as it stood before the source refresh: the SSO consolidation current at the
earlier retrieval, still in git at commit da331074. The deposit has since been replaced by the consolidation current as at
9 October 2026, whose text differs. **The row has not been re-checked against the refreshed text.** Its assertions do not
read the source, so they still pass; whether the encoded provisions changed is an open question.
