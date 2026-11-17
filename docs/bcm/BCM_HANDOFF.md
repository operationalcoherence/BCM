# BCM_HANDOFF.md
2026-11-17 · Preview at **v193** · Live `/gsmlive` untouched (old v92; never touch without Gregory's go-ahead)

## Start here
- Repo `operationalcoherence/BCM` (public; attach with push to publish). `main` feeds the preview page through GitHub Pages.
- **Build:** edit `gsm-readable.js` (the source) → `npx esbuild@0.24 gsm-readable.js --minify --outfile=gsm-preview.js`. 3D: `tools/relief/relief.js` + three@0.187.0 → `npx esbuild tools/relief/relief.js --bundle --minify --format=iife --outfile=gsm-relief.js`.
- Each version = one patch script in `tools/patches/` (it must reproduce the source exactly) + `docs/vNNN_update.md`. Bump the label (`t.textContent = "vNNN"`).
- **Test every version:**
  - `tests/matrix.py` on his workbooks plus `mkwb.py`'s synthetic ones (always the clinic one);
  - with the 3D loaded: Playwright with `--use-angle=swiftshader`, serving `gsm-relief.js`, scroll the cards into view (matrix blocks 3D and cannot see card failures — v174 lesson);
  - `grep -c 'AAPK\|AIza'` = 0.
- His workbooks: `bear-canyon-workbook-2026-11-13.json` (line map, 31 notes) and `…-11-05.json` (Broadview, place map, 14 notes). Both are in this conversation's uploads, not the repo.
- Project memory: `docs/bcm/` (ARCHITECTURE, CURRENT_STATE, TASK_QUEUE, CONCEPT_REGISTRY, this file).

## Standing rules (his)
Preview only. American spelling. "Emotion", never "feeling". "The method" = the whole BCM. The Q.1–Q.4 / Q.5–Q.7 grouping is silent on screen. Changes go in the engine for everyone, never tied to his workbook. Never merge words unless he says (THE SAME THING? asks). Flag Claude's wording; show redlines for his text and wait. Send files one per message. Story over list; tell people what they don't already know.

## Architecture in one breath
One IIFE engine (~20k lines) plus an appended terrain module. The module's `mount(host, data)` has modes: Synthesis (default), `card` (Taking Action), `an` (Pattern Analysis, with question buttons and WHAT THIS SUGGESTS), `an`+`par` (In Parallel, with question spokes, numbers and WHERE THE TWO PICTURES MEET). The 3D relief (`window.gsmRelief.mount`) replaces the canvas when WebGL is available. The canvas is the fallback only (v184).
Word engine:
- saturation filter (`window.gsmMED`, v172) and same-meaning asks (`asks["same|a|b"]`, v173);
- story generator SY() (v173);
- action grid (`window.gsmGridPts`, v179/v184) feeds Taking Action's MOVES, IN ORDER (v181);
- route stats: effort, impact, benefit, return (v177);
- voice weighting in the ground (v183).

## Open work, in order
1. **Esri place map as ground (his question 3, 11-17; D1).** Not built. Today a place-map-only workbook (Broadview) gets no 3D at all, because the terrain module reads line-map notes only (`C.m`). Plan:
   - a `place` mode in the module: project `C.p.m` lat/lng into a local frame around the notes and the location;
   - texture the ground with Esri World Imagery (or topo) tiles plus a place-names reference layer;
   - lay the emotion color translucently on top; relief gentle or off (he said relief is not necessary);
   - pins, question flags at the centers of their notes, the goal at the location;
   - use it on Analysis, Synthesis and Taking Action;
   - place notes drawn as areas (row[4] polygons) as shaded patches.
   Risk: tile CORS and the key (`window.GSM_ESRI_KEY`, only on the Webador page) cannot be tested in the sandbox, so verify on the preview. The per-instance 3D map from Esri output with topological anchoring (F1/F2) is the later, larger version he wants to discuss.
2. T5: Taking Action asks "What constraint or rule keeps this note in the low ground, and how do we change it?" (Juarrero), tied to Q.4–Q.7.
3. A2: a coworking-ready schema. G1: a glossary popover for every term.
4. Priority 3 (F3–F8): friction field, reflexive loop, synthetic bridging, hysteresis, lexical world-making, dashboards.

## Waiting on Gregory
- U5 instruction redlines (`docs/v173_update.md`, bottom).
- D8: voice weighting on by default, or a switch?
- D1: the discussion about a per-instance 3D Esri map.
- His pass on all Claude wording (v171–v184 update docs).

Reminder (his request, 11-17): F8 (project administrator dashboards) is saved for the end. Remind Gregory when F4, F6 and F7 are done.
