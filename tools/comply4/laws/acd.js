// Rule pack: ASEAN Cosmetic Directive.
//
// Text basis (read 2 October 2026):
//   - Agreement on the ASEAN Harmonized Cosmetic Regulatory Scheme, Phnom Penh, 2 September 2003,
//     Schedule B (ASEAN Cosmetic Directive), Articles 1-12, in the unofficial text published by the
//     Centre for International Law, NUS.
//   - Appendix II, ASEAN Cosmetic Labeling Requirements, version dated 4 September 2007, in the copy
//     published by the Health Sciences Authority, Singapore.
// Every requirement below is paraphrased, with its provision cited; the text itself is not bundled.
//
// Each fact and duty carries an `l4` name: the field or rule that states the same thing in
// laws/acd.l4. build.js reads those names to generate laws/acd-cases.l4, so the two cannot drift
// without `l4 run` saying so.

(function (root, factory) {
  var pack = factory();
  if (typeof module === 'object' && module.exports) module.exports = pack;
  else (root.Comply4Packs = root.Comply4Packs || {})[pack.id] = pack;
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var STATES = [
    ['BN', 'Brunei Darussalam'], ['KH', 'Cambodia'], ['ID', 'Indonesia'], ['LA', 'Lao PDR'],
    ['MY', 'Malaysia'], ['MM', 'Myanmar'], ['PH', 'Philippines'], ['SG', 'Singapore'],
    ['TH', 'Thailand'], ['VN', 'Viet Nam']
  ].map(function (s) { return { v: s[0], label: s[1] }; });

  // Where a label particular appears. Appendix II C.1 wants it on the outer packaging, or on the
  // immediate packaging where there is no outer one; C.2 lets it move to a leaflet, hang tag,
  // display panel or shrink wrap only where the container cannot carry it.
  var WHERE = [
    { v: 'pack', label: 'On the outer packaging (or the immediate packaging if there is none)', l4: 'on the packaging' },
    { v: 'insert', label: 'Only on a leaflet, hang tag, display panel or shrink wrap', l4: 'only on a leaflet or tag' },
    { v: 'none', label: 'Not shown', l4: 'not shown' }
  ];
  function shown(id) { return { any: [{ is: [id, 'pack'] }, { all: [{ is: [id, 'insert'] }, 'smallPack'] }] }; }

  var YOU = 'isResponsible';

  return {
    id: 'acd',
    title: 'ASEAN Cosmetic Directive',
    short: 'ACD',
    citation: 'Agreement on the ASEAN Harmonized Cosmetic Regulatory Scheme (Phnom Penh, 2 September 2003), Schedule B, with Appendix II (ASEAN Cosmetic Labeling Requirements, 4 September 2007)',
    subjectNoun: 'product',

    sources: [
      {
        label: 'Agreement and Schedule B (unofficial text, Centre for International Law, NUS)',
        url: 'https://cil.nus.edu.sg/wp-content/uploads/2019/02/2003-Agreement-on-the-ASEAN-Harmonized-Cosmetic-Regulatory-Scheme-1.pdf'
      },
      {
        label: 'Appendix II, ASEAN Cosmetic Labeling Requirements (Health Sciences Authority, Singapore)',
        url: 'https://file.go.gov.sg/appendix-ii-asean-cosmetic-labelling-requirements.pdf'
      }
    ],

    limits: [
      'The Directive binds the ten Member States. It reaches a company through each State\'s implementing law, which also sets the penalties; the Directive itself sets none. This pack checks the Directive only.',
      'The Annexes (the lists of prohibited, restricted and permitted substances) are not bundled. Comply4 asks you whether your formula is within them; it does not look ingredients up.',
      'The pack follows the 2003 text of the Directive and the 2007 Appendix II. Later decisions of the ASEAN Cosmetic Committee have not been checked.',
      'Appendix III (claims), Appendix IV (notification particulars) and Appendix VI (good manufacturing practice) are each reduced to one yes-or-no question.',
      'Article 12(2) let Member States tolerate non-conforming products for 36 months from the Directive taking effect. That period is treated as spent.'
    ],

    // How content is read into answers (intake.js). Claude reads; the rules below decide.
    intake: {
      subject: 'cosmetic products: what they are, what is in them, how they are labelled and claimed, and the file kept on them',
      kinds: [
        { v: 'label', label: 'Label or packaging' },
        { v: 'formula', label: 'Formula, recipe or ingredient list' },
        { v: 'listing', label: 'Product or service offered for sale' },
        { v: 'description', label: 'Product description or marketing' },
        { v: 'process', label: 'Manufacturing process or method' },
        { v: 'file', label: 'Technical, safety or test document' },
        { v: 'other', label: 'Something else' }
      ],
      guidance: [
        'Always answer "site" and "mainPurpose" if the content shows what the thing is, including when it is plainly not a cosmetic (a food, a medicine, a device, a service): that is how the tool learns the law does not apply.',
        'A label particular is "pack" only when you can see it on the packaging itself. Answer "none" for a particular only when the content shows the whole label, every face of it, and the particular is not there; a single photo of one face does not show that. A web listing or a description is not the label: do not answer the label-placement questions from one unless it shows the label.',
        'A formula, recipe or ingredient list shows whether the product contains colouring agents, preservatives, UV filters, a perfume composition or botanicals. Answer those from the ingredients named.',
        'The Annexes are not supplied to you. Answer a question about an Annex only where you are confident from your own knowledge that a named ingredient is on that Annex, name the ingredient in the evidence, say that it rests on your knowledge of the Annex and not on a copy of it, and give confidence no higher than "medium". Never answer that a product contains NO Annex substance, and never answer that limits or conditions are met.',
        'A page offering the product for sale shows that it has been placed on the market. Answer "markets" only for Member States the content plainly shows it is sold in.',
        'Claims are benefits the content says the product delivers. Whether they are permitted or substantiated is not something content like a label can show; leave those questions out unless the content is the evidence itself.',
        'Do not answer who the user is, what authorities have been told, or what the user keeps on file, unless the content is that very record.'
      ]
    },

    // Things noticed in the text while writing the rules. Both copies read are unofficial or
    // secondary, so each of these may be a transcription slip rather than the signed text.
    observations: [
      { ref: 'Art 8(1)', text: 'The product information is to be kept at the address specified on the label "in accordance with Article 5". Article 5 is the ingredients handbook; labelling is Article 6. The rule here reads it as Article 6.' },
      { ref: 'Art 8(1)', text: 'The list of information runs (a) to (e) and then (g). There is no (f).' },
      { ref: 'Art 6(2)', text: 'The paragraph has no operative verb: it names the special precautions "which must appear on the label" and stops. The rule here reads it with Appendix II C.1(i) as a requirement that they appear.' },
      { ref: 'Art 1(2)', text: 'The free-movement rule is made subject to "Article 10", which is institutional arrangements. The safeguard that lets a Member State block a compliant product is Article 11.' },
      { ref: 'Art 4(2)(b), (f), (h)', text: 'Marketing is prohibited where a listed substance is used "beyond the limits and outside the conditions". Read literally, exceeding a limit while keeping to the conditions would not be caught. The rule here treats either as enough.' },
      { ref: 'App II C.1(a)', text: 'The name and function must appear "unless it is clear from the presentation of the product". "It" could be the function alone or both. The rule here always requires the name and excuses only the function.' },
      { ref: 'App II C.1(i)', text: 'The Annexes whose warnings must be printed are left blank ("Annexes __"). Article 6(2) names Annexes III, IV, VI, VII and VIII.' },
      { ref: 'App II C.1(f)', text: 'Contents may be given "in either metric or both metric and imperial system". The rule here treats imperial units alone as not enough.' }
    ],

    defs: {
      isCosmetic: { all: [{ 'in': ['site', ['external', 'oral']] }, 'mainPurpose'] },
      inScope: { all: [{ def: 'isCosmetic' }, { not: 'hasAnnexV' }] },
      colourRulesApply: { all: ['hasColour', { not: 'colourHairOnly' }] },
      // At least one colouring agent, preservative or UV filter is off Part 1 of its Annex.
      unlistedPresent: { any: [
        { all: [{ def: 'colourRulesApply' }, { not: 'colourListed' }] },
        { all: ['hasPreservative', { not: 'presListed' }] },
        { all: ['hasUV', { not: 'uvListed' }] }
      ] },
      unlistedCovered: { 'in': ['unlistedCover', ['part2', 'art5']] },
      reliesOnArt5: { all: [{ def: 'unlistedPresent' }, { is: ['unlistedCover', 'art5'] }] }
    },
    scope: { def: 'inScope' },

    groups: [
      { id: 'who', title: 'You and your markets', ref: 'Arts 1, 11' },
      { id: 'product', title: 'What the product is', ref: 'Art 2' },
      { id: 'formula', title: 'Formula', ref: 'Arts 3–5' },
      { id: 'label', title: 'Label', ref: 'Art 6, Appendix II' },
      { id: 'claims', title: 'Claims', ref: 'Art 7' },
      { id: 'file', title: 'Product information file', ref: 'Arts 1(4), 8, 9' }
    ],

    facts: [
      // ---- You and your markets
      {
        id: 'isResponsible', group: 'who', type: 'bool', l4: 'you are the company or person responsible for placing the product in the market',
        q: 'Are you the company or person responsible for placing this product on the market?',
        help: 'Articles 1(3), 1(4), 8 and 9 put duties on that company or person directly. If someone else holds the role, those duties are theirs.'
      },
      {
        id: 'markets', group: 'who', type: 'multi', options: STATES,
        q: 'In which Member States will the product be marketed?'
      },
      {
        id: 'notifiedIn', group: 'who', type: 'multi', options: STATES, noneLabel: 'None yet', limitTo: 'markets',
        q: 'Which of their regulatory authorities have been told the place of manufacture or of initial importation?',
        help: 'Article 1(3) requires this for each Member State where the product will be marketed.'
      },
      {
        id: 'onMarket', group: 'who', type: 'bool', l4: 'the product has been placed in the market',
        q: 'Has the product already been placed on the market in any of them?'
      },
      {
        id: 'marketDate', group: 'who', type: 'date', optional: true, askWhen: { not: 'onMarket' },
        q: 'When do you plan to place it on the market?',
        help: 'Optional. Used only to show how long is left for anything that must be done first.'
      },
      {
        id: 'art11Measure', group: 'who', type: 'bool', l4: 'a Member State has prohibited or conditioned the product under Article 11',
        q: 'Has any of those Member States provisionally prohibited this product, or put special conditions on it?',
        help: 'Article 11 lets a Member State do this to a product that complies with the Directive, for a health hazard or for religious or cultural sensitivity.'
      },

      // ---- What the product is
      {
        id: 'site', group: 'product', type: 'enum', l4: 'where the product is applied',
        q: 'Where is the product intended to be applied?',
        options: [
          { v: 'external', label: 'External parts of the body: skin, hair, nails, lips, external genital organs', l4: 'external parts of the body' },
          { v: 'oral', label: 'Teeth or the lining of the mouth', l4: 'teeth or the mucous membranes of the oral cavity' },
          { v: 'other', label: 'Anywhere else, or it is swallowed, injected or inhaled', l4: 'somewhere else' }
        ]
      },
      {
        id: 'mainPurpose', group: 'product', type: 'bool', l4: 'its exclusive or main purpose is a cosmetic one',
        q: 'Is its exclusive or main purpose to clean, perfume, change the appearance of, correct the odour of, protect, or keep in good condition those parts?',
        help: 'Article 2(1). A product whose main purpose is to treat or prevent disease is not a cosmetic product.'
      },
      {
        id: 'hasAnnexV', group: 'product', type: 'bool', l4: 'it contains a substance listed in Annex V',
        q: 'Does it contain any substance listed in Annex V?',
        help: 'Article 2(3) takes such products outside the Directive altogether; each Member State deals with them as it sees fit.'
      },

      // ---- Formula
      {
        id: 'safeConclusion', group: 'formula', type: 'bool', l4: 'the safety assessment concludes it does not damage human health',
        q: 'Does your safety assessment conclude that the product does not damage human health in normal or reasonably foreseeable use?',
        help: 'Article 3(1). The assessment takes account of presentation, labelling, instructions for use and disposal, and warnings. Comply4 records your answer; it cannot make the assessment.'
      },
      {
        id: 'hasAnnexII', group: 'formula', type: 'bool', l4: 'it contains a substance listed in Annex II',
        q: 'Does the product contain any substance listed in Annex II (prohibited substances)?'
      },
      {
        id: 'annexIITrace', group: 'formula', type: 'bool', askWhen: 'hasAnnexII', l4: 'every Annex II substance is a trace unavoidable in good manufacturing practice',
        q: 'Is every such substance present only as a trace that is technically unavoidable in good manufacturing practice?'
      },
      {
        id: 'hasAnnexIII', group: 'formula', type: 'bool', l4: 'it contains a substance listed in Annex III Part 1',
        q: 'Does it contain any substance listed in Annex III, Part 1 (restricted substances)?'
      },
      {
        id: 'annexIIIWithin', group: 'formula', type: 'bool', askWhen: 'hasAnnexIII', l4: 'every Annex III substance is within its limits and conditions',
        q: 'Is each of them within the limits and the conditions that Annex III lays down?'
      },
      {
        id: 'hasColour', group: 'formula', type: 'bool', l4: 'it contains colouring agents',
        q: 'Does it contain colouring agents?'
      },
      {
        id: 'colourHairOnly', group: 'formula', type: 'bool', askWhen: 'hasColour', l4: 'its colouring agents are intended solely to colour hair',
        q: 'Are the colouring agents intended solely to colour hair?',
        help: 'Article 4(2)(c) and (d) leave such products out of the colouring-agent rules.'
      },
      {
        id: 'colourListed', group: 'formula', type: 'bool', askWhen: { def: 'colourRulesApply' }, l4: 'every colouring agent is listed in Annex IV Part 1',
        q: 'Is every colouring agent listed in Annex IV, Part 1?'
      },
      {
        id: 'colourWithin', group: 'formula', type: 'bool', askWhen: { def: 'colourRulesApply' }, l4: 'every listed colouring agent is used within its conditions',
        q: 'Are the listed colouring agents used within the conditions Annex IV lays down?'
      },
      {
        id: 'hasPreservative', group: 'formula', type: 'bool', l4: 'it contains preservatives',
        q: 'Does it contain preservatives?'
      },
      {
        id: 'presListed', group: 'formula', type: 'bool', askWhen: 'hasPreservative', l4: 'every preservative is listed in Annex VI Part 1',
        q: 'Is every preservative listed in Annex VI, Part 1?'
      },
      {
        id: 'presWithin', group: 'formula', type: 'bool', askWhen: 'hasPreservative', l4: 'every listed preservative is within its limits and conditions',
        q: 'Are the listed preservatives within the limits and conditions Annex VI lays down?'
      },
      {
        id: 'presSpecific', group: 'formula', type: 'bool', askWhen: { all: ['hasPreservative', { not: 'presWithin' }] }, l4: 'the other concentration serves a specific purpose apparent from the presentation',
        q: 'Is the different concentration used for a specific purpose that is apparent from the presentation of the product?',
        help: 'Article 4(2)(f) allows other concentrations in that case.'
      },
      {
        id: 'hasUV', group: 'formula', type: 'bool', l4: 'it contains UV filters',
        q: 'Does it contain UV filters?'
      },
      {
        id: 'uvListed', group: 'formula', type: 'bool', askWhen: 'hasUV', l4: 'every UV filter is listed in Annex VII Part 1',
        q: 'Is every UV filter listed in Annex VII, Part 1?'
      },
      {
        id: 'uvWithin', group: 'formula', type: 'bool', askWhen: 'hasUV', l4: 'every listed UV filter is within its limits and conditions',
        q: 'Are the listed UV filters within the limits and conditions Annex VII lays down?'
      },
      {
        id: 'unlistedCover', group: 'formula', type: 'enum', l4: 'what covers the unlisted substances',
        askWhen: { def: 'unlistedPresent' },
        q: 'What covers the colouring agents, preservatives or UV filters that are not on Part 1 of their Annex?',
        options: [
          { v: 'part2', label: 'Each is on Part 2 of its Annex, within its limits and before its end date', l4: 'Part 2 of the Annex' },
          { v: 'art5', label: 'Each is on Part 2, or has a current national authorisation in every market', l4: 'a national authorisation under Article 5' },
          { v: 'none', label: 'At least one is not covered', l4: 'nothing' }
        ],
        help: 'Article 4(4) allows Part 2 substances provisionally. Article 5 lets a Member State authorise an unlisted substance within its own territory for up to three years.'
      },
      {
        id: 'art5Indication', group: 'formula', type: 'bool', askWhen: { def: 'reliesOnArt5' }, l4: 'it bears the distinctive indication the authorisation defines',
        q: 'Does the product bear the distinctive indication that the national authorisation defines?'
      },

      // ---- Label
      {
        id: 'smallPack', group: 'label', type: 'bool', l4: 'the container cannot carry all the particulars',
        q: 'Is the container too small, or of a shape or nature, that it cannot display all the label particulars?',
        help: 'If so, Appendix II C.2 lets particulars move to a leaflet, hang tag, display panel or shrink wrap, except the name and the batch number.'
      },
      { id: 'lblName', group: 'label', type: 'enum', options: WHERE, l4: 'where the name is shown', q: 'Where is the name of the product shown?' },
      {
        id: 'functionClear', group: 'label', type: 'bool', l4: 'its function is clear from its presentation',
        q: 'Is the product\'s function clear from its presentation?'
      },
      {
        id: 'lblFunction', group: 'label', type: 'enum', options: WHERE, askWhen: { not: 'functionClear' }, l4: 'where the function is shown',
        q: 'Where is its function shown?'
      },
      {
        id: 'useClear', group: 'label', type: 'bool', l4: 'how to use it is clear from its name or presentation',
        q: 'Is how to use it clear from the product name or presentation?'
      },
      {
        id: 'lblInstructions', group: 'label', type: 'enum', options: WHERE, askWhen: { not: 'useClear' }, l4: 'where the instructions are shown',
        q: 'Where are the instructions for use shown?'
      },
      { id: 'lblIngredients', group: 'label', type: 'enum', options: WHERE, l4: 'where the ingredient list is shown', q: 'Where is the full ingredient list shown?' },
      {
        id: 'ingOrder', group: 'label', type: 'bool', l4: 'the ingredients are in the order Appendix II requires',
        q: 'Are the ingredients listed in descending order of weight at the time they were added?',
        help: 'Ingredients under 1% may follow in any order, and colouring agents may come last in any order. Perfume and aromatic compositions may be named "perfume", "fragrance", "aroma" or "flavor".'
      },
      {
        id: 'ingNames', group: 'label', type: 'bool', l4: 'the ingredients are named from the standard references',
        q: 'Are the ingredients named using the latest edition of a standard reference?',
        help: 'International Cosmetic Ingredient Dictionary, British Pharmacopeia, United States Pharmacopeia or Chemical Abstract Services.'
      },
      { id: 'hasBotanicals', group: 'label', type: 'bool', l4: 'it contains botanicals', q: 'Does it contain botanicals or botanical extracts?' },
      {
        id: 'botanicalNames', group: 'label', type: 'bool', askWhen: 'hasBotanicals', l4: 'the botanicals are identified by genus and species',
        q: 'Are they identified by genus and species?'
      },
      { id: 'lblCountry', group: 'label', type: 'enum', options: WHERE, l4: 'where the country of manufacture is shown', q: 'Where is the country of manufacture shown?' },
      {
        id: 'lblResponsible', group: 'label', type: 'enum', options: WHERE, l4: 'where the responsible company is shown',
        q: 'Where are the name and address of the company or person responsible for placing the product on the local market shown?'
      },
      { id: 'lblContents', group: 'label', type: 'enum', options: WHERE, l4: 'where the contents are shown', q: 'Where are the contents (weight or volume) shown?' },
      {
        id: 'contentsUnits', group: 'label', type: 'enum', askWhen: { 'in': ['lblContents', ['pack', 'insert']] }, l4: 'the units the contents are given in',
        q: 'In which units?',
        options: [
          { v: 'metric', label: 'Metric', l4: 'metric' },
          { v: 'both', label: 'Metric and imperial', l4: 'metric and imperial' },
          { v: 'imperial', label: 'Imperial only', l4: 'imperial only' }
        ]
      },
      { id: 'lblBatch', group: 'label', type: 'enum', options: WHERE, l4: 'where the batch number is shown', q: 'Where is the manufacturer\'s batch number shown?' },
      {
        id: 'durability', group: 'label', type: 'number', unit: 'months', l4: 'its minimum durability in months',
        q: 'What is the product\'s minimum durability, in months?',
        help: 'How long it keeps fulfilling its function and stays safe when stored properly. Under 30 months, an expiry date is mandatory.'
      },
      { id: 'lblExpiry', group: 'label', type: 'enum', options: WHERE, l4: 'where the expiry date is shown', q: 'Where is the expiry date shown?' },
      {
        id: 'lblMfg', group: 'label', type: 'enum', options: WHERE, askWhen: { not: shown('lblExpiry') }, l4: 'where the manufacturing date is shown',
        q: 'Where is the manufacturing date shown?'
      },
      {
        id: 'dateFormat', group: 'label', type: 'bool', l4: 'the date is given as month and year or day month and year',
        q: 'Is the date given as month and year, or as day, month and year in that order?'
      },
      {
        id: 'expiryWords', group: 'label', type: 'bool', askWhen: shown('lblExpiry'), l4: 'the expiry date is preceded by the words Appendix II suggests',
        q: 'Is the expiry date preceded by the words "expiry date" or "best before"?'
      },
      {
        id: 'needsPrecautions', group: 'label', type: 'bool', l4: 'special precautions must be observed in use',
        q: 'Must any special precautions be observed in using the product?',
        help: 'Including any warning that the Annexes say must be printed on the label for a substance you use.'
      },
      {
        id: 'lblPrecautions', group: 'label', type: 'enum', options: WHERE, askWhen: 'needsPrecautions', l4: 'where the precautions are shown',
        q: 'Where are those precautions shown?'
      },
      {
        id: 'nameOnImmediate', group: 'label', type: 'bool', askWhen: 'smallPack', l4: 'the name is on the immediate packaging',
        q: 'Is the product name on the immediate packaging itself?'
      },
      {
        id: 'batchOnImmediate', group: 'label', type: 'bool', askWhen: 'smallPack', l4: 'the batch number is on the immediate packaging',
        q: 'Is the batch number on the immediate packaging itself?'
      },
      {
        id: 'lblLegible', group: 'label', type: 'bool', l4: 'the particulars are easily legible visible and clearly comprehensible',
        q: 'Are the label particulars easily legible, visible and clearly comprehensible?'
      },
      { id: 'lblIndelible', group: 'label', type: 'bool', l4: 'the particulars are indelible', q: 'Are they indelible?' },
      {
        id: 'lblLanguage', group: 'label', type: 'bool', l4: 'the particulars are in an accepted language',
        q: 'Are they in English, the national language, or a language consumers in each market understand?',
        help: 'A Member State may go further and require the name and function, instructions, responsible company, contents and precautions in its national language.'
      },
      {
        id: 'noMisleading', group: 'label', type: 'bool', l4: 'nothing in the labelling or advertising implies characteristics it lacks',
        q: 'Are the labelling, presentation and advertising free of any text, name, trade mark, picture or sign implying characteristics the product does not have?'
      },

      // ---- Claims
      {
        id: 'makesClaims', group: 'claims', type: 'bool', l4: 'a benefit is claimed for it',
        q: 'Do the label, packaging or advertising claim a benefit for the product?'
      },
      {
        id: 'claimsGuideline', group: 'claims', type: 'bool', askWhen: 'makesClaims', l4: 'the claims comply with the Claims Guideline',
        q: 'Do the claims comply with the ASEAN Cosmetic Claims Guideline (Appendix III)?',
        help: 'Claims are also under national control: a Member State may permit or prohibit particular claims.'
      },
      {
        id: 'claimsEvidence', group: 'claims', type: 'bool', askWhen: 'makesClaims', l4: 'each claimed benefit is justified by evidence or the formulation',
        q: 'Is each claimed benefit justified by substantial evidence, or by the formulation itself?'
      },

      // ---- Product information file
      {
        id: 'pifAccessible', group: 'file', type: 'bool', l4: 'the file is readily accessible at the address on the label',
        q: 'Is the product information kept readily accessible to the regulatory authority at the address shown on the label?'
      },
      {
        id: 'pifComposition', group: 'file', type: 'bool', l4: 'the file holds the qualitative and quantitative composition',
        q: 'Does the file hold the qualitative and quantitative composition of the product?'
      },
      { id: 'hasPerfume', group: 'file', type: 'bool', l4: 'it contains a perfume composition', q: 'Does the product contain a perfume composition?' },
      {
        id: 'pifPerfume', group: 'file', type: 'bool', askWhen: 'hasPerfume', l4: 'the file identifies the perfume composition and its supplier',
        q: 'Does the file give the name and code number of the composition and the identity of its supplier?'
      },
      {
        id: 'pifSpecs', group: 'file', type: 'bool', l4: 'the file holds the specifications',
        q: 'Does the file hold the specifications of the raw materials and of the finished product?'
      },
      {
        id: 'pifMethod', group: 'file', type: 'bool', l4: 'the file holds a method of manufacture complying with good manufacturing practice',
        q: 'Does the file hold the method of manufacture, complying with the ASEAN Guidelines for Cosmetic Good Manufacturing Practice (Appendix VI)?'
      },
      {
        id: 'qualifiedPerson', group: 'file', type: 'bool', l4: 'the person responsible for manufacture or importation is adequately qualified',
        q: 'Does the person responsible for manufacture or importation have adequate knowledge or experience under the law and practice of the Member State concerned?'
      },
      {
        id: 'pifSafety', group: 'file', type: 'bool', l4: 'the file holds the safety assessment',
        q: 'Does the file hold the assessment of the safety for human health of the finished product?',
        help: 'Covering the product, its ingredients, its chemical structure and its level of exposure.'
      },
      {
        id: 'pifUndesirable', group: 'file', type: 'bool', l4: 'the file holds the existing data on undesirable effects',
        q: 'Does the file hold the existing data on undesirable effects on human health from use of the product?'
      },
      {
        id: 'pifClaimsData', group: 'file', type: 'bool', askWhen: 'makesClaims', l4: 'the file holds supporting data for the claimed benefits',
        q: 'Does the file hold supporting data for the claimed benefits?'
      },
      {
        id: 'pifLanguage', group: 'file', type: 'bool', l4: 'the file is in a language the authority accepts',
        q: 'Is the file in the national language of each Member State concerned, or a language its regulatory authority readily understands?'
      },
      {
        id: 'art9Methods', group: 'file', type: 'bool', l4: 'the methods of checking ingredients are available to the authority',
        q: 'Are the methods the manufacturer uses to check the ingredients against the Certificate of Analysis available to the regulatory authority?'
      },
      {
        id: 'art9Criteria', group: 'file', type: 'bool', l4: 'the microbiological and purity criteria are available to the authority',
        q: 'Are the criteria for microbiological control and for the chemical purity of ingredients, or the methods for checking them, available to the regulatory authority?'
      }
    ],

    // The L4 rule that is ANDed into every duty, as `scope` is here.
    l4Scope: 'the Directive applies to the product',

    // Facts the L4 states differently from the console: one yes/no in place of two lists.
    l4Derived: [
      {
        field: 'every regulatory authority concerned has been notified',
        from: function (f) {
          var m = f.markets || [], n = f.notifiedIn || [];
          return m.length > 0 && m.every(function (x) { return n.indexOf(x) >= 0; });
        }
      }
    ],

    parts: [
      { id: 'market', title: 'Getting to market', ref: 'Arts 1, 11' },
      { id: 'safety', title: 'Safety', ref: 'Art 3' },
      { id: 'formula', title: 'Ingredients', ref: 'Arts 4–5' },
      { id: 'label', title: 'Labelling', ref: 'Art 6, Appendix II' },
      { id: 'claims', title: 'Claims', ref: 'Art 7' },
      { id: 'file', title: 'Product information', ref: 'Arts 1(4), 8, 9' }
    ],

    // binds: 'you'      a duty the Directive puts on the responsible company or person by name
    //        'product'  a condition the product must meet; Member States must keep products that
    //                   fail it off the market (Art 1(1)), so it reaches you through national law
    duties: [
      // ---- Getting to market
      {
        id: 'notify', part: 'market', ref: 'Art 1(3)', binds: 'you',
        title: 'Notify each regulatory authority before marketing',
        text: 'Before the product is placed on the market, the responsible company or person must tell the cosmetics regulatory authority of every Member State where it will be marketed the place of manufacture or of initial importation.',
        appliesWhen: YOU, metWhen: { covers: ['markets', 'notifiedIn'] },
        pendingWhen: { not: 'onMarket' }, deadlineFact: 'marketDate',
        fix: 'Notify the authorities still outstanding. Each Member State sets its own form; Appendix IV lists the particulars.',
        l4: { applies: 'Article 1(3) binds you', met: 'every regulatory authority concerned has been notified', pending: 'the time to notify has not passed' }
      },
      {
        id: 'art11', part: 'market', ref: 'Art 11(1)', binds: 'product',
        title: 'No national prohibition or special conditions',
        text: 'A Member State may provisionally prohibit a product that complies with the Directive, or subject it to special conditions, where it finds on substantiated grounds a hazard to health, or for reasons of religious or cultural sensitivity.',
        metWhen: { not: 'art11Measure' },
        fix: 'Meeting the Directive does not clear that market. Deal with the Member State\'s measure under its own law; Article 11(3) requires it to state the remedies available and their time limits.',
        l4: { met: 'no Article 11 measure stands against the product' }
      },

      // ---- Safety
      {
        id: 'safe', part: 'safety', ref: 'Art 3(1)', binds: 'product',
        title: 'The product must not damage human health',
        text: 'A cosmetic product on the market must not cause damage to human health when applied under normal or reasonably foreseeable conditions of use, taking account of its presentation, labelling, instructions for use and disposal, and warnings. Under Article 3(2) a warning does not excuse a failure to meet any other requirement.',
        metWhen: 'safeConclusion',
        fix: 'Do not market the product until a safety assessment supports it.',
        l4: { met: 'the product meets the safety requirement of Article 3' }
      },

      // ---- Ingredients
      {
        id: 'annexII', part: 'formula', ref: 'Art 4(2)(a), 4(3)', binds: 'product',
        title: 'No prohibited substances',
        text: 'A product containing a substance listed in Annex II may not be marketed. Traces are allowed where they are technically unavoidable in good manufacturing practice and the product still meets Article 3.',
        metWhen: { any: [{ not: 'hasAnnexII' }, { all: ['annexIITrace', 'safeConclusion'] }] },
        fix: 'Reformulate to remove the Annex II substance, or show that it is an unavoidable trace and that the product is still safe.',
        l4: { met: 'the product is clear of Annex II' }
      },
      {
        id: 'annexIII', part: 'formula', ref: 'Art 4(2)(b)', binds: 'product',
        title: 'Restricted substances within their limits',
        text: 'A product containing a substance listed in Annex III, Part 1 may not be marketed if the substance is used beyond the limits or outside the conditions laid down there.',
        reading: 'The text says "beyond the limits and outside the conditions". This rule treats either as enough.',
        metWhen: { any: [{ not: 'hasAnnexIII' }, 'annexIIIWithin'] },
        fix: 'Bring each Annex III substance within its limit and conditions of use.',
        l4: { met: 'the restricted substances are within Annex III' }
      },
      {
        id: 'colour', part: 'formula', ref: 'Art 4(2)(c)–(d), 4(4)(b), 5', binds: 'product',
        title: 'Colouring agents are permitted ones',
        text: 'Colouring agents must be listed in Annex IV, Part 1 and used within its conditions. An agent on Part 2 is allowed within its limits until its end date, and a Member State may authorise an unlisted one within its territory under Article 5. Products whose colouring agents are intended solely to colour hair are excepted.',
        appliesWhen: { def: 'colourRulesApply' },
        metWhen: { all: ['colourWithin', { any: ['colourListed', { def: 'unlistedCovered' }] }] },
        fix: 'Replace any colouring agent that is not on Annex IV, and keep listed ones within their conditions.',
        l4: { applies: 'the colouring agent rules apply', met: 'the colouring agents are permitted' }
      },
      {
        id: 'preservative', part: 'formula', ref: 'Art 4(2)(e)–(f), 4(4)(c), 5', binds: 'product',
        title: 'Preservatives are permitted ones',
        text: 'Preservatives must be listed in Annex VI, Part 1 and used within its limits and conditions, unless another concentration serves a specific purpose apparent from the presentation of the product. Part 2 preservatives are allowed until their end dates, and a Member State may authorise an unlisted one under Article 5.',
        reading: 'The text says "beyond the limits and outside the conditions". This rule treats either as enough.',
        appliesWhen: 'hasPreservative',
        metWhen: { all: [{ any: ['presWithin', 'presSpecific'] }, { any: ['presListed', { def: 'unlistedCovered' }] }] },
        fix: 'Replace any preservative that is not on Annex VI, and bring listed ones within their limits.',
        l4: { applies: 'the preservative rules apply', met: 'the preservatives are permitted' }
      },
      {
        id: 'uv', part: 'formula', ref: 'Art 4(2)(g)–(h), 4(4)(d), 5', binds: 'product',
        title: 'UV filters are permitted ones',
        text: 'UV filters must be listed in Annex VII, Part 1 and used within its limits and conditions. Part 2 filters are allowed until their end dates, and a Member State may authorise an unlisted one under Article 5.',
        reading: 'The text says "beyond the limits and outside the conditions". This rule treats either as enough.',
        appliesWhen: 'hasUV',
        metWhen: { all: ['uvWithin', { any: ['uvListed', { def: 'unlistedCovered' }] }] },
        fix: 'Replace any UV filter that is not on Annex VII, and bring listed ones within their limits.',
        l4: { applies: 'the UV filter rules apply', met: 'the UV filters are permitted' }
      },
      {
        id: 'art5mark', part: 'formula', ref: 'Art 5(1)(c)', binds: 'product',
        title: 'Distinctive indication for a nationally authorised substance',
        text: 'A product made with a substance that a Member State has authorised under Article 5 must bear the distinctive indication defined in that authorisation.',
        appliesWhen: { def: 'reliesOnArt5' }, metWhen: 'art5Indication',
        fix: 'Add the indication the authorisation specifies.',
        l4: { applies: 'the product relies on an Article 5 authorisation', met: 'it bears the distinctive indication the authorisation defines' }
      },

      // ---- Labelling
      {
        id: 'lName', part: 'label', ref: 'Art 6(1); App II C.1(a)', binds: 'product',
        title: 'Name of the product',
        text: 'The name of the cosmetic product must appear on the outer packaging, or on the immediate packaging where there is no outer packaging.',
        reading: 'C.1(a) excuses "it" where clear from the presentation. This rule takes "it" to be the function, so the name is always required.',
        metWhen: shown('lblName'), fix: 'Put the product name on the packaging.',
        l4: { met: 'the label shows the name' }
      },
      {
        id: 'lFunction', part: 'label', ref: 'App II C.1(a)', binds: 'product',
        title: 'Function of the product',
        text: 'The function of the product must appear, unless it is clear from the presentation of the product.',
        metWhen: { any: ['functionClear', shown('lblFunction')] }, fix: 'State what the product is for.',
        l4: { met: 'the label shows the function or it is clear' }
      },
      {
        id: 'lUse', part: 'label', ref: 'App II C.1(b)', binds: 'product',
        title: 'Instructions for use',
        text: 'Instructions on the use of the product must appear, unless that is clear from the product name or presentation.',
        metWhen: { any: ['useClear', shown('lblInstructions')] }, fix: 'Add instructions for use.',
        l4: { met: 'the label shows the instructions or they are clear' }
      },
      {
        id: 'lIngredients', part: 'label', ref: 'App II C.1(c)', binds: 'product',
        title: 'Full ingredient listing',
        text: 'The label must list every ingredient, in descending order of weight at the time added, named from the latest edition of a standard reference. Ingredients under 1% and colouring agents may follow in any order.',
        metWhen: { all: [shown('lblIngredients'), 'ingOrder', 'ingNames'] },
        fix: 'Show the full list, in the required order, using standard ingredient names.',
        l4: { met: 'the label carries a full ingredient listing' }
      },
      {
        id: 'lBotanicals', part: 'label', ref: 'App II C.1(c)', binds: 'product', advisory: true,
        title: 'Botanicals by genus and species',
        text: 'Botanicals and botanical extracts should be identified by genus and species. The genus may be abbreviated.',
        appliesWhen: 'hasBotanicals', metWhen: 'botanicalNames', fix: 'Name each botanical by genus and species.',
        l4: { applies: 'it contains botanicals', met: 'the botanicals are identified by genus and species' }
      },
      {
        id: 'lCountry', part: 'label', ref: 'App II C.1(d)', binds: 'product',
        title: 'Country of manufacture',
        text: 'The country of manufacture must appear.',
        metWhen: shown('lblCountry'), fix: 'Add the country of manufacture.',
        l4: { met: 'the label shows the country of manufacture' }
      },
      {
        id: 'lResponsible', part: 'label', ref: 'App II C.1(e)', binds: 'product',
        title: 'Name and address of the responsible company',
        text: 'The name and address of the company or person responsible for placing the product on the local market must appear. Article 8 makes this the address where the product information is kept.',
        metWhen: shown('lblResponsible'), fix: 'Add the local responsible company\'s name and address for each market.',
        l4: { met: 'the label shows the responsible company' }
      },
      {
        id: 'lContents', part: 'label', ref: 'App II C.1(f)', binds: 'product',
        title: 'Contents by weight or volume',
        text: 'The contents must be given by weight or volume, in metric units or in both metric and imperial units.',
        reading: 'Imperial units alone are treated as not enough.',
        metWhen: { all: [shown('lblContents'), { 'in': ['contentsUnits', ['metric', 'both']] }] },
        fix: 'State the contents in metric units.',
        l4: { met: 'the label shows the contents in accepted units' }
      },
      {
        id: 'lBatch', part: 'label', ref: 'App II C.1(g)', binds: 'product',
        title: 'Batch number',
        text: 'The manufacturer\'s batch number must appear.',
        metWhen: shown('lblBatch'), fix: 'Add the batch number.',
        l4: { met: 'the label shows the batch number' }
      },
      {
        id: 'lDate', part: 'label', ref: 'App II C.1(h)', binds: 'product',
        title: 'Manufacturing or expiry date',
        text: 'The manufacturing date or the expiry date must appear in clear terms, as month and year or as day, month and year in that order. An expiry date is mandatory where the product\'s minimum durability is less than 30 months.',
        metWhen: { all: [
          { any: [shown('lblExpiry'), shown('lblMfg')] },
          { implies: [{ lt: ['durability', 30] }, shown('lblExpiry')] },
          'dateFormat'
        ] },
        fix: 'Show an expiry date if durability is under 30 months; otherwise a manufacturing or expiry date, as month and year.',
        l4: { met: 'the label shows a sufficient date' }
      },
      {
        id: 'lExpiryWords', part: 'label', ref: 'App II C.1(h)', binds: 'product', advisory: true,
        title: 'Wording before the expiry date',
        text: 'The expiry date should be preceded by the words "expiry date" or "best before".',
        appliesWhen: shown('lblExpiry'), metWhen: 'expiryWords', fix: 'Put "expiry date" or "best before" in front of the date.',
        l4: { applies: 'an expiry date is shown', met: 'the expiry date is preceded by the words Appendix II suggests' }
      },
      {
        id: 'lPrecautions', part: 'label', ref: 'Art 6(2); App II C.1(i)', binds: 'product',
        title: 'Special precautions and required warnings',
        text: 'Special precautions to be observed in use must appear on the label, in particular the warnings that the Annexes require to be printed for a substance used, together with any other special precautionary information.',
        appliesWhen: 'needsPrecautions', metWhen: shown('lblPrecautions'), fix: 'Print the precautions and each Annex warning that applies.',
        l4: { applies: 'special precautions must be observed in use', met: 'the label shows the precautions' }
      },
      {
        id: 'lSmall', part: 'label', ref: 'App II C.2', binds: 'product',
        title: 'Name and batch number on a small container',
        text: 'Where the container cannot display all the particulars, they may go on a leaflet, hang tag, display panel or shrink wrap. The product name and the batch number must still appear on the immediate packaging.',
        appliesWhen: 'smallPack', metWhen: { all: ['nameOnImmediate', 'batchOnImmediate'] },
        fix: 'Print the name and batch number on the container itself.',
        l4: { applies: 'the container cannot carry all the particulars', met: 'the small container carries the name and batch number' }
      },
      {
        id: 'lLegible', part: 'label', ref: 'Art 6(1); App II C.3', binds: 'product',
        title: 'Legible, comprehensible and indelible',
        text: 'The particulars must be in legible and visible lettering, easily legible, clearly comprehensible and indelible.',
        metWhen: { all: ['lblLegible', 'lblIndelible'] }, fix: 'Rework the label so the particulars can be read and will not rub off.',
        l4: { met: 'the particulars are legible and indelible' }
      },
      {
        id: 'lLanguage', part: 'label', ref: 'App II C.4', binds: 'product',
        title: 'Language of the label',
        text: 'The particulars must be in English, the national language, or a language understood by consumers where the product is marketed. A Member State may require the name and function, instructions, responsible company, contents and precautions in its national language.',
        metWhen: 'lblLanguage', fix: 'Translate the label for each market that needs it.',
        l4: { met: 'the particulars are in an accepted language' }
      },
      {
        id: 'lMisleading', part: 'label', ref: 'Art 6(3)', binds: 'product',
        title: 'Nothing that implies characteristics the product lacks',
        text: 'In labelling, putting up for sale and advertising, text, names, trade marks, pictures and other signs must not be used to imply that the product has characteristics it does not have.',
        metWhen: 'noMisleading', fix: 'Remove the wording or imagery that overstates the product.',
        l4: { met: 'nothing in the labelling or advertising implies characteristics it lacks' }
      },

      // ---- Claims
      {
        id: 'cGuideline', part: 'claims', ref: 'Art 7(1)', binds: 'product',
        title: 'Claims comply with the Claims Guideline',
        text: 'Product claims must comply with the ASEAN Cosmetic Claims Guideline (Appendix III). Claims are subject to national control.',
        appliesWhen: 'makesClaims', metWhen: 'claimsGuideline', fix: 'Reword or drop the claims the Guideline does not allow for a cosmetic.',
        l4: { applies: 'a benefit is claimed for it', met: 'the claims comply with the Claims Guideline' }
      },
      {
        id: 'cEvidence', part: 'claims', ref: 'Art 7(2)', binds: 'product',
        title: 'Claimed benefits are justified',
        text: 'Claimed benefits must be justified by substantial evidence or by the formulation itself. The responsible company may generate the data with its own scientifically accepted protocols, provided it can justify the design.',
        appliesWhen: 'makesClaims', metWhen: 'claimsEvidence', fix: 'Assemble the evidence for each claim, or withdraw the claim.',
        l4: { applies: 'a benefit is claimed for it', met: 'each claimed benefit is justified by evidence or the formulation' }
      },

      // ---- Product information
      {
        id: 'fAccessible', part: 'file', ref: 'Arts 1(4), 8(1)', binds: 'you',
        title: 'Keep the product information accessible at the label address',
        text: 'The responsible company or person must keep the product\'s technical and safety information readily accessible to the regulatory authority of the Member State concerned, at the address specified on the label.',
        reading: 'Article 8(1) says the address specified "in accordance with Article 5". This rule reads that as Article 6.',
        appliesWhen: YOU, metWhen: 'pifAccessible', fix: 'Hold the file at the address printed on the label, ready for inspection.',
        l4: { applies: 'Article 8 binds you', met: 'the file is readily accessible at the address on the label' }
      },
      {
        id: 'fComposition', part: 'file', ref: 'Art 8(1)(a)', binds: 'you',
        title: 'Composition',
        text: 'The file must hold the qualitative and quantitative composition of the product. For a perfume composition: its name and code number, and the identity of the supplier.',
        appliesWhen: YOU, metWhen: { all: ['pifComposition', { implies: ['hasPerfume', 'pifPerfume'] }] },
        fix: 'Add the full formula, and the perfume supplier\'s details where there is one.',
        l4: { applies: 'Article 8 binds you', met: 'the file holds the composition' }
      },
      {
        id: 'fSpecs', part: 'file', ref: 'Art 8(1)(b)', binds: 'you',
        title: 'Specifications',
        text: 'The file must hold the specifications of the raw materials and of the finished product.',
        appliesWhen: YOU, metWhen: 'pifSpecs', fix: 'Add raw-material and finished-product specifications.',
        l4: { applies: 'Article 8 binds you', met: 'the file holds the specifications' }
      },
      {
        id: 'fMethod', part: 'file', ref: 'Art 8(1)(c)', binds: 'you',
        title: 'Method of manufacture',
        text: 'The file must hold the method of manufacture, complying with good manufacturing practice as laid down in the ASEAN Guidelines for Cosmetic Good Manufacturing Practice (Appendix VI).',
        appliesWhen: YOU, metWhen: 'pifMethod', fix: 'Document the manufacturing method and its compliance with the ASEAN guidelines.',
        l4: { applies: 'Article 8 binds you', met: 'the file holds a method of manufacture complying with good manufacturing practice' }
      },
      {
        id: 'fPerson', part: 'file', ref: 'Art 8(1)(c)', binds: 'you',
        title: 'Qualified person for manufacture or importation',
        text: 'The person responsible for manufacture, or for importation into the market, must have adequate knowledge or experience in accordance with the legislation and practice of the Member State of manufacture or importation.',
        appliesWhen: YOU, metWhen: 'qualifiedPerson', fix: 'Appoint a person who meets that Member State\'s requirements.',
        l4: { applies: 'Article 8 binds you', met: 'the person responsible for manufacture or importation is adequately qualified' }
      },
      {
        id: 'fSafety', part: 'file', ref: 'Art 8(1)(d)', binds: 'you',
        title: 'Safety assessment',
        text: 'The file must hold an assessment of the safety for human health of the finished product, its ingredients, its chemical structure and its level of exposure.',
        appliesWhen: YOU, metWhen: 'pifSafety', fix: 'Commission the safety assessment and file it.',
        l4: { applies: 'Article 8 binds you', met: 'the file holds the safety assessment' }
      },
      {
        id: 'fUndesirable', part: 'file', ref: 'Art 8(1)(e)', binds: 'you',
        title: 'Data on undesirable effects',
        text: 'The file must hold the existing data on undesirable effects on human health resulting from use of the product.',
        appliesWhen: YOU, metWhen: 'pifUndesirable', fix: 'Collect the adverse-effect reports you hold and file them.',
        l4: { applies: 'Article 8 binds you', met: 'the file holds the existing data on undesirable effects' }
      },
      {
        id: 'fClaims', part: 'file', ref: 'Art 8(1)(g)', binds: 'you',
        title: 'Supporting data for claims',
        text: 'Supporting data for the claimed benefits should be made available, to justify the nature of the product\'s effect.',
        reading: 'The item sits in a list the company "shall keep", but is itself worded "should be made available". This rule treats it as required where a benefit is claimed.',
        appliesWhen: { all: [YOU, 'makesClaims'] }, metWhen: 'pifClaimsData', fix: 'File the data behind each claim.',
        l4: { applies: 'Article 8(1)(g) binds you', met: 'the file holds supporting data for the claimed benefits' }
      },
      {
        id: 'fLanguage', part: 'file', ref: 'Art 8(2)', binds: 'you',
        title: 'Language of the file',
        text: 'The information must be available in the national language or languages of the Member State concerned, or in a language its regulatory authority readily understands.',
        appliesWhen: YOU, metWhen: 'pifLanguage', fix: 'Translate the file, or confirm the authority accepts its language.',
        l4: { applies: 'Article 8 binds you', met: 'the file is in a language the authority accepts' }
      },
      {
        id: 'aMethods', part: 'file', ref: 'Art 9(a)', binds: 'you',
        title: 'Methods of checking ingredients',
        text: 'The responsible company or person must make available to the regulatory authority the methods the manufacturer uses to check the ingredients, corresponding with the Certificate of Analysis.',
        appliesWhen: YOU, metWhen: 'art9Methods', fix: 'Obtain the manufacturer\'s test methods and hold them for the authority.',
        l4: { applies: 'Article 9 binds you', met: 'the methods of checking ingredients are available to the authority' }
      },
      {
        id: 'aCriteria', part: 'file', ref: 'Art 9(b)', binds: 'you',
        title: 'Microbiological and purity criteria',
        text: 'The responsible company or person must make available the criteria used for microbiological control of the product and for the chemical purity of its ingredients, or the methods for checking compliance with them.',
        appliesWhen: YOU, metWhen: 'art9Criteria', fix: 'Document the microbiological and purity criteria and hold them for the authority.',
        l4: { applies: 'Article 9 binds you', met: 'the microbiological and purity criteria are available to the authority' }
      }
    ],

    // Invented products, to show the console working. None is a real product or company.
    samples: [
      {
        id: 'sunscreen', name: 'Imported sunscreen, 50 ml tube',
        blurb: 'Already on sale in three Member States. Small tube, most particulars on a leaflet.',
        facts: {
          isResponsible: true, markets: ['SG', 'MY', 'TH'], notifiedIn: ['SG', 'MY'], onMarket: true, art11Measure: false,
          site: 'external', mainPurpose: true, hasAnnexV: false,
          safeConclusion: true, hasAnnexII: false, hasAnnexIII: true, annexIIIWithin: true,
          hasColour: false, hasPreservative: true, presListed: true, presWithin: true,
          hasUV: true, uvListed: true, uvWithin: false,
          smallPack: true, lblName: 'pack', functionClear: true, useClear: false, lblInstructions: 'insert',
          lblIngredients: 'insert', ingOrder: true, ingNames: true, hasBotanicals: true, botanicalNames: false,
          lblCountry: 'pack', lblResponsible: 'pack', lblContents: 'pack', contentsUnits: 'metric',
          lblBatch: 'insert', durability: 24, lblExpiry: 'none', lblMfg: 'pack', dateFormat: true,
          needsPrecautions: true, lblPrecautions: 'insert', nameOnImmediate: true, batchOnImmediate: false,
          lblLegible: true, lblIndelible: true, lblLanguage: true, noMisleading: true,
          makesClaims: true, claimsGuideline: true, claimsEvidence: true,
          pifAccessible: true, pifComposition: true, hasPerfume: true, pifPerfume: true, pifSpecs: true, pifMethod: true,
          qualifiedPerson: true, pifSafety: false, pifUndesirable: true, pifClaimsData: true, pifLanguage: true,
          art9Methods: true, art9Criteria: false
        }
      },
      {
        id: 'daycream', name: 'Day cream, before launch',
        blurb: 'Not yet on the market. One authority still to notify.',
        facts: {
          isResponsible: true, markets: ['ID', 'PH'], notifiedIn: ['ID'], onMarket: false, marketDate: '2026-12-01', art11Measure: false,
          site: 'external', mainPurpose: true, hasAnnexV: false,
          safeConclusion: true, hasAnnexII: false, hasAnnexIII: false,
          hasColour: true, colourHairOnly: false, colourListed: true, colourWithin: true,
          hasPreservative: true, presListed: true, presWithin: true, hasUV: false,
          smallPack: false, lblName: 'pack', functionClear: false, lblFunction: 'pack', useClear: true,
          lblIngredients: 'pack', ingOrder: true, ingNames: true, hasBotanicals: false,
          lblCountry: 'pack', lblResponsible: 'pack', lblContents: 'pack', contentsUnits: 'both',
          lblBatch: 'pack', durability: 36, lblExpiry: 'none', lblMfg: 'pack', dateFormat: true,
          needsPrecautions: false, lblLegible: true, lblIndelible: true, lblLanguage: true, noMisleading: true,
          makesClaims: true, claimsGuideline: true, claimsEvidence: true,
          pifAccessible: true, pifComposition: true, hasPerfume: false, pifSpecs: true, pifMethod: true,
          qualifiedPerson: true, pifSafety: true, pifUndesirable: true, pifClaimsData: true, pifLanguage: true,
          art9Methods: true, art9Criteria: true
        }
      },
      {
        id: 'drink', name: 'Collagen beauty drink',
        blurb: 'Sold as a beauty product, but swallowed.',
        facts: {
          isResponsible: true, markets: ['SG'], notifiedIn: [], onMarket: false, art11Measure: false,
          site: 'other', mainPurpose: true, hasAnnexV: false
        }
      }
    ]
  };
});
