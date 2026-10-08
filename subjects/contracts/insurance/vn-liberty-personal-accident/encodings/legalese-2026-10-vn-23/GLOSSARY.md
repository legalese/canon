# GLOSSARY — Liberty personal accident rules (UW-PAG-W-001-10-V), row `legalese-2026-10-vn-23`

The bilingual deliverable.
Every Vietnamese term below occurs verbatim in `../../source/raw/liberty-pa.txt` (checked by `tools/vnsrc.py check`); `src N` is a line of that file.
One row for every term the document defines (ĐỊNH NGHĨA, src 30-304, and the terms defined elsewhere in the text), then the terms behind the types, fields and constants the L4 declares.
Identifiers are the L4 names, in backticks; a row marked "inert" is quoted or cited but no rule reads it.

## Terms the document defines

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Công ty | `the Company` (in `An actor`, `A side to the contract`) | Liberty Insurance Co. Ltd., the insurer | ĐỊNH NGHĨA, src 32 | low |
| Bên mua bảo hiểm | `the policyholder` | the organisation that makes the contract and pays the premium | ĐỊNH NGHĨA src 34; general provision 3(b) src 1161-1164 | medium: literally "the insurance-buying party"; "policyholder" is the market word, but in a group contract the employees hold certificates too. Distinct from the insured throughout. |
| Người được bảo hiểm | `An insured person`, `the insured` | a person the Company has confirmed by issuing a summary naming them | ĐỊNH NGHĨA src 37-39 | medium: in some English markets "the insured" means the policyholder; here it is always the covered person |
| Giấy yêu cầu bảo hiểm | `the application, quotation, renewal notice or renewal quotation` (in `A contract document`) | the application or proposal form | ĐỊNH NGHĨA src 41-44; general provision 1 src 1126 | low ("application" or "proposal") |
| Sửa đổi bổ sung | `an endorsement` | a document the Company issues to amend or supplement the contract | ĐỊNH NGHĨA src 46-48 | medium: literally "amendment-supplement"; "endorsement" is the market word and carries no Vietnamese legal sense of its own |
| Giấy chứng nhận bảo hiểm | `the certificate or the summary` | the certificate of insurance | ĐỊNH NGHĨA src 50-51 | low |
| Bản tóm tắt Hợp đồng bảo hiểm | `The policy schedule`; `the certificate or the summary` | the summary: the period, the programme, the premium and other terms | ĐỊNH NGHĨA src 54-56 | medium: "summary" is literal; the document does the work of an English "schedule", which is the identifier chosen. A reader expecting a mere summary would under-read it. |
| Chương trình bảo hiểm | `the insurance programme` | the plan of benefits that applies to an insured | ĐỊNH NGHĨA src 58-64 | low ("programme" or "plan") |
| Hợp đồng bảo hiểm | (the contract; `A contract document` lists its parts) | the agreement made of the documents in general provision 1 | ĐỊNH NGHĨA src 66-67; general provision 1 src 1118-1130 | low |
| Hạn mức bảo hiểm | `death limit`, `permanent injury limit`, `limit`, `medical expense limit` | the Company's maximum total liability for each insured, in the period, for each section | ĐỊNH NGHĨA src 69-71 | high: "limit" here also does the work of a sum insured (benefit A pays "Hạn mức" on death); 8.4 and 16B speak of "số tiền bảo hiểm" (sum insured) for the same thing |
| Thời hạn bảo hiểm | `first day of the period of insurance`, `last day of the period of insurance`, `the first day of cover for` | the period of insurance, with its deferred start | ĐỊNH NGHĨA src 73-83 | low |
| Sự kiện bảo hiểm | `general provision 13: the day of the insured event for` | the insured event: the event on which the Company must pay | ĐỊNH NGHĨA src 85-86; general provision 13(a) src 1482-1486 | high: which date it names for death and permanent injury is not said (fork F2) |
| Hiệu lực bảo hiểm | `the insured's cover was in force on` | the Company's liability runs from the start to the end of the period unless ended | ĐỊNH NGHĨA src 88-92 | low; defined and not used again by that name |
| Ngày hiệu lực | `the effective date for` | the first day of the insured's period | ĐỊNH NGHĨA src 94-96 | medium: English "effective date" often means the contract date; here it is per insured and moves with the deferred start |
| Năm bảo hiểm | `the first day of the insurance year` | 00:01 on the first day (or issue, if later) to 11:59 pm on the last day, Vietnam time | ĐỊNH NGHĨA src 98-102 | low; never used again (Findings D20) |
| Người phụ thuộc | `a dependant`, `within the definition of a dependant:` | a spouse, a partner living as spouse, or an unmarried child the insured supports, within age limits | ĐỊNH NGHĨA src 104-114 | medium: English "dependant" implies financial dependence; the Vietnamese term is also "dependent person", but a spouse qualifies whether dependent or not |
| Trẻ em vị thành niên | `a minor:` | a child from six months to under 18 | ĐỊNH NGHĨA src 116 | medium: "vị thành niên" ordinarily means any person under 18; here the definition starts at six months |
| Tuổi | `the age of`, `the age at the last birthday, from` | age at the last birthday passed | ĐỊNH NGHĨA src 118-121 | low |
| Quê quán | inert | the country of the insured's passport or identity card | ĐỊNH NGHĨA src 123-128 | high: in ordinary Vietnamese "quê quán" is one's home town or place of origin; the wording gives it the sense of a nationality country |
| Nước thường trú | `resident in Vietnam:` | the country where the person lived when cover began, as declared | ĐỊNH NGHĨA src 130-135 | high: "thường trú" is also a registered-residence status in Vietnamese administrative law (outside knowledge, unverified); the wording defines it by fact and declaration instead |
| Bác sĩ | Doctor (`directed by a Doctor`) | a licensed practitioner acting within training and licence | ĐỊNH NGHĨA src 137-139 | low |
| Cơ sở y tế | Medical Facility (`for professional services of a Doctor at a Medical Facility`) | a licensed hospital, clinic or treatment facility | ĐỊNH NGHĨA src 141-143 | low |
| Tai nạn | Accident (`the limbs of the definition of an Accident, other than the period, are met by`) | a sudden event caused by an external visible force, unintended, the direct and sole cause | ĐỊNH NGHĨA src 145-149 | medium: English "accident" carries none of the five limbs; the sole-cause limb is the one that bites |
| Thương tật | Injury (`the definition of an Injury is met by`) | bodily injury caused solely by an Accident, within the geographical scope | ĐỊNH NGHĨA src 151-154 | high: "thương tật" also means disability (as in a percentage of disability); "Injury" was chosen because the definition is of a bodily harm, not a loss of function |
| Thương tật vĩnh viễn | `A permanent injury`, `benefit A.2, permanent injury` | an Injury in the table, lasting 104 / 52 consecutive weeks without hope of recovery | ĐỊNH NGHĨA src 156-163 | medium: English wordings say "permanent disablement" |
| Thương tật toàn bộ vĩnh viễn | `total permanent injury` | the 104-week class; the first table | src 160, 344 | medium (as above) |
| Thương tật bộ phận vĩnh viễn | `partial permanent injury, the head` (and the limbs) | the 52-week class; the second table | src 163, 359 | medium: "bộ phận" is "part"; the class is of injuries to a part of the body, priced as a fraction |
| Thương tật tạm thời | `The temporary injury claim`, `benefit B, temporary injury` | an Injury that alone disables the insured entirely from their business or occupation for a time | ĐỊNH NGHĨA src 165-168 | medium: the market term is "temporary total disablement"; the "time" in the summary is read as a maximum (fork F5) |
| Đang làm việc | inert | actively at work | ĐỊNH NGHĨA src 170-177 | low; never used again |
| Người lao động | `an employee of the employer` | a person 18 or over working for pay under the employer's management | ĐỊNH NGHĨA src 179-181 | low ("employee" or "worker") |
| Người sử dụng lao động | (the employer, in `an employee of the employer`) | the employer through which the group contract is made | ĐỊNH NGHĨA src 183-186 | low |
| Nhóm | (the group) `the definition of a group: the group may join, formed for insurance:` | employees of an employer, or members of a sponsoring organisation, with dependants | ĐỊNH NGHĨA src 188-195 | low |
| Tổ chức tài trợ | `a member of the sponsoring organisation` | a union or other body accepted as policyholder for its members | ĐỊNH NGHĨA src 197-199 | medium: "tài trợ" is "sponsor" or "fund"; "sponsoring organisation" follows the English market term |
| Ốm đau/Bệnh tật | (illness, in `the injury came from illness, ...`) | a change from the normal state of health | ĐỊNH NGHĨA src 201 | low; misspelt "Ôm đau" once at src 153 |
| Mất thị lực | inert | total, irreversible loss of sight | ĐỊNH NGHĨA src 203-204 | low; never used again (D20) |
| Mất chi | inert | loss of function, or physical loss, from the wrist or ankle upward | ĐỊNH NGHĨA src 206-207 | medium: never used again, so it does not tell the reader whether "một bàn tay" in the table means loss at the wrist |
| Bệnh bẩm sinh | inert | congenital disease, as a Doctor or the law determines | ĐỊNH NGHĨA src 209-215 | low |
| Bệnh di truyền | inert | hereditary disease | ĐỊNH NGHĨA src 217-221 | low |
| Trợ cấp Ngày nằm viện | `daily hospital allowance`, `benefit D, hospital allowance` | the daily allowance for each 24 hours of treatment in a Medical Facility | ĐỊNH NGHĨA src 223-227; benefit D src 518-521 | low |
| Chi phí y tế | `A medical expense`, `benefit C, medical expenses` | costs within 12 months of the Injury for treating it, with the dental exclusions | ĐỊNH NGHĨA src 229-240 | low |
| Thu nhập | `monthly income at the time of the accident` | monthly base salary or fixed wage, without commission, bonus or overtime | ĐỊNH NGHĨA src 242-244 | high: "thu nhập" ordinarily means all income; the definition narrows it to base pay |
| Tình trạng tồn tại trước | `A prior condition`, `a pre-existing condition:` | an illness or injury known, treated or symptomatic before cover | ĐỊNH NGHĨA src 246-259 | low |
| Thông thường và hợp lý | `the reasonable and customary amount` | the charge common among comparable facilities in the locality | ĐỊNH NGHĨA src 261-266 | low (the market term) |
| Cần thiết về mặt y học | (medically necessary, in the 13(b) field) | treatment a Doctor finds appropriate, meeting (a)-(e) | ĐỊNH NGHĨA src 268-278 | low |
| Phân loại nhóm nghề | `An occupation class`: `class 1` to `class 4` | four classes of occupation by manual work and hazard | ĐỊNH NGHĨA src 280-304 | low |
| Hạn mức mỗi chuyến | `the limit per conveyance` | 25.000.000.000 đồng for all insured on one flight, road or rail/boat journey | HẠN MỨC CHUNG src 535-538 | medium: "chuyến" is a trip; the limit is per journey of one conveyance, not per vehicle |
| hành động khủng bố | `an act of terrorism` | force or threat by a person or group for political, religious or ideological ends | general exclusion 2 src 687-692 | low |
| Hiện trạng | (the "Condition" of 5(d), in `the insured knew beforehand that the condition was present`) | intoxication, drugs, alcohol, stimulants, or insanity from natural causes | general exclusion 5(d) src 759-762 | low |
| Rủi ro do năng lượng nguyên tử | (special exclusions 4 and 6, refused by name) | insurance contracts relating to nuclear installations, fuel or material | special exclusion 4 src 897-917; 6 src 1017-1035 | medium: the definition is of classes of insurance business, not of perils |
| Vật liệu Nguyên tử | inert | nuclear fuel (not natural or depleted uranium) and radioactive products or waste | special exclusion 4 src 957-969 | low |
| Đối tượng bảo hiểm | inert | the subject of the insurance: the insured's health | general provision 3(a) src 1159-1160 | low |
| Người thụ hưởng | `the beneficiary designated` | the person designated to receive the benefit | general provision 3(e) src 1184-1188 | low |
| Thời Hạn Thanh Toán | `general provision 16A: the last day of the payment period, effective` | the payment period: 30 days from the effective date, or the period if shorter | general provision 16 src 1537-1555 | low |
| Tỷ lệ phí ngắn hạn; Biểu phí ngắn hạn | `general provision 9: the short-period rate, cover from` | the short-period rates and table | general provision 7 src 1274; 9 src 1429-1435 | low |

## Terms behind the types, fields and constants the L4 declares

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| Quyền lợi bảo hiểm | `A benefit` | the benefits A to D | PHẠM VI BẢO HIỂM I src 309, 320 | low |
| Tử vong | `benefit A.1, death`; `date of death` | death | benefit A.1 src 324-330 | low; capitalised and never defined |
| Phạm vi địa lý | `within the geographical area in the schedule`; `worldwide geographical scope` | the geographical scope listed in the summary | PHẠM VI BẢO HIỂM II src 524-527; general provision 3(f) src 1189 | low |
| Phải; Trái | `A side of the body`: `the right side`, `the left side` | the right and left columns of the upper-limb table | src 379 | low |
| người thuận tay trái | `left-handed` | a left-handed insured, for whom the columns swap | src 413-414 | low |
| ngón cái; ngón trỏ | `A finger`: `the thumb`, `the index finger` | the two fingers the table names | src 403-411 | medium: the source names no other finger ("ngón khác"); `the middle finger`, `the ring finger`, `the little finger` are the encoding's words |
| ngón chân cái | `A toe`: `the big toe` | the one toe the table names | src 448-450 | medium: the other four toes are the encoding's words |
| Cụt | `amputation of ...` | amputation | src 403-411, 418-421, 448-450 | low |
| Dính khớp | `ankylosis of ...` | fused or stiffened joint | src 388-402, 437-438, 453 | medium: literally "joint stuck"; "ankylosis" is the medical term the English tables use |
| Mất răng; răng giả | `loss of teeth`; `can be replaced by dentures` | lost teeth; dentures | src 371-374 | low |
| khoảng | (in `shortening of a leg by at least about 5 cm`) | "about" | src 445 | medium: read as no tolerance (fork F8) |
| Sự mất tích | `A disappearance` | disappearance with a conveyance | special provision 1 src 586-592 | low |
| Án mạng và đột kích | `murder or assault on the insured` | murder and assault | special provision 3 src 601-604 | medium: "đột kích" is literally a raid or sudden attack |
| Cướp phương tiện chuyên chở | `hijacking of a conveyance` | hijacking | special provision 4 src 606-614 | low |
| Ngạt thở | (asphyxiation, in `inhaling smoke, toxic vapour, gas or poison`) | asphyxiation by sudden inhalation | special provision 5 src 616-619 | low |
| Nhân viên được bảo hiểm | (insured employees, special provision 6) | the employees on the list | special provision 6 src 621-628 | medium: capitalised and never defined; not the defined "Người lao động" |
| phí bảo hiểm tối thiểu | `special provision 7: the minimum premium` | VND1.500.000 | special provision 7(b) src 640-641 | low |
| xe gắn máy/xe mô tô | `riding a motorcycle, as driver or passenger` | moped or motorcycle | special provision 8 src 650-653 | medium: Vietnamese distinguishes the two vehicle classes (outside knowledge, unverified); the provision treats them together under one 150cc limit |
| ngộ độc thực phẩm | `poisoning by food or drink` | food poisoning | special provision 9 src 656-660; general exclusion 5(g) src 770 | low |
| Thai sản | (maternity, in a kind of medical expense and in 5(f)) | maternity | general exclusions 5(f), 9 src 769, 818 | low; capitalised and never defined |
| đại dịch | `a disease declared or assessed a pandemic by the WHO or another competent authority` | pandemic | general exclusion 18 src 868-871 | low |
| bảo hiểm xã hội | `also insured under another contract, other than social insurance` | social insurance | special exclusion 3 src 887-889 | low |
| điều kiện tiên quyết | `condition precedent 4(a)(i): ...`, `4(a)(ii)` | condition precedent | general provision 4 src 1197-1214; 16 src 1537 | low |
| Gian lận | `general provision 5: the claim is false or fraudulent` | fraud | general provision 5 src 1216-1229 | low |
| Đề phòng hợp lý và Thay đổi quan trọng | `general provision 6: the claim arises from a change ...`; `A change increasing the risk` | precautions and material change | general provision 6 src 1230-1243 | low |
| thông báo cho Công ty ngay | `notified to the Company immediately` | notice at once | general provision 7.1(f) src 1261 | medium: "ngay" names no number of days |
| Hủy bỏ | `general provision 8.3(b) ...`, `8.3(c) ...` | cancellation (rescission from the start) | general provision 8.3 src 1348-1370 | high: Vietnamese law distinguishes "hủy bỏ" (rescission) from "đơn phương chấm dứt thực hiện" (unilateral termination for the future); English "cancel" blurs them |
| Đơn phương chấm dứt thực hiện | `general provision 8.4.2 ...`, `8.4.4-8.4.5 ...` | unilateral termination | general provision 8.4 src 1371-1402 | high (as above) |
| Hợp đồng bảo hiểm Nhóm | (the group contract; `date the group contract ended`) | the group contract | src 185, 1219, 1247 | low; used, never defined as a compound |
| CHUYỂN ĐỔI | `conversion: the insured may ask, insured since` | conversion of group cover to an individual contract | src 1593-1604 | low |
