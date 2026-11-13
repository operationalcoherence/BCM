# Pattern Synthesis only: the approved 3D relief model (gsm-relief.js, three.js) replaces the canvas map.
# Loaded on demand from next to gsm-preview.js; if it fails or there is no WebGL, the canvas map stays.
rep('function render(st){\n','function render(st){\n  if(host._rel){host._rel.hl(HL);return;}\n')
