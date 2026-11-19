# BCM_CURRENT_STATE.md
Rev 24 · 2026-11-19 · Preview at **v239** · Basis: 11-17 review, 11-18 review, export 2026-11-13, workbook 2026-11-18, repo

## Shipped
- **v239** (2026-11-19, preview): Taking Action shows each card's 3D map open under its decision strip; the card legend is folded; everything else stays closed. See `docs/v239_update.md`.
- **v238** (2026-11-19, preview): F1 item 1. A workbook with both maps gets YOUR PLACE IN 3D, a closed fold on Analysis and Synthesis with the place ground (place notes P1, P2, and so on). The line map is untouched. See `docs/v238_update.md`.
- **v237** (2026-11-19, preview): Way A on strategy cards follows the data's path, through the low ground (nearest the ridge first, defiance last), over the nearest ridge, and up to acceptance, matching THE WAY ACROSS. See `docs/v237_update.md`.
- **v236** (2026-11-19, preview): his answers to the pre-F8 review table applied. See `docs/v236_update.md`.
- **v235** (2026-11-19, preview): plan 3g. YOUR OWN WORDS opens with a strip, Q.1 to Q.7 under the context grasped and what you would design, with each question's key phrases and where else they appear. See `docs/v235_update.md`.
- **v234** (2026-11-19, preview): the Synthesis tour opens each of his four acts with what it means, counted from the workbook. See `docs/v234_update.md`.
- **v233** (2026-11-19, preview): plan item 3c. With All notes shown on YOUR LANDSCAPE (Analysis), a tap on the ground pins WHAT GATHERS HERE, a reading of that spot: the notes and questions that shape it, the emotion that colors it and its ground, any climb between distant emotions, and how what you would design meets the context you have grasped there. In 3D and flat. See `docs/v233_update.md`.
- **v232** (2026-11-19, preview): **Phase 2 step 9, part 1.** Start here keeps the method (01–06). The mapping steps sit in the Mapping Landscape drop-downs (HOW TO MAP on step 1; DESCRIBE YOUR NOTES: INSTRUCTION on step 2). Analysis and Synthesis each have a closed INSTRUCTION drop-down on their own tab. Every note shows the paper's definition of its emotion in gray under the buttons. Mapping Context says what combining puts in WHO DID WHAT. His text was moved word for word. See `docs/v232_update.md`.
- **v231** (2026-11-18, preview): the constraint boxes and grayed Q.4/Q.6/Q.7 buttons show again on Taking Action. See `docs/v231_update.md`.
- **v230** (2026-11-18, preview): Taking Action speaks about the situation, not the workbook (his wording review). THE SYSTEM THAT HOLDS becomes WHAT HOLDS THE SITUATION IN PLACE, on Analysis and Taking Action. THE TEST lines say what remains unresolved, what keeps reinforcing the situation, and what help is not yet used, with note numbers small and gray. Also the short check of Taking Action, with four fixes. See `docs/v230_update.md`.
- **v229** (2026-11-18, preview): the 3D way readings on each card (why choose each way, comparing them, moves in order, when to stop) move to Evidence under HOW THE WAYS READ ON THE GROUND. The map and chart stay in Why this action. See `docs/v229_update.md`.
- **v228** (2026-11-18, preview): Taking Action in three layers, with nothing removed. The cheapest first move leads THE TEST; the test is summarized first. Each card shows a decision strip (meets the test, first move, the way across, reading splits), then "Why this action" (closed except on the first-move card), then "Evidence" (closed). Empty constraint boxes collapse to "Name what holds it". On first load the 11-18 page shows about 1,800 words instead of about 5,100. See `docs/v228_update.md`.
- **v227** (2026-11-18, preview): the constraint loop made visible. The Q.4/Q.6/Q.7 buttons show grayed out until a constraint is written, and each note on Mapping Landscape shows the constraint named for it and whether it is in Q.4, Q.6, or Q.7. See `docs/v227_update.md`.
- **v226** (2026-11-18, preview): **Phase 2 step 8, Taking Action, done.** The page is rebuilt around the central test (ARCHITECTURE §0.3). THE TEST panel reads the workbook against it: what holds it, what already moves, where it can shift, where the reading splits, constraints named, and the cheapest first move. Cards are seeded from Pattern Analysis's structure: strategies from THE SYSTEM THAT HOLDS, THE KEY TENSION, and THE LOOP; programs from THE OPPORTUNITY, WHAT IS ALREADY HELPING, and SUPPORT NOT YET REINFORCED. Each seeded card has its own test, THE WAY ACROSS (ridge before bare rock, the cost of each move, behaviors first below the ridge and emotions first above it, entrenched notes), and 3D ways. In Parallel's split readings (TWO PEOPLE, TWO SIDES; THE EMOTION CHANGES; ONE IDEA UNDER TWO NAMES; PLACED ONE WAY, TIED THE OTHER) are carried onto the cards they touch, as what each means for acting. Constraints now go somewhere: one tap adds a constraint to Q.4, Q.6, or Q.7; WHAT YOU DID lists and saves them (`acts[].c`) and flags their notes; SINCE YOU ACTED shows them. Strategies and programs are grouped, with word-only cards folded under each group. The chart is open, and each field says what it does. Analysis, Synthesis, and In Parallel are unchanged. See `docs/v226_update.md`.
- **v220–v225** (2026-11-18, preview): the interpretation pass. Analysis: meaning first (v220), WHY IT BEHAVES THIS WAY (v221), YOUR STORY SO FAR leads (v222, v224). In Parallel: WHAT THE TWO PICTURES REVEAL (v223), and double readings without counts (v225). See `docs/v220_update.md` to `docs/v225_update.md`.
- **v219** (2026-11-18, preview): no (Vigneaux, 2026) in either tour (his call; page text keeps citations); Full screen on the In Parallel figure with a HOW TO READ IT panel, the key, and the word reading. See `docs/v219_update.md`.
- **v218** (2026-11-18, preview): the patterns row stays in full screen (moved into the map at top left via `D.onFs`; hidden while the tour plays). See `docs/v218_update.md`.
- **v217** (2026-11-18, preview): the patterns row shows only on the Synthesis map (it leaked onto Analysis through the shared template, where its buttons did nothing). Lesson: the terrain template is shared by Analysis, Synthesis, In Parallel, and cards; gate anything new on ANH/PAR/CARDH. See `docs/v217_update.md`.
- **v216** (2026-11-18, preview): In Parallel cut to the figure (5c–5e): figure, Where to start, then MORE FROM BOTH PICTURES (closed) and THE EARLIER 3D VIEW (closed, last); agree/differ paragraphs dropped where the figure shows (`gsmIntOrder`). See `docs/v216_update.md`.
- **v215** (2026-11-18, preview): his call: no action grid anywhere. In Parallel opens with THE TWO PICTURES, SIDE BY SIDE (moved there from the end of Synthesis); gsmGrid() deleted; MOVES, IN ORDER without grid or reach wording; tapped lines wait for the Synthesis 3D (`window.gsmSynPend`). See `docs/v215_update.md`.
- **v214** (2026-11-18, preview): the agreement figure drawn with lines, his call ("use lines"): solid black = the ground agrees, dashed red = it asks; boxes styled by what Analysis found (black contested, dashed gap, teal unused support, grey designed without a cause); key under the figure; thin lines on the 3D too. See `docs/v214_update.md`.
- **v213** (2026-11-18, preview): THE TWO PICTURES, SIDE BY SIDE closes Pattern Synthesis (review 5a/5b): Analysis words in a column, hoses onto the Synthesis ground painted by the relief's rule (black = the ground agrees, white = it asks); tapping a word reads it and draws its hoses on the 3D above (`hoses()` in relief.js; `window.gsmSynRel`); In Parallel's own 3D folded behind THE EARLIER 3D VIEW. Line maps only. Built in `gsmAgreeFig()` from the same lists as WHERE BOTH PICTURES AGREE. Test: `tests/agree.py`. See `docs/v213_update.md`. Next: In Parallel 5c–5e (explain risk/wildfire risk/vegetation; cut the text; WORTH A SECOND LOOK visual; shorter WHERE BOTH AGREE).
- **v212** (2026-11-18, preview): step 7, Pattern Synthesis: patterns row above the figure (`fillLay`/`syncLay`); the Supports questions only under PATTERNS; matches bolded in pattern sentences and CAUSE AND EFFECT; findings with no note name their answers (gsmPhNameH). See `docs/v212_update.md`.
- **v211** (2026-11-18, preview): 3d, WHAT IT PRODUCED: bigger themes (repeated phrases sharing ≥2 notes, identical notes counted once), no lone words (else the shortest note quoting the word), leads into YOUR LANDSCAPE. See `docs/v211_update.md`.
- **v210** (2026-11-18, preview): the tour: full screen on Play; big Play/Pause + End tour at bottom center; 17/20 px captions held by reading time (~1.5 min on 11-18); READING THE GROUND opens it (cost and feasibility of moves, bare rock); a bare-rock reading (`rockFaces()`); WHAT THE GROUND SAYS edited; Pattern Analysis gets its own short tour (`introStops(true)`); Escape-in-full-screen bug fixed. Tests: `tests/tour.py`, `tests/tour_an.py`. See `docs/v210_update.md`.
- **v209** (2026-11-18, preview): the tour in full screen clears the legend; Pause/Play instead of Stop (a click pauses; Play returns to the same stop); no hover boxes while it plays; about 30 s. Confirmed it visits all 12 readings in order. See `docs/v209_update.md`.
- **v208** (2026-11-18, preview): the guided tour of the ground (review 4c). Play the tour on the Synthesis 3D: the camera visits each reading of WHAT THE GROUND SAYS in his four acts, captioned with the data (share of the ground, climb as a share of the map's height); about 25 s; a click or Escape stops it. See `docs/v208_update.md`. Not yet: WebM download. Next: WHAT IT PRODUCED (3d), then step 7.
- **v207** (2026-11-18, preview): card titles show their whole context sentence in small gray text (hover didn't work for him); thread cards pick the phrase's most central sentence (wildfire management: N33, not N12). See `docs/v207_update.md`. Next: the guided tour of the ground (he asked for it next, with % of energy and key data points), then WHAT IT PRODUCED (3d) and step 7.
- **v206** (2026-11-18, preview): Phase 2 step 6, second half. YOUR STORY SO FAR told as a story from the context grasped (Q.1, the present, further on toward the goal, how it is spread), quoting his notes; the medium word closes it in one sentence. Architecture doc brought to Rev 9. See `docs/v206_update.md`. Next: deepen WHAT IT PRODUCED (3d), then step 7 (Pattern Synthesis reordered).
- **v205** (2026-11-18, preview): Phase 2 step 6, first half. Pattern Analysis opens with AT A GLANCE, THE SAME THING? as a prompt (with a sentence for each word), then WHAT IT PRODUCED; WORDS THAT MAKE THE WORLD has its own fold; question hovers on YOUR LANDSCAPE; THE SAME THING? buttons fixed (they never saved). See `docs/v205_update.md`. Next: step 6 second half, YOUR STORY SO FAR as a story (3e) and WHAT IT PRODUCED deepened (3d).
- **v204** (2026-11-18, preview): read against his 11-18 workbook. Ground cards don't decide what the emotion is aimed at; the FIRST MOVES way line names the emotions; up to three ground cards (N35 gets one). See `docs/v204_update.md`.
- **v203** (2026-11-18, preview): FIRST MOVES follows the selected way (a line per way under FIRST MOVES). E9 done the other way round: the words follow the way, because making way A follow FIRST MOVES made ways far longer (measured, see the doc). Phase 1 of the review plan is done. See `docs/v203_update.md`. Next: Phase 2 (reordering Analysis, Synthesis, and Taking Action; constraint fields that go somewhere; In Parallel's agreement figure).
- **v202** (2026-11-18, preview): P3 first half. Acceptance into aggression, distrust, or defiance makes a strategy; a saved manual switch on every card; cards from the ground for hostile emotion among acceptance on the help side; up to four strategies. See `docs/v202_update.md`. Next: v203, FIRST MOVES follows the selected way and way A follows FIRST MOVES.
- **v201** (2026-11-18, preview): P1 second half, Analysis and Synthesis. WHAT YOU WOULD DO without causes or counts; findings named by repeated phrases with their notes; no single-word themes; 3l counts Q.5–Q.7 notes as planning; ONE WORD, SEVERAL MEANINGS opens each meaning into sentences and lists the actions around the word. See `docs/v201_update.md`. Next: P3, cards from the ground (v202).
- **v200** (2026-11-18, preview): P1 first half, Taking Action. Card titles are phrases from his own writing (never a lone word; whole sentence on hover), and every card has IN SERVICE OF THE GOAL. See `docs/v200_update.md`. Next: P1 second half (v201), the same layer on Pattern Analysis and Pattern Synthesis (3f, 3i, 4h, 4i).
- **v199** (2026-11-18, preview): one derived-state pass (P2). The action points MOVES, IN ORDER reads are computed by gsmDerive() from the workbook on every pass, not inside In Parallel's drawing; In Parallel's grid draws from them. No page reads differently on his workbooks. See `docs/v199_update.md`. Next: Phase 1 step 4, the phrase-and-meaning layer (P1, v200–v201).
- **v198** (2026-11-18, preview): first pass on his 11-18 review. Emotion definitions (direct quotes from Vigneaux, 2026) on every emotion button and under the emotion key; Mapping Context title at the top, the goal's instruction, WORKING WITH A FRIEND under the goal; instruction 10 for place maps; Supports / Does Not Support; the two pictures card moved to the end of Pattern Synthesis; Taking Action sources into REFERENCES, Morin citation, NOTHING YOU WOULD DO ANSWERS THESE YET. See `docs/v198_update.md`. Next: Phase 1 step 3 of the review plan, one derived-state pass (gsmGridPts out of In Parallel).
- **v197** (2026-11-17, built; pushed 2026-11-18): the method's name under every 3D map; indifference joined into one yellow band (reaches N31 on 11-13); ways keep fixed letters (A notes, B firm ground, C support), one badge each, side by side where shared. See `docs/v197_update.md`.
- **v196** (2026-11-17, preview): his wording review of v171–v195 applied; serial comma everywhere. Action grid redesign (row 30) and rows 34–35 open. See `docs/v196_update.md`.
- **v195** (2026-11-17, preview): F7, WORDS THAT MAKE THE WORLD on Pattern Analysis (bare saturated words; other voices tested as perturbations). D10 answered yes. See `docs/v195_update.md`.
- **v194** (2026-11-17, preview): F4 reflexive loop, WHAT YOU DID on cards flags Q.1–Q.4 notes; SINCE YOU ACTED on Mapping Landscape. See `docs/v194_update.md`.
- **v193** (2026-11-17, preview): F6 hysteresis, emotion history per note (eh); held opposition costs more to cross. See `docs/v193_update.md`.
- **v192** (2026-11-17, preview): F3 + F5, ways weigh friction, boomerang risk and bare rock faces; effort and chart updated. See `docs/v192_update.md`.
- **v191** (2026-11-17, preview): A2, coworking-ready schema (sv 2, wid, mt, gone); Combine takes newer edits and their own deletions. See `docs/v191_update.md`.
- **v190** (2026-11-17, preview): Open workbook (and Combine) work from every tab; the Replace question was showing on a hidden tab. See `docs/v190_update.md`.
- **v189** (2026-11-17, preview): place maps stand on the real terrain, true to scale (AWS Terrain Tiles), emotion as color only; replaces v186's emotion relief on places. See `docs/v189_update.md`.
- **v188** (2026-11-17, preview): G1, glossary popovers on the first use of 12 terms per section and card; definitions reuse on-screen wording. See `docs/v188_update.md`.
- **v187** (2026-11-17, preview): T5, WHAT HOLDS IT IN THE LOW GROUND on Taking Action cards, his constraint question per low-ground note, answers saved in the workbook. See `docs/v187_update.md`.
- **v186** (2026-11-17, preview): place-map-only workbooks get the 3D ground on Esri imagery (Analysis, Synthesis, In Parallel, cards); areas as patches; START = note farthest from the goal. See `docs/v186_update.md`.
- **v185** (2026-11-17, preview): Taking Action legends back as before v184 (under every card map, programs too); card full screen gets the Pattern Synthesis legend drawer. See `docs/v185_update.md`.
- **v184** (2026-11-17, preview): maps load once (no flat chart or blurry canvas first); strategy cards keep a legend, programs none; action grid shows every note, hoverable. See `docs/v184_update.md`.
- **v183** (2026-11-17, preview): POSSIBLE PATTERNS names the emotion (N3); voices weighted evenly on the ground (V5). See `docs/v183_update.md`.
- **v182** (2026-11-17, preview): tap to inspect on touch (U7); long lists fold into View details (U8); WHAT STANDS OUT findings say what they mean (N3). See `docs/v182_update.md`.
- **v181** (2026-11-17, preview): MOVES, IN ORDER on strategy cards (T6). See `docs/v181_update.md`.
- **v180** (2026-11-17, preview): In Parallel findings told as meaning (N4). See `docs/v180_update.md`.
- **v179** (2026-11-17, preview): action grid on In Parallel (T4). See `docs/v179_update.md`.
- **v178** (2026-11-17, preview): full-screen legend pushes the map aside (his bug report); In Parallel has its own picture (question lines + numbered places) and WHERE THE TWO PICTURES MEET. See `docs/v178_update.md`.
- **v177** (2026-11-17, preview): Taking Action ways compared (why choose each, why the harder way, when to stop and readjust per Morin, chart of effort/impact/benefit/return). See `docs/v177_update.md`.
- **v176** (2026-11-17, preview): In Parallel shows one 3D landscape for both pictures; readings no longer mention petals or the tangle. See `docs/v176_update.md`.
- **v175** (2026-11-17, preview): Pattern Analysis opens with the 3D landscape, one question at a time, and WHAT THIS SUGGESTS read from it. See `docs/v175_update.md`.
- **v174** (2026-11-17, preview): Taking Action cards show their 3D again (a v171 regression had dropped every card to the flat fallback); Juarrero and Waldrop references corrected. See `docs/v174_update.md`.
- **v173** (2026-11-17, preview): story-form YOUR STORY SO FAR (N1), BIGGEST GAP sentence (N2), THE SAME THING? question (E3), symbol explainers (U2), ridge through other emotions (B3), 3D full-screen fix. See `docs/v173_update.md`.
- **v172** (2026-11-17, preview): saturation filter (E1), ONE WORD, SEVERAL MEANINGS (E2), stopwords (E4). See `docs/v172_update.md`.
- **v171** (2026-11-17, preview): Priority 1 batch 1. See `docs/v171_update.md`. Done: U1, U3, U4, B1, B4, B5, B6, C1, C2, C3, C4, C5, U6, R1, I1, the removal of THE EARLIER FIGURE on Synthesis, and an early version of V3 (full-screen legend drawer + name).

## Completed / working
- Q.1–Q.7 workbook, goal, notes with emotion, voice, source and author; JSON export/import; edit log.
- Mapping: 2D line map (PRESENT/FUTURE × HELP/HINDER) and ESRI spatial map.
- Pattern Analysis: the "Your story so far" opening paragraph is the right depth ("fire is resisted and supported and is in the goal"). Per-voice reading of "wildfire" is strong.
- Pattern Synthesis: 3D terrain, routes A/B, "Where it is easiest to get to" (strong insight, but descriptive only).
- Taking Action: "The Ways Forward, Sketched on the Ground" is the most valuable element.
- "Possible patterns": the "management" line works. "For and against" and "Unused support" are useful.

## Known gaps
- Place-map-only workbooks get the 3D ground on real terrain since v186/v189; the fuller per-instance Esri map (F1/F2) is still open.

## Known bugs
| ID | Bug | Page |
|---|---|---|
| B8 | Other low-meaning words can still surface ("measures", "set", "human"); the stopword list is domain-free and grows only for words with no meaning in any field | Analysis, In Parallel |
| B9 | Fullscreen legend clips over map nodes (3D: fixed v171 with a drawer; canvas fallback unchanged) | Synthesis |
| B10 | Hover-only tooltips unusable on touch; canvas gestures fight page scroll | All 3D/hover |

## Active issues (quality)
- Story over list: done for YOUR STORY SO FAR, BIGGEST GAP and WHAT THIS SUGGESTS; still lists in WHAT STANDS OUT, Possible patterns and In Parallel's patterns.
- Engine granularity: "fire" is never split into prescribed / unplanned / managed / mitigated / vilified, and stemming loses phrase context.
- "Thread" is used everywhere but never defined.
- Unclear findings: "Not in Q.5–Q.7 yet (30)", "Condition (3)", "Q.5–Q.7 only (9)", "Areas to reinforce", "Grounded across the board", "Spread out", "Placed one way, tied the other", "The emotion changes", "Where they differ", the In Parallel "Tradition/reduce/involved" paragraph.
- Low-value sections: Top strategy, Top program, What it rests on (keep Source and Voices), What stands out, In the words, Condition.
- "Behaviors first" is referenced without being explained.
- The minority voice (Other wildfire professionals, 5 notes) risks being flattened visually.
- Synthesis→Action: ways costed (v177), sequenced (v181), weighted by friction (v192), and, since v226, ordered through the ridge before bare rock (THE WAY ACROSS on seeded cards).
- Taking Action's word-only cards still come from recurring words. Since v226 they fold under the structure-seeded cards. A word card that repeats a seeded card isn't merged yet.
- Instructions are out of date across pages.

## Work in progress
- New 3D visualization (Synthesis) replacing the old figures; to be carried to Analysis and In Parallel.
- Note linking on Mapping Landscape (replaces the old "what you linked").

## Current dataset (test instance)
- Goal: make visible the distinction between aggressive suppression and putting more fire on the ground by managing unplanned fires.
- 31 notes · voices: Mine, Other wildfire professionals (5) · spatial map empty (`p.m: []`) · `links: []`.

## Pending decisions
| ID | Decision |
|---|---|
| D1 | Partly resolved v186/v189: place maps get a 3D ground (Esri imagery on real terrain, true to scale; emotion as color only). Still to discuss: the fuller per-instance Esri map with topological anchoring (F1/F2) |
| D2 | Resolved v172–v173: medium words are split by the person's own phrases; fire ≡ wildfire only on his Yes to THE SAME THING? |
| D3 | Formal IP statement: now a footer fold (v171). Move it to its own off-nav website page? |
| D4 | Resolved v174: "How constraints create coherence" |
| D5 | Resolved v174: "Complexity: The emerging science…" |
| D6 | Morin quote typo "andA" → "and" |
| D7 | 2 or 3 pathways by default on Taking Action |
| D8 | Saturation 40% (min 10 pieces, 2+ phrases); voice weighting √(mean/size) clamped 0.6–1.8, on by default (v183): on, or a switch? |
| D9 | Resolved v171: the per-question lines in WHAT IT RESTS ON were removed |
| D10 | Resolved v195: yes, as one folded item on Pattern Analysis |
| D11 | Resolved: the 7 symbols are the seven question symbols |

## Current priorities
0. **Build order (11-19):** 3g strip, tour captions, WebM download, review rows 34/35, A1, word-budget cuts drafted for the review table. Then the review table, then F8. The short check of Taking Action is done (v230). His redlines on the v226 wording are listed at the end of `docs/v226_update.md`; three wording items the v230 check left are in `docs/v230_update.md`.
1. His pass on Claude's wording, v171–v195 (each update doc ends with the list); U5 redlines (`docs/v173_update.md`).
2. Open questions from v186–v195: Combine and PDF for WHAT YOU DID (v194); the friction and hysteresis weights (v192, v193); coworker deletions and answers on Combine (v191); whether a place map should word "high/low ground" differently (he said: keep it, it means the emotion ground).
3. Remaining from the queue: A1 engine side (threads across question boundaries), D8 (voice weighting on or a switch), F1/F2 (per-instance Esri map, anchoring).
4. **F8, project lead dashboards: LAST. Remind Gregory.** Planned 11-17, no code yet (ARCHITECTURE §12a). Firebase project set up and locked, $0.
