# BCM_HANDOFF.md

2026-11-18, night. Preview at **v228** (v197–v228 all pushed 11-18). The BCM page is operationalcoherence.com/bcm (/gsmlive is defunct). The work queue is his v196 review, analyzed in claude/v196_review_plan.md in the Claude project (private, because it quotes his workbook). Version-by-version detail is in docs/bcm/BCM_CURRENT_STATE.md and docs/vNNN_update.md.

## First thing next session
1. Attach operationalcoherence/BCM with push. If it's refused, tell him plainly and stop; don't work around it. (A read-only clone of the public repo is fine for reading code.) On 11-18 every first attempt was refused, and each time it worked after he said "push access granted."
2. **A short check of Taking Action only** (the agreed cadence after step 8). Read it on his 11-18 workbook. His redlines on v226's wording are listed at the end of docs/v226_update.md; raise them one at a time, only as the check reaches them.
3. Then **Phase 2 step 9, Mapping Context** (below).
4. When he reports something already fixed, check which version his page shows first (the label is at the bottom of the page). GitHub Pages can serve the previous build for up to ~10 minutes after a push.

## Review cadence (agreed 11-18 17:18)
- After step 8 (now): a short check of Taking Action only.
- Next full review: after Phase 3, before F8.
- One session per step, starting from this file.

## Where the review plan stands
- **Phase 1** (v197–v203): done.
- **Phase 2:**
  - Step 6 (Pattern Analysis reordered): done (v205–v207, v211).
  - Step 7 (Pattern Synthesis reordered): done (v212, v217, v218).
  - Step 10 (In Parallel): done (v213–v216, v219).
  - Interpretation pass: done for Analysis (v220–v222, v224) and In Parallel (v223, v225); keeps going as he asks.
  - **Step 8 (Taking Action): done, v226.**
  - **Next: step 9, Mapping Context.** Instructions in a drop-down; emotion definitions where notes are written (2g; approved quotes in claude/emotion_definitions_draft.md); the Start here text moved to its pages (his redlines, items marked R, still pending).
- **Phase 3:** a WebM download of the tour; tour captions from his confirmed meanings of the four acts; 3g, YOUR OWN WORDS as a strip; the word-budget ("poetic") pass with every cut shown to him first (THE WAY FORWARD on Taking Action first); 3c, the "no questions" click on the map.

## v227
The constraint buttons show grayed out before typing; each note on Mapping Landscape shows its constraint (`gsmNoteCons`). 

## v228
Taking Action in three layers (his yes, 21:37): a decision strip, then Why this action, then Evidence; `gsmTALayer()` in `gsmTAPass`. The strip reads `data-tv`/`data-ts`/`data-ws` on seeded cards. Tests that type into a card must open `.tawhy` and click `.tanb` first. Open: the 3D way readings (drawn after mount) stay in layer 2.

## What v226 built (Taking Action, step 8)
Built to BCM_ARCHITECTURE.md §0.3, the central test: "Does what you would design change the conditions and invite the transitions the goal needs?" Full detail is in docs/v226_update.md.
- **THE TEST** panel at the top. It shows a verdict for each of: what holds it, what already moves, where it can shift, where the reading splits, the constraints named, and the cheapest first move. WHAT EACH PART OF A CARD DOES sits under it, closed.
- **Seeded cards**, from `gsmStructSum.D` (gsmStructBuild now keeps its notes):
  - strategies: the system that holds, the key tension, the loop;
  - programs: the opportunity, what is already helping, support not yet reinforced.

  Each has its own test, THE WAY ACROSS (ridge before bare rock, cost words, behaviors first and emotions first, entrenched notes), its ways, and its constraint fields. Switch keys are `seed|sys` and so on.
- **Split readings** (`window.gsmSplit`, captured in In Parallel's builder) are placed on cards by `gsmTAPass()` as WHERE THE READING SPLITS.
- **Constraint loop:** the `cons|id` field gets one-tap buttons for Q.4, Q.6, and Q.7 (`gsmConsQ`, a `button[data-cq]` listener). WHAT YOU DID lists the constraints and saves them (`acts[].c`), and flags their notes. SINCE YOU ACTED shows them.
- **Grouping:** STRATEGIES, then PROGRAMS, each headed by its explanation. Seeded cards come first. Word-only cards fold under MORE … FROM THE WORDS YOU USE, unless the card has a decision, a WHAT YOU DID entry, a manual switch, or is the Where to start card. The chart is open.
- "Answers" uses the same rule as NOTHING YOU WOULD DO (`gsmNR` now exposes `rw`, `cm`, `ri`). "Builds on" uses the engine's unused-support terms (`ge[t].c === "unused"`), so the page agrees with Analysis.
- Tests: tests/ta_flow.py (new, the whole constraint loop), plus matrix, relief_text, and dump2. matrix.py and relief_text.py accept `GSMJS=<file>` to compare against an older build.

## Open calls for him (raise one only when the work reaches it; never as a list)
- The v226 wording (list at the end of docs/v226_update.md). Whether word-only cards should stay folded. Whether a word card that repeats a seeded card should merge into it.
- His redlines on claude/meaning_patterns_draft.md, claude/structure_pass_plan.md, and the v222–v225 wording.
- Rename THE EMOTION CHANGES to THE HIDDEN CHANNELS? (offered 11-18 19:14)
- The In Parallel figure's word labels still show lone words where the workbook repeats no phrase ("tradition", "reduce"). Quote the shortest note instead?
- Way A's zigzag on strategy cards (v203) is still open.
- Older, still waiting: his redlines on his own text (items marked R) and the U5 instruction redlines; D8 voice weighting; D1/F1/F2; review rows 34 and 35; the real-tile check; F8's open calls; small calls (v191–v194).

## Standing rules (his)
- Preview only: never touch anything else. The preview page is public; every push is live within minutes.
- American spelling; serial comma everywhere. "Emotion", never "feeling". "The method" = the whole BCM.
- Q.1–Q.4 are grasping context; Q.5–Q.7 are designing for the context grasped. On screen, say "the context you have grasped" and "what you would design" rather than bare question numbers.
- Changes go in the engine for everyone, never tied to his workbook.
- Never merge words unless he says (THE SAME THING? asks).
- Flag Claude's wording; show redlines for his text and wait.
- Story over list; tell people what they don't already know. Send files one per message.
- Don't ask long lists of questions: decide, say which, let him redirect.
- **No action grid anywhere in the project** (11-18 14:30), including its Act Here / Act Anywhere or reach language.
- **Tour captions never cite the paper** (11-18 15:21). Page text keeps its citations.
- Don't frame anything as context-free versus context-sensitive, or as bounded applicability (Snowden and Juarrero's terms).
- Never rely on hover alone to carry meaning (v207).
- Lead each tab with meaning; put the inventory under it, closed. Interpretation over inventory.
- Don't let a page grow long: v226 kept Taking Action near its old length by folding word-only cards.

## How to build and test
- **Repo:** operationalcoherence/BCM (public). main feeds the preview through GitHub Pages; the page loads gsm-preview.js and gsm-relief.js with a per-minute cache-buster.
- **Engine:** edit gsm-readable.js, then `esbuild@0.24 gsm-readable.js --minify --outfile=gsm-preview.js`.
- **3D:** tools/relief/relief.js plus three@0.187.0, then `esbuild tools/relief/relief.js --bundle --minify --format=iife --outfile=gsm-relief.js`. Install three and esbuild in a scratch directory and point NODE_PATH at it.
- **Each version** = one patch script in tools/patches/ + docs/vNNN_update.md + the label bump (`t.textContent = "vNNN"`). To rebuild from scratch, restore gsm-readable.js and tools/relief/relief.js from v209 (commit 3a00154) and run v210 → v228 in order (v220–v226 have no relief part). Before any `git checkout -- .`, run `git checkout HEAD -- <files>`.
- **His workbooks** are in the Claude project (workbooks/…-11-18.json line map, 35 notes, test it first; …-11-13.json; …-11-05.json Broadview place map). Read them with the project tool; don't ask him. Local copies tests/w18.json, tests/broadview.json, and mkwb's tests/wb_*.json stay out of git via .git/info/exclude (a fresh clone needs them written again). Run mkwb.py and matrix.py from inside tests/.
- **Tests, every version:** tests/matrix.py on his workbooks plus every mkwb workbook; tests/dump2.py to read a tab (closed details stay closed); tests/ta_flow.py for Taking Action; with the 3D loaded, relief_text.py, tour.py, tour_an.py, agree.py, waymoves.py, derive.py as the change needs; Playwright screenshots with `--use-angle=swiftshader --enable-unsafe-swiftshader`; `grep -c 'AAPK\|AIza'` = 0 on both built files. The story moves into place a moment after render, so wait ~3 s before reading or screenshotting it.
- **Template note (v217):** the terrain module's markup is shared by four views; gate anything new on ANH / PAR / CARDH.
- **Tabs in the DOM:** Analysis, Synthesis, and In Parallel share data-tab 2; tell them apart by `[data-pv]` (2 Analysis, 6 In Parallel, 4 Taking Action). `S()` assigns data-pv to Rt's children by the preceding `.part`, so new blocks must be Rt children in the right region (v226's groups are).

## Architecture in one breath
- One IIFE engine (~24k lines) plus an appended terrain module (modes: Synthesis, card, an, an+par). The 3D relief replaces the canvas when WebGL is available. Card maps mount when they scroll into view (IntersectionObserver), so folded cards mount when opened.
- Terrain coordinates: 340 × 230; help and hinder line y = 118; START (10, 118), GOAL (305, 118).
- Note arrays: [question kind, x, y, text, line, emotion (0 aggression, 1 acceptance, 2 distrust, 3 indifference, 4 defiance), source, voice, id, …]. In the builders, note items have id "note N" or "PN"; the page shows them as N1 links.
- Ways on cards: buildCourse() makes ROUTES A/B/C; routeStats() gives effort, impact, benefit, friction, boomerang risk, and rock faces. gsmDerive() recomputes derived state on every pass.
- The phrase layer: phBest, phClause, phCentral, gsmPhName, gsmPhNameH, gsmPhTitle, gsmPurpose, all inside phKeep.
- Watch for a local `var P = []` shadowing the save function near THE SAME THING? (v205 bug).
- NO RESPONSE YET = window.gsmNR. Constraint textareas save to asks["cons|id"], which Taking Action reads since v226.

## Project memory
- In the repo, docs/bcm/: this file, BCM_CURRENT_STATE.md, BCM_ARCHITECTURE.md (Rev 11; its §10 and §0b lines on constraints and split readings were corrected for v226), BCM_TASK_QUEUE.md, and BCM_CONCEPT_REGISTRY.md.
- In the Claude project: workbooks/, a private archive/, claude/v196_review_plan.md, claude/in_parallel_figure.md, claude/meaning_patterns_draft.md, claude/structure_pass_plan.md, claude/emotion_definitions_draft.md, claude/layers_tracker.md, claude/README.md, claude/BCM_HANDOFF.md (a copy of this file), and papers/Vigneaux_2026_JEM_paper.md (the FULL TEXT of his paper; read it there, never ask him for it).

## Later work, in order
1. Step 9, then Phase 3 (and more interpretation work as he asks).
2. Review rows 34 and 35.
3. A1, engine side: threads that cross question boundaries.
4. F1/F2: the fuller per-instance Esri map (discuss with him first).
5. F8, project lead dashboards: LAST. Remind him it's the last item left. Plan in BCM_ARCHITECTURE.md §12a. Firebase: "The Bear Canyon Method", Spark plan ($0), Firestore nam5, rules locked, web app "BCM Preview", Google sign-in on. Never upgrade to Blaze without asking. Never put the Firebase web config or key in chat, docs, memory, or the repo. Test data only until there is a privacy page.

Not yet done: docs/v193_update.md was never written (v193 is F6 hysteresis).

## Links
- The two-pictures canvas: https://claude.ai/artifact/GfYmgywiBj3q7F7vKvgJR9
- Wording review sheet (done): https://claude.ai/artifact/KkdeKLx5E45pWKpYU1FE3V
- F8 mockup: https://claude.ai/artifact/Dqy6xjxr4wPyGpKAf6hn4T
- F8 costs write-up: https://claude.ai/artifact/4QdCsBzitJneX76CDjHuiL
