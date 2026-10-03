# Round 3: index the remaining US states and Canadian provinces and territories

You are indexing legislation for the `legalese/canon` L4 corpus. **Metadata only: never download,
copy or quote statute text.** The point is to identify, for each jurisdiction you are given, the
principal statute that governs each of twelve everyday topics, and to record the register's licence.

## The twelve topics

Payroll/wages · Leave/holiday pay · Termination/severance · Pensions/social security ·
Government benefits · Personal tax/withholding · Insurance claims · Utility billing ·
Passenger compensation · Consumer/tenancy · Customs/duties · Work permits/immigration

One statute per topic, at most. A statute may serve more than one topic: list it once per topic it
covers (the scaffold groups them later). If a topic is governed by federal law, or by regulation
rather than statute, or simply does not exist there, do not invent one: record it in `topic_gaps`
with the reason, naming the federal Act where that is the answer (for US states, customs and
immigration are federal; for Canadian provinces, customs and immigration are federal, and EI and
CPP/OAS are federal).

Choose the **principal consolidated statute**, not an amending Act. In the US, statutes are usually
codified: name the code division the way that state cites it (e.g. "California Labor Code
Division 2, Part 1" style), and give the identifier the state's own register uses. Prefer the
state's or province's **official** register (Legislature, Legislative Counsel, King's Printer,
Secretary of State) over Justia, Casetext, FindLaw or a commercial publisher. Note in
`access_notes` if only a commercial or unofficial site carries the consolidated text.

## Verify, don't assume

For every Act you list, **fetch the register's own page** and say in `verified_how` what you saw:
the exact title, its in-force or repealed status, the version or as-at date. `in_force` is `"yes"`,
`"not yet in force"` or `"unclear"`; anything not plainly in force needs a `notes` explanation.
Do not rely on search-result snippets, your own memory, or a secondary site for in-force status.

## Access rules, which are absolute

- Identify yourself honestly. Do not pretend to be a browser you are not.
- If a register blocks scripted access, returns 403/429, or shows a bot challenge, **stop and
  record that** in `access_notes`. Never work around a block, a CAPTCHA or a rate limit.
- Space requests about 1.5-2 seconds apart. Do not hammer a register.
- If you cannot verify a jurisdiction at all, return it with an empty `acts` list and say why.

## The licence matters as much as the Acts

Read the register's **own** terms or copyright page and quote from it. Set `open_licence` true only
if reuse *and adaptation* are permitted. Be careful and jurisdiction-specific:

- **US states**: statute text is generally not copyrightable (government edicts doctrine, *Georgia
  v. Public.Resource.Org*, 590 U.S. 255 (2020)), but several states' sites assert copyright, often
  over a publisher's annotations and numbering. Say what the site asserts *and* what the doctrine
  means for the statute text itself. Note if the official code is published by a commercial
  publisher (LexisNexis, Thomson Reuters) under contract.
- **Canadian provinces and territories**: Crown copyright applies, and each King's Printer sets its
  own terms. Some permit reproduction but not adaptation; some require a licence or a fee; a few use
  an open licence. Quote the condition, and say plainly whether adaptation is permitted.
- **Quebec** (and New Brunswick, Manitoba, Nunavut, NWT, Yukon in part): French and English versions
  are both official. Say so in `language_authenticity`.

## Output

Write one JSON file: `tools/topics/round3/<group>.json` (the group name is in your task). It is an
object keyed by jurisdiction name, exactly this shape — the scaffold script reads it:

```json
{
  "Alabama (US state)": {
    "jurisdiction": "Alabama (US state)",
    "register": {"name": "...", "url": "https://...",
                 "access_notes": "how you fetched it, what worked, what blocked you, how many requests"},
    "licence": {"summary": "...", "open_licence": true,
                "terms_url": "https://...", "attribution": "...",
                "quote": "a short verbatim quote from the terms"},
    "language_authenticity": "English is the sole official language of the statutes." ,
    "acts": [
      {"topic": "Payroll/wages", "title": "...", "identifier": "...", "url": "https://...",
       "in_force": "yes", "verified_how": "fetched ...: title '...', status ..., as at ...",
       "notes": "optional"}
    ],
    "topic_gaps": [{"topic": "Customs/duties", "reason": "Federal matter (19 U.S.C.)."}]
  }
}
```

Name US jurisdictions `"<State> (US state)"`, and `"District of Columbia (US)"`. Name Canadian ones
`"<Province> (Canada)"` and `"<Territory> (Canada)"`.

Return, as your final message, only a short summary: for each jurisdiction, the count of Acts and
gaps, the licence verdict in a few words, and anything a human must check. Do not paste the JSON.
