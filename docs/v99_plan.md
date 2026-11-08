# v99 plan: figure clipping, the Pattern Synthesis rewrite, "feeling" → "emotion"

Written 2026-11-07, at v98. Nothing built yet. All wording below is Claude's.
Companions: `vocabulary_architecture.md`, `vocabulary_funnel.md`,
`engine_audit_v98.md`.

His standing instruction for this batch: **every change goes in the engine for
the general case, not for his workbook.** Measurements below come from his real
workbook only as evidence that the general bug exists.

## 1. The tangle figure is clipped (measured, general)

The `hang` figure's SVG viewBox is hardcoded `-24 -14 388 348` (x -24 to 364,
y -14 to 334) for every workbook. The loops are drawn from where the dots sit,
so the drawn extent varies. Measured at v98, Chromium, same build:

| Workbook | Drawn extent (x0,y0,x1,y1) | Clipped |
| --- | --- | --- |
| His real (2026-11-07, line map) | 12, -1, 352, **350** | 16 units off the bottom |
| Broadview (2026-11-05, place map) | 13, 15, 347, 333 | fits by 1 unit |
| Synthetic 24-note | 1, **-22**, **375**, 315 | top and right |

Full screen does not help: `#gsm .pnet.fs svg{height:100%}` scales the
already-clipped viewBox. Confirmed by screenshot at 1876x886 and 1326x770.

**Fix:** compute the viewBox from the union of the drawn geometry plus a
margin, instead of the constant. Correct for any workbook and any note count.
Also removes the asymmetric dead space on the left (content starts at x=12
inside a frame starting at -24).

Verify after the fix on all three workbooks above, line map and place map.

## 2. Pattern Synthesis is too long (his words: "too long")

Measured on his workbook: the whole page renders to **1,947 words**. Inside it:

- "What this suggests" (the tangle reading): **478 words**, 12 labelled
  paragraphs - The center, The tangle, Bridges, In Q.1-Q.4 not in Q.5-Q.7,
  In Q.5-Q.7 not in Q.1-Q.4, Help and hinder, Feeling, Voices x2, Outliers,
  Where to look first.
- "WHAT IT MIGHT MEAN": **347 words**, 18 items.

Both are flat lists of every finding at equal weight. This is the Layer 1
problem (score and select) arriving from the other direction.

### What he asked the page to become

Key points; takeaways; theories of patterns; **patterns needed to reach the
goal**; **patterns that reach the goal**; "make it important, surprisingly deep
insights."

### The signals already exist, buried

Both of his named sections are already computed and shown as minor lines:

- *Patterns that reach the goal* - the existing line "18 of them tie back to
  the goal (managing unplanned, unplanned fire, aggressive suppression, good
  fire)", currently near the bottom of WHAT IT MIGHT MEAN.
- *Patterns needed to reach the goal* - the existing buckets "Not in Q.5-Q.7
  yet (13)", "Condition (1)" and "Unused support (8)". The page already
  concludes "those 14 are where Q.5-Q.7 are thinnest" and then buries it.

So the rewrite is mostly selection and ordering, not new computation. Proposed
shape, three or four blocks at full weight and everything else folded:

1. What reaches the goal.
2. What the goal needs and does not have.
3. One or two deep readings (below).
4. Where to look first.

### A finding family that produces the depth he is asking for

**Heavy overlap, opposite emotion.** Two threads that run through many of the
same dots but carry different leading emotions. Domain-free rule; no word list.

Measured on his workbook from the engine's own thread data:

| Thread | Dots | Leading emotion |
| --- | --- | --- |
| fire | 19 | acceptance |
| good fire | 10 (a complete subset of *fire*) | acceptance |
| wildfire | 16 | aggression |
| suppression | 13 | aggression |
| aggressive | 8 | aggression |
| force | 7 | aggression |

*fire* and *wildfire* share 11 dots - 69% of everywhere *wildfire* appears -
and lead with opposite emotions. His workbook's stated goal is the distinction
between a suppression vocabulary and an ecological one; that distinction is
measurable in his own writing and the page does not currently say so.

The rule generalizes: in any workbook, two heavily-overlapping threads with
opposing emotion marks a split in how the person feels about one subject
depending on which word they reach for. Related existing rules to rank
alongside it: THE FEELING CHANGES (same word, different emotion across
Q.1-Q.4 vs Q.5-Q.7) and ONE IDEA UNDER TWO NAMES.

Ranking for which blocks run at full weight: surprise, reach, consequence
(bears on Q.5-Q.7 or the goal), corroboration - as set out in the evaluation
document's Layer 1, with the correlation discount that `engine_audit_v98.md`
defect 6 requires.

## 3. "feeling" -> "emotion" (his instruction)

19 occurrences of feeling/Feeling in the built file. The page is currently
inconsistent with itself: the header says "23 with emotion" and WHAT IT MIGHT
MEAN says "Emotional disposition", while the tangle reading says "Feeling" and
"the same feeling everywhere". Change every one to emotion/Emotion, including
the "Feeling" section heading and the "Feeling read on N of N notes" line.
Check the PDF walker for the same strings. The synonym-interface mockup uses
"Feeling" on its Entry screen and needs the same change.

## 4. Found on the way: one British spelling

`"One feeling may be colouring more of the workbook than you meant."` ->
"coloring". His standing rule is American spelling; he has called British
spelling in the workbook the biggest error. ("realistic" elsewhere is correct
and stays.)

## Decided 2026-11-07, 20:57

Asked directly, he chose:

- **Scope: all of it, synthesis rewrite included.** v99 carries the four
  measured fixes, the engine changes (proper nouns visible, the -ly adjective
  fix, stopword cleanup, PRESENT-FUTURE findings, the emotion/placement
  redundancy finding), and the Pattern Synthesis rewrite.
- **Length: one screen, no scrolling.** Roughly 150-250 words at full weight,
  three or four blocks, everything else behind folds. Nothing is deleted.

Build order, so the safe part can be looked at first: the four measured fixes
ship as one push, the engine changes and the synthesis rewrite as a second.

The build was stopped before it started - he called it a night at 20:59. None
of the code changes below exist yet. Everything in this repository at this
point is documentation and the readable source; `gsm-preview.js` is still v98
untouched, so the preview page is unchanged.

### First step when picking this up

Prove the rebuild path before editing anything: minify the unchanged
`gsm-readable.js` with esbuild, and confirm it renders identical page text to
`gsm-preview.js` on the real workbook across all four reading tabs. Only then
start editing the readable file. Baseline captures for five workbooks were
being generated for exactly this comparison. If the round trip does not come
out clean, fall back to exact-string patching of `gsm-preview.js`, which is how
v95-v98 were made.

## Not yet settled

- Whether the bottom clipping he saw on screen matches the 16 units measured
  here, or whether his screen shows more.
- Whether the folded remainder keeps all 12 paragraphs or drops some.
- All new synthesis wording will be Claude's and needs his pass.
