# BCM_TASK_QUEUE.md
Rev 7 · 2026-11-18 (v227) · Source: 11-17 review, then the 11-18 review plan · ✔ = shipped (version)

Categories: BUG · UI · VIZ · ENG · CONTENT · NARR · ARCH · RES · FUT
Page keys: GLB (all) · MAP (Mapping Landscape) · PA (Pattern Analysis) · PAR (In Parallel) · PS (Pattern Synthesis) · TA (Taking Action)
Source: repo operationalcoherence/BCM (attached 2026-11-17).

## Current queue (11-18): the v196 review plan
The live queue is claude/v196_review_plan.md in the Claude project (it quotes his workbook, so it stays private). Status at v219:
- Phase 1 (v197–v203): done.
- Phase 2: step 6, Pattern Analysis (v205–v207, v211): done. Step 7, Pattern Synthesis (v212, v217, v218): done. Step 10, In Parallel (v213–v216, v219): done.
- Interpretation pass (v220–v225): done for Analysis and In Parallel.
- ✔v226 **Step 8, Taking Action:** rebuilt around the central test.
  - ✔ THE TEST panel.
  - ✔ Strategies seeded from the system that holds, the key tension, and the loop.
  - ✔ Programs seeded from the opportunity, what is already helping, and support not yet reinforced.
  - ✔ Ways through the ridge before bare rock, with the cost of each move and the emotional movement.
  - ✔ Split readings carried onto cards.
  - ✔ Constraint → card → WHAT YOU DID → re-map, with one tap to Q.4, Q.6, or Q.7.
  - ✔ Strategies grouped, programs grouped, the chart open, and every field explained.
  - ✔ One references list (already done in v198).
- ✔v227 The constraint loop made visible: buttons shown before typing; the constraint shown on its note on Mapping Landscape.
- Proposed 11-18 21:31, waiting for his yes: the Taking Action hierarchy pass (decision, explanation, evidence layers).
- **Next:** a short check of Taking Action only, then **step 9, Mapping Context** (instruction drop-down, emotion definitions where notes are written, Start here text moved to its pages, his redlines).
- Open from v226, his calls: the redlines on its wording; whether word-only cards should stay folded; merging word cards that repeat a seeded card.
- Phase 3: WebM download of the tour; captions from his confirmed meanings of the four acts; YOUR OWN WORDS strip (3g); the word-budget pass; the "no questions" map click (3c).
- The guided tour (4c): built v208–v210, v219.

The tables below are the 11-17 review's queue, kept for history.

---

## Priority 1

| ID | Task | Cat | Impacts | Depends |
|---|---|---|---|---|
| ✔v172 E1 | Semantic saturation filter: suppress medium terms ("fire") as findings/cluster nodes or force sub-phrase granularity | ENG | engine, PA, PAR, PS | — |
| ✔v172 E2 | Co-occurrence neighborhood profiling: tag note functional sub-type (fire → prescribed/unplanned/managed/mitigated/vilified/suppressed) | ENG | engine, all analysis, terrain | — |
| ✔v173 E3 | Synonym family fire ≡ wildfire, split by sub-type; remove duplicate fire/wildfire prose | ENG | engine, PA, PS | E2, D2 |
| ✔v172 E4 | Low-meaning token filter ("involved", "necessary"); recurrence becomes input only, never a standalone finding | ENG | engine, PA, PAR, PS | — |
| ✘ T4b | Action grid redesign: **dropped.** All mocked options were rejected 11-17, and on 11-18 he removed the grid from the project ("I don't want the grid anywhere near this project"); deleted in v215 | — | — | — |
| ✔v196 R1 | His wording review of v171–v195 applied; serial comma everywhere. Rows 34–35 still open | COPY | all pages | — |
| A1 (part ✔v171) | Define "thread" (cross-question graph edge by shared tokens/vector proximity) in engine and UI, with a plain-language popover | ARCH | engine, PAR, PS, glossary | — |
| ✔v173 N1 | Rewrite PA "Your story so far" as a 2–3 paragraph story with headings (What stands in the way · What is already helping · What has to be true · What you would do · Where to start · Not yet answered); keep note/question popovers; give meta-meaning | NARR | PA | E1–E4 |
| ✔v173 N2 | Rewrite PA "Biggest gap" as a story (fold its 9 headings in); make "Not in Q.5–Q.7 yet", "Condition", "Q.5–Q.7 only" meaningful or drop them | NARR | PA | E1–E4 |
| ✔v171 B1 | Fix the PS "Patterns that run through it" loop toggle | BUG | PS | — |
| ✔v174 B2 | Taking Action cards fell back to flat charts (v171 regression); 3D restored | BUG | TA | — |
| ✔v173 B3 | Indifference ridge follows indifferent notes across emotion areas (N31) | BUG | PS terrain | — |
| ✔v171 B4 | Remove "fire in 22 places" | BUG | PA | E1 |
| ✔v171 B5 | Remove repeated words in "Biggest gap" and recurrence lines (PA "In the words": list once at most; PS "What it might mean") | BUG | PA, PS | — |
| ✔v171 B6 | Fix or remove "Q.1 not already is answered…" | BUG | PA | — |
| ✔v171 C1 | PA removals: Top strategy, First moves (→ TA), Top program, "What it rests on" (keep Source, Voices), "necessary" pattern | CONTENT | PA, TA | — |
| ✔v171 C2 | PS "What it might mean": keep For/against and Unused support; narrativize Q.5–Q.7 only; drop Condition and the rest; say *how* to reinforce in "Areas to reinforce" (e.g. add a note) | CONTENT | PS | E4 |
| ✔v171 C3 | Explain "behaviors first" in place (popover/pop-out) from Vigneaux (2026); also emotions-first | CONTENT | PS, glossary | — |
| ✔v171 C4 | Cite (Thompson, 2007) on "Where it is easiest to get to" (cell turning toward what feeds it) | CONTENT | PS | — |
| ✔v171 C5 | Define or rewrite "Spread out", "Grounded across the board" | CONTENT | PS | A1 |
| ✔v171 U1 | Rename page and instructions to "Mapping Landscape" | UI | MAP, nav, instructions | — |
| ✔v173 U2 | Hover/tap explainer for each of the 7 symbols | UI | MAP | D11 |
| ✔v171 U3 | Defiance → darker blue (painting); present flag green; goal flag checkered | UI | MAP, PS, legends | — |
| ✔v171 U4 | Replace "what you linked" with note-linking; add linking to the MAP instructions | UI | PA, MAP | — |
| U5 | Update all page instructions to match current features: redlines proposed in docs/v173_update.md, waiting for his approval (his text) | CONTENT | GLB | his approval |
| ✔v171 U6 | PS layout: "How this map is made" at top under Looking out; "What the ground says" above the viz (under About what you collected); "Patterns that run through it" directly under the viz | UI | PS | B1 |
| ✔v171 R1 | Add references: TA (Kurtz & Snowden 2003; Morin 2008); full end-of-workbook reference list (Ackoff, Juarrero, Kurtz & Snowden, Morin, Morin & Kern, Paci-Green et al., Thompson, Vigneaux, Waldrop) | RES | TA, GLB | D4, D5 |
| ✔v171 I1 | Footer IP statement + link to the formal IP page (off-nav); IP statement on exported files/reports | CONTENT | GLB, export | D3 |

## Priority 2

| ID | Task | Cat | Impacts | Depends |
|---|---|---|---|---|
| ✔v175 (line map) V1 | Bring the new 3D viz to PA (line-map version now; spatial version via ESRI basemap with goal/notes/emotions, no relief) | VIZ | PA | — |
| ✔v176, superseded v213–v216 V2 | Replace both In Parallel visualizations (In Parallel is now THE TWO PICTURES, SIDE BY SIDE); rewrite "Read together", "Where they differ", "Closest/farthest" for the new visuals | VIZ/NARR | PAR | V1 |
| V3 (✔v171, drawer fix v178, Taking Action cards v185) | Fullscreen: legend + "The Bear Canyon Method · Operational Coherence", rotation/expansion; legend as dockable, collapsible blur drawer | VIZ/UI | PS, PA | — |
| ✔v175 V4 | Visual within ~1 screen on PA; rewrite "What this suggests" against the new visual | UI/NARR | PA | V1 |
| ✔v183 V5 | Voice normalization weight so the minority voice isn't flattened in terrain or prose | ENG/VIZ | engine, PS, PAR | D8 |
| ✔v182 U7 | Touch: tap-to-inspect popovers, tap-outside dismiss, `touch-action:none` on canvases, Orbit Mode toggle + touch helper | UI | GLB | — |
| ✔v182 U8 | Progressive disclosure: raw lists/gap metrics in "View details" accordions; narrative and visual lead | UI | PA, PAR, PS | N1, N2 |
| ✔v182–183 N3 | PA story rewrites: What stands out (implications or delete); Possible patterns (name the emotion, widen context); Q-sections lacking meaning (Q2–Q7, D9) | NARR | PA | E1–E4 |
| ✔v180 N4 | PAR story rewrites: Emotion (expand into story; emotion is the method's cornerstone); "Two people, two sides" (beyond the obvious); "Placed one way…", "The emotion changes" (meaning to the user); fix the "Tradition/reduce/involved" paragraph | NARR | PAR | E1–E4, V2 |
| ✔v177 T1 | TA: 2–3 toggleable pathways, same goal, different routes; each with rationale, difference, when to choose, impact, benefit, effort/energy | ENG/UI | TA | D7 |
| ✔v177 T2 | TA "Comparing the ways" depth: why take the harder route; when to stop and readjust (watch signals); integrate Morin (2008) ecology of action and strategy vs. program, cited | NARR/RES | TA | T1, D6 |
| ✔v177 T3 | TA comparison chart (expandable bar/radial/line): effort, impact, benefit, ROI per pathway | VIZ | TA | T1 |
| ✘ T4 | Act-here/anywhere × easy/difficult action grid: built v179, **deleted v215** (his call, 11-18) | — | — | — |
| ✔v187 T5 | Constraint prompt on TA: "What constraint or rule keeps this note in the low ground, and how do we change it?"; distinguish trajectory optimization from constraint reconfiguration (Juarrero), linked to Q.4–Q.7 | ENG/NARR | TA, PS | — |
| ✔v181 T6 | Synthesis→Action handoff rule: terrain vector (cost, height, transition) → sequenced moves | ENG | PS, TA | T1 |
| ✔v191 A2 | Coworking-ready schema: per-note authorship, multi-perspective merge, `others` structure (no dashboards yet) | ARCH | schema, export | — |
| ✔v188 G1 | Glossary/term popovers for every major term (thread, ridge, bare rock face, voice, low ground…) | UI/CONTENT | GLB | A1 |

## Priority 3

| ID | Task | Cat | Impacts | Depends |
|---|---|---|---|---|
| F1 | Per-instance 3D map generated from ESRI spatial output; same visual features as the line-map terrain; keep place names | FUT/VIZ | MAP, PA, PS | D1 |
| F2 | Topological anchoring + local semantic relaxation (goal, axes, Q flags fixed) | ENG | terrain | F1 (applies to the current terrain too) |
| ✔v192 F3 | Action friction vector field: dynamic energetic ROI across emotional terrain; boomerang risk | ENG | TA, PS | T1, T6 |
| ✔v194 F4 | Reflexive loop: logging/adjusting an action flags affected Q.1–Q.4 nodes and contours, prompts re-synthesis | FUT/ENG | TA → PA/PS | T1, A2 |
| ✔v192 F5 | Synthetic bridging cost across bare rock faces | ENG | PS, TA | F3 |
| ✔v193 F6 | Hysteresis: historical friction from emotional lineage (uses the edit log) | ENG | PS, TA | F3 |
| ✔v195 F7 | Lexical world-making prompts + perturbation audit mode (only if clutter-free) | FUT/RES | engine, MAP, PA | E2, D10 |
| F8 (LAST — remind Gregory) | Project lead dashboards: live collection (Firebase, set up 11-17), invite links, Other voice, every-workbook list, Combine on the opening page. Plan in ARCHITECTURE §12a | FUT | new, backend | A2 |
