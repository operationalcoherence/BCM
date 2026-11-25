# v266 · The simple Pattern Synthesis page

His call 11-24: build only the relationship graph, shape detection, and a simple page using their outputs; the question engine waits. His go-ahead 20:43: "then, build the simple page". Design: claude/pattern_synthesis_minimal_page_2026-11-24.md in the Claude project.

## What changed
- Two new blocks at the top of Pattern Synthesis, under 2 · LOOKING OUT:
  - **WHAT CHANGED WHAT**: the strongest single relationship the graph finds (stated over placed; inferred never leads).
  - **WHAT KEEPS ITSELF GOING** (a loop), **WHAT HOLDS IT IN PLACE** (a settlement), or **WHERE IT IS HEADING** (an open chain): the strongest shape.
- Each block: one line of meaning, a short explanation, and one line of evidence (note numbers, linked, and how sure the reading is in plain words: "The workbook says this directly", "Shown by the order and wording of the notes", "You drew this yourself", or "One step rests on a single shared word, so it needs your answer").
- Notes are described by what they are and where they stand (emotion, side, stretch). What ties them is named only as wording two differently worded parts share, as the person wrote it; emotion words are never used as that wording.
- Code: tools/graph/page.js, on top of tools/graph/graph.js and shapes.js. The engine change is two lines (it hands the graph its own stopwords; it calls the page after Synthesis renders).
- **Build changed:** the three modules are bundled ahead of the engine:
  `cat tools/graph/graph.js tools/graph/shapes.js tools/graph/page.js gsm-readable.js | npx esbuild@0.24 --minify --loader=js > gsm-preview.js`
  Built the old way, the page simply doesn't appear; nothing breaks.

## What did not change
Everything else on Pattern Synthesis stays, under the new blocks. Analysis, In Parallel, and Taking Action read word for word the same as v265 (dump2 on 11-20). No 3D change.

## Known weaknesses (said, not hidden)
- The explanations are rule-written. They are accurate to the graph but read stiffly ("acceptance on the hinder side, midway").
- They inherit the graph's word ties. On Good fire the chain's first step rests on "fire-adapted"; on Broadview the tie is "work" and "place" (from "taking place").
- The 11-20 loop rests on one phrase, "command and control", three times.
- No question block, by his call. Where a shape has an inferred step, the page says that step is open until he answers.

Tests: tests/graph_pass.js (18 of 22, the 4 known misses), tests/shapes_pass.js (all pass), dump2.py on 11-20, Good fire, and Broadview. Key check: 0.
