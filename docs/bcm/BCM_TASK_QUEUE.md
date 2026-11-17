# BCM_TASK_QUEUE.md
Rev 2 · 2026-11-17 · Source: 11-17 review · ✔ = shipped (version)

Categories: BUG · UI · VIZ · ENG · CONTENT · NARR · ARCH · RES · FUT
Page keys: GLB (all) · MAP (Mapping Landscape) · PA (Pattern Analysis) · PAR (In Parallel) · PS (Pattern Synthesis) · TA (Taking Action)
Source: repo operationalcoherence/BCM (attached 2026-11-17).

---

## Priority 1

| ID | Task | Cat | Impacts | Depends |
|---|---|---|---|---|
| E1 | Semantic saturation filter: suppress medium terms ("fire") as findings/cluster nodes or force sub-phrase granularity | ENG | engine, PA, PAR, PS | — |
| E2 | Co-occurrence neighborhood profiling: tag note functional sub-type (fire → prescribed/unplanned/managed/mitigated/vilified/suppressed) | ENG | engine, all analysis, terrain | — |
| E3 | Synonym family fire ≡ wildfire, split by sub-type; remove duplicate fire/wildfire prose | ENG | engine, PA, PS | E2, D2 |
| E4 | Low-meaning token filter ("involved", "necessary"); recurrence becomes input only, never a standalone finding | ENG | engine, PA, PAR, PS | — |
| A1 | Define "thread" (cross-question graph edge by shared tokens/vector proximity) in engine and UI, with a plain-language popover | ARCH | engine, PAR, PS, glossary | — |
| N1 | Rewrite PA "Your story so far" as a 2–3 paragraph story with headings (What stands in the way · What is already helping · What has to be true · What you would do · Where to start · Not yet answered); keep note/question popovers; give meta-meaning | NARR | PA | E1–E4 |
| N2 | Rewrite PA "Biggest gap" as a story (fold its 9 headings in); make "Not in Q.5–Q.7 yet", "Condition", "Q.5–Q.7 only" meaningful or drop them | NARR | PA | E1–E4 |
| ✔v171 B1 | Fix the PS "Patterns that run through it" loop toggle | BUG | PS | — |
| B2 | Remove old Taking Action versions: needs his clarification (old route chart is only a fallback) | BUG | TA | his answer |
| B3 | Indifference ridge follows indifferent notes across emotion areas (N31) | BUG | PS terrain | — |
| ✔v171 B4 | Remove "fire in 22 places" | BUG | PA | E1 |
| ✔v171 B5 | Remove repeated words in "Biggest gap" and recurrence lines (PA "In the words": list once at most; PS "What it might mean") | BUG | PA, PS | — |
| ✔v171 B6 | Fix or remove "Q.1 not already is answered…" | BUG | PA | — |
| ✔v171 C1 | PA removals: Top strategy, First moves (→ TA), Top program, "What it rests on" (keep Source, Voices), "necessary" pattern | CONTENT | PA, TA | — |
| ✔v171 C2 | PS "What it might mean": keep For/against and Unused support; narrativize Q.5–Q.7 only; drop Condition and the rest; say *how* to reinforce in "Areas to reinforce" (e.g. add a note) | CONTENT | PS | E4 |
| ✔v171 C3 | Explain "behaviors first" in place (popover/pop-out) from Vigneaux (2026); also emotions-first | CONTENT | PS, glossary | — |
| ✔v171 C4 | Cite (Thompson, 2007) on "Where it is easiest to get to" (cell turning toward what feeds it) | CONTENT | PS | — |
| ✔v171 C5 | Define or rewrite "Spread out", "Grounded across the board" | CONTENT | PS | A1 |
| ✔v171 U1 | Rename page and instructions to "Mapping Landscape" | UI | MAP, nav, instructions | — |
| U2 | Hover/tap explainer for each of the 7 symbols | UI | MAP | D11 |
| ✔v171 U3 | Defiance → darker blue (painting); present flag green; goal flag checkered | UI | MAP, PS, legends | — |
| ✔v171 U4 | Replace "what you linked" with note-linking; add linking to the MAP instructions | UI | PA, MAP | — |
| U5 | Update all page instructions to match current features | CONTENT | GLB | follows each change |
| ✔v171 U6 | PS layout: "How this map is made" at top under Looking out; "What the ground says" above the viz (under About what you collected); "Patterns that run through it" directly under the viz | UI | PS | B1 |
| ✔v171 R1 | Add references: TA (Kurtz & Snowden 2003; Morin 2008); full end-of-workbook reference list (Ackoff, Juarrero, Kurtz & Snowden, Morin, Morin & Kern, Paci-Green et al., Thompson, Vigneaux, Waldrop) | RES | TA, GLB | D4, D5 |
| ✔v171 I1 | Footer IP statement + link to the formal IP page (off-nav); IP statement on exported files/reports | CONTENT | GLB, export | D3 |

## Priority 2

| ID | Task | Cat | Impacts | Depends |
|---|---|---|---|---|
| V1 | Bring the new 3D viz to PA (line-map version now; spatial version via ESRI basemap with goal/notes/emotions, no relief) | VIZ | PA | — |
| V2 | Replace both In Parallel visualizations; rewrite "Read together", "Where they differ", "Closest/farthest" for the new visuals | VIZ/NARR | PAR | V1 |
| V3 (part ✔v171) | Fullscreen: legend + "The Bear Canyon Method · Operational Coherence", rotation/expansion; legend as dockable, collapsible blur drawer | VIZ/UI | PS, PA | — |
| V4 | Visual within ~1 screen on PA; rewrite "What this suggests" against the new visual | UI/NARR | PA | V1 |
| V5 | Voice normalization weight so the minority voice isn't flattened in terrain or prose | ENG/VIZ | engine, PS, PAR | D8 |
| U7 | Touch: tap-to-inspect popovers, tap-outside dismiss, `touch-action:none` on canvases, Orbit Mode toggle + touch helper | UI | GLB | — |
| U8 | Progressive disclosure: raw lists/gap metrics in "View details" accordions; narrative and visual lead | UI | PA, PAR, PS | N1, N2 |
| N3 | PA story rewrites: What stands out (implications or delete); Possible patterns (name the emotion, widen context); Q-sections lacking meaning (Q2–Q7, D9) | NARR | PA | E1–E4 |
| N4 | PAR story rewrites: Emotion (expand into story; emotion is the method's cornerstone); "Two people, two sides" (beyond the obvious); "Placed one way…", "The emotion changes" (meaning to the user); fix the "Tradition/reduce/involved" paragraph | NARR | PAR | E1–E4, V2 |
| T1 | TA: 2–3 toggleable pathways, same goal, different routes; each with rationale, difference, when to choose, impact, benefit, effort/energy | ENG/UI | TA | D7 |
| T2 | TA "Comparing the ways" depth: why take the harder route; when to stop and readjust (watch signals); integrate Morin (2008) ecology of action and strategy vs. program, cited | NARR/RES | TA | T1, D6 |
| T3 | TA comparison chart (expandable bar/radial/line): effort, impact, benefit, ROI per pathway | VIZ | TA | T1 |
| T4 | Act-here/anywhere × easy/difficult action grid (axis.png style) on PAR, feeding TA | VIZ/ENG | PAR, TA | T1 |
| T5 | Constraint prompt on TA: "What constraint or rule keeps this note in the low ground, and how do we change it?"; distinguish trajectory optimization from constraint reconfiguration (Juarrero), linked to Q.4–Q.7 | ENG/NARR | TA, PS | — |
| T6 | Synthesis→Action handoff rule: terrain vector (cost, height, transition) → sequenced moves | ENG | PS, TA | T1 |
| A2 | Coworking-ready schema: per-note authorship, multi-perspective merge, `others` structure (no dashboards yet) | ARCH | schema, export | — |
| G1 | Glossary/term popovers for every major term (thread, ridge, bare rock face, voice, low ground…) | UI/CONTENT | GLB | A1 |

## Priority 3

| ID | Task | Cat | Impacts | Depends |
|---|---|---|---|---|
| F1 | Per-instance 3D map generated from ESRI spatial output; same visual features as the line-map terrain; keep place names | FUT/VIZ | MAP, PA, PS | D1 |
| F2 | Topological anchoring + local semantic relaxation (goal, axes, Q flags fixed) | ENG | terrain | F1 (applies to the current terrain too) |
| F3 | Action friction vector field: dynamic energetic ROI across emotional terrain; boomerang risk | ENG | TA, PS | T1, T6 |
| F4 | Reflexive loop: logging/adjusting an action flags affected Q.1–Q.4 nodes and contours, prompts re-synthesis | FUT/ENG | TA → PA/PS | T1, A2 |
| F5 | Synthetic bridging cost across bare rock faces | ENG | PS, TA | F3 |
| F6 | Hysteresis: historical friction from emotional lineage (uses the edit log) | ENG | PS, TA | F3 |
| F7 | Lexical world-making prompts + perturbation audit mode (only if clutter-free) | FUT/RES | engine, MAP, PA | E2, D10 |
| F8 | Project administrator dashboards | FUT | new | A2 |
