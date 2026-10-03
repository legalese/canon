// Stated facts and the status each must produce, for the ASEAN Cosmetic Directive pack.
//
// Two readers. check.js runs every case through the engine. build.js writes every case whose
// duties are all settled into laws/acd-cases.l4 as #ASSERTs against laws/acd.l4, so the console's
// rules and the L4 are held to the same answers.
//
// `from` names a sample in the pack; `change` overrides facts (undefined removes an answer).
// `expect` maps duty ids to statuses; `verdict` is the overall result.

'use strict';

module.exports = [
  // Art 1(3)
  { name: 'Art 1(3): unnotified and on the market', from: 'daycream', change: { onMarket: true }, expect: { notify: 'breach' }, verdict: 'breach' },
  { name: 'Art 1(3): every market notified', from: 'daycream', change: { notifiedIn: ['ID', 'PH'] }, expect: { notify: 'met' }, verdict: 'clear' },
  { name: 'Art 1(3): an extra notification does no harm', from: 'daycream', change: { notifiedIn: ['ID', 'PH', 'SG'] }, expect: { notify: 'met' } },
  { name: 'Art 1(3): not the responsible person, so not your duty; labelling conditions hold whoever asks', from: 'daycream', change: { isResponsible: false }, expect: { notify: 'na', fSafety: 'na', aMethods: 'na', lBatch: 'met' } },
  { name: 'Art 1(3): cannot tell due from breached without knowing if it is on the market', from: 'daycream', change: { onMarket: undefined }, expect: { notify: 'unknown' } },

  // Art 2
  { name: 'Art 2(1): main purpose not cosmetic', from: 'daycream', change: { mainPurpose: false }, verdict: 'outside' },
  { name: 'Art 2(3): an Annex V substance takes it outside', from: 'daycream', change: { hasAnnexV: true }, verdict: 'outside' },
  { name: 'Art 2(1): the mouth is within the definition', from: 'daycream', change: { site: 'oral' }, verdict: 'due' },
  { name: 'Art 2(1): scope unanswered leaves everything open', from: 'daycream', change: { site: undefined }, verdict: 'incomplete' },

  // Art 3, 4, 5
  { name: 'Art 3(1): no safety conclusion', from: 'daycream', change: { safeConclusion: false }, expect: { safe: 'breach' } },
  { name: 'Art 4(3): unavoidable trace, product safe', from: 'daycream', change: { hasAnnexII: true, annexIITrace: true }, expect: { annexII: 'met' } },
  { name: 'Art 4(3): a trace does not help an unsafe product', from: 'daycream', change: { hasAnnexII: true, annexIITrace: true, safeConclusion: false }, expect: { annexII: 'breach' } },
  { name: 'Art 4(2)(a): more than a trace', from: 'daycream', change: { hasAnnexII: true, annexIITrace: false }, expect: { annexII: 'breach' } },
  { name: 'Art 4(2)(b): restricted substance outside its limits', from: 'daycream', change: { hasAnnexIII: true, annexIIIWithin: false }, expect: { annexIII: 'breach' } },
  { name: 'Art 4(2)(c): hair-colouring exception', from: 'daycream', change: { colourHairOnly: true }, expect: { colour: 'na' } },
  { name: 'Art 4(4)(b): provisional listing', from: 'daycream', change: { colourListed: false, unlistedCover: 'part2' }, expect: { colour: 'met', art5mark: 'na' } },
  { name: 'Art 4(2)(c): unlisted colouring agent', from: 'daycream', change: { colourListed: false, unlistedCover: 'none' }, expect: { colour: 'breach' } },
  { name: 'Art 4(2)(d): listed colouring agent outside its conditions', from: 'daycream', change: { colourWithin: false }, expect: { colour: 'breach' } },
  { name: 'Art 4(2)(c): unlisted, cover not yet stated', from: 'daycream', change: { colourListed: false }, expect: { colour: 'unknown' } },
  { name: 'Art 4(2)(f): other concentration for an apparent purpose', from: 'daycream', change: { presWithin: false, presSpecific: true }, expect: { preservative: 'met' } },
  { name: 'Art 4(2)(f): beyond the limit', from: 'daycream', change: { presWithin: false, presSpecific: false }, expect: { preservative: 'breach' } },
  { name: 'Art 4(2)(g): unlisted UV filter', from: 'sunscreen', change: { uvWithin: true, uvListed: false, unlistedCover: 'none' }, expect: { uv: 'breach' } },
  { name: 'Art 5(1)(c): indication not yet answered', from: 'daycream', change: { presListed: false, unlistedCover: 'art5' }, expect: { preservative: 'met', art5mark: 'unknown' } },
  { name: 'Art 5(1)(c): no distinctive indication', from: 'daycream', change: { presListed: false, unlistedCover: 'art5', art5Indication: false }, expect: { art5mark: 'breach' } },
  { name: 'Art 5(1)(c): distinctive indication borne', from: 'daycream', change: { presListed: false, unlistedCover: 'art5', art5Indication: true }, expect: { art5mark: 'met' } },

  // Art 6 and Appendix II
  { name: 'C.1(g): a leaflet is not enough when the container has room', from: 'daycream', change: { lblBatch: 'insert' }, expect: { lBatch: 'breach' } },
  { name: 'C.2: a leaflet is enough for a small container', from: 'daycream', change: { lblBatch: 'insert', smallPack: true, nameOnImmediate: true, batchOnImmediate: true }, expect: { lBatch: 'met', lSmall: 'met' } },
  { name: 'C.2(a): small container without the name on it', from: 'daycream', change: { smallPack: true, nameOnImmediate: false, batchOnImmediate: true }, expect: { lSmall: 'breach' } },
  { name: 'C.1(a): function neither clear nor stated', from: 'daycream', change: { functionClear: false, lblFunction: 'none' }, expect: { lFunction: 'breach' } },
  { name: 'C.1(a): no name', from: 'daycream', change: { lblName: 'none' }, expect: { lName: 'breach' } },
  { name: 'C.1(b): use neither clear nor stated', from: 'daycream', change: { useClear: false, lblInstructions: 'none' }, expect: { lUse: 'breach' } },
  { name: 'C.1(c): wrong order', from: 'daycream', change: { ingOrder: false }, expect: { lIngredients: 'breach' } },
  { name: 'C.1(c): botanicals named by genus and species', from: 'sunscreen', change: { botanicalNames: true }, expect: { lBotanicals: 'met' } },
  { name: 'C.1(d): no country of manufacture', from: 'daycream', change: { lblCountry: 'none' }, expect: { lCountry: 'breach' } },
  { name: 'C.1(e): no responsible company', from: 'daycream', change: { lblResponsible: 'none' }, expect: { lResponsible: 'breach' } },
  { name: 'C.1(f): imperial only', from: 'daycream', change: { contentsUnits: 'imperial' }, expect: { lContents: 'breach' } },
  { name: 'C.1(h): 30 months is not less than 30', from: 'daycream', change: { durability: 30 }, expect: { lDate: 'met' } },
  { name: 'C.1(h): 29 months needs an expiry date', from: 'daycream', change: { durability: 29 }, expect: { lDate: 'breach' } },
  { name: 'C.1(h): expiry date shown, without the suggested words', from: 'daycream', change: { durability: 29, lblExpiry: 'pack', lblMfg: undefined, expiryWords: false }, expect: { lDate: 'met', lExpiryWords: 'advice' } },
  { name: 'C.1(h): durability unknown, only a manufacturing date shown', from: 'daycream', change: { durability: undefined }, expect: { lDate: 'unknown' } },
  { name: 'C.1(h): an expiry date satisfies it whatever the durability', from: 'daycream', change: { durability: undefined, lblExpiry: 'pack', lblMfg: undefined, expiryWords: true }, expect: { lDate: 'met', lExpiryWords: 'met' } },
  { name: 'C.1(h): no date at all', from: 'daycream', change: { lblMfg: 'none' }, expect: { lDate: 'breach' } },
  { name: 'C.1(h): date not in the required form', from: 'daycream', change: { dateFormat: false }, expect: { lDate: 'breach' } },
  { name: 'Art 6(2): precautions not shown', from: 'daycream', change: { needsPrecautions: true, lblPrecautions: 'none' }, expect: { lPrecautions: 'breach' } },
  { name: 'C.3: label rubs off', from: 'daycream', change: { lblIndelible: false }, expect: { lLegible: 'breach' } },
  { name: 'C.4: label in no accepted language', from: 'daycream', change: { lblLanguage: false }, expect: { lLanguage: 'breach' } },
  { name: 'Art 6(3): misleading presentation', from: 'daycream', change: { noMisleading: false }, expect: { lMisleading: 'breach' } },

  // Arts 7, 8, 9, 11
  { name: 'Art 7: no claims made', from: 'daycream', change: { makesClaims: false }, expect: { cGuideline: 'na', cEvidence: 'na', fClaims: 'na' } },
  { name: 'Art 7(2): claim without evidence', from: 'daycream', change: { claimsEvidence: false }, expect: { cEvidence: 'breach', cGuideline: 'met' } },
  { name: 'Art 8(1): file not at the label address', from: 'daycream', change: { pifAccessible: false }, expect: { fAccessible: 'breach' } },
  { name: 'Art 8(1)(a): perfume supplier not identified', from: 'daycream', change: { hasPerfume: true, pifPerfume: false }, expect: { fComposition: 'breach' } },
  { name: 'Art 8(1)(g): claims made, no supporting data on file', from: 'daycream', change: { pifClaimsData: false }, expect: { fClaims: 'breach' } },
  { name: 'Art 9(a): test methods not available', from: 'daycream', change: { art9Methods: false }, expect: { aMethods: 'breach' } },
  { name: 'Art 11: a national measure stands against the product', from: 'daycream', change: { art11Measure: true }, expect: { art11: 'breach' } }
];
