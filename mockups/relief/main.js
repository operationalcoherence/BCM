import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

const D = window.DATA;
const VX = D.VX, VY = D.VY, CX = D.CX, CY = D.CY;
const W = (VX - 1) * CX, H = (VY - 1) * CY;
const HS = 58;                       // height scale (engine hn -> model units)
let STYLE = 'field', ALPHA = 0.45;

/* ---------- noise ---------- */
function hash(x, y) { let h = x * 374761393 + y * 668265263; h = (h ^ (h >>> 13)) * 1274126177; return ((h ^ (h >>> 16)) >>> 0) / 4294967295; }
function vn(x, y) { const i = Math.floor(x), j = Math.floor(y), u = x - i, v = y - j, su = u * u * (3 - 2 * u), sv = v * v * (3 - 2 * v);
  const a = hash(i, j), b = hash(i + 1, j), c = hash(i, j + 1), d = hash(i + 1, j + 1); return a + (b - a) * su + (c - a) * sv + (a - b - c + d) * su * sv; }
function fbm(x, y, o = 5) { let s = 0, a = 0.5, f = 1; for (let k = 0; k < o; k++) { s += a * vn(x * f, y * f); f *= 2.03; a *= 0.5; } return s; }
function ridged(x, y, o = 4) { let s = 0, a = 0.5, f = 1; for (let k = 0; k < o; k++) { const n = 1 - Math.abs(vn(x * f, y * f) * 2 - 1); s += a * n * n; f *= 2.1; a *= 0.5; } return s; }
const sstep = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
const mix = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];

/* ---------- height field (map coords x 0..W, y 0..H) ---------- */
function bil(arr, x, y, stride = 1, off = 0) {
  const fx = Math.max(0, Math.min(VX - 1.001, x / CX)), fy = Math.max(0, Math.min(VY - 1.001, y / CY));
  const i = fx | 0, j = fy | 0, u = fx - i, v = fy - j;
  const g = (ii, jj) => arr[(jj * VX + ii) * stride + off];
  return g(i, j) * (1 - u) * (1 - v) + g(i + 1, j) * u * (1 - v) + g(i, j + 1) * (1 - u) * v + g(i + 1, j + 1) * u * v;
}
function hRaw(x, y) { return bil(D.hn, x, y) * HS; }
// a little fine relief so it reads as rock, strongest on steep ground
function hAt(x, y) {
  const e = 0.6, gx = (hRaw(x + e, y) - hRaw(x - e, y)) / (2 * e), gy = (hRaw(x, y + e) - hRaw(x, y - e)) / (2 * e), s = Math.hypot(gx, gy);
  const k = sstep(0.25, 1.1, s), ux = s > 1e-4 ? -gy / s : 1, uy = s > 1e-4 ? gx / s : 0, across = x * ux + y * uy, along = (x * gx + y * gy) / (s || 1);
  const gul = (ridged(across * 0.18 + vn(x * 0.04, y * 0.04) * 2, along * 0.025, 3) - 0.4) * 2.4 * k;
  return hRaw(x, y) + gul + (ridged(x * 0.11 + 3, y * 0.11 + 7) - 0.35) * 0.9 * (1 - 0.6 * k) + (fbm(x * 0.35, y * 0.35, 3) - 0.5) * 0.5;
}
function vivid(c) { let [r, g, b] = c.map(v => v / 255); const mx = Math.max(r, g, b), mn = Math.min(r, g, b); let l = (mx + mn) / 2, sa = 0, h = 0, d = mx - mn;
  if (d > 1e-6) { sa = l > 0.5 ? d / (2 - mx - mn) : d / (mx + mn); h = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h /= 6; }
  sa = Math.min(1, sa * 1.5 + 0.08); l = Math.min(0.62, Math.max(0.42, l));
  const q = l < 0.5 ? l * (1 + sa) : l + sa - l * sa, p = 2 * l - q, f = t => { t = (t + 1) % 1; return t < 1 / 6 ? p + (q - p) * 6 * t : t < 0.5 ? q : t < 2 / 3 ? p + (q - p) * (2 / 3 - t) * 6 : p; };
  return [f(h + 1 / 3) * 255, f(h) * 255, f(h - 1 / 3) * 255]; }
const EN = D.notes.filter(n => n.col && n.e != null), EMOC = D.emo.map(e => vivid(e[1]));
const EF = { w: 96, h: 0, a: null };
function buildEmoField() { // per-emotion weight on a coarse grid
  EF.h = Math.round(EF.w * H / W); const K = D.emo.length, a = new Float32Array(EF.w * EF.h * (K + 2)), R = 26;
  for (let j = 0; j < EF.h; j++) for (let i = 0; i < EF.w; i++) { const x = i / (EF.w - 1) * W, y = j / (EF.h - 1) * H, ws = new Float32Array(K);
    EN.forEach(n => { const d2 = (n.x - x) ** 2 + (n.y - y) ** 2; ws[n.e] += Math.exp(-d2 / (2 * R * R)); });
    let tot = 0, p = 0; for (let k = 0; k < K; k++) { const v = ws[k] ** 2.2; a[(j * EF.w + i) * (K + 2) + k] = v; p += v; tot += ws[k]; }
    for (let k = 0; k < K; k++) a[(j * EF.w + i) * (K + 2) + k] /= (p || 1);
    a[(j * EF.w + i) * (K + 2) + K] = sstep(0.04, 0.5, tot);
    const ord = [...ws.keys()].sort((u, v) => ws[v] - ws[u]), k1 = ord[0], k2 = ord[1], s1 = ws[k1], s2 = ws[k2];
    const RANK = D.emo.map(e => /accept/i.test(e[0]) ? 0 : /indiff/i.test(e[0]) ? 1 : /distrust/i.test(e[0]) ? 2 : /aggress/i.test(e[0]) ? 3 : 4);
    a[(j * EF.w + i) * (K + 2) + K + 1] = (Math.abs(RANK[k1] - RANK[k2]) < 2 || RANK[k1] === 1 || RANK[k2] === 1 || s2 < 0.03) ? 0 : sstep(0.22, 0.42, s2 / (s1 + s2)); }
  EF.a = a; EF.K = K; }
function emoMix(x, y) { const K = EF.K, fx = Math.min(EF.w - 1.001, x / W * (EF.w - 1)), fy = Math.min(EF.h - 1.001, y / H * (EF.h - 1)), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j;
  const g = (ii, jj, k) => EF.a[(jj * EF.w + ii) * (K + 2) + k], b = (k) => g(i, j, k) * (1 - u) * (1 - v) + g(i + 1, j, k) * u * (1 - v) + g(i, j + 1, k) * (1 - u) * v + g(i + 1, j + 1, k) * u * v;
  let c = [0, 0, 0]; for (let k = 0; k < K; k++) { const w = b(k); c = [c[0] + EMOC[k][0] * w, c[1] + EMOC[k][1] * w, c[2] + EMOC[k][2] * w]; } return [c, b(K), b(K + 1)]; }
function emoAt(x, y) { return [bil(D.col, x, y, 3, 0), bil(D.col, x, y, 3, 1), bil(D.col, x, y, 3, 2)]; }

/* ---------- mesh ---------- */
const MX = 2 * VX - 1, MY = 2 * VY - 1;
const hGrid = new Float32Array(MX * MY);
let hMin = 1e9, hMax = -1e9;
for (let j = 0; j < MY; j++) for (let i = 0; i < MX; i++) { const h = hAt(i / (MX - 1) * W, j / (MY - 1) * H); hGrid[j * MX + i] = h; hMin = Math.min(hMin, h); hMax = Math.max(hMax, h); }
const BASE = hMin - 7;
function gH(x, y) { const fx = Math.max(0, Math.min(MX - 1.001, x / W * (MX - 1))), fy = Math.max(0, Math.min(MY - 1.001, y / H * (MY - 1))), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j;
  const g = (a, b) => hGrid[b * MX + a]; return g(i, j) * (1 - u) * (1 - v) + g(i + 1, j) * u * (1 - v) + g(i, j + 1) * (1 - u) * v + g(i + 1, j + 1) * u * v; }

/* ---------- substrate texture ---------- */
const TW = 2048, TH = Math.round(2048 * H / W);
const tcv = document.createElement('canvas'); tcv.width = TW; tcv.height = TH;
const tctx = tcv.getContext('2d');
function buildTexture() {
  const img = tctx.createImageData(TW, TH), px = img.data;
  const GR = [98, 108, 62], GR2 = [140, 134, 86], SO = [124, 96, 66], SO2 = [86, 68, 50], RK = [122, 118, 112], RK2 = [168, 160, 148];
  for (let py = 0; py < TH; py++) for (let pxx = 0; pxx < TW; pxx++) {
    const x = pxx / (TW - 1) * W, y = py / (TH - 1) * H, e = W / TW * 1.5;
    const h = gH(x, y), hx = gH(x + e, y) - gH(x - e, y), hy = gH(x, y + e) - gH(x, y - e), s = Math.hypot(hx, hy) / (2 * e);
    const lap = (gH(x + 3 * e, y) + gH(x - 3 * e, y) + gH(x, y + 3 * e) + gH(x, y - 3 * e) - 4 * h);
    const n1 = fbm(x * 0.08, y * 0.08, 4), n2 = vn(x * 1.7, y * 1.7), sp = hash(pxx, py);
    let c;
    if (STYLE === 'field') {
      const grass = mix(GR, GR2, sstep(0.35, 0.75, fbm(x * 0.05 + 9, y * 0.05, 4)));
      const soil = mix(SO, SO2, sstep(-0.2, -0.9, h / HS) * 0.8);
      let rock = mix(RK, RK2, n2 * 0.7); rock = rock.map(v => v * (0.92 + 0.08 * vn(x * 0.6, y * 0.6)));
      const tRock = sstep(0.55, 1.15, s + (n1 - 0.5) * 0.5), tSoil = sstep(0.25, 0.55, s + (n1 - 0.5) * 0.6) * (1 - tRock);
      c = mix(mix(grass, soil, tSoil + sstep(-0.4, -1.0, h / HS) * 0.5 * (1 - tRock)), rock, tRock);
      const k = 0.93 + 0.14 * sp; c = c.map(v => v * k);
    } else {
      c = [234, 230, 222]; const k = 0.96 + 0.06 * sp; c = c.map(v => v * k);
      if (sp > 0.965) c = mix(c, [70, 70, 70], 0.55 + 0.4 * (sp - 0.965) / 0.035);
    }
    // crease shading: hollows a touch darker, crests lighter
    const ao = Math.max(-0.28, Math.min(0.18, -lap * 0.11)); c = c.map(v => v * (1 + ao));
    // emotion wash
    const [em, st, gap] = emoMix(x, y);
    if (gap > 0.01) { const rk = STYLE === 'field' ? mix(RK, RK2, n2 * 0.7).map(v => v * (0.92 + 0.08 * vn(x * 0.6, y * 0.6)) * (1 + ao)) : [214, 210, 202].map(v => v * (0.96 + 0.06 * sp)); c = mix(c, rk, gap * 0.85); }
    const lum = q => 0.3 * q[0] + 0.59 * q[1] + 0.11 * q[2];
    const ls = lum(c), le = lum(em) || 1, tinted = em.map(v => Math.min(255, v * ls / le * 1.05));
    c = mix(c, tinted, ALPHA * st * (1 - gap));
    const o = (py * TW + pxx) * 4; px[o] = c[0]; px[o + 1] = c[1]; px[o + 2] = c[2]; px[o + 3] = 255;
  }
  tctx.putImageData(img, 0, 0);
}

/* ---------- three ---------- */
const stage = document.getElementById('stage');
const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(Math.min(2, window.devicePixelRatio));
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.3;
stage.appendChild(renderer.domElement);
const scene = new THREE.Scene(); scene.background = new THREE.Color('#ffffff');
const camera = new THREE.PerspectiveCamera(30, 1, 1, 5000);
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; controls.maxPolarAngle = Math.PI * 0.47; controls.minDistance = 120; controls.maxDistance = 1400;

scene.add(new THREE.HemisphereLight(0xffffff, 0x9a9384, 1.0));
const sun = new THREE.DirectionalLight(0xfff6ea, 3.3);
sun.position.set(-260, 260, -160); sun.castShadow = true;
sun.shadow.mapSize.set(4096, 4096); sun.shadow.bias = -0.0006; sun.shadow.normalBias = 0.6;
Object.assign(sun.shadow.camera, { left: -260, right: 260, top: 200, bottom: -200, near: 10, far: 900 });
scene.add(sun);
const fill = new THREE.DirectionalLight(0xffffff, 0.9); fill.position.set(120, 90, 400); scene.add(fill);

const X = x => x - W / 2, Z = y => y - H / 2;
// terrain
const geo = new THREE.PlaneGeometry(W, H, MX - 1, MY - 1); geo.rotateX(-Math.PI / 2);
const pos = geo.attributes.position;
for (let j = 0; j < MY; j++) for (let i = 0; i < MX; i++) pos.setY(j * MX + i, hGrid[j * MX + i]);
geo.computeVertexNormals();
const tex = new THREE.CanvasTexture(tcv); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
const terrMat = new THREE.MeshStandardMaterial({ map: tex, roughness: 0.95, metalness: 0 });
const terrain = new THREE.Mesh(geo, terrMat); terrain.castShadow = terrain.receiveShadow = true; scene.add(terrain);

// plinth walls that follow the edge, like a cut block
function wallStrip(pts) { // pts: [[x,y],...] along the edge
  const g = new THREE.BufferGeometry(), v = [], uv = [], idx = [];
  pts.forEach((p, k) => { const h = gH(p[0], p[1]); v.push(X(p[0]), h, Z(p[1]), X(p[0]), BASE, Z(p[1])); uv.push(k / (pts.length - 1), 1, k / (pts.length - 1), 0); });
  for (let k = 0; k < pts.length - 1; k++) { const a = 2 * k; idx.push(a, a + 1, a + 2, a + 2, a + 1, a + 3); }
  g.setAttribute('position', new THREE.Float32BufferAttribute(v, 3)); g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2)); g.setIndex(idx); g.computeVertexNormals(); return g;
}
const N = 300, edge = { s: [], n: [], w: [], e: [] };
for (let k = 0; k <= N; k++) { const t = k / N; edge.s.push([t * W, H]); edge.n.push([W - t * W, 0]); edge.w.push([0, t * H]); edge.e.push([W, H - t * H]); }
// strata texture for the cut faces
function strataTex(label) {
  const c = document.createElement('canvas'); c.width = 2048; c.height = 256; const x = c.getContext('2d');
  if (STYLE === 'field') { x.fillStyle = '#1e1d1b'; x.fillRect(0, 0, 2048, 256); for (let i = 0; i < 9000; i++) { x.fillStyle = `rgba(255,255,255,${Math.random() * 0.05})`; x.fillRect(Math.random() * 2048, Math.random() * 256, 2, 2); } }
  else { const bands = ['#8b6f4e', '#a1835f', '#6f5640', '#b49a76', '#7c624a', '#94785a']; let y0 = 0; while (y0 < 256) { const hgt = 8 + Math.random() * 26; x.fillStyle = bands[(Math.random() * bands.length) | 0]; x.fillRect(0, y0, 2048, hgt + 1); y0 += hgt; }
    for (let i = 0; i < 14000; i++) { x.fillStyle = `rgba(0,0,0,${Math.random() * 0.12})`; x.fillRect(Math.random() * 2048, Math.random() * 256, 2, 1); } }
  if (label) { x.font = 'bold 70px Questrial, Helvetica, Arial, sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillStyle = STYLE === 'field' ? 'rgba(255,255,255,.9)' : 'rgba(255,255,255,.95)'; x.fillText(label, 1024, 150); }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}
const walls = [];
function buildWalls() {
  walls.forEach(w => { scene.remove(w); w.material.map.dispose(); w.material.dispose(); }); walls.length = 0;
  [['s', '↓  HINDER'], ['n', '↑  HELP'], ['w', 'PRESENT'], ['e', 'FUTURE']].forEach(([k, lab]) => {
    const m = new THREE.Mesh(wallStrip(edge[k]), new THREE.MeshStandardMaterial({ map: strataTex(lab), roughness: 1, side: THREE.DoubleSide }));
    m.castShadow = m.receiveShadow = true; scene.add(m); walls.push(m);
  });
}
const slab = new THREE.Mesh(new THREE.BoxGeometry(W + 30, 4, H + 30), new THREE.MeshStandardMaterial({ color: 0xeeeeec, roughness: 0.9 }));
slab.position.y = BASE - 2; slab.receiveShadow = true; scene.add(slab);
const bottom = new THREE.Mesh(new THREE.PlaneGeometry(W, H), new THREE.MeshStandardMaterial({ color: 0x222222 })); bottom.rotateX(Math.PI / 2); bottom.position.y = BASE + 0.01; scene.add(bottom);

/* ---------- data layer ---------- */
const labels = document.getElementById('labels'), data = new THREE.Group(); scene.add(data);
const L = []; // {el, v:Vector3, grp}
function addLabel(text, cls, x, y, lift, grp) { const el = document.createElement('div'); el.className = 'lb ' + cls; el.textContent = text; labels.appendChild(el); L.push({ el, v: new THREE.Vector3(X(x), gH(x, y) + lift, Z(y)), grp }); return el; }
const G = { notes: new THREE.Group(), qs: new THREE.Group(), ways: new THREE.Group() }; Object.values(G).forEach(g => data.add(g));
const blk = new THREE.MeshStandardMaterial({ color: 0x111111, roughness: 0.6 });
D.notes.forEach(n => {
  const h = gH(n.x, n.y), st = new THREE.Mesh(new THREE.CylinderGeometry(0.45, 0.45, 11, 6), blk); st.position.set(X(n.x), h + 5.5, Z(n.y)); st.castShadow = true; G.notes.add(st);
  const hd = new THREE.Mesh(new THREE.SphereGeometry(3.3, 20, 14), new THREE.MeshStandardMaterial({ color: n.col ? new THREE.Color(`rgb(${n.col.join(',')})`) : 0xffffff, roughness: 0.5 }));
  hd.position.set(X(n.x), h + 12, Z(n.y)); hd.castShadow = true; G.notes.add(hd);
  addLabel('N' + n.k, 'nl', n.x, n.y, 12, 'notes');
});
D.qpos.forEach(Q => { if (!Q) return; const h = gH(Q.x, Q.y), st = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 0.6, 20, 6), blk); st.position.set(X(Q.x), h + 10, Z(Q.y)); st.castShadow = true; G.qs.add(st); addLabel('Q.' + Q.q, 'ql', Q.x, Q.y, 21, 'qs'); });
// start and goal
{ const s = D.START, h = gH(s.x, s.y); const p = new THREE.Mesh(new THREE.CylinderGeometry(0.7, 0.7, 26, 6), blk); p.position.set(X(s.x), h + 13, Z(s.y)); p.castShadow = true; data.add(p);
  const f = new THREE.Mesh(new THREE.BoxGeometry(0.6, 9, 14), new THREE.MeshStandardMaterial({ color: 0x111111 })); f.position.set(X(s.x), h + 21.5, Z(s.y) + 7); data.add(f); addLabel('PRESENT', 'pl', s.x, s.y, 29, null); }
function ringAt(cx, cy, r) { const pts = []; for (let k = 0; k <= 64; k++) { const a = k / 64 * Math.PI * 2, x = cx + Math.cos(a) * r, y = cy + Math.sin(a) * r; pts.push(new THREE.Vector3(X(x), gH(x, y) + 0.5, Z(y))); } return pts; }
[24, 15, 6].forEach(r => { const c = new THREE.CatmullRomCurve3(ringAt(D.GOAL.x, D.GOAL.y, r), true); data.add(new THREE.Mesh(new THREE.TubeGeometry(c, 80, 1.1, 6, true), new THREE.MeshStandardMaterial({ color: 0xffffff }))); data.add(new THREE.Mesh(new THREE.TubeGeometry(c, 80, 0.6, 6, true), blk)); });
addLabel('GOAL', 'pl', D.GOAL.x, D.GOAL.y, 20, null);
{ const g = D.GOAL, hh = gH(g.x, g.y); const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.7, 0.7, 18, 6), blk); pole.position.set(X(g.x), hh + 9, Z(g.y)); data.add(pole); const st = new THREE.Mesh(new THREE.OctahedronGeometry(4.5), new THREE.MeshStandardMaterial({ color: 0x111111 })); st.position.set(X(g.x), hh + 19, Z(g.y)); st.castShadow = true; data.add(st); }
{ const el = addLabel('↑ HELP', 'side', W / 2, 0, 0, null); let nm = -1e9; for (let k = 0; k <= 100; k++) nm = Math.max(nm, gH(k / 100 * W, 0)); L[L.length - 1].v.set(X(-8), gH(0, 2) + 6, Z(2)); }
// ways
const RC = { A: '#111111', B: '#1450ff', C: '#d6007a' }, wayMesh = {};
D.routes.forEach((R, ri) => {
  const pts = R.pts.filter((p, k) => k % 2 === 0 || k === R.pts.length - 1).map(p => new THREE.Vector3(X(p[0]), gH(p[0], p[1]) + 1.4, Z(p[1])));
  const c = new THREE.CatmullRomCurve3(pts), grp = new THREE.Group();
  grp.add(new THREE.Mesh(new THREE.TubeGeometry(c, 900, 1.5, 8), new THREE.MeshStandardMaterial({ color: RC[R.key], roughness: 0.45, emissive: RC[R.key], emissiveIntensity: R.key==='A'?0:0.25 })));
  grp.children.forEach(m => m.castShadow = true); G.ways.add(grp); wayMesh[R.key] = grp;
  [0.25, 0.6].forEach(f => { const p = R.pts[Math.floor(R.pts.length * (f + ri * 0.07))]; const el = addLabel(R.key, 'wl', p[0], p[1], 4, 'ways'); el.style.background = RC[R.key]; L[L.length - 1].way = R.key; });
});

/* ---------- layout / render ---------- */
function size() { const w = stage.clientWidth, h = stage.clientHeight; renderer.setSize(w, h); camera.aspect = w / h; camera.updateProjectionMatrix(); }
function home() { camera.position.set(0, 290, 330); controls.target.set(0, -18, 14); controls.update(); }
window.addEventListener('resize', size);
const v = new THREE.Vector3();
function place() {
  const w = stage.clientWidth, h = stage.clientHeight;
  L.forEach(o => { if (o.grp && !G[o.grp].visible) { o.el.style.display = 'none'; return; }
    if (o.way && wayMesh[o.way] && !wayMesh[o.way].visible) { o.el.style.display = 'none'; return; }
    v.copy(o.v).project(camera); if (v.z > 1) { o.el.style.display = 'none'; return; }
    o.el.style.display = ''; o.el.style.transform = `translate(${(v.x * 0.5 + 0.5) * w}px,${(-v.y * 0.5 + 0.5) * h}px)`; });
}
function loop() { controls.update(); renderer.render(scene, camera); place(); requestAnimationFrame(loop); }

/* ---------- UI ---------- */
function rebuild() { buildTexture(); tex.needsUpdate = true; buildWalls(); slab.material.color.set(STYLE === 'field' ? 0xeeeeec : 0xf4f2ee); }
document.querySelectorAll('[data-style]').forEach(b => b.onclick = () => { STYLE = b.dataset.style; document.querySelectorAll('[data-style]').forEach(x => x.classList.toggle('on', x === b)); rebuild(); });
const al = document.getElementById('alpha'), alv = document.getElementById('alv');
al.oninput = () => { alv.textContent = al.value + '%'; }; al.onchange = () => { ALPHA = al.value / 100; buildTexture(); tex.needsUpdate = true; };
['notes', 'qs', 'ways'].forEach(k => { const c = document.getElementById('t_' + k); c.onchange = () => { G[k].visible = c.checked; }; });
const wb = document.getElementById('waybtns');
if (D.routes.length > 1) { const mk = (key, txt) => { const b = document.createElement('button'); b.textContent = txt; if (key) b.style.borderColor = RC[key]; b.onclick = () => { Object.keys(wayMesh).forEach(k => wayMesh[k].visible = !key || k === key); wb.querySelectorAll('button').forEach(x => x.classList.toggle('on', x === b)); }; if (!key) b.classList.add('on'); wb.appendChild(b); };
  mk(null, 'All ways'); D.routes.forEach(R => mk(R.key, R.key + ': ' + (/firm/.test(R.name) ? 'firm ground only' : /support/.test(R.name) ? 'from the support' : 'through its notes'))); }
document.getElementById('home').onclick = home;
const lg = document.getElementById('emokey'); D.emo.forEach(e => { const s = document.createElement('span'); s.innerHTML = `<i style="background:rgb(${e[1].join(',')})"></i>${e[0]}`; lg.appendChild(s); });

const qs = new URLSearchParams(location.search); if (qs.get('style')) { STYLE = qs.get('style'); document.querySelectorAll('[data-style]').forEach(x => x.classList.toggle('on', x.dataset.style === STYLE)); }
if (qs.get('alpha')) { ALPHA = +qs.get('alpha') / 100; al.value = qs.get('alpha'); alv.textContent = qs.get('alpha') + '%'; }
buildEmoField(); size(); rebuild(); home(); loop(); window.__ready = true;
