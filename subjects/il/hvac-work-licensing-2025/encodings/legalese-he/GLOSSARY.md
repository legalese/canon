# HVAC work licensing — the Hebrew term contract

**GENERATED from `glossary.json` by `../../source/revoice.py`. Do not edit by hand.**
The JSON is the machine-readable form and the one to change; this page is the same map, readable.

**What this is.** Every identifier of the English encoding at [`../legalese`](../legalese) — type names, constructors, record fields, rule names, parameters, fixtures and `§` headings — with the Hebrew name the Hebrew-canonical row [`.`](.) uses for it.
The English row is the oracle: renaming is all that happens, and every numeric assertion keeps its exact value.

**Grounded in the instruments first.** A row marked `law`, `schedule` or `regulations` uses the instrument's own words and the note says where.
A row marked `composed` has no counterpart in either instrument and the note says why; those are the rows a Hebrew reviewer should read first.

| provenance | entries |
| --- | --- |
| `law` | 72 |
| `schedule` | 24 |
| `regulations` | 36 |
| `composed` | 63 |
| **total** | **195** |

Two names are deliberately **not** renamed, because they are not ours: `add years` and `add months`, which the `daydate` library defines.

## Types

| English | Hebrew | source | note |
| --- | --- | --- | --- |
| `Act` | `פעולה` | composed | the Law has no collective noun for the acts a duty can require |
| `Actor` | `גורם` | composed | the Law names the two parties but has no collective noun for them |
| `Applicant` | `מבקש` | law | s.5(a) (בחוק זה – מבקש) |
| `Foreign expert` | `מומחה זר` | law | s.9(a) (בסעיף זה – מומחה זר) |
| `Grade` | `דרגה` | law | s.2 ”רישיון דרגה 1/2/3“; the grade itself is דרגה and the word רישיון is carried by the heralds |
| `Outcome` | `תוצאה` | composed | SimpLEX's table has an outcome column; the Regulations have no word for it |
| `Prior qualification` | `הכשרה או ניסיון קודמים` | schedule | column A heading, טור א׳ הכשרה או ניסיון קודמים |
| `Requirement` | `דרישה` | schedule | column B heading, טור ב׳ דרישות לקבלת הרישיון המבוקש |
| `Service` | `שירות` | regulations | reg. 4 ‘מבקש הרישיון או השירות’ |

## Constructors

| English | Hebrew | source | note |
| --- | --- | --- | --- |
| `appeal against a practical examination score` | `השגה על ציון הבחינה המעשית` | regulations | reg. 2(b) as made says only ‘ציון הבחינה’; the adjective is the encoding's reading, which is the whole point of the as-made vintage |
| `appeal against a theoretical examination score` | `השגה על ציון הבחינה העיונית` | regulations | reg. 2(b) as amended, verbatim |
| `appeal under review` | `הערעור נבדק` | composed | the SimpLEX screen's phrase. Note it says ערעור where reg. 2(b) says השגה; the screen's word is kept because this enum transcribes the screen |
| `application for a licence` | `בקשה לקבלת רישיון או לחידושו` | regulations | the draft's reg. 2(d), verbatim: the fee is charged on the application (fork F5) |
| `Division completion certificate, grade 1` | `תעודת גמר בלימודי קירור ומיזוג אוויר דרגה 1 מהאגף להכשרה מקצועית` | schedule | Part B item 3(2), verbatim |
| `Division completion certificate, grade 2` | `תעודת גמר בלימודי קירור ומיזוג אוויר דרגה 2 מהאגף להכשרה מקצועית` | schedule | Part C item 4(2), verbatim |
| `Division completion certificate, refrigeration and air conditioning` | `תעודת גמר בלימודי קירור ומיזוג אוויר מהאגף להכשרה מקצועית` | schedule | Part A item 3, verbatim |
| `Division youth vocational school completion certificate` | `תעודת גמר בלימודי קירור ומיזוג אוויר מבית ספר מקצועי לנוער של האגף להכשרה מקצועית` | schedule | Part B item 5(2), verbatim |
| `Grade 1` | `דרגה 1` | law | s.2's defined term is רישיון דרגה 1 in full; the bare דרגה 1 keeps the herald רישיון %דרגה% from reading ‘licence licence grade 1’ |
| `Grade 2` | `דרגה 2` | law | as for דרגה 1 |
| `Grade 3` | `דרגה 3` | law | as for דרגה 1 |
| `holds a Grade 1 licence` | `בעל רישיון דרגה 1` | schedule | Part B item 3(1) ‘רישיון דרגה 1’, with s.2's בעל רישיון |
| `holds a Grade 2 licence` | `בעל רישיון דרגה 2` | schedule | Part C item 4(1) |
| `Ministry of Education climate-control certificate, 3 units` | `תעודת גמר בלימודי בקרת אקלים ברמה של 3 יחידות לימוד ממשרד החינוך` | schedule | Part A item 1(2) and Part B item 3(3) |
| `Ministry of Education climate-control certificate, 5 units` | `תעודת גמר בלימודי בקרת אקלים ברמה של 5 יחידות לימוד ממשרד החינוך` | schedule | Part B item 1(2) and Part C item 4(3) |
| `no further requirements` | `בלא דרישות נוספות` | schedule | Part B item 2 and Part C item 2, verbatim |
| `no prior training or experience` | `בלא הכשרה או ניסיון קודמים` | schedule | item 1 of all three parts, verbatim |
| `no route in the Second Schedule` | `אין מסלול בתוספת השנייה` | composed | the Schedule has no word for the absence of a row; this is the encoding's own |
| `notify the registrar of the change` | `להודיע לרשם על השינוי` | law | s.16 ‘יודיע לרשם על כל שינוי’, put in the infinitive because it is the object of a duty |
| `practical examination` | `בחינה מעשית` | regulations | reg. 1, verbatim |
| `qualifying experience` | `ניסיון מזכה` | composed | the Schedule spells the row out (שנת ניסיון במצטבר מתוך שלוש שנים / שלוש שנות ניסיון מתוך שבע) and gives it no short name |
| `receipt or renewal of a licence` | `קבלת רישיון או חידושו` | regulations | reg. 2(c) as made, verbatim: the fee is charged on receipt (fork F5) |
| `registered certified technician, having completed a study programme with the completion course` | `טכנאי מוסמך מיזוג אוויר שסיים תוכנית לימודים הכוללת את קורס ההשלמה` | schedule | Part B item 2, verbatim |
| `registered certified technician, refrigeration and air conditioning` | `טכנאי מוסמך מיזוג אוויר` | schedule | Part B item 2 names it itself: (להלן – טכנאי מוסמך מיזוג אוויר) |
| `registered engineer, mechanical branch` | `מהנדס רשום בפנקס המהנדסים והאדריכלים בענף מכונות` | schedule | Part C item 8, verbatim |
| `registered practical engineer, having completed a study programme with the completion course` | `הנדסאי מיזוג אוויר שסיים תוכנית לימודים הכוללת את קורס ההשלמה` | schedule | Part C item 2, verbatim |
| `registered practical engineer, refrigeration and air conditioning` | `הנדסאי מיזוג אוויר` | schedule | Part C item 2 names it itself: (להלן – הנדסאי מיזוג אוויר) |
| `registration approved` | `הרשמה מאושרת` | composed | the phrase the SimpLEX screen shows; the English row already carries it as a comment |
| `registration refused` | `הרשמה נדחית` | composed | the phrase the SimpLEX screen shows |
| `temporary licence for a foreign expert` | `רישיון זמני למומחה זר` | regulations | reg. 2(d) and the s.9 heading, verbatim |
| `the licence holder` | `בעל הרישיון` | law | s.2 defines בעל רישיון; ss.16 and 17 use it with the article |
| `the registrar` | `הרשם` | law | s.2, verbatim |
| `theoretical examination` | `בחינה עיונית` | regulations | reg. 1 as amended, verbatim |
| `training of up to` | `הכשרה של עד` | schedule | every column B cell opens with הכשרה של עד N שעות |

## Record fields

| English | Hebrew | source | note |
| --- | --- | --- | --- |
| `completed the supplementary studies the Schedule requires` | `סיים בהצלחה לימודי השלמה` | law | s.6(a)(4)(c), verbatim |
| `holds a completion certificate for the grade` | `הוא בעל תעודת גמר לדרגה` | law | s.6(a)(4)(a) ‘הוא בעל תעודת גמר’, with the grade added because the encoding asks it per grade |
| `hours` | `שעות` | schedule | the N in הכשרה של עד N שעות |
| `is an adult` | `הוא בגיר` | law | s.6(a)(1), verbatim |
| `is an applicant from a foreign country` | `מבקש ממדינת חוץ` | law | s.9(a) chapeau, verbatim |
| `is an Israeli citizen or resident` | `הוא אזרח ישראלי או תושב ישראל` | law | s.6(a)(2), verbatim |
| `is authorised abroad and in the six years before applying installed or maintained systems similar to those invited for` | `מוסמך לבצע עבודות במדינת חוץ וביצע בשש השנים שקדמו להגשת הבקשה התקנה או תחזוקה של מערכות דומות לאלה שלשמן הוזמן` | law | s.9(a)(2), verbatim but for the ellipsis of רישיון זמני |
| `is recognised by the registrar as of repute and expertise` | `הרשם הכיר בו כבעל מוניטין וכמומחה בעל שם בתחומו` | law | s.9(a)(3), verbatim |
| `is unfit by reason of a conviction or pending indictment` | `אינו ראוי מפאת הרשעה או כתב אישום תלוי ועומד` | law | s.6(a)(3), condensed from the full clause; the registrar's לדעת הרשם is what makes it an input |
| `prior qualifications` | `הכשרותיו וניסיונו הקודמים` | law | s.6(a)(4)(c) ‘הכשרתו ולניסיונו הקודמים’, in the plural because the field is a LIST. Deliberately distinct from the type הכשרה או ניסיון קודמים |
| `the holder met the requirements of those courses` | `בעל הרישיון עמד בדרישות אותן השתלמויות` | law | s.17(a) ‘ויעמוד בדרישות אותן השתלמויות’ |
| `the training was in the field of the licence` | `ההשתלמות הייתה בתחום עיסוקו לפי רישיונו` | law | s.17(a) ‘בתחום עיסוקו לפי רישיונו’ |
| `was invited to Israel for work on a system of` | `הוזמן לישראל לשם ביצוע עבודות במערכת שתפוקת הקירור שלה` | law | s.9(a)(1), verbatim up to the number |

## Rules and helper functions

| English | Hebrew | source | note |
| --- | --- | --- | --- |
| `31 March of the fifth year` | `31 במרץ של השנה החמישית` | law | s.8, verbatim |
| `a further renewal of the temporary licence is available` | `ניתן לחדש שוב את הרישיון הזמני` | law | s.9(b) ‘הרשם רשאי לחדש את תוקפו של רישיון זמני’ |
| `a licence of the grade permits work on the system` | `רישיון הדרגה מתיר עבודה במערכת` | law | s.2's ‘רישיון לביצוע עבודה במערכת …’ |
| `Chapter F commences on` | `תחילתו של פרק ו׳ ביום` | law | s.63(b) ‘תחילתו של פרק ו׳’ |
| `five years from grant` | `חמש שנים ממתן הרישיון` | law | s.8 ‘לחמש שנים’ |
| `Part A -- Grade 1` | `חלק א׳ — רישיון דרגה 1` | schedule | part heading, verbatim |
| `Part B -- Grade 2` | `חלק ב׳ — רישיון דרגה 2` | schedule | part heading, verbatim |
| `Part C -- Grade 3` | `חלק ג׳ — רישיון דרגה 3` | schedule | part heading, verbatim |
| `regulation 4 is satisfied` | `תקנה 4 מתקיימת` | regulations | reg. 4 encoded once, as a function of whatever fee is prescribed |
| `rounded to the nearest whole shekel` | `מעוגל לשקל החדש השלם הקרוב` | regulations | reg. 3(a) ‘ויעוגל לשקל החדש השלם הקרוב’ |
| `the 5786 amendment is in force` | `תיקון התשפ״ו בתוקף` | composed | true for a rule-effective date on or after יום תחילתו של תיקון התשפ״ו |
| `the appeal fee plus its base` | `אגרת ההשגה בתוספת אגרת הבחינה` | regulations | shared by the enacted rule and the draft: "נוסף על" in both |
| `the applicant qualifies through the Schedule row for` | `המבקש עומד בשורת התוספת לדרגה` | composed | ‘שורה’ for a row of the Schedule's table is ours; the Schedule numbers its rows פרט |
| `the applicant satisfies the personal conditions` | `המבקש עומד בתנאים האישיים` | composed | s.6(a)(1)-(3) have no collective name; ‘תנאים’ is s.6's heading word |
| `the applicant satisfies the training condition` | `המבקש עומד בתנאי ההכשרה` | composed | s.6(a)(4); הכשרה is the Schedule's word |
| `the chapters the Division director may exempt the applicant from` | `הפרקים שמנהל האגף להכשרה מקצועית רשאי לפטור מהם` | law | s.7 ‘מנהל האגף להכשרה מקצועית רשאי לתת … פטור מלימודי פרק החשמל’ |
| `the commencement day` | `יום התחילה של החוק` | law | s.63(a)(1)'s יום התחילה. Deliberately NOT the bare יום התחילה, which is the parameter of the same idea elsewhere; two identifiers may not share a name |
| `the continuing-education duty is met` | `חובת ההשתתפות בהשתלמויות מתקיימת` | law | s.17 heading חובת השתתפות בהשתלמויות |
| `the day the 5786 amendment came into force` | `יום תחילתו של תיקון התשפ״ו` | composed | the amending regulations state no תחילה; the day of publication under s.17 of פקודת הפרשנות [נוסח חדש] (fork F6) |
| `the day the Regulations came into force` | `יום תחילתן של התקנות` | regulations | reg. 5: "תחילתן של תקנות אלה 7 ימים מיום פרסומן"; computed, not asserted |
| `the duty to report a change of registered details` | `חובת עדכון פרטים` | law | s.16 heading, verbatim |
| `the examination fee the appeal fee is added to` | `אגרת הבחינה שאגרת ההשגה נוספת עליה` | regulations | reg. 2(b): "נוסף על התשלום בעד האגרה כאמור בתקנת משנה (א1)" |
| `the examination fee the draft's appeal fee is added to` | `אגרת הבחינה שאגרת ההשגה שבטיוטה נוספת עליה` | composed | the draft's 2(c) adds the 40 to "the fee under (a)", the theoretical fee (fork F5) |
| `the fee prescribed by reg. 2 as amended for` | `האגרה שקובע נוסח תקנה 2 כפי שתוקן בעד` | regulations | the text after KT 12383, 5786 p. 2062 |
| `the fee prescribed by reg. 2 as made for` | `האגרה שקובע נוסח תקנה 2 כפי שהותקן בעד` | regulations | the text at KT 11951, 5785 p. 2116; "בעד" is reg. 2's own preposition |
| `the fee prescribed for` | `האגרה הקבועה בעד` | regulations | the ONE rule for reg. 2; reg. 4's own words are "שנקבעה בעדו אגרה" |
| `the fee the SimpLEX draft prescribes for` | `האגרה שקובעת טיוטת SimpLEX בעד` | composed | the draft in Figure 4; no date, because it was never in force |
| `the latest day a temporary licence can run to` | `היום המאוחר ביותר שאליו יכול להימשך רישיון זמני` | composed | the arithmetic consequence of s.9(a) plus s.9(b) |
| `the Law applies to systems on refrigerants outside the Fourth Schedule from` | `החוק חל על מערכות בקרר שאינו מנוי בתוספת הרביעית החל מיום` | law | s.63(a)(2) ‘קרר שאינו כאמור בפסקה (1)’, and (1) points at the Fourth Schedule |
| `the licence expires on` | `הרישיון פוקע ביום` | composed | s.8 says תוקפו של רישיון יהיה ל…; the expiry day is the encoding's framing |
| `the licence grade reaches the system` | `דרגת הרישיון מגיעה למערכת` | composed | s.3(a) is a prohibition and speaks of רישיון מהסוג המתאים; ‘reaches’ is the encoding's, because only the cooling-output half of s.3(a) is modelled |
| `the licence may be renewed` | `ניתן לחדש את הרישיון` | law | s.8 ‘וניתן לחדשו’ |
| `the lowest grade permitted to work on a system of` | `הדרגה הנמוכה ביותר המתירה עבודה במערכת של` | composed | reads s.2's three grade definitions backwards, from kilowatts to grade |
| `the outcome the SimpLEX draft would show for` | `התוצאה שהייתה טיוטת SimpLEX מציגה בעד` | composed | Figure 4's table, run against the draft it was written for |
| `the rank of` | `דירוג הדרגה` | composed | an ordering the Law does not state; it follows from the 18/70/any nesting |
| `the registrar may extend validity by` | `הרשם רשאי להאריך את תקופת התוקף` | law | s.17(c) ‘רשאי … להאריך את תקופת תוקף רישיונו’; s.8 defines תקופת תוקף |
| `the registrar may grant a temporary Grade 3 licence` | `הרשם רשאי לתת רישיון דרגה 3 זמני` | law | s.9(a), verbatim |
| `the registrar shall grant the licence` | `הרשם ייתן את הרישיון` | law | s.6(a) ‘הרשם ייתן רישיון למבקש’ |
| `the Regulations are in force` | `התקנות בתוקף` | composed | true for a rule-effective date on or after יום תחילתן של התקנות |
| `the Regulations commence on` | `תחילתן של התקנות ביום` | regulations | reg. 5, verbatim |
| `the route is open on the application date` | `המסלול פתוח במועד הגשת הבקשה` | composed | as above; מועד הגשת הבקשה is the Law's phrase (s.9(a)(2)) |
| `the route is time-limited` | `המסלול מוגבל בזמן` | composed | column C says הוראה זו תעמוד בתוקף לתקופה של שלוש שנים; ‘מסלול’ is ours |
| `the Second Schedule requires, for the grade, of an applicant with` | `מה שהתוספת השנייה דורשת, לדרגה, ממבקש שהכשרתו או ניסיונו הקודמים הם` | schedule | the two column headings joined |
| `the service may be provided` | `ניתן לספק את השירות` | regulations | reg. 4 is a prohibition (לא ייתן … לא יאפשר); this is its positive form |
| `the SimpLEX draft would have allowed` | `טיוטת SimpLEX הייתה מתירה` | composed | reg. 4 applied to the draft's fees; מתירה echoes reg. 4's "לא יאפשר" |
| `the SimpLEX outcome for` | `תוצאת SimpLEX בעד` | composed | Figure 4's table, run against the law as it stood on the rule-effective date |
| `the total the SimpLEX draft would have required for` | `הסכום הכולל שהייתה דורשת טיוטת SimpLEX בעד` | composed | subjunctive throughout: the draft never required anything of anyone |
| `the total to be tendered for` | `הסכום הכולל שיש לשלם בעד` | composed | the aggregate reg. 2 never names; לשלם and בעד are the Regulations' words |
| `the updated fee` | `האגרה המעודכנת` | regulations | reg. 3 heading עדכון אגרות |
| `three months from publication` | `שלושה חודשים מיום הפרסום` | law | s.63(a)(1), verbatim |

## Parameters and inputs

| English | Hebrew | source | note |
| --- | --- | --- | --- |
| `a` | `המבקש` | law | the definite form keeps it apart from the type מבקש; the genitive המבקש's lexes |
| `application date` | `מועד הגשת הבקשה` | law | s.9(a)(2) ‘הגשת הבקשה’ |
| `base index` | `המדד היסודי` | regulations | reg. 3(a) definition, verbatim |
| `commencement day` | `יום התחילה` | law | s.63(a)(1) (להלן – יום התחילה) |
| `e` | `המומחה` | law | s.9's מומחה זר |
| `eighteen` | `שמונהעשר` | law | s.63(b) ‘18 חודשים’. A BARE name, so it is written solid: a space or a maqaf would split it |
| `fee` | `אגרה` | regulations | reg. 2's word |
| `fee prescribed` | `האגרה הקבועה` | regulations | reg. 4: "שנקבעה בעדו אגרה" |
| `fee regulations in force` | `תחילת תקנות האגרות` | law | s.63(a)(1) ‘מועד כניסתן לתוקף של תקנות לפי סעיף 59’ |
| `first granted` | `יום מתן הרישיון הראשון` | composed | s.9 does not name the first grant day |
| `grade` | `הדרגה` | law | the definite form keeps it apart from the type דרגה |
| `grant` | `מתן` | law | s.8 ‘השנה שבה ניתן הרישיון’ |
| `holds a valid electricity licence` | `בעל רישיון חשמל בתוקף` | law | s.7(a), verbatim |
| `holds a valid work-at-height certificate` | `בעל אישור עבודה בגובה בתוקף` | law | s.7(b), verbatim |
| `hours of recognised training in the final year of validity` | `שעות השתלמות מוכרת בשנה האחרונה לתוקף הרישיון` | law | s.17(a) ‘במהלך השנה האחרונה לתוקפו של הרישיון … שהאגף להכשרה מקצועית הכיר בהן’ |
| `kw` | `תפוקה` | law | s.2 ‘תפוקת הקירור שלה’. A BARE name, so it may carry no maqaf: קילו־ואט would not lex outside backticks |
| `licence` | `הרישיון` | law | s.2 רישיון |
| `months of extension sought` | `חודשי ההארכה המבוקשים` | composed | s.17(c) caps the extension at שלושה חודשים and does not name the quantity |
| `new index` | `המדד החדש` | regulations | reg. 3(a) definition, verbatim |
| `p` | `הכשרה` | schedule | the Schedule's column A value inside the three per-part helpers |
| `paid` | `ששולם` | regulations | reg. 4 ‘שילם את האגרה במלואה’ |
| `prior` | `הכשרתו` | law | s.6(a)(4)(c) ‘הכשרתו ולניסיונו הקודמים’, shortened for a parameter |
| `published` | `פרסום` | law | s.63(a)(1) ‘מיום פרסומו’; reg. 5 ‘מיום פרסומן’ |
| `r` | `מועד` | composed | the s.46 commencement date inside the CONSIDER |
| `renewals already granted` | `חידושים שכבר ניתנו` | composed | s.9(b) allows שתי תקופות נוספות and does not count them |
| `s.46 regulations in force` | `תחילת התקנות לפי סעיף 46` | law | s.63(b), verbatim |
| `service` | `השירות` | regulations | the definite form keeps it apart from the type שירות |
| `the case is special and the circumstances justify it` | `במקרים מיוחדים ובנסיבות מוצדקות` | law | s.17(c), verbatim |
| `the council has been consulted` | `לאחר התייעצות עם המועצה` | law | s.17(c), verbatim |
| `the duty under s.17(a) or (b) is unmet` | `לא מילא את חובתו לפי סעיף 17(א) או (ב)` | law | s.17(c) ‘שלא מילא את חובתו להשתתף בהשתלמות לפי סעיף קטן (א) או (ב)’ |
| `the system type is exempted by order under s.3(b)` | `סוג המערכת פטור בצו לפי סעיף 3(ב)` | law | s.3(b) ‘פטור מקבלת רישיון’ by ministerial order; an input, no order located |
| `x` | `סכום` | regulations | reg. 2 ‘אגרה בסכום של’ |

## Fixtures

| English | Hebrew | source | note |
| --- | --- | --- | --- |
| `a day before the Regulations commenced` | `יום שלפני תחילתן של התקנות` | composed | 1 July 2025: the Regulations did not yet exist |
| `a day under the Regulations as amended` | `יום שבו התקנות כנוסחן המתוקן` | composed | the amendment's commencement day, 4 May 2026 |
| `a day under the Regulations as made` | `יום שבו התקנות כנוסחן המקורי` | composed | the commencement day itself, 16 July 2025 |
| `Dana` | `דנה` | composed | an invented applicant |
| `Dana, who relies on her experience` | `דנה, הנסמכת על ניסיונה` | composed | an invented applicant |
| `Noa, once she holds the completion certificate` | `נועה, משהיא בעלת תעודת גמר` | composed | an invented applicant |
| `Noa, with the five-unit certificate` | `נועה, בעלת תעודת 5 יחידות` | composed | an invented applicant |
| `the fee regulations day` | `יום תחילת תקנות האגרות` | law | s.63's own note: (תחילתן של התקנות לפי סעיף 59, היא ביום 16.7.2025) |
| `the gazette date` | `יום הפרסום ברשומות` | composed | 14 January 2025, ס״ח 3349 |
| `Yossi` | `יוסי` | composed | an invented applicant |
| `Yossi, after the completion course` | `יוסי, לאחר קורס ההשלמה` | composed | an invented applicant |
| `Yossi, who also has the experience` | `יוסי, שיש לו גם הניסיון` | composed | an invented applicant |

## `§` headings

| English | Hebrew | source | note |
| --- | --- | --- | --- |
| `Chapter A -- Definitions` | `פרק א׳ — הגדרות` | regulations | chapter heading of the Regulations, verbatim |
| `Chapter A -- Purpose and definitions` | `פרק א׳ — מטרה והגדרות` | law | chapter heading, verbatim |
| `Chapter B -- Fees` | `פרק ב׳ — אגרות` | regulations | chapter heading, verbatim |
| `Chapter B -- Licensing` | `פרק ב׳ — רישוי` | law | chapter heading, verbatim |
| `Chapter B continued -- the provisions that did not change` | `פרק ב׳ המשך — ההוראות שלא שונו` | regulations | פרק ב׳ is the Regulations' own chapter heading; regs 3-5 did not move |
| `Chapter C -- Duties of a licence holder` | `פרק ג׳ — חובות בעל רישיון` | composed | the Law's chapter ג׳ has no printed subtitle in the wikitext deposited |
| `Chapter G -- Miscellaneous` | `פרק ז׳ — שונות` | composed | s.63 sits in the Law's last chapter |
| `Illustrations` | `דוגמאות` | composed | the encoding's own section, in both modules |
| `Illustrations -- one rule, three vintages of the law` | `דוגמאות — כלל אחד, שלושה נוסחים של הדין` | composed | the demonstration: same question, three dates, three answers |
| `reg. 1 Definitions` | `תקנה 1 הגדרות` | regulations | reg. 1 heading; the gazette prints הגדרה with an erratum note [צ״ל: הגדרות] |
| `reg. 2 -- what an appellant must tender in all` | `תקנה 2 -- הסכום הכולל שעל מגיש ההשגה לשלם` | regulations | section title, composed; reg. 2(b)/(c) ‘נוסף על התשלום’ |
| `reg. 2 Fees -- the one rule, on the rule-effective-time axis` | `תקנה 2 אגרות — הכלל האחד, על ציר תחילת הדין` | composed | names the design: one rule for reg. 2, selecting its text off the axis |
| `reg. 2 Fees -- the text as amended, Kovetz HaTakanot 5786 p. 2062` | `תקנה 2 אגרות — הנוסח כפי שתוקן, ק״ת התשפ״ו עמ׳ 2062` | regulations | the gazette reference is the issue's own |
| `reg. 2 Fees -- the text as made, Kovetz HaTakanot 5785 p. 2116` | `תקנה 2 אגרות — הנוסח כפי שהותקן, ק״ת התשפ״ה עמ׳ 2116` | regulations | the gazette reference is the issue's own |
| `reg. 2 on the rule-effective-time axis` | `תקנה 2 על ציר תחילת הדין` | composed | family g of the generated suite |
| `reg. 3 -- the annual indexation of the fees` | `תקנה 3 — עדכון האגרות השנתי` | composed | the encoding's own |
| `reg. 3 Updating of fees` | `תקנה 3 עדכון אגרות` | regulations | reg. 3 heading, verbatim |
| `reg. 4 Payment of the fee as a condition of a licence or an examination` | `תקנה 4 תשלום אגרה כתנאי למתן רישיון או ביצוע בחינות` | regulations | reg. 4 heading, verbatim |
| `reg. 5 Commencement` | `תקנה 5 תחילה` | regulations | reg. 5 heading, verbatim |
| `s.16 Duty to report a change of details` | `סעיף 16 חובת עדכון פרטים` | law | s.16 heading, verbatim |
| `s.17 Continuing education` | `סעיף 17 חובת השתתפות בהשתלמויות` | law | s.17 heading, verbatim |
| `s.2 Definitions -- licence grades` | `סעיף 2 הגדרות — דרגות הרישיון` | law | s.2 heading הגדרות, narrowed to the grades |
| `s.3 Duty to hold a licence` | `סעיף 3 חובת רישוי` | law | s.3 heading, verbatim |
| `s.6 Conditions for the grant of a licence, with the Second Schedule` | `סעיף 6 תנאים למתן רישיון, עם התוספת השנייה` | law | s.6 heading, verbatim, plus the Schedule it sends you to |
| `s.6 with the Second Schedule -- the sunset on the experience route` | `סעיף 6 עם התוספת השנייה — פקיעת מסלול הניסיון` | composed | ‘פקיעה’ is ours; column C says הוראה זו תעמוד בתוקף לתקופה של שלוש שנים |
| `s.63 -- commencement` | `סעיף 63 — תחילה` | law | s.63 heading, shortened |
| `s.63 Commencement` | `סעיף 63 תחילה ותחולה` | law | s.63 heading, verbatim |
| `s.7 Exemptions from parts of the training` | `סעיף 7 פטור מהכשרה` | law | s.7 heading, verbatim |
| `s.8 -- the period of validity of a licence` | `סעיף 8 — תקופת תוקפו של רישיון` | law | s.8 heading, shortened |
| `s.8 Period of validity and renewal` | `סעיף 8 תקופת תוקפו של רישיון וחידושו` | law | s.8 heading, verbatim |
| `s.9 -- the foreign expert's temporary licence` | `סעיף 9 — הרישיון הזמני של המומחה הזר` | law | s.9 heading, re-ordered |
| `s.9 Temporary licence for a foreign expert` | `סעיף 9 רישיון זמני למומחה זר` | law | s.9 heading, verbatim |
| `ss.2 and 3 -- the grades and the duty to hold a licence` | `סעיפים 2 ו־3 — הדרגות וחובת הרישוי` | law | s.3 heading חובת רישוי |
| `The draft's expectations, against the Regulations as made` | `ציפיות הטיוטה, כנגד התקנות כפי שהותקנו` | composed | the encoding's own |
| `The same, as assertions` | `אותו הדבר, כטענות` | composed | the illustrations restated as checkable assertions |
| `The SimpLEX draft -- a counterfactual, OFF the time axis` | `טיוטת SimpLEX — תרחיש נגדי, מחוץ לציר הזמן` | composed | the draft was never in force and has no יום תחילה, so it is not a point on the axis |
| `The two points on the rule-effective-time axis` | `שתי נקודות הזמן שעל ציר תחילת הדין` | composed | the two commencement days that divide the axis; no counterpart in either instrument |
| `Three days to ask the same question on` | `שלושה ימים שבהם נשאלת אותה שאלה` | composed | the three sample dates the tier 2 tests pin the axis to |
| `Tier 1 -- the SimpLEX test table, against the draft it was written for` | `שכבה 1 — טבלת הבדיקות של SimpLEX, כנגד הטיוטה שלמענה נכתבה` | composed | the encoding's own |
| `Tier 1 -- the SimpLEX test table, in its own words` | `שכבה 1 — טבלת הבדיקות של SimpLEX, בלשונה שלה` | composed | the encoding's own |
| `Tier 2 -- before the Regulations commenced` | `שכבה 2 — לפני תחילתן של התקנות` | composed | תחילתן is reg. 5's own word |
| `Tier 2 -- the day the amendment commenced` | `שכבה 2 — יום תחילתו של התיקון` | composed | the boundary fork F6 turns on |
| `Tier 2 -- the same scenarios against the Regulations as amended` | `שכבה 2 — אותם תרחישים כנגד התקנות כפי שתוקנו` | composed | the encoding's own |
| `Tier 2 -- the same scenarios against the Regulations as made` | `שכבה 2 — אותם תרחישים כנגד התקנות כפי שהותקנו` | composed | the encoding's own |
| `Tier 2 -- what the texts say, side by side` | `שכבה 2 — מה אומרים הנוסחים, זה לצד זה` | composed | replaces the old "three texts" heading: two are vintages, one is a draft |

## Modules

Hebrew module basenames do not work: an `IMPORT` of one resolves to nothing, silently.
See `NOTES.md` § 4 for the measurement. The Hebrew row therefore keeps Latin filenames with a `-he` suffix.

| English module | Hebrew module |
| --- | --- |
| `hvac-law.l4` | `hvac-law-he.l4` |
| `hvac-fees.l4` | `hvac-fees-he.l4` |
| `hvac-tests-simplex.l4` | `hvac-tests-simplex-he.l4` |
| `hvac-tests-simplex-red.l4` | `hvac-tests-simplex-red-he.l4` |
| `hvac-tests-generated.l4` | `hvac-tests-generated-he.l4` |

## Prose that is translated, not renamed

`@export` and `@desc` carry sentences, not identifiers, so they are translated whole from the glossary's `prose` map rather than composed out of renamed parts. There are 25 of them.

## Comments

15 comment blocks quote the statute or the regulations in ENGLISH TRANSLATION in the English row; each is replaced by the Hebrew original from `source/law.wiki` or `source/regulations-fees.wiki`.
Every other comment stays English on purpose: the rules are for Hebrew readers, the commentary around them is addressed to whoever maintains the encoding.
The one place the Hebrew original could not be used is the **SimpLEX draft** vintage of regulation 2, whose only witness is a screen capture in a published paper; those comments stay in the English translation the English row made, and say so.
