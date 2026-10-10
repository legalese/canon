#!/usr/bin/env python3
"""Build ../../registers/fork-register.json: NOTES.md section 3 (the 38 forks F1..F38) in the pipeline's fork-register format.

  python3 -I tools/make_fork_register.py            write the register (and check it)
  python3 -I tools/make_fork_register.py --check    check the written register without rewriting it
  python3 -I tools/make_fork_register.py --check --schema FILE --external FILE
                                                    also validate against a JSON schema file, and resolve cross_refs
                                                    against an external-modifications register file

The register re-expresses the fork register of NOTES.md; it decides nothing new. The structured data below is a Python literal.
Every source.quote is TAKEN FROM the raw text by this script (a range of lines and a regular expression that selects the
ambiguous words); nothing in a quote is typed. The check asserts that each quote is a substring of the raw text (whitespace
collapsed, so a quote may run across a line break but never across a page header), that each anchor is a definition in its
module, and every x-rule of the schema.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROW = os.path.dirname(HERE)
RAWDIR = os.path.normpath(os.path.join(ROW, "..", "..", "source", "raw"))
OUT = os.path.normpath(os.path.join(ROW, "..", "..", "registers", "fork-register.json"))
FILES = {
    "q": "law08-2022-qh15.txt",
    "b": "law08-2022-qh15-577-578.txt",
    "a": "law139-2025-qh15.txt",
}
PREFIX = "subjects/vn/insurance-business-law-08-2022/encodings/legalese-2026-10-vn-29/"
P2_IDS = {"AM139", "AM139b", "GUIDE46"}  # entry ids of the P2 external-modifications register
LAW08 = "Luật Kinh doanh bảo hiểm số 08/2022/QH15"
LAW139 = "Luật số 139/2025/QH15"


def P(art):
    return {"kind": "provision", "cite": f"{LAW08}, {art}"}


def A(art):
    return {"kind": "provision", "cite": f"{LAW139}, {art}"}


def R(id, description, status, citations, why=None):
    """A reading. `why` is the rejection_rationale (rejected) or the foreclosure (arguable); live readings carry none."""
    r = {"id": id, "description": description, "status": status, "citations": citations}
    if status == "rejected":
        r["rejection_rationale"] = why
    elif status == "arguable":
        r["foreclosure"] = why
    else:
        assert why is None
    return r


def Q(file, a, b, pattern):
    """A quote: lines a..b of the raw file `file` ('q', 'b' or 'a'), the span matched by `pattern`."""
    return (file, a, b, pattern)


# --- the forks -------------------------------------------------------------------------------------------------------
# Each: id, kind, materialisation, delegated_field, module, anchor, provisions, quote, source citations, readings,
# taken (reading, mechanism-implied-by-materialisation, rationale), cross_refs, notes
E = []


def fork(id, kind, mat, module, anchor, provisions, quote, cites, readings, taken, cross_refs, notes=None, delegated_field=None):
    E.append(dict(id=id, kind=kind, mat=mat, module=module, anchor=anchor, provisions=provisions, quote=quote, cites=cites,
                  readings=readings, taken=taken, cross_refs=cross_refs, notes=notes or [], delegated_field=delegated_field))


fork("F1", "fact-convention", "resolved-at-encode", "law08-ch2-general.l4", "Dieu 31(1): the last day for the insurer to pay",
     ["Điều 30", "Điều 31", "Điều 35", "Điều 37", "Điều 70", "Điều 72", "Điều 74", "Điều 80", "Điều 83", "Điều 93", "Điều 96",
      "Điều 112", "Điều 113", "Điều 136"],
     Q("q", 723, 724, r"trong thời hạn 15 ngày kể từ ngày nhận được đầy đủ hồ sơ hợp lệ"),
     [P("Điều 31(1)"), P("Điều 117(2)")],
     [R("CalendarDays", "A period counted in 'ngày' is counted in calendar days, from the day named as day 0 (the last day is that day plus N).",
        "live", [P("Điều 117(2)")]),
      R("WorkingDays", "A period counted in 'ngày' is counted in working days.", "rejected", [P("Điều 117(2)")],
        "Điều 117(2) writes 'ngày làm việc' (working days) where it means them; the contrast shows the plain 'ngày' is not that.")],
     ("CalendarDays", "Điều 117(2) writes 'ngày làm việc' (working days) where it means them (src:2559, 2562, 2564); the Law defines neither phrase. The contrast licenses calendar days for the plain 'ngày'. Outside knowledge about the Civil Code's rules on periods is not used."),
     [],
     ["The quoted clause is one example of the plain 'ngày'; the fork covers every period the NOTES lists. Source lines in NOTES: src:707-708, 723, 761-762, 782, 1307, 1336-1342, 1394-1400, 1541-1542, 1652, 1972, 2039, 2343, 2396-2415."])

fork("F2", "encoding-placement", "resolved-at-encode", "law08-vintage.l4", "the date Law 08/2022/QH15 took effect (V1 begins)",
     ["Điều 156(1)"], Q("b", 524, 525, r"Luật này có hiệu lực thi hành kể từ ngày 01 tháng 01 năm 2023"),
     [P("Điều 156(1)")],
     [R("OnlyDatedRulesRefuse", "A rule that reads no vintage date does not refuse for a date before 1 January 2023; only a rule with a dated arm has a pre-commencement arm and refuses there.",
        "live", [P("Điều 156(1)")]),
      R("EveryRuleRefusesBefore2023", "Every rule refuses for a date before the commencement.", "rejected", [P("Điều 156(1)")],
        "Only a rule with a dated arm has a pre-commencement arm to write; the others quote one text. A question about a date before 2023 should be asked of a pinned vintage.")],
     ("OnlyDatedRulesRefuse", "Only a rule with a dated arm has a pre-commencement arm to write; the others quote one text. A question about a date before 2023 should be asked of a pinned vintage (the tests do)."),
     [])

fork("F3", "statutory-wording", "resolved-at-encode", "law08-ch1-general.l4", "Dieu 3(1): the later law meets the condition of Dieu 3(1)",
     ["Điều 3(1)"], Q("q", 55, 56, r"thì phải xác định cụ thể nội dung thực hiện hoặc không thực hiện theo quy định của Luật này"),
     [P("Điều 3(1)")],
     [R("ConditionOnly", "The text states the condition (the later law must say specifically what content of this Law it applies or does not apply) and no consequence; the encoding asserts the condition and no consequence.",
        "live", [P("Điều 3(1)")]),
      R("DifferingProvisionIneffective", "A later law that differs without saying what content it applies has the differing provision ineffective.", "arguable", [P("Điều 3(1)")],
        "The Law states no consequence; the encoding asserts none, so it does not execute this reading."),
      R("LaterLawPrevails", "The later law prevails despite not saying what content it applies.", "arguable", [P("Điều 3(1)")],
        "The Law states no consequence; the encoding asserts none, so it does not execute this reading."),
      R("ThisLawPrevails", "This Law prevails over a later law that does not say what content it applies.", "arguable", [P("Điều 3(1)")],
        "The Law states no consequence; the encoding asserts none, so it does not execute this reading.")],
     ("ConditionOnly", "The text states the condition and no consequence, so the rule answers only whether the condition is met."),
     [],
     ["NOTES records 'Taken: None'. The schema requires a taken reading, so the stance actually taken (assert the condition and no consequence) is represented as a live reading, and the three consequence readings the encoding does not assert are 'arguable'. No reading was chosen on argument."])

fork("F4", "statutory-wording", "resolved-at-encode", "law08-ch1-general.l4", "Dieu 4(6): the activity is insurance brokerage activity",
     ["Điều 4(6)"], Q("q", 99, 100, r"chi nhánh nước ngoài tại Việt Nam; các hoạt động liên quan đến việc đàm phán, thu xếp giao kết và thực hiện hợp đồng bảo hiểm, tái bảo hiểm"),
     [P("Điều 4(6)")],
     [R("EitherLimb", "Either limb makes the activity brokerage: giving information and advice to the policyholder, or the activities of negotiating, arranging and performing the contract.", "live", [P("Điều 4(6)")]),
      R("BothLimbs", "Both limbs are needed.", "rejected", [P("Điều 4(6)")],
        "The semicolon after the first limb introduces a second activity of the same kind, not a further condition.")],
     ("EitherLimb", "The semicolon after the first limb ('...doanh nghiệp tái bảo hiểm, chi nhánh nước ngoài tại Việt Nam;') introduces a second activity of the same kind, not a further condition."),
     [])

fork("F5", "vagueness", "delegated-to-fact", "law08-ch1-general.l4", "Dieu 8(2): the product is compulsory insurance",
     ["Điều 8(2)(c)"], Q("a", 321, 322, r"Thay thế cụm từ “hoạt động đầu tư xây dựng” bằng cụm từ “hoạt động xây dựng” tại Điều 8"),
     [P("Điều 8(2)(c)"), A("Điều 2(1)")],
     [R("TwoPhrasesTwoFacts", "The encoding does not decide whether 'hoạt động xây dựng' is wider, narrower or the same as 'hoạt động đầu tư xây dựng': each phrase is a separate input fact, the V1 phrase read in V1 and the V2 phrase in V2.", "live",
        [P("Điều 8(2)(c)"), A("Điều 2(1)")]),
      R("PhraseWider", "'Hoạt động xây dựng' is wider than 'hoạt động đầu tư xây dựng'.", "arguable", [A("Điều 2(1)")],
        "Neither phrase is defined in the sources and the encoding takes no position on scope; it does not execute this reading."),
      R("PhraseNarrower", "'Hoạt động xây dựng' is narrower than 'hoạt động đầu tư xây dựng'.", "arguable", [A("Điều 2(1)")],
        "Neither phrase is defined in the sources and the encoding takes no position on scope; it does not execute this reading."),
      R("PhraseSame", "The two phrases cover the same ground.", "arguable", [A("Điều 2(1)")],
        "Neither phrase is defined in the sources and the encoding takes no position on scope; it does not execute this reading.")],
     ("TwoPhrasesTwoFacts", "Any reading would rest on the law on construction, which is not a source (outside knowledge, unverified), so the two phrases are two separate input facts."),
     ["AM139"],
     ["NOTES records 'Taken: None'. The schema requires a taken reading, so the stance actually taken (the scope relation is left to the fact-supplier through two input flags) is represented as a live reading; the three scope relations are 'arguable'. No reading was chosen on argument.",
      "The delegated field is a pair: one flag per vintage's phrase."],
     delegated_field="is insurance in construction investment activity (V1) / is insurance in construction activity (V2)")

fork("F6", "statutory-wording", "resolved-at-encode", "law08-ch3-scope.l4", "the product is a short health product or a short death-risk product",
     ["Điều 63(3)(b)-(c)"], Q("q", 1160, 1161, r"có thời hạn từ 01 năm trở xuống và các sản phẩm bảo hiểm cho rủi ro tử vong có thời hạn từ 01 năm trở xuống"),
     [P("Điều 63(3)(b)"), P("Điều 63(3)(c)"), A("Điều 1(2)")],
     [R("InclusiveTwelveMonthsEachProductSeparately", "'Từ 01 năm trở xuống' is a term of 12 months or less, and the two products of (b) are each separately allowed.", "live", [P("Điều 63(3)(b)")]),
      R("StrictlyUnderOneYear", "'Từ 01 năm trở xuống' means strictly under one year.", "rejected", [P("Điều 63(3)(b)")],
        "'Trở xuống' means 'and below', so the bound is inclusive."),
      R("BothProductsTogether", "'Và' joins two products that must both be offered together.", "rejected", [P("Điều 63(3)(b)")],
        "The list of exceptions would be empty if 'và' required both products at once.")],
     ("InclusiveTwelveMonthsEachProductSeparately", "'Trở xuống' means 'and below', so the bound is inclusive; the list of exceptions would be empty if 'và' required both products at once."),
     ["AM139"],
     ["NOTES gives two sub-questions: the bound ((i) 12 months or less, (ii) strictly under one year) and 'và' ((i) each product separately, (ii) both together). The taken combination is (i)+(i), recorded as one live reading; each rejected sub-reading is its own reading."])

fork("F7", "statutory-wording", "resolved-at-encode", "law08-ch2-general.l4", "Dieu 22(2): the premium the insurer must refund",
     ["Điều 22(2)", "Điều 35", "Điều 47(2)"], Q("q", 549, 551, r"hoàn lại phí bảo hiểm cho bên mua bảo hiểm sau khi trừ đi các chi phí hợp lý \(nếu có\)"),
     [P("Điều 22(2)"), P("Điều 35"), P("Điều 47(2)")],
     [R("RefuseWhenCostsExceed", "A refund net of reasonable costs cannot be negative: where the costs exceed the premium the rule refuses.", "live", [P("Điều 22(2)")]),
      R("RefundZero", "Where the costs exceed the premium the refund is zero.", "arguable", [P("Điều 22(2)")],
        "The Law says nothing on the floor and the encoding refuses rather than computing a zero; it does not execute this reading."),
      R("InsuredOwesDifference", "Where the costs exceed the premium the policyholder owes the difference.", "arguable", [P("Điều 22(2)")],
        "The Law says nothing on the floor and the encoding refuses rather than computing a debt; it does not execute this reading.")],
     ("RefuseWhenCostsExceed", "The Law says 'sau khi trừ các chi phí hợp lý (nếu có)' and nothing on the floor."),
     [])

fork("F8", "statutory-wording", "resolved-at-encode", "law08-ch2-general.l4", "Dieu 26: the party has the right to terminate on the ground",
     ["Điều 26"], Q("q", 624, 626, r"Doanh nghiệp bảo hiểm, chi nhánh doanh nghiệp bảo hiểm phi nhân thọ nước ngoài hoặc bên mua bảo hiểm có quyền đơn phương chấm dứt thực hiện hợp đồng bảo hiểm"),
     [P("Điều 26")],
     [R("SideImpliedByGround", "Each ground belongs to the side the ground implies: non-payment and unsafe property, the insurer; non-acceptance of a change of risk, either; refusal of a portfolio transfer, the policyholder.", "live", [P("Điều 26")]),
      R("EitherSideOnEveryGround", "Either side may terminate on every ground.", "rejected", [P("Điều 26")],
        "It would let a policyholder who stopped paying terminate for non-payment.")],
     ("SideImpliedByGround", "The chapeau gives the right to 'doanh nghiệp bảo hiểm ... hoặc bên mua bảo hiểm' without allocating; reading it for either side on every ground would let a policyholder who stopped paying 'terminate for non-payment'."),
     [])

fork("F9", "statutory-wording", "resolved-at-encode", "law08-ch2-general.l4", "Dieu 28: the transfer takes effect",
     ["Điều 28"], Q("q", 685, 685, r"Việc chuyển giao hợp đồng bảo hiểm chỉ có hiệu lực khi bên mua bảo hiểm"),
     [P("Điều 28")],
     [R("AllThreeConditionsOfEffect", "The insured person's consent (life), the transferee's insurable interest, and notice plus the insurer's consent are all required for the transfer to take effect.", "live", [P("Điều 28")]),
      R("OnlyParagraph3IsCondition", "Only paragraph 3 is a condition of effect.", "arguable", [P("Điều 28")],
        "Paragraphs 1 and 2 are written as requirements ('phải được', 'phải có') on the transfer; the encoding treats them as conditions of effect and does not execute this reading.")],
     ("AllThreeConditionsOfEffect", "Paragraph 2 says the transferee 'phải có' an insurable interest and paragraph 1 requires the written consent; paragraph 3 alone speaks of effect ('chỉ có hiệu lực khi')."),
     [])

fork("F10", "fact-convention", "resolved-at-encode", "law08-ch2-general.l4", "Dieu 30: the last day for submitting the claim dossier",
     ["Điều 30(1)"], Q("q", 708, 709, r"là 01 năm kể từ ngày xảy ra sự kiện bảo hiểm\. Thời gian xảy ra sự kiện bất khả kháng hoặc trở ngại khách quan không tính vào thời hạn"),
     [P("Điều 30(1)")],
     [R("AnniversaryPlusForceMajeureDays", "The last day of the one year is the anniversary of the starting day, plus the force majeure days.", "live", [P("Điều 30(1)")]),
      R("DayBeforeAnniversary", "The last day is the day before the anniversary.", "arguable", [P("Điều 30(1)")],
        "The encoding adds a year to the starting day and does not subtract one; it does not execute this reading.")],
     ("AnniversaryPlusForceMajeureDays", "'01 năm kể từ ngày xảy ra sự kiện' fixes a year from a day; the Law does not say whether the starting day counts."),
     [],
     ["The leap-day start (29 February) is not decided and no test asserts it: the library's `add years` clamps to 28 February."])

fork("F11", "statutory-wording", "resolved-at-encode", "law08-ch2-general.l4", "Dieu 30: the day from which the year runs",
     ["Điều 30(2)-(3)"], Q("q", 712, 714, r"thời hạn quy định tại khoản 1 Điều này được tính từ ngày người được bảo hiểm hoặc người thụ hưởng biết việc xảy ra sự kiện bảo hiểm đó"),
     [P("Điều 30(2)"), P("Điều 30(3)")],
     [R("ThirdPartyDemandFirst", "Where the claimant did not know of the event and a third person has also made a demand, the year runs from the third person's demand.", "live", [P("Điều 30(3)")]),
      R("DayClaimantLearnedFirst", "The year runs from the day the claimant learned of the event.", "rejected", [P("Điều 30(2)")],
        "Paragraph 3 is the more specific (liability) rule.")],
     ("ThirdPartyDemandFirst", "Both paragraphs say the period of paragraph 1 is counted from a stated day; paragraph 3 is the more specific (liability) rule."),
     [],
     ["The quote is paragraph 2's clause; paragraph 3's is 'thời hạn quy định tại khoản 1 Điều này được tính từ ngày người thứ ba yêu cầu' (src:717)."])

fork("F12", "fact-convention", "delegated-to-fact", "law08-ch2-general.l4", "Dieu 31(2): the interest on the late payment",
     ["Điều 31(2)"], Q("q", 728, 729, r"Lãi suất đối với số tiền chậm trả được xác định theo thỏa thuận của các bên theo quy định của Bộ luật Dân sự"),
     [P("Điều 31(2)")],
     [R("PerDayRateInput", "The interest rate is the parties' (Civil Code) and is taken as a rate per day, supplied as an input; there is no default.", "live", [P("Điều 31(2)")]),
      R("PerYearRateInput", "The rate is a per-year input applied with a 365-day year.", "arguable", [P("Điều 31(2)")],
        "The input field is a per-day rate and the encoding does not convert a per-year rate; it does not execute this reading."),
      R("DefaultRate", "The rule supplies a default rate where the parties agreed none.", "rejected", [P("Điều 31(2)")],
        "The rate and its unit come from outside the sources and the encoding invents no default.")],
     ("PerDayRateInput", "'Lãi suất ... xác định theo thỏa thuận của các bên theo quy định của Bộ luật Dân sự': the rate and its unit come from outside the sources, and the encoding supplies no default."),
     [],
     delegated_field="daily interest rate agreed under the Civil Code")

fork("F13", "statutory-wording", "resolved-at-encode", "law08-ch2-general.l4", "Dieu 27(2): the premium the insurer must refund for the remaining period",
     ["Điều 27(2)"], Q("q", 660, 662, r"hoàn phí bảo hiểm đã đóng cho thời gian còn lại của hợp đồng bảo hiểm theo thỏa thuận trong hợp đồng bảo hiểm"),
     [P("Điều 27(2)")],
     [R("PremiumForRemainingPeriod", "The refund 'theo thỏa thuận' is taken as the premium paid for the remaining period.", "live", [P("Điều 27(2)")]),
      R("PremiumForRemainingPeriodLessCosts", "The refund is the premium for the remaining period less reasonable costs.", "rejected", [P("Điều 27(2)")],
        "Điều 27(2) allows no deduction, unlike Điều 22(2), 35 and 47.")],
     ("PremiumForRemainingPeriod", "Điều 27(2) allows no deduction, unlike Điều 22(2), 35 and 47."),
     [])

fork("F14", "fact-convention", "resolved-at-encode", "law08-ch2-life-health.l4", "Dieu 35: the contract has a term of more than one year",
     ["Điều 35"], Q("q", 761, 761, r"có thời hạn trên 01 năm"),
     [P("Điều 35")],
     [R("LastDayAfterFirstAnniversary", "A term is 'trên 01 năm' when the last day of the term falls after the first anniversary of the first day (1 January 2025 to 1 January 2026 is exactly a year; to 2 January 2026 is more).", "live", [P("Điều 35")]),
      R("Days366OrMore", "A term is more than a year when it is 366 days or more.", "arguable", [P("Điều 35")],
        "The Law does not say how a term is measured; the encoding measures by anniversary and does not execute this reading."),
      R("InclusiveCountingOfLastDay", "The last day of the term is counted inclusively when measuring the year.", "arguable", [P("Điều 35")],
        "The Law does not say how a term is measured; the encoding measures by anniversary and does not execute this reading.")],
     ("LastDayAfterFirstAnniversary", "The Law does not say how a term is measured, so it is measured by the anniversary of its first day."),
     [])

fork("F15", "fact-convention", "resolved-at-encode", "law08-ch2-life-health.l4", "Dieu 35: the last day to refuse to go on",
     ["Điều 35"], Q("q", 761, 762, r"trong thời hạn 21 ngày kể từ ngày nhận được hợp đồng bảo hiểm"),
     [P("Điều 35")],
     [R("DayOfReceiptIsDayZero", "The 21 days run from the day the policyholder receives the contract, which is day 0; the last day is the day of receipt plus 21.", "live", [P("Điều 35")]),
      R("DayOfReceiptIsDayOne", "The day of receipt is day 1; the last day is the day of receipt plus 20.", "arguable", [P("Điều 35")],
        "The encoding adds 21 days to the day of receipt; it does not execute this reading.")],
     ("DayOfReceiptIsDayZero", "'Trong thời hạn 21 ngày kể từ ngày nhận được' counts from the day of receipt."),
     [])

fork("F16", "statutory-wording", "resolved-at-encode", "law08-ch2-life-health.l4", "Dieu 35: the policyholder may refuse to go on",
     ["Điều 35"], Q("q", 761, 763, r"Đối với các hợp đồng bảo hiểm có thời hạn trên 01 năm, trong thời hạn 21 ngày kể từ ngày nhận được hợp đồng bảo hiểm, bên mua bảo hiểm có quyền từ chối tiếp tục tham gia bảo hiểm"),
     [P("Điều 35"), P("Điều 21(1)(đ)")],
     [R("EveryClassOfContract", "Điều 35 applies to every contract of more than a year, not only life and health, by its words.", "live", [P("Điều 35"), P("Điều 21(1)(đ)")]),
      R("LifeAndHealthOnly", "Điều 35 applies to life and health contracts only, by its placement under Mục 2.", "arguable", [P("Điều 35")],
        "The words of Điều 35 carry no limit to life and health and Điều 21(1)(đ) lists the right for the policyholder generally; the encoding applies it to every class and does not execute this reading.")],
     ("EveryClassOfContract", "The words begin 'Đối với các hợp đồng bảo hiểm có thời hạn trên 01 năm' with no limit; Điều 21(1)(đ) lists a right to rescind under Điều 35 for the policyholder in general."),
     [],
     ["The Mục 2 heading (src:737-739) is the text that makes the narrower reading arguable. NOTES finding W6."])

fork("F17", "vagueness", "delegated-to-fact", "law08-ch2-life-health.l4", "Dieu 37(2): the last day of the grace period",
     ["Điều 37(2)"], Q("q", 782, 782, r"thời gian gia hạn đóng phí là 60 ngày"),
     [P("Điều 37(2)")],
     [R("StartDateSuppliedAsInput", "The 60 days of grace run from a date the contract or the instalment fixes; the encoding takes that date as an input and does not say which event it is.", "live", [P("Điều 37(2)")]),
      R("FromDueDateOfUnpaidInstalment", "The grace period runs from the due date of the unpaid instalment.", "arguable", [P("Điều 37(2)")],
        "The text gives the length and not the start; the encoding takes the start date as an input and does not execute this reading."),
      R("FromInsurerNotice", "The grace period runs from notice by the insurer.", "arguable", [P("Điều 37(2)")],
        "The text gives the length and not the start; the encoding takes the start date as an input and does not execute this reading.")],
     ("StartDateSuppliedAsInput", "The text gives the length and not the start, so the start date is an input field."),
     [],
     ["NOTES records the reading taken as 'Neither: the start date is an input field' (not 'Taken: None', but the same stance). Represented as F3, F5 and F19 are: the stance is a live reading and the two start events are 'arguable'.",
      "DISCREPANCY: the instruction named F3, F5 and F19 as the forks with no reading taken; NOTES section 3 says the same of F17 ('Neither').",
      "NOTES section 3 gives the licence for F17 as 'The text gives the length and not the start'; this entry adds nothing to it."],
     delegated_field="date the grace period began")

fork("F18", "statutory-wording", "resolved-at-encode", "law08-ch2-life-health.l4", "Dieu 39: the contract on the death of another may be made",
     ["Điều 39(1)-(2)"], Q("q", 810, 811, r"Người chưa thành niên, trừ trường hợp cha, mẹ hoặc người giám hộ của người đó đồng ý bằng văn bản"),
     [P("Điều 39(1)"), P("Điều 39(2)")],
     [R("ParentConsentSatisfiesBoth", "For a minor the parent's or guardian's written consent also satisfies the person's own consent in paragraph 1.", "live", [P("Điều 39(2)")]),
      R("MinorOwnConsentAlsoNeeded", "The minor's own written consent is also needed.", "rejected", [P("Điều 39(1)")],
        "A minor's written consent to a contract on their own death is not a coherent requirement beside 39(2)(a).")],
     ("ParentConsentSatisfiesBoth", "A minor's written consent to a contract on their own death is not a coherent requirement beside 39(2)(a)."),
     [])

fork("F19", "statutory-wording", "delegated-to-fact", "law08-ch2-life-health.l4", "Dieu 40(3): the amount the insurer must return to the policyholder",
     ["Điều 40(3)"], Q("q", 836, 838, r"giá trị hoàn lại của hợp đồng bảo hiểm hoặc toàn bộ số phí bảo hiểm đã đóng sau khi trừ các chi phí hợp lý \(nếu có\) theo thỏa thuận trong hợp đồng bảo hiểm"),
     [P("Điều 40(3)")],
     [R("FigureSuppliedAsInput", "The amount returned is a single figure supplied as an input; the encoding does not say how it is formed from the surrender value or the premium less costs.", "live", [P("Điều 40(3)")]),
      R("SurrenderValueElsePremiumLessCosts", "The surrender value if there is one, else the premium less reasonable costs.", "arguable", [P("Điều 40(3)")],
        "The Law leaves the choice to the contract; the encoding computes no figure and does not execute this reading."),
      R("TheLarger", "The larger of the surrender value and the premium less reasonable costs.", "arguable", [P("Điều 40(3)")],
        "The Law leaves the choice to the contract; the encoding computes no figure and does not execute this reading."),
      R("ContractChooses", "The contract chooses between the surrender value and the premium less reasonable costs.", "arguable", [P("Điều 40(3)")],
        "The encoding does not model the contract's choice; it takes the resulting figure as an input.")],
     ("FigureSuppliedAsInput", "The Law leaves the choice to 'thỏa thuận trong hợp đồng bảo hiểm', so the figure is an input."),
     [],
     ["NOTES records 'Taken: None'. The schema requires a taken reading, so the stance actually taken (a single figure is an input) is represented as a live reading, and the three ways of forming the figure are 'arguable'. No reading was chosen on argument."],
     delegated_field="surrender value or premium paid, less reasonable costs")

fork("F20", "statutory-wording", "resolved-at-encode", "law08-ch2-property.l4", "Dieu 46: the compensation after the reduction",
     ["Điều 46(1)"], Q("q", 924, 926, r"có quyền giảm trừ số tiền phải bồi thường bảo hiểm tương ứng với thiệt hại mà doanh nghiệp bảo hiểm, chi nhánh doanh nghiệp bảo hiểm phi nhân thọ nước ngoài phải chịu"),
     [P("Điều 46(1)")],
     [R("FloorAtZero", "The reduction cannot take the compensation below zero.", "live", [P("Điều 46(1)")]),
      R("RefuseWhenReductionExceeds", "Where the reduction would exceed the compensation the rule refuses.", "arguable", [P("Điều 46(1)")],
        "The encoding floors the result at zero and does not execute this reading.")],
     ("FloorAtZero", "The reduction is 'tương ứng với thiệt hại mà' the insurer bears, which can exceed the compensation."),
     [])

fork("F21", "vagueness", "resolved-at-encode", "law08-ch2-property.l4", "the proportionate premium for the excess",
     ["Điều 47(2)(a)"], Q("q", 942, 944, r"số phí bảo hiểm đã đóng tương ứng với số tiền bảo hiểm vượt quá giá thị trường của tài sản được bảo hiểm tại thời điểm giao kết hợp đồng"),
     [P("Điều 47(2)(a)")],
     [R("PremiumTimesExcessOverSumInsured", "'Tương ứng' is premium x (sum insured - market value) / sum insured.", "live", [P("Điều 47(2)(a)")]),
      R("PremiumTimesExcessOverMarketValue", "'Tương ứng' is premium x excess / market value.", "rejected", [P("Điều 47(2)(a)")],
        "The premium paid is for the whole sum insured, so the part for the excess is the excess over the sum insured."),
      R("ProRataOverTerm", "'Tương ứng' is a pro rata over the term.", "arguable", [P("Điều 47(2)(a)")],
        "The Law states no time apportionment in 47(2)(a); the encoding apportions by amount and does not execute this reading.")],
     ("PremiumTimesExcessOverSumInsured", "The premium paid is for the whole sum insured, so the part for the excess is the excess over the sum insured."),
     [])

fork("F22", "vagueness", "resolved-at-encode", "law08-ch2-property.l4", "Dieu 47(2)(b): the compensation for the loss",
     ["Điều 47(2)(b)"], Q("q", 947, 949, r"chỉ chịu trách nhiệm bồi thường thiệt hại tương ứng với giá thị trường của tài sản được bảo hiểm tại thời điểm xảy ra thiệt hại"),
     [P("Điều 47(2)(b)")],
     [R("CappedAtMarketValueAtLoss", "The compensation is the lesser of the loss and the market value at the time and place of the loss.", "live", [P("Điều 47(2)(b)")]),
      R("RatioOfMarketValueToSumInsured", "The compensation is the loss in the ratio of the market value to the sum insured.", "rejected", [P("Điều 47(2)(b)")],
        "A ratio would need a stated denominator, and the sentence says the insurer 'chỉ chịu trách nhiệm' for the loss corresponding to the market value, which reads as a cap.")],
     ("CappedAtMarketValueAtLoss", "The sentence says the insurer 'chỉ chịu trách nhiệm' for the loss corresponding to the market value, which reads as a cap; a ratio would need a stated denominator."),
     [])

fork("F23", "fact-convention", "resolved-at-encode", "law08-ch3-solvency.l4", "the next working day after",
     ["Điều 117(2)-(3)"], Q("q", 2559, 2559, r"Trong thời hạn 07 ngày làm việc kể từ ngày kết thúc thời hạn gửi báo cáo"),
     [P("Điều 117(2)")],
     [R("WeekendsExcludedHolidaysSupplied", "Saturday and Sunday are not working days and a calendar of other non-working days is supplied as an input.", "live", [P("Điều 117(2)")]),
      R("SixDayWeek", "Only Sunday is a non-working day.", "arguable", [P("Điều 117(2)")],
        "The encoding excludes Saturday and Sunday and does not execute this reading."),
      R("NoCalendarRefuse", "With no calendar of non-working days the rule refuses.", "arguable", [P("Điều 117(2)")],
        "The encoding takes the calendar as a list of dates (possibly empty) and applies the weekend rule alone; it does not refuse on an empty list.")],
     ("WeekendsExcludedHolidaysSupplied", "The Law defines 'ngày làm việc' nowhere in the sources. Which weekdays are working days in Vietnam is outside the sources, so holidays are an input and only the weekend rule is assumed."),
     ["AM139"],
     ["The holiday calendar is an input parameter (`the non-working days supplied`), not a record field; the weekend rule is encoded. The entry is therefore recorded as resolved-at-encode. Điều 117(3) is repealed by Law 139/2025/QH15 Điều 2(7) from V2."])

fork("F24", "statutory-wording", "resolved-at-encode", "law08-ch3-finance.l4", "Dieu 98(2): the contribution to the compulsory reserve fund for the year",
     ["Điều 98(2)"], Q("q", 2074, 2075, r"Quỹ dự trữ bắt buộc được trích hằng năm theo tỷ lệ 05% lợi nhuận sau thuế cho đến khi bằng mức tối đa theo quy định của Chính phủ"),
     [P("Điều 98(2)")],
     [R("CappedByRoomLeft", "The last year's contribution is 5% of after-tax profit limited to the room left under the maximum.", "live", [P("Điều 98(2)")]),
      R("AlwaysFivePercentThenStop", "The contribution is always 5% of after-tax profit, then stops once the maximum is reached.", "arguable", [P("Điều 98(2)")],
        "The encoding limits the final contribution to the room left and does not execute this reading.")],
     ("CappedByRoomLeft", "'Cho đến khi bằng mức tối đa' — until the fund equals the maximum."),
     [])

fork("F25", "statutory-wording", "resolved-at-encode", "law08-ch3-finance.l4", "Dieu 101: the insurer meets the requirements on separating sources",
     ["Điều 101(2)"], Q("a", 211, 213, r"Doanh nghiệp bảo hiểm phi nhân thọ, chi nhánh doanh nghiệp bảo hiểm phi nhân thọ nước ngoài phải thông báo bằng văn bản cho Bộ Tài chính nguyên tắc tách nguồn vốn chủ sở hữu và nguồn phí bảo hiểm"),
     [A("Điều 1(8)")],
     [R("NoDutyForReinsurerOrMutual", "In V2 the second paragraph of Điều 101(2) names no duty for a reinsurer or a mutual organisation, so none is applied.", "live", [A("Điều 1(8)")]),
      R("NonLifeDutyExtendsToReinsurers", "The non-life notice duty extends to reinsurers.", "rejected", [A("Điều 1(8)")],
        "The paragraph names life insurers and non-life insurers or branches only.")],
     ("NoDutyForReinsurerOrMutual", "The paragraph names life insurers and non-life insurers or branches only."),
     ["AM139"])

fork("F26", "statutory-wording", "resolved-at-encode", "law08-ch3-licensing.l4", "the member reaches the Government's minimum if one is supplied",
     ["Điều 65(1)(d)", "Điều 65(2)", "Điều 65(3)"], Q("q", 1227, 1228, r"Căn cứ quy định tại điểm d khoản 1 và khoản 2 Điều này, Chính phủ quy định cụ thể mức tổng tài sản tối thiểu phù hợp với từng thời kỳ"),
     [P("Điều 65(3)")],
     [R("BothThresholdsApply", "The Law's two thresholds and the Government's minimum for the period both apply: the member must reach both.", "live", [P("Điều 65(3)")]),
      R("GovernmentFigureReplaces", "The Government's figure replaces the Law's.", "arguable", [P("Điều 65(3)")],
        "Paragraph 3 fixes the minimum on the basis of the Law's figures but does not say whether the Government may lower them; the encoding applies both and does not execute this reading.")],
     ("BothThresholdsApply", "Paragraph 3 says the Government fixes the minimum 'căn cứ quy định tại điểm d khoản 1 và khoản 2', i.e. on the basis of the Law's figures."),
     ["GUIDE46"],
     ["Whether the Government may set the figure lower than the Law's is not said (NOTES finding W10). The Government's figure is an optional input; the implementing instruments reported in GUIDE46 are the kind that would settle it, and were not read."])

fork("F27", "statutory-wording", "resolved-at-encode", "law08-ch2-property.l4", "Dieu 58(1): the insurer's liability arises",
     ["Điều 58(1)"], Q("q", 1084, 1086, r"chỉ phát sinh nếu người thứ ba yêu cầu người được bảo hiểm bồi thường do có hành vi gây thiệt hại cho người thứ ba trong thời hạn bảo hiểm"),
     [P("Điều 58(1)")],
     [R("OccurrenceRule", "'Trong thời hạn bảo hiểm' qualifies the act that caused the damage: the act occurred within the insurance term.", "live", [P("Điều 58(1)")]),
      R("ClaimsMadeRule", "'Trong thời hạn bảo hiểm' qualifies the third person's claim: the claim was made within the insurance term. Encoded as a separate function.", "live", [P("Điều 58(1)")])],
     ("OccurrenceRule", "The modifier follows both 'yêu cầu' and 'hành vi gây thiệt hại'; the sentence has no comma. The occurrence reading is the one used elsewhere in the encoding."),
     [],
     ["Both readings are executable: the claims-made reading is the function `Dieu 58(1): the insurer's liability arises (claims-made reading)` in the same module. NOTES finding W8."])

fork("F28", "statutory-wording", "resolved-at-encode", "law08-ch3-products.l4", "Dieu 87(3)-(3a): the premium method meets the requirement that applies to its product line",
     ["Điều 87(3)", "Điều 87(1)"], Q("q", 1780, 1782, r"tính phí bảo hiểm của các sản phẩm bảo hiểm thuộc nghiệp vụ bảo hiểm nhân thọ, bảo hiểm sức khỏe, bảo hiểm xe cơ giới, trừ bảo hiểm trách nhiệm dân sự của chủ xe cơ giới"),
     [P("Điều 87(3)"), P("Điều 87(1)"), A("Điều 1(7)")],
     [R("NoRequirementForUnnamedLine", "A product line the article does not name has no premium-method requirement.", "live", [P("Điều 87(1)")]),
      R("RefuseForUnnamedLine", "For a product line the article does not name the rule refuses.", "rejected", [P("Điều 87(1)")],
        "A refusal would mean the Law forbids what it does not mention.")],
     ("NoRequirementForUnnamedLine", "By Điều 87(1) the insurer is free ('chủ động, tự chịu trách nhiệm') in developing products; a refusal would mean the Law forbids what it does not mention."),
     ["AM139"])

fork("F29", "vagueness", "resolved-at-encode", "law08-ch3-licensing.l4", "Dieu 81: the chair or member of the board or members' council meets the conditions",
     ["Điều 81(2)(c)"], Q("q", 1563, 1564, r"giữ vị trí là người quản lý, điều hành, kiểm soát tại doanh nghiệp hoạt động trong lĩnh vực bảo hiểm, tài chính, ngân hàng"),
     [P("Điều 81(2)(c)"), A("Điều 1(5)")],
     [R("OneFieldForBothWords", "'Doanh nghiệp' (V1) and 'tổ chức' (V2) in the experience limb for board members are not distinguished: one field serves both vintages.", "live", [P("Điều 81(2)(c)"), A("Điều 1(5)")]),
      R("TwoFields", "'Doanh nghiệp' and 'tổ chức' are distinguished and carried in two fields.", "rejected", [P("Điều 81(2)(c)")],
        "The sources do not define either word; a witness would have no way to tell them apart.")],
     ("OneFieldForBothWords", "The sources do not define either word; a witness would have no way to tell them apart."),
     ["AM139"],
     ["The V2 widening for the chief executive (insurer-only versus any insurance, finance or banking organisation) is encoded with two fields, as NOTES says.",
      "DISCREPANCY: NOTES F29 contrasts 'doanh nghiệp' (V1) with 'tổ chức' (V2) only. The V2 text (src:a:92-93 and 98-99) also adds 'trực tiếp' ('tại tổ chức hoạt động trực tiếp trong lĩnh vực'), which V1 (src:1563-1564) lacks; the encoding's single field does not carry that difference and NOTES does not list it as a reading."])

fork("F30", "vagueness", "resolved-at-encode", "law08-ch4-intermediaries.l4", "Dieu 127(1): the individual may not be the agent of both principals",
     ["Điều 127(1)"], Q("q", 2736, 2737, r"hoạt động trong cùng loại hình bảo hiểm với doanh nghiệp bảo hiểm"),
     [P("Điều 127(1)"), P("Điều 63(3)(a)"), A("Điều 1(9)")],
     [R("OverlapOfTypesCarriedOn", "In V1, 'cùng loại hình bảo hiểm' is tested by the two principals carrying on a type of insurance in common.", "live", [P("Điều 63(3)(a)")]),
      R("PrimaryTypesOnly", "'Cùng loại hình bảo hiểm' compares the principals' own primary types.", "rejected", [P("Điều 63(3)(a)")],
        "The Law lets a life insurer carry on health insurance, so the 'type' of an insurer is a set.")],
     ("OverlapOfTypesCarriedOn", "The Law lets a life insurer carry on health insurance (Điều 63(3)(a)), so the 'type' of an insurer is a set."),
     ["AM139"],
     ["The V2 text of Điều 127(1) (Law 139/2025/QH15 Điều 1(9)) lists the pairs of principals directly, so this fork concerns the V1 text only."])

fork("F31", "statutory-wording", "resolved-at-encode", "law08-ch3-licensing.l4", "the founder meets limbs (b) and (c)",
     ["Điều 64(1)"], Q("q", 1169, 1171, r"Tổ chức có tư cách pháp nhân, đang hoạt động hợp pháp; trường hợp tham gia góp từ 10% vốn điều lệ trở lên thì phải kinh doanh có lãi trong 03 năm tài chính liên tục gần nhất"),
     [P("Điều 64(1)"), P("Điều 66(2)")],
     [R("LimbsAsDescribed", "Limb (a) applies to every founder (V1), limb (b) to organisations and limb (c) to licensed insurers founding a new one; '10% trở lên' includes 10%.", "live", [P("Điều 64(1)")]),
      R("LimbBAlsoToIndividuals", "Limb (b) also applies to individuals.", "rejected", [P("Điều 64(1)")],
        "Limb (b) begins 'Tổ chức có tư cách pháp nhân', and Điều 66(2) separately limits individuals to 10%.")],
     ("LimbsAsDescribed", "Limb (b) begins 'Tổ chức có tư cách pháp nhân'; Điều 66(2) separately limits individuals to 10%."),
     ["AM139"],
     ["Law 139/2025/QH15 Điều 2(7) repeals limb (a) of Điều 64(1) from V2."])

fork("F32", "fact-convention", "resolved-at-encode", "law08-ch3-licensing.l4", "Dieu 79: the governance structure is one the Law allows",
     ["Điều 79(1)(b)"], Q("q", 1504, 1504, r"ít nhất 20% số thành viên Hội đồng quản trị phải là thành viên độc lập"),
     [P("Điều 79(1)(b)")],
     [R("NoRounding", "'Ít nhất 20%' is tested without rounding: independent members at least 0.2 x the board (one of four and one of five pass, one of six fails).", "live", [P("Điều 79(1)(b)")]),
      R("RoundedUp", "The 20% is rounded up to a whole number of members.", "arguable", [P("Điều 79(1)(b)")],
        "No rounding rule is stated and the encoding applies none; it does not execute this reading.")],
     ("NoRounding", "No rounding rule is stated, so the figure is tested as written."),
     [])

fork("F33", "statutory-wording", "resolved-at-encode", "law08-ch2-life-health.l4", "Dieu 40(1): the insurer need not pay the claimant",
     ["Điều 40(1)(b)-(c)", "Điều 40(2)"], Q("q", 830, 833, r"nếu một hoặc một số người thụ hưởng cố ý gây ra cái chết hay thương tật vĩnh viễn cho người được bảo hiểm, doanh nghiệp bảo hiểm, chi nhánh doanh nghiệp bảo hiểm phi nhân thọ nước ngoài vẫn phải bồi thường, trả tiền bảo hiểm cho những người thụ hưởng khác"),
     [P("Điều 40(1)"), P("Điều 40(2)"), P("Điều 40(3)")],
     [R("OthersPaidFaultyNotPaid", "The beneficiary at fault is not paid and the other beneficiaries are; where there is a single beneficiary the exclusion applies to the claim, with the Điều 40(3) refund to the policyholder.", "live", [P("Điều 40(2)"), P("Điều 40(3)")]),
      R("InsurerPaysPolicyholderEstate", "Where there is a single beneficiary at fault the insurer pays the policyholder's estate.", "rejected", [P("Điều 40(2)")],
        "Paragraph 2 protects 'những người thụ hưởng khác' only.")],
     ("OthersPaidFaultyNotPaid", "Paragraph 2 protects 'những người thụ hưởng khác' only."),
     [])

fork("F34", "statutory-wording", "resolved-at-encode", "law08-ch3-finance.l4", "Dieu 99(2): the investment complies with the principles",
     ["Điều 99(2)(d)", "Điều 90(2)(đ)", "Điều 120(1)(m)"], Q("q", 2097, 2097, r"Không được đầu tư quá 30% nguồn vốn đầu tư"),
     [P("Điều 99(2)(d)"), P("Điều 90(2)(đ)"), P("Điều 120(1)(m)")],
     [R("FigureItselfPasses", "'Không quá 30%' (Điều 99(2)(d)), 'tối thiểu 75%' (Điều 90(2)(đ)) and '10% trở lên' (Điều 120(1)(m)) are tested with the figure itself passing.", "live", [P("Điều 99(2)(d)"), P("Điều 90(2)(đ)"), P("Điều 120(1)(m)")]),
      R("FigureItselfFails", "The bounds are exclusive.", "rejected", [P("Điều 99(2)(d)")],
        "'Không quá', 'tối thiểu' and 'trở lên' all include the figure.")],
     ("FigureItselfPasses", "'Không quá', 'tối thiểu' and 'trở lên' all include the figure."),
     [])

fork("F35", "statutory-wording", "resolved-at-encode", "law08-ch3-solvency.l4", "Dieu 120(1)(dd): the transfer of shares is unusual information",
     ["Điều 120(1)(đ)"], Q("q", 2602, 2603, r"Việc chuyển nhượng cổ phần, phần vốn góp dẫn đến có cổ đông, thành viên góp vốn sở hữu từ 10% vốn điều lệ trở lên hoặc giảm xuống dưới 10% vốn điều lệ"),
     [P("Điều 120(1)(đ)")],
     [R("CrossingEitherDirection", "A transfer that takes a holder to 10% or above, or below 10%, is unusual information; a move inside either band is not.", "live", [P("Điều 120(1)(đ)")]),
      R("AnyTransferByOrToTenPercentHolder", "Any transfer by or to a holder of 10% or more is unusual information.", "rejected", [P("Điều 120(1)(đ)")],
        "The text names the two crossings.")],
     ("CrossingEitherDirection", "The text names the two crossings."),
     [])

fork("F36", "fact-convention", "resolved-at-encode", "law08-ch3-licensing.l4", "Dieu 73(1): the last day to begin official operation",
     ["Điều 73(1)"], Q("q", 1350, 1351, r"thời gian gia hạn tối đa là 12 tháng"),
     [P("Điều 73(1)"), A("Điều 1(3)")],
     [R("TwelvePlusNMonthsFromLicence", "The extension is counted in months from the licence date: the last day is the licence date plus 12 + n months.", "live", [P("Điều 73(1)"), A("Điều 1(3)")]),
      R("NMonthsFromOriginalDeadline", "The extension is n months from the original deadline.", "arguable", [P("Điều 73(1)")],
        "It reaches the same date as the taken reading, so nothing in the encoding turns on it; the encoding does not execute it separately.")],
     ("TwelvePlusNMonthsFromLicence", "'Thời gian gia hạn tối đa là 12 tháng'; the original deadline is 12 months from the licence date."),
     ["AM139"],
     ["NOTES records the two readings as giving the same date."])

fork("F37", "encoding-placement", "resolved-at-encode", "law08-ch7-commencement.l4", "Dieu 156(2): the provision is in force on the day",
     ["Điều 156(2)"], Q("b", 528, 530, r"Khoản 3 Điều 86, khoản 4 và khoản 5 Điều 94, Điều 95, khoản 3 và khoản 4 Điều 99, các điều 109, 110, 111, 112, 113, 114 và 116 của Luật này có hiệu lực thi hành từ ngày 01 tháng 01 năm 2028"),
     [P("Điều 156(2)"), A("Điều 1(14)")],
     [R("DayAsSecondInput", "A deferred commencement is asked of two clocks: the text in force (the rule-version axis) and the day in the question, which is a second, explicit input.", "live", [P("Điều 156(2)"), A("Điều 1(14)")]),
      R("RuleVersionDateDoublesAsDay", "The rule-version date also serves as the day in the question.", "rejected", [P("Điều 156(2)")],
        "A question 'was Điều 110 in force on 1 June 2029' has a different answer under the text as made and under the amended text, and one clock cannot ask it.")],
     ("DayAsSecondInput", "A question 'was Điều 110 in force on 1 June 2029' has a different answer under the text as made and under the amended text; one clock cannot ask that."),
     ["AM139"])

fork("F38", "encoding-placement", "resolved-at-encode", "law08-ch1-general.l4", "Dieu 8(5): the premium of compulsory insurance",
     ["Điều 8(5)", "Điều 17(2)", "Điều 87(5)-(6)"], Q("q", 244, 245, r"Chính phủ quy định chi tiết về điều kiện bảo hiểm, mức phí bảo hiểm, số tiền bảo hiểm tối thiểu đối với bảo hiểm bắt buộc"),
     [P("Điều 8(5)")],
     [R("RefuseWhereNoFallback", "The Government's and the Minister's content is never supplied: a rule that needs it, where the article has no fallback of its own, refuses.", "live", [P("Điều 8(5)")]),
      R("UseLawsOwnDefault", "Where the article supplies its own default, that default is used (for example the 15 days of Điều 31(1)); no default is invented.", "live", [P("Điều 31(1)")])],
     ("RefuseWhereNoFallback", "'Inputs, never defaults': a delegated matter with no fallback in the article is refused rather than filled."),
     ["AM139", "GUIDE46"],
     ["NOTES gives the two readings as '(i) refuse; (ii) assume the Law's own default where it has one' and the reading taken as '(i) where the article has no fallback, (ii) never invented'. Both are therefore live; the first is recorded as the one taken and the second as the other reading the encoding executes.",
      "The delegations are listed in NOTES section 1; the entry's site is one of them."])


# --- building --------------------------------------------------------------------------------------------------------
_RAW = {}


def raw(kind):
    if kind not in _RAW:
        _RAW[kind] = open(os.path.join(RAWDIR, FILES[kind]), encoding="utf-8").read()
    return _RAW[kind]


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def take(spec):
    kind, a, b, pat = spec
    lines = raw(kind).split("\n")
    seg = norm(" ".join(lines[a - 1 : b]))
    m = re.search(pat, seg)
    if not m:
        sys.exit(f"quote pattern not found in {FILES[kind]} lines {a}-{b}: {pat!r}\n  segment: {seg[:400]}")
    quote = m.group(0)
    assert quote in norm(raw(kind)), (quote, "not a substring of the raw text")
    return quote


def build():
    entries = []
    for e in E:
        mech = {"resolved-at-encode": "encoded", "delegated-to-fact": "fact-supplied"}[e["mat"]]
        ent = {
            "id": e["id"],
            "kind": e["kind"],
            "materialisation": e["mat"],
        }
        if e["delegated_field"]:
            ent["delegated_field"] = e["delegated_field"]
        ent["site"] = {"file": PREFIX + e["module"], "anchor": e["anchor"], "provisions": e["provisions"]}
        ent["source"] = {"quote": take(e["quote"]), "citations": e["cites"]}
        ent["readings"] = e["readings"]
        ent["taken"] = {"reading": e["taken"][0], "mechanism": mech, "rationale": e["taken"][1]}
        ent["status"] = "resolved"
        ent["cross_refs"] = e["cross_refs"]
        if e["notes"]:
            ent["notes"] = e["notes"]
        entries.append(ent)
    return {
        "kind": "fork-register",
        "register_version": 1,
        "subject": "insurance-business-law-08-2022",
        "note": ("The pipeline-format rendering of section 3 (the fork register) of NOTES.md for row legalese-2026-10-vn-29: Law 08/2022/QH15 on Insurance Business "
                 "as made (V1), as amended by Law 139/2025/QH15 from 1 January 2026 (V2) and with Điều 2(6) and 2(8) of that Law from 1 July 2026 (V3). "
                 "The 38 forks F1 to F38, their readings and the reading taken are the encoder's, copied from NOTES.md and not re-decided; where this file found NOTES.md wrong or incomplete the entry's notes say so, prefixed DISCREPANCY. "
                 "No Vietnamese-qualified lawyer has read any reading, and no authority has settled any fork, so every entry is 'resolved' by the encoder alone. "
                 "No Interpretation record exists in this encoding, so no entry is an interpretation-field and the interpretation_type is omitted. "
                 "Completeness is unfalsifiable: the register lists the ambiguities the encoder met, and an ambiguity not met is not in it. "
                 "Where NOTES records that no reading was taken (F3, F5, F17, F19), the stance actually taken is represented as a live reading. "
                 "Each source.quote is extracted by tools/make_fork_register.py from the named lines of the raw gazette text, not typed; whitespace is collapsed, so a quote may run across a line break."),
        "entries": entries,
    }


# --- checking --------------------------------------------------------------------------------------------------------
def validate_schema(inst, schema, root, path="$", errs=None):
    """A validator for the subset of JSON Schema the fork-register schema uses (standard library only)."""
    errs = errs if errs is not None else []
    if "$ref" in schema:
        ref = root
        for part in schema["$ref"].lstrip("#/").split("/"):
            ref = ref[part]
        return validate_schema(inst, ref, root, path, errs)
    t = schema.get("type")
    py = {"object": dict, "array": list, "string": str, "integer": int}
    if t and not isinstance(inst, py[t]):
        errs.append(f"{path}: not a {t}")
        return errs
    if "const" in schema and inst != schema["const"]:
        errs.append(f"{path}: not {schema['const']!r}")
    if "enum" in schema and inst not in schema["enum"]:
        errs.append(f"{path}: {inst!r} not in {schema['enum']}")
    if isinstance(inst, str):
        if len(inst) < schema.get("minLength", 0):
            errs.append(f"{path}: shorter than minLength")
        if "pattern" in schema and not re.search(schema["pattern"], inst):
            errs.append(f"{path}: {inst!r} does not match {schema['pattern']}")
    if isinstance(inst, list):
        if len(inst) < schema.get("minItems", 0):
            errs.append(f"{path}: fewer than minItems")
        for i, x in enumerate(inst):
            if "items" in schema:
                validate_schema(x, schema["items"], root, f"{path}[{i}]", errs)
    if isinstance(inst, dict):
        for k in schema.get("required", []):
            if k not in inst:
                errs.append(f"{path}: missing {k}")
        props = schema.get("properties", {})
        for k, v in inst.items():
            if k in props:
                validate_schema(v, props[k], root, f"{path}.{k}", errs)
            elif schema.get("additionalProperties") is False:
                errs.append(f"{path}: unexpected property {k}")
    return errs


def check(reg, schema_path=None, external_path=None):
    errs = []
    ids = [e["id"] for e in reg["entries"]]
    if schema_path:
        schema = json.load(open(schema_path, encoding="utf-8"))
        errs += validate_schema(reg, schema, schema)
    peer = P2_IDS
    if external_path:
        peer = {x["id"] for x in json.load(open(external_path, encoding="utf-8"))["entries"]}
    if not reg["entries"] and not reg.get("note"):
        errs.append("empty-register-explains")
    if len(set(ids)) != len(ids):
        errs.append("entry-ids-unique: duplicate ids")
    ifields = []
    for e in reg["entries"]:
        i = e["id"]
        rids = [r["id"] for r in e["readings"]]
        if len(set(rids)) != len(rids):
            errs.append(f"{i}: reading-ids-unique-within-entry")
        by = {r["id"]: r for r in e["readings"]}
        t = e["taken"]
        if t["reading"] not in by or by[t["reading"]]["status"] != "live":
            errs.append(f"{i}: taken-names-a-live-reading")
        if not any(r["status"] == "live" for r in e["readings"]):
            errs.append(f"{i}: at-least-one-live-reading")
        m = e["materialisation"]
        has_if, has_df = "interpretation_field" in e, "delegated_field" in e
        if m == "interpretation-field" and (not has_if or has_df):
            errs.append(f"{i}: materialisation-implies-field")
        if m == "delegated-to-fact" and (not has_df or has_if):
            errs.append(f"{i}: materialisation-implies-field")
        if m == "resolved-at-encode" and (has_if or has_df):
            errs.append(f"{i}: materialisation-implies-field")
        want = {"interpretation-field": "TYPICALLY", "resolved-at-encode": "encoded", "delegated-to-fact": "fact-supplied"}[m]
        if t["mechanism"] != want:
            errs.append(f"{i}: materialisation-implies-mechanism")
        if has_if:
            ifields.append(e["interpretation_field"])
        for r in e["readings"]:
            s = r["status"]
            if s in ("rejected", "demoted") and not r.get("rejection_rationale"):
                errs.append(f"{i}.{r['id']}: non-live-readings-explain")
            if s == "live" and not r["citations"]:
                errs.append(f"{i}.{r['id']}: live-readings-cite-their-licence")
            if s == "arguable":
                if not r["citations"] or not r.get("foreclosure") or "rejection_rationale" in r:
                    errs.append(f"{i}.{r['id']}: arguable-readings-cite-and-foreclose")
            if s != "arguable" and "foreclosure" in r:
                errs.append(f"{i}.{r['id']}: arguable-readings-cite-and-foreclose (foreclosure on a non-arguable reading)")
            if s == "live" and ("rejection_rationale" in r):
                errs.append(f"{i}.{r['id']}: rejection_rationale on a live reading")
        if (e["status"] in ("settled", "demoted")) != ("settled_by" in e):
            errs.append(f"{i}: settled-or-demoted-requires-authority")
        if e["status"] == "demoted" and not any(r["status"] == "demoted" for r in e["readings"]):
            errs.append(f"{i}: demoted-requires-a-demoted-reading")
        src = e["source"]
        if ("quote" in src) == ("quote_absent_reason" in src):
            errs.append(f"{i}: quote-or-absent-reason")
        if m != "resolved-at-encode" and "divergence" not in e and m == "interpretation-field":
            errs.append(f"{i}: materialised-forks-declare-divergence")
        div = e.get("divergence")
        wit = e.get("witnesses")
        if div == "observable" and not wit:
            errs.append(f"{i}: observable-divergence-requires-witnesses")
        if wit and div != "observable":
            errs.append(f"{i}: witnesses-only-when-observable")
        if "cross_refs" not in e:
            errs.append(f"{i}: cross_refs missing")
        for c in e.get("cross_refs", []):
            if c not in peer:
                errs.append(f"{i}: cross-refs-resolve: {c}")
        # the quote is in the raw text (whitespace collapsed)
        if "quote" in src:
            if not any(src["quote"] in norm(raw(k)) for k in FILES):
                errs.append(f"{i}: quote is not a substring of any raw source")
        # the anchor is a definition in its module
        mod = os.path.join(ROW, os.path.basename(e["site"]["file"]))
        if not e["site"]["file"].startswith(PREFIX):
            errs.append(f"{i}: site.file prefix")
        if not os.path.exists(mod):
            errs.append(f"{i}: module {mod} does not exist")
        else:
            text = open(mod, encoding="utf-8").read().split("\n")
            if not any(l.startswith("`" + e["site"]["anchor"] + "`") or l.startswith("DECLARE `" + e["site"]["anchor"] + "`") for l in text):
                errs.append(f"{i}: anchor {e['site']['anchor']!r} is not a definition in {os.path.basename(mod)}")
        if "line" in e["site"]:
            errs.append(f"{i}: site.line should be omitted")
    if len(set(ifields)) != len(ifields):
        errs.append("interpretation-fields-unique")
    return errs


def main():
    args = sys.argv[1:]
    schema = args[args.index("--schema") + 1] if "--schema" in args else None
    external = args[args.index("--external") + 1] if "--external" in args else None
    if "--check" in args:
        reg = json.load(open(OUT, encoding="utf-8"))
    else:
        reg = build()
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(reg, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"wrote {OUT}")
    errs = check(reg, schema, external)
    for x in errs:
        print("ERROR", x)
    n = len(reg["entries"])
    print(f"{n} entries, {len(errs)} problems")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
