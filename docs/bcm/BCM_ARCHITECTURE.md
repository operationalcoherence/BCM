# BCM_ARCHITECTURE.md
The Bear Canyon Method (BCM) — authoritative architecture
Rev 10 · 2026-11-18 (v219; v196–v206 in §16, v207–v219 in §17) · Sources: 11-17 and 11-18 reviews, workbook 2026-11-18, workbook export 2026-11-13, Vigneaux (2026), repo operationalcoherence/BCM

Markers: **[I]** inferred from the export or review, needs confirming against the code · **[?]** unknown · **[D]** decided in a review

---

## 1. Purpose
BCM is a free web workbook from Operational Coherence. It helps a practitioner, or later a group, work out how to move a goal forward in a complex social setting. It does this by reading the emotional and structural terrain around the goal.
- Users have read none of the source papers. The app must carry that theory for them. Vigneaux (2026) is the core text.
- Output rule: **tell users what they don't already know.** Give synthesis, relations and meta-meaning, never a recount of what they wrote.
- Presentation rule: **story over list.** Findings are written as narrative prose built from the user's own data points, and those data points keep their hover/tap popovers.
- Long-term direction [D]: BCM should be a living decision loop (map → act → re-map), not a one-off assessment.

## 2. System overview
- Internal app id: `groundsmith` (export `"app"` key). Export schema version `v: 1`.
- Hosting: the BCM page on the Operational Coherence website.
- Persistence: JSON export/import (`bear-canyon-workbook-YYYY-MM-DD.json`) and localStorage. No backend yet. A Firebase backend is set up for F8 (§12) but nothing uses it.
- Repo: `operationalcoherence/BCM` (public), served by GitHub Pages. The Webador page loads `gsm-preview.js` through a small stub. The old `/gsmlive` page (pasted v92) is **defunct** (Gregory, 11-17). The preview page `operationalcoherence.com/bcm` is the BCM page.
- Files: `gsm-readable.js` (the source, ~22k lines, one IIFE plus the terrain module appended) → esbuild minify → `gsm-preview.js` (what the preview page runs). `gsm-relief.js` = `tools/relief/relief.js` + three.js r187, loaded on demand for the 3D map. The canvas map is the fallback.
- Place map: Leaflet + Esri tiles. The key lives only in the Webador stub (`window.GSM_ESRI_KEY`), never in the repo.
- Storage: localStorage key `groundsmith-web-v1`; save/open as JSON; workbooks can be combined.
- Tests: `tests/` (Playwright). `matrix.py` runs every tab of every workbook; `dump2.py` renders tabs to text; `mkwb.py` writes the synthetic workbooks (always include a non-wildfire one); `relief_text.py` loads the 3D; `derive.py`, `switch.py`, `waymoves.py`, `qhover.py` check single features (see `tests/README.md`).
- Derived state (v199): `gsmDerive()` runs on every pass, right after `gsmMED` is set in `Ut`, and computes everything other pages read (`gsmGridPts`, `gsmGridAll`; phrase caches reset here). No page computes what another page needs.
- Release rule: one numbered version per batch, preview only, plus an update doc in `docs/`.

## 3. The questions (Q.1–Q.7)
The seven questions belong together. They are read as one flow in two phases, "like a river cascading" from one shelf of rock to the next [D]:

| Phase | Q | Role (inferred from the answers and the review) |
|---|---|---|
| **Grasping** (the context) | Q.1 | Within the community, why has the goal not already taken root? (map symbol label: "already doing") |
| | Q.2 | Is there opposition to the goal? |
| | Q.3 | Is there support for the goal? |
| | Q.4 | In order for the goal to take root and grow, what conditions need to be established? |
| **Designing** (for that context) | Q.5 | What needs to be designed? |
| | Q.6 | What needs to be redesigned? |
| | Q.7 | What needs to be reinforced? ("reinforced" in Vygotsky's scaffolding sense) |

Wording rules (his): "the method" means the whole BCM, never a part. The Q.1–Q.4 / Q.5–Q.7 grouping stays silent on screen: write only the question numbers, never a group name (the "grasping/designing" phases are for the architecture, not for display, unless he says otherwise). Write "emotion", never "feeling". Use American spelling. Changes go in the engine for every user, never tied to his own workbook.

The engine's category vocabulary (seen in the UI): opposition, support, conditions, design, redesign, reinforce.

## 4. Pages
In page order [I]:

| Page | Function | Key sections (current) |
|---|---|---|
| Start Here (tab 5) | Name, how to use, glossary (WORDS USED HERE) | — |
| Mapping Context (tab 0) | Goal, place, Q.1–Q.7 answers, who did what | — |
| **Mapping Landscape** (tab 1; was "Mapping Change", renamed v171) | Place notes on a 2D line map (x = PRESENT→FUTURE, y = HELP↑/HINDER↓) and a spatial ESRI map. 7 symbols. Note linking (new) | instructions, symbol legend |
| Pattern Analysis (tab 2) | Analysis of notes and answers | (v205 order) AT A GLANCE → THE SAME THING? prompt while unanswered → What your use of the method produced (v211: bigger themes from phrases in the same notes; leads into the map) → 1 · Looking in: Your landscape, one question at a time (3D; hover a question for its notes; its own short tour, v210) → Your story so far (v206: told as a story) → What stands out → In the words → Words that make the world (own fold) → Possible patterns → Still open |
| In Parallel (tab 6) | THE TWO PICTURES, SIDE BY SIDE (v213–v216, v219): Analysis's words in a column, a line to every note on the Synthesis ground that carries each (solid black = the ground agrees, dashed red = it asks); tap a word to read it and put its lines on the Synthesis 3D; full screen with HOW TO READ IT. Line maps only | Figure → Where to start → MORE FROM BOTH PICTURES (closed: Read together, Closest/farthest, Emotion, Voices, Patterns worth a second look, What might relate) → THE EARLIER 3D VIEW (closed). Where both agree / Where they differ appear only where the figure can't be drawn (place maps) |
| Pattern Synthesis (tab 3) | 3D terrain of emotion × structure | Looking out → How this map is made (fold) → About what you collected → The lay of the land: What the ground says (numbered readings, a bare rock reading, v210) → patterns row (v212; carried into full screen, v218) → 3D map with Play the tour → Patterns that run through it (phrase loops; the Supports questions; matches in bold) → Model a course of action → Cause and effect, Now and later, Scale, One judgement twice, In your answers not on the map, Does this serve the goal?, What it might mean, What it rests on, What you linked, What to pay attention to |
| Taking Action (tab 4) | Program/strategy cards (titles are phrases from the user's writing, v200; IN SERVICE OF THE GOAL; program/strategy by where the way goes plus a saved manual switch, v202; ground cards for hostile emotion among acceptance, up to three, v202/v204), each with FIRST MOVES (a line per way, v203), a 3D way through it (ways A notes, B firm ground, C support; fixed letters, v197), and keep/change/drop | How to read, Nothing you would do answers these yet, Does this answer it?, cards, Where the cards meet, More information needed, What you decided and why, References (v198: one list) |
| Footer (all pages) | IP footer statement + "Intellectual property statement" fold (formal statement), since v171 | — |

The 7 Mapping symbols are the seven question symbols, labeled already doing (Q.1), opposition, support, conditions, design, redesign and reinforce. A note takes its symbol's question number.

## 5. Emotion model (Vigneaux, 2026; Starratt painting)
Export index → emotion. The mapping is confirmed by the note content and matches the painting's color order:

| idx | Emotion | Color | Adoption potential (1 = best) | Terrain |
|---|---|---|---|---|
| 1 | Acceptance | teal | 1 | the highest ground |
| 3 | Indifference | yellow | 2 | **ridge**, the transitional crossing |
| 2 | Distrust | lavender | 3 | low ground |
| 0 | Aggression | red | 4 | lower ground |
| 4 | Defiance | deep ultramarine `#1b2a8f` (v171, matches the painting) | 5 | lowest ground |

Rules:
- Indifference is the emotion of transition. Most moves pass through it. It can also be a resting state.
- Transition cost is an energy gradient. Defiance→acceptance is rare and high-energy. Distrust↔acceptance costs more than indifference→acceptance.
- No emotion is stable, acceptance included.
- Strategies: **emotions-first** (for acceptance, indifference and transitional zones) and **behaviors-first** (for aggression, distrust and defiance: introduce the behavior without its label).

## 6. Terrain model (Pattern Synthesis 3D)
Legend [D]:
- Indifference = ridge · Distrust = low ground · Aggression = lower ground · Defiance = lowest ground.
- **Bare rock face**: two distant emotions meet with no indifference ridge between them. Crossing is a climb. Big moves cost energy; most moves go through indifference.
- Plain grass/soil/rock, no color = no notes nearby, so no information.
- Routes: **A** · its way through its notes; **B** · through its notes on firm ground only.
- Pins = notes in their emotion color · black flags = questions · present flag green · goal flag checkered (both since v171).
- Axes: ← PRESENT / FUTURE → along the front; ↑ HELP / ↓ HINDER back to front.
- **Indifference ridge must follow indifferent notes all the way**, even into another emotion's area [D]. (N31 currently adds color but no terrain.)
- Controls: drag to turn, scroll/pinch to zoom, hover/tap to inspect.
- Fullscreen must include the legend and the "The Bear Canyon Method · Operational Coherence" mark, with rotation and expansion [D].
- **Guided tours** (v208–v210, v219; in relief.js: startTour/stepTour/pauseTour/resumeTour/stopTour). Play opens full screen; one large Play/Pause at bottom center with End tour; captions 17/20 px held by reading time (3.3 words/s, 2.4–6 s a stop). Synthesis: READING THE GROUND (two stops, `D.intro` from `introStops(false)`), then every reading in WHAT THE GROUND SAYS. Analysis: a primer on the user's own notes (`introStops(true)`: high ground, ridge, bare rock, deepest ground, what a move costs). Captions never cite the paper [D 11-18].
- **Bare rock in the engine** (v210): `rockFaces()` replicates the relief's rock rule (two strongest emotions nearly balanced, ≥2 steps apart, neither indifference; indifference band included) to find the largest face for its reading.
- **Lines on the relief** (v213, v214): `hoses(spec)` draws a word's lines (thin black, or dashed red) from the In Parallel figure; `window.gsmSynRel`, `gsmSynHost`, and `gsmSynPend` (lines wait for the Synthesis 3D to mount).

### Terrain engine principles (adopted from the review)
- **Topological anchoring** — the goal, the PRESENT/FUTURE axes and the question flags are fixed anchors. A note edit triggers only local semantic relaxation, never a global re-layout, so the user's spatial memory survives.
- **Synthetic bridging** — a bare rock face is a design challenge, not a dead stop. The engine estimates the cost of building a transitional (indifference) bridge where no notes link the two sides.
- **Hysteresis** — crossing cost increases with the note's emotional lineage (entrenched vs. transient opposition).
- **Attractor basins** (Juarrero) — separate *trajectory optimization* (the cheapest path inside the current constraints) from *constraint reconfiguration* (changing the rules that make the basin). Ties to Q.4–Q.7.
- **Voice normalization** — weight voices so that a small but dense voice is not flattened by note count.

## 7. Spatial map (target architecture) [D, pending discussion]
- Each user/instance gets a unique 3D map generated from its ESRI spatial-map output. It reuses the same visual features as the emotion/terrain line-map viz and keeps place names.
- A simpler option for the Pattern Analysis view: an ESRI basemap with the goal, notes and emotions, without relief.
- Line map and spatial map may need different visualizations.

## 8. Threads and linking
- **Thread** [D]: a graph edge between notes/answers that share specific semantic tokens or are close in vector space, **across question boundaries (Q.1–Q.7)**. The engine today builds threads from shared words and two-word phrases. On screen: "a word or phrase that two or more answers or notes share", defined in place (v171) and in Start Here's glossary.
- **Pattern that runs through it** (Pattern Synthesis): a two-word phrase used in more than one note or answer, drawn as a loop on the 3D map when ticked.
- **Links**: user-made note↔note links, created on Mapping Landscape (`data.links`). These replace the old "what you linked" section, which belonged to the old figure.

## 9. Text engine
Current: stemmed unigrams and bigrams, a 352-entry stopword list, proper-noun handling, role-based scoring (v113+) ("liveli", "wildfi force", "putt fire"). Recurrence counts drive many findings.

Shipped (v172–v173):
- **Saturation filter** (v172): a stem in ≥40% of the pieces (goal, answers, notes; at least 10 pieces) that also heads ≥2 recurring bigrams is the medium. Its count is set to 1, so no finding, card or reading names the bare word; its phrases carry the meaning. `window.gsmMED` = {word: {n, of, subs, cnt}}.
- **ONE WORD, SEVERAL MEANINGS** (v172): the medium word's phrases sorted by side of the line (help/hinder/both).
- **Same-meaning declarations** (v173): `asks["same|A|B"] = "y"` rewrites A→B in the tokenizer input (`gsmSame` inside `Ht`), never in the displayed text. Asked only for two medium words where one contains the other. Split by default; merge only on the person's yes.
- **Story** (v173; opening rewritten v206): YOUR STORY SO FAR is generated prose (SY() in the Looking In builder). Since v206 the opening tells the context grasped (Q.1–Q.4 only) in order, quoting the notes: Q.1's most connected sentence, then what holds the goal back and what sits on the help side in the present, then what waits further on toward the goal (line map: x < 157 = present, y < 118 = helps; notes ranked by distance from the line, then emotion), then how help and hindrance are spread over time, and last the medium word's two jobs in one sentence. Place maps use the questions instead of position. The sections after it (What stands in the way …) draw on counts per question, emotion mix, voice, `gsmFR.it`, `gsmMED`, `gsmWS` and `gsmNR`.
- **Phrase-and-meaning layer** (v200–v201): `phBest`, `phClause`, `gsmPhTitle`, `gsmPurpose`, `gsmPhName`, `gsmSenses`, `phIn`, all wrapped in `phKeep` so the word tallies (`Mt`, `NmK`, `NmD`) don't move. No finding, card title, or theme is a lone word.
- **THE SAME THING?** (v205): shown as a prompt at the top of Pattern Analysis while unanswered (`window.gsmSameAsk`), with one sentence from the workbook for each word. Saves through `window.gsmSaveP` (a local `var P = []` near the IN THE WORDS builder hides the save function `P`; never call `P()` there).

Required behavior [D] (status):
1. **Semantic saturation filter** (✔ v172): a term found across nearly all of Q.1–Q.7 without differentiated emotional or structural context (e.g. "fire") is the medium, not a signal. Suppress it as a primary cluster node or require sub-phrase granularity.
2. **Co-occurrence neighborhood profiling** (✔ first form v172: bigram neighbors + side of the line; sliding window wider than two words still open): a sliding window tags each note's functional sub-type (fire → prescribed / unplanned / managed / mitigated / vilified / suppressed) before spatial placement or prose.
3. **Synonym families**: only by the person's declaration (✔ v173, THE SAME THING?).
4. Drop low-meaning tokens as findings ("involved", "necessary").
5. Recurrence is input to analysis, never a finding shown on its own.
6. **Lexical world-making** (optional, if clutter-free): prompt users to reframe generic terms.
7. **Perturbation audit** (optional): treat incoming notes, especially other voices, as perturbations to test against the terrain, not as instructions.

## 10. Action model (Taking Action)
Shipped v177: each way's route stats carry climb (energy), notes met by emotion, and effort / impact / benefit / return on effort (formulas in `docs/v177_update.md`). Readings per way say why to choose it; plus "Why take the harder way?", "When to stop and readjust" (Morin, 2008, p. 55) and an expandable bar chart.
Terrain module modes (one `mount`): Synthesis (default: readings, phrase loops, course model), `card` (Taking Action), `an` (Pattern Analysis: question filter + WHAT THIS SUGGESTS), `an`+`par` (In Parallel: question filter, no paragraph).

- 2–3 toggleable pathways to the same goal by different routes. Each has its rationale, how it differs, when to choose it, impact, benefit, effort (energy) and ROI, plus a comparison chart.
- **Strategy vs. program** (Morin): programs suit stable sequences; strategy is needed where the environment shifts. Actions escape their intent (ecology of action), so each pathway needs *watch signals* and a *stop-and-readjust point*.
- **Action friction field**: an action's energy cost depends on the emotional terrain it crosses.
- **Action grid: deleted** (v215) [D 11-18, his call: "I don't want the grid anywhere near this project"]. Not to be reintroduced in any form. MOVES, IN ORDER still reads each note's ease (its emotion and side of the line) from `gsmDerive`; nothing is drawn from it.
- **Synthesis→Action handoff**: a rule that turns a terrain vector (cost, height, emotional transition) into sequenced moves.
- **Reflexive loop**: logging or adjusting an action flags the upstream Q.1–Q.4 nodes and emotional contours it affects, and prompts re-synthesis.
- Constraint prompt: "What constraint or rule keeps this note in the low ground, and how do we change it?" Saves to `asks["cons|id"]`; nothing reads it yet (review 6h, Phase 2 step 8).
- Program or strategy [D 11-18]: a way from acceptance into distrust, aggression, or defiance, or one that crosses the help and hinder line, is a strategy (v202, `MixE` in `Fn`). The manual switch (`asks["mode|key"]`) wins in both directions.
- FIRST MOVES follows the way (v203, `wayMoves(k)` in the terrain module): the words follow the drawn way, not the other way round (measured; reordering the way made it far longer). Way A's zigzag is still open.

## 11. Data schema (export v1)
```
{ app:"groundsmith", v:1, saved:ISO, data:{
  goal: string,
  a: string[7],                        // answers Q.1–Q.7
  m: Note[],                           // notes
  p: { m: Marker[], c:[lat,lon,zoom] },// spatial (ESRI) map; markers [?]
  voices: string[],                    // e.g. "Mine", "Other wildfire professionals"
  links: [],                           // note↔note links [?] shape
  decisions: { "<KIND>|<term>": {d:int, w:string} },  // e.g. STRATEGY|fire
  others: [],                          // other perspectives (coworking) [?]
  who: string,                         // current author
  fig: { goal:{pos,hide,add}, hang:{pos,hide,add}, by, at },  // old figure layouts
  log: [{w, t, k, i, d}],              // edit log; k ∈ note+, notemove, notetext, noteemo, notesrc, notevoice, notetype
  asks: { "goal|<noteId>"|"theme|<stem>"|"resp|<noteId>"|"same|<a>|<b>": "y"|"n", "cons|<noteId>": string },  // confirmations; T5 answers (v187)
  sv: 2,                               // schema version (v191)
  wid: string,                         // workbook id, made once (v191)
  mt: { <noteId>: ISO },               // last edit per note, from the log (v191)
  gone: { <noteId>: ISO },             // deletions (v191)
  eh: { <noteId>: [[ISO|null, emotion], ...] },  // emotion history (v193)
  acts: [{k, t, w, x, n, l}],          // WHAT YOU DID per card (v194)
  remap: { <noteId>: ISO },            // notes flagged to re-map after acting (v194)
  // others: [{name, goal, a[7], at, wid}]  (at, wid since v191); lastCombine: {name, at, notes, places, links, upd, edits, gone}
  // p: { m: Marker[], c:[lat,lon,zoom], loc:{name,lat,lng,bb}, name }; Marker = [q, lat, lng, text, polygon[[lat,lng]]|null, emotion, source, voice, id, author?, extraVoices?]
  // links: [{f, t, r, w, src?, by?, at?}]
}}
Note = [q(1–7), x, y, text, null[?], emotionIdx, sourceIdx[?], voice, id, author?, extraVoices?]
```
- x ≈ 12–280 (PRESENT→FUTURE), y ≈ 43–210 (small = HELP / above the line) [I].
- `fig.goal` / `fig.hang` belong to the visualizations being retired. Keep import compatibility.

## 12. Coworking (schema ready, v191; F8 dashboards planned)
Several people give perspectives on the same data: authorship per note (index 9), `who`, `log.w`, `voices`, `others`. Since v191, each workbook has a `wid`, each note an edit time (`mt`) and deletions are kept (`gone`). Combine takes the newer edit of a shared note, removes notes the other person deleted from their own, and never removes yours.

### 12a. Project lead dashboards (F8) [D 11-17, planning only, no code]
Mockup: https://claude.ai/artifact/Dqy6xjxr4wPyGpKAf6hn4T. Costs write-up: https://claude.ai/artifact/4QdCsBzitJneX76CDjHuiL. All the wording in both is Claude's and has not been approved. Gregory expects about a month before it goes public. Estimate: 6–9 versions.

**The flow.**
- The opening page has three choices: On my own · Combine workbooks · Lead a project.
- **Lead a project:** the lead sets the project name and the goal everyone shares (only the lead can change it), the voices wanted (plus **Other**, which the person writes in; leads can also add their own), a date answers are due, and the map. The lead gets an invite link (copy, email or QR code).
- **Invited person:** opens the link and the workbook comes up with the lead's goal and map. They add a name and a voice. Saving is **live**: "Sharing with <lead> · saved N ago", with a Pause sharing button. While paused, work stays on the device. There is no Send button.
- **Dashboard ("Open a project I lead"):** live, like Google Forms. It shows:
  - a count of people started and working now, the voices heard, and the total notes;
  - a reading of what the group is telling you, with "Patterns suggests; you decide." said once there;
  - everyone's ground on one 3D relief, with a filter by voice;
  - WHERE THEY AGREE / WHERE THEY SPLIT, with bare rock faces between groups;
  - emotion by voice;
  - WHAT NOBODY HAS SAID YET;
  - EVERY WORKBOOK: a table listing each person's voice, questions answered, notes, main emotion and last change, with Open for each one and Remind for anyone who hasn't started;
  - an In Parallel comparison of any two people or voices;
  - a button that takes everyone to Taking Action.
- A file route stays as a fallback: a small "Add it" link on the dashboard, and Combine workbooks on the opening page.

**Backend [D]:** Google Firebase on the **Spark plan ($0)**. Never upgrade to Blaze without Gregory's say-so.
- Firebase project: "The Bear Canyon Method". Firestore (default) database in **nam5 (US)**, which can't be changed. Rules are locked (`allow read, write: if false`). No data. Scheduled backups are off.
- Web app registered as "BCM Preview". Firebase Hosting is not used; the site stays on GitHub Pages.
- Auth: Google sign-in, for project leads only. People answering need no account; the invite link is their key to that one project.
- Gregory holds the web config. **Never put it in chat, docs, memory or the repo until the build, and then only the page key, on purpose.**

**Before building:**
- The build check `grep -c 'AAPK\|AIza'` = 0 has to allow exactly the one Firebase web key. Restrict that key to the BCM sites in Google Cloud.
- Write the security rules: a lead reads only their own project; a person writes only their own workbook, and only in a project they hold the invite for.
- Set up App Check before going live.
- Use test data only until there is a privacy page (what is stored, where, who sees it, how to delete it; get a short legal look).
- Store each person's record in BCM's own workbook format (schema §11) so a later move off Firebase is easy.
- Save about every 30 seconds, not on every keystroke. If a free daily cap is hit (20K writes a day), keep work on the device and send it later.

**Open calls (Gregory):** who may lead a project (anyone, or approved people only); how long answers are kept and who can delete them; whether the file route stays for people who don't want to share live; which account owns the Firebase project long term.

## 13. UI rules
- No surprise phrasing; define every major term in place (popover or glossary).
- Narrative and visual lead; raw lists go in collapsible "View details" drawers.
- Touch: tap-to-inspect popovers (tap outside to dismiss). `touch-action:none` on 3D canvas wrappers, plus an Orbit Mode toggle and a touch helper.
- Fullscreen 3D: dockable, collapsible legend drawer with a translucent/blur backdrop. The same drawer opens when a Taking Action card goes full screen (v185); outside full screen, each card's legend sits under its map, on strategy and program cards alike.
- A visual must appear within ~1 screen of the top of analysis pages.
- Instructions on every page stay current with features.
- The terrain module's markup is shared by the Analysis map, the Synthesis map, In Parallel's earlier 3D, and the cards; gate anything new on ANH / PAR / CARDH (v217 lesson).
- Never rely on hover alone to carry meaning (v207).

## 14. Attribution / IP
- Footer, export, and formal statements: the texts are in the 11-17 review (§IP). The formal statement lives on an off-nav page linked from the footer.
- References block at the end of the workbook; page-specific references on Taking Action.

## 15. Terminology
See `BCM_CONCEPT_REGISTRY.md`.

## 16. Changes since Rev 8 (v196–v206, 11-17 to 11-18)
- v196: his wording review applied; serial comma everywhere.
- v197: the method's name under every 3D map; indifference joined into one yellow band; ways with fixed letters, one badge each, side by side where shared.
- v198: review wording: emotion definitions (direct quotes from Vigneaux, 2026) on every emotion button; Supports / Does Not Support; one REFERENCES list; NOTHING YOU WOULD DO ANSWERS THESE YET.
- v199: one derived-state pass (`gsmDerive`).
- v200–v201: the phrase-and-meaning layer (cards, findings, ONE WORD, SEVERAL MEANINGS).
- v202–v204: cards from the ground; the program/strategy rule and switch; FIRST MOVES per way; ground cards that don't decide what the emotion is aimed at.
- v205: Pattern Analysis reordered (first half); THE SAME THING? buttons fixed.
- v206: YOUR STORY SO FAR told as a story.
- In Parallel [D 11-18]: keeps its tab. The agreement figure (Analysis words in a column, hoses onto the Synthesis ground; black = agrees, white = raises a question) will close Pattern Synthesis; clicking a word draws its hoses on the 3D relief. The old In Parallel 3D retires behind a switch.
- The work queue is the 11-18 review plan (`claude/v196_review_plan.md` in the Claude project).

## 17. Changes since Rev 9 (v207–v219, 11-18)
- v207: card titles carry their context inline (`gsmHdT`); thread cards use `phCentral()`.
- v208–v209: the guided tour on Synthesis, with Pause/Play.
- v210: his tour notes: full screen on Play; big Play/Pause and End tour; bigger captions held by reading time; READING THE GROUND; a bare rock reading; WHAT THE GROUND SAYS reworded; a primer tour on Analysis; the Escape-in-full-screen bug fixed (the engine's `.pnet.fs` handler skips `.grel`); off-frame labels hidden.
- v211: WHAT IT PRODUCED with bigger themes (3d).
- v212: Synthesis step 7: patterns row above the map; the Supports questions only under PATTERNS; matches in bold; findings with no note link to their answers.
- v213: THE TWO PICTURES, SIDE BY SIDE (`gsmAgreeFig()`), first with hoses at the end of Synthesis; In Parallel's old 3D folded away.
- v214: drawn with lines [D 11-18 14:09]; box styles by what Analysis found; a key.
- v215: In Parallel opens with the figure; the action grid deleted [D 11-18 14:30]; MOVES, IN ORDER without grid wording.
- v216: In Parallel cut to the figure (`gsmIntOrder()`): Where to start, then the rest folded.
- v217: the patterns row only on the Synthesis map.
- v218: the patterns row stays in full screen (`D.onFs`).
- v219: no paper citation in either tour [D 11-18 15:21]; full screen for the figure with HOW TO READ IT.
