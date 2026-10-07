# GLOSSARY — Law 36/2024/QH15, row VN-28

One row for every term the Law defines in the provisions encoded, and for every type, field or constant the nouns module declares that renders a Vietnamese concept.
The Vietnamese is verbatim from the two source files (checked by `tools/vnsrc.py check`): "src N" is line N of `law36-2024-qh15.txt` (gazette issue 979+980, Articles 24-89); "977+978 src N" is line N of `law36-2024-qh15-977-978.txt` (issue 977+978, Articles 1-23).
Where the Law has no word for a concept the encoding needed, the first column says so.

| Vietnamese term (verbatim) | English identifier in the L4 | English meaning, one line | where defined or used (Điều / clause, src line) | translation risk |
| --- | --- | --- | --- | --- |
| phương tiện giao thông đường bộ | `A road vehicle` | a vehicle used on the road | Art 34 heading, src 251 | "phương tiện" is "means (of transport)"; "vehicle" is the usual rendering |
| phương tiện giao thông cơ giới đường bộ (sau đây gọi là xe cơ giới) | `Article 34(1) — a motor vehicle` | a motor vehicle: the kinds of Article 34(1)(a)-(h) | Art 2(2), 977+978 src 34-35; Art 34(1), src 252 | the class Decree 67 insures; under this Law it no longer includes tractors (R8) |
| Người điều khiển phương tiện tham gia giao thông đường bộ; người lái xe | `A driver` | the person driving a road vehicle; "người lái xe" is the driver of a motor vehicle | Art 2(9), 977+978 src 54-56 | "người lái xe" is narrower than English "driver": the operator of a special-use machine is not one |
| xe ô tô | `an automobile` | a powered vehicle of four or more wheels (or three above 400 kg) for road use: cars, trucks, buses, special-use automobiles | Art 34(1)(a), src 253-258 | "car" in English suggests a passenger car; the Vietnamese covers trucks and coaches, hence "automobile" |
| rơ moóc | `a trailer`; `A towed vehicle` | a towed vehicle whose mass rests mainly on its own axles | Art 34(1)(b), src 259-261 | — |
| sơ mi rơ moóc | `a semi-trailer`; `a semi-trailer` (field) | a towed vehicle a significant part of whose mass rests on the tractor unit | Art 34(1)(c), src 262-264 | — |
| xe chở người bốn bánh có gắn động cơ | `a four-wheeled motorised passenger vehicle` | a slow (30 km/h) four-wheeled passenger vehicle for up to 15 | Art 34(1)(d), src 265-268 | sometimes rendered "golf cart" or "electric shuttle"; the Law's definition is by limits, not by use |
| xe chở hàng bốn bánh có gắn động cơ | `a four-wheeled motorised goods vehicle` | a light four-wheeled goods vehicle (60 km/h, 550 kg kerb) | Art 34(1)(đ), src 269-274 | — |
| xe mô tô | `a motorcycle` | a powered two- or three-wheeler that is not a moped | Art 34(1)(e), src 275-277 | colloquial "xe máy" covers both motorcycles and mopeds; the Law does not use it |
| xe gắn máy | `a moped` | a two- or three-wheeler of at most 50 km/h and 50 cm3 or 4 kW | Art 34(1)(g), src 278-284 | literally "vehicle with a motor attached"; "moped" in English may suggest pedals, which it need not have |
| xe tương tự | (declined) | similar vehicles | Art 34(1)(h), (2)(e), (5), src 285, 294, 306 | open-textured; not decided |
| xe thô sơ | `another rudimentary vehicle` | a non-motor vehicle | Art 34(2), src 286 | also rendered "primitive" or "non-motorised" vehicle |
| xe đạp máy | `a motor-assisted bicycle` | a bicycle whose motor only assists pedalling and cuts out at 25 km/h | Art 34(2)(b), src 289-290 | close to an EU "pedelec"; not a moped |
| xe máy chuyên dùng | `a special-use machine`; `A kind of special-use machine` | construction, farm and forestry machines, tractors, their trailers, special-function and defence machines | Art 34(3), src 295-302 | "chuyên dùng" is "for special use"; distinct from "ô tô chuyên dùng" (a special-use automobile) |
| máy kéo | `a tractor` | a tractor (farm or industrial) | Art 34(3)(c), src 298 | English "tractor" also means a semi-trailer tractor unit, which is "xe ô tô đầu kéo" here |
| xe ô tô đầu kéo | `a semi-trailer tractor unit` | the automobile that draws a semi-trailer | Art 57(1)(m), src 1052-1053 | see "máy kéo" |
| động cơ nhiệt | `a heat engine` | an internal combustion engine | Art 34(1)(g), src 282 | — |
| dung tích làm việc hoặc dung tích tương đương; dung tích xi-lanh | `working capacity in cm3` | engine capacity in cm3 | Art 34(1)(g), src 282-283; Art 57(1)(a), src 1012 | two Vietnamese phrases, one field |
| động cơ điện; công suất động cơ điện | `an electric motor`; `power in kW` | an electric motor and its power | Art 34(1)(g), src 283-284; Art 57(1)(a), src 1013 | rated or peak power is not said |
| trợ lực từ động cơ | `a motor that only assists pedalling, …` | pedal assistance | Art 34(2)(b), src 289-290 | — |
| sức người thông qua bàn đạp hoặc tay quay | `human power, through pedals or a hand crank` | human power | Art 34(2)(a), src 287-288 | — |
| xe vật nuôi kéo | `a draught animal` | an animal-drawn vehicle | Art 34(2)(đ), src 293 | — |
| không có động cơ để di chuyển | `none: the vehicle is towed` | no engine to move itself | Art 34(1)(b)-(c), src 259, 262 | — |
| chở người; chở hàng; chức năng, công dụng đặc biệt | `A purpose of construction` (`carrying persons`, `carrying goods`, `a special function`) | what the automobile is built for | Art 34(1)(a), src 254-256 | "chở" is "to carry"; a special passenger or goods automobile is counted with passenger or goods ones (fork F22) |
| xe ô tô tải | `licensed as a truck` | a truck (goods automobile) | Art 57(1)(d)-(e), src 1020-1028 | "tải" is "load"; also "xe ô tô chở hàng" (src 509) |
| ô tô chuyên dùng | `licensed as a special-use automobile` | a special-use automobile | Art 57(1)(d)-(e), src 1020, 1023, 1027; Art 40(3)(a), src 515 | see "xe máy chuyên dùng" |
| bánh | `wheels` | wheels | Art 34(1), src 253 | — |
| vận tốc thiết kế | `design speed in km/h` | the speed the vehicle is designed for | Art 34(1)(d), (đ), (g), src 267, 272, 279 | not the speed driven |
| khối lượng bản thân | `kerb mass in kg` | unladen (kerb) mass | Art 34(1)(a), (e), src 257, 276-277 | "bản thân" is "own"; kerb mass, not tare |
| khối lượng toàn bộ theo thiết kế | `gross design mass in kg` | gross mass as designed | Art 57(1)(d)-(e), src 1020-1028 | close to "GVWR"; distinct from payload |
| trọng tải | `payload in kg` | carrying capacity | Art 89(2)(d)-(h), src 1977-1990 | may be read as total load capacity; the former classes use it, the new classes do not (R11) |
| không kể chỗ của người lái xe | `seats, not counting the driver's` | seats or persons besides the driver | Art 57(1)(d), src 1019-1020 | "chỗ" is "place": in a sleeper coach, a berth |
| xe ô tô cùng loại, kích thước giới hạn tương đương và có số chỗ nhiều nhất | `seats of the same type of automobile with the most seats` | the largest automobile of the same type | Art 57(4), src 1070-1072 | — |
| hàng ghế | `rows of seats` | rows of seats | Art 34(1)(đ), src 271-272 | — |
| phần động cơ và thùng hàng lắp trên cùng một khung xe | `engine and cargo body on one chassis` | engine and cargo body on one chassis | Art 34(1)(đ), src 271 | — |
| xe ô tô chở người giường nằm | `a sleeper coach` | a passenger automobile with berths | Art 57(1)(i), src 1043 | — |
| xe ô tô chở khách nối toa | `an articulated coach` | an articulated (jointed) coach | Art 57(1)(p), src 1059-1060 | "nối toa" is "joined carriages" |
| số tự động | `automatic transmission`; `only automatic automobiles` | automatic gearbox | Art 89(2)(đ), (3)(đ), src 1979-1981, 2019-2020 | — |
| xe mô tô ba bánh dùng cho người khuyết tật | `a three-wheeled motorcycle for disabled persons` | a three-wheeler for a disabled person | Art 57(2), src 1061-1062 | — |
| kéo rơ moóc | `towing` | towing a trailer | Art 57(1)(d), src 1021 | — |
| nam; nữ | `male`; `female` (`A sex`) | man; woman | Art 59(1)(e), src 1154-1155 | — |
| giấy phép lái xe | `A driving licence` | a driving licence | Art 57, src 1010 | written "Giấy phép lái xe" at the head of a sentence |
| hạng | `A licence class under Article 57` (`class A1` … `class DE`) | a licence class | Art 57(1), src 1011-1060 | the letters are the Law's; four of them (A1, B1, C, D) also name former classes with other meanings (R2) |
| Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành | `A licence class issued before 1 January 2025` (`former class A1` … `former class FE`) | a licence issued under the former law | Art 89(1)-(2), src 1962-1965 | "former" is the encoding's word, not the Law's |
| người không hành nghề lái xe; người hành nghề lái xe | `former class B1, for a non-professional driver`; `former class B2, for a professional driver` | a driver who does not, or does, drive for a living | Art 89(2)(e), (g), src 1983-1987 | whether it limits the use of a B1 card is not said (no fork taken: the encoding does not limit it) |
| điều kiện hạn chế | `A restriction on a licence` | a restriction on an exchanged licence | Art 89(3)(a), (đ), src 2011, 2020 | — |
| do cơ quan có thẩm quyền của Việt Nam cấp | `a competent Vietnamese authority` (`An issuer of a licence`) | issued by a Vietnamese authority | Art 57(6)(a), src 1079 | — |
| giấy phép lái xe quốc tế | `a foreign or international issuer` | an international driving permit | Art 57(6)(b), (8), src 1080, 1092 | foreign licences are declined, not mapped |
| ngày cấp | `date of issue` | the day of issue | Art 57(5), src 1075 | — |
| thời hạn ghi trên giấy phép lái xe | `expiry date printed on it` | the term printed on the card | Art 89(1), src 1963 | "thời hạn" is a term or a time limit; here its end |
| điểm | `points remaining` | points on the licence (12 at most) | Art 58(1), src 1118-1120 | — |
| bị thu hồi | `revoked under Article 62(5) on` | revoked | Art 57(7)(b), 62(5), src 1091, 1255 | "thu hồi" is also "recover" or "withdraw"; for registrations and plates the same word is rendered "revoke" |
| tước quyền sử dụng giấy phép lái xe có thời hạn | `right to use withdrawn` (`A period`) | deprivation of the right to use the licence for a term | Art 57(8)(c), src 1105-1106 | often rendered "suspension"; it is a penalty under the law on administrative violations |
| đang còn điểm, còn hiệu lực | `Article 56(1) — the licence … may be driven under on …` | with points left and in force | Art 56(1), src 970 | — |
| không có hiệu lực | `Article 57(7) — the licence … is in force on …` (negated) | not in force | Art 57(7), src 1089 | "hiệu lực" is "effect" or "validity"; "có giá trị sử dụng" (57(6)) is "valid for use", a different test |
| hết thời hạn sử dụng | `Article 57(7)(a) — … has expired by …` | expired | Art 57(7)(a), src 1090 | the same words mean a registration's or plate's expiry in Art 39(3)(d) |
| phù hợp với loại xe | `the class of the licence … entitles the driving of …` | appropriate to the kind of vehicle | Art 56(1), src 970 | Decree 67's "phù hợp" is read the same way (fork F25) |
| đủ … tuổi | `has reached … years of age, born on … , on …` | has reached the age of | Art 59(1), src 1146-1155 | "đủ" is "full"; whether the maximum age ends on reaching it is fork F5 |
| Tuổi tối đa | `Article 59(1)(e) — the maximum age for …` | the maximum age | Art 59(1)(e), src 1153 | see "đủ … tuổi" |
| bằng hoặc chứng chỉ điều khiển xe máy chuyên dùng | `holds a certificate to operate this special-use machine` | the operator's diploma or certificate | Art 56(2), src 983-984 | — |
| chứng chỉ bồi dưỡng kiến thức pháp luật về giao thông đường bộ | `holds a certificate of training in road-traffic law` | the certificate of training in road-traffic law | Art 56(2), 59(1)(b), 63, src 985-986, 1148 | — |
| lực lượng quân đội, công an làm nhiệm vụ quốc phòng, an ninh | `in the army or police, on defence or security duty` | army and police on duty | Art 59(3), src 1162-1163 | — |
| Người tập lái xe ô tô, người dự sát hạch lái xe ô tô | `a learner or examinee in a training or test automobile on its route, …` | a learner or examinee driver | Art 56(5), src 1006-1009 | — |
| xét nghiệm nồng độ cồn | `A test of the driver` | a test for alcohol | Art 81(3), src 1762 | — |
| máu | `blood` (`A medium tested`) | blood | Art 9(2), 977+978 src 238; Art 81(3), 87(5), src 1763, 1936 | — |
| hơi thở | `breath` (`A medium tested`) | breath | Art 9(2), 977+978 src 239 | Article 87(5) provides an endogenous finding for blood only (R13) |
| nồng độ cồn | `alcohol concentration found` | alcohol concentration | Art 9(2), 977+978 src 239; Art 81(3), 83(2)(a), 87(5), src 1762, 1822, 1936 | unit not stated; 9(2) forbids any, so only zero and above zero matter |
| Điều khiển phương tiện tham gia giao thông đường bộ mà trong máu hoặc hơi thở có nồng độ cồn | `Article 9(2) — the test … shows driving with alcohol in the blood or breath, on …`; `the permitted level of alcohol under the Law` (0) | driving with alcohol in the blood or breath (prohibited) | Art 9(2), 977+978 src 238-239 | "có nồng độ cồn" is "has an alcohol concentration": any, not "over a limit" |
| nồng độ cồn nội sinh | `found endogenous by the Ministry of Health's method` | endogenous alcohol (produced in the body) | Art 87(5), src 1936 | — |
| chất ma túy; các chất kích thích khác mà pháp luật cấm sử dụng | `a narcotic or another stimulant the law prohibits was found` | narcotics; other stimulants the law prohibits | Art 9(3), 977+978 src 240-241; Art 83(2)(a), src 1822-1823 | "chất kích thích" is wider than English "stimulant": any intoxicating substance |
| chứng nhận đăng ký xe | `A registration`; `registration certificate revoked on` | the vehicle registration certificate | Art 39, src 437 | Article 39 writes it without "giấy" (paper); Article 43(2)(c) writes "giấy chứng nhận đăng ký xe" (src 630), as Decree 67 does; the same document |
| biển số xe | `plate revoked on` | the number plate | Art 39, src 437 | "biển số" is both the plate and its number; Art 36(3)(b) keeps the number with the owner |
| Các trường hợp thu hồi chứng nhận đăng ký xe, biển số xe | `A case for revocation under Article 39(6)` | the cases for revocation | Art 39(6), src 478-479 | — |
| Chuyển quyền sở hữu xe | `ownership transferred` | transfer of ownership | Art 39(6)(a), src 480 | — |
| biển số xe trúng đấu giá | `the plate was won at auction` | an auctioned plate | Art 39(6)(a), src 481 | — |
| hư hỏng không sử dụng được | `damaged beyond use` | damaged beyond use | Art 39(6)(d), src 490 | — |
| Xe bị thải bỏ, bị mất không tìm được | `scrapped, or lost and not found, and the owner asked for revocation` | scrapped or lost | Art 39(6)(đ), src 491-492 | — |
| niên hạn sử dụng | `the year its service life ends …`; `Article 40 — …` | the service life (an age limit for a vehicle) | Art 40, src 500-517 | not "useful life" in the accounting sense |
| năm sản xuất xe | `year of manufacture` | year of manufacture | Art 40(1), src 501 | — |
| Cải tạo xe (sau đây gọi là cải tạo) | `before conversion` | conversion: a change to a registered (or used imported) vehicle that changes its type | Art 2(7), 977+978 src 48-50; Art 40(2), src 503-512 | also "renovation"; a change that does not change the type is not one |
| Cải tạo xe ô tô loại khác thành xe ô tô chở người | `Article 9(10) — prohibits the conversion of` | converting another automobile into a passenger automobile (prohibited) | Art 9(10), 977+978 src 258-259 | — |
| Các hành vi bị nghiêm cấm | (Article 9 functions) | prohibited acts | Art 9, 977+978 src 233 | — |
| Điều khiển xe cơ giới tham gia giao thông đường bộ không có giấy phép lái xe theo quy định của pháp luật | `Decision 1 — the driver … may drive … on …` (its negation) | driving a motor vehicle without the licence the law requires (prohibited) | Art 9(1), 977+978 src 234-235 | "theo quy định của pháp luật" (as the law provides) lets Article 56(4)-(5) carve out mopeds and learners |
| Tai nạn giao thông đường bộ | (not encoded) | a road traffic accident: an unintended collision causing harm | Art 2(12), 977+978 src 63-66 | "va chạm" is "collision" (R15) |
| Xe cơ giới của quân đội, công an phục vụ mục đích quốc phòng, an ninh | `a military or police vehicle for defence or security` | army and police vehicles for defence or security | Art 40(3)(b), src 516 | — |
| đổi, cấp lại | `An exchange under Article 89(3)` | exchange and reissue | Art 89(3), src 2008-2009 | — |
| chứng chỉ điều khiển xe máy chuyên dùng cho người điều khiển máy kéo | `a certificate to operate tractors, …` | a tractor operator's certificate | Art 89(3)(d)-(n), src 2015-2046 | — |
| Hiệu lực thi hành | `Article 88(1) — the day this Law takes effect` | entry into force | Art 88, src 1950-1952 | — |
