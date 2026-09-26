#!/bin/bash
# Reproduction transcript. Run from inside Israel WITHOUT the --socks5-hostname flag;
# from elsewhere the site is geo-blocked, hence the SOCKS tunnel.
cd "$(dirname "$0")"
P="--socks5-hostname localhost:1080"
show() { printf '$ %s\n' "$1"; }
RES='https://api.justice.gov.il/reshumot/resolver?path='
BAD='akn%2Fil%2FofficialGazette%2FgeneralSL%2F5587%2Fheb%401994-03-21'
GOOD='akn%2Fil%2FofficialGazette%2FstatuteBook%2F3541%2Fheb%402026-06-30'

show "curl -s -o /dev/null -D - \"$RES$BAD\" | grep -iE '^(HTTP|location|content-type)' | sed -E 's/(\?X-Amz-Algorithm=).*/\1…/'"
curl -s $P -o /dev/null -D - "$RES$BAD" | tr -d '\r' | grep -iE '^(HTTP|location|content-type)' | sed -E 's/(\?X-Amz-Algorithm=).*/\1…/'
echo
show "curl -sL -D headers.txt -o generalSL-5587.pdf \"$RES$BAD\""
curl -sL $P -D headers.txt -o generalSL-5587.pdf "$RES$BAD"
show "grep -iE '^(HTTP|Content-Type|Content-Disposition|Content-Length)' headers.txt | tail -4"
tr -d '\r' < headers.txt | grep -iE '^(HTTP|Content-Type|Content-Disposition|Content-Length)' | tail -4
echo
show "file generalSL-5587.pdf"
file generalSL-5587.pdf
show "pdfinfo generalSL-5587.pdf 2>&1 | head -3"
pdfinfo generalSL-5587.pdf 2>&1 | head -3
echo
show "head -c 160 generalSL-5587.pdf | cat -v"
head -c 160 generalSL-5587.pdf | cat -v; echo
echo
show "tail -c 60 generalSL-5587.pdf | cat -v"
tail -c 60 generalSL-5587.pdf | cat -v; echo
echo
show "/usr/bin/grep -abo '%PDF-' generalSL-5587.pdf | head -1"
/usr/bin/grep -abo '%PDF-' generalSL-5587.pdf | head -1
show "/usr/bin/grep -abo '%%EOF' generalSL-5587.pdf | tail -1"
/usr/bin/grep -abo '%%EOF' generalSL-5587.pdf | tail -1
show "wc -c < generalSL-5587.pdf"
wc -c < generalSL-5587.pdf | tr -d ' '
echo
START=$(/usr/bin/grep -abo '%PDF-' generalSL-5587.pdf | head -1 | cut -d: -f1)
END=$(/usr/bin/grep -abo '%%EOF' generalSL-5587.pdf | tail -1 | cut -d: -f1)
show "tail -c +$((START+1)) generalSL-5587.pdf | head -c $((END-START+5)) > generalSL-5587.unwrapped.pdf"
tail -c +$((START+1)) generalSL-5587.pdf | head -c $((END-START+5)) > generalSL-5587.unwrapped.pdf
show "file generalSL-5587.unwrapped.pdf"
file generalSL-5587.unwrapped.pdf
show "pdfinfo generalSL-5587.unwrapped.pdf | grep -E '^(Pages|Producer|Creator|Title)'"
pdfinfo generalSL-5587.unwrapped.pdf | grep -E '^(Pages|Producer|Creator|Title)'
echo
echo "# ---- control: a born-digital issue from the same resolver is a plain PDF ----"
show "curl -sL -o statuteBook-3541.pdf \"$RES$GOOD\" && head -c 8 statuteBook-3541.pdf | cat -v && echo && file statuteBook-3541.pdf"
curl -sL $P -o statuteBook-3541.pdf "$RES$GOOD" && head -c 8 statuteBook-3541.pdf | cat -v && echo && file statuteBook-3541.pdf
echo
echo "# ---- the S3 object keys the resolver redirects to (query string elided) ----"
for p in "$BAD" "akn%2Fil%2FofficialGazette%2FstatuteBook%2F57%2Fheb%401950-08-09" "akn%2Fil%2FofficialGazette%2FstatuteBook%2F1964%2Fheb%402004-12-13" "$GOOD" "akn%2Fil%2FofficialGazette%2FstatuteBook%2F1976%2Fheb%402005-01-26"; do
  show "curl -s -o /dev/null -w '%{redirect_url}\n' \"$RES$p\" | sed -E 's/\?.*//'"
  curl -s $P -o /dev/null -w '%{redirect_url}\n' "$RES$p" | sed -E 's/\?.*//'
done
