# AI-content labelling across three authorities

Three bodies of law now tell the makers and publishers of AI-generated media to mark it, and they do not agree on when.
The **EU**'s AI Act, Article 50, requires providers to mark generative output in a machine-readable form and deployers to disclose deep fakes, from 2 August 2026; a voluntary **Code of Practice** spells out what marking counts.
**Washington**'s E2SHB 1170 requires large consumer generators to embed provenance data from 1 February 2027.
**California**'s AI Transparency Act, rewritten by SB 1000 on 30 September 2026, requires every generator accessible in the state to embed a latent disclosure, and from 1 January 2027 requires large platforms to show users the provenance data they find.

The common technology is C2PA's Content Credentials, a signed manifest recording how a file was made.
Only Washington names it.
This subject runs the same content, including real signed C2PA files, through all three, and its census (`encodings/legalese/CENSUS.md`) lists where they give different answers.

## Why this subject is under `comparative/`, which is a proposal, not a ruling

Canon files enacted law by the authority that made it (`docs/directory-conventions.md` §2.1), and this subject has three.
Filing it as three sibling subjects (`eu/…`, `us/wa/…`, `us/ca/…`) would leave the census, the reason it exists, with no home: the census imports all three encodings and one shared domain module, and its answers are about the relation between them.
That is the argument `subjects/README.md` makes for `doctrine/contract/unilateral-mistake`, a rule compared across four jurisdictions, and for the bundled `contracts/payments/sg-miles-card`.

So this subject seeds `comparative/<topic>/`, for enacted law from more than one authority encoded against one domain module for the purpose of comparison.
**That grammar is proposed, not ruled.** `docs/directory-conventions.md` has not been amended.
Each instrument's authority is recorded in `subject.json` under `instruments`, so a reader looking for California's law can find it.
If the grammar is not adopted, the cheapest alternative is to file the subject under `eu/` with cross-links, which misstates two of its three authorities; or to split it, which strands the census.
