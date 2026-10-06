# Protection from Harassment Act 2014 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
17 August 2026. The deposit carries the Act 23 of 2025 amendments with effect
from 29 June 2026, which added "humiliation" to the harm formula in ss 3, 4 and
7, added the online-activity limbs to s 7(3), and inserted s 11A.

**Checks:** `l4 run pha-cases.l4` and `l4 run pha-civil-cases.l4` — 194
assertions satisfied, 0 errors, 0 warnings. **One of those assertions records a
disagreement with the Act's own Illustration**; see finding 4.

## Scope

The Act is about 172,000 characters. This encodes:

- **Part 2 in full** — ss 2 to 10: the five offences (ss 3, 4, 5, 6, 7), the
  three enhanced-penalty provisions (ss 8, 8A, 8B, with s 8C), and the offence
  of breaching an order (s 10).
- **Part 3, Division 1** — ss 11, 11A, 12, 13, 13B and 14: the statutory tort,
  enhanced damages for online activity, the protection order, the expedited
  protection order, the mandatory treatment order, and the abolition of the
  common law tort.

Not encoded: s 9 (community order — a power), **the whole of Part 3 Division 2**
(ss 15 to 16BB — stop publication, correction, disabling and notification orders
and their interim counterparts), ss 16C to 16D, Part 3A (the Protection from
Harassment Court) and Part 4.

Division 2 is roughly half the Act's text and is a different regime: it is about
**false statements of fact**, not about harassment, and it runs on its own
machinery (the subject of a false statement applies; the orders bind authors,
internet intermediaries and administrators). Leaving it out is a deliberate
scoping decision, not an oversight, and nothing here should be read as covering
it.

Every judgment the Act asks a court to make is a fact supplied: whether words
are threatening, abusive, insulting, sexual or indecent; whether a purpose
related to art is one a reasonable person would regard as art; whether conduct
was reasonable; whether a repetition is likely.

## What the Act turns out to say

### 1. The section 3 bystander can be paid but cannot be protected

s 3(1) makes the victim "the target person **or any other person**" caused
harassment, alarm, distress or humiliation. Illustration (c) to s 3 is exactly
that case: X posts Y's photographs and mobile number, Y never sees the posts, and
Y is harassed by strangers who did.

s 11(1) lets "the victim under section 3, 4, 5 or 7" bring civil proceedings,
and takes s 3's own definition of victim.

s 12(9) says that "**for the purposes of this section and section 13**", the
victim of a contravention of s 3 "includes only the person to whom the respondent
intended to cause harassment … and not any other person harassed".

So the bystander has the money remedy and not the forward-looking one. Asserted
as the pair: `a claim lies under section 11` for the bystander, and
`NOT the court may make a protection order` on the same facts. The expedited
order goes the same way, because s 12(9) names s 13 too.

s 12(9) is confined to s 3. A s 4 victim — and s 4's victim is anyone who
perceived the conduct and was likely to be harmed — has both remedies. Asserted.

### 2. The section 6 victim is the orphan of the Act

| | s 3, 4, 5, 7 | **s 6** |
|---|---|---|
| offence | yes | yes |
| protection order (s 12) | yes | **yes** |
| statutory tort (s 11) | yes | **no** |
| vulnerable-person enhancement (s 8A) | yes | **no** |
| intimate-relationship enhancement (s 8B) | yes | **no** |
| subsequent-conviction enhancement (s 8) | yes | yes |

s 11(1) lists ss 3, 4, 5 and 7. s 12(1) lists ss 3, 4, 5, **6** and 7. s 8A(1)
and s 8B(1) list ss 3, 4, 5 and 7 (and s 10 in respect of such a victim).

So a bus driver abused at the wheel can stop it happening again and cannot be
compensated for it under this Act — and s 14(1) has abolished the common law
tort of harassment, so there is no fallback in tort either. A victim of
*identical conduct* who was not at work has the s 11 claim. s 6(1) and s 4(1) use
the same five qualities; the only difference is that the s 6 victim was working.

And a public servant who is also a vulnerable person gets no enhancement at all
on a first conviction, where a victim of the same conduct under s 4 would.
Asserted.

### 3. For sections 3, 5 and 7 the two enhancement routes give the identical ceiling

s 8 sets fixed maxima for a subsequent conviction. s 8A and s 8B let the court
impose "punishment not exceeding **twice** the maximum punishment" otherwise
available — and both say so only "where the enhanced penalty under section 8
does not apply".

For ss 3, 5 and 7 the fixed figures in s 8 are exactly double the first-
conviction figures, so the two routes land in the same place:

| | first conviction | s 8 subsequent | s 8A/8B doubling |
|---|---|---|---|
| s 3 | $5,000 / 6 mths | $10,000 / 12 mths | $10,000 / 12 mths |
| s 5 | $5,000 / 12 mths | $10,000 / 24 mths | $10,000 / 24 mths |
| s 7 | $5,000 / 12 mths | $10,000 / 24 mths | $10,000 / 24 mths |
| **s 4** | **$5,000 / none** | **$10,000 / 6 mths** | **$10,000 / none** |

Asserted as equalities, not as figures, so the point survives a change to the
numbers.

Two consequences:

- **The mutual exclusion in s 8A(1) and s 8B(1) makes no difference to the
  ceiling for ss 3, 5 and 7.** A repeat offender who also targeted a vulnerable
  intimate partner faces exactly the maximum that a first offender against a
  vulnerable person faces. Asserted.
- **s 4 is the exception, and the exception runs the other way.** s 4 is the only
  Part 2 offence with no imprisonment on a first conviction, and a doubling of
  nothing is nothing. So a first-time offender who harasses a vulnerable person
  under s 4 cannot be imprisoned at all, while a repeat offender can be
  imprisoned for 6 months. The vulnerable-person enhancement adds nothing to
  s 4 beyond the fine. Asserted.

s 8C confirms there is at most one doubling: where both s 8A and s 8B apply,
"the punishment … shall not be enhanced by the application of more than one
section". Asserted.

### 4. Illustration (b) to section 3 cannot be derived from section 3

> (b) X writes a letter containing threatening words towards Y intending to send
> the letter to Y to cause him or her alarm. X decides not to send the letter and
> throws it away. Y finds the letter and is alarmed. **X is not guilty of an
> offence under this section as he or she had no reason to believe that the letter
> would be seen by Y.**

Every element of s 3(1) is present on those facts: the intent, the use of
threatening words, and alarm caused to the target as a result. The reason the
Illustration gives — no reason to believe the letter would be seen — appears
nowhere in s 3. It is the s 4(3)(a) defence, and the s 5(3)(a) defence, and the
s 6(4)(a) defence. **s 3 does not have it.** s 3(3) gives only a reasonableness
defence.

The encoding therefore finds a contravention and an offence on the Illustration's
own facts, and the assertion recording that is deliberate:

```
#ASSERT `section 3(1) is contravened` `Illustration 3(b) -- the discarded letter`
#ASSERT `an offence under section 3(2) is committed` `Illustration 3(b) -- the discarded letter`
```

There are three readings and the encoding does not choose between them:

- the Illustration is wrong;
- "as a result causing" in s 3(1) carries an implicit requirement that the
  causal path be one the accused contemplated, which would do the work the
  Illustration attributes to a defence that is not there;
- the conduct of throwing the letter away was "reasonable" within s 3(3), which
  is a strain on the word.

The second is the most likely intended reading. But it is not what the section
says, and the Illustration states a *defence-shaped* reason rather than a
causation-shaped one.

### 5. Doxxing without provable intent contravenes neither section 3 nor section 4

s 3(1) has three conduct limbs, the third being "**publish any identity
information** of the target person or a related person" — and s 3 requires
intent to cause harassment.

s 4(1) has **two** limbs and no third. It requires no intent, but the conduct
must be "threatening, abusive, insulting, sexual or indecent". A home address, a
telephone number, an employer's name — the things s 2(1) defines as identity
information — are none of those. That is precisely why s 3 needed a separate limb
for them.

So publishing someone's address and workplace to a hostile audience, where intent
to harass cannot be proved, falls outside s 3 (no intent) and outside s 4 (no
limb). Asserted as that pair.

What catches it instead is s 5(1A), inserted by Act 17 of 2019, which reaches
the publication of identity information where the publisher intended to cause a
belief in unlawful violence or to facilitate it, **or knew or had reasonable
cause to believe it likely** to do so. Illustration (c) to s 5 is that case: B
posts Y's home address in reply to X's call to hunt Y down.

The fault standard in s 5(1A)(b) sits between the two others in the Act:
knowledge or reasonable cause to believe, which is lower than the intent
s 5(1A)(a) requires and higher than the bare likelihood in s 5(1)(b). Asserted.

So the doxxer is reached when violence is in prospect and not when harassment
alone is.

### 6. What a reasonableness defence answers depends on which section you are in

ss 3(3), 4(3), 5(3) and 6(4) each open "In any proceedings **for an offence**
under subsection (2) … it is a defence for the accused to prove". The
prohibition is in subsection (1); the offence is in subsection (2).

s 7 is drafted differently. s 7(2) — the subsection that says when a person
unlawfully stalks another — opens "**Subject to subsection (7)**". The defences
are therefore built into the definition of unlawful stalking, and so into whether
s 7(1) was contravened at all.

s 4(1A) is a third form again: "An individual or entity **does not contravene**
subsection (1) where …" — a non-contravention, sitting in the same section as the
s 4(3) defences.

s 11(2) asks whether "the respondent **has contravened** that section". Read
literally, the consequence is:

| | answers the prosecution | answers the s 11 claim |
|---|---|---|
| s 4(3)(b) reasonable conduct | yes | **no** |
| s 4(1A) legitimate purpose | yes | yes |
| s 7(7)(a) reasonable course of conduct | yes | yes |

**This is a reading of the words and not a settled proposition.** The contrary
argument is strong: a court may well read "contravened" in s 11(2) as meaning
conduct for which there is no answer, so that the Part 2 defences travel with it.
The encoding states the literal reading, names it as a reading, and asserts the
pairs so the difference between the sections is visible rather than assumed away.

What is not a matter of reading is that the four sections and s 7 are drafted
differently from each other, and that s 4 contains both forms.

### 7. Smaller things worth recording

**s 4(1A) protects the sexual limb and not the rest.** It applies where "the
sexual or indecent words or behaviour … has a legitimate purpose related to
science, medicine, education or art". Material with a genuine educational purpose
that is *also* abusive or insulting is outside it, because the contravention
stands on the other limb; it must fall back on s 4(3)(b). Asserted on
Illustration (d)'s facts and on a variant where the same material is abusive.

**s 5(3)(a) is confined to one limb of one subsection.** The
no-reason-to-believe defence is available only "in respect of a contravention of
**subsection (1)(b)**" — not to an accused who had the intent under (1)(a), which
is coherent, and not to one who published identity information under (1A), which
means the doxxer cannot say they never expected the victim to see the post.
Asserted on both.

**Indecency alone cannot reach s 5.** ss 3, 4 and 6 name five qualities;
s 5(1) names three. Asserted.

**A single occasion is a course of conduct if the accused has a record.**
s 7(10)(a)(ii) makes one non-protracted occasion a course of conduct where "the
accused has a previous conviction under this section in respect of the same
victim". So the threshold turns on the accused's history rather than on the
conduct: identical facts, different answer. Asserted as that pair. s 7(10)(a)(i)
does the same for one protracted occasion — the Act's own Illustration is the
hidden camera watched over several days.

**s 6(2) is a condition, not a defence.** "No offence is committed under this
section unless the accused knows or ought reasonably to know that the victim was
acting in the victim's capacity as a public servant". So the absence of knowledge
means no offence at all, and the burden is not on the accused. Asserted: the
conduct limb is made out and the offence is not.

**s 7(8)'s certificate is conclusive.** A ministerial certificate that an act
falls within the national-security limb of s 7(7)(d) "is conclusive evidence
that the act falls within that paragraph". The encoding establishes the limb from
the certificate alone, and the cases assert it on facts where the underlying
proposition is recorded as false. That is what "conclusive" means.

**The one obligation in a protection order that no prosecution can enforce is
the therapeutic one.** s 10(1) backs orders under ss 12(2), 12(2E), 13(1) and
13(1B) with an offence, "except any provision mentioned in section 12(2B)(c)" —
the referral to counselling or mediation. Asserted.

**The respondent can be excluded from premises they own outright.** s 12(2C)
permits exclusive occupation of a shared residence "whether or not the shared
residence is solely owned or leased by the respondent", and s 12(2D) says the
order "does not affect any title or interest". Asserted as that pair.

**The fastest route to protection cannot reach the cause.** s 13B(1) ties the
mandatory treatment order to a protection order under s 12(2) and to nothing
else. An expedited order under s 13 cannot carry one. That is coherent — the
expedited order is made on prima facie evidence — but it means the respondent
whose conduct is imminent and severe enough to need an expedited order is the one
who cannot be sent for psychiatric assessment at that stage. Asserted.

**s 13 asks for two things s 12 does not**: that the future contravention be
**imminent** rather than merely likely, and that it be "likely to have a
substantial adverse effect on the victim or the victim's day-to-day activities".
Both asserted as independent gates.

**s 12(2A)(b) bridges from violence to this Act.** The court is *deemed*
satisfied that the respondent contravened ss 3 to 7 if it is satisfied that the
respondent voluntarily caused hurt (Penal Code s 321) to the victim. Causing hurt
is not harassment and is not a contravention of any of those sections, but it
produces a protection order under them. Asserted on facts where no contravention
is proved at all.

**s 11 has no measure, no cap and no limitation period of its own.** "Such
damages … as the court may, having regard to all the circumstances of the case,
think just and equitable" is the whole of the guidance. s 11A(3) lets the Minister
cap *enhanced* damages and clarify how the Limitation Act 1959 applies to a claim
for them — which leaves the ordinary claim to the general law and implies, by
contrast, that ordinary damages are uncapped.

**s 11A turns on a letter.** Enhanced damages for online activity require that
the victim "made a reasonable written request … to address the online activity"
and that the respondent "failed, without reasonable excuse, to address" it within
a reasonable time. A victim who goes straight to court gets ordinary damages
only. Asserted. No regulations under s 11A(3)(a) were retrieved, so no maximum
is presently prescribed; recorded as a function so a later change is visible.

## What would need doing before this is worth anything

- **Division 2 of Part 3 is not encoded at all.** Any use of this row for a
  question about a false statement of fact would be a misuse of it.
- **No case law was searched.** The PHA has been litigated — including on the
  meaning of "harassment" and on the availability of orders against foreign
  respondents — and none of that is reflected here. Findings 4 and 6 in
  particular are readings of the words and nothing more.
- No Rules of Court, Family Justice Rules or regulations were retrieved,
  including any under s 11A(3).
- The Schedule's list of specified offences is carried as a single flag rather
  than as the ten Penal Code sections and the Private Security Industry Act
  provision it names. Nothing in the encoding checks which offence a conviction
  was for.
- Part 3A was not encoded, so nothing here says which court an application goes
  to, what it costs, or how long it takes — which for the kind of claimant this
  Act exists for may matter more than anything above.
