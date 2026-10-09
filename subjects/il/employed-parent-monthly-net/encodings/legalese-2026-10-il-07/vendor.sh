#!/usr/bin/env bash
# Copy the composed rows' rule modules flat into this directory, and check the copies.
#
# Why this exists: the l4 CLI resolves `IMPORT name` beside the importing file (then the
# embedded library), so a module in a sibling directory cannot be imported, and a symlink
# fails because the linked module's own imports are looked for beside the link (checked
# 2026-10-07; row IL-05's NOTES section 8 found the same). So the six rows' rule modules are
# copied here under their own file names. The copies are NOT committed (.gitignore); this
# script regenerates them, and VENDORED.sha256 (committed) pins what they must be.
#
# Only rule modules, their nouns and their published-figure modules are copied: never a
# row's tests, tests-independent.l4, DECIDED-ANSWERS.md, INDEPENDENT-FINDINGS.md or tools.
#
# Version 0.2.0 (2026-10-07) adds row IL-08's two halves, each in its own subject's directory:
# the modules the capstone composes and their import closure (the ITO half's s 1 and s 2
# modules are not composed and not copied). 36 + 14 = 50 modules.
#
# Version 0.6.0 (2026-10-09, BACKLOG IL-55) adds the rows for the new Laws the capstone composes,
# each from its own subject's directory where it has one: IL-36 (the Encouragement of Aliyah and
# Return (Temporary Provision) Law 5786-2026), IL-32 (the Minimum Wage Law 5747-1987, its figures
# module and what it imports), IL-28 (ITO ss 48 and 48A, the Area order and the foreign worker
# regulations), IL-25 (the National Health Insurance Law 5754-1994, s 14, for a cross-check only),
# IL-26 (ITO s 164 and the Deduction from Salary and Wages Regulations 5753-1993, for an entry
# point beside the pipeline; its copies of row IL-03's modules are the ones IL-03's line vendors).
# NOTES.md section 15.
#
# Usage:
#   vendor.sh            copy every module, then check it against VENDORED.sha256;
#                        fails if a row's source no longer matches what was recorded
#   vendor.sh --check    copy nothing; fail unless every copy exists, equals its source,
#                        and both equal the recorded sha256 (check.sh runs this first)
#   vendor.sh --record   copy every module and rewrite VENDORED.sha256 from the sources
#                        as they now stand (do this only after reading what changed)
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMMONS="$(cd "$HERE/../../../../.." && pwd)"
IL="$COMMONS/subjects/il"
ITO="$IL/income-tax-ordinance-new-version/encodings"
NII="$IL/national-insurance-law-consolidated-version-5755-1995/encodings"
ALIYAH="$IL/encouragement-of-aliyah-and-return-temporary-provision-law-5786-2026/encodings"
MW="$IL/minimum-wage-law-5747-1987/encodings"
NHI="$IL/national-health-insurance-law-5754-1994/encodings"
MANIFEST="$HERE/VENDORED.sha256"

# row  source-directory  module ... (each row's import closure, rule modules only)
rows() {
  echo "IL-01 $ITO/legalese-2026-10-il-01 ito-credit-points-nouns.l4 ito-s33a-credit-point.l4 ito-s34-s36-s36a-credits.l4 ito-credit-points-published-figures.l4"
  echo "IL-02 $ITO/legalese-2026-10-il-02 ito66-nouns.l4 ito66-tax-years.l4 ito66-d-common-source.l4 ito66-a-separate-calculation.l4 ito66-b-property-income.l4 ito66-ab-taxable-income.l4 ito66-c-credit-points.l4"
  echo "IL-03 $ITO/legalese-2026-10-il-03 ito-il03-nouns.l4 ito-120b-indexation.l4 ito-121-individual-rates.l4 ito-121b-additional-tax.l4"
  echo "IL-04 $NII/legalese-2026-10-il-04 nii-il04-nouns.l4 nii-il04-published-figures.l4 nii-s1-definitions.l4 nii-s334-interpretation.l4 nii-schedule-j-tables.l4 nii-schedule-j.l4 nii-s337-rates.l4"
  echo "IL-05 $NII/legalese-2026-10-il-05 nii-il05-nouns.l4 nii-il05-published-figures.l4 nii-schedule-k.l4 nii-s348-maximum-minimum.l4 nii-s342-liability-and-deduction.l4"
  echo "IL-06 $NII/legalese-2026-10-il-06 nii-il06-nouns.l4 nii-il06-period.l4 nii-s1-basic-amount.l4 nii-s65-interpretation.l4 nii-s66-entitlement.l4 nii-s67-count-of-children.l4 nii-s68-amount.l4 nii-il06-published-figures.l4 nii-il06-family-on-a-day.l4"
  echo "IL-08 $ITO/legalese-2026-10-il-08 ito-il08-nouns.l4 ito-il08-tax-years.l4 ito-il08-published-figures.l4 ito-s47a-definitions.l4 ito-s45a-insurance-and-pension-credit.l4 ito-s47-deduction.l4 ito-s40-children-credit-points.l4 ito-s37-s38-s39-spouse-credits.l4 ito-s35-new-immigrant.l4 ito-s64b-s65-registered-spouse.l4"
  echo "IL-08 $NII/legalese-2026-10-il-08 nii-il08-nouns.l4 nii-s72-period-of-allowance.l4 nii-s335-branches.l4 nii-schedule-a1-part-d.l4"
  echo "IL-28 $ITO/legalese-2026-10-il-28 ito-il28-nouns.l4 ito-s48-area-order.l4 ito-s48a-foreign-worker-regs.l4 ito-il28-routing.l4"
  echo "IL-26 $ITO/legalese-2026-10-il-26 ito-il26-nouns.l4 ito-il26-schedule-a.l4 ito-il26-published-figures.l4 ito-il26-regulations.l4"
  echo "IL-25 $NHI/legalese-2026-10-il-25 nhi-il25-nouns.l4 nhi-il25-published-figures.l4 nhi-s14-income.l4 nhi-s14-fixed-and-benefits.l4 nhi-s14-month.l4"
  echo "IL-32 $MW/legalese-2026-10-il-32 mw-il32-nouns.l4 mw-s1-definitions.l4 mw-il32-published-figures.l4"
  echo "IL-36 $ALIYAH/legalese-2026-10-il-36 il36-nouns.l4 il36-s1-definitions.l4 il36-s4-departure.l4 il36-s5-s6-commencement.l4 il36-s2-exemption.l4 il36-s3-entity.l4 il36-answers.l4"
}

sha() { shasum -a 256 "$1" | cut -d' ' -f1; }

# The commons commit that last touched a file, and whether the working tree differs from it.
# Read-only git: log and diff only.
commit_of() {
  local f="$1" c
  c="$(git -C "$COMMONS" log -1 --format=%H -- "$f" 2>/dev/null)"
  if ! git -C "$COMMONS" diff --quiet HEAD -- "$f" 2>/dev/null; then c="$c+uncommitted"; fi
  echo "${c:-uncommitted}"
}

mode="${1:-copy}"
status=0

case "$mode" in
  --record)
    tmp="$(mktemp "$HERE/.VENDORED.XXXXXX")"
    {
      echo "# sha256  row  module  commons-commit-of-source  source-path-relative-to-commons"
      echo "# Written by vendor.sh --record. Each vendored copy must equal this hash and its source."
    } > "$tmp"
    rows | while read -r row dir mods; do
      for m in $mods; do
        cp "$dir/$m" "$HERE/$m"
        echo "$(sha "$dir/$m")  $row  $m  $(commit_of "$dir/$m")  ${dir#$COMMONS/}/$m" >> "$tmp"
      done
    done
    mv "$tmp" "$MANIFEST"
    echo "vendor.sh: recorded $(grep -vc '^#' "$MANIFEST") modules in VENDORED.sha256"
    ;;
  copy|--check)
    [ -f "$MANIFEST" ] || { echo "vendor.sh: no VENDORED.sha256; run vendor.sh --record" >&2; exit 2; }
    while read -r want row m commit src; do
      case "$want" in \#*|"") continue ;; esac
      srcpath="$COMMONS/$src"
      if [ ! -f "$srcpath" ]; then echo "vendor.sh: $row $m: source missing at $src" >&2; status=1; continue; fi
      have_src="$(sha "$srcpath")"
      if [ "$have_src" != "$want" ]; then
        echo "vendor.sh: $row $m: the row's source has changed since it was recorded ($want -> $have_src); read the change, then vendor.sh --record" >&2
        status=1
      fi
      if [ "$mode" = copy ]; then cp "$srcpath" "$HERE/$m"; fi
      if [ ! -f "$HERE/$m" ]; then echo "vendor.sh: $row $m: no vendored copy; run vendor.sh" >&2; status=1; continue; fi
      have_copy="$(sha "$HERE/$m")"
      if [ "$have_copy" != "$want" ]; then
        echo "vendor.sh: $row $m: the vendored copy differs from the recorded hash ($have_copy); run vendor.sh" >&2
        status=1
      fi
    done < "$MANIFEST"
    # Every module rows() names must be in the manifest, and nothing else may be.
    want_list="$(rows | while read -r row dir mods; do for m in $mods; do echo "$m"; done; done | sort)"
    have_list="$(grep -v '^#' "$MANIFEST" | awk '{print $3}' | sort)"
    if [ "$want_list" != "$have_list" ]; then
      echo "vendor.sh: the module list in vendor.sh and VENDORED.sha256 disagree; run vendor.sh --record" >&2
      status=1
    fi
    [ "$status" -eq 0 ] && echo "vendor.sh: $(grep -vc '^#' "$MANIFEST") vendored modules match their sources and VENDORED.sha256"
    ;;
  *)
    echo "usage: vendor.sh [--check | --record]" >&2; exit 2 ;;
esac
exit $status
