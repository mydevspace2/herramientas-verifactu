#!/bin/sh
# Ejecuta todas las pruebas. Uso: sh qa/run-all.sh  (desde site/)
cd "$(dirname "$0")/.."
T=$(cd ../.tools && pwd)
export PLAYWRIGHT_BROWSERS_PATH=$T/browsers NODE_PATH=$T/node_modules:$(pwd)/qa/node_modules VF_GSV="$(cat ../gsv.txt)"
for c in "node qa/test-core.js" "node qa/test-b2b.js" "python3 qa/test-xsd-qr.py" "node qa/test-site.js"; do
  echo "== $c"; $c > /tmp/vf-$$.log 2>&1; echo "exit $?"; grep -c "✗" /tmp/vf-$$.log; grep -B0 "Resultado" /tmp/vf-$$.log | tail -1; tail -1 /tmp/vf-$$.log
done
for c in "node qa/test-browser-csp.js" "node qa/test-ux-mobile.js"; do
  echo "== $c"; $c > /tmp/vf-$$.log 2>&1; echo "exit $?"; grep -c "✗" /tmp/vf-$$.log; grep "✗" /tmp/vf-$$.log; tail -1 /tmp/vf-$$.log
done
