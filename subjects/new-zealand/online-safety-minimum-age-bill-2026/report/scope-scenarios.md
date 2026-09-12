# Online Safety Bill — three scope scenarios, worked against real services

**Date:** 2026-09-11
**Subject:** `new-zealand/online-safety-minimum-age-bill-2026`
**Source:** Online Safety (Minimum Age and Child Safety Risk Assessment) Bill, 2026 No 339-1
**Related incidents:** #1, #2, #4

---

## How to read this

Each scenario runs a real, publicly described service through the cl 5 test as encoded in
`part-1-preliminary.l4`. The services are named because abstract examples let a drafter say
"that would never happen"; these exist today.

**This is scope analysis, not a determination about any company.** Every characterisation below
is based on public descriptions of these products, and each one turns on a question the Bill
leaves to the operator's own assessment — which is the point being made. Nothing here says any
named company is or would be in breach of anything.

The first two scenarios are **over-breadth**: services with no plausible connection to the harm
the Bill describes are caught. The third is **under-inclusion**: a service matching the Bill's
own account of harm is not caught.

---

## Scenario 1 — The AI tutor
### Over-breadth. Incident #1.

**Real example: [Buddy.ai](https://buddy.ai/)** — a voice-based AI English tutor for children
aged 3 to 8. The child talks to an animated character called Buddy, which uses speech
recognition to run conversation practice, alphabet and number games. It is a language-learning
product for pre-schoolers, sold to parents on exactly that basis.

**The contrast case: [Khanmigo](https://www.khanmigo.ai/)** — Khan Academy's AI tutor, which
its own marketing calls a "never-judgy study buddy", designed to guide a student through a
problem rather than give the answer.

### How the Bill applies

Both are, on any ordinary reading, education services. cl 5(2)(f) excludes an internet service
that "solely or primarily enables a user to ... access or engage in education services", and
cl 5(1)(a)(iv) requires that an age-restricted platform *not* be an excluded service. So both
sit outside limb (a). That is the carve-out working as intended.

Then limb (b) arrives with no carve-out at all. cl 5(1)(b) catches any internet service that is
accessible in New Zealand, displays digital content, and "uses artificial intelligence solely or
primarily to simulate a social connection, an emotional connection, or any other form of
personal connection with a user". Nothing in that limb refers to cl 5(2). An excluded service
is excluded from limb (a) and from nowhere else.

Machine-evaluated on the drafted text:

```
5(1)(a)   an ai tutor with a companion avatar   →  FALSE    (excluded service)
5(1)(b)   an ai tutor with a companion avatar   →  TRUE     →  in scope
          an ai tutor whose ai only teaches     →  FALSE    →  out of scope
```

### Why it is problematic

**The line falls in an unworkable place.** The test is not "does it use AI" or "does it have an
avatar" — it is whether the AI is used *solely or primarily to simulate a personal connection*.
Buddy.ai's whole pedagogy is that a small child will talk to a friendly character when they
will not talk to an exercise. Khanmigo's is that a patient tutor gets a teenager to the answer
themselves. Both rely on rapport; one is arguably built on simulating it. Nobody can say in
advance which side of that line either sits on, and the drafting gives no help.

**Marketing copy becomes legally operative.** Khan Academy calls Khanmigo a "study buddy". On
the Bill's language, a product page describing warmth, companionship or friendship is evidence
that the AI is used primarily to simulate a personal connection. The rational response is to
scrub the marketing, which changes nothing about what children experience.

**The consequence is disproportionate to the doubt.** Getting it wrong means failing the cl 11
duty, which is cl 34(3)(a), routed by cl 45 to Tier 1: for a body corporate, the greater of $40
million and 10% of relevant global turnover. A small EdTech company facing that exposure on an
unanswerable characterisation question will either geoblock New Zealand or strip the persona
that makes the product work for young children.

**And the exclusion it defeats was deliberate.** Parliament decided education services should be
out. Limb (b) reverses that decision for a subset of education services, silently, by omission.
If that reversal is intended it needs saying in terms; if it is not, limb (b) needs the cl 5(2)
carve-out that limb (a) already has.

---

## Scenario 2 — The scholarly repository
### Over-breadth. Incident #4.

**Real example: [SSRN](https://www.ssrn.com/)** — the Social Science Research Network, owned by
Elsevier. Authors upload working papers; readers browse and download them. SSRN reports, at
author level, how many papers an author has posted, how many times each has been downloaded,
and how the author ranks; at paper level, how many times the abstract has been viewed and the
paper downloaded. It distributes subject-matter alerts, and some metrics require a free account
to view.

### How the Bill applies

Run it through limb (a):

- **cl 5(1)(a)(i)** — accessible from New Zealand. Yes.
- **cl 5(1)(a)(ii)** — enables the exchange of digital content between 2 or more users. Authors
  upload; readers download. Yes.
- **cl 5(1)(a)(iii)** — has one or more specified features. **cl 5(2)(c)** is a feature that
  "displays information to a user about how others have viewed or engaged with **the user's**
  digital content or account". That is precisely an author download and abstract-view count.
  One feature is enough, and SSRN's recommendation alerts arguably supply a second under
  cl 5(2)(a).
- **cl 5(1)(a)(iv)** — not an excluded service. Here everything turns. Is a working-paper
  repository "solely or primarily" enabling a user to "access or engage in education services"
  under cl 5(2)(f)? A repository disseminates scholarship between researchers; it does not
  teach anyone. On that reading it is not an education service, and it is in scope.

Machine-evaluated on the drafted text:

```
has 1 or more specified features                        →  TRUE
is an age-restricted platform                           →  TRUE
same service, characterised as an education service     →  FALSE
```

### Why it is problematic

**The same service is in or out on a characterisation the Bill never settles.** Two competent
lawyers reach opposite answers on cl 5(2)(f) and the encoding shows both, from the same facts.
That is not a hard case at the margin; it is a coin-flip at the centre of the definition, with
Tier 1 exposure riding on it.

**The feature that catches it is a scholarly norm, not a risk.** cl 5(2)(c) exists because
like-counts and view-counts drive compulsive checking in teenagers. Download statistics on an
academic paper are the same mechanism aimed at a different population for a different purpose.
The Bill's definition captures the mechanism and cannot see the purpose.

**The reach is much wider than SSRN.** Any service that shows a contributor how their own
contribution performed is caught by the same limb: arXiv-style preprint servers, code hosting
with stars and view counts, photography and writing communities, recipe and hobby sites.

**The effect on the 15-year-old is real but narrower than it first looks.** cl 11 is a duty to
prevent under-16s *having an account*, not a duty to block access. A 15-year-old could still
read an open-access paper. But where a repository requires an account to download, or where
metrics and alerts sit behind sign-in, the distinction collapses — and the operator's compliant
response is to refuse the account, which is the first-year law student, the accelerated
14-year-old, and the school science-fair entrant turned away from the research literature.

---

## Scenario 3 — The AI-generated feed
### Under-inclusion. Incident #2. The loophole.

**Real example: [Meta's Vibes](https://about.fb.com/news/2025/09/introducing-vibes-ai-videos/)**
— a TikTok-style vertical feed inside the Meta AI app, launched September 2025, where nothing in
the feed is made by a human: it is an endless stream of AI-generated video. Meta began testing a
standalone Vibes app in early 2026, live in Brazil and Mexico. OpenAI's Sora app was the other
entrant; OpenAI announced in March 2026 that it would discontinue it.

**Vibes as it exists today is in scope**, and this matters to the argument. Users can generate
videos from a prompt, remix videos other users have generated, and post the result to the feed.
That is the exchange of digital content between 2 or more users under cl 5(1)(a)(ii), and with a
recommender and an endless feed it satisfies cl 5(1)(a)(iii) comfortably.

**The loophole is one product decision away.** Remove the post button. Keep the feed, the
personalised recommender, the infinite scroll, the disappearing content; generate everything
server-side; let the user watch, and rate, and never contribute. Now:

- **cl 5(1)(a)(ii)** fails. There is no exchange of digital content between 2 or more users,
  because there is only one user and a model.
- **cl 5(1)(b)(iii)** fails. The AI generates and recommends content; it does not simulate a
  social, emotional or personal connection with the user.
- **cl 5(1)(c)** is unused until the Minister makes regulations naming that specific service.

Machine-evaluated on the drafted text:

```
has 1 or more specified features   →  TRUE
is an age-restricted platform      →  FALSE
```

### Why it is problematic

**Every feature the Bill itself nominates as risky is present, and the service is out of
scope.** Read cl 5(2)'s specified features and cl 14(2)(b)'s risk matters — recommender
systems, behaviour profiling, endless feeds, time-limited content, the business model — and then
read this service. It is the Bill's own description of harm, assembled in full, outside the
Bill's own definition.

**The requirement doing the excluding is a proxy that has stopped tracking the risk.** Feeds used
to be dangerous *because* users fed them: the content came from peers, and peer content is what
makes a 13-year-old compare themselves to others. cl 5(1)(a)(ii) encodes that assumption. AI
video generation removes the peers and keeps the feed. The harm mechanism — algorithmic
optimisation of a minor's attention — survives intact, and the definitional hook does not.

**It is a stable product strategy, not an accident.** An operator facing Tier 1 exposure has an
obvious and entirely lawful response: stop being a platform where users exchange content, and
become a publisher that broadcasts generated content to an audience of one. The economics of
generated feeds already point that way — no moderation cost, no creator payouts, no rights
clearance. The Bill supplies a regulatory reason to finish the journey.

**The fix available is one service at a time.** cl 62(1)(a) lets the Minister specify such a
service as an age-restricted platform by regulation — after considering its content, features
and users, seeking the regulator's advice, and consulting. That is a workable answer for one
known product and no answer at all for a category that can be spun up in an afternoon. The Act
would be permanently one Order in Council behind the market.

---

## What the three have in common

The scope test in cl 5 works by proxies: *exchange between users* as a proxy for social risk,
*specified features* as a proxy for compulsive design, *primary character* as a proxy for what a
service is really for. Each proxy was sound about the 2020 internet.

Scenarios 1 and 2 are proxies **over-firing**: an AI persona and a download counter trip
definitions written for companion apps and like-counts. Scenario 3 is a proxy **under-firing**:
generated content walks through the gap where user-generated content used to be.

Two drafting responses follow, and they are independent:

1. **Give limb (b) the cl 5(2) carve-out that limb (a) has**, so that an excluded service is
   excluded from the whole of cl 5 — or say expressly that it is not, and why.
2. **Sever the feature test from the exchange requirement** in limb (a), so that a service with
   specified features and no user-to-user exchange can still be caught. As drafted, cl
   5(1)(a)(ii) and (iii) are cumulative; making the feature limb independent would close
   Scenario 3 without touching anything else.

Neither response needs the review under cl 64, and both are cheaper now than after commencement.
