# Source licence: Decree 67/2023/NĐ-CP and Decree 220/2026/NĐ-CP

**Terms: not established by us.**

The sources are a decree of the Government of Vietnam and its amending decree, a normative legal document published in the Government gazette (Công báo).
Legal normative documents are generally outside copyright in Vietnam, but this file does not rely on that and has not verified the provision, so no grant is written here.

What this repository does about it: the gazette PDFs are **not held** here; `source/fetch.sh` fetches them from the gazette's server and checks their sha256 (ruling of 2026-10-01). The encodings quote the provisions they encode one `-- src:N |` line at a time.

The encodings are Apache-2.0.

## Hosting

- `nd67-congbao-1017-1018`: congbaocdn.chinhphu.vn, the Government gazette (Công báo) issue 1017+1018, 20 September 2023: the decree's body and Phụ lục I-III. The server wants a Referer.
- `nd67-congbao-1019-1020`: congbaocdn.chinhphu.vn, the Government gazette (Công báo) issue 1019+1020: the decree's remaining annexes (Phụ lục III continued to X, including Phụ lục VI). The server wants a Referer.
- `nd220-2026-congbao-367`: congbaocdn.chinhphu.vn, the Government gazette (Công báo) no. 367, 3 July 2026: Decree 220/2026/NĐ-CP, which amends Decree 67/2023. The server wants a Referer.
