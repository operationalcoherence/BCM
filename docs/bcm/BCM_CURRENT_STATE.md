# BCM_CURRENT_STATE.md
Rev 3 · 2026-11-17 · Preview at **v174** · Basis: 11-17 review, export 2026-11-13, repo

## Shipped
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

## Known bugs
| ID | Bug | Page |
|---|---|---|
| B8 | Other low-meaning words can still surface ("measures", "set", "human"); the stopword list is domain-free and grows only for words with no meaning in any field | Analysis, In Parallel |
| B9 | Fullscreen legend clips over map nodes (3D: fixed v171 with a drawer; canvas fallback unchanged) | Synthesis |
| B10 | Hover-only tooltips unusable on touch; canvas gestures fight page scroll | All 3D/hover |

## Active issues (quality)
- Most analysis is lists of data points without context. Story over list is the top-level fix.
- Engine granularity: "fire" is never split into prescribed / unplanned / managed / mitigated / vilified, and stemming loses phrase context.
- "Thread" is used everywhere but never defined.
- Unclear findings: "Not in Q.5–Q.7 yet (30)", "Condition (3)", "Q.5–Q.7 only (9)", "Areas to reinforce", "Grounded across the board", "Spread out", "Placed one way, tied the other", "The emotion changes", "Where they differ", the In Parallel "Tradition/reduce/involved" paragraph.
- Low-value sections: Top strategy, Top program, What it rests on (keep Source and Voices), What stands out, In the words, Condition.
- About 4 seconds of scrolling before the first visual on Pattern Analysis.
- "Behaviors first" is referenced without being explained.
- The minority voice (Other wildfire professionals, 5 notes) risks being flattened visually.
- Synthesis→Action gap: terrain insights don't turn into moves.
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
| D8 | Saturation set at 40% of answers and notes (min 10), with 2+ recurring phrases; voice-normalization weighting still open |
| D9 | Resolved v171: the per-question lines in WHAT IT RESTS ON were removed |
| D10 | Whether to include the optional lexical world-making / perturbation audit (only if clutter-free) |
| D11 | Resolved: the 7 symbols are the seven question symbols |

## Current priorities
3. Remaining Priority 1: U5 (his approval of redlines), A1 engine side (threads that cross question boundaries). Then Priority 2: V1/V2 new visuals on Analysis and In Parallel, Taking Action pathways (T1–T6), touch (U7), progressive disclosure (U8), N3/N4 story rewrites.
4. Carry the new visuals to Analysis and In Parallel; fullscreen legend and branding; touch support.
5. Taking Action pathways + Morin integration.
