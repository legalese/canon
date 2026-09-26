# Penal Code 1871 — verification register, pass 7

**Run date:** 2026-09-15
**Scope:** the 204 sections added on 15 Sep 2026, which are every live section of the Code
that had none — the whole of Chapters 6 (ss 121 to 130A), 6A (ss 130B, 130C), 6B (ss 130D,
130E), 7 (ss 131 to 140B), 8 (ss 141 to 158), 9 (ss 161 to 171), 10 (ss 172 to 190),
11 (ss 191 to 229), 12 (ss 255 to 263), 14 (ss 267A to 294) and 15 (ss 298, 298A); the nine
remaining sections of Chapter 5 (ss 109, 110, 112, 115 to 120); ss 501, 502 and 507; and the
24 standalone punishment sections the earlier passes had left out by policy (ss 302, 304,
311, 323, 325, 341, 342, 363, 363A, 379, 379A, 384, 392, 395, 406, 417, 419, 426, 447, 448,
458A, 465, 500, 512). With this pass every live section of the Act but the seven that state
no test (ss 1, 7, 8, 9, 49, 50, 79A) has a rule.
**Method:** every rule read back against the deposited source text in
`registers/source-bundle/PC1871.txt`, clause by clause, after it was written and
machine-checked. Same method as passes 1 to 6. Not an adversarial review.

**Result: 5 defects found in read-back, all fixed before the machine check; 9 traps in the
Act's drafting recorded; 1 policy change recorded; 1 observation on the toolchain recorded.**

---

## 1. What this pass covers, and the limit of it

The same limit as passes 3 to 6, and heavier here than in any of them: 204 sections were
written and read back on one day, so **a misreading shared by the rule and the read-back is
invisible**. The five defects in §2 are the ones the read-back caught; the number caught is
some evidence the read-back was real, and no evidence that it caught everything.

This pass is richer in outcome-stating Illustrations than any since pass 4, and 31 of them
are fixtures. The ones that decide something a constructed pair could not:

| Illustration | what it tests | fixture |
| --- | --- | --- |
| s 109 Ill (a) / s 116 Ill (a) | the same bribe, accepted and refused, splits ss 109 and 116 | `instigating a bribe that is accepted`, `instigating a bribe that is refused` |
| s 111 Ill (b) with s 112 Ill | the abettor is liable for a distinct offence he knew was likely | `instigating resistance to a distress that causes grievous hurt` |
| s 118 Ill | a false report to the police is concealment by representation | `misdirecting the police from a gang-robbery` |
| s 121 Ill | joining an insurrection is waging war | `joining an insurrection` |
| s 130 Explanation | a parolee beyond his limits has escaped | `feeding a parolee who has overstepped his limits` |
| s 144 Ill | a sharpened pole is a thing likely to cause death | `joining the crowd with a sharpened pole` |
| s 161 Ill (a) | a job for the judge's brother is a gratification | `a judge taking a job for his brother as a reward` |
| s 163 Ill | an advocate's fee is not personal influence | `an advocate taking a fee to argue before a judge` |
| s 164 Ill | the public servant abetting his wife's taking | `an official abetting his wife taking a present to sway him` |
| s 165 Ill (a) | renting below market from a litigant | `a judge renting cheap from a litigant` |
| s 174 Ill (b) | a witness ignoring a Magistrate's summons | `a witness who skips a Magistrate summons` |
| s 177 Ill | the landholder's snake bite | `a landholder blaming a murder on a snake` |
| s 182 Ill (b) | a false tip of contraband to get a search | `a false tip of contraband to get a rival searched` |
| s 186 Ill | the paramedics and the broken lift | `telling paramedics the lift is broken as a prank` |
| s 188 Ill | the procession down the banned street | `marching a procession down a banned street` |
| s 191 Ill (a), (c) | a false oath; a true statement of a wrong belief | `swearing falsely to an admission at trial`, `a good-faith but wrong opinion on handwriting` |
| s 192 Ill (a) | jewels planted in a box | `planting jewels in a box to frame the owner` |
| s 195 Ill | perjury to convict of gang-robbery | `perjury to convict of gang-robbery` |
| s 201 Ill | hiding the body | `helping a murderer hide the body` |
| s 204A Expl 1, 2 | the perjury warning; fleeing a sentence | `warning a witness that perjury is a crime`, `fleeing Singapore to dodge a sentence` |
| s 208 Ill | the collusive judgment | `letting a collusive judgment pass to share the proceeds` |
| s 212 Ill (b), (c) | the spouse who shelters, with and without the intent to screen | `a spouse sheltering a house-breaker as usual`, `a spouse sheltering a gang-robber to dodge the police` |
| s 255 Expl | one denomination made to look like another | `doctoring a two dollar stamp into a twenty` |
| s 512 Ill | the attempted kidnapping to murder | `an attempted kidnapping to murder` (in `punishment-provisions.l4`) |

The other 257 new assertions are constructed pairs of the kind passes 4 to 6 used.

## 2. Five defects found in read-back, and fixed

### D1 — section 149 was built on section 141, not on section 142

s 149 makes "every person who, at the time of the committing of that offence, is a member
of the same assembly" guilty of the offence committed in prosecution of the common object.
The first draft conjoined the s 141 unlawful-assembly test and a timing fact, and left out
s 142 — so a person unaware of the facts making the assembly unlawful, who had not
intentionally joined it, was caught. "Member" is a defined term (s 142) and the rule now
conjoins `the person is a member of an unlawful assembly`. The fixture `a bystander present
when a member commits arson` is the regression test.

### D2 — section 177 borrowed section 176's duty

s 176 is "legally bound to give any notice or to furnish information"; s 177 is "legally
bound to furnish information". The first draft used one fact for both, so a person bound
only to give a notice who volunteered false information satisfied s 177. Two facts now.

### D3 — section 263 lost the revenue stamp when it lost the stamp certificate

s 255(2) extends "stamp" to a stamp certificate under the Stamp Duties Act 1929 "in this
section and sections 256 to 262" — not s 263. The first draft carried the definition in one
fact whose name included the extension, and, to keep the extension out of s 263, dropped
the fact from s 263 altogether. That removed the requirement that the stamp be a Government
revenue stamp at all. The revenue stamp and the certificate are now two facts, gathered by
one rule for ss 255 to 262; s 263 tests the revenue stamp alone. The fixture `rubbing out
the cancellation mark on a stamp certificate` is the regression test.

### D4 — "fraudulently" in sections 206 to 210 was written into the conduct

Pass 6 §N20 settled that "fraudulently" and "dishonestly" are the s 25 and s 24 terms and
come from the `Fault` record (ss 471, 489F), while "with intent to defraud" (s 477A) is not
the s 25 term and stays in the fact. The first draft of ss 206, 207, 208 and 210 wrote
"fraudulently" into each conduct fact, which is the s 477A treatment applied to the s 471
word. The four rules now take a `Fault` and conjoin `the act is done fraudulently`, and
the wrappers pass the proposed act's fault. Chapter 12's ss 261 to 263 had the right
treatment from the start.

### D5 — the fraction constructor made a fine available the offence did not provide

ss 119 and 120 punish with "one-half [or one-fourth, or one-eighth] of the longest term
provided for that offence, or with such fine as is provided for that offence, or with
both". The first draft of `a fraction of the longest term provided for the offence with its
fine` set `fine is available` TRUE unconditionally. It now carries the offence's own
availability, as it already carried the offence's maximum fine.

## 3. Nine traps in the drafting

### N23 — section 154 conjoins three omissions, and is read as written

The owner or occupier "shall be punishable with fine ... if he or his agent or manager,
knowing that such offence is being or has been committed, or having reason to believe it is
likely to be committed, do not give the earliest notice thereof ... to the principal officer
at the nearest police station, **and** do not, in the case of his or their having reason to
believe that it is about to be committed, use all lawful means ... to prevent it, **and** in
the event of its taking place, do not use all lawful means ... to disperse or suppress".
Read literally the three omissions are cumulative: a landowner who gave notice but did
nothing else is outside the section. The rule reads it literally, and `a landowner who
calls the police about a riot on his land` is the fixture that shows it. A court might read
the "and"s distributively; `NOTES.md` §3 records the choice. ss 155 and 156 have one duty
each and raise no such question.

### N24 — section 151 overlaps section 145, and its Explanation routes punishment only

s 151 (an assembly of 5 or more likely to disturb the peace, commanded to disperse) has no
s 141 common object; s 145 (an unlawful assembly commanded to disperse) does. The s 151
Explanation says that where the assembly is unlawful within s 141 "the offender will be
punishable under section 145". That is a direction about which punishment applies; it does
not narrow s 151's elements. So a s 145 case satisfies s 151 as well, and the encoding does
not negate s 141 inside s 151. Neither punishment is computed, so nothing turns on the
routing here; a reader who later computes them should apply it there.

### N25 — "harbour" is defined three times, and each definition is a rule

ss 130A, 140A and 216B define "harbour" in identical words for Chapter 6, Chapter 7 and
ss 212, 216 and 216A respectively: it "includes the supplying a person with shelter, food,
drink, money, clothes, arms, ammunition, or means of conveyance, or the assisting a person
in any way to evade apprehension". Each is encoded as a rule disjoining the harbouring fact
with the supply fact, so the supply route reaches every harbouring limb. D3's lesson
applies here in reverse: because the definitions are rules and not field names, s 216A --
which s 216B does name -- gets the supply route, and s 157 (harbouring persons hired for an
unlawful assembly), which no definition names, does not.

### N26 — section 139 is a saving, and bites in the wrapper

"No person who is subject to such provision shall be subject to punishment under this Code
for the offence defined in this Chapter." It does not say the act is not an offence; it says
the person is not punishable under the Code for it. The section tests therefore ignore it
and the Chapter 7 wrapper conjoins its negation, so an agent asking the section question
gets the Code's answer and an agent asking the screen gets the saving. `a soldier urging
mutiny under service law` is the fixture, and it satisfies s 131 and fails the wrapper.

### N27 — section 286 is a presumption, and is encoded, where sections 372 and 373 were not

Pass 4 left the ss 372 and 373 presumptions unencoded as "rebuttable presumptions of fact,
not elements". s 286 is also a rebuttable presumption -- one who drops a cigarette where a
fire occurs within 60 minutes "is, until the contrary is proved, presumed to have
substantially contributed to the risk". It is encoded, as a route into s 285's contribution
element with `the contrary of the section 286 presumption is proved` as a negated conjunct.
The difference is that s 286 is a whole section, and this pass's brief was every section;
the pass 4 presumptions are sub-provisions of sections that are encoded on their elements.
The inconsistency is recorded rather than resolved.

### N28 — the consequence ladders of sections 284 to 289 are shared, and section 288 is two rungs short

ss 284, 285, 287, 288 and 289 each list consequences from "likely to cause hurt" up to
death, and punish each rung separately. The rung facts are shared across the five sections
and each section disjoins the rungs it lists. s 288 lists only two -- endangering life, and
death -- so a demolition that merely bruises a passer-by is outside it, though it would be
inside s 284 or s 287. `demolishing a wall with no hoarding and a passer-by is bruised` is
the fixture. s 285 alone has the property-damage rung, and s 289 alone has "likely to cause
grievous hurt".

### N29 — section 292(3) and the section 292 Exception have different reach

s 292(3) deems an object not obscene where the dealing is authorised by written law, "for
the purposes of this section and sections 292B and 293". The Exception takes religious
books and temple representations out of "this section and section 292B" -- not s 293. So the
obscene-object rule carries the s 292(3) negation, and the Exception is a separate negated
conjunct on ss 292, 292(1C) and 292B only. A religious drawing sold to a person below 21 is
within s 293.

### N30 — section 225A's fault is the punishment split

s 225A punishes the residual omission to apprehend "(a) if he does so intentionally" and
"(b) if he does so negligently". The offence clause itself has no fault word. A public
servant whose omission was neither intentional nor negligent is not within either paragraph,
so the encoding conjoins one fact, `intentionally or negligently omits ...`, as an element.
That is a reading; the alternative, that the omission alone is the offence and the
paragraphs merely grade it, would leave an inadvertent omission with no punishment.

### N31 — section 109 says "by this Code"; sections 115 and 116 say "or by any other written law"

s 109's carve-out is "no express provision is made by this Code for the punishment of such
abetment"; ss 115 and 116 add "or by any other written law". One fact carries the carve-out
for all three, worded in the wider ss 115/116 form. A s 109 case where another written law
provides for the abetment's punishment is therefore excluded from s 109 here, where the
Code's words would not exclude it. The difference is recorded; no fixture turns on it.

## 4. One policy change, recorded

### P1 — the standalone punishment sections are encoded

Every earlier pass excluded the sections whose whole content is a punishment -- s 302 for
murder, s 379 for theft, s 465 for forgery and the rest -- on the policy that this subject
does not compute sentence. This pass encodes them, in `punishment-provisions.l4` and in
the chapter modules for the new chapters (ss 130E, 143, 147, 193, 267B, 290, and ss 109,
110, 115 to 120), as `Punishment` values in the Chapter 3 vocabulary.

The policy that no sentence is computed stands: a `Punishment` is the ceiling and, where
the Code fixes one, the floor that a section makes available, and that is all these rules
return. What changed is that the sections themselves are now law with a rule, and the
three that carry a test (s 302 on the s 300 limb, s 304 on the s 299 intention, s 512 on
the offence attempted) decide it. The wrappers still return no punishment, and the screen
carries none. `NOTES.md` §2 records the change.

## 5. One observation on the toolchain, recorded

### T7 — the run cost returned, and with it the memory

Pass 6 §T6 recorded `l4 run agent-cases.l4` at about one minute and left open whether pass
5's 35-minute run was the anomaly or the rule. This pass answers it: with the `Proposed
Act` record grown from 31 nested records to 45 and the fixture file from 7,163 lines to
17,000, the first full run was killed after 40 minutes at 5 GB resident, having starved a
concurrent `l4 check` of memory (`getMBlocks: VirtualAlloc MEM_COMMIT failed`). The 288
section-level assertions of this pass, run alone in a temporary module without the
`Proposed Act` fixtures, completed in 41 seconds. The cost is in the proposed-act bundle,
not in the rules. `report/machine-evaluation.md` §14 records the run that was finally
accepted and how long it took.

## 6. Clause-by-clause read-back

### Chapter 5, sections 109 to 120

| s | provision | reading |
| --- | --- | --- |
| 109 | punishment where the act abetted is committed | s 108 abetment, committed in consequence (Explanation wording), no express provision (N31). Returns the caller's punishment for the offence. |
| 110 | different intention from the abettor's | s 108 abetment and the different intention or knowledge. Returns the caller's punishment for the offence the abettor's intention would have made. |
| 112 | cumulative punishment | s 111 liability, plus the s 111 act being additional to the act abetted and a distinct offence. Boolean. |
| 115, 116 | offence not committed | Each: s 108 abetment, the offence's gravity, **not** committed in consequence, no express provision. s 115 is 20 years with fine or caning; s 116 is the offence's punishment with its minimums stripped (s 116(2)), via `with no minimum sentence`. |
| 117 | abetting the public or more than 10 | s 108 abetment and the fact. 5 years or fine or both. |
| 118 to 120 | concealing a design | One shared test (the facilitating intent or knowledge, and the concealment or false representation), plus the offence's gravity or the public servant's duty. Punishments: fixed terms (s 118), fractions with the offence's fine (ss 119, 120; D5), and fixed terms for a capital or life offence in s 119. |

### Chapters 6, 6A and 6B

| s | provision | reading |
| --- | --- | --- |
| 121, 125 | waging war | One fact each, carrying the attempt and the abetment as the sections do. |
| 121A, 121B, 121C | plans against the President and authority; abetting them | One fact each. The plan is the offence. |
| 121D | omission to inform | Knowledge or reason to believe, and the intentional omission of information one is legally bound to give. |
| 122, 123, 124 | preparing; concealing; assaulting or overawing | Each conduct plus its intention. s 124's attempts are inside its conduct fact. |
| 126, 127 | depredation; receiving | One fact each. Forfeiture is punishment. |
| 128, 129 | the custodian | Public servant with custody, then voluntary allowing or negligent suffering. |
| 130 | aiding, rescuing, harbouring, resisting recapture | Three limbs disjoined; the harbouring limb conjoins the s 130A rule and the Explanation's escape rule (parole beyond limits). |
| 130A | harbour | A rule (N25). |
| 130B | piracy by the law of nations | Caller-asserted. s 130B(2) is a boolean on the aggravation, not a punishment. |
| 130C | piratical acts | Four limbs disjoined. "In or out of Singapore" needs no fact. |
| 130D | genocide | The intent, and one of five acts. |
| 130E | punishment | Death if the act is killing; else life or 20 years. Computed from the s 130D(a) fact. |

### Chapter 7

| s | provision | reading |
| --- | --- | --- |
| 140B | the person concerned | SAF or visiting force, or (s 140B) the police and its attached forces; one rule conjoined by every section that names the officer or serviceman. |
| 131 to 135, 138 | abetments | Each a fact on the record, not the s 107 record (the section names what is abetted). ss 132, 134 and 138 add the consequence. |
| 136 | harbouring a deserter | Knowledge or reason to believe, the s 140A harbouring rule, and the intention to prevent apprehension. |
| 137 | the master | No knowledge: "though ignorant of such concealment". The neglect or want of discipline is the element. |
| 139 | saving | A negated conjunct on the wrapper (N26). |
| 140 | the dress of a serviceman | Not a serviceman; the garb or token; the intention. |

### Chapter 8

| s | provision | reading |
| --- | --- | --- |
| 141 | unlawful assembly | 5 or more, and one of five objects. The Explanation adds no limb. |
| 142 | member | s 141, awareness of the facts, intentional joining or continuing. |
| 143, 147 | punishments | Computed. |
| 144, 148 | armed | s 142 or s 146, plus the shared armed fact (Illustration: the sharpened pole). |
| 145, 151 | commanded to disperse | s 145 on s 141; s 151 on its own two facts (N24). |
| 146 | rioting | s 142 member, and force or violence by the assembly or any member in prosecution of the object. |
| 149 | constructive guilt | s 142 member (D1), the offence, the timing. |
| 150, 157, 158 | hiring, harbouring the hired, being hired | One or two facts each. s 158's armed limb is punishment. |
| 152, 153 | obstructing suppression; provocation | s 153 needs the illegal act, the provocation and the intent or knowledge; whether rioting follows is punishment. |
| 154 | owner or occupier | Read as written (N23). |
| 155, 156 | beneficiary; agent | Same riot fact, different person, the reason to believe, the omission. |

### Chapter 9

| s | provision | reading |
| --- | --- | --- |
| 161 | gratification for an official act | Is or expects to be a public servant; the taking; other than legal remuneration; the motive or reward. The Explanations are in the fact wording. |
| 162, 163 | to influence a public servant | The taking, and the motive or reward for inducing by corrupt or illegal means, or by personal influence. No public-servant element. |
| 164 | abetment by the public servant concerned | Public servant, in respect of whom, abets. |
| 165 | valuable thing | Public servant, the taking without adequate consideration, from a person concerned or interested or related. |
| 166, 167 | disobeying the law; framing a document | Public servant, the conduct, the intent or knowledge as to injury. |
| 168, 169 | trade; property | Public servant, the legal bar, the conduct. Confiscation is punishment. |
| 170, 171 | personation; garb | s 170 needs the act under colour of office; s 171 the intention or knowledge as to belief. |

### Chapter 10

| s | provision | reading |
| --- | --- | --- |
| 172 | absconding | One fact. The court tier is punishment. |
| 173 | preventing service | Three limbs disjoined. The individual split and court tier are punishment. |
| 174, 175, 176, 179, 187 | duties: to attend, produce, notify, answer, assist | Each a duty fact and an intentional omission or refusal. s 187(2)'s demand is punishment. |
| 177 | false information | Its own duty fact (D2), and the false furnishing. |
| 178, 180 | refusing an oath; a signature | One fact each. |
| 181 | false statement on oath | The oath, and the statement known or believed false or not believed true. |
| 182 | false information to move a public servant | The false information, and the intent or knowledge as to its effect. |
| 183, 184, 185 | property by lawful authority | One fact each; s 185 two limbs. |
| 186 | obstruction | One fact, carrying s 186(2)'s width. |
| 188 | disobedience to an order | Knowledge of the order, disobedience, and one of the two harm tiers. No intent, per the Explanation. |
| 189, 190 | threats | Each the threat and the purpose. |

### Chapter 11

| s | provision | reading |
| --- | --- | --- |
| 191 | giving false evidence | The binding, and the false statement known or believed so or not believed true. Explanations 1 and 2 in the wording. |
| 192 | fabricating | The act, the intention that it appear in evidence, the intention that it mislead on a material point. |
| 193 | punishment, and the offence | The offence is s 191 or s 192, intentionally. The punishment splits on the judicial-proceeding fact, whose wording carries Explanations 1 to 3. |
| 194, 195 | to procure a conviction | s 191 or s 192, plus the intent or knowledge as to the conviction. The execution (s 194) and the life split (s 195(2)) are punishment. |
| 196 to 200 | using false evidence; certificates; declarations | One or two facts each; none builds on s 191. |
| 201, 202, 203 | screening; omitting; false information | Shared knowledge fact. s 201 adds the screening intent and one of two acts; s 203 is the false information without the intent. |
| 204, 204A, 204B | destroying a document; perverting justice; bribing witnesses | s 204A: the tendency (with Explanation 2 as a second route), the knowledge or intent, and Explanation 1 negated. s 204B: four limbs. |
| 205 | personation in a suit | Two facts. |
| 206 to 210 | fraud on forfeiture and decrees | `Fault` for "fraudulently" (D4); ss 206 and 207 share the intention. |
| 211 | false charge | Intent to injure, the proceeding or charge, knowledge of no ground. The 7-year tier is punishment. |
| 212, 216, 216A | harbouring | Each the s 216B rule (N25), with its own knowledge and intention. |
| 213, 214 | screening for a gift | Each the taking or giving, the consideration, and the compounding Exception negated. |
| 215 | recovery of stolen property | The taking, and the proviso negated. |
| 217 to 223 | public servants | Each the public-servant fact, the duty or charge, the conduct, the intent where the section has one. |
| 224, 225, 225B | resistance, escape, rescue | One fact each; s 225B carries its residual character. |
| 225A | residual omission | Public servant, the residual duty, the intentional-or-negligent omission (N30). |
| 225C | no special punishment | The prohibited act or enjoined omission, and the absence of a special punishment. |
| 228, 229 | insult; assessor | One fact; two limbs. |

### Chapter 12

| s | provision | reading |
| --- | --- | --- |
| 255(2) | the stamp | Two facts, one rule for ss 255 to 262 (D3). |
| 255 | counterfeiting | The stamp rule, and the counterfeiting fact or the Explanation's denomination fact. |
| 256 to 260 | instruments, sale, possession, use | The stamp rule and one conduct fact each; s 259 adds the intent. |
| 261 to 263 | reuse | `Fault` s 25 or the intent to cause loss, shared; then the conduct. s 263 tests the revenue stamp alone. |

### Chapter 14

| s | provision | reading |
| --- | --- | --- |
| 267A, 267B | affray; punishment | One fact; computed. |
| 267C | incitement | Two shapes, (1) and (2), each conduct + content + intent or knowledge, disjoined. |
| 268, 290, 291 | public nuisance; punishment; continuance | s 268 on the act or omission and one of two effects; s 290 the residual offence and the graded punishment; s 291 its own two facts. |
| 268A, 268B, 268C | hoaxes | s 268A knowledge of falsity; ss 268B and 268C share the placing and the reasonable-excuse negation and split on intent versus intentional act with knowledge of the real risk. |
| 269, 270 | infection | Shared act fact, split on the fault. |
| 271 to 283 | quarantine, food, drugs, water, air, ways, navigation | One or two facts each. |
| 284 to 289 | rash or negligent conduct | Conduct fact per section and the shared consequence ladder (N28); s 286 as a route into s 285 (N27). |
| 292 | obscene objects | The s 292(2)/(3) object rule, the Exception negated, six limbs (N29). (1A) and (1B) are a boolean aggravation; (1C) its own offence. |
| 292A, 292B, 293, 294 | sex-doll; online location; young person; obscene act | s 292B carries both the object rule and the Exception; s 293 the object rule only. |

### Chapter 15, and sections 501, 502, 507

| s | provision | reading |
| --- | --- | --- |
| 298, 298A | racial feelings; enmity | One fact; two limbs. |
| 501, 502 | printing; selling defamatory matter | One fact each; neither builds on s 499. |
| 507 | anonymous criminal intimidation | s 503 plus the anonymity fact. The added term is punishment. |

### The standalone punishment sections

| s | provision | reading |
| --- | --- | --- |
| 302 | murder | Death if the s 300(a) fact holds; else death or life with caning. |
| 304 | culpable homicide not murder | Life or 20 with fine or caning if either s 299 intention holds; else 15 with fine or caning. |
| 311, 323, 325, 341, 342, 363, 363A, 379, 384, 395, 406, 417, 419, 426, 447, 448, 465, 500 | constants | Each one builder call, read against the section. s 384 needed a new builder (a range with caning liable, no minimum strokes). s 341 and s 447 carry their months as fractions of a year. |
| 379A | motor vehicle | The fact; else s 379. Disqualification is not a s 53 punishment and is not carried. |
| 392 | robbery | The hour fact splits 2-10 with 6 strokes from 3-14 with 12. |
| 458A | subsequent house-breaking | The previous conviction; caning added to the caller's punishment. |
| 512 | attempts | Express provision: nothing. Death or life: 20 with fine or caning. Else the offence's punishment without its minimums (s 512(3)). |

## 7. Machine check

45 modules, **0 type errors**; the assertion count and run cost are in
`report/machine-evaluation.md` §14, which was written after this register.
