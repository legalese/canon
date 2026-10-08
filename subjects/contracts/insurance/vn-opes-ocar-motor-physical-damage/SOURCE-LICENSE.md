# Source licence: Công ty Cổ phần Bảo hiểm OPES (OPES Insurance)

**Terms: undetermined.**

The source is a standard-form insurance document published by Công ty Cổ phần Bảo hiểm OPES (OPES Insurance): private contract terms, not law, and the issuer's text.
No copyright, reproduction or confidentiality notice was found in it (searched on 2026-10-06 for `copyright`, `©`, `bản quyền`, `all rights`, `không được sao chép`, `confidential`: no hit).
Absence of a notice is not a grant, so no licence is claimed.

What this repository does about it:

- the PDF and its `pdftotext` rendering are **not held** here; `source/fetch.sh` fetches them from the publisher and checks the sha256 (ruling of 2026-10-01);
- the encodings quote the clauses they encode, one `-- src:N |` comment line at a time, so a reviewer can check each rule against its text; they do not reproduce the document wholesale;
- if the issuer objects to the quotation, remove the `src:` lines; the rules and tests stand without them.

The encodings are Apache-2.0 (the licence of this repository). That does not extend to the quoted source text.

## Ruling on quotation

Meng, 2026-10-06: "quoting the encoded clauses as short -- src:N | comment lines is acceptable for private insurers' text."
That is a ruling to quote, not a finding that the terms permit it: the licence of the source remains **undetermined** above, and the removal path above stands.
The ruling covers short clause-level lines, one clause at a time. It does not cover reproducing the document; the encoders were told not to, and the lead checks how many `src:` lines each encoding carries against the length of its source before committing.

## Hosting

- `opes-ocar`: opes.com.vn, the insurer's own website (behind a Cloudflare challenge). Downloaded by hand in a browser on 2026-10-06 by Meng (the server returns 403 or a bot challenge to curl); the file name matches the URL's. fetch.sh accepts a file placed at raw/ whose sha256 matches; otherwise it tries curl and says how to place it.
