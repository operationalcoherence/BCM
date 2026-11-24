# v262: distance haze (3D relief test, strategy 7; his go-ahead 11-24 16:16).
# Line maps only; place maps unchanged. Presentation only: the heights, colors, notes, ways, and words are unchanged.
# 1. Haze: ground farther than the point the camera looks at fades slightly toward a pale sky color, as distant
#    ridges do in his Bear Canyon photos (at most 20%, scaled to the current zoom). Pins, flags, and labels are not hazed.
# A denser, smoother mesh was tried (2x, then 1.5x): it changed nothing visible (the fine hatching on cliffs is the
#    painted rock detail, not the mesh), and 2x made tour.py time out. Dropped.
p = "tools/relief/relief.js"
s = open(p, encoding="utf-8").read()

old = """normal = bumpN(-vViewPosition, normal, rkH * rkM * 0.9);`); }; }"""
assert s.count(old) == 1
s = s.replace(old, """normal = bumpN(-vViewPosition, normal, rkH * rkM * 0.9);`)
      /* v262: distance haze, after the ground's color is final */
      .replace('#include <fog_fragment>', `#include <fog_fragment>
{ float hz = clamp((length(vViewPosition) - hazeN) / max(1.0, hazeF - hazeN), 0.0, 1.0); gl_FragColor.rgb = mix(gl_FragColor.rgb, vec3(0.86, 0.89, 0.93), hz * 0.2); }`)
      .replace('uniform sampler2D rockMask;', 'uniform sampler2D rockMask; uniform float hazeN; uniform float hazeF;');
    sh.uniforms.hazeN = HAZE.n; sh.uniforms.hazeF = HAZE.f; }; }""", 1)

old = "  const draw = () => renderer.render(scene, camera);"
assert s.count(old) == 1
s = s.replace(old, "  const HAZE = { n: { value: 1e5 }, f: { value: 2e5 } };\n  const draw = () => { if (!PL) { const d = camera.position.distanceTo(controls.target); HAZE.n.value = d * 0.9; HAZE.f.value = d * 1.5; } renderer.render(scene, camera); };", 1)
open(p, "w", encoding="utf-8").write(s)

p = "gsm-readable.js"; s = open(p, encoding="utf-8").read()
assert s.count('t.textContent = "v261"') == 1
s = s.replace('t.textContent = "v261"', 't.textContent = "v262"'); open(p, "w", encoding="utf-8").write(s)
