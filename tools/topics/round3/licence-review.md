# Round 3 licence evidence, for a human decision

One row per jurisdiction, as the index agents found it on 2026-09-23. **Nothing here is a decision.**
Record decisions in `licence-decisions.json` (copy `licence-decisions.template.json`), using
one of `open`, `conditional`, `not-open`, `unclear`. `scaffold-round3.py` treats anything
undecided as `unclear`, which means metadata only: no statute text is ever deposited there.

For US states, remember that the text of a statute is not copyrightable at all: it is an edict
of government (*Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)). A register's copyright
notice may still validly cover a publisher's annotations and numbering, and a platform's terms
of use bind whoever takes text *from that platform* as a matter of contract, whatever the
copyright position. Those are two different questions and this sheet keeps them apart.

| jurisdiction (decisions key) | Acts | agent's reading | what the register asserts |
|---|---|---|---|
| **Alabama** (`us-al`) | 7 | reuse and adaptation permitted | The Legislature's code site publishes no terms of use and no licence; the only notice is a bare '(c) 2026' in the footer. Nothing on the site asserts copyright in the statutory text or restricts reuse. Under the US government edicts doctrine (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)) the ... |
| **Alaska** (`us-ak`) | 8 | not established | Not open as the register presents it. akleg.gov footers read 'Copyright (c) 2026 Alaska Legislature, All Rights Reserved' and the site's Disclaimer/Credits page requires you to ask permission before reproducing site content, with credit and a copy of the result. That is a permission-on-request regim... |
| **Alberta** (`ca-ab`) | 9 | not established | Crown copyright, held by the Government of Alberta through the Alberta King's Printer. Reproduction of Alberta's statutes and regulations is expressly permitted to any person, free and without asking permission, on two conditions: due diligence as to accuracy, and acknowledgement in the form '(c) Al... |
| **Arizona** (`us-az`) | 10 | not established | Not open as the register presents it: every page carries '© 2026 Arizona State Legislature. All Rights Reserved', with no terms-of-use or licence page and no permission to copy or adapt. The register also disclaims being the official text - it says the online compilation is 'primarily maintained for... |
| **Arkansas** (`us-ar`) | 7 | not established | Not open. The only notices on the state's own access route are LexisNexis's: 'Copyright © 2026 LexisNexis.' in the footer, with links to LexisNexis's general Terms & Conditions, and a 'Purchase Code of Arkansas in Print' link - i.e. free read access under a commercial publisher's terms, with no perm... |
| **Colorado** (`us-co`) | 8 | not established | Not open, and Colorado is unusual in claiming copyright by statute: the Colorado Revised Statutes table of contents shows s 2-5-115, 'Copyright by state', and s 2-5-118, 'Official statutes - publications by other persons or agencies'. The public-access site tells anyone wanting to republish to come ... |
| **Connecticut** (`us-ct`) | 8 | reuse and adaptation permitted | No reuse licence is offered and none is needed for the statutory text itself: under the government edicts doctrine (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)) the text of the General Statutes is uncopyrightable, so reuse and adaptation are free as a matter of US copyright law. The site car... |
| **Delaware** (`us-de`) | 9 | reuse and adaptation permitted | The register makes no copyright claim at all: there is no terms-of-use or copyright page on delcode.delaware.gov, and the only policy link in the site chrome is the Delaware.gov portal privacy policy. Delaware has instead legislated for the electronic Code's official status by adopting the Uniform E... |
| **District of Columbia** (`us-dc`) | 9 | reuse and adaptation permitted | Open. The Council's own site states flatly that the material is in the public domain, on every page footer, and offers bulk HTML and XML downloads - so reuse AND adaptation are permitted. This matches the US government edicts doctrine (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)): the text o... |
| **Florida** (`us-fl`) | 6 | reuse and adaptation permitted | The site asserts a blanket copyright in its footer — 'Copyright © 1995-2026 The Florida Legislature' — but that claim cannot reach the statutory text: under the government edicts doctrine (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)) the text of the Florida Statutes is uncopyrightable, so re... |
| **Georgia** (`us-ga`) | 9 | reuse and adaptation permitted | This is the code that was at issue in Georgia v. Public.Resource.Org, 590 U.S. 255 (2020), where the Supreme Court held that the whole O.C.G.A. — the statutory text and the annotations prepared by LexisNexis under the Code Revision Commission's supervision — is uncopyrightable under the government e... |
| **Hawaii** (`us-hi`) | 9 | not established | Not open. The State of Hawaii's terms of access and use, which by their own definition apply to every official state site whose address contains 'hawaii.gov' (so, to the Legislature's HRS site), bar automated access entirely and bar commercial duplication, and say nothing permitting adaptation. That... |
| **Idaho** (`us-id`) | 0 | not established | Not verified. The register's own copyright and terms pages could not be fetched (see access_notes), so no licence statement was read and none is asserted. As a matter of US law the text of Idaho's statutes is very likely not copyrightable at all (government edicts doctrine, Georgia v. Public.Resourc... |
| **Illinois** (`us-il`) | 0 | not established | Not verified. The General Assembly's own copyright and disclaimer pages could not be fetched (see access_notes), so no licence statement was read. Under the government edicts doctrine (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)) the text of the Illinois Compiled Statutes is very likely not ... |
| **Indiana** (`us-in`) | 8 | reuse and adaptation permitted | No copyright notice, licence or terms-of-use statement appears anywhere on the register: the footer of iga.in.gov ends with the Statehouse address and no copyright line, and a scan of the site's FAQ page for the words copyright, reproduce, public domain and terms of use returned nothing. The statute... |
| **Iowa** (`us-ia`) | 9 | reuse and adaptation permitted | The register asserts no copyright over the Iowa Code and publishes no licence: the only statement is a disclaimer about accuracy plus a pointer to the official edition, and the separate 'Official and Unofficial Editions' page explains the UELMA designation scheme under Iowa Code ch. 2B rather than r... |
| **Kansas** (`us-ks`) | 8 | reuse and adaptation permitted | Kansas does assert copyright, unusually plainly for a US register: every statute page ends with a Revisor notice and the site footer claims all rights reserved, and the Kansas.gov portal policies claim the compilation of site content as the property of the Information Network of Kansas. Those assert... |
| **Kentucky** (`us-ky`) | 9 | not established | The register asserts blanket copyright in its footer ('Copyright Kentucky Legislative Research Commission / All rights Reserved') and the statute pages add that catchlines and headings are not part of the law. The formal Disclaimers page is 403 to scripted access, so the full terms could not be read... |
| **Louisiana** (`us-la`) | 0 | not established | NOT VERIFIED. The register's own terms and copyright page could not be reached (see access_notes), so nothing is asserted here. What can be said without reading the site: under the government edicts doctrine (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)) the text of the Louisiana Revised Stat... |
| **Maine** (`us-me`) | 9 | reuse and adaptation permitted | The Office of the Revisor of Statutes asserts no copyright anywhere on the statutes pages - there is no copyright line in the footer and no terms-of-use or permissions page; the only notices are a currency statement, a warning that the text may change without notice, and a disclaimer that the office... |
| **Manitoba** (`ca-mb`) | 10 | not established | Crown copyright, Province of Manitoba - and there are two notices that do not say the same thing, which matters here. The Manitoba Laws-specific notice is purpose-limited: copies of all or part of any Act or regulation may be made free and without permission only for study or research, or for use in... |
| **Maryland** (`us-md`) | 9 | reuse and adaptation permitted | The Maryland General Assembly's site makes no copyright, ownership, reuse or terms-of-use assertion at all: the footer carries only Accessibility and Privacy Notice links, the Privacy Notice is purely about data collection and says nothing about content reuse, and no statute page bears a copyright l... |
| **Massachusetts** (`us-ma`) | 0 | not established | NOT VERIFIED. The register's own pages, including any terms or copyright notice, could not be reached (see access_notes), so nothing is asserted here from first-hand reading. What can be said without reading the site: under the government edicts doctrine (Georgia v. Public.Resource.Org, 590 U.S. 255... |
| **Michigan** (`us-mi`) | 0 | not established | Not established. The Michigan Legislature's copyright/terms page could not be reached (CloudGuard WAF block), so nothing is quoted here. Independently of the site's terms, the text of the Michigan Compiled Laws is a government edict and is not subject to copyright under Georgia v. Public.Resource.Or... |
| **Minnesota** (`us-mn`) | 9 | reuse and adaptation permitted | No copyright is asserted over Minnesota Statutes on the register. The chapter and section pages carry no copyright notice, there is no terms-of-use or copyright page (/copyright/ returns 404), and the 'About Minnesota Statutes' page addresses only official/authentic status, not reuse. The Revisor's ... |
| **Mississippi** (`us-ms`) | 8 | not established | Not open. Mississippi is the strongest copyright assertion of the group: the Secretary of State states that the laws of Mississippi are copyrighted by the State of Mississippi, citing Miss. Code Ann. s. 1-1-9, and that section (seen in the code's own search results) provides that copyright in the Mi... |
| **Missouri** (`us-mo`) | 0 | not established | Not established - the Revisor of Statutes site, which carries any terms or copyright statement, is unreachable from here, so nothing is quoted. Background for the human who re-checks: RSMo is compiled by the Committee on Legislative Research's Revisor of Statutes (a legislative office, not a commerc... |
| **Montana** (`us-mt`) | 9 | reuse and adaptation permitted | Open in practice. The Montana Code Annotated is prepared and published by the Legislature's own Legislative Services Division, with no commercial publisher in the chain for the free web edition. I found no copyright notice anywhere on the MCA site and no terms-of-use or copyright page (all candidate... |
| **Nebraska** (`us-ne`) | 0 | not established | Not verified - the register's own copyright/terms page could not be reached (see access_notes), so no quotation is possible. As a matter of law, the text of the Nebraska Revised Statutes is a government edict and is not subject to copyright (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)); Nebr... |
| **Nevada** (`us-nv`) | 0 | not established | Not verified - the register blocked all access (see access_notes), so its own copyright/terms wording could not be read or quoted. As a matter of law the text of the Nevada Revised Statutes is a government edict and not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). Nevada is, ... |
| **New Brunswick** (`ca-nb`) | 0 | not established | NOT VERIFIED. New Brunswick asserts Crown copyright in its legislation through the King's Printer for New Brunswick, and the reproduction terms are published on laws.gnb.ca / gnb.ca, but that host could not be reached at all (HTTP 403 to fetches; an unresolving bot-verification interstitial in a rea... |
| **New Hampshire** (`us-nh`) | 0 | not established | Not verified - the register returned 403 for every request (see access_notes), so its own copyright/terms wording could not be read or quoted. As a matter of law the text of the New Hampshire Revised Statutes Annotated is a government edict and not copyrightable (Georgia v. Public.Resource.Org, 590 ... |
| **New Jersey** (`us-nj`) | 0 | not established | Not verified - neither the Legislature's register nor the State Library mirror would serve content (see access_notes), so no terms could be read or quoted. As a matter of law the text of the New Jersey Statutes is a government edict and not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255... |
| **New Mexico** (`us-nm`) | 9 | not established | Not an open licence. The New Mexico Compilation Commission, a state agency, compiles and publishes NMSA 1978 and asserts all rights reserved over its publications; nothing on nmonesource.com or nmcompcomm.us grants reuse, and nothing grants adaptation. The statutory text itself, however, is a govern... |
| **Newfoundland and Labrador** (`ca-nl`) | 9 | not established | Crown copyright. The consolidations carry 'Copyright (c) <year>: Queen's Printer, St. John's, Newfoundland and Labrador, Canada' (2006 on older consolidations, 2020 on newer ones). The House of Assembly's Copyright and Privacy Statement grants permission to excerpt and cite web content for use in ed... |
| **North Carolina** (`us-nc`) | 0 | not established | UNVERIFIED - the register's own copyright/terms page could not be read (403 Forbidden). As a matter of US law the text of the North Carolina General Statutes is not copyrightable: under the government edicts doctrine confirmed in Georgia v. Public.Resource.Org, 590 U.S. 255 (2020), works produced by... |
| **North Dakota** (`us-nd`) | 9 | reuse and adaptation permitted | The register carries no terms of use and no permission or reuse statement. Its only legal page is a bare accuracy disclaimer, and the footer renders a script-generated site-wide notice 'Copyright (c) <current year> North Dakota Legislative Council' - a blanket website notice, not a claim over the st... |
| **Northwest Territories** (`ca-nt`) | 9 | not established | Not open. Crown copyright in right of the Government of the Northwest Territories is asserted over the whole site, legislation included, and the terms grant only non-commercial reproduction with acknowledgement. Commercial use or reproduction requires prior written consent from the Department of Jus... |
| **Nova Scotia** (`ca-ns`) | 9 | not established | Crown copyright in right of the Province of Nova Scotia. The Government of Nova Scotia's copyright terms permit reproduction for non-commercial purposes without further permission, but only on conditions that include identifying the Government of Nova Scotia as the source, acknowledging Crown copyri... |
| **Nunavut** (`ca-nu`) | 9 | not established | Not open, though more permissive in tone than most. The Department of Justice states that, to ensure access to the laws of Nunavut, the statutes and regulations, their consolidations, and the carried-over NWT statutes and regulations as adopted for Nunavut 'may be copied freely for personal use', wi... |
| **Ohio** (`us-oh`) | 0 | not established | UNVERIFIED - the register's own copyright/terms page could not be reached at all. As a matter of US law the text of the Ohio Revised Code is not copyrightable: under the government edicts doctrine confirmed in Georgia v. Public.Resource.Org, 590 U.S. 255 (2020), statutory text produced by legislator... |
| **Oklahoma** (`us-ok`) | 8 | reuse and adaptation permitted | The register asserts nothing. No copyright notice, terms of use, disclaimer or reuse restriction appears anywhere on the Oklahoma Legislature site: the titles index, the homepage and the statute search page were each read in full and contain no 'copyright' string and no (c) symbol, and there is no t... |
| **Oregon** (`us-or`) | 0 | not established | UNVERIFIED - the register's own copyright page could not be reached at all. This one needs a human look more than the others, because Oregon is the state with the best-known history of asserting copyright in its statutes: the Legislative Counsel Committee claimed copyright in the ORS (over the numbe... |
| **Pennsylvania** (`us-pa`) | 0 | not established | UNVERIFIED - the register's own terms or copyright page could not be reached at all. As a matter of US law the text of the Pennsylvania Consolidated Statutes is not copyrightable: under the government edicts doctrine confirmed in Georgia v. Public.Resource.Org, 590 U.S. 255 (2020), statutory text pr... |
| **Prince Edward Island** (`ca-pe`) | 0 | not established | NOT VERIFIED. Crown copyright in right of the Province of Prince Edward Island applies to its legislation, but the copyright/terms page is on princeedwardisland.ca, which served a Radware CAPTCHA rather than content, so no terms were read and nothing is quoted. open_licence is false because the perm... |
| **Quebec** (`ca-qc`) | 10 | not established | Crown copyright, and the most restrictive of the four provinces. The Government of Quebec's own copyright page asserts exclusive intellectual-property rights over everything it produces, publishes or distributes and names statutes and regulations explicitly ('que ces documents soient des textes offi... |
| **Rhode Island** (`us-ri`) | 0 | not established | UNVERIFIED - the register's own terms or copyright page could not be reached at all. As a matter of US law the text of the General Laws of Rhode Island is not copyrightable: under the government edicts doctrine confirmed in Georgia v. Public.Resource.Org, 590 U.S. 255 (2020), statutory text produced... |
| **Saskatchewan** (`ca-sk`) | 10 | not established | Crown copyright. The Government of Saskatchewan permits reproduction for non-commercial purposes only, provided the material is reproduced accurately and the reproduction is not represented as an official version. Reproduction for commercial purposes requires advance written permission, and requests... |
| **South Carolina** (`us-sc`) | 8 | reuse and adaptation permitted | Open for the statutory text, by the register's own express permission. The Legislative Council's disclaimer at the head of the Code of Laws index grants copying of the Code text, numbering, history and the Effect of Amendment, Editor's and Code Commissioner's notes from the website without permissio... |
| **South Dakota** (`us-sd`) | 8 | reuse and adaptation permitted | Mixed, and the most restrictive of the three verified jurisdictions in this group. The register's own Disclaimer page (https://sdlegislature.gov/Disclaimer) says nothing about copyright or reuse at all - it is a pure accuracy disclaimer. The operative claim is statutory: SDCL 2-16-8 ('Copyrights of ... |
| **Tennessee** (`us-tn`) | 8 | not established | NOT open on the only reachable source. LexisNexis asserts a blanket prohibition over everything on its sites: its copyright page states that no part of the materials may be copied, reproduced, translated or reduced to machine-readable form, in whole or in part, for any reason, and its General Terms ... |
| **Utah** (`us-ut`) | 0 | not established | NOT VERIFIED. The Utah Code's own terms/copyright page could not be read because le.utah.gov is unreachable from this network, so nothing here is based on the register's own words. What can be said as a matter of law rather than observation: under the US government edicts doctrine (Georgia v. Public... |
| **Vermont** (`us-vt`) | 9 | reuse and adaptation permitted | The Vermont General Assembly's site carries a bare footer notice 'Copyright 2026 State of Vermont. All rights reserved.' and, on every statutes page, the caveat that the online text is 'an unofficial copy of the Vermont Statutes Annotated'. The official compilation is the Vermont Statutes Annotated,... |
| **Virginia** (`us-va`) | 9 | reuse and adaptation permitted | The site footer reads '(c) Copyright Commonwealth of Virginia, <year>. All rights reserved. Site developed by the Division of Legislative Automated Systems (DLAS)', but the Code of Virginia pages themselves carry a narrower and more informative notice: the online database 'excludes material copyrigh... |
| **Washington** (`us-wa`) | 8 | reuse and adaptation permitted | CAUTION - Washington is the one jurisdiction in this group whose register affirmatively asserts copyright in the code itself. The Legislature's disclaimer page states that a user intending to obtain the RCW or the WAC 'for the purpose of selling the same is advised to contact the Washington State St... |
| **West Virginia** (`us-wv`) | 0 | not established | NOT VERIFIED. The West Virginia Code site's own copyright or terms page could not be read, because code.wvlegislature.gov redirects this network to fbi.gov, so nothing here rests on the register's own words. As a matter of law rather than observation: under the US government edicts doctrine (Georgia... |
| **Wisconsin** (`us-wi`) | 0 | not established | NOT VERIFIED - the register's own copyright or terms page could not be reached (see access_notes), so nothing can be quoted, and open_licence is set false as a placeholder rather than as a finding. What can be said without the register: as a matter of law the text of the Wisconsin Statutes is a gove... |
| **Wyoming** (`us-wy`) | 6 | reuse and adaptation permitted | Open in substance, but stated nowhere. The LSO site carries no copyright notice, no terms-of-use page and no licence of any kind - the footer links are Home, About the Legislature, Legislative Service Office, Contact Us, Disclaimer and Privacy Policy, and the Disclaimer page asserts no rights at all... |
| **Yukon** (`ca-yt`) | 0 | not established | UNVERIFIED. Yukon statutes are subject to Crown copyright in right of the Government of Yukon, and the Yukon King's Printer sets the reproduction terms, but I could not reach the register's copyright or terms-of-use page (the whole laws.yukon.ca host is behind a Cloudflare bot challenge), so nothing... |

## Quoted terms, register and language, per jurisdiction

### Alabama -- `us-al` (US)

- **Register**: ALISON - Alabama Legislature Official Information System, Code of Alabama 1975
- **Terms page**: https://alison.legislature.state.al.us/code-of-alabama
- **Acts indexed**: 7
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "© 2026"
- **Language**: English only. Alabama statutes are enacted and published in English; there is no second authentic language version.

### Alaska -- `us-ak` (US)

- **Register**: Alaska State Legislature, BASIS - Alaska Statutes (Legislative Affairs Agency)
- **Terms page**: https://akleg.gov/disclaimer.php
- **Acts indexed**: 8
- **Agent's reading**: not established
- **Quoted**: "To obtain permission to reproduce the information (text or graphics) contained on the Alaska Legislature web site, send an email to: webmaster@akleg.gov. The Alaska Legislature should be given credit and provided a copy of the final product."
- **Language**: English only. The Alaska Statutes are enacted and published in English; there is no second authentic language version.

### Alberta -- `ca-ab` (Canada)

- **Register**: Alberta King's Printer - Laws Online / Catalogue
- **Terms page**: https://kings-printer.alberta.ca/copyright.cfm
- **Acts indexed**: 9
- **Agent's reading**: not established
- **Quoted**: "Alberta King's Printer permits any person to reproduce Alberta's statutes and regulations without seeking permission and without charge, provided due diligence is exercised to ensure the accuracy of the materials produced, and copyright is acknowledged"
- **Language**: English only. Alberta enacts and publishes its statutes in English; the King's Printer catalogue carries no French version of any Act indexed here, and no rule of bilingual equal authority applies.

### Arizona -- `us-az` (US)

- **Register**: Arizona State Legislature - Arizona Revised Statutes
- **Terms page**: https://www.azleg.gov/arsDetail/?title=23
- **Acts indexed**: 10
- **Agent's reading**: not established
- **Quoted**: "This online version of the Arizona Revised Statutes is primarily maintained for legislative drafting purposes and reflects the version of law that is effective on January 1st of the year following the most recent legislative session. The official version of the Arizona Revised Statutes is published by Thomson Reuters."
- **Language**: English only. Arizona statutes are enacted and published in English; there is no second authentic language version.

### Arkansas -- `us-ar` (US)

- **Register**: Arkansas Code Annotated - Code of Arkansas Public Access (LexisNexis, for the Arkansas Bureau of Legislative Research / Arkansas Code Revision Commission)
- **Terms page**: https://www.lexisnexis.com/terms/general.aspx
- **Acts indexed**: 7
- **Agent's reading**: not established
- **Quoted**: "Copyright © 2026 LexisNexis."
- **Language**: English only. Arkansas statutes are enacted and published in English; there is no second authentic language version.

### Colorado -- `us-co` (US)

- **Register**: Colorado Legal Resources - Colorado Revised Statutes Annotated (LexisNexis, under contract to the Committee on Legal Services of the Colorado General Assembly)
- **Terms page**: https://www.lexisnexis.com/terms/general.aspx
- **Acts indexed**: 8
- **Agent's reading**: not established
- **Quoted**: "Colorado law recognizes that persons, agencies, or political subdivisions, other than the General Assembly, may seek to publish, reprint, or distribute the statutes of the state of Colorado, in print format, digital format, or both. See § 2-5-118, C.R.S. Any person, agency, or political subdivision seeking to publish, reprint, or distribute the Colorado Revised Statutes by using the statutory database containing the official text of the statutes as prepared by the General Assembly should contact the Office of Legislative Legal Services for further information."
- **Language**: English only. Colorado statutes are enacted and published in English; there is no second authentic language version.

### Connecticut -- `us-ct` (US)

- **Register**: Connecticut General Assembly — General Statutes of Connecticut (prepared under the direction of the Legislative Commissioners' Office)
- **Terms page**: https://www.cga.ct.gov/asp/menu/disclaimer.asp
- **Acts indexed**: 8
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "These documents are not official copies and should not be quoted or cited. The official copy is the paper copy, which may be obtained from the Legislative Bill Room in the Legislative Office Building (Room 1210)."
- **Language**: English is the sole official language of the statutes; Connecticut publishes no other language version.

### Delaware -- `us-de` (US)

- **Register**: The Delaware Code Online (Delaware General Assembly, Division of Research)
- **Terms page**: https://delcode.delaware.gov/title1/c004/index.html
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "This chapter applies to all legal material in an electronic record that is designated as official under § 403 of this title and first published electronically on or after October 21, 2014."
- **Language**: English is the sole official language of the statutes; Delaware publishes no other language version.

### District of Columbia -- `us-dc` (US)

- **Register**: D.C. Law Library - Code of the District of Columbia (Council of the District of Columbia, published with the non-profit Open Law Library)
- **Terms page**: https://code.dccouncil.gov/
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "The codes and laws on this website are in the public domain."
- **Language**: English is the sole language of the Code of the District of Columbia. D.C. laws are enacted and codified in English only; there is no second authentic language version.

### Florida -- `us-fl` (US)

- **Register**: Online Sunshine — The Florida Legislature, The 2026 Florida Statutes
- **Terms page**: http://www.leg.state.fl.us/cgi-bin/View_Page.pl?File=privacy.html&Directory=welcome/&Location=app&Tab=info_center&Submenu=4
- **Acts indexed**: 6
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "Copyright © 1995-2026 The Florida Legislature"
- **Language**: English is the sole official language of the statutes; Florida's Constitution, art. II, § 9, makes English the official language of the State.

### Georgia -- `us-ga` (US)

- **Register**: Official Code of Georgia Annotated, public access edition — published for the Georgia Code Revision Commission by LexisNexis (linked from the Georgia General Assembly site as 'Georgia Code')
- **Terms page**: https://www.lexisnexis.com/terms/copyright.aspx
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "No part of the materials including graphics or logos, available in this Web site may be copied, photocopied, reproduced, translated or reduced to any electronic medium or machine-readable form, in whole or in part, for any reason."
- **Language**: English is the sole official language of the statutes; Georgia publishes no other language version.

### Hawaii -- `us-hi` (US)

- **Register**: Hawaii Revised Statutes, published by the Hawaii State Legislature (Legislative Reference Bureau, Revision of Statutes Division)
- **Terms page**: https://portal.ehawaii.gov/page/terms-of-use/
- **Acts indexed**: 9
- **Agent's reading**: not established
- **Quoted**: "You specifically agree not to access, or attempt to access, or allow any employee, agent or contractor to access or attempt to access any of the Services through any automated means (including, but not limited to, use of scripts, web crawlers or screen scrapers) and shall ensure that you and your agents, employees and contractors comply with the instructions set out in any robots.txt file present on the site."
- **Language**: Hawaiian and English are both official languages of the State (Haw. Const. art. XV, § 4), but that article provides that Hawaiian is required for public acts and transactions only as provided by law, and the Hawaii Revised Statutes are enacted and published in English. English is therefore the authentic language of the statutes.

### Idaho -- `us-id` (US)

- **Register**: Idaho Legislature - Idaho Statutes (Legislative Services Office)
- **Terms page**: https://legislature.idaho.gov/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(nothing quoted: the register returned no HTTP response, so its terms were never read)"
- **Language**: Not verified on the register. Idaho enacts and publishes its statutes in English only; there is no second authentic language version.

### Illinois -- `us-il` (US)

- **Register**: Illinois General Assembly - Illinois Compiled Statutes (ILCS)
- **Terms page**: https://www.ilga.gov/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(nothing quoted: the register returned no HTTP response, so its terms were never read)"
- **Language**: Not verified on the register. Illinois enacts and publishes its statutes in English only; there is no second authentic language version.

### Indiana -- `us-in` (US)

- **Register**: Indiana General Assembly - Indiana Code (published by the Legislative Services Agency)
- **Terms page**: https://iga.in.gov/information/faq
- **Acts indexed**: 8
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "FAQ Archives (2000 - 2013) Publications Agency Reports Portal Accessibility Site Map Contact Us Administrative Code Indiana Legislator Database IN.gov Find an Agency Indiana Statehouse 200 W Washington St. Indianapolis, IN. 46204 (317) 233-5293 (the complete footer of the register, verbatim: there is no copyright or terms line to quote)"
- **Language**: English is the sole language of the Indiana Code; there is no second authentic language version.

### Iowa -- `us-ia` (US)

- **Register**: Iowa Legislature - Iowa Code (Legislative Services Agency)
- **Terms page**: https://www.legis.iowa.gov/law/disclaimer
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "Although the accuracy and timeliness of the information provided is excellent, some information is provisional and all information is provided 'as is' and without any express or implied warranty."
- **Language**: English is the sole language of the Iowa Code; there is no second authentic language version.

### Kansas -- `us-ks` (US)

- **Register**: Kansas Statutes on the Kansas Legislature's site (statutes compiled by the Office of Revisor of Statutes)
- **Terms page**: https://portal.kansas.gov/portal-policies/
- **Acts indexed**: 8
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "(c) 2026 Revisor of Statutes, State of Kansas - and, in the site footer, (c) 2026 Kansas State Legislature. All rights reserved. The Kansas.gov portal policies add: The compilation (meaning the collection, arrangement and assembly) of all content on this site is the exclusive property of INK."
- **Language**: English is the sole language of the Kansas Statutes; there is no second authentic language version.

### Kentucky -- `us-ky` (US)

- **Register**: Kentucky Revised Statutes, Legislative Research Commission (official)
- **Terms page**: https://legislature.ky.gov/policies-security/Pages/Disclaimers.aspx
- **Acts indexed**: 9
- **Agent's reading**: not established
- **Quoted**: "Copyright Kentucky Legislative Research Commission All rights Reserved"
- **Language**: English is the sole official language of the Kentucky Revised Statutes; no other language version is authoritative.

### Louisiana -- `us-la` (US)

- **Register**: Louisiana State Legislature - Louisiana Laws (Revised Statutes, Civil Code, Constitution), official register of the Legislature
- **Terms page**: https://legis.la.gov/legis/Home.aspx
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(no quote - the register's terms page returned ECONNREFUSED on every attempt and was never read)"
- **Language**: English is the sole official language of the current Louisiana Revised Statutes and Civil Code. Louisiana is a mixed civil-law jurisdiction and its earlier codes (notably the Digest of 1808 and the Civil Code of 1825) were promulgated in both French and English, with the French text historically treated as controlling for those editions; the 1870 revision and everything since is English only. Not confirmed against the register in this round.

### Maine -- `us-me` (US)

- **Register**: Maine Revised Statutes, Office of the Revisor of Statutes (official)
- **Terms page**: https://legislature.maine.gov/statutes/
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "The text reflects changes made through the First Special Session of the 132nd Maine Legislature, and is current through October 1, 2025. The text is subject to change without notice."
- **Language**: English is the sole official language of the Maine Revised Statutes; no other language version is authoritative.

### Manitoba -- `ca-mb` (Canada)

- **Register**: Manitoba Laws (King's Printer for Manitoba / Legislative Counsel)
- **Terms page**: https://manitoba.ca/legal/mb_laws.html
- **Acts indexed**: 10
- **Agent's reading**: not established
- **Quoted**: "You may, without charge and without requesting permission, make copies of all or part of any Act or regulation for study or research, or for use in legal proceedings or for providing legal advice. You must not make copies for any other purpose without first obtaining the written consent of King's Printer."
- **Language**: English and French are both official for Manitoba legislation (s. 23 of the Manitoba Act, 1870), and the register says so expressly: 'Only the bilingual version of an Act on the Manitoba Laws website is an official copy of that Act.' The English-only HTML versions linked below are convenience versions; the bilingual PDF is the official one. Some older Acts are still marked '(English version only)' in the consolidation and remain to be re-enacted bilingually.

### Maryland -- `us-md` (US)

- **Register**: Maryland General Assembly - Statute Text (Annotated Code of Maryland), official legislative site
- **Terms page**: https://mgaleg.maryland.gov/mgawebsite/Information/Text/privacy_notice
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "When you use the Maryland General Assembly website, information is collected automatically and voluntarily."
- **Language**: English is the sole official language of the Annotated Code of Maryland; no other language version is authoritative.

### Massachusetts -- `us-ma` (US)

- **Register**: Massachusetts General Court - General Laws of Massachusetts (the Legislature's own register)
- **Terms page**: https://malegislature.gov/Laws/GeneralLaws
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(no quote - the register returned ECONNREFUSED on every attempt and no page of it was ever read)"
- **Language**: English is the sole official language of the General Laws of Massachusetts; no other language version is authoritative. Not confirmed against the register in this round.

### Michigan -- `us-mi` (US)

- **Register**: Michigan Legislature (Michigan Compiled Laws, published by the Legislative Service Bureau / Legislative Council)
- **Terms page**: https://www.legislature.mi.gov/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: (the register states no terms)
- **Language**: English is the sole language of enactment and publication for Michigan statutes.

### Minnesota -- `us-mn` (US)

- **Register**: Minnesota Office of the Revisor of Statutes - Minnesota Statutes (official publisher)
- **Terms page**: https://www.revisor.mn.gov/statutes/info
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "The second official version consists of the online, authenticated PDFs of chapters or sections of Minnesota statutes, which have been designated as official records by the Revisor of Statutes."
- **Language**: English is the sole language of enactment and publication; there is no second authentic language version.

### Mississippi -- `us-ms` (US)

- **Register**: Mississippi Code of 1972 Annotated - 'Mississippi Code Public Access', hosted on LexisNexis Advance for the Joint Legislative Committee on Compilation, Revision and Publication of Legislation (linked as the code source by both the Mississippi Legislature and the Secretary of State)
- **Terms page**: https://www.sos.ms.gov/publications-external-affairs/mississippi-law
- **Acts indexed**: 8
- **Agent's reading**: not established
- **Quoted**: "the laws of Mississippi are copyrighted by the State of Mississippi"
- **Language**: English is the sole language of enactment and publication; there is no second authentic language version.

### Missouri -- `us-mo` (US)

- **Register**: Missouri Revisor of Statutes - Revised Statutes of Missouri (RSMo)
- **Terms page**: https://revisor.mo.gov/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: (the register states no terms)
- **Language**: English is the sole language of enactment and publication for Missouri statutes.

### Montana -- `us-mt` (US)

- **Register**: Montana Code Annotated, published by the Legislative Services Division of the Montana Legislature
- **Terms page**: https://mca.legmt.gov/bills/mca/index.html
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "The Internet version of the Montana Code Annotated is provided as a research tool to users of the Code. In case of inconsistencies resulting from omissions or other errors, the printed version will prevail."
- **Language**: English is the sole language of enactment and publication; there is no second authentic language version.

### Nebraska -- `us-ne` (US)

- **Register**: Nebraska Legislature - Nebraska Revised Statutes
- **Terms page**: https://nebraskalegislature.gov/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: (the register states no terms)
- **Language**: English is the sole language of the statutes; Nebraska has designated English as its official language (Neb. Const. art. I, sec. 27). Not verified against the register in this session.

### Nevada -- `us-nv` (US)

- **Register**: Nevada Legislature (Legislative Counsel Bureau) - Nevada Revised Statutes
- **Terms page**: https://www.leg.state.nv.us/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "Sorry, you have been blocked / You are unable to access leg.state.nv.us"
- **Language**: English is the sole language of the statutes. Not verified against the register in this session.

### New Brunswick -- `ca-nb` (Canada)

- **Register**: New Brunswick Acts and Regulations / Lois et reglements du Nouveau-Brunswick (Office of the Attorney General; King's Printer for New Brunswick)
- **Terms page**: https://laws.gnb.ca/en/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(no quote available: the register's terms page could not be retrieved - see access_notes)"
- **Language**: New Brunswick is the only officially bilingual province, and BOTH language versions of its statutes are official and equally authoritative: English and French have equality of status under sections 16(2) to 18(2) of the Constitution Act, 1982, and under the provincial Official Languages Act, SNB 2002, c. O-0.5, so neither version is a mere translation of the other for interpretive purposes. The register accordingly publishes every Act in parallel English (/en/) and French (/fr/) versions. This is recorded from the constitutional and statutory position rather than from the register itself, which could not be reached - see access_notes.

### New Hampshire -- `us-nh` (US)

- **Register**: New Hampshire General Court - New Hampshire Revised Statutes Annotated
- **Terms page**: https://www.gencourt.state.nh.us/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: (the register states no terms)
- **Language**: English is the sole language of the statutes. Not verified against the register in this session.

### New Jersey -- `us-nj` (US)

- **Register**: New Jersey Legislature - New Jersey Statutes (NJSA)
- **Terms page**: https://www.njleg.state.nj.us/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: (the register states no terms)
- **Language**: English is the sole language of the statutes. Not verified against the register in this session.

### New Mexico -- `us-nm` (US)

- **Register**: New Mexico Compilation Commission - NM OneSource (Current New Mexico Statutes Annotated 1978)
- **Terms page**: https://www.nmcompcomm.us/scope-of-coverage-2/
- **Acts indexed**: 9
- **Agent's reading**: not established
- **Quoted**: "© Copyright New Mexico Compilation Commission All Rights Reserved"
- **Language**: English. New Mexico has no statutorily designated official language, and NMSA 1978 is compiled and published in English only; the English text on NM OneSource is the official text. The New Mexico Constitution's provision for publishing laws in Spanish as well as English (art. XX, sec. 12) was a time-limited transitional provision and does not make a Spanish version of the current statutes authoritative.

### Newfoundland and Labrador -- `ca-nl` (Canada)

- **Register**: House of Assembly of Newfoundland and Labrador - Statutes and Subordinate Legislation (consolidations prepared by the Office of the Legislative Counsel, Department of Justice)
- **Terms page**: https://www.assembly.nl.ca/CopyrightPrivacyStatement.aspx
- **Acts indexed**: 9
- **Agent's reading**: not established
- **Quoted**: "No permission to reproduce, adapt or distribute this copyright material, other than that which is expressly stated above, is to be implied by the availability of the material or images on this site."
- **Language**: English is the sole official language of Newfoundland and Labrador's statutes, and the register publishes them in English only. There is no constitutional or statutory requirement of bilingual enactment as there is in New Brunswick, Quebec or Manitoba.

### North Carolina -- `us-nc` (US)

- **Register**: North Carolina General Assembly - North Carolina General Statutes (Revisor of Statutes)
- **Terms page**: https://www.ncleg.gov/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(none - the register returned HTTP 403 Forbidden for every page, so no verbatim quote could be taken)"
- **Language**: English is the sole official language of the statutes.

### North Dakota -- `us-nd` (US)

- **Register**: North Dakota Legislative Branch - North Dakota Century Code (North Dakota Legislative Council)
- **Terms page**: https://ndlegis.gov/disclaimer
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "We do not warrant the accuracy, reliability, or timeliness of any information available from this site, nor endorse any content, viewpoint, product, or service linked from this site."
- **Language**: English is the sole official language of the statutes.

### Northwest Territories -- `ca-nt` (Canada)

- **Register**: Legislation of the Northwest Territories - the consolidated statutes and regulations service of the Legislation Division, Department of Justice, Government of the Northwest Territories
- **Terms page**: https://www.justice.gov.nt.ca/en/terms-of-use/page/2/
- **Acts indexed**: 9
- **Agent's reading**: not established
- **Quoted**: "Material may not be used or reproduced for commercial purposes without the prior written consent arranged by the Department's Communications Unit. If it is reproduced or redistributed for non-commercial purposes, the Government of the Northwest Territories copyright is to be acknowledged."
- **Language**: The Northwest Territories has eleven official languages, but statutes are authentic in two. Verified on the register's own consolidation of the Official Languages Act, RSNWT 1988, c.O-1: s. 4 provides that 'Chipewyan, Cree, English, French, Gwich'in, Inuinnaqtun, Inuktitut, Inuvialuktun, North Slavey, South Slavey and Tlicho are the Official Languages of the Northwest Territories', and s. 7(1) provides that 'Acts of the Legislature and records and journals of the Legislative Assembly shall be printed and published in English and French and both language versions are equally authoritative.' Every consolidated Act PDF on the register is accordingly bilingual English/French, with the French title and citation printed facing the English on the cover page (e.g. 'EMPLOYMENT STANDARDS ACT / SNWT 2007,c.13' facing 'LOI SUR LES NORMES D'EMPLOI / LTNO 2007, ch. 13'). The other nine official languages have status for services and in the Legislative Assembly, not as authentic versions of the statutes.

### Nova Scotia -- `ca-ns` (Canada)

- **Register**: Nova Scotia Office of the Legislative Counsel - Consolidated Statutes (nslegislature.ca/legc/statutes), UNREACHABLE; title and citation verification fell back to the Government of Nova Scotia Office of the Registrar of Regulations (novascotia.ca/just/regulations)
- **Terms page**: https://www.novascotia.ca/copyright
- **Acts indexed**: 9
- **Agent's reading**: not established
- **Quoted**: "materials must not be modified and the reproduction must be accurate"
- **Language**: English is the sole official language of Nova Scotia's statutes; they are enacted and published in English only. The French-language Services Act provides for provincial services in French but does not make a French version of the statutes authoritative.

### Nunavut -- `ca-nu` (Canada)

- **Register**: Nunavut Legislation website (Consolidated Law of Nunavut) - Legislation Division, Department of Justice, Government of Nunavut; official consolidations are published by authority of the Nunavut Territorial Printer under the Legislation Act
- **Terms page**: https://www.nunavutlegislation.ca/en/welcome-nunavut-legislation-website
- **Acts indexed**: 9
- **Agent's reading**: not established
- **Quoted**: "There is no requirement to seek permission and there are no fees to be paid for reproductions of the statutes and regulations for personal use. The electronic versions of the statutes and regulations may not be copied for the purpose of resale in this or any other form without the written consent of the Territorial Printer."
- **Language**: Three official languages, but only two authentic statute versions by default. Verified on the register's own Official Consolidation of the Official Languages Act, C.S.Nu., c.O-20 (in force April 1, 2013, SI-001-2013; current to September 18, 2025): s. 3(1) 'Inuktut, English and French are the Official Languages of Nunavut', and s. 5(1) 'The Acts of the Legislature shall be made, printed and published in English and French and both versions are equally authoritative.' The Inuit language does not automatically carry statute-authenticity: s. 5(2) requires an Inuktitut version of a bill to be available when the bill is introduced, s. 5(3) lets the Commissioner in Executive Council order an Inuktut version of an Act to be published, and s. 5(4) provides that the Legislative Assembly, on the recommendation of the Executive Council, may by resolution designate an Inuktut version of an Act to be authoritative. So Inuktut versions have official status only where so designated, Act by Act. In practice the register offers Francais on essentially every Act page and Inuktitut (and, for some Acts such as the Official Languages Act itself, Inuinnaqtun) on a subset. 'Inuktut' is the current statutory term, substituted for 'the Inuit Language' by S.Nu. 2025, c.22, s.45(1); the companion statute is now the Inuktut Protection Act (formerly the Inuit Language Protection Act).

### Ohio -- `us-oh` (US)

- **Register**: Ohio Laws and Administrative Rules - Ohio Revised Code (Ohio Legislative Service Commission)
- **Terms page**: https://codes.ohio.gov/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(none - every connection to the register was refused at the network layer, so no verbatim quote could be taken)"
- **Language**: English is the sole official language of the statutes.

### Oklahoma -- `us-ok` (US)

- **Register**: Oklahoma Legislature - Oklahoma Statutes (Oklahoma State Legislature, oklegislature.gov)
- **Terms page**: https://www.oklegislature.gov/OSSTATUESTITLE.HTML
- **Acts indexed**: 8
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "The Oklahoma Constitution and Oklahoma Statutes were last updated on November 18th, 2025."
- **Language**: English is the sole official language of the statutes.

### Oregon -- `us-or` (US)

- **Register**: Oregon Revised Statutes (Oregon Legislative Assembly, Legislative Counsel Committee)
- **Terms page**: https://www.oregonlegislature.gov/bills_laws/Pages/ORS.aspx
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(none - every connection to the register was refused at the network layer, so no verbatim quote could be taken)"
- **Language**: English is the sole official language of the statutes.

### Pennsylvania -- `us-pa` (US)

- **Register**: Pennsylvania General Assembly - Pennsylvania Consolidated Statutes and Unconsolidated Statutes (Legislative Reference Bureau)
- **Terms page**: https://www.palegis.us/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(none - every connection to the register was refused at the network layer, so no verbatim quote could be taken)"
- **Language**: English is the sole official language of the statutes.

### Prince Edward Island -- `ca-pe` (Canada)

- **Register**: Prince Edward Island Acts and Regulations (Legislative Counsel Office, Department of Justice and Public Safety)
- **Terms page**: https://www.princeedwardisland.ca/en/information/copyright
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(no quote available: the register's terms page could not be retrieved - see access_notes)"
- **Language**: English is the sole official language of Prince Edward Island's statutes; they are enacted and published in English. The French Language Services Act provides for provincial services in French but does not make a French version of the statutes authoritative. Recorded from the statutory position rather than from the register, which could not be reached - see access_notes.

### Quebec -- `ca-qc` (Canada)

- **Register**: LegisQuebec - Recueil des lois et des reglements du Quebec (Editeur officiel du Quebec / Publications du Quebec)
- **Terms page**: https://www.quebec.ca/droit-auteur
- **Acts indexed**: 10
- **Agent's reading**: not established
- **Quoted**: "Il est interdit de reproduire, telecharger, stocker, traduire, adapter, publier ou representer en public les contenus du gouvernement du Quebec sans autorisation prealable."
- **Language**: French and English are both official. Section 133 of the Constitution Act, 1867 requires Quebec's Acts to be printed and published in both languages, and s. 7 of the Charter of the French language provides that the French and English versions of statutes and regulations are equally authoritative; LegisQuebec publishes both and the RLRQ chapter number is the same in each. French titles are given below with their official English equivalents. Neither text is subordinate to the other.

### Rhode Island -- `us-ri` (US)

- **Register**: Rhode Island General Assembly - General Laws of Rhode Island (Office of Legislative Data Systems)
- **Terms page**: https://webserver.rilegislature.gov/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "(none - every connection to the register was refused at the network layer, so no verbatim quote could be taken)"
- **Language**: English is the sole official language of the statutes.

### Saskatchewan -- `ca-sk` (Canada)

- **Register**: Office of the King's Printer for Saskatchewan - Publications Centre (Freelaw)
- **Terms page**: https://www.saskatchewan.ca/copyright
- **Acts indexed**: 10
- **Agent's reading**: not established
- **Quoted**: "Unless otherwise noted, materials may be reproduced for non-commercial purposes. The materials must be reproduced accurately, and the reproduction must not be represented as an official version."
- **Language**: English. Saskatchewan's consolidated statutes are published in English; every King's Printer product record retrieved for the Acts below carried a null 'nameFrench', and the register offers no French consolidation of them.

### South Carolina -- `us-sc` (US)

- **Register**: South Carolina General Assembly - South Carolina Code of Laws (South Carolina Legislative Council / Legislative Services Agency)
- **Terms page**: https://www.scstatehouse.gov/code/statmast.php
- **Acts indexed**: 8
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "The South Carolina Code, consisting only of Code text, numbering, history, and Effect of Amendment, Editor's, and Code Commissioner's notes may be copied from this website at the reader's expense and effort without need for permission."
- **Language**: English is the sole official language of the statutes.

### South Dakota -- `us-sd` (US)

- **Register**: South Dakota Legislature - South Dakota Codified Laws (Legislative Research Council)
- **Terms page**: https://sdlegislature.gov/Disclaimer
- **Acts indexed**: 8
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "The internet version of the South Dakota Codified Laws is made available as a public service. ... In the case of inconsistencies resulting from omissions or other errors, the current printed version of the Code will prevail. [Disclaimer page; the copyright claim itself is statutory - SDCL 2-16-8.1: 'Except as authorized by federal copyright law, no person may print or distribute copyrighted material from the South Dakota Codified Laws']"
- **Language**: English is the sole official language of the statutes.

### Tennessee -- `us-tn` (US)

- **Register**: Tennessee Code Unannotated - Free Public Access (LexisNexis, published under contract with the Tennessee Code Commission)
- **Terms page**: https://www.lexisnexis.com/terms/copyright.aspx
- **Acts indexed**: 8
- **Agent's reading**: not established
- **Quoted**: "No part of the materials including graphics or logos, available in this Web site may be copied, photocopied, reproduced, translated or reduced to any electronic medium or machine-readable form, in whole or in part, for any reason."
- **Language**: English is the sole official language of the statutes.

### Utah -- `us-ut` (US)

- **Register**: Utah State Legislature - Utah Code (le.utah.gov/xcode)
- **Terms page**: https://le.utah.gov/xcode/code.html
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "NOT VERIFIED - no terms page could be fetched; no quote available."
- **Language**: English only. Utah statutes are enacted and published in English; there is no second authentic language version.

### Vermont -- `us-vt` (US)

- **Register**: Vermont Statutes Online - Vermont General Assembly (Office of Legislative Counsel)
- **Terms page**: https://legislature.vermont.gov/home/site-resources/disclaimers
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "The Vermont Statutes Online is an unofficial copy of the Vermont Statutes Annotated that is provided as a convenience."
- **Language**: English only. Vermont statutes are enacted and published in English; there is no second authentic language version.

### Virginia -- `us-va` (US)

- **Register**: Virginia Law Portal - Code of Virginia (Virginia General Assembly, Division of Legislative Automated Systems, for the Virginia Code Commission)
- **Terms page**: https://law.lis.virginia.gov/vacode/
- **Acts indexed**: 9
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "The Code of Virginia online database excludes material copyrighted by the publisher, Michie, a division of Matthew Bender."
- **Language**: English only. Virginia statutes are enacted and published in English; there is no second authentic language version.

### Washington -- `us-wa` (US)

- **Register**: Revised Code of Washington (RCW) - Washington State Legislature / Office of the Code Reviser
- **Terms page**: https://leg.wa.gov/disclaimer/
- **Acts indexed**: 8
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "Any user intending to obtain the Revised Code of Washington or the Washington Administrative Code for the purpose of selling the same is advised to contact the Washington State Statute Law Committee, which claims copyright for both codes"
- **Language**: English only. Washington statutes are enacted and published in English; there is no second authentic language version.

### West Virginia -- `us-wv` (US)

- **Register**: West Virginia Code - West Virginia Legislature
- **Terms page**: https://code.wvlegislature.gov/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: "NOT VERIFIED - no terms page could be fetched; no quote available."
- **Language**: English only. West Virginia statutes are enacted and published in English; there is no second authentic language version.

### Wisconsin -- `us-wi` (US)

- **Register**: Wisconsin State Legislature - Wisconsin Statutes and Annotations (Legislative Reference Bureau)
- **Terms page**: https://docs.legis.wisconsin.gov/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: (the register states no terms)
- **Language**: English is the sole language of the Wisconsin Statutes; they are enacted and published in English only. Not verified against the register in this session.

### Wyoming -- `us-wy` (US)

- **Register**: Wyoming Legislature, Legislative Service Office - Wyoming Statutes (text-only NXT edition)
- **Terms page**: https://wyoleg.gov/Legislature/disclaimer
- **Acts indexed**: 6
- **Agent's reading**: reuse and adaptation permitted
- **Quoted**: "The information obtained from this site is not the official record, nor intended to replace the official record, of the Wyoming Legislature."
- **Language**: English is the sole language of the Wyoming Statutes; they are enacted and published in English only, and there is no second authentic language version.

### Yukon -- `ca-yt` (Canada)

- **Register**: Yukon Legislation (laws.yukon.ca) - the Government of Yukon's official legislation website, maintained by the Legislative Counsel Office, Department of Justice; printed official copies are issued by the Yukon King's Printer
- **Terms page**: https://laws.yukon.ca/
- **Acts indexed**: 0
- **Agent's reading**: not established
- **Quoted**: (the register states no terms)
- **Language**: UNVERIFIED on the register. Yukon's Languages Act (a Yukon statute) recognises English and French, and Yukon's First Nations languages, but I could not reach laws.yukon.ca to confirm what the register itself says about the language(s) in which Acts are enacted and published or whether both language versions are equally authoritative. Note that Yukon is not in the same position as NWT or Nunavut: its Acts are, in practice, enacted and published in English, with French versions provided for some statutes. A human must check this on the register before relying on it.

