# Carriage by Air Act 1988 — encoding notes

Status `draft`. **No domain expert has read this against the source.** An independent test pass was run on 2026-09-30 (section 6).

## 1. What is encoded and what is not

The whole Act as printed in Singapore Statutes Online's PDF, "Current version as at 30 Sep 2026": ss 1 to 13 and the three Schedules, which set out the Warsaw Convention in three texts that s 3 gives the force of law:

| Schedule | text | encoded as the `Convention` input |
| --- | --- | --- |
| Second | the original Warsaw Convention (1929) | `the Warsaw Convention` |
| First | the Warsaw Convention as amended by the Hague Protocol (1955) | `the Warsaw (Hague) Convention` |
| Third | the Warsaw (Hague) Convention as amended by Montreal Protocol No. 4 (1975) | `the Warsaw (Hague) (Montreal) Convention` |

**The three texts are three vintages and each is its own answer.** They differ on the limits (Article 22), the complaint periods (Article 26), what a missing or defective document costs the carrier (Articles 3, 4 and 9), the defences (Articles 20, 21, 25), the servants' limits (Article 25A) and the rules on cargo. So the `Convention` is the first input to every rule where they differ. Where a text has no provision on a point the rule is a `REFUSE` that names it, never a figure taken from another text.

One nouns module, `caa-types.l4` (DECLARE only), four rule modules and four test modules:

| module | covers |
| --- | --- |
| `caa-types.l4` | every noun |
| `caa-convention-scope.l4` | Chapters I and II: Articles 1 to 16 and the documents part of Article 34 |
| `caa-convention-liability.l4` | Chapter III: Articles 17 to 30A |
| `caa-convention-final.l4` | Chapters IV and V: Articles 31 to 41, and the Additional Protocol |
| `caa-act.l4` | the Act, ss 1 to 13 |

**Shape.** The Convention is a set of tests over facts a witness could give (was a ticket delivered; did the occurrence take place during the carriage by air) and a set of amounts. Each test is a `BOOLEAN` rule; each limit is a number in francs or Special Drawing Rights. Where a court "may", the rule answers whether the power is available, never whether it will be exercised. Two duties are regulative rules (Articles 12(2), 13(2)), neither with a stated number of days, so neither has a `WITHIN`.

**Not encoded, and why:**

- the conversion of francs and Special Drawing Rights into Singapore dollars. Article 22(5) and (6) give gold and IMF valuation methods; s 6(4) lets the Minister specify equivalents by order. No order is an input, so `the sum in Singapore dollars` is a named `REFUSE`.
- the other Acts the Act points at (Civil Law Act 1909, Contributory Negligence and Personal Injuries Act 1953, Limitation Act 1959). Their answers are facts.
- the Legislative History, Abbreviations and Comparative Table, which are not part of the Act.

## 2. Coverage table

Disposition: `encoded` (a rule in the module named), `inert` (quoted, adds no condition or answer; the reason is given), `refuse` (the source does not answer: a named `REFUSE`). No row is `deferred`. "First", "Second" and "Third" are the Schedules.

### 2.1 The Act

| provision | heading | disposition | where |
| --- | --- | --- | --- |
| 1 | Short title | inert: names the Act | — |
| 2 "court" | Interpretation | encoded | act |
| 2 the five Convention and Protocol definitions | | inert: they name the three Schedules, which are the `Convention` input | types |
| 3(1) | Conventions to have force of law | encoded | act |
| 3(2) | French text prevails | encoded | act |
| 4(1)(a) to (d) | High Contracting Parties | encoded | act |
| 4(1)(e) | Additional Protocol | encoded (fork F1) | act |
| 4(2) | Article 40A(2) | encoded | act |
| 5 | Fatal accidents | encoded | act |
| 6(1) | Limitations of liability | encoded | act |
| 6(2), 6(3) | court's powers | encoded | act |
| 6(4) | Minister's order on equivalents | refuse (no order is an input) | act |
| 6(5) | Article 25A as applied | inert: a rule of construction | — |
| 7 | Notice of partial loss | encoded | act |
| 8(1), 8(4) | Time for bringing proceedings | encoded | act |
| 8(2) | | encoded | act |
| 8(3) | contribution | encoded | act |
| 9 | Contributory negligence | encoded | act |
| 10(1) | Minister's order | input fact | act |
| 10(2) | military aircraft | encoded (fork F9) | act |
| 11(1), 11(2) | Actions against High Contracting Parties | encoded | act |
| 12 | Regulations | refuse | act |
| 13 | Application to Government | encoded | act |

### 2.2 The Convention, article by article

Every article appears in all three Schedules unless the third column says otherwise. "Enc" = encoded. Rule names are in the modules.

| Article | heading | differences between the texts | disposition | where |
| --- | --- | --- | --- | --- |
| 1(1), 1(2) | scope; international carriage | one test in all three (the wording differs: "State" or "Power") | enc | scope |
| 1(3) | successive carriage | none | enc | scope |
| 2(1) | State carriage | Additional Protocol | enc | scope |
| 2(2), 2(3) | postal carriage | Second: international postal Convention; First: mail and postal packages; Third: liable only to the postal administration | enc; Second and First refuse the Third's rule | scope |
| 3(1), 3(2) | Passenger ticket | Second: five particulars, forfeits all limits if accepted without a ticket; First and Third: notice, forfeits Article 22 | enc | scope |
| 4 | Baggage check | Second: eight particulars, forfeits for absence or lack of (d), (f), (h); First and Third: notice, forfeits Article 22(2) | enc | scope |
| 5 | Air waybill; cargo documentation | Second, First: right to require; Third: shall be delivered, other means, refusal not allowed | enc; refuse where a text lacks the rule | scope |
| 6 | Parts and signatures | Second: signs on acceptance; First: before loading; Third: no time | enc | scope |
| 7 | Separate waybills | Third adds separate receipts | enc | scope |
| 8 | Contents | Second: 17 particulars; First: 3 incl. notice; Third: 3 incl. weight | enc | scope |
| 9 | Non-compliance | Second: forfeits limits for lack of (a) to (i), (q); First: Article 22(2); Third: nothing | enc | scope |
| 10 | Consignor's responsibility | Second: any other person; First, Third: a person the carrier is liable to; Third: carrier indemnifies the consignor | enc | scope |
| 11 | Evidence | none | enc | scope |
| 12 | Right of disposition | none | enc | scope |
| 13(1), 13(3) | Consignee | none | enc | scope |
| 13(2) | notice of arrival | none | enc, regulative, no deadline | scope |
| 14 | Enforcement in own name | none | enc | scope |
| 15(1) | Relations of others | none | inert: a saving | — |
| 15(2) | Variation | Third adds the receipt | enc | scope |
| 15(3) | negotiable waybill | First only | enc; refuse for Second and Third | scope |
| 16 | Customs | none | enc | scope |
| 17 | Passenger death or injury | none | enc | liability |
| 18 | Baggage and cargo | Third: cargo strict, four exceptions | enc | liability |
| 19 | Delay | none | enc | liability |
| 20 | Defence | Second: adds negligent pilotage; Third: none for destruction, loss or damage of cargo | enc | liability |
| 21 | Contributory negligence | Third: cargo exoneration mandatory | enc | liability |
| 22(1) to (3) | Limits | see 3.1 | enc | liability |
| 22(2)(b) or (c) | weight of other packages | First and Third only | enc; refuse for Second | liability |
| 22(4) First, Third | costs | Second has no costs rule | enc; refuse for Second | liability |
| 22(4) Second, 22(5), 22(6) | franc, SDR, conversion | definitions | inert; conversion refuses (s 6(4)) | — |
| 23 | Contractual provisions | First and Third add the inherent-defect exception | enc | liability |
| 24 | Exclusivity | Third: cargo limits are maximum limits | enc | liability |
| 25 | Loss of the limits | Second: wilful misconduct; First: intent or recklessness; Third: passengers and baggage only | enc | liability |
| 25A | Servants and agents | First and Third only | enc; refuse for Second | liability |
| 26 | Complaint | see 3.2 | enc | liability |
| 27 | Death of the person liable | none | enc | liability |
| 28 | Jurisdiction | none | enc | liability |
| 29 | Two years | none | enc | liability |
| 30 | Successive carriers | none | enc | liability |
| 30A | Recourse | Third only | inert: a saving | — |
| 31 | Combined carriage | none | enc | final |
| 32 | Clauses infringing | none | enc | final |
| 33 | Refusal; regulations | Third: except Article 5(3) | enc | final |
| 34 | Extraordinary circumstances | Second: whole Convention, and experimental trials; First: Articles 3 to 9; Third: Articles 3 to 8 | enc | scope |
| 35 | Days | none | enc | final |
| 36 | Language and deposit | none | inert: a formality | — |
| 37(1), 37(3) | Ratification | none | inert: duties of the depositary | — |
| 37(2) | Entry into force | none | enc | final |
| 38(1), 38(2) | Accession | none | inert | — |
| 38(3) | Effect of accession | none | enc | final |
| 39(1) | Denunciation | none | inert | — |
| 39(2) | Effect of denunciation | none | enc | final |
| 40 | Territories | none | inert: powers of States | — |
| 40A(1) | "High Contracting Party" | First and Third only | enc; refuse for Second | final |
| 40A(2) | "territory" | First and Third only | inert: a definition | — |
| 41 | New conference; signature | none | inert | — |
| Additional Protocol | Article 2 declaration | none | enc as the `availed` facts | scope |

## 3. Answer tables

### 3.1 The limits of liability, per Schedule (Article 22)

| what | Second (1929) | First (Hague) | Third (Montreal 4) |
| --- | --- | --- | --- |
| each passenger | 125,000 francs | 250,000 francs | 250,000 francs |
| a higher limit | by special contract | by special contract | by special contract |
| registered baggage | 250 francs per kg | 250 francs per kg | 250 francs per kg |
| cargo | 250 francs per kg | 250 francs per kg | **17 SDR per kg** |
| objects the passenger holds | 5,000 francs | 5,000 francs | 5,000 francs |
| declared value | declared sum, unless proved above the actual value | declared sum, unless proved above the actual interest | same |
| weight of other packages | no rule (refuses) | counted where value affected | counted where value affected |
| costs on top of the limit | no rule (refuses) | yes, unless the damages do not exceed a written offer within 6 months of the occurrence or before action | same |
| limits lost | wilful misconduct or equivalent default | intent, or recklessness with knowledge | same, passengers and baggage only |

### 3.2 Complaint periods (Article 26(2))

| complaint | Second | First and Third |
| --- | --- | --- |
| damage to baggage | 3 days from receipt | 7 days |
| damage to cargo | 7 days | 14 days |
| delay | 14 days from being placed at disposal | 21 days |

### 3.3 What a missing or defective document costs the carrier

| document | Second | First | Third |
| --- | --- | --- | --- |
| passenger ticket | absent: every limiting provision | absent, or no notice: Article 22 | same as First |
| baggage check | absent, or lacks ticket number, number and weight, or liability statement: every limiting provision | absent, or no notice (unless combined with a compliant ticket): Article 22(2) | same as First |
| air waybill | absent, or lacks a particular in (a) to (i) or (q): every limiting provision | absent with consent, or no notice: Article 22(2) | nothing (Article 9) |

### 3.4 Every number, period and date

| provision | quantity | value |
| --- | --- | --- |
| Article 13(3) | rights if cargo has not arrived | after 7 days from when it ought to have arrived |
| Article 22(4) | written offer | within 6 months of the occurrence, or before the action if later |
| Article 26(2) | complaint | 3 or 7, 7 or 14, 14 or 21 days (3.2) |
| Article 29(1), s 8(1) | action | 2 years |
| s 8(3) | contribution | 2 years from judgment or award |
| Article 37(2) | entry into force | ninetieth day after the fifth ratification, and after each later deposit |
| Article 38(3) | accession | ninetieth day after notification |
| Article 39(2) | denunciation | six months after notification |

### 3.5 What the Act delegates, and what this encoding does about it

| provision | delegation | treatment |
| --- | --- | --- |
| s 6(4) | Minister's order on equivalents in francs and SDR | `REFUSE` (no order is an input); the limits are in units |
| s 10(1) | Minister's order that s 10 applies to a State | input fact |
| s 12 | regulations extending the Schedules | `REFUSE` |
| Additional Protocol | a State's declaration on Article 2(1) | input fact |
| Article 22(5), (6) | gold and IMF valuation | not encoded; conversion is s 6(4)'s |

## 4. Fork register

Each reading below is a choice where the text survives more than one. None is materialised as a switch: each is resolved at encode time and recorded here.

| id | provision | readings | taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 4(1)(e) | "this Act applies to any such High Contracting Party ... to the extent that it has availed itself of the provisions of the Additional Protocol": literally, only to the extent it has availed itself; or subject to its declaration | the Act does not apply to State-performed carriage where the party has availed itself of the Additional Protocol | the Additional Protocol only lets a party exclude Article 2(1); the literal reading would apply the Act only to parties that had opted out |
| F2 | Article 20(2) (Second) | "in the carriage of cargo and baggage": whether it reaches damage by delay | destruction, loss or damage of baggage or cargo only | the paragraph is about "negligent pilotage or negligence in the handling of the aircraft or in navigation", which causes destruction and damage |
| F3 | Article 22(2) (Second) | the weight to take where part of the baggage or cargo is lost | no rule; refuses when other packages are affected | the Second Schedule has no partial-loss paragraph |
| F4 | Article 26(2) | "forthwith after the discovery ... and, at the latest, within N days": is "forthwith" a condition of the time limit in 26(4) | yes | 26(4) bars an action "failing complaint within the times aforesaid" and the times are those in 26(2) |
| F5 | Article 13(3) | "at the expiration of seven days after the date on which it ought to have arrived" | from the eighth day after that date (the rule is `asserted GREATER THAN ought PLUS 7`, i.e. from ought + 8; the ninth day if the date itself is counted as day 1) | expiration of the seventh day |
| F6 | Article 29(2), s 8 | how the two years are counted | by the anniversary date (`add months`; 29 Feb 2024 + 2 years is 28 Feb 2026) | 29(2) leaves the method to the law of the court seised; the rule takes the ordinary one |
| F7 | Article 25A(3) (First) | the exclusion applies where the damage resulted from the servant's act "done with intent to cause damage or recklessly" | the servant may not avail himself of the limits in that case; the Third confines it to passengers and baggage | the text |
| F8 | Article 34 | First names Articles 3 to 9, Third Articles 3 to 8 | in both, the documentary provisions do not apply to extraordinary carriage | the difference (Article 9) does not change the answer, since Third's Article 9 keeps the limits in any case |
| F9 | s 10(2) | the Warsaw Convention is not mentioned | s 10 does not exclude it | the text names the other two |
| F10 | Article 3(2) (Second) | forfeiture for a defective ticket | only for absence of a ticket | the text says "accepts a passenger without a passenger ticket having been delivered" |
| F11 | Article 9 (Second) | which missing particulars forfeit | (a) to (i) and (q) | the text |
| F12 | Article 4(4) (Second) | forfeiture for baggage that needs no check | none for small personal objects the passenger keeps | Article 4(1) excepts them |
| F13 | Article 21(2) (Third) | "shall be wholly or partly exonerated ... to the extent" | a separate rule: the carrier must be exonerated to the extent of the claimant's fault | "shall", unlike "may" in 21(1) |
| F14 | Article 22(2)(a), (b), (c) (Third) | "[(c)]" is bracketed in the printed text | the weight paragraph applies to baggage and cargo | the paragraph speaks of "registered baggage or cargo" |
| F15 | Article 1(2) | Second says "another Power" and First and Third "another State" | one rule | the same test |

**Where I looked and found no fork**: Articles 5 to 8 (mechanical), 10 to 12 and 14 to 16, 17, 19, 23, 24, 27, 28, 30, 31, 32, 35, and ss 5 to 9, 11 and 13. A reviewer should not treat that as proof there are none.

## 5. What `check.sh` prints, and #TRACE

Run on `l4` from `legalese/prereleases` tag `unstable-20260926-c76e6b0`, 2026-09-30:

```
module                                    errors satisfied  failed
caa-act.l4                                     0         0       0
caa-convention-final.l4                        0         0       0
caa-convention-liability.l4                    0         0       0
caa-convention-scope.l4                        0         0       0
caa-tests-act.l4                               0        68       0
caa-tests-final.l4                             0        32       0
caa-tests-liability.l4                         0       192       0
caa-tests-scope.l4                             0       165       0
caa-types.l4                                   0         0       0
TOTAL (9 modules)                              0       457       0
```

No test is meant to fail. The harness can fail (a scratch file with `#ASSERT 1 EQUALS 2` prints `errors 1, failed 1` and exits 1), so the 0 is not vacuous. The assertions were written from the text of each Article in the Schedule named beside it, on both sides of each threshold, and for every rule that differs between the three texts against each text; **but they were written by the same session that wrote the rules; the independent pass is `tests-independent.l4` (343 assertions, all satisfied; report in `INDEPENDENT-TEST-REPORT.md`).**

`#TRACE` results are printed, not asserted. Read on 2026-09-30: `the carrier's duty to inform the consignor ...` and `the carrier's duty to give the consignee notice ...` each give `FULFILLED` when the carrier acts.

## 6. Open questions, and what has not been done

1. **Independent test pass run, 2026-09-30.** A fresh agent fixed its expected answers from the source, then wrote `tests-independent.l4` (343 assertions, 0 failed); it skimmed some rule bodies, so it was not fully blind. Untested by it: Arts 12, 14, 16, 27, 28, 31, 36, 40, 41, content checks for Arts 6 and 8, Art 29(2) month-end counting (F6), Montreal postal carriage, Art 22(5) and (6) conversion. To settle: the Art 13(3) day count (the agent counts the ninth day; F5 above says the eighth, the rule is `ought PLUS 7`), and that Art 21(2) returns FALSE, not REFUSE, for texts with no such provision.
2. **HG1 (fidelity) has not been sought.** An aviation-law reader should go through 3.1 to 3.3 and forks F1 to F15, particularly F1, F2, F4.
3. **The pipeline has not been run** on this encoding.
4. **The source is an unofficial SSO consolidation** (SOURCE-LICENSE.md); the printed Schedules were not compared with the treaty texts or the authentic French text that s 3(2) makes prevail.
5. **Conversion.** Is there an order under s 6(4)? None is an input.
6. **Does Singapore's court count the two years by the anniversary date** (Article 29(2))? The rule assumes so.
7. **Additional Protocol.** Which High Contracting Parties have declared under it is a question of fact for each case; no list is encoded.
