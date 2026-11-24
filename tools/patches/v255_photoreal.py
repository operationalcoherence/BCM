"""v255: toward photorealism (his note 11-24 10:08: "it is a great improvement, but I am just not seeing that photo
realism"). Line maps: the rock's fine detail (layers by height, grain) is drawn on the graphics card from each point's
3D position, sharp at any zoom and wrapping cliff faces instead of stretching down them, only where the ground is already
rock; the painted rock detail that streaked on cliffs is toned down; light from a whole sky; the ground mesh is 1.5 times as
fine each way, so ledges are crisp; hollows shade a little deeper. Colors, meaning, and place maps unchanged.
Usage: python3 v255_photoreal.py tools/relief/relief.js gsm-readable.js"""
import sys
R, G = sys.argv[1], sys.argv[2]
def patch(P, pairs):
    s = open(P).read()
    for a, b in pairs:
        c = s.count(a); assert c == 1, (P, c, a[:90]); s = s.replace(a, b)
    open(P, 'w').write(s)
PAIRS = [
[
"    return hr + gul * (1 - 0.5 * kt) + ter + (fbm(x * 0.08 + 3, y * 0.08 + 7, 4) - 0.5) * 1.1 * (1 - 0.8 * kt) + (fbm(x * 0.35, y * 0.35, 3) - 0.5) * 0.3 * (1 - 0.6 * kt); }\n  const MX = 2 * VX - 1, MY = 2 * VY - 1, CK = landKey(D), CH = CACHE.get(CK) || {};\n  const hGrid = CH.hGrid || new Float32Array(MX * MY); let hMin = 1e9;",
"    return hr + gul * (1 - 0.5 * kt) + ter + (fbm(x * 0.08 + 3, y * 0.08 + 7, 4) - 0.5) * 1.1 * (1 - 0.8 * kt) + (fbm(x * 0.35, y * 0.35, 3) - 0.5) * 0.3 * (1 - 0.6 * kt); }\n  const RS = PL ? 2 : 3, MX = RS * (VX - 1) + 1, MY = RS * (VY - 1) + 1, CK = landKey(D), CH = CACHE.get(CK) || {};\n  const hGrid = CH.hGrid || new Float32Array(MX * MY); let hMin = 1e9;"
],
[
"  const ncv = PL ? null : (CH.ncv || document.createElement('canvas')); if (ncv && !CH.ncv) { ncv.width = TW; ncv.height = TH; }\n  /* how much of the sky each spot sees: 8 directions out to ~24 map units, on every other grid point */",
"  const ncv = PL ? null : (CH.ncv || document.createElement('canvas')); if (ncv && !CH.ncv) { ncv.width = TW; ncv.height = TH; }\n  const mcv = PL ? null : (CH.mcv || document.createElement('canvas')); if (mcv && !CH.mcv) { mcv.width = TW; mcv.height = TH; }\n  /* how much of the sky each spot sees: 8 directions out to ~24 map units, on every other grid point */"
],
[
"  /* how much of the sky each spot sees: 8 directions out to ~24 map units, on every other grid point */\n  const AOW = (MX + 1) >> 1, AOH = (MY + 1) >> 1, HAO = CH.hao || new Float32Array(AOW * AOH);\n  if (!PL && !CH.hao) for (let j = 0; j < AOH; j++) for (let i = 0; i < AOW; i++) {",
"  /* how much of the sky each spot sees: 8 directions out to ~24 map units, on every other grid point */\n  const AOS = RS, AOW = Math.floor((MX - 1) / AOS) + 1, AOH = Math.floor((MY - 1) / AOS) + 1, HAO = CH.hao || new Float32Array(AOW * AOH);\n  if (!PL && !CH.hao) for (let j = 0; j < AOH; j++) for (let i = 0; i < AOW; i++) {"
],
[
"  if (!PL && !CH.hao) for (let j = 0; j < AOH; j++) for (let i = 0; i < AOW; i++) {\n    const x = Math.min(W, i * 2 / (MX - 1) * W), y = Math.min(H, j * 2 / (MY - 1) * H), h0 = gH(x, y); let occ = 0;\n    for (let k = 0; k < 8; k++) { const a = k * Math.PI / 4 + 0.3, dx = Math.cos(a), dy = Math.sin(a); let t = 0;",
"  if (!PL && !CH.hao) for (let j = 0; j < AOH; j++) for (let i = 0; i < AOW; i++) {\n    const x = Math.min(W, i * AOS / (MX - 1) * W), y = Math.min(H, j * AOS / (MY - 1) * H), h0 = gH(x, y); let occ = 0;\n    for (let k = 0; k < 8; k++) { const a = k * Math.PI / 4 + 0.3, dx = Math.cos(a), dy = Math.sin(a); let t = 0;"
],
[
"  if (!PL) CH.hao = HAO;\n  const aoAt = (x, y) => { const fx = Math.max(0, Math.min(AOW - 1.001, x / W * (MX - 1) / 2)), fy = Math.max(0, Math.min(AOH - 1.001, y / H * (MY - 1) / 2)), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j, g = (a, b) => HAO[b * AOW + a];\n    return g(i, j) * (1 - u) * (1 - v) + g(i + 1, j) * u * (1 - v) + g(i, j + 1) * (1 - u) * v + g(i + 1, j + 1) * u * v; };",
"  if (!PL) CH.hao = HAO;\n  const aoAt = (x, y) => { const fx = Math.max(0, Math.min(AOW - 1.001, x / W * (MX - 1) / AOS)), fy = Math.max(0, Math.min(AOH - 1.001, y / H * (MY - 1) / AOS)), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j, g = (a, b) => HAO[b * AOW + a];\n    return g(i, j) * (1 - u) * (1 - v) + g(i + 1, j) * u * (1 - v) + g(i, j + 1) * (1 - u) * v + g(i + 1, j + 1) * u * v; };"
],
[
"  function paint(base) {\n    const ctx = tcv.getContext('2d'), img = ctx.createImageData(TW, TH), px = img.data, bp = base && base.data, DT = ncv ? new Float32Array(TW * TH) : null;\n    const GR = [98, 108, 62], GR2 = [140, 134, 86], SO = [124, 96, 66], SO2 = [86, 68, 50], RK = [122, 118, 112], RK2 = [168, 160, 148], lum = q => 0.3 * q[0] + 0.59 * q[1] + 0.11 * q[2];",
"  function paint(base) {\n    const ctx = tcv.getContext('2d'), img = ctx.createImageData(TW, TH), px = img.data, bp = base && base.data, DT = ncv ? new Float32Array(TW * TH) : null, RW = ncv ? new Uint8Array(TW * TH) : null;\n    const GR = [98, 108, 62], GR2 = [140, 134, 86], SO = [124, 96, 66], SO2 = [86, 68, 50], RK = [122, 118, 112], RK2 = [168, 160, 148], lum = q => 0.3 * q[0] + 0.59 * q[1] + 0.11 * q[2];"
],
[
"          const rough = fbm(x * 2.2, y * 2.2, 3) - 0.5;\n          rock = mix(mix(rc, LICH, lich), VARN, Math.max(streak, crack * 0.6, joint * 0.45, under * 0.35, riser * 0.22)).map(v => v * (1 + rough * 0.4) * (1 + lip * 0.08));\n          dR = -0.32 * under + 0.08 * lip - 0.45 * crack - 0.25 * joint + 0.36 * rough;\n        }",
"          const rough = fbm(x * 2.2, y * 2.2, 3) - 0.5;\n          rock = mix(mix(rc, LICH, lich), VARN, Math.max(streak, crack * 0.2, joint * 0.15, under * 0.2, riser * 0.22)).map(v => v * (1 + rough * 0.1) * (1 + lip * 0.04));\n          dR = (-0.32 * under + 0.08 * lip - 0.45 * crack - 0.25 * joint + 0.36 * rough) * 0.3;\n        }"
],
[
"      let c = bp ? [bp[o0], bp[o0 + 1], bp[o0 + 2]] : mix(mix(grass, soil, tS + sstep(-0.4, -1.0, h / HS) * 0.5 * (1 - tR)), rock, tR); const kk = bp ? 1 : PL ? 0.93 + 0.14 * sp : 0.96 + 0.08 * sp; c = c.map(v => v * kk);\n      let ao = Math.max(-0.28, Math.min(0.18, -lap * (PL ? 0.5 : 0.11))); if (!PL) ao = Math.max(-0.42, ao * 0.7 - aoAt(x, y) * 0.4); c = c.map(v => v * (1 + ao));\n      /* v243: a place gets a hillshade over its imagery (light from the northwest, 45\u00b0 up) so benches and slopes read */",
"      let c = bp ? [bp[o0], bp[o0 + 1], bp[o0 + 2]] : mix(mix(grass, soil, tS + sstep(-0.4, -1.0, h / HS) * 0.5 * (1 - tR)), rock, tR); const kk = bp ? 1 : PL ? 0.93 + 0.14 * sp : 0.96 + 0.08 * sp; c = c.map(v => v * kk);\n      let ao = Math.max(-0.28, Math.min(0.18, -lap * (PL ? 0.5 : 0.11))); if (!PL) ao = Math.max(-0.42, ao * 0.7 - aoAt(x, y) * 0.5); c = c.map(v => v * (1 + ao));\n      /* v243: a place gets a hillshade over its imagery (light from the northwest, 45\u00b0 up) so benches and slopes read */"
],
[
"      const o = (py * TW + pxx) * 4; px[o] = c[0]; px[o + 1] = c[1]; px[o + 2] = c[2]; px[o + 3] = 255;\n      if (DT) { const rw = Math.max(tR, gap); DT[py * TW + pxx] = dG * (1 - rw) + dR * rw; }\n    }",
"      const o = (py * TW + pxx) * 4; px[o] = c[0]; px[o + 1] = c[1]; px[o + 2] = c[2]; px[o + 3] = 255;\n      if (DT) { const rw = Math.max(tR, gap); DT[py * TW + pxx] = dG * (1 - rw) + dR * rw; RW[py * TW + pxx] = rw * 255; }\n    }"
],
[
"        nd[o] = (nx / l * 0.5 + 0.5) * 255; nd[o + 1] = (ny / l * 0.5 + 0.5) * 255; nd[o + 2] = (1 / l * 0.5 + 0.5) * 255; nd[o + 3] = 255; }\n      nctx.putImageData(ni, 0, 0); }\n  }",
"        nd[o] = (nx / l * 0.5 + 0.5) * 255; nd[o + 1] = (ny / l * 0.5 + 0.5) * 255; nd[o + 2] = (1 / l * 0.5 + 0.5) * 255; nd[o + 3] = 255; }\n      nctx.putImageData(ni, 0, 0);\n      const mctx = mcv.getContext('2d'), mi = mctx.createImageData(TW, TH), md = mi.data; for (let q = 0; q < RW.length; q++) { md[4 * q] = md[4 * q + 1] = md[4 * q + 2] = RW[q]; md[4 * q + 3] = 255; } mctx.putImageData(mi, 0, 0); }\n  }"
],
[
"  if (!CH.tcv) paint(null);\n  CH.tcv = tcv; if (ncv) CH.ncv = ncv;\n  /* a place: Esri imagery, roads and place names under the emotion color; areas drawn as shaded patches */",
"  if (!CH.tcv) paint(null);\n  CH.tcv = tcv; if (ncv) { CH.ncv = ncv; CH.mcv = mcv; }\n  /* a place: Esri imagery, roads and place names under the emotion color; areas drawn as shaded patches */"
],
[
"  /* v253: on line maps a sky that is a little blue and a ground that bounces warm, and a lower, warmer sun from the same side */\n  scene.add(PL ? new THREE.HemisphereLight(0xffffff, 0x9a9384, 1.0) : new THREE.HemisphereLight(0xe2ebf5, 0x8f7c66, 1.05));\n  const sun = new THREE.DirectionalLight(PL ? 0xfff6ea : 0xfff0dc, 3.3); if (PL) sun.position.set(-260, 260, -160); else sun.position.set(-290, 215, -175); sun.castShadow = true;",
"  /* v253: on line maps a sky that is a little blue and a ground that bounces warm, and a lower, warmer sun from the same side */\n  scene.add(PL ? new THREE.HemisphereLight(0xffffff, 0x9a9384, 1.0) : new THREE.HemisphereLight(0xe2ebf5, 0x8f7c66, 0.85));\n  const sun = new THREE.DirectionalLight(PL ? 0xfff6ea : 0xfff0dc, 3.3); if (PL) sun.position.set(-260, 260, -160); else sun.position.set(-290, 215, -175); sun.castShadow = true;"
],
[
"  const fill = new THREE.DirectionalLight(0xffffff, 0.9); fill.position.set(120, 90, 400); scene.add(fill);\n  const X = x => x - W / 2, Z = y => y - H / 2;",
"  const fill = new THREE.DirectionalLight(0xffffff, 0.9); fill.position.set(120, 90, 400); scene.add(fill);\n  /* v255: on line maps the light also comes from the whole sky (blue above, warm ground below), as outdoors */\n  if (!PL) { const sk = new THREE.Scene(), sg = new THREE.SphereGeometry(10, 32, 16), sm = new THREE.ShaderMaterial({ side: THREE.BackSide, vertexShader: 'varying vec3 d; void main(){ d = position; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',\n      fragmentShader: 'varying vec3 d; void main(){ float y = normalize(d).y; vec3 c = y > 0.0 ? mix(vec3(0.95, 0.93, 0.88), vec3(0.55, 0.68, 0.88), pow(y, 0.6)) : mix(vec3(0.62, 0.52, 0.42), vec3(0.32, 0.27, 0.22), -y); gl_FragColor = vec4(c * 1.4, 1.0); }' });\n    sk.add(new THREE.Mesh(sg, sm)); const pm = new THREE.PMREMGenerator(renderer); scene.environment = pm.fromScene(sk, 0.02).texture; scene.environmentIntensity = 0.3; pm.dispose(); }\n  const draw = () => renderer.render(scene, camera);\n  const X = x => x - W / 2, Z = y => y - H / 2;"
],
[
"  const tmat = new THREE.MeshStandardMaterial({ map: tex, roughness: 0.95 }); if (ncv) { const nt = new THREE.CanvasTexture(ncv); nt.anisotropy = 8; tmat.normalMap = nt; tmat.normalScale.set(1, 1); }\n  const terrain = new THREE.Mesh(geo, tmat); terrain.castShadow = terrain.receiveShadow = true; scene.add(terrain);",
"  const tmat = new THREE.MeshStandardMaterial({ map: tex, roughness: 0.95 }); if (ncv) { const nt = new THREE.CanvasTexture(ncv); nt.anisotropy = 8; tmat.normalMap = nt; tmat.normalScale.set(1, 1); }\n  /* v255: the rock's fine detail is drawn on the graphics card from each point's real position in 3D (layers by height,\n     grain, cracks), so it stays sharp at any zoom and wraps cliff faces instead of stretching down them. It shows only\n     where the painted ground is already rock (the mask), so where rock sits is unchanged. Finer than a pixel fades out. */\n  if (mcv) { const mt = new THREE.CanvasTexture(mcv); tmat.onBeforeCompile = sh => { sh.uniforms.rockMask = { value: mt };\n    sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\\nvarying vec3 vWP;').replace('#include <worldpos_vertex>', '#include <worldpos_vertex>\\nvWP = (modelMatrix * vec4(transformed, 1.0)).xyz;');\n    sh.fragmentShader = sh.fragmentShader.replace('#include <common>', `#include <common>\nvarying vec3 vWP; uniform sampler2D rockMask;\nfloat h3(vec3 p){ p = fract(p * 0.1031); p += dot(p, p.zyx + 31.32); return fract((p.x + p.y) * p.z); }\nfloat n3(vec3 x){ vec3 i = floor(x), f = fract(x); f = f * f * (3.0 - 2.0 * f);\n  return mix(mix(mix(h3(i), h3(i + vec3(1,0,0)), f.x), mix(h3(i + vec3(0,1,0)), h3(i + vec3(1,1,0)), f.x), f.y),\n             mix(mix(h3(i + vec3(0,0,1)), h3(i + vec3(1,0,1)), f.x), mix(h3(i + vec3(0,1,1)), h3(i + vec3(1,1,1)), f.x), f.y), f.z); }\nfloat rockH(vec3 p, float fw, out float tone){\n  float s = p.y * 1.7 + p.x * 0.06 + (n3(p * 0.25) - 0.5) * 2.4, lay = floor(s), b = s - lay;\n  tone = h3(vec3(lay, 3.0, 7.0));\n  float h = smoothstep(0.72, 0.9, b) * 0.3 * smoothstep(0.5, 0.18, fw * 1.7);\n  float a = 0.55, f = 1.1;\n  for (int k = 0; k < 3; k++) { h += a * (n3(p * f + float(k) * 7.1) - 0.5) * smoothstep(0.45, 0.15, fw * f); f *= 2.15; a *= 0.5; }\n  return h; }\nvec3 bumpN(vec3 sp, vec3 n, float h){ vec3 dx = dFdx(sp), dy = dFdy(sp), r1 = cross(dy, n), r2 = cross(n, dx); float det = dot(dx, r1);\n  vec3 g = sign(det) * (dFdx(h) * r1 + dFdy(h) * r2); return normalize(abs(det) * n - g); }\nfloat rkM; float rkH; float rkT;`)\n      .replace('#include <map_fragment>', `#include <map_fragment>\nrkM = texture2D(rockMask, vMapUv).r; { float fw = length(fwidth(vWP)); rkH = rockH(vWP, fw, rkT); }\ndiffuseColor.rgb *= mix(1.0, (0.86 + 0.28 * rkT) * (1.0 + rkH * 0.55), rkM);`)\n      .replace('#include <normal_fragment_maps>', `#include <normal_fragment_maps>\nnormal = bumpN(-vViewPosition, normal, rkH * rkM * 0.9);`); }; }\n  const terrain = new THREE.Mesh(geo, tmat); terrain.castShadow = terrain.receiveShadow = true; scene.add(terrain);"
],
[
"    if (!!(D.card && host.closest('.gtfs-on')) !== lastCfs) dirty = true;\n    if (dirty && wrap.clientWidth) { RD.forEach(o => o.rim && o.rim.quaternion.copy(camera.quaternion)); if ((wrap.clientWidth !== lastW || !!(D.card && host.closest('.gtfs-on')) !== lastCfs) && !wrap.classList.contains('fs')) { lastCfs = !!(D.card && host.closest('.gtfs-on')); size(); } renderer.render(scene, camera); place(); dirty = false; } requestAnimationFrame(loop); }\n  function dispose() { if (!alive) return; alive = false; if (ro) ro.disconnect(); window.removeEventListener('resize', size); document.removeEventListener('keydown', onKey); document.removeEventListener('click', offClick, true); renderer.dispose(); try { renderer.forceContextLoss(); } catch (e) {} }",
"    if (!!(D.card && host.closest('.gtfs-on')) !== lastCfs) dirty = true;\n    if (dirty && wrap.clientWidth) { RD.forEach(o => o.rim && o.rim.quaternion.copy(camera.quaternion)); if ((wrap.clientWidth !== lastW || !!(D.card && host.closest('.gtfs-on')) !== lastCfs) && !wrap.classList.contains('fs')) { lastCfs = !!(D.card && host.closest('.gtfs-on')); size(); } draw(); place(); dirty = false; } requestAnimationFrame(loop); }\n  function dispose() { if (!alive) return; alive = false; if (ro) ro.disconnect(); window.removeEventListener('resize', size); document.removeEventListener('keydown', onKey); document.removeEventListener('click', offClick, true); renderer.dispose(); try { renderer.forceContextLoss(); } catch (e) {} }"
],
[
"  return { loops, hoses, hoseCount() { return hoseN; }, focusQ, tour: startTour, touring() { return !!TOUR; }, paused() { return !!TOUR && TOUR.paused != null; }, hl(i) { if (!pinned) RD.forEach((o, k) => o.el.classList.toggle('on', k === i)); }, setWay(k) { if (k !== selWay) { selWay = k; showWays(); } }, hoverWay(k) { hoverWay(k); },\n    snap() { renderer.render(scene, camera); return renderer.domElement.toDataURL('image/jpeg', 0.85); }, height() { return wrap.offsetHeight; }, dispose };\n}",
"  return { loops, hoses, hoseCount() { return hoseN; }, focusQ, tour: startTour, touring() { return !!TOUR; }, paused() { return !!TOUR && TOUR.paused != null; }, hl(i) { if (!pinned) RD.forEach((o, k) => o.el.classList.toggle('on', k === i)); }, setWay(k) { if (k !== selWay) { selWay = k; showWays(); } }, hoverWay(k) { hoverWay(k); },\n    snap() { draw(); return renderer.domElement.toDataURL('image/jpeg', 0.85); }, height() { return wrap.offsetHeight; }, dispose };\n}"
]
]
patch(R, PAIRS)
patch(G, [('t && (t.textContent = "v254");', 't && (t.textContent = "v255");')])
