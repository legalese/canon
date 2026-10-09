# Police Force Act 2004 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 16
of 2024 and Act 43 of 2024). From Part 12 the arrangement of sections numbers
the provisions differently from the body; the encoding follows the body.

**Checks:** two case files, 135 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**64 of the 527 Singapore Acts** deposited here cite it; the most cited section
is s 64 (17 Acts), which creates Commercial Affairs Officers. Most of the Act's
355,000 characters govern the Force internally: engagement, discipline, the
Special Constabulary, the Auxiliary Police Forces. This row takes the
provisions that reach members of the public.

## What the Act turns out to say

### 1. Not stopping at a police roadblock: seven years. Impersonating a police officer: six months.

s 26(5) and (8)(a): a driver who fails to stop at a barrier when ordered is liable
to $10,000 or **seven years**. s 120A: wearing a police uniform to personate an
officer is $2,500 or **six months**. A pedestrian who walks past a barrier
against a direction is $2,500 or three months. (Personation of a public servant is
also a Penal Code offence, which this row does not read.) Asserted.

### 2. A sign you ought to have seen is an order to stop

s 26(4): a warning sign "constitutes and is to be treated ... as an order ...
addressed by a police officer to any driver ... who **ought reasonably to have
seen** the notice or sign". A driver who did not see it is treated as ordered.
The only defence (s 26(9)) is that more was not reasonably practicable, not that
the sign was missed. The deeming applies to drivers and riders, not to
pedestrians. Asserted.

### 3. Passengers hurt when a driver fails to stop cannot look to the police

s 26(11): no police officer is liable for injury "to the driver or rider **or any
other occupant**" resulting from the driver's failure to obey. Asserted.

### 4. s 25(3) says "warrant card", which saves the wrong document

s 25(1) protects an officer acting in obedience to a **warrant**. s 25(3) then saves
the officer where "the signature on a **warrant card** is not genuine" but was
reasonably believed genuine. A warrant card is the officer's identity card (s 8).
Read literally, (3) covers a forgery on the officer's own card and not a forgery
on the warrant, which is the case the section needs. The encoding follows the
text and asserts both readings' outcomes. It may be a drafting slip; no case law
was searched.

### 5. The police can freeze the bank account of someone who attempted suicide

ss 26A and 26D: where an officer reasonably suspects an attempted or imminent
suicide and it is reasonably necessary (to prevent harm, for a coroner's inquiry,
or to preserve evidence of an arrestable offence), an officer may "seize, or
prohibit the disposal of or dealing in, **any property**", and an inspector may
order a bank to freeze an account "for such period as may be specified" -- the
Act sets **no maximum**. A court may release money only for the listed purposes:
basic expenses, legal fees, holding charges, extraordinary expenses, prior liens,
or a company's daily operations. Attempted suicide is no longer an offence
(a Penal Code point this row does not read). Asserted.

### 6. Lost property: must return for 30 days, may return for a year, then nothing -- and the finder never

s 108: inside 30 days an identified owner who claims **must** get the property
back. After 30 days it is "unclaimed property" and may be sold or forfeited; an
owner who claims within **one year** of deposit **may** get it or the proceeds back
at the Commissioner's discretion. After a year, nothing. s 108(6): "A finder ...
has **no rights**". Asserted at days 5, 29, 30, 45, 200 and 400.

### 7. A dead person's property is better protected than a living person's

s 109(5): where the owner of a deceased person's property (under $1,000, released
without letters of administration) appears after disposal, "restitution **must** be
made", with no time limit. The owner of lost property under s 108 has no
entitlement after 30 days and nothing after a year. Asserted.

### 8. "Security activity" includes detaining people, armed or not

s 2(1)(d): "security activity" includes "the detention or arrest of individuals that
police officers ... are authorised ... to apprehend". s 86A: carrying it on in the
course of business without being an authorised Auxiliary Police Force employer is
punishable by $500,000 or three years for an individual and $1 million for anyone
else. Limbs (a) to (c) require arms; (d) does not. A business whose staff detain
shoplifters for the police falls within the text of (d). Asserted, as the text's
reach rather than a claim about enforcement.

### 9. A Commercial Affairs Officer can investigate any offence

s 64(2): a CAO "may investigate any suspected offence which appears ... to have been
committed under **any** written law", with police powers of an inspector, arrest
without warrant, entry and search. Nothing confines it to commercial crime. s 65B(2):
a forensic specialist can never be authorised to arrest, though s 65B(3)(a)(vi) lets
them detain and search a person interfering with a crime scene. Asserted.

### 10. Smaller things worth recording

- **s 26E:** forced entry for a medical emergency is barred where a suicide attempt
  is suspected; those cases go through s 26B instead.
- **s 27(3):** when police are hired privately, the Government is not liable for any
  property loss, including a third party's.
- **s 24(2):** a police officer acquitted by a court cannot be tried on the same
  charge under this Act.
- **s 115(2):** desertion and absence without leave by a national serviceman can be
  charged at any time; other disciplinary offences within three years.
- **s 110:** cash up to $1,000, perishables and things costly to keep may be disposed
  of at once.

## Relation to other rows

The Road Traffic Act 1961, s 65AA(2), orders forfeiture of a vehicle on conviction
under "section 26(2) of the Police Force Act 2004". In this Act as deposited,
s 26(2) is the officer's power to order a driver to stop; the offence is s 26(5)
(penalty s 26(8)). See the `road-traffic-act-1961` row, finding 1.

## What would need doing before this is worth anything

- **No case law was searched**, and finding 4 most needs it.
- The Police Regulations, General Orders and Auxiliary Police Forces Regulations
  were not retrieved; s 26F, s 27 fees and the prescribed security activities live
  there.
- The Criminal Procedure Code provisions the Act imports (arrest, search, release)
  are not followed.
