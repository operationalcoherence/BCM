# BCM_HANDOFF.md

2026-11-18, evening. Preview at **v219** (v197–v219 all pushed 11-18). The BCM page is operationalcoherence.com/bcm (/gsmlive is defunct). The work queue is his v196 review, analyzed in claude/v196_review_plan.md in the Claude project (private, because it quotes his workbook). Version-by-version detail is in docs/bcm/BCM_CURRENT_STATE.md and docs/vNNN_update.md.

## First thing next session
1. Attach operationalcoherence/BCM with push. If it's refused, tell him plainly and stop; don't work around it. (A read-only clone of the public repo is fine for reading code.) On 11-18 the first attempt was refused; it worked after he said "push access granted."
2. Pick up at **Phase 2 step 8, Taking Action** (below). The review plan's section E holds calls already made; don't re-ask them. He does not want lists of questions: make the call, say which, and let him redirect.
3. When he reports something already fixed, check which version his page shows first (the label is at the bottom of the page). GitHub Pages can serve the previous build for up to ~10 minutes after a push; on 11-18 his 14:52 screenshots were v214 after v215 had deployed.

## Where the review plan stands
- **Phase 1** (v197–v203): done.
- **Phase 2:**
  - Step 6 (Pattern Analysis reordered): done (v205–v207, v211 for 3d).
  - Step 7 (Pattern Synthesis reordered): done (v212, v217, v218).
  - Step 10 (In Parallel): done (v213–v216, v219; details below).
  - **Next: step 8, Taking Action.** Group strategies and programs together; show the chart openly; one references list; each text field says in one line what it does, and what's written there goes somewhere (proposal: a named constraint shows on that note's card and in WHAT YOU DID, with a one-tap offer to add it to Q.4, Q.6, or Q.7); the poetic pass on THE WAY FORWARD comes in Phase 3.
  - Then step 9, Mapping Context: instructions in a drop-down, emotion definitions where notes are written (2g; approved quotes in claude/emotion_definitions_draft.md), the Start here text moved to its pages (his redlines, items marked R, still pending).
- **Phase 3:** a WebM download of the tour; tour captions from his confirmed meanings of the four acts; 3g, YOUR OWN WORDS as a strip (Q.1 to Q.7, key phrases under each); the word-budget ("poetic") pass with every cut shown to him first; 3c, the "no questions" click on the map.

## What 11-18 built (v210–v219)
- **The tour (v210, v219).**
  - Play opens full screen. A big Play/Pause button sits at the bottom center, with End tour beside it.
  - Captions are 17 px with 20 px titles, held by reading time (the Synthesis tour runs about 1.5 min on 11-18).
  - It opens with READING THE GROUND: what color and height mean, what a move costs, which moves are feasible now, and bare rock.
  - Bare rock has its own reading (`rockFaces()` replicates the relief's rock rule in the engine).
  - Pattern Analysis has its own short "how to read this map" tour (`introStops(true)`); his question was answered as "two tours, different jobs."
  - v219: no paper citation in either tour.
- **WHAT IT PRODUCED (v211):** bigger themes from repeated phrases that share notes; no lone words; leads into YOUR LANDSCAPE.
- **Pattern Synthesis (v212, v217, v218):**
  - A patterns row sits above the map (Synthesis only), and full screen carries it into the map.
  - The Supports questions appear only under PATTERNS.
  - Matching words are in bold; findings with no note link back to their answers.
- **In Parallel (v213–v216, v219).** The tab is THE TWO PICTURES, SIDE BY SIDE, drawn with lines:
  - The left column holds Analysis's words. Box styles: black = contested, dashed = a gap, teal = unused support, grey = designed without a cause.
  - Each word has a line to every note that carries it: solid black where the ground agrees, dashed red where it asks.
  - The ground is painted by the relief's own rule.
  - Tapping a word reads it and draws its lines on the Synthesis 3D.
  - Full screen opens with a HOW TO READ IT panel.
  - Under the figure: Where to start, then MORE FROM BOTH PICTURES (closed), then THE EARLIER 3D VIEW (closed).
  - Line maps only; on place maps (Broadview) the figure doesn't show and the agree/differ text stays.
  - Code: `gsmAgreeFig()` (built in the In Parallel IIFE from the lists p/g/m/v/y/w), `gsmIntOrder()`, relief `hoses()`/`hoseCount()`, `window.gsmSynRel`/`gsmSynHost`/`gsmSynPend`.
- **The action grid is deleted** (v215, his call). MOVES, IN ORDER now says "easy to take, on ground that already holds," using each note's ease from gsmDerive. Nothing is drawn from it.
- **Bugs fixed on the way:**
  - Escape in full screen left the button saying "Close full screen" and threw an error; the engine's `.pnet.fs` handler now skips `.grel`.
  - Off-frame labels piled up at the edges of the 3D; they're hidden now.
  - The patterns row leaked onto the Analysis map, where it did nothing (v217).

## Open calls for him (raise one only when the work reaches it; never as a list)
- Does the tour's feasibility sentence say what he means? ("From acceptance and indifference, change can start now; from distrust, aggression, and defiance, it is unlikely in the short or medium term.")
- Are tours of about 1.5 minutes all right?
- The figure's word labels and WHAT IT MIGHT MEAN still show lone words where the workbook repeats no phrase ("tradition", "reduce"). Quote the shortest note instead, as v211 does?
- Social media is a strategy but ranks 5th, so it's hidden (v202).
- Way A's zigzag across the line on strategy cards (v203) is still open.
- Older, still waiting:
  - His redlines on his own text in the review (items marked R) and the U5 instruction redlines (docs/v173_update.md, bottom).
  - D8: voice weighting on by default, or a switch? Also D1/F1/F2, and review rows 34 and 35.
  - The real-tile check on the preview.
  - F8's open calls.
  - Small calls: friction and hysteresis weights (v192/v193); a coworker's deletions on Combine (v191); Combine and PDF for WHAT YOU DID (v194).

## Standing rules (his)
- Preview only: never touch anything else. The preview page is public; every push is live within minutes.
- American spelling; serial comma everywhere. "Emotion", never "feeling". "The method" = the whole BCM.
- Q.1–Q.4 are grasping context; Q.5–Q.7 are designing for the context grasped. On screen, say "the context you have grasped" and "what you would design" rather than leaving question numbers bare.
- Changes go in the engine for everyone, never tied to his workbook.
- Never merge words unless he says (THE SAME THING? asks).
- Flag Claude's wording; show redlines for his text and wait.
- Story over list; tell people what they don't already know. Send files one per message.
- Don't ask long lists of questions: decide, say which, let him redirect.
- **No action grid anywhere in the project** (11-18 14:30: "I don't want the grid anywhere near this project"). Don't propose, mock up, or reintroduce it, including its Act Here / Act Anywhere or reach language.
- **Tour captions never cite the paper** (11-18 15:21). Page text keeps its citations.
- Don't frame anything in the method as context-free versus context-sensitive, or as bounded applicability (Snowden and Juarrero's terms); the method stands in its own terms.
- Never rely on hover alone to carry meaning (v207).

## How to build and test
- **Repo:** operationalcoherence/BCM (public). main feeds the preview through GitHub Pages; the page loads gsm-preview.js and gsm-relief.js with a per-minute cache-buster.
- **Engine:** edit gsm-readable.js, then `esbuild@0.24 gsm-readable.js --minify --outfile=gsm-preview.js`.
- **3D:** tools/relief/relief.js plus three@0.187.0, then `esbuild tools/relief/relief.js --bundle --minify --format=iife --outfile=gsm-relief.js`. Install three and esbuild in a scratch directory and point NODE_PATH at it. Both builds reproduce byte for byte from source.
- **Each version** = one patch script in tools/patches/ (engine edits; relief edits behind `--relief`) + docs/vNNN_update.md + the label bump (`t.textContent = "vNNN"`). The patch scripts reproduce the source exactly.
  - To rebuild from scratch, restore gsm-readable.js and tools/relief/relief.js from v209 (commit 3a00154) and run v210 → v219 in order, each on the relief with `--relief` and then on the engine.
  - Restoring with `git checkout <commit> -- files` stages them. Before any `git checkout -- .`, run `git checkout HEAD -- <files>` to get back to the committed state.
- **His workbooks** are in the Claude project:
  - workbooks/bear-canyon-workbook-2026-11-18.json: line map, 35 notes; test it first. N32–N35 are aggression he placed on the help side on purpose.
  - workbooks/bear-canyon-workbook-2026-11-13.json: line map, 31 notes.
  - workbooks/bear-canyon-workbook-2026-11-05.json: Broadview, a place map, 14 notes.

  Read them with the project tool; don't ask him.
  - Local copies: tests/w18.json is 11-18 without its edit log; tests/real.json (11-13) is derived from it (first 31 notes, N26 back to Q.2, resp|nnujara dropped); tests/broadview.json.
  - Keep all of them, and mkwb's tests/wb_*.json, out of git via .git/info/exclude; the repo is public.
- **Tests, every version:**
  - tests/matrix.py on his workbooks plus every mkwb workbook (always the clinic one).
  - With the 3D loaded: tests/relief_text.py, tests/tour.py, tests/tour_an.py, tests/agree.py, tests/waymoves.py, tests/derive.py, as the change needs. Matrix blocks the 3D and can't see card failures.
  - Look at the 3D with Playwright screenshots, using `--use-angle=swiftshader --enable-unsafe-swiftshader`. Cards and the Synthesis 3D mount only when scrolled into view.
  - `grep -c 'AAPK\|AIza'` = 0 on both built files.
  - Esri and AWS tiles can't be reached from the sandbox; ask him to check the real ones on the preview.
- **Template note (v217):** the terrain module's markup is shared by the Analysis map, the Synthesis map, In Parallel's earlier 3D, and the cards. Anything added to it shows on all of them unless gated on ANH / PAR / CARDH; check each tab after a change there.
- **Several terrain modules** sit in the page at once (one per tab). In tests, scope selectors to the visible one (`.closest('.gterr')`), or a hidden module's element answers instead.

## Architecture in one breath
- One IIFE engine (~22k lines) plus an appended terrain module. The module's mount(host, data) has modes: Synthesis (default), card (Taking Action), an (Pattern Analysis), and an+par (In Parallel's earlier 3D). The 3D relief (window.gsmRelief.mount) replaces the canvas when WebGL is available; the canvas is the fallback.
- Terrain coordinates are the line map's: 340 × 230; the help and hinder line is y = 118; START (10, 118), GOAL (305, 118).
- Ways on cards: buildCourse() makes ROUTES (A through its notes, B firm ground only, C from the support); routeStats() gives effort, impact, benefit, friction, boomerang risk, and rock faces.
- gsmDerive() recomputes derived state on every pass (v199).
- The phrase layer: phBest, phClause, phCentral, gsmPhName, gsmPhNameH, gsmPhTitle, gsmPurpose, all inside phKeep so the word tallies don't move.
- Engine note ids are "note N"; on screen they're "N3".
- Watch for a local `var P = []` shadowing the save function near the THE SAME THING? code (v205 bug).
- NO RESPONSE YET = window.gsmNR. The constraint textareas save to asks["cons|id"], but nothing reads them yet (step 8 fixes this).

## Project memory
- In the repo, docs/bcm/: this file, BCM_CURRENT_STATE.md, BCM_ARCHITECTURE.md (Rev 9, through v206; needs v207–v219 added), TASK_QUEUE, CONCEPT_REGISTRY.
- In the Claude project:
  - workbooks/ and a private archive/ (design notes that quote his workbook).
  - claude/v196_review_plan.md (the queue) and claude/in_parallel_figure.md (the figure and his calls on it).
  - claude/emotion_definitions_draft.md (approved quotes), claude/layers_tracker.md, claude/README.md.
  - papers/Vigneaux_2026_JEM_paper.md: the FULL TEXT of his paper. Read it there for every emotion meaning and dynamic, and never ask him for the paper again.

## Later work, in order
1. The rest of the review plan (steps 8 and 9, then Phase 3).
2. Review rows 34 and 35.
3. A1, engine side: threads that cross question boundaries.
4. F1/F2: the fuller per-instance Esri map with topological anchoring (discuss with him first).
5. F8, project lead dashboards: LAST. Remind him it's the last item left.
   - The plan is in BCM_ARCHITECTURE.md §12a: 6–9 versions. Safe first step if he wants it early: Firestore security rules tested with fake people. Review row 33 (TWO PEOPLE, TWO SIDES) is for the dashboard.
   - Firebase: project "The Bear Canyon Method", Spark plan ($0), Firestore nam5, rules locked, web app "BCM Preview", Google sign-in on.
   - Never upgrade to Blaze without asking.
   - Never put the Firebase web config or key in chat, docs, memory, or the repo; at build time, allow exactly that one key in the AIza check.
   - Test data only until there is a privacy page.

Not yet done: docs/v193_update.md was never written (v193 is F6 hysteresis).

## Links
- The two-pictures canvas (mockups 1–3 and the chosen "lines" artboard): https://claude.ai/artifact/GfYmgywiBj3q7F7vKvgJR9
- Wording review sheet (done): https://claude.ai/artifact/KkdeKLx5E45pWKpYU1FE3V
- F8 mockup: https://claude.ai/artifact/Dqy6xjxr4wPyGpKAf6hn4T
- F8 costs write-up: https://claude.ai/artifact/4QdCsBzitJneX76CDjHuiL
