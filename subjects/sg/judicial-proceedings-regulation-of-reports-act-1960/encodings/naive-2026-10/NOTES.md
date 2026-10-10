# Judicial Proceedings (Regulation of Reports) Act 1960 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all amendments
up to and including 1 December 2021" and came into operation on 31 December 2021. The
Legislative History lists one amending Act, the Criminal Procedure Code 2010 (Act 15 of
2010, in force 2 January 2011); the sections carry no annotations saying what it changed.

**Checks:** one case file, 46 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0051**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. The Act has five
sections, so the whole operative text (ss 2 to 5) is encoded. What "indecent" and
"calculated to injure public morals" mean is left as an input flag for a court to
decide, and so is whether posting online is "publishing".

## What the Act turns out to say

### 1. Anyone can break the law, but only four kinds of person can be convicted

s 2 makes it unlawful to print or publish "or cause or procure" printing or
publishing, so a reporter, or a party who feeds the details to the press, contravenes
it. But the proviso to s 3 says no person "other than the proprietor, editor, printer
or publisher" can be convicted. The reporter and the party commit an unlawful act for
which they cannot be convicted. Asserted.

### 2. Divorce reporting is a closed list of four things

For divorce, dissolution, nullity, judicial separation and restitution of conjugal
rights, s 2(1)(b) bans "any particulars other than" names, addresses and occupations of
parties and witnesses; a concise statement of charges, defences and countercharges "in
support of which evidence has been given"; points of law and their rulings; and the
decision with the court's observations. The evidence itself is out, and so is a charge
on which no evidence was given. Because (i) names only "parties and witnesses", the
name of a child who did not testify, the parties' ages and a photograph are out too
(inference from the list; the text does not mention them). Asserted.

### 3. Even the permitted particulars yield to the indecency rule

s 2(2): nothing in (1)(b) permits "anything contrary to subsection (1)(a)". So indecent
matter calculated to injure public morals may not be published even when it is the
court's own decision or observations. Asserted.

### 4. Outside matrimonial cases, only indecency is restricted

A criminal trial, a civil claim or (inference) a free-standing maintenance or custody
application falls only under s 2(1)(a): the testimony may be reported in full so long
as it is not indecent matter injurious to public morals. Asserted.

### 5. Law reports, medical journals and court-directed notices are outside the Act

s 5 saves documents printed for use in the proceedings or communicated to those
concerned, anything published "in pursuance of the directions of the court", and bona
fide law report series and technical publications for the legal or medical profession.
A medical journal may print indecent physiological details from a case. Note that
s 5(a) speaks of "printing" and "communication" to persons concerned, not publishing to
the world. Asserted.

### 6. The penalty is small and the prosecutor holds the key

$1,000 or one year, or both (s 3), and no prosecution without the Public Prosecutor's
consent (s 4). Asserted.

## What would need doing before this is worth anything

- Whether "publisher" reaches an individual posting on social media, and whether online
  posting is "printing or publishing", needs case law; none was searched.
- The Act still lists restitution of conjugal rights; whether such proceedings remain
  available under current family law was not checked.
- Other reporting restrictions (in family, criminal procedure or children's
  legislation) were not read; they may override or add to this Act.
- What the Criminal Procedure Code 2010 amendment changed is not shown in the deposit.
