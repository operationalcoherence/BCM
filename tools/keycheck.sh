#!/bin/sh
# Key check before every push (replaces the manual `grep -c 'AAPK\|AIza'` = 0).
# Esri keys (AAPK…) are never allowed in the repo: the Esri key lives in the Webador block.
# Google keys (AIza…) are allowed only if listed in tools/allowed_keys.txt, one per line. That file is meant to hold
# exactly one key: the Firebase web key for F8, added on purpose during the build and restricted to the BCM sites
# in Google Cloud. Any other key fails the check.
#   sh tools/keycheck.sh            checks gsm-preview.js, gsm-readable.js, gsm-relief.js and the stubs
cd "$(dirname "$0")/.." || exit 2
ALLOW=tools/allowed_keys.txt
FILES="gsm-preview.js gsm-readable.js gsm-relief.js webador_stub_tiny_LIVE.html webador_stub_tiny_PREVIEW.html"
[ -f gsm.js ] && FILES="$FILES gsm.js"
fail=0
if grep -l 'AAPK' $FILES >/dev/null 2>&1; then echo "FAIL: an Esri key (AAPK) is in: $(grep -l 'AAPK' $FILES | tr '\n' ' ')"; fail=1; fi
n=$(grep -v '^#' "$ALLOW" 2>/dev/null | grep -c 'AIza')
[ "$n" -gt 1 ] && { echo "FAIL: $ALLOW lists $n keys; it may list only one"; fail=1; }
for k in $(grep -oh 'AIza[0-9A-Za-z_-]\{35\}' $FILES | sort -u); do
  if ! grep -v '^#' "$ALLOW" 2>/dev/null | grep -qx "$k"; then echo "FAIL: a Google key not in $ALLOW: ${k%${k#????????}}…"; fail=1; fi
done
[ $fail = 0 ] && echo "key check OK"
exit $fail
