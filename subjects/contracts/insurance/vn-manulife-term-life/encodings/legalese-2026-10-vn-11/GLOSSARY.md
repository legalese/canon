# GLOSSARY: Manulife term life product terms (row VN-11)

The bilingual record of this encoding.
Every Vietnamese term below is copied from `../../source/raw/manulife-term-life.txt` and checked to occur there verbatim by `tools/vnsrc.py check`.
"src:N" is line N of that file; "Điều N" is the document's Article N, cited in the L4 as "Art N".
Identifiers are those of the `.l4` modules in this directory; a field is shown with the type that declares it.

## Terms the document defines (Điều 1) or uses as terms of art

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Công ty | `the Company` (`A party`) | Manulife Vietnam, the insurer | Điều 1.1; src:8-12 | Low. "Company" is the document's own capitalised short name. |
| Bên mua bảo hiểm | `the policyholder` (`A party`) | the person or organisation named as policyholder on the contract page | Điều 1.2; src:13-20 | Medium. Literally "the party buying the insurance". "Policyholder" can mean the owner of the policy in common-law usage; here it is the contracting and paying party, who may differ from the insured. |
| Người được bảo hiểm | `The insured` | the person whose life is the subject of the contract | Điều 1.3; src:21-26 | Medium. "The insured" and "the life assured" both fit; the English "insured" can also mean the policyholder in some markets, which this document keeps separate. |
| Tuổi | `the Age of` … `on` … | age at the last birthday | Điều 1.4; src:32-33 | High. Capitalised as a defined term. English "age" does not say last birthday as against nearest birthday; the identifier keeps the capital to mark the definition. |
| Năm Hợp đồng | `contract anniversary number` … `of` … | contract year, counted from the effective date | Điều 1.5; src:34-38 | Low. "Policy year" is the usual English. |
| Ngày kỷ niệm Hợp đồng | `contract anniversary number` … `of` … | contract anniversary | Điều 1.5; src:34-38 | Low. "Policy anniversary". |
| Ngày hiệu lực Hợp đồng | `effective date` (`The contract page`) | the day the contract begins to have effect | Điều 1.5; src:37-43 | High. Defined by reference to signing of the application "and accepted by the Company", which leaves open whether it is the signing or the acceptance day (fork F1). Not the same as the issue date. |
| ngày cấp Hợp đồng bảo hiểm | `issue date` (`The contract page`) | the day the contract was issued | Điều 1.3, 7, 10, 11; src:28, 201, 272, 279 | High. Used as if defined, never defined, and distinct from the effective date (fork F3, finding 4). "Issue date" and "policy date" are both plausible; they differ. |
| Ngày đáo hạn | `maturity date` (`The contract page`) | the day the contract ends | Điều 1.5; src:46-48 | Low. "Maturity" in English suggests a payout; this product pays nothing at maturity. |
| Thời hạn Hợp đồng bảo hiểm | `Art 1.6 — the day falls in the contract term` | the contract term, effective date to maturity date | Điều 1.6; src:54-56 | Low. |
| Trang Hợp đồng | `The contract page` | the contract's data page, where the sum insured, dates and premium plan are written | Điều 1.2, 1.5, 3(a), 5, 16; src:15, 43, 83, 148, 356 | Medium. "Policy schedule", "data page" and "certificate" are all plausible; the document never says what else is on it. |
| Đơn yêu cầu bảo hiểm | `The application` | the application for insurance, with its forms, statements and answers | Điều 1.5, 2, 9, 17; src:40, 58-61, 238, 393 | Low. |
| Hợp đồng bảo hiểm | (the contract; no identifier) | the insurance contract | throughout | Low. |
| Quyền lợi khi tử vong | `Art 3(a) — the death benefit` | the death benefit | Điều 3 a.; src:76-93 | Low. |
| Số tiền bảo hiểm | `sum insured` (`The contract page`) | the sum insured on the contract page or as later approved | Điều 3 a.(i), 3 b., 9; src:83-85, 98, 246-247 | Medium. "Sum insured" and "sum assured" are both used in English; for life cover "sum assured" is the British term. |
| điều khoản bảo hiểm bổ trợ | `rider benefits payable` (`The claim`) | the riders (supplementary terms) whose benefits are added to the death benefit | Điều 2, 3 a.(ii), 3 b.; src:62-63, 89-91, 98-100 | Medium. "Rider" is the market term; "supplementary terms" is closer to the words. |
| phí bảo hiểm chưa đóng | `premiums due and unpaid at the death` (`The premium record`) | premiums not paid, deducted from the death benefit | Điều 3 a.(iii); src:93 | High. "Chưa đóng" is "not yet paid", which can include premiums not yet due (fork F7, finding 13). The field name commits to "due and unpaid". |
| trẻ em | (no identifier) | child | Điều 3 b.; src:95-96 | Medium. Not defined; the table's last row makes it decide nothing. |
| Loại trừ đối với Quyền lợi khi tử vong | `Art 3(c) — the death benefit is excluded for` | exclusions from the death benefit | Điều 3 C.; src:130 | Low. |
| Phạm tội | `resulting directly or indirectly from the insured committing a crime, …` (`The death`) | committing a crime | Điều 3 C.(i); src:137 | High. No subject: "the insured committing a crime" adds a subject the Vietnamese does not have (fork F6, finding 1). "Crime" (tội) is a criminal offence, intended or not (finding 2). |
| cố tình phạm tội hình sự | same field | intentionally committing a criminal offence | Điều 3 C.(i); src:137 | Medium. "Cố tình" is "intentionally" or "deliberately"; only this limb carries it. |
| Hội chứng suy giảm miễn dịch mắc phải | `related to AIDS, an AIDS-related condition (ARC), or HIV infection` (`The death`) | acquired immune deficiency syndrome (AIDS) | Điều 3 C.(ii); src:141-142 | Low for the disease names; high for "do liên quan đến" (related to), whose reach is a judgement (finding 9). |
| chi phí và phí tổn phát sinh hợp lý | `reasonable costs and expenses deducted by the Company` (`The premium record`) | reasonable costs and expenses incurred, deducted from a refund | Điều 3 C., 9, 11; src:172-173, 253-254, 283-284 | Medium. "Hợp lý" is "reasonable"; no criteria are given (finding 7). |
| không có lãi | `the premium refunded, without interest, after the reasonable costs` | without interest | Điều 3 C., 9, 11; src:171-172, 244, 253, 283 | Low. |
| Từ chối tham gia bảo hiểm | `Art 4 — the result of the request to cancel` | refusing to take up the insurance (the free-look period) | Điều 4; src:181 | Medium. Literally "refusal to participate in the insurance"; English "free look" and "cooling-off" are market terms with their own statutory meanings elsewhere. |
| hủy bỏ | `cancelled, and the premium is refunded` (`The result of a request to cancel under Art 4`) | cancel (undo) the contract | Điều 4; src:185 | High. "Hủy bỏ" (cancel, rescind from the start) and "chấm dứt" (terminate, for the future) are different acts; English "cancel" is used for both in insurance (outside knowledge, unverified). |
| hoá đơn thu phí bảo hiểm | `premium receipts returned to the Company` (`A request to cancel under Art 4`) | premium receipts | Điều 4; src:193 | Low. |
| chi phí y tế | `medical expenses the Company paid in assessing the risk` | medical expenses of underwriting | Điều 4; src:190-192 | Low. |
| Kế hoạch đóng phí bảo hiểm | `A premium instalment` | the premium plan on the contract page | Điều 5; src:147-148 | Low. |
| ngày đến kỳ đóng phí | `due date` (`A premium instalment`) | the premium due date | Điều 5; src:153-154, 176 | Low. |
| đại lý | `paid to an agent of the Company` (`A payee of the premium`) | the Company's agent | Điều 5; src:152 | Low. |
| Thời gian gia hạn đóng phí bảo hiểm | `Art 5 — the last day of the grace period for` | the grace period for paying a premium | Điều 5; src:155-158 | High. "Gia hạn" is literally "extension"; read as a grace period after the due date, not a new due date (phrasebook 4.11). |
| mất hiệu lực và chấm dứt | `Art 5 — the contract had lapsed by` … `for non-payment of` … | lapses and terminates | Điều 5; src:161 | Medium. "Mất hiệu lực" (loses effect) is "lapses"; the document pairs it with "chấm dứt" (terminates) and then lets a lapsed contract be reinstated (Điều 14). |
| nửa năm, hàng quý hoặc hàng tháng | `premiums of the policy year not yet due at the death` (`The premium record`) | half-yearly, quarterly or monthly modes of payment | Điều 5; src:168-169 | Low. |
| đồng Việt Nam | `Art 6 — the currency of every payment to or by the Company` | Vietnamese dong (VND) | Điều 6; src:198-199 | Low. |
| cư trú | `resided in Vietnam on the issue date` (`The insured`) | reside | Điều 1.3, 7; src:26-28, 201-203 | Medium. Residence is not defined (habitual residence, registered residence, presence?). |
| đi lại | (no identifier: encoded by absence) | travel | Điều 7; src:204-205 | Low. |
| nghề nghiệp | (no identifier: encoded by absence) | occupation | Điều 7; src:205 | Low. |
| Người thụ hưởng | `a beneficiary` (`A party`), `A beneficiary designation` | beneficiary | Điều 8; src:215-235 | Low. |
| chia đều | `Art 8 — the amounts paid to the beneficiaries, in the order they are named` | divided equally | Điều 8; src:222-224 | Low. |
| giới tính | `sex misstated in it` (`The application`) | sex (as stated in the application) | Điều 9; src:237-242 | Low. |
| khai báo sai | `Age misstated in it`, `sex misstated in it`; `material information not disclosed or misstated` | misstate | Điều 9, 10; src:237, 249, 259 | Medium. Covers innocent and deliberate misstatement alike. |
| Tuổi thực | `true date of birth` (`The insured`) | the true Age | Điều 9; src:250 | Low. |
| vô hiệu | `the Company has treated the contract as void` (`The outcome of a death claim`) | void | Điều 10; src:257-258 | High. "Có quyền xem … là vô hiệu" (has the right to regard as void) makes the contract voidable at the Company's choice, not void by law. |
| tầm quan trọng | `material information not disclosed or misstated` (`The disclosure record`) | material (importance to the insurance) | Điều 10; src:260 | Medium. "Material" is a common-law term of art with tests the Vietnamese does not import. |
| gian lận | `fraud` (`The disclosure record`) | fraud | Điều 10; src:268 | Low. |
| Mặc nhiên thừa nhận Hợp đồng bảo hiểm | `Art 10 — the Company may treat the contract as void` | incontestability (the Company accepts the contract after two years) | Điều 10; src:255-256 | High. Literally "tacit acknowledgement of the contract". "Incontestability" is a US term of art with its own case law. |
| duy trì liên tục | `Art 10 — the day the two years run from` | maintained continuously | Điều 10; src:273 | Low. |
| khôi phục hiệu lực | `date of the most recent reinstatement` (`The premium record`), `An application to reinstate` | reinstatement | Điều 10, 11, 14; src:274, 280, 298-311 | Low. |
| Tự tử | `by suicide` (`The death`) | suicide | Điều 11; src:277-278 | Low. |
| mất trí | (no identifier: not read) | of unsound mind | Điều 11; src:281-282 | Low. |
| chia lãi | `Art 12 — the contract shares in the Company's profits` | participation in profits | Điều 12; src:289-291 | Medium. "Lãi" is both "profit" and "interest"; here profit. |
| Giá trị hoàn lại | `Art 13 — the contract has a surrender value` | surrender value | Điều 13; src:295 | Low. |
| Các quyền lợi không bị tước đoạt | `Art 13 — the contract has non-forfeiture benefits` | non-forfeiture benefits | Điều 13; src:295-296 | Medium. A US actuarial term of art, rendered word for word. |
| sự xem xét của Công ty | `the Company agreed to reinstate` (`An application to reinstate`) | the Company's consideration (its discretion) | Điều 14; src:301 | Medium. "Xem xét" is "consideration" or "review"; the encoding records the decision, not a standard for it. |
| bằng chứng về khả năng có thể bảo hiểm | `evidence of insurability accepted by the Company` (`An application to reinstate`) | evidence of insurability | Điều 2, 10, 14; src:60-61, 262-263, 305 | Low. |
| Ngân hàng Nhà nước Việt Nam | `pay the death benefit with interest at the State Bank of Vietnam's overdue-debt rate` (`An act`) | the State Bank of Vietnam | Điều 14, 16; src:310-311, 382-383 | Low. |
| lãi suất nợ quá hạn | same act | the overdue-debt interest rate | Điều 16; src:381-382 | High. Which published rate this names is not said; the encoding refuses to compute the interest. |
| Chuyển nhượng | `An assignment` | assignment | Điều 15; src:312-334 | Medium. "Chuyển nhượng" is "transfer" or "assignment"; the Law uses "chuyển giao" for transfer of a contract (Law 08/2022/QH15 Art 28). |
| người được chuyển nhượng | `an assignee` (`A party`) | the assignee | Điều 15; src:322-323 | Low. |
| văn bản chuyển nhượng gốc | `original instrument submitted to the Company` (`An assignment`) | the original instrument of assignment | Điều 15; src:327-328 | Low. |
| bằng chứng về tử vong | `proof of death received` (`The claim`) | proof of death | Điều 16; src:339 | Low. |
| sự kiện bảo hiểm | `Art 16 — the last day to claim` | the insured event (here, the death) | Điều 16; src:367, 373-375 | Medium. Not defined in the document; item (iv) says the insured event is "ghi ở Trang Hợp đồng". |
| sự kiện bất khả kháng | `days of force majeure or other objective obstacle` (`The claim`) | force majeure | Điều 16; src:368 | Medium. A Civil Code term (outside knowledge, unverified). |
| trở ngại khách quan | same field | an objective obstacle | Điều 16; src:368-369 | Medium. |
| thương lượng | `settled by negotiation` (`A dispute`) | negotiation | Điều 17; src:391 | Low. |
| tòa án | `Art 17 — the courts the dispute may be taken to` | court | Điều 17; src:392-394 | Low. |
| Thời hiệu khởi kiện | `Art 17 — the last day to bring proceedings` | limitation period for suit | Điều 17; src:395 | Low. |
| Chấm dứt Hợp đồng | `A termination under Art 18` | termination of the contract | Điều 18; src:399-409 | Medium. See "hủy bỏ" above. |
| Tổng giám đốc | `the General Director` (`A signatory for the Company`) | the General Director | Điều 2; src:72 | Low. Often rendered "CEO". |
| Phó Tổng giám đốc | `a Deputy General Director` (`A signatory for the Company`) | a Deputy General Director | Điều 2; src:73 | Low. |

## Types, fields and constants declared in the L4 that render a Vietnamese concept, not listed above

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| có thể nhưng không nhất thiết là Bên mua bảo hiểm | `also the policyholder` (`The insured`) | the insured may be, but need not be, the policyholder | Điều 1.3; src:24-25 | Low. |
| được Bên mua bảo hiểm và Người được bảo hiểm ký | `signed by the policyholder`, `signed by the insured` (`The application`) | signed by the policyholder and the insured | Điều 1.5; src:44-45 | Medium. Says nothing of signing for a child (finding 10). |
| đóng phí bảo hiểm lần đầu | `first premium paid` (`The premium record`) | the first premium was paid | Điều 5; src:151 | Low. |
| đóng đủ | `paid in full on` (`A premium instalment`) | paid in full | Điều 5; src:159-160 | Low. |
| quá hạn | `all overdue premiums paid with the interest the Company set` (`An application to reinstate`) | overdue | Điều 14; src:307 | Low. |
| còn sống | `the insured alive when it was made` (`An assignment`); `made while the insured was alive` (`A change of beneficiary`) | while the insured is alive | Điều 8, 10, 15; src:228, 275-276, 314 | Low. |
| đang có hiệu lực | `the contract in force when it was made` (`An assignment`) | in force | Điều 15; src:315 | Low. |
| thông báo bằng văn bản | `written notice received by the Company` (`An assignment`) | written notice | Điều 15; src:326 | Low. |
| chấp thuận bằng văn bản | `approved by the Company in writing` (`An assignment`) | approved in writing | Điều 15; src:329 | Low. |
| văn bản | `in writing` (`An amendment`, `A change of beneficiary`) | in writing | Điều 2, 8; src:72, 230 | Low. |
| Mối quan hệ của người hoặc những người | `evidence of the claimants' relationship provided` (`The claim`) | the relationship of the claimant or claimants | Điều 16(iii); src:351-352 | Medium. Relationship to whom (the insured? the policyholder?) is not said. |
| Hoàn chỉnh các mẫu đơn từ có liên quan | `the Company's forms completed` (`The claim`) | the Company's forms, completed | Điều 16(ii); src:348-349 | Low. |
| nộp cho Công ty bằng chứng phù hợp về | `proof of age submitted earlier` (`The claim`) | proof of Age already submitted | Điều 16(v); src:361-362 | Low. |
| gần địa chỉ của Bên mua bảo hiểm nhất | `address of the policyholder stated in it` (`The application`) | nearest the policyholder's address | Điều 17; src:392-393 | Low. |
| do hai bên thống nhất lựa chọn | `court chosen by both parties` (`A dispute`) | chosen by the two parties | Điều 17; src:394 | Low. |
| thời điểm phát sinh tranh chấp | `date the dispute arose` (`A dispute`) | when the dispute arose | Điều 17; src:397-398 | Medium. When a dispute "arises" is not defined. |
