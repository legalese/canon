# Spam Control Act 2007 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 April 2022.

**Checks:** `l4 run spam-cases.l4` and `l4 run spam-civil-action-cases.l4` —
163 assertions satisfied, 0 errors, 0 warnings.

## Scope

The Act is about 30,000 characters and this encodes ss 2–15 and both Schedules.
Not encoded: s 1 (short title), s 16 (codes of practice — a power to approve and
a duty to comply with whatever is approved; no code was retrieved), s 17
(amendment of Schedules) and s 18 (regulations).

The one judgment the Act asks for and this encoding does not make is the s 3(1)
conclusion that the **primary purpose** of a message is one of the twelve things
listed. That is a conclusion on the content, presentation and linked content of
the whole message. It is taken here as a fact supplied.

The s 6(1) bulk thresholds are carried as parameters rather than written in,
because s 6(2) lets the Minister vary any of them by order in the Gazette. No
such order was retrieved. `the thresholds in section 6(1) as enacted` supplies
the figures the Act itself states.

## What the Act turns out to say

### 1. Part 2 does not apply to mobile telephone numbers

The long title describes an Act to control spam "sent in bulk **by email or by
text or multimedia messaging to mobile telephone numbers**". Part 2 — the only
part that prohibits the way a list was built — then says, in s 8(2), that it
"does not apply to any electronic message sent to a mobile telephone number".

So a person who generates mobile numbers by permutation (a dictionary attack in
terms of the s 2 definition) and texts every one of them **does not contravene
s 9**. The identical conduct against email addresses does. Asserted as that
pair.

What is left for the texter is s 11, and s 11 asks only that the message carry a
compliant unsubscribe facility and an `<ADV>` label. It says nothing about how
the numbers were obtained. A fully compliant bulk text campaign built entirely
on permuted numbers contravenes nothing in the Act.

Part of the hole is closed from an unexpected direction. s 4A says that where a
message is sent to an instant messaging account whose name is a mobile number,
the message is **not** a message sent to that number. So the same blast
delivered through a messaging app is inside Part 2 and a dictionary attack
against it does contravene s 9. The provision was plainly written to stop
senders claiming the benefit of the mobile-number rules; its effect here is to
make the messaging-app route *more* regulated than the SMS route in Part 2.

### 2. The Second Schedule is wider than the section that gives it force

Every requirement in the Second Schedule opens "**every** unsolicited commercial
electronic message must contain …". The only provision that gives the Schedule
force is s 11, and s 11 binds only "any person who sends … unsolicited
commercial electronic messages **in bulk**".

Nothing else picks the Schedule up: s 17 lets the Minister amend it, and s 13
gives a right of action for a contravention of s 9 or s 11 and of nothing else.

So an unsolicited commercial mailing of 90 messages with a false subject line,
forged headers and no unsubscribe address **fails the Second Schedule and
contravenes nothing**. Asserted: the mailing of 90 fails
`the Second Schedule requirements are met` and passes
`NOT the person contravenes section 11`.

The encoding keeps the two questions apart for exactly this reason —
`the Second Schedule requirements are met` does not ask about bulk, and
`the person contravenes section 11` does.

### 3. One dollar of proved loss is worth $1.5 million

s 14(3)(b) caps statutory damages twice over: at $25 for each message, **and** at
$1 million in the aggregate — the second "unless the claimant proves that the
actual loss suffered by the claimant from such electronic messages **exceeds**
$1 million".

Two claimants, each with 100,000 messages:

| proved loss | aggregate cap | statutory damages ceiling |
|---|---|---|
| exactly $1,000,000 | holds | **$1,000,000** |
| $1,000,001 | lifted | **$2,500,000** |

Asserted as that pair, together with
`what one more dollar of proved loss adds to the ceiling` = **$1,500,000**.

But the escape is narrower than it looks, because the thing that lifts the cap
is also the thing that makes the *other* election worth having. s 14(3) gives the
claimant an election between actual damages and statutory damages, and s 14(2)
makes them mutually exclusive. A claimant who can prove a loss above $1 million
can simply elect that loss. So the lifted cap is worth something only where $25
a message comes to more than the loss proved — which needs **more than 40,000
messages** before the per-message limb even reaches $1 million. The four cases
are asserted:

| messages | proved loss | statutory ceiling | better election | lifting worth anything? |
|---|---|---|---|---|
| 30,000 | $1,200,000 | $750,000 | damages | no |
| 50,000 | $1,500,000 | $1,250,000 | damages | no |
| 100,000 | $1,200,000 | $2,500,000 | **statutory** | **yes** |
| 40,000 | $1,000,001 | $1,000,000 | damages | no — exactly on the cap |
| 40,001 | $1,000,001 | $1,000,025 | statutory | yes, by $25 |

For the claim this Act was most likely written to support — an individual with a
thousand messages and a few hundred dollars of provable loss — none of this
matters. $25 a message comes to $25,000 against $500 of loss, and the aggregate
cap is nowhere in sight. That case is asserted too.

### 4. Loss or damage is the gate, and being spammed is not loss

s 13(1) gives the action to "any person who has **suffered loss or damage** as a
direct or an indirect result". s 14(5) widens what counts by including "any
pecuniary loss", but the requirement stands. A recipient who received a hundred
unlawful messages and is out of pocket by nothing has no action. Asserted.

Two further points on s 13(1) which the encoding records:

- The gateway is a contravention of **s 9 or s 11 and nothing else**. A
  contravention of s 12(1) cannot stand alone, because s 12(1) is itself defined
  by reference to a contravention of s 9 or s 11.
- "Any person" is not confined to recipients. A provider whose network carried
  the traffic, or a business whose domain was forged in the header information,
  suffers loss as an indirect result and is within the section.

### 5. Smaller things worth recording

**Wilfulness is a factor, not an element.** Neither s 9 nor s 11 carries any
mental element; both are flat prohibitions. "Wilful" appears once, in s 14(4)(a),
as something the court weighs in fixing statutory damages. A sender who harvests
addresses deliberately and one who buys a tainted list in good faith contravene
s 9 alike, and are distinguished at the remedy stage or not at all. Asserted as
`NOT wilfulness is required for the contravention`.

**Only limb (c) of s 12(1) carries knowledge.** "Aid, abet or procure" in limb
(a) does not, which is a departure from the general law of abetment.

**The carriers' safe harbour reaches all three prohibitions.** s 12(2) protects a
provider from s 12(1), s 9 **and** s 11 — but only "merely because" it provides
the service. The encoding reads a made-out limb of s 12(1) as taking the person
outside "merely because", and asserts the pair (`is within the safe harbour` and
`contravenes section 12(1)` both true for the provider who also conspired) so
that the reading is visible rather than buried.

**A mistake lifts almost everything, and not quite everything.** Second Schedule
para 2(9) lifts sub-paragraphs (1) to (7) where the message was sent by mistake
— defined in para 1 as a *reasonable mistake of fact*. It does not lift para
2(8), the duty not to disclose what is in an unsubscribe request. That is the
right carve-out: a mistaken mailing still draws real requests from real people.
Asserted.

**Instant messaging accounts escape paragraph 3 entirely.** Para 3(3) excludes
them from the labelling requirements, so a messaging-app blast needs an
unsubscribe facility (para 2 applies) but needs no `<ADV>`, and its header
information and the sender's contact details may be false. Combined with the
fact that neither para 2(2) nor para 2(3) bites on that channel — so a postal
address will do for unsubscribing — five thousand unsolicited commercial
messages with forged headers, no label and a post-box satisfy the Schedule.
Asserted.

**Para 1's definition of "header information"** — source, destination and routing
information — was written for email and, given para 3(3), has nothing left to do
on the messaging-app channel.

**s 14(1) and s 14(3) are in tension over who decides.** s 14(1) says the types of
relief "that the court **may** grant **include**" the three listed; s 14(3) says
the claimant "**is entitled**, at the election of the claimant". The encoding
follows s 14(3), the more specific provision, and does not model a residual
discretion to refuse what s 14(3) grants. Recorded as an interpretive choice.

**The First Schedule's widest ground has no certificate.** Para 1 excludes a
message authorised by the Government or a statutory body "on the occurrence of
any public emergency, **in the public interest** or in the interests of public
security or national defence". Para 2 makes a ministerial certificate conclusive
evidence where doubt arises "as to the existence of a public emergency or as to
whether any electronic message is sent in the interests of public security or
national defence" — the emergency limb and the security limb. The public
interest limb, which is the broadest of the three, has no certificate and no
stated way of being settled. Asserted as
`NOT a ministerial certificate can settle the doubt` on that fixture.

**s 15 names only the defendant as payer**, so it confers no power to order an
unsuccessful claimant to pay, leaving that to the court's general jurisdiction.

**s 4(2) is a non-effect.** It says it does not matter whether the address exists
or whether the message arrives. The two facts are carried as fields that nothing
reads, and the cases assert that a message to a dead address that never arrived
is still an unsolicited commercial electronic message. That is the whole of what
the subsection does — except that it gives s 7(2)(e), the undeliverable-message
Singapore link, something to operate on.

**s 3(2)'s deeming does not reach the fraud limbs.** "It does not matter whether
the goods … exist" is confined to paragraphs (d) to (l). Paragraphs (m), (n) and
(o) — the deception limbs — are outside it, which is unsurprising, since what a
fraud offers never exists, but it means the deeming is not available there.

## What would need doing before this is worth anything

- No code of practice under s 16 was retrieved, and none of the Act's technical
  content about what providers must actually do is in those codes' absence
  knowable.
- No order under s 6(2) varying the bulk thresholds was searched for.
- No regulations under s 18 were retrieved.
- **No case law was searched.** In particular, nothing here reflects how a court
  has read "primary purpose" in s 3(1), "loss or damage" in s 13(1), or the
  election in s 14(3). The $1 million discontinuity in finding 3 is a reading of
  the words and has not been tested against authority.
- The interaction described in finding 1 — Part 2's mobile-number exclusion
  against the Act's own long title — is stated as a reading of the deposited
  text. It should be checked against the 2020 amending Act (40/2020), which
  inserted s 8(1), s 8(2) and s 4A together, before it is relied on as a defect
  rather than a deliberate allocation between Parts 2 and 3.
