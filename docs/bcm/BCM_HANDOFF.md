# BCM_HANDOFF.md

2026-11-25 21:50: **v292 live**: the A LOOP BETWEEN GROUPS and TWO WAYS OF RUNNING questions are restored (his "We just added these! Nooko", 21:41). v291 removed them by mistake. **The no-questions rule covers only questions that admit the engine can't tell; never remove a question he asked for, and ask before removing any question.** His redline answers now go in as v293.

2026-11-25 22:10: **v291 live**, third pass on Pattern Analysis and Taking Action (his go-ahead 21:22; docs/v291_update.md). Removed the one-tap questions that cover engine limits (Is it a theme?, Does it serve the goal?, the loop and two-ways questions); kept THE SAME THING? and DOES THIS ANSWER THE GOAL? (he renamed it 11-25; **asked him whether it goes too**). Single-word rule enforced in WHAT STANDS OUT (`uo`, `gsmOkW`), WHAT YOU WOULD DO, and `gsmThing` ("that" after a noun is not a determiner). One first move: no "Decide X first"; WHERE TO START copies THE CHEAPEST FIRST MOVE after the title rewrite. **Next:** his redline answers (claude/start_mapping_redlines_2026-11-25.md) as v293; the vague 11-13 title "Redesign “aggressive suppression” with those who oppose it" (vague_titles.py FAIL, present since before v290); "The whole workbook read as one story" fold still quotes notes and lists IDs against his story rule (decide: cut its opening paragraph, keep the sections). Full-text 11-20 copy: tests/w20full.json (excluded).

2026-11-25 21:20: **v290 live**, Start Here and the two Mapping pages tidied (his yes 19:34; docs/v290_update.md). Main fix: on Mapping Context questions 1 to 7 the goal's heading, its help, and WORKING WITH A FRIEND showed with no goal box under them. Also cut: the repeated save line and name help on Mapping Context, the dashed PLACE MAP box once the line map has notes; "homes" → "spots" in the place hint. **Waiting on him:** 11 redlines on his own text, claude/start_mapping_redlines_2026-11-25.md in the Claude project (R1 is the dashed-ring Thread line). Apply his answers as v293. **Next:** the third pass on Pattern Analysis and Taking Action (items below, under v289). New tool: tests/pagewalk.py. **Never commit tests/wb_both.json:** mkwb builds it from his workbooks; it was pushed by mistake, then scrubbed from history with his go-ahead (21:19; force-pushed with lease, content unchanged), and is now in .git/info/exclude. 11-13 and Broadview tested this session (tests/w13.json, tests/broadview.json, tests/real.json = 11-13, all excluded).

2026-11-25 19:35: **v289 live.** Tonight's work, his call 18:31: "start preparing the pages for market. Delete repeats, consolidate where possible, tidy up, make engine fixes, focus on UI." Context: he wants to move BCM to market; it stays free (the next product will be paid). Launch plan, two stages (solo version first, F8 second): the Docs artifact "BCM launch checklist", https://claude.ai/artifact/4WV5hB2nFq8LqCkkFzu9jx.
- **v285** each phrase once in the Q.5–Q.7 lists; RUNS TOGETHER never quotes the goal; "once" on card maps; no "dont fix" fragments; no preposition or generic-verb pairings in DOES THIS ANSWER THE GOAL? (docs/v285_update.md)
- **v286** repeats cut (his "Cut"): story opening vs AT A GLANCE, WHAT STILL STANDS IN THE WAY vs THE TEST, THE FIVE PAGES → THE PAGES (docs/v286_update.md)
- **v287** no single-word findings in the word overlaps, WHERE THESE MEET, POSSIBLE PATTERNS; WHERE THE CARDS MEET says a name once; **bug fixed:** DOES THIS SERVE THE GOAL? had an empty heading on Taking Action since v269 while its questions sat inside IN YOUR ANSWERS on Analysis; `gsmGoalQ` now moves them (docs/v287_update.md)
- **v288** his halfway measure on the one-word rule (his yes 19:19): `gsmThing` states a single word when it reads as a thing (after a/the/their…, ending the phrase), comes up in 2+ places, and is always shown with the user's own clause and where it is: **lease**: “A stable lease would let staff be hired” (N5) (docs/v288_update.md)
- **v289** a plural word after a preposition counts as a thing ("a threat to referrals"). **His rule (19:28): don't add one-tap questions just to cover the engine's limits: "it bothers the user with our shortcomings."** (docs/v289_update.md)

**Next (said to him, not started):** Start Here and the two Mapping pages. His text there goes to him as redlines, never edited directly. Already spotted: Start Here's Thread definition still mentions "a dashed ring on a dot" (the figure is gone); check the Mapping Landscape instruction line "Pattern Analysis opens once you have answered all seven questions" against the engine. Then a third pass on Pattern Analysis and Taking Action (still seen on 11-20: THE CHEAPEST FIRST MOVE's "Decide organizational transformation first" is vague; Legend/LEGEND doubled; POSSIBLE PATTERNS' meta lines like "“indifference” sits behind two findings" add little).
**Not tested this session:** 11-13 and Broadview (no local copies). Build tests/w13.json and tests/broadview.json from the project's workbooks/ first next time. Full-text 11-20 copy: tests/w20full.json (in .git/info/exclude).
**Push access:** the first add_repo was refused again tonight and worked after he said "push access granted". This session pushed from a clone at /home/claude/BCM.

2026-11-25 16:10: **v276 live**, WHO STANDS WHERE (groups across ground; docs/v276_update.md). Fires on his 11-20 workbook for leadership (the plan relies on the people it distrusts) and supporters (a loop of aggression). Test copies of his 11-20 and 11-13 workbooks with real note text: build them from the project's workbooks/ (keep out of git). **Next in his order:** Risk After the Goal (item 3), then the rest of Designer Is the Obstacle on Taking Action (item 4), Same Emotion, Different Targets (item 5).

2026-11-25 15:30: **v275 live**, Pattern Analysis says each thing once (his "fix all" 14:58 on claude/pattern_analysis_repeats_review_2026-11-25.md; docs/v275_update.md), plus three fixes. Test tool for a full read with every fold open and the 3D loaded: the dump in that update's checks (tests/dump2.py leaves <details> closed). **Next:** the next queue item (his call 14:59).

2026-11-24 21:15: **v267 live**, the Synthesis blocks rewritten as prose (his note 21:01, "the writing is really dry"; docs/v267_update.md). Change is in tools/graph/page.js. **Next:** his read.

2026-11-24 21:00: **v266 live**, the simple Pattern Synthesis page (docs/v266_update.md): WHAT CHANGED WHAT and the strongest shape at the top of Synthesis, from tools/graph/ (graph.js, shapes.js, page.js, pushed this session). **The build now bundles tools/graph/*.js ahead of the engine** (README). No question block (his call). **Next:** his eye on the wording; his call on emotion words as tags in the graph; then a real large workbook. Local tests/graph_wb/ (trimmed 11-20, Good fire, Broadview) is kept out of git.

2026-11-24 17:00: **v265 live**. Since v261: **v262** distance haze (line maps; a denser mesh was tried and dropped, no visible change and too heavy at 2x), **v263** a crisper crest along ridges, **v264** far note labels fade a little, **v265** the attribution lettered on the front face of the block (or the base when the face is low). **"NOW · the 3D visual" is done** except his two calls (the v255 lighting check, the color wash). **Next: his call (16:16): "can we switch focuses?"** Ask him what to work on next. Tools: tests/cardshot.py, tests/reliefshot.py. Local tests/w20.json and tests/broadview.json are trimmed copies, kept out of git.

2026-11-24 15:40: **v261 live**, ways laid on the ground (relief test strategy 5; docs/v261_update.md). Card-map ways are bands on the ground with a rim, flat arrowheads, and the hills' shadows; the walked leg is gold with a wide black rim and shows faintly through rises. He said "im up to speed" (15:00) after v258 to v260. Claude's calls for the rest (15:05, his to redirect): 4 crisper ridge crest only (no drainage channels: water imagery); 6 slight fade for far labels; 7 light distance haze and a smoother mesh; 8 contour lines dropped (Snowden). **Next:** his eye on v261; then strategy 7 (haze, smoother mesh), then 4 (ridge crest), then 6 (far-label fade), then attribution. Still open: the v255 lighting check and the color wash (his call only). New tool: tests/cardshot.py. Local tests/w20.json (46 notes, placeholder text) and tests/broadview.json are trimmed copies, kept out of git.

2026-11-24 15:20: **v260 live**, the goal rings no longer sit over a label (his yes 14:45; docs/v260_update.md): the rings count as taken ground when labels are placed, and a label moved off them gets a leader line. GOAL and the side words keep their places. Broadview ground unchanged. **Next:** his eye on v258, v259, and v260; then strategies 4 to 8 of the relief test (strategy 5, routes laid on the ground, also finishes entangled strategies), then attribution. Still open: the v255 lighting check and the color wash (his call only). Local tests/w20.json, tests/broadview.json, and tests/wring.json (w20 plus three notes on the rings) are trimmed test copies, kept out of git.

2026-11-24 13:45: **v259 live**, Taking Action: walk a way, step by step (his ask 12:39, "not being able to trace where nonlinear strategies go and in what order"; docs/v259_update.md). Claude's call: one leg at a time with the rest dimmed, plus every stop listed in order in a strip that can be tapped. A "Walk way A, step by step" button sits beside Reset view on card maps; Back, Next, the arrow keys, and Escape work; on a card in the page it opens the card's full screen and closes it after. Test: tests/walk.py (NOFS=1 for a card in the page, CARD=n for a given card). Earlier the same hour: **v258 live**, 3D label pile-ups fixed (docs/v258_update.md): labels find free ground around their own pin, with a thin leader line when moved; other pins' heads count as taken ground. He praised v257's WHAT THE SYSTEM IS DOING (12:34: "brilliant! Keep that up!"). **Next:** his eye on v258 and v259; then the goal rings over a label, then strategies 4 to 8 of the relief test, then attribution ("NOW · the 3D visual"). Still open: the v255 lighting check and the color wash (his call only). Local tests/w20.json and tests/broadview.json rebuilt from the project and kept out of git.

2026-11-24 12:30: **v257 live**, WHAT THE SYSTEM IS DOING trimmed to four paragraphs and tied to his own levers (docs/v257_update.md). **Next:** his eye on it; then "NOW · the 3D visual" (label pile-ups first). Still open: the v255 lighting check and the color wash (his call only). Local tests/w20.json rebuilt (goal, answers, notes) and kept out of git.

2026-11-24 12:10: **v256 live**, the approved emotion definitions (his calls 11:52 to 12:00; docs/v256_update.md; final text in the Claude project, claude/emotion_definitions_redline.md). **Next:** trim WHAT THE SYSTEM IS DOING to match the definitions and tie it to his own levers; then back to "NOW · the 3D visual" (label pile-ups first). Still open from the morning: the lighting check on v255 and the color wash (his call only).

2026-11-24 10:47: **v255 live** (checked on operationalcoherence.com/bcm: the label reads v255). Today's 3D work, his call 09:37: "lets work on the 3d visual some more"; his rule 09:38, with five of his Bear Canyon photos: "Improve quality and realism only. Do not reinterpret or redesign."
- **v253** realism, first pass (docs/v253_update.md). **v254** the whole map reads as rock, not coral (his note 10:00; docs/v254_update.md). **v255** toward photorealism (his note 10:08, "I am just not seeing that photo realism"; docs/v255_update.md).
- **Open with him:**
  1. Lighting (10:45). He prefers the lighting in the screenshot I sent (h1, v255 full screen, Synthesis on 11-20) to what he saw on Taking Action, Analysis, and Synthesis. v255 went out at 10:39, so he most likely still had v254. I asked him to reload, check the label says v255, and send a screenshot of any view that still differs. All views share one lighting setup in relief.js, and a sharper screen tested the same brightness. If a view does differ, match it to h1.
  2. Color wash. I sent him color_60_vs_40.png (the same view at 60% and at 40%, the 40% not shipped). The 60% wash is what limits photorealism. Changing it is his call only (ALPHA in relief.js); do not change it unasked.
- **Next on the queue** (BCM_TASK_QUEUE.md, "NOW · the 3D visual"): label pile-ups, then the goal rings over a label, then strategies 4 to 8 of the relief test, then entangled strategies, then attribution.
- **How the 3D now works (line maps; place maps untouched, Broadview pixel-identical every version):**
  - `layerAt()` is one bedding coordinate (LP = 6 units of height per layer, a slight dip, a slow wander). It drives both the cliff bands in `hAt()` and the rock's color bands.
  - `hAt()`: hard layers stand out as cliff bands on steep ground, fading along their length (`hard`, `kt`); gentle ground rolls. `hRaw` (the notes' shape) is never changed.
  - `paint()`: works out each material only where it shows. Horizon shading comes from `HAO`. It writes a normal map (`ncv`) and a rock mask (`mcv`).
  - Terrain material `onBeforeCompile`: rock detail drawn on the graphics card from world position (3-octave noise plus layers by height), only where the mask is rock, fading below a pixel.
  - The ground is RS = 3 (1.5× the old grid). Sky light comes from a PMREM gradient sky (environmentIntensity 0.3) plus a hemisphere light (0.85). The sun is (-290, 215, -175), warm. Soft shadows, map 4096.
- **Tried and dropped (don't retry without reason):** GTAO post-processing (flattened the picture, grayed the background); RS = 4 with 5-octave detail (tour.py times out, i.e. frames too heavy); even ledges (looked like contour lines); a strong tilt (looked like wood grain); full rings in pits (looked like a quarry); squiggly crack lines (looked like dried mud); dark shrub clumps (looked like puddles, i.e. water imagery).
- **Cost:** first build about 5.3 s on 11-20 in testing (v252: 2.2 s); cached after.
- **Tools:** tests/reliefshot.py PREVIEW.js RELIEF.js WB.json OUT.png [tab] takes a same-camera full-screen shot and prints the build time; DSF=2 gives sharp crops. tour.py on 11-20 is the frame-cost guard: run it after any 3D change. To test a variant, sed a copy of relief.js into tools/relief/_x.js (so imports resolve), build it to /tmp, delete the copy.
- Local test copies tests/w20.json, tests/w13.json, and tests/broadview.json are trimmed (positions and emotions only; Broadview with its drawn areas) and kept out of git. Rebuild them from the project's workbooks/ when needed.

2026-11-24 10:25: **v254 live**, the whole map reads as rock, not coral (his note 10:00; docs/v254_update.md): bedded cliff bands on steep ground, rolling gentle ground; the notes' shape is unchanged. **Next:** his eye on v254; then label pile-ups and the goal rings ("NOW · the 3D visual" in BCM_TASK_QUEUE.md).

2026-11-24 09:57: **v253 live**, the 3D ground looks more like real Bear Canyon (his photos, 09:38: "Improve quality and realism only. Do not reinterpret or redesign."; docs/v253_update.md). Line maps only; Broadview pixel-identical. The 3D work is now at the top of BCM_TASK_QUEUE.md ("NOW · the 3D visual"). **Next:** his eye on v253, then label pile-ups and the goal rings. Screenshot tool: tests/reliefshot.py (same camera; DSF=2 for close crops). Local test copies tests/w20.json, tests/w13.json, tests/broadview.json are trimmed (positions and emotions only) and kept out of git.

2026-11-24 later: **v252 live**, every note brings its own emotion color to its own spot on the 3D ground (docs/v252_update.md); acceptance on the hinder side now shows teal. **Next:** he marks claude/emotion_definitions_redline.md, the definitions ship, and WHAT THE SYSTEM IS DOING is trimmed to match and tied to his own levers. Local test copies tests/w20.json and tests/broadview.json are trimmed and kept out of git.

2026-11-24 09:30: **v251 live**, Pattern Analysis read as a reader (his go-ahead 09:03; docs/v251_update.md; review in the Claude project, claude/pattern_analysis_reader_review_2026-11-24.md). Still open from that review: trim WHAT THE SYSTEM IS DOING in full and tie it to his own levers. **Next (his call 09:23): the ground color fix**, acceptance on the hinder side doesn't show its color on the 3D ground (BCM_TASK_QUEUE.md, "Acceptance on the hinder side doesn't show on the ground"); every note's emotion stays visible at its own spot, nothing else on the line map changes. Then he marks claude/emotion_definitions_redline.md, the definitions ship, and WHAT THE SYSTEM IS DOING is trimmed to match.

2026-11-24: **v248 live**, Pattern Analysis as several stories, the first build of Several Systems (docs/v248_update.md). His 11-20 workbook is now in the Claude project as workbooks/bear-canyon-workbook-2026-11-20.json. Its local copy is tests/w20.json, kept out of git. Test with tests/stories.py, tests/storyshot.py, and matrix.py. 2026-11-24 later: **v249 live**, the Pattern Analysis gibberish fixed in the phrase layer (docs/v249_update.md). Then **v250 live**: no note fragments in any narrative line (his note 08:23, docs/v250_update.md); a line names a theme only when two differently worded notes share the phrase, else counts the notes with their numbers behind. Local test copies tests/w13.json and tests/broadview.json are trimmed (notes and answers only) and kept out of git. Next on the queue: the acceptance color and emotions on both sides of the line; the Taking Action review.

Earlier: 2026-11-19, morning. Preview at **v247** (v197–v231 pushed 11-18; v232–v247 pushed 11-19). **The pre-F8 review table is answered and applied (v236, docs/v236_update.md).** The BCM page is operationalcoherence.com/bcm (/gsmlive is defunct). The work queue is his v196 review, analyzed in claude/v196_review_plan.md in the Claude project (private, because it quotes his workbook). Version-by-version detail is in docs/bcm/BCM_CURRENT_STATE.md and docs/vNNN_update.md.

## First thing next session
1. Attach operationalcoherence/BCM with push. If it's refused, tell him plainly and stop; don't work around it. (A read-only clone of the public repo is fine for reading code.) On 11-18 every first attempt was refused, and each time it worked after he said "push access granted."
2. ~~A short check of Taking Action only~~ Done in v230. What it left open (the "Carries furthest" wording, the ground card titles in docs/v230_update.md, and his redlines on the v226 wording at the end of docs/v226_update.md) goes into the review table.
3. **Next:** (a) ~~Way A~~ done in v237: it follows the data's path (docs/v237_update.md); (b) "One through four" confirmed by him 11-19 09:57; (c) F1/F2 talked through 11-19 10:03: F2 is already true (fixed goal and axes, notes stay where placed, local ground edits); F1 item 1 done in v238 (YOUR PLACE IN 3D, docs/v238_update.md); his ask 11-19 10:26: card maps open on Taking Action (done, v239) and direction arrows on the ways (done, v240); numbered stops on the selected way (his note 10:52; done, v241); place relief exaggerated and sharper imagery (his note 11:15; done, v242); looser cap and hillshade (his yes 11:47; done, v243); place tours read the place (his note 12:01; done, v244; v244 broke Synthesis 3D on places with emotionless notes, fixed v245); tour Back/Next and glowing focus (his ask 14:13; done, v246); next v247. Queued 14:34 (BCM_TASK_QUEUE.md, top): place-map Pattern Analysis drops the old figure and takes the line map's content format; place-map In Parallel aligns with the line map's (figure, format, everything), bare rock on place maps shown as color (his yes 11-19 10:06). His rule (11-19 10:05): no modifications to the line map or its visuals, "its perfect". **F8 is not part of this cycle** (his call, 11-19 09:56). History: **His call (11-19 07:06): finish the whole build (everything except F8) first, then one thorough review, as a table, before F8.** All redlines (step 9 part 2 in docs/v232_update.md, the v226 wording, the R items, the word-budget cuts, and every open call below) go into that table, not one at a time. Reprioritized 11-19 07:37 by effect on the UI (his usage is limited): done are 3c the ground tap (v233), the tour act captions (v234), and the YOUR OWN WORDS strip (v235). Still to do: the word-budget cuts, drafted straight into the review table; the WebM download (skipped for now); A1 (skipped for now). Rows 34 and 35 (THE EMOTION CHANGES and PLACED ONE WAY, TIED THE OTHER wording) go in the table. F1/F2 is discussed in the review. F8 is last.
4. When he reports something already fixed, check which version his page shows first (the label is at the bottom of the page). GitHub Pages can serve the previous build for up to ~10 minutes after a push.

## Review cadence (agreed 11-18 17:18; confirmed 11-19)
- After step 8: a short check of Taking Action only (done, v230).
- Next full review: once everything but F8 is built, as one table, before F8.
- One session per step, starting from this file.

## Where the review plan stands
- **Phase 1** (v197–v203): done.
- **Phase 2:**
  - Step 6 (Pattern Analysis reordered): done (v205–v207, v211).
  - Step 7 (Pattern Synthesis reordered): done (v212, v217, v218).
  - Step 10 (In Parallel): done (v213–v216, v219).
  - Interpretation pass: done for Analysis (v220–v222, v224) and In Parallel (v223, v225); keeps going as he asks.
  - **Step 8 (Taking Action): done, v226.**
  - **Step 9, Mapping Context: built, v232** (instructions on their pages, emotion meanings on every note, WHO DID WHAT line). His redlines on it wait for the review table.
- **Phase 3:** done are 3c, the ground tap (v233, tests/groundtap.py); the tour act openers (v234, tour.py); and 3g, the YOUR OWN WORDS strip (v235, tests/ownwords.py). Still to do: the word-budget ("poetic") cuts, which go in the review table (THE WAY FORWARD first); the WebM download, skipped for now.

## v227
The constraint buttons show grayed out before typing; each note on Mapping Landscape shows its constraint (`gsmNoteCons`). 

## v228
Taking Action in three layers (his yes, 21:37): a decision strip, then Why this action, then Evidence; `gsmTALayer()` in `gsmTAPass`. The strip reads `data-tv`/`data-ts`/`data-ws` on seeded cards. Tests that type into a card must open `.tawhy` and click `.tanb` first.

## v229
The 3D way readings go into the card's Evidence (`.taev > .taways`, written by `fillCourseBox()` when the card is layered and not in full screen).

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

## Open calls for him
- Answered in the review table and applied in v236 (docs/v236_update.md). Done in v247 (his yes 14:50): place pages lose the line map's language (bare rock as color on place maps). F8 is not in this cycle. D8: voices stay equal until F8. The WebM download and A1 come after F8, or are dropped.
- Older items not in the table (his redlines on claude/meaning_patterns_draft.md and claude/structure_pass_plan.md, the U5 instruction redlines, the real-tile check, small calls v191–v194): treat them as settled by the table unless he raises them.

## Standing rules (his)
- Preview only: never touch anything else. The preview page is public; every push is live within minutes.
- American spelling; serial comma everywhere. "Emotion", never "feeling". "The method" = the whole BCM.
- Q.1–Q.4 are grasping context; Q.5–Q.7 are designing for the context grasped. On screen, say "the context you have grasped" and "what you would design" rather than bare question numbers.
- Changes go in the engine for everyone, never tied to his workbook.
- Place maps never get bare rock (11-19 14:39): rock there is the real land and means nothing; on line maps it means everything.
- Test every place-map change on Broadview (tests/broadview.json, rebuilt from the project copy): it has notes with no emotion, drawn areas, and repeated notes. v244 broke on it.
- Never merge words unless he says (THE SAME THING? asks).
- Flag Claude's wording; show redlines for his text and wait.
- Story over list; tell people what they don't already know. Send files one per message.
- Don't ask long lists of questions: decide, say which, let him redirect.
- **No action grid anywhere in the project** (11-18 14:30), including its Act Here / Act Anywhere or reach language.
- **Tour captions never cite the paper** (11-18 15:21). Page text keeps its citations.
- Don't frame anything as context-free versus context-sensitive, or as bounded applicability (Snowden and Juarrero's terms).
- Never rely on hover alone to carry meaning (v207).
- Never name a note by a fragment of its text in a narrative line (11-24 08:23): name a theme only when two differently worded notes share the phrase; otherwise say what the notes are and where they stand, numbers behind.
- Lead each tab with meaning; put the inventory under it, closed. Interpretation over inventory.
- Taking Action describes the situation, not the workbook (11-18 21:53): say what remains unresolved, keeps reinforcing, or is not yet used; never "answered" or "built on". Note numbers go behind, small and gray. On screen, "the system that holds" is WHAT HOLDS THE SITUATION IN PLACE.
- Don't let a page grow long: v226 kept Taking Action near its old length by folding word-only cards.
- **Single words (v288, his halfway measure 11-25):** a single word is stated only when it reads as a thing, comes up in 2+ places, and is shown with the user's own clause and its place; emotion names always count.
- **No one-tap questions just to cover the engine's limits** (11-25 19:28: "it bothers the user with our shortcomings"). Widen or tighten the engine's own tests instead. Not the questions he asked for: A LOOP BETWEEN GROUPS and TWO WAYS OF RUNNING stay (11-25 21:41). Ask before removing any question.

## How to build and test
- **Repo:** operationalcoherence/BCM (public). main feeds the preview through GitHub Pages; the page loads gsm-preview.js and gsm-relief.js with a per-minute cache-buster.
- **Engine:** edit gsm-readable.js, then `esbuild@0.24 gsm-readable.js --minify --outfile=gsm-preview.js`.
- **3D:** tools/relief/relief.js plus three@0.187.0, then `esbuild tools/relief/relief.js --bundle --minify --format=iife --outfile=gsm-relief.js`. Install three and esbuild in a scratch directory and point NODE_PATH at it.
- **Each version** = one patch script in tools/patches/ + docs/vNNN_update.md + the label bump (`t.textContent = "vNNN"`). To rebuild from scratch, restore gsm-readable.js and tools/relief/relief.js from v209 (commit 3a00154) and run v210 → v247 in order (v220–v226 have no relief part). Before any `git checkout -- .`, run `git checkout HEAD -- <files>`.
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
1. ~~Way A~~ done, v237.
2. F1/F2: talked through 11-19. ~~F1 item 1~~ done, v238; v239 card maps open on Taking Action; v240 arrows on the ways; v241 numbered stops; v242 place relief; v243 place hillshade; v244 place tours; v245 fix; v246 tour focus; bare rock on place maps dropped (his call 11-19 14:39: naturally occurring rock means nothing on a place map, everything on a line map) (ask first: v244's tours no longer speak of rock on places) as color on place maps. F2 is already true.
3. F8, project lead dashboards: not this cycle (his call 11-19). When it comes: Plan in BCM_ARCHITECTURE.md §12a. Firebase: "The Bear Canyon Method", Spark plan ($0), Firestore nam5, rules locked, web app "BCM Preview", Google sign-in on. Never upgrade to Blaze without asking. Never put the Firebase web config or key in chat, docs, memory, or the repo. Test data only until there is a privacy page.
4. After F8, if still wanted: the WebM download of the tour, and A1 (threads across question boundaries).

Not yet done: docs/v193_update.md was never written (v193 is F6 hysteresis).

## Links
- The two-pictures canvas: https://claude.ai/artifact/GfYmgywiBj3q7F7vKvgJR9
- Wording review sheet (done): https://claude.ai/artifact/KkdeKLx5E45pWKpYU1FE3V
- F8 mockup: https://claude.ai/artifact/Dqy6xjxr4wPyGpKAf6hn4T
- F8 costs write-up: https://claude.ai/artifact/4QdCsBzitJneX76CDjHuiL
- **The pre-F8 review table (11-19, v235): https://claude.ai/artifact/84H2tJCmJvqMcQoDDZdrit** (37 rows; answered 11-19 09:20, applied in v236)
