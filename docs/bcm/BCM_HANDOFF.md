# BCM_HANDOFF.md
2026-11-17 (end of day) · Preview at **v196** (his wording review applied) · `/gsmlive` is defunct (his word, 11-17); the BCM page is `operationalcoherence.com/bcm`

## Start here
- Repo `operationalcoherence/BCM` (public; attach with push to publish). `main` feeds the preview page through GitHub Pages.
- **Build:** edit `gsm-readable.js` (the source) → `npx esbuild@0.24 gsm-readable.js --minify --outfile=gsm-preview.js`. 3D: `tools/relief/relief.js` + three@0.187.0 → `npx esbuild tools/relief/relief.js --bundle --minify --format=iife --outfile=gsm-relief.js` (install three and esbuild in a scratch dir and point NODE_PATH at it). Relief edits are made directly in `relief.js`; there is no patch script for it.
- Each version = one patch script in `tools/patches/` (it must reproduce the source exactly) + `docs/vNNN_update.md`. Bump the label (`t.textContent = "vNNN"`).
- **Test every version:**
  - `tests/matrix.py` on his workbooks plus `mkwb.py`'s synthetic ones (always the clinic one);
  - with the 3D loaded: Playwright with `--use-angle=swiftshader`, serving `gsm-relief.js`, scroll the cards into view (matrix blocks 3D and cannot see card failures — v174 lesson);
  - `grep -c 'AAPK\|AIza'` = 0.
- His workbooks: `bear-canyon-workbook-2026-11-13.json` (line map, 31 notes) and `…-11-05.json` (Broadview, place map, 14 notes). They are not in the repo. They are saved in the Claude project as `workbooks/bear-canyon-workbook-2026-11-13.json` and `workbooks/bear-canyon-workbook-2026-11-05.json` (see `workbooks/README.md`): read them with the project tool, don't ask him. Test every version on BOTH (11-13 first). He asked for this.
- Esri and AWS tiles can't be reached from the sandbox. Test with stand-in tiles served by Playwright (imagery, reference layers, and Terrarium elevation PNGs), and ask him to check the real ones on the preview.
- Project memory: `docs/bcm/` (ARCHITECTURE, CURRENT_STATE, TASK_QUEUE, CONCEPT_REGISTRY, this file).
- The Claude project was cleared out on 11-17. It now holds only `workbooks/`, a private `archive/` of 18 design notes (they quote his workbook, so they're kept out of this public repo) and `claude/layers_tracker.md`. See the project's `README.md`.
- **The preview page is public.** `operationalcoherence.com/bcm` loads `gsm-preview.js` from `main`, so every push is live for visitors within minutes (archive/deploy_problem_2026_11_11.md). "Preview only" means: never touch anything else.

## Standing rules (his)
Preview only. American spelling. "Emotion", never "feeling". "The method" = the whole BCM. The Q.1–Q.4 / Q.5–Q.7 grouping is silent on screen. Changes go in the engine for everyone, never tied to his workbook. Never merge words unless he says (THE SAME THING? asks). Flag Claude's wording; show redlines for his text and wait. Send files one per message. Serial comma everywhere (11-17). Story over list; tell people what they don't already know.

## Architecture in one breath
One IIFE engine (~20k lines) plus an appended terrain module. The module's `mount(host, data)` has modes: Synthesis (default), `card` (Taking Action), `an` (Pattern Analysis, with question buttons and WHAT THIS SUGGESTS), `an`+`par` (In Parallel, with question spokes, numbers and WHERE THE TWO PICTURES MEET). The 3D relief (`window.gsmRelief.mount`) replaces the canvas when WebGL is available. The canvas is the fallback only (v184).
Word engine:
- saturation filter (`window.gsmMED`, v172) and same-meaning asks (`asks["same|a|b"]`, v173);
- story generator SY() (v173);
- action grid (`window.gsmGridPts`, v179/v184) feeds Taking Action's MOVES, IN ORDER (v181);
- route stats: effort, impact, benefit, return (v177); friction, boomerang risk, rock faces (v192); hysteresis weights (v193);
- voice weighting in the ground (v183).
Place maps (v186/v189):
- `gsmData()` projects place notes into the 340×230 frame when no line note has text;
- the relief drapes Esri imagery, roads and names over the real terrain (AWS Terrain Tiles, true to scale; `gsmRelief.prep` loads it before the scene is built);
- emotion is color only on a place. "High/low ground" and "climbs" in the readings mean the emotion ground: keep that wording (his call, 11-17).
Since v185:
- card full screen has the Synthesis legend drawer (v185);
- T5 boxes (v187), glossary popovers (v188), Open workbook from every tab (v190);
- coworking schema: sv, wid, mt, gone, eh, acts, remap (v191–v194);
- WORDS THAT MAKE THE WORLD (v195).

## What happened this session (11-17, afternoon)
No code. Docs and planning only.
- His two workbooks were saved to the Claude project (`workbooks/`), so sessions stop asking for them.
- F8 was planned with him. There is a design-canvas mockup with four boards: the opening page, project setup, the invited person's view and the lead's dashboard. All of its wording is Claude's and not yet approved. He then chose:
  - an **Other** voice that people write in;
  - an every-workbook list "like Google Forms";
  - **Combine workbooks** as one of the three choices on the opening page;
  - **live** collection, with no sending of files.
- He read a costs write-up and picked **Firebase on the free Spark plan**. He set up the Firebase project himself, with Claude walking him through it (details in ARCHITECTURE §12a). It is locked and costs $0.
- The plan was written into ARCHITECTURE §12a; TASK_QUEUE and CURRENT_STATE now point to it.
- He asked whether to build F8 now. Claude advised **not yet**: F8 stays last, after his pass on the preview and after A1. The reasons: the dashboard reuses the v185–v195 readings, A1's cross-question threads feed WHERE THEY AGREE / SPLIT, and F8 holds other people's data. He hasn't answered yet. Ask him which order he wants.

## Open work, in order (Claude's recommendation; confirm with him)
1. Whatever he raises after his pass on the preview (v185–v195).
2. A1 engine side: threads that cross question boundaries.
3. F1/F2: the fuller per-instance Esri map with topological anchoring (to discuss with him first).
4. **F8, project lead dashboards: LAST. Remind Gregory when it's next.** The full plan is in BCM_ARCHITECTURE.md §12a. Estimate: 6–9 versions. If he wants to start early, the one safe first step is the Firestore security rules tested with fake people, which touches nothing on the preview. Build order after that: the privacy page and the rules, then live saving with Pause sharing, then the dashboard.
   - Firebase: project "The Bear Canyon Method", Spark plan ($0), Firestore nam5, rules locked, web app "BCM Preview", Google sign-in on. **Never upgrade it to Blaze without asking him.**
   - **Never put the Firebase web config or its key in chat, docs, memory or the repo.** He holds it. At build time, change the AIza check to allow exactly that one key.
   - Use test data only until there is a privacy page.

## Waiting on Gregory
- U5 instruction redlines (`docs/v173_update.md`, bottom).
- D8: voice weighting on by default, or a switch?
- D1/F1/F2: the discussion about the fuller per-instance 3D Esri map.
- His pass on Claude's wording, v171 to v195, is done and shipped as v196. Still open from it: rows 34 and 35 (In Parallel), and row 30, the action grid, which needs a redesign. It should come before Taking Action and draw on Analysis and Synthesis. Offer 2–3 designs before building (docs/v196_update.md).
- Real-tile check on the preview: Broadview imagery and terrain (v186/v189).
- F8 open calls (ARCHITECTURE §12a): who may lead a project; how long answers are kept and who can delete them; whether the file route stays; which account owns Firebase long term. Also the wording on the mockup and in the costs doc.
- Small calls: friction and hysteresis weights (v192/v193); a coworker's deletions of his notes and answers on Combine (v191); Combine and PDF for WHAT YOU DID (v194).

Reminder (his request, 11-17): F8 (project lead dashboards) is saved for the end. F4, F6 and F7 are done (v193–v195), so remind him F8 is the last item left.

## Links
- F8 mockup (design canvas): https://claude.ai/artifact/Dqy6xjxr4wPyGpKAf6hn4T
- F8 costs write-up: https://claude.ai/artifact/4QdCsBzitJneX76CDjHuiL
