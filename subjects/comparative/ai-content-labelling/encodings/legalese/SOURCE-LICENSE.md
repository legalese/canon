# Source licence — quoted legal text and fixture files

## Quoted legal text

The modules quote, in comments and field names, Regulation (EU) 2024/1689 and Regulation (EU) 2026/1744 (status **UNDETERMINED**), the Commission's Code of Practice and Guidelines (**DETERMINED: CC BY 4.0, attribution required**), and the Washington and California enactments (**DETERMINED: not subject to copyright**).
The reasons, the Commission's notice quoted verbatim, and what was not checked are in `subjects/comparative/ai-content-labelling/SOURCE-LICENSE.md` in `legalese/canon`.

This file sits in the row as well as beside `source/` because the vendored mirror in `legalese/l4-ide` (`jl4/examples/canon/`) carries each row's `SOURCE-LICENSE.md` and not the subject-level one.

## Fixture files — `fixtures/files/`

- `c2pa-rs-camera-capture.jpg` and `c2pa-rs-colour-adjusted.jpg` are copied unchanged from the test fixtures of `contentauth/c2pa-rs` at commit `518fe03a4a09dd38b68c1c5215d572fb1116bb66`.
  That repository's README, read at the same commit on 2026-10-01: "The `c2pa` crate is distributed under the terms of both the MIT license and the Apache License (Version 2.0)." `LICENSE-MIT` reads "© Copyright 2020 Adobe." **DETERMINED: MIT or Apache-2.0, attribution required**; recorded in the repository `NOTICE`.
  The files are test fixtures inside the crate's repository; the README's statement is taken to cover them, and no separate notice on the fixtures directory was found.
- The other six files were made for this encoding by `fixtures/build-fixtures.sh`. Three (`ai-object-removed.jpg`, `ai-filtered.jpg`, `ai-red-eye-removed.jpg`) are derived from the c2pa-rs camera capture above, which is their parent ingredient, and carry its terms; the other three (`ai-generated.jpg`, `ai-generated-watermark-declared.jpg`, `ai-generated-stripped.jpg`) are built on a flat-colour image the script makes. They are signed with `c2patool`'s built-in test certificate and time-stamped by DigiCert's public time-stamping authority. They are released with the encoding under Apache-2.0.

## The encoding

The **encoding** is licensed under **Apache-2.0**, per the repository `NOTICE`. That licence covers the encoding only.
