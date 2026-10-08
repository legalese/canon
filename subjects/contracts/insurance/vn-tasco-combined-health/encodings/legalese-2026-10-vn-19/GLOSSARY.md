# GLOSSARY — vn-tasco-combined-health, row `legalese-2026-10-vn-19`

The bilingual deliverable: every term the rules define (Article 2, thirty definitions), and every type, field or constant of the L4 that renders a Vietnamese concept.
The Vietnamese is verbatim from the deposited text (checked by `tools/vnsrc.py check`); a line quoting one of the two lists carries an `[in:…]` marker naming it.
"src:N" is line N of `../../source/raw/tasco-combined-health.txt`; "G" and "E" lines are lines of the guarantee and excluded lists.
The L4 identifiers are in the modules named `tasco-vn19-*.l4`.

## The definitions of Article 2

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used | translation risk |
| --- | --- | --- | --- | --- |
| Doanh nghiệp bảo hiểm | `Tasco` (a party to a claim) | the insurer: Tasco Insurance Co. Ltd and its member units | 2.1, src:23-24 | Generic in the Law ("an insurance enterprise"); here it names one company, including its member units. |
| Người được bảo hiểm | `The insured person` | the person named on the contract or certificate whose health is insured | 2.2, src:26-29 | English "the insured" is often the policyholder; here a distinct person, who may also be the beneficiary. |
| Bên mua bảo hiểm | `The policyholder` | the organisation or individual that concludes the contract and pays the premium | 2.3, src:31-40 | Literally "the party buying the insurance"; English "policyholder" can also mean the insured. |
| Người thụ hưởng | `the insured or the beneficiary` (party); `the beneficiary` (relation) | the person named to receive the benefit, or the heir by law | 2.4, src:42-45 | Close. |
| Sự kiện bảo hiểm | `date of the insured event` | the objective event on which Tasco must pay | 2.5, src:47-49 | The rules never say which day an illness's insured event is; this encoding takes the day the risk arose (Article 10's "thời điểm phát sinh rủi ro"). |
| Hợp đồng bảo hiểm | `The contract` | the agreement; the certificate ("Giấy chứng nhận") is evidence of it | 2.6, src:51-55 | The rules write "Hợp đồng/Giấy chứng nhận bảo hiểm" throughout; one record stands for both. |
| Hợp đồng bảo hiểm nhóm | `a group contract` | a contract insuring members of an enterprise, union or association and their dependants | 2.7, src:59-61 | Close. |
| Số tiền bảo hiểm | `sum insured for scope A`, `... B`, `... C` | the most Tasco pays: per insured event for A and B, per policy year for C | 2.8, src:63-70 | "Sum insured" in English often means a fixed benefit; here it is a limit of liability ("giới hạn trách nhiệm tối đa"), and also the base of every percentage. |
| Phí bảo hiểm | `premium` | the money the policyholder pays | 2.9, src:72-75 | Close. |
| Tai nạn | `an accident` | a sudden, unforeseen external force, the sole direct cause of death or injury | 2.10, src:77-81 | Narrower than everyday English: "sole and direct cause" and "outside the insured's control and intent" are part of the term. |
| Bệnh đặc biệt | `a special disease`; `the special diseases listed in Article 2.11` | the 46 listed illnesses, covered only from the second year | 2.11, src:83-93 | Not an English term of art; "specified" or "serious" illnesses would be closer, and the list includes things that are not diseases (finding X10). |
| Bệnh có sẵn/ tình trạng có sẵn | `Article 2.12, a pre-existing condition` | an illness treated in the 3 years before, or with symptoms known before, the start | 2.12, src:95-105 | Close; "tình trạng" (condition) widens it beyond illness. |
| Bệnh bẩm sinh/Dị tật bẩm sinh | `treatment or surgery of a congenital disease or defect` | congenital disease or defect | 2.13, src:111-115; 11.8 | Close. |
| Bệnh nghề nghiệp | `malaria, tuberculosis or an occupational disease` | a disease from harmful working conditions on the state's list | 2.14, src:117-120; 11.9 | Close; "occupational disease" is tied to an official list. |
| Biến chứng thai sản | `a pregnancy complication` | an abnormality or complication of pregnancy needing a doctor's treatment | 2.15, src:122-134 | "Thai sản" covers pregnancy, childbirth and maternity; the term excludes childbirth and premature birth. |
| Bác sĩ | `The treating doctor`; `Article 2.16, a doctor` | a licensed physician practising within licence and specialty, not related to the insured | 2.16, src:136-141 | English "doctor" can mean any doctorate; the term also excludes the insured's relatives and the policyholder's employer or employees. |
| Cơ sở y tế | `The treating facility`; `Article 2.17, a medical facility` | a lawful medical facility in Vietnam able to diagnose, treat and operate, of none of the excluded kinds | 2.17, src:143-151 | "Medical facility" is wider in English; the term excludes rest homes, rehabilitation, workplace units and private traditional-medicine clinics. |
| Nằm viện | `Article 2.18, a hospitalisation`; `Article 2.18, the days in hospital` | a stay of at least 24 continuous hours with admission and discharge | 2.18, src:153-158 | English "hospitalisation" includes day cases; this one needs 24 hours. |
| Phẫu thuật | `A surgery`; `Article 2.19, a surgery` | an operation by licensed surgeons in a hospital, on the Ministry of Health list | 2.19, src:163-167 | Close. |
| Thương tật thân thể | `An accidental injury` | bodily harm caused solely by an accident, in Vietnam, in the term | 2.20, src:169-173 | "Thương tật" is both injury and disability; context decides. |
| Thương tật toàn bộ vĩnh viễn | `total permanent disability by loss`; `... by paralysis or assessment` | loss or paralysis of two limbs, eyes, or a limb and an eye; or 81% or more for 180 days | 2.21, src:175-195 | English "total permanent disability" usually means inability to work; here it is anatomical. |
| Thương tật bộ phận vĩnh viễn | `partial permanent disability by loss`; `... by loss of function` | a listed injury under 81%: loss of a part, or loss of function for 180 days | 2.22, src:197-221 | As above. |
| Thương tật tạm thời | `temporary injury` | an injury preventing work or daily life for a period of treatment, as the injury table lists | 2.23, src:223-229 | English "temporary disability" suggests time off work; the list is in the missing table. |
| Chi phí y tế | `actual reasonable cost of treatment` | necessary, reasonable costs on a doctor's order, within the province's usual charges | 2.24, src:231-236 | Defined for treating injury ("thương tật") only (finding X12). |
| Thể thao chuyên nghiệp | `training for or competing in a professional sport` | sport that is the insured's main, regular income | 2.25, src:238-240 | Narrower than English "professional": defined by income. |
| Hoạt động nguy hiểm | `A dangerous activity`; `Article 2.26, a dangerous activity as listed` | the listed pursuits (racing, climbing with gear, diving with a hard helmet, boxing ...) | 2.26, src:242-246 | "Võ thuật" (martial arts) and "bóng bầu dục" (rugby) are broader in Vietnamese usage than the English sports. |
| Ngộ độc | not encoded (finding X13) | an acute pathological state from toxic substances, diagnosed by a doctor | 2.27, src:248-254 | Whether it is an accident or an illness is not said. |
| Bộ phận giả | `supplying, maintaining, fitting, repairing or replacing a medical device or a prosthesis` | an artificial part implanted to replace a function | 2.28, src:256-260; 11.12 | Close. |
| Các thiết bị/dụng cụ y tế hỗ trợ điều trị | same circumstance | devices implanted or worn to support function or treatment | 2.29, src:262-273; 11.12 | "Dụng cụ chỉnh hình" (orthopaedic appliances) sits in this definition too. |
| Tuổi được bảo hiểm | `the age under Article 2.30` | the age at the last birthday before the contract takes effect | 2.30, src:275-277 | "Liền trước" (immediately before) excludes a birthday on the start date (fork F2). |

## Other Vietnamese concepts the L4 renders

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used | translation risk |
| --- | --- | --- | --- | --- |
| người Nước ngoài đang cư trú hợp pháp tại Việt Nam | `a foreigner residing lawfully in Vietnam` | a foreign national lawfully resident | 1.1, src:11 | Close. |
| tàn phế hoặc thương tật vĩnh viễn | `permanent disability or injury, in percent` | a permanent disability rated 50% or more bars acceptance | 1.2(b), src:16 | Close. |
| năng lực hành vi dân sự đầy đủ | `full civil act capacity when the contract is concluded` | full legal capacity to act | 2.3, src:36 | A civil-law term ("capacity for civil acts"), not English "capacity" in contract. |
| quyền lợi có thể được bảo hiểm | `an insurable interest under the law` | an interest the law lets one insure | 2.3, src:39 | Close; the Law's Art 34 lists the persons for health insurance. |
| Bảo hiểm trùng | `Article 3, the cost left for Tasco` | the same costs insured under two contracts | 3, src:281 | "Trùng" is overlap or duplication; English "double insurance" is close. |
| Tái tục, tái tục liên tục | `Article 5, the cover is continuous` | renewal, continuous renewal | 5, src:336-346; 1.1 | "Liên tục" (continuous) is a status with four conditions, not just "without a gap". |
| khôi phục hiệu lực | `date of the most recent reinstatement` | reinstatement of a lapsed contract | 2.12, src:96; 10, src:497 | Close. |
| Chương trình phổ thông | `the standard programme` | the column for sums insured up to 20 million | 8, src:390 | "Phổ thông" is common or general; "basic" is another rendering. |
| Chương trình đặc biệt | `the special programme` | the column for sums insured over 20 million | 8, src:390 | "Đặc biệt" here is premium or enhanced; unrelated to "bệnh đặc biệt". |
| Phạm vi bảo hiểm A | `scope A` (likewise B, C) | a section of cover | 7.2, src:373-375 | "Phạm vi" is scope or range; "section" in English policy usage. |
| Quyền lợi bảo hiểm chính | `A benefit` | the main benefits of the Article 8 table | 8, src:383 | Close. |
| Nằm viện tây y | `III.1 hospitalisation in Western medicine` | an inpatient stay in modern medicine | 8, src:437 | Close. |
| Nằm viện đông y | `III.2 hospitalisation in Eastern medicine` | an inpatient stay in traditional medicine | 8, src:445 | "Đông y" is traditional (Sino-Vietnamese) medicine; "Eastern" is a calque. |
| Thời gian chờ | `Article 10, the waiting period has run` | time in which no benefit is paid | 10, src:492-499 | Close; the term includes treatment begun in it and ending after. |
| Bệnh thông thường | `row 3, ordinary illness` | an illness that is neither special nor pre-existing | 10.1, src:515 | Never defined: the residual class. |
| Sinh đẻ | `childbirth` | giving birth | 10.1, src:526 | Close. |
| Điều khoản bổ sung | `Article 10.2 applies to` | a supplementary clause adopted for groups over 100 | 10.2, src:531 | Close. |
| chỉnh hình | `cosmetic treatment, cosmetic surgery, or orthopaedic correction` | correction of form; also orthopaedics | 11.11, src:607 | **High.** The ordinary word for orthopaedics; read so, 11.11 excludes treating fractures (finding X3). "Plastic" or "corrective" are other renderings. |
| nồng độ cồn | `breath alcohol while driving`, `blood alcohol while driving` | alcohol concentration | 11.3, src:577 | The units printed are impossible (finding X9). |
| hành khách có vé | `aviation, other than as a ticketed passenger` | a passenger with a ticket | 11.6, src:589 | Close. |
| dịch bệnh theo công bố của cơ quan có thẩm quyền | `an epidemic declared by a competent authority` | an epidemic officially declared | 11.18, src:635-636 | Close. |
| bất khả kháng | `days lost to force majeure` | force majeure | 12.1, 12.2, src:650-654 | "Theo quy định của pháp luật" ties it to the law's meaning. |
| Hồ sơ yêu cầu trả tiền bảo hiểm | `A claim document`; `Article 13, the documents for` | the claim file | 13, src:669 | Close. |
| bản gốc, bản sao | `(original)`, `(copy)` in the document names | original, copy | 13, src:673-674 | "Bản sao" may be certified ("bản sao công chứng") or not; the rules say which per item. |
| khiếu nại | `a claim has arisen during the contract` (4.2(a)); `Article 16.1, the last day to complain about a claims decision` | a claim, or a complaint | 4.2(a), src:314; 16.1, src:807; 16.2, src:813 | **High.** The same word is a claim for payment in 4.2(a) and a complaint in 16.1 and 16.2 (finding X30). |
| Thời hiệu khởi kiện | `Article 16.2, the last day to sue` | the limitation period for a suit | 16, src:806, 812 | "Thời hiệu" is prescription; English "limitation" is close. |
| Bảng tỷ lệ trả tiền bảo hiểm thương tật | `percentage in the injury table` | the table of percentages for injuries | 2.22, src:200; 8, src:409 | Not in the source (finding X2). |
| Bảng tỷ lệ trả tiền bảo hiểm phẫu thuật [cell:tasco-combined-health:459-462] | `percentage in the surgery table` | the table of percentages for surgeries | 8, src:459-462 | Not in the source (finding X2). |
| BẢO LÃNH VIỆN PHÍ [in:tasco-guarantee-hospitals] | `A row of the guarantee list` | Tasco's guarantee of the hospital bill: direct billing | Annex 5, G1 | "Bảo lãnh" is guarantee; the industry sense is direct billing, which the rules never mention. |
| NỘI TRÚ, NGOẠI TRÚ, RĂNG [in:tasco-guarantee-hospitals] | `inpatient`, `outpatient`, `dental` | the three kinds of care with direct billing | Annex 5, G3 | Close. |
| VÙNG [in:tasco-guarantee-hospitals] | `region` | the city or province of the facility | Annex 5, G3 | "Vùng" is region; the values are cities and provinces. |
| CƠ SỞ Y TẾ LOẠI TRỪ [in:tasco-excluded-facilities] | `A row of the excluded-facility list` | facilities whose treatment is excluded | excluded list, E1 | "Loại trừ" is the word Article 11 uses for exclusions, but no clause ties the list to Article 11 (finding X20). |
| TỈNH, HỆ THỐNG CSYT [in:tasco-excluded-facilities] | `province`, `facilities` | province; the facility or chain of facilities | excluded list, E5 | "Hệ thống" (system) signals a chain with several branches. |
