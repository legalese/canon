# Four ways to get out of a contract you signed by mistake

**A comparative encoding of unilateral mistake, built around the doctrine Singapore kept and
England may have lost.**

Status: `draft`. Law stated as at 7 September 2026. Nothing here has been reviewed by a lawyer;
see [NOTES.md](NOTES.md) for what that means and what else is missing.

---

## The situation

You sell laser printers online. At 3am somebody fat-fingers the price field and a printer that
costs $3,854 goes up at **$66**. By the time you notice, six people have ordered 1,606 of them.

Everyone's instinct is that the buyers should not get 1,606 printers. The law's problem is
saying *why* — because the ordinary rule is that you are bound by what you signed, and the
buyers signed nothing wrong. They clicked "buy" on a price you published.

That was Singapore in 2003, and the Court of Appeal's answer in
**Chwee Kin Keong v Digilandmall.com Pte Ltd [2005] SGCA 2** is the doctrine this corpus is
built around. Four jurisdictions answer the same question differently, and the differences are
not academic: on the same facts, one of them voids the contract, one makes it merely
cancellable, one leaves it standing, and one cannot say.

## What "unilateral mistake" means

Three kinds of mistake have three different names, and only one of them is here:

| | who is mistaken | example |
| --- | --- | --- |
| **common** mistake | both parties, about the same thing | both believe the rescue ship is 35 miles away; it is 410 |
| **mutual** mistake | both parties, at cross purposes | you mean the October ship, I mean the December one |
| **unilateral** mistake | one party only, and the other knows | you type $66 for a $3,854 printer, and I notice |

The Court of Appeal's own definition: *"In a unilateral mistake, only one of the parties makes a
mistake and the other party knows of his mistake"* (at [33]).

Everything below is about that third row.

## The two doors, and why there are two

Singapore lets a mistaken party through one of two doors, and which door matters enormously.

**The common law door** says the contract was **void** — there never was a contract, because the
two of you never actually agreed on the same thing. To get through it you need to show the other
side **actually knew** you were mistaken. *"[I]t is only where the court finds that there is
actual knowledge that the case comes within the ambit of the common law doctrine of unilateral
mistake. There is no consensus ad idem"* (at [53]).

**The equity door** says the contract was real but the court will **set it aside** — it is
**voidable**. This door opens on a lower knowledge threshold: it is enough that the other side
**ought to have suspected**. But — and this is Singapore's distinctive move — suspicion alone is
not enough. You also need something the Court of Appeal called *an additional element of
impropriety*.

Here is the holding, in full, because everything in this corpus is built on it (at [80]):

> Where the case falls within the common law doctrine of unilateral mistake, there is, in effect,
> no contract. There will be no room for equity to intervene. But where it does not and the court
> finds that there is constructive knowledge on the part of the non-mistaken party, the court
> would, in the exercise of its equitable jurisdiction, be entitled to intervene and grant relief
> when it is unconscionable for the non-mistaken party to insist that the contract be performed.
> Accordingly, we accept the amicus curiae's submission that constructive knowledge alone should
> not suffice to invoke equity. **There must be an additional element of impropriety.** The
> conduct of deliberately not bringing the suspicion of a possible mistake to the attention of the
> mistaken party could constitute such impropriety.

Two lines are drawn through "impropriety", and both are encoded:

- **Carelessness is not enough.** *"Negligence per se, on the other hand, should not be sufficient
  to invoke equity. Parties to a contract do not owe a duty of care to each other"* (at [77]).
- **Saying nothing is enough.** *"[A] conscious omission to disabuse a mistaken party is itself
  sufficient to constitute unconscionable conduct and thus justify the grant of equitable relief"*
  (at [73]).

## Why "uniquely Singaporean"

Because England had just abolished the equivalent jurisdiction, and Singapore declined to follow.

**Great Peace Shipping Ltd v Tsavliris Salvage (International) Ltd [2003] QB 679** held there is
no equitable jurisdiction to rescind for **common** mistake, overruling *Solle v Butcher*. The
Singapore High Court read that as sweeping away equitable relief for **unilateral** mistake too.
The Court of Appeal disagreed, and gave a reason that reads more like an argument about
institutions than about doctrine (at [74]):

> We would be loath to hold that there is no equitable jurisdiction in the courts with regard to
> unilateral mistake just because it may be difficult to delineate the scope or extent of that
> jurisdiction. By its very nature, the manner in which equity should be applied must depend on
> the facts of each case and the dictates of justice.

Having kept the jurisdiction, it then had to say what triggers it — and the
constructive-knowledge-**plus**-impropriety formula at [80] is that answer. No other jurisdiction
in this corpus draws the line in that place. That is the sense in which the doctrine is
Singapore's own: not that nobody else relieves against unilateral mistake, but that nobody else
relieves on **exactly these conditions**, and the neighbours diverge in both directions — one
relieves less, one relieves much more.

The doctrine is not a 2005 curiosity. A five-judge court restated it fifteen years later in
**Quoine Pte Ltd v B2C2 Ltd [2020] SGCA(I) 02** at [13], applying it to trades executed by
algorithms with no human in the loop.

---

## The four tests, side by side

| | **Singapore** | **England & Wales** | **Australia** (*Taylor v Johnson*) | **United States** (Restatement § 153) |
| --- | --- | --- | --- | --- |
| mistake must be about | a **term** | a **term** | a **term** | any **basic assumption** |
| knowledge needed | **actual** (common law) / **constructive** (equity) | **actual** (common law); equity unsettled | **actual or constructive** | **reason to know** — *or none at all* |
| extra element | **impropriety**, for the equity door | — | **deliberate steps** to stop discovery | none — the limbs are **alternatives** |
| result | **void** or **voidable** | **void**, or unsettled | **voidable** only | **voidable** only |
| relief without any knowledge? | no | no | no | **yes**, if enforcement is unconscionable |

The two structural differences that generate almost every divergence below:

1. **Singapore's equity door needs two things at once** — constructive knowledge **and**
   impropriety. The American rule needs **either** reason-to-know **or** unconscionability. A
   conjunction against a disjunction.
2. **Singapore has a "void" outcome and America does not.** § 153 makes a contract "voidable by
   him", full stop. Singapore's common law door produces a contract that never existed.

## The battery

Ten fixtures — eight decided cases and two clearly-labelled counterfactuals — run through all
four encodings. Every cell below is **computed by the modules in this directory**, not typed by
hand; the generator and its output are in [report/](report/).

| case | SG | E&W | AU | US |
| --- | --- | --- | --- | --- |
| *Digilandmall*, 3rd appellant — actual knowledge | **void** | void | stands | voidable |
| *Digilandmall*, 2nd appellant — constructive knowledge + sharp practice | **voidable** | *refuses* | stands | voidable |
| *Hartog v Colin & Shields* — hare skins per pound, not per piece | void | **void** | stands | voidable |
| *Riverlate Properties v Paul* — lessor's own solicitor's slip | stands | **stands** | stands | stands |
| *Taylor v Johnson* — $15,000 total, not per acre | voidable | *refuses* | **voidable** | voidable |
| *Smith v Hughes* — the oats were new, not old | stands | **stands** | stands | stands |
| *Smith v Hughes*, counterfactual: risk not borne | stands | stands | stands | **voidable** |
| *Donovan v RRL Corp* — misprinted car advertisement | stands | stands | stands | **voidable** |
| *Quoine v B2C2* — algorithmic trades at 250× market | **stands** | stands | stands | stands |
| *Quoine*, counterfactual: enforcement unconscionable | stands | stands | stands | **voidable** |

**Bold** marks the jurisdiction that actually decided the case; those cells are checkable against
the judgment and the module comments say which paragraph. The other cells are what the encoded
rule computes on those facts — useful for comparison, and **not** a claim that any foreign court
has so held.

---

## The five deltas

### Delta 1 — Singapore relieves where Australia's stated test does not

*Digilandmall*'s **second appellant** is the purest instance of the doctrine. He suspected the
$66 price was wrong, searched other sites and found the printer at $3,000, wondered aloud whether
he might be buying only parts, asked a friend what the position would be if the price were an
error — and then bought 180 printers without mentioning any of it. The Court of Appeal (at [92]):

> While he had thought that there could be a mistake, he went on to snap up a total of 180
> printers. The court should be entitled to set side the various purchases on the ground of sharp
> practice or unconscionable conduct.

He is relieved against in Singapore. Under **Taylor v Johnson** he is not — because that test asks
whether the other party *"deliberately set out to ensure that the [mistaken] party does not become
aware of his mistake"*, and he did no such thing. He simply said nothing.

The Court of Appeal saw the gap and stepped across it deliberately (at [73]):

> What is less clear is whether it was an essential element for equity to intervene that the
> non-mistaken party must "deliberately [set] out to ensure that the [mistaken] party does not
> become aware of his mistake or misapprehension". It seems to us that a conscious omission to
> disabuse a mistaken party is itself sufficient to constitute unconscionable conduct.

**One sentence of divergence, and it decides the case.** Australia asks what you *did*; Singapore
asks what you *didn't do*.

### Delta 2 — void against voidable, which only a third party ever feels

Take *Digilandmall*'s **third appellant**, where actual knowledge was found. Singapore says
**void**. The Restatement says **voidable**. Both let the seller out, so on the face of it nothing
turns on the difference.

It turns on it completely the moment somebody else is involved. Suppose the buyer resells a
printer to a stranger who pays full price and knows nothing. Under a **void** contract the buyer
never owned it, so he had nothing to sell and the stranger gets nothing. Under a **voidable** one
he owned it until the seller rescinded, so the stranger keeps his printer and the seller's remedy
is gone.

The Court of Appeal had exactly this in view when it refused to simplify the doctrine into a
single actual-knowledge rule (at [76]):

> [W]e believe that simplicity may not always lead to a just result, especially where innocent
> third parties are involved.

This is asserted in the encoding rather than described: `a good faith purchaser for value without
notice keeps what he bought` is `FALSE` on Singapore's verdict and `TRUE` on the American one, for
the same case.

**Australia's version of this delta is larger.** On the reading the Singapore court attributed to
*Taylor v Johnson*, Australia routes *even an actually-known* fundamental mistake to equity, so it
has no "void" outcome at all — which is why its column reads `stands` on facts where Singapore and
England both void. The Court of Appeal flagged the point and declined to follow it: *"we would
hesitate to adopt a similar position"* (at [73]). This is the single most consequential
characterisation in the corpus and it rests on one hedged sentence in a Singapore judgment about
an Australian one; it is recorded as fork **F-AU1** and the module says so on its face.

### Delta 3 — America relieves against a wholly innocent counterparty

**Donovan v RRL Corp** (2001) 26 Cal 4th 261: a newspaper's proofreading error advertised a used
Jaguar at $25,995 instead of $37,995. The buyer walked in with the advertisement. He *"was unaware
of the mistake before it was disclosed to him"* — he had no idea, and did nothing wrong.

The dealer got out of the contract anyway, because § 153(a) asks only whether **enforcement would
be unconscionable** and never asks what the other party knew.

All three Commonwealth tests stop at their very first condition. There is no knowledge, so there is
no doctrine to apply. The buyer in Singapore, England or Australia drives away in a Jaguar at
$12,000 under the dealer's cost.

**This is the widest gap in the corpus**, and it is a difference in *kind*, not degree: Singapore's
doctrine is fundamentally about **the other party's conscience**, and the American rule has a limb
that is about **the bargain** instead.

### Delta 4 — England cannot answer the question Singapore answered

Two fixtures make the England column **refuse** rather than answer: *Digilandmall*'s second
appellant, and *Taylor v Johnson*. They are the two that fall in the class the Court of Appeal
decided at [80] — constructive but not actual knowledge, plus impropriety.

That is not a hole in the encoding. It is the finding. After *Great Peace Shipping* the surviving
English authority is two first-instance decisions noted in passing by a foreign appellate court
(at [74], citing *Huyton SA v Distribuidora Internacional* and *Harrison v Halliwell Landau*).
Two High Court judgments are not a settled rule, and a model that answered anyway would be
inventing English law — which is a worse outcome than saying so, because it would be believed.

So the England module carries the corpus's one `REFUSE`, and it is deliberately **narrow**:
England answers everywhere else in the battery, including *Smith v Hughes*, where a *known*
mistake as to quality still binds. A refusal that swallowed the settled cases would be reporting
doubt about a case decided in 1871.

**The refusal is the most interesting cell in the table.** Singapore's contribution is visible
precisely as the two rows where its nearest relative has nothing to say.

### Delta 5 — where everybody agrees, they agree for different reasons

*Smith v Hughes* — the buyer wanted old oats, got new ones, and the seller knew what he believed —
comes out `stands` in all four columns. But the encoding shows the four are not agreeing about
anything:

- **Singapore, England and Australia** stop because the mistake was about the **quality of the
  oats**, not about a **term** of the sale. The inquiry never reaches knowledge or conduct.
- **The United States** clears that threshold — a basic assumption is enough — and stops one step
  later, on **risk allocation**: a buyer who inspects a sample and forms his own view *"treats his
  limited knowledge as sufficient"* under § 154(b).

Move that one field and the agreement collapses: the counterfactual fixture, identical but for
risk, comes out **voidable** in America and `stands` everywhere else. Agreement in the outcome
column can conceal complete disagreement about the law, and only running the tests separately
shows it.

---

## What this cannot tell you

- **It is not legal advice, and it is not reviewed.** No lawyer has read it. `status: draft`.
- **"Fundamental" is an input, not an output.** The Court of Appeal expressly declined to define
  it: *"it is wholly unnecessary for us to deal with the question as to what nature of mistake
  would constitute a serious mistake sufficient to vitiate a contract"* (at [34]). So the model
  asks you whether the mistake was fundamental; it will not tell you.
- **Three of the four modules are read through a Singapore lens.** The Australian and English
  materials are quoted from *Chwee Kin Keong*'s account of them, because that is the source this
  corpus actually retrieved. The Restatement is quoted from a Californian judgment that adopted
  it. None of the three is a survey of that jurisdiction's law, and the Australian module says so
  in its first paragraph.
- **The Restatement is not the law of the United States.** It is law where a State adopts it, and
  adoption is uneven.
- **Remedies stop at the verdict.** Whether relief is granted on terms, the bars to rescission
  (delay, affirmation, restitution becoming impossible), rectification, and how registration
  statutes cut across the third-party consequence are all outside the encoding.
- **Characterising a judgment into nine fields is a judgement.** The contestable calls are in
  [registers/fork-register.json](registers/fork-register.json), not buried in comments.

## The files

| file | what it is |
| --- | --- |
| `mistake-domain.l4` | the shared vocabulary. No rule of law in it |
| `sg-unilateral-mistake.l4` | Singapore — both doors, from *Chwee Kin Keong* |
| `ew-unilateral-mistake.l4` | England & Wales — the settled common law, and the one refusal |
| `au-unilateral-mistake.l4` | *Taylor v Johnson*, as *Chwee Kin Keong* read it |
| `us-unilateral-mistake.l4` | Restatement (Second) §§ 153–154 |
| `mistake-comparison.l4` | verdict naming, divergence, and the third-party consequence |
| `mistake-cases.l4` | ten fixtures, 69 assertions, and the five deltas asserted |

Run it:

```sh
l4 run mistake-cases.l4
```

69 assertions, 0 failing, measured 7 September 2026.
