# GLOSSARY — Vietnamese terms and their English identifiers

Row `legalese-2026-10-vn-26`.
Every Vietnamese term is copied from `../../source/raw/prudential-notes.txt` and checked by `tools/vnsrc.py check`.
"src" is the line of that file; Articles are those of the Rules and Terms unless "notes" says otherwise.
One row for each term the document defines (Articles 1.1-1.25, 2.1-2.3), and for each type, field or constant declared in `pru-nouns.l4` (or elsewhere) that renders a Vietnamese concept.

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Prudential | `Prudential` (in `A party`) | the insurer, a limited liability life insurance company | 1.1, src 110 | none |
| Bên mua bảo hiểm | `the policyholder`, `The policyholder` | the party who applies, signs and pays | 1.2, src 113 | literally "the insurance-buying party"; English "policyholder" also suggests the owner of the policy, which 12.1(e)-(g) bear out, but it is not the insured |
| Người được bảo hiểm | `the insured` | the person whose life and body are covered | 1.3, src 128 | English "the insured" is sometimes used for the policyholder; here it is only the life covered |
| quyền lợi có thể được bảo hiểm | `Article 1.2 — an insurable interest` | the relationship that lets the policyholder insure this person | 1.2, src 117 | the English term of art fits; the fourth bullet ("Người khác, nếu …") is circular in both languages |
| năng lực hành vi dân sự đầy đủ | `with full civil act capacity` | full capacity for civil acts | 1.2, src 114-115 | a civil-law term; "legal capacity" in common law is wider (it includes capacity to have rights) |
| cư trú tại Việt Nam | `residing in Vietnam`, `the insured residing in Vietnam` | resides in Vietnam | 1.2, 1.3, 12.2(d), src 114, 128, 895 | residence, not nationality or domicile; the document does not define it |
| Tuổi bảo hiểm | `age last birthday of someone born … on the date …` | insurance age: the age at the last birthday | 1.4, src 132 | some markets use age nearest birthday for "insurance age"; here it is last birthday |
| Người thụ hưởng | `A beneficiary`, `the designated beneficiary` | the person designated to receive benefits | 1.5, src 135 | low |
| Giấy Chứng nhận bảo hiểm nhân thọ | `original certificate and endorsement letters` | the life insurance certificate | 1.6, 2.1(b), src 143, 299 | "certificate" not "policy": the contract is the set of documents in 2.1 |
| Ngày cấp Giấy chứng nhận bảo hiểm nhân thọ | `date the cover was decided` (Article 3), `received` (Article 4) | the date the certificate issues | 1.6, 3, 4, src 143, 333, 350 | Article 4 counts from receipt, not issue |
| Ngày hiệu lực hợp đồng | `effective date` | the day the application was completed and premium paid in full | 1.7, src 146 | not the issue date: it reaches back to the application, which matters for 11.1(g) |
| Năm hợp đồng | `the contract year of … in which falls …` | a one-year period from the effective date or an anniversary | 1.8, src 151 | "policy year" is the usual English |
| Ngày kỷ niệm năm hợp đồng | `contract anniversary number … of …` | the yearly anniversary of the effective date | 1.9, src 153 | "policy anniversary" |
| Ngày kết thúc thời hạn hợp đồng | `the end of the contract term of` | the last day of the term | 1.10, src 155 | whether the anniversary itself is the last day is fork F-28 |
| Số tiền bảo hiểm | `sum insured` | the amount Prudential accepts to insure, on the certificate | 1.11, src 157 | life-insurance English often says "sum assured"; "sum insured" chosen to match the sibling rows |
| thư xác nhận điều chỉnh hợp đồng | `original certificate and endorsement letters` | a letter confirming an amendment of the contract | 1.11, 2.1(c), src 158, 300 | "endorsement" is the insurance term; the source says "confirmation letter" |
| Phí bảo hiểm | `total premiums paid` | the premium | 1.12, src 160 | low |
| Giá trị hoàn lại | `surrender value` | what the policyholder receives on early termination | 1.13, src 163 | literally "refund value"; "cash value" in US usage |
| Khoản giảm thu nhập đầu tư | `investment income reduction` | the charge for an advance or a late premium | 1.14, src 170 | it works like interest; calling it "interest" would hide its stated basis |
| Khoản nợ | `debts` | unpaid premium, advances and the reduction above | 1.15, src 175 | "debt" suggests an enforceable loan; the source only deducts it |
| Tai nạn | `An accident`, `Article 1.16 — an Accident` | a sudden external event, the sole and direct cause of injury or death | 1.16, src 180-190 | capitalised as a defined term; ordinary "accident" is wider (no sole-cause limb) |
| Thương tật toàn bộ và vĩnh viễn | `A disability`, `Article 1.17 — total and permanent disability` | loss or paralysis of two limbs or eyes, or 81% loss of working capacity | 1.17, src 192 | "thương tật" is both injury and disability; TPD is the usual English |
| mất sức lao động | `loss of working capacity, in percent` | loss of working capacity | 1.17(b), src 206 | a Vietnamese assessment scale, not an English disability percentage |
| Hội đồng giám định y khoa | `confirmed by a provincial-level or higher medical authority or assessment council` | the medical assessment council | 1.17, src 208-209 | institutional; no exact English equivalent |
| Thương tật vĩnh viễn | `A permanent injury`, `Article 1.18 — a permanent injury` | a loss of a body part or a brain injury listed in annex section 1 | 1.18, src 215 | "permanent disability" is also a fair rendering; "injury" chosen to keep it apart from 1.17 |
| Chấn thương sọ não | `brain injury`, `A head injury`, `Article 1.19 — a brain injury` | a severe head injury: a 96-hour coma, or a depressed skull fracture needing surgery | 1.19, src 218 | literally "skull-brain trauma"; medical "traumatic brain injury" is much wider |
| Hôn mê | `continuous coma, in hours` | coma | 1.19, src 220 | low |
| thang điểm hôn mê Glasgow | `Glasgow score of 6 or less throughout 96 hours of hospital treatment` | the Glasgow coma scale | 1.19, src 222-223 | low |
| Gãy xương | `A fracture`, `Article 1.20 — a Fracture` | a complete fracture confirmed by a Doctor on imaging | 1.20, src 240 | narrower than ordinary "fracture" |
| Nứt xương | `a complete break, not a hairline crack or greenstick fracture` | a hairline crack | 1.21, src 244 | "nứt" is crack; "hairline fracture" is the medical English, which ordinary readers may count as a fracture |
| Gãy cành tươi | the same field | a greenstick fracture | 1.22, src 247 | literally "fresh-branch break" |
| Bệnh viện | `A medical facility`, `Article 1.23 — a Hospital` | a facility meeting four conditions, and none of ten listed kinds | 1.23, src 250 | much narrower than ordinary "hospital": a general clinic is not one |
| Khoa chăm sóc đặc biệt | `A care unit`, `Article 1.24 — an intensive care unit` | a hospital unit for intensive care, not a recovery or emergency room | 1.24, src 271 | literally "special care department"; "ICU" is a gloss |
| Bác sĩ | `A medical practitioner`, `Article 1.25 — a Doctor` | a graduate in Western medicine, licensed, not related to the parties | 1.25, src 286 | narrower than "doctor": traditional-medicine practitioners and relatives are excluded |
| Hợp đồng bảo hiểm | (the contract; no identifier) | the set of documents in 2.1(a)-(g) | 2.1, src 297 | the notes are not among them (F-17) |
| Thời hạn hợp đồng | `chosen contract term in years` | the contract term | 2.2, src 307 | low |
| Thời hạn đóng phí | (inert) | the premium-paying term | 2.3, src 312 | low |
| Bảo hiểm tạm thời | `The temporary cover`, `What Article 3 pays` | cover between application and decision | 3, src 314 | "interim cover" or "conditional receipt" elsewhere |
| Thời hạn cân nhắc | `Article 4 — the free look` | the 21-day period to refuse the contract | 4, src 349 | "free-look" or "cooling-off" period; both fit |
| Điều khoản miễn truy xét | `Article 6 — Prudential may still raise the misstatement` | the incontestability clause | 6, src 384 | "incontestability" usually bars rescission for all but fraud; here material misstatements stay contestable (F-15) |
| Hồ sơ yêu cầu bảo hiểm | `The application` | the application for insurance | 1.2, 1.7, src 115, 146 | low |
| phương tiện vận chuyển thương mại công cộng có phép trên bộ | `a ticketed passenger on licensed public commercial land transport on a regular schedule and an established route` | licensed public commercial land transport | 8.1(b), src 424 | "public" and "commercial" together; a private hired car is neither |
| phương tiện hàng không thương mại có phép | `a ticketed passenger on a licensed commercial flight on a regular schedule and an established route` | a licensed commercial flight | 8.1(c), src 429 | low |
| Quà đáo hạn | `Article 8.9 — the maturity benefit` | the maturity benefit | 8.9, src 52, 526 | literally "maturity gift", a marketing word for a contractual benefit |
| Chuyển viện | `transferred to another hospital` | a hospital transfer | 8.6, src 512 | undefined in the source (F-21) |
| Người nhận quyền lợi bảo hiểm | `the claimant`, `A recipient` | whoever receives a benefit | 10.2-10.8, 11.1, src 65, 576 | "claimant" suggests the person who claims; 8.10 gives the right to claim to the insured, who may not be the recipient (F-13) |
| Hồ sơ yêu cầu giải quyết quyền lợi bảo hiểm | `The claim documents`, `Article 10.1 — the claim file is complete` | the claim file | 10.1, src 562 | low |
| Sự kiện bảo hiểm | `the insured event` (parameter) | the insured event | 10.4, 10.6, src 614, 647 | which date it is (accident, injury, death) is not defined |
| bất khả kháng | (the `LEST` of `Article 10.6 — Prudential's duty to resolve the claim`) | force majeure | 10.6, src 652 | low |
| Ngân hàng Ngoại thương Việt Nam | (an input to the interest) | the bank whose deposit rate sets late-payment interest | 10.6, src 655 | glossed "Vietcombank" in comments: outside knowledge, unverified |
| Tạm ứng từ giá trị hoàn lại | `Article 12.1(d) — the most that may be advanced` | an advance (policy loan) from the surrender value | 12.1(d), src 766 | "policy loan" is the usual English; the source says advance |
| Chuyển nhượng | `Article 12.1(e)-(f) — the change has effect on` | assignment of the contract | 12.1(e), src 781 | "transfer" also fits |
| Khôi phục hiệu lực | `A reinstatement request`, `Article 12.1(h) — …` | reinstatement of a lapsed contract | 12.1(h), src 813 | "revival" in some markets |
| Mất hiệu lực | `date the contract last ceased to be in force` | lapse | 15.1, 16, src 949, 963 | the identifier also covers termination, which the source keeps apart |
| thời gian gia hạn đóng Phí bảo hiểm | `Article 15.1 — the last day of the grace period` | the grace period | 15.1, src 951-952 | low |
| liên quan đến | `related to it, but not caused by it` (in `A link to a cause`) | related to | notes item 3, src 60-61 | wider than any causal phrase; the crux of F-11 |
| được gây ra trực tiếp do | `directly caused by it` | directly caused by | 11.1, src 697 | "proximately caused" would import a common-law test |
| trực tiếp hoặc gián tiếp | `directly caused by it`, `indirectly caused by it` | directly or indirectly | 3, src 336 | low |
| Chiến tranh | `war, belligerent acts, rebellion, civil disorder or riot` | war and the like | 11.1(a), notes item 3, src 63, 699 | low |
| Phạm tội | `a crime of the policyholder, the insured or the claimant` | a crime | 11.1(b), 3, notes, src 65, 341, 701 | the Rules and Terms require an authority's conclusion; the notes do not |
| theo kết luận của cơ quan Nhà nước có thẩm quyền | `a competent State authority concluded it was a crime` | as a competent State authority concluded | 11.1(b), 3, src 341, 701 | low |
| Tự tử | `suicide or self-inflicted injury of the insured` | suicide | 11.1(c), 3, notes, src 67, 337, 703 | low |
| hoạt động nguy hiểm | `a dangerous activity of the insured` | a dangerous activity, with examples | 11.1(d), 3, notes, src 69, 343, 705 | the lists are open ("như"), and differ between Article 3 and 11.1 |
| chất gây nghiện | `the influence of addictive substances, psychiatric drugs, alcohol, poison, gas, similar substances or narcotics` | addictive substances | 11.1(e), notes, src 72, 708 | low |
| hành động cố ý | `an intentional act of the policyholder, the insured or the claimant` | an intentional act | 11.1(f), notes, src 76, 712 | whose intent counts for 1.16's "ngoài ý muốn" is not said |
| tình trạng bệnh | `an illness (such as osteoporosis or a bone disease), or medical treatment` | an illness | 11.1(h), notes, src 82, 718 | low |
| Mất cả hai tay | `loss of both hands` | loss of both hands | annex 1, src 1018 | **high**: "tay" is both hand and arm; the annex note "Mất tay được tính từ cổ tay trở lên" (from the wrist up) makes "hand" the narrower and "arm" an equally fair reading |
| Mất cả hai chân | `loss of both legs` | loss of both legs | annex 1, src 1019 | **high**: "chân" is both leg and foot; the note "từ mắt cá chân trở lên" (from the ankle up) |
| Mất một ngón tay cái | `loss of one thumb` | loss of a thumb | annex 1, src 1028 | whether a thumb is also "một ngón tay" is open (F-04) |
| Mất một ngón tay | `loss of one finger` | loss of a finger | annex 1, src 1029 | as above |
| Mất tất cả các ngón trên một bàn tay | `loss of all the fingers of one hand` | loss of all the digits of one hand | annex 1, src 1030 | "các ngón" may or may not include the thumb |
| Mất một ngón chân | `loss of one toe` | loss of a toe | annex 1, src 1031 | low |
| Tràn khí màng phổi | `pneumothorax or haemothorax from external trauma` | pneumothorax | annex 2, src 1039 | low |
| Chấn thương hai thận do cùng một Tai nạn | `injury to both kidneys in the same Accident` | both kidneys in one Accident | annex 2, src 1062 | overlaps the single-kidney row (F-07) |
| Xương cột sống | `the spine, except the coccyx` | the spine | annex 3, src 1064 | low |
| Khuỷu tay | `the elbow` | the elbow, a joint | annex 3, src 1072 | a joint, not a bone, in a table of bones (F-06) |
| Xương cổ tay | `a wrist bone` | a carpal bone | annex 3, src 1073 | low |
| Mắt cá chân | `the ankle` | the ankle, a joint | annex 3, src 1074 | overlaps the tibia and fibula (F-06) |
| Xương sườn | `a rib` | a rib | annex 3, src 1077 | whether several ribs are several rows is fork F-05 |
| Xương cụt | `the coccyx` | the coccyx | annex 3, src 1078 | low |
| phỏng độ 3 | `percent of body skin area with third-degree burns` | third-degree burn | annex 4, src 1091 | "phỏng" is a regional word for burn (outside knowledge, unverified); the degree scale is not defined (F-21) |
