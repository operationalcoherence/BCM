# BCM_ARCHITECTURE.md
The Bear Canyon Method (BCM) — authoritative architecture
Rev 6 · 2026-11-17 (v191) · Sources: 11-17 review, workbook export 2026-11-13, Vigneaux (2026), repo operationalcoherence/BCM

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
- Persistence: JSON export/import (`bear-canyon-workbook-YYYY-MM-DD.json`). [?] Whether there is also local storage or a backend.
- Repo: `operationalcoherence/BCM` (public), served by GitHub Pages. The Webador page loads `gsm-preview.js` through a small stub. The live page `/gsmlive` is still the old pasted v92 and is never touched without his go-ahead.
- Files: `gsm-readable.js` (the source, ~19k lines, one IIFE plus the terrain module appended) → esbuild minify → `gsm-preview.js` (what the preview page runs). `gsm-relief.js` = `tools/relief/relief.js` + three.js r187, loaded on demand for the 3D map. The canvas map is the fallback.
- Place map: Leaflet + Esri tiles. The key lives only in the Webador stub (`window.GSM_ESRI_KEY`), never in the repo.
- Storage: localStorage key `groundsmith-web-v1`; save/open as JSON; workbooks can be combined.
- Tests: `tests/` (Playwright). `matrix.py` runs every tab of every workbook; `dump2.py` renders tabs to text; `mkwb.py` writes the synthetic workbooks (always include a non-wildfire one).
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
| Pattern Analysis (tab 2) | Analysis of notes and answers | Looking in: *Your story so far*, *Biggest gap*, What stands out, In the words, Possible patterns, Source, Voices |
| In Parallel (tab 6) | Analysis and the "tangle" read side by side (still uses the old petal and hang figures; Synthesis keeps the hang figure hidden for it) | Read together, Where they differ, Closest/farthest, Emotion, Voices, Patterns worth a second look |
| Pattern Synthesis (tab 3) | 3D terrain of emotion × structure | Looking out → How this map is made (fold) → About what you collected → The lay of the land: What the ground says (numbered readings) → 3D map → Patterns that run through it (phrase loops) → Model a course of action → Cause and effect, Now and later, Scale, One judgement twice, In your answers not on the map, Does this serve the goal?, What it might mean, What it rests on, What you linked, What to pay attention to |
| Taking Action (tab 4) | Program/strategy cards per area, each with first moves or a sequence, a 3D "way through it" (routes A and B), and keep/change/drop | Sources, How to read, No response yet, Does this answer it?, cards, Where the cards meet, More information needed, What you decided and why, References |
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
- **Story** (v173): YOUR STORY SO FAR is generated prose (SY() in the Looking In builder) from note counts per question, emotion mix per question and voice, `gsmFR.it` term categories, `gsmMED`, `gsmWS` and `gsmNR`.

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
- **Act-here / act-anywhere × easy / difficult** grid (axis.png): plots possible actions by energy and by reach (context-specific vs. universal). It sits before Taking Action (In Parallel) and feeds it.
- **Synthesis→Action handoff**: a rule that turns a terrain vector (cost, height, emotional transition) into sequenced moves.
- **Reflexive loop**: logging or adjusting an action flags the upstream Q.1–Q.4 nodes and emotional contours it affects, and prompts re-synthesis.
- Constraint prompt: "What constraint or rule keeps this note in the low ground, and how do we change it?"

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
  // others: [{name, goal, a[7], at, wid}]  (at, wid since v191); lastCombine: {name, at, notes, places, links, upd, edits, gone}
  // p: { m: Marker[], c:[lat,lon,zoom], loc:{name,lat,lng,bb}, name }; Marker = [q, lat, lng, text, polygon[[lat,lng]]|null, emotion, source, voice, id, author?, extraVoices?]
  // links: [{f, t, r, w, src?, by?, at?}]
}}
Note = [q(1–7), x, y, text, null[?], emotionIdx, sourceIdx[?], voice, id, author?, extraVoices?]
```
- x ≈ 12–280 (PRESENT→FUTURE), y ≈ 43–210 (small = HELP / above the line) [I].
- `fig.goal` / `fig.hang` belong to the visualizations being retired. Keep import compatibility.

## 12. Coworking (schema ready, v191)
Several people give perspectives on the same data: authorship per note (index 9), `who`, `log.w`, `voices`, `others`. Since v191, each workbook has a `wid`, each note an edit time (`mt`) and deletions are kept (`gone`). Combine takes the newer edit of a shared note, removes notes the other person deleted from their own, and never removes yours. Project administrator dashboards (F8) come later.

## 13. UI rules
- No surprise phrasing; define every major term in place (popover or glossary).
- Narrative and visual lead; raw lists go in collapsible "View details" drawers.
- Touch: tap-to-inspect popovers (tap outside to dismiss). `touch-action:none` on 3D canvas wrappers, plus an Orbit Mode toggle and a touch helper.
- Fullscreen 3D: dockable, collapsible legend drawer with a translucent/blur backdrop. The same drawer opens when a Taking Action card goes full screen (v185); outside full screen, each card's legend sits under its map, on strategy and program cards alike.
- A visual must appear within ~1 screen of the top of analysis pages.
- Instructions on every page stay current with features.

## 14. Attribution / IP
- Footer, export, and formal statements: the texts are in the 11-17 review (§IP). The formal statement lives on an off-nav page linked from the footer.
- References block at the end of the workbook; page-specific references on Taking Action.

## 15. Terminology
See `BCM_CONCEPT_REGISTRY.md`.
