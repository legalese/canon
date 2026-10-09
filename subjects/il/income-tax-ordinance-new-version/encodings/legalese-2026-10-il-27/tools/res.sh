#!/usr/bin/env bash
# Print the outcome of each assertion in a module: line, outcome, message. Usage: tools/res.sh FILE.l4
L4="${L4:-l4}"
"$L4" run "$1" 2>&1 | awk '
/^  Range:/ {r=$2}
/^  Severity:/ {sev=$2}
/^  Message:/ {getline nxt; msg=$0 nxt; if (msg ~ /assertion|rror|Warning/ || sev ~ /Error|Warning/) print r, sev, msg}
' | sed 's/DiagnosticSeverity_//' | grep -v "assertion satisfied" | head -${2:-40}
"$L4" run "$1" 2>&1 | grep -c "assertion satisfied" | sed 's/^/satisfied lines: /'
