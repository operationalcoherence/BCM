# Pattern Synthesis only: the approved 3D relief model (gsm-relief.js, three.js) replaces the canvas map.
# Loaded on demand from next to gsm-preview.js; if it fails or there is no WebGL, the canvas map stays.
rep('function render(st){\n','function render(st){\n  if(host._rel){host._rel.hl(HL);return;}\n')
# cards: the relief follows the Show buttons; course rows carry their way letter for hover matching
rep('function render(st){\n  if(host._rel){host._rel.hl(HL);return;}\n','function render(st){\n  if(host._rel){host._rel.hl(HL);if(CARDH)host._rel.setWay(ROUTESEL);return;}\n')
rep('courseReadings(COURSE).forEach(function(r){var d=document.createElement("div");d.className="rd";','courseReadings(COURSE).forEach(function(r){var d=document.createElement("div");d.className="rd";if(r.k)d.setAttribute("data-way",r.k);')
