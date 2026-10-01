#!/usr/bin/env bash
# Build the signed C2PA files this encoding's census runs on.
#
# Two files are REAL third-party test files, copied unchanged from the C2PA reference
# library's own fixtures (contentauth/c2pa-rs, MIT or Apache-2.0):
#   c2pa-rs-camera-capture.jpg   <- sdk/tests/fixtures/C_with_CAWG_data.jpg
#   c2pa-rs-colour-adjusted.jpg  <- sdk/tests/fixtures/CA.jpg
#
# The others are SYNTHETIC: a 64x64 flat-colour JPEG, or the camera capture above as a
# parent ingredient, signed here by c2patool with its built-in "C2PA Test Signing Cert"
# and time-stamped by DigiCert's public time-stamping authority. They validate as
# "Valid", not "Trusted": the test certificate is not on the C2PA trust list. No
# generator made them. They show what a manifest of each kind states, nothing more.
# In particular, the one that DECLARES a watermark does not carry one.
#
# Requires: c2patool 0.27.22 (C2PATOOL), gh, python3 with Pillow, network access.
# Usage:    C2PATOOL=/path/to/c2patool ./build-fixtures.sh
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
C2PATOOL="${C2PATOOL:-c2patool}"
C2PA_RS_SHA=518fe03a4a09dd38b68c1c5215d572fb1116bb66
TA=http://timestamp.digicert.com
mkdir -p files

fetch() {  # fetch <fixture name> <output>
  curl -fsSL "https://raw.githubusercontent.com/contentauth/c2pa-rs/${C2PA_RS_SHA}/sdk/tests/fixtures/$1" -o "files/$2"
}
fetch C_with_CAWG_data.jpg c2pa-rs-camera-capture.jpg
fetch CA.jpg               c2pa-rs-colour-adjusted.jpg

python3 -c "from PIL import Image; Image.new('RGB',(64,64),(120,90,200)).save('files/base.jpg', quality=90)"

sign() {  # sign <base> <out> <config-json> [extra c2patool args...]
  local base=$1 out=$2 cfg=$3; shift 3
  "$C2PATOOL" "files/$base" -c "$cfg" -o "files/$out" -f "$@" >/dev/null
}

DST=http://cv.iptc.org/newscodes/digitalsourcetype

# 1. Generated from a prompt by a generative model.
sign base.jpg ai-generated.jpg \
  "{\"ta_url\":\"$TA\",\"title\":\"AI-generated image (synthetic, test-signed)\",
    \"claim_generator_info\":[{\"name\":\"babel-fixture-generator\",\"version\":\"0.1.0\"}],
    \"assertions\":[{\"label\":\"c2pa.actions\",\"data\":{\"actions\":[
      {\"action\":\"c2pa.created\",\"digitalSourceType\":\"$DST/trainedAlgorithmicMedia\"}]}}]}"

# 2. The same, declaring that a watermark was inserted to bind the manifest (C2PA 2.3
#    "fine-grained watermarking actions"). The file carries no actual watermark.
sign base.jpg ai-generated-watermark-declared.jpg \
  "{\"ta_url\":\"$TA\",\"title\":\"AI-generated image declaring a watermark (synthetic, test-signed)\",
    \"claim_generator_info\":[{\"name\":\"babel-fixture-generator\",\"version\":\"0.1.0\"}],
    \"assertions\":[{\"label\":\"c2pa.actions\",\"data\":{\"actions\":[
      {\"action\":\"c2pa.created\",\"digitalSourceType\":\"$DST/trainedAlgorithmicMedia\"},
      {\"action\":\"c2pa.watermarked.bound\"}]}}]}"

# 3-5. The camera capture, edited by an AI system.
edit() {  # edit <out> <action> <source type> <description>
  local cfg="{\"ta_url\":\"$TA\",\"title\":\"$4 (synthetic, test-signed)\",
    \"claim_generator_info\":[{\"name\":\"babel-fixture-editor\",\"version\":\"0.1.0\"}],
    \"assertions\":[{\"label\":\"c2pa.actions\",\"data\":{\"actions\":[
      {\"action\":\"$2\",\"digitalSourceType\":\"$DST/$3\",\"description\":\"$4\"}]}}]}"
  "$C2PATOOL" files/c2pa-rs-camera-capture.jpg -c "$cfg" -p files/c2pa-rs-camera-capture.jpg -o "files/$1" -f >/dev/null
}
edit ai-object-removed.jpg c2pa.edited   compositeWithTrainedAlgorithmicMedia "removal of an object by generative fill"
edit ai-filtered.jpg       c2pa.filtered compositeWithTrainedAlgorithmicMedia "a stylistic filter applied by a generative model"
edit ai-red-eye-removed.jpg c2pa.edited  algorithmicallyEnhanced              "removal of red-eye by an AI system"

# 6. The AI-generated image with its manifest gone: the pixels re-saved by Pillow,
#    which writes no C2PA data. This is what a platform that strips metadata delivers.
python3 -c "from PIL import Image; Image.open('files/ai-generated.jpg').save('files/ai-generated-stripped.jpg', quality=90)"

rm -f files/base.jpg
for f in files/*.jpg; do
  printf '%s  %s\n' "$(shasum -a 256 "$f" | cut -d' ' -f1)" "$(basename "$f")"
done > files/SHA256SUMS
echo "built: $(ls files/*.jpg | wc -l | tr -d ' ') files"
