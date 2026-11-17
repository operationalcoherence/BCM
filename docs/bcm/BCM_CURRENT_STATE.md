# BCM_CURRENT_STATE.md
Rev 3 · 2026-11-17 · Preview at **v184** · Basis: 11-17 review, export 2026-11-13, repo

## Shipped
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
- Place-map-only workbooks (e.g. Broadview) get no 3D landscape; the Esri place ground is the next build (see BCM_HANDOFF.md).

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
- Synthesis→Action: ways costed (v177) and sequenced (v181). Still a rule of thumb, not the friction field (F3).
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
| D1 | Per-instance 3D spatial map from ESRI output: approach, generator, anchoring (user wants to discuss) |
| D2 | Resolved v172–v173: medium words are split by the person's own phrases; fire ≡ wildfire only on his Yes to THE SAME THING? |
| D3 | Formal IP statement: now a footer fold (v171). Move it to its own off-nav website page? |
| D4 | Resolved v174: "How constraints create coherence" |
| D5 | Resolved v174: "Complexity: The emerging science…" |
| D6 | Morin quote typo "andA" → "and" |
| D7 | 2 or 3 pathways by default on Taking Action |
| D8 | Saturation 40% (min 10 pieces, 2+ phrases); voice weighting √(mean/size) clamped 0.6–1.8, on by default (v183): on, or a switch? |
| D9 | Resolved v171: the per-question lines in WHAT IT RESTS ON were removed |
| D10 | Whether to include the optional lexical world-making / perturbation audit (only if clutter-free) |
| D11 | Resolved: the 7 symbols are the seven question symbols |

## Current priorities
3. Remaining Priority 1: U5 (his approval of redlines), A1 engine side (threads that cross question boundaries). Priority 2 remaining: T5 (constraint prompt), A2 (coworking schema), G1 (glossary popovers), V1 place-map version (waits on D1).
4. Carry the new visuals to Analysis and In Parallel; fullscreen legend and branding; touch support.
5. Taking Action pathways + Morin integration.
