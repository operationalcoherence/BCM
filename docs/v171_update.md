# v171 (preview only) — 2026-11-17

The first batch from Gregory's 11-17 review (`docs/bcm/BCM_TASK_QUEUE.md`, Priority 1).
All new wording is Claude's and is marked for his pass. His own text, such as the
IP statements and the reference list, is used exactly as he wrote it.

## How it was built (new workflow)

`gsm-readable.js` is now the source. It is edited, then minified with esbuild into
`gsm-preview.js`:

    npx esbuild@0.24 gsm-readable.js --minify --outfile=gsm-preview.js

The esbuild minify was tested on unchanged v170 first. It rendered byte-identical text
on every tab. Exact-string patching of the minified file is retired. The batch itself
is kept as a script: `tools/patches/v171_batch1.py`.

`gsm-relief.js` is rebuilt from `tools/relief/relief.js` with three@0.187.0:

    npm i three@0.187.0 esbuild@0.24
    npx esbuild tools/relief/relief.js --bundle --minify --format=iife --outfile=gsm-relief.js

## What changed

| Task | Change |
|---|---|
| U1 | "Mapping Change" is now **Mapping Landscape** everywhere: tab, heading, instructions, back links, Start Here. "the change map" → "the landscape map". |
| C1/B4 | Pattern Analysis AT A GLANCE drops PRESSING NOW ("fire in 22 places"), TOP STRATEGY, TOP PROGRAM, WHAT IT RESTS ON and WHAT YOU LINKED. Only BIGGEST GAP remains until the story rewrite (N2). |
| B5 | IN THE WORDS drops A NAME THAT RECURS. WHAT IT MIGHT MEAN drops the "136 words recur" count, the "In Q.5–Q.7" and "Condition" groups, "N of them tie back to the goal" and the "more of what recurs" line. |
| B6 | "Q.1 not already is answered but has no symbol on the map yet" now reads: "Q.1 (why the goal has not taken root) is answered, but no note on the map carries its symbol yet…", with what to do about it. |
| C2 | WHAT IT MIGHT MEAN: "Not in Q.5–Q.7 yet", "Q.5–Q.7 only" and "Areas to reinforce" say what they mean and what to do (reinforce = add a Q.7 note naming who keeps it going, with what, for how long). |
| C3 | "Behaviors first" and "emotions first" are explained in place, from Vigneaux (2026). The domain-specific "build toward the mitigation work" is now "what needs doing to reach the goal". |
| — | WHAT IT RESTS ON keeps Source, Voices and "X reads differently by voice". The per-question voice lines and "Q.4, Q.6, Q.7 have notes but none seen firsthand" are gone. |
| U4 | WHAT YOU LINKED is about linking notes on Mapping Landscape. "You moved N dots in the figures" is gone. |
| C5 | "Spread out" and "Leans on a few pieces" define a thread in place. "Grounded across the board" says what it means. |
| PS | THE EARLIER FIGURE fold is gone from Pattern Synthesis. The old figure is still built, hidden, because In Parallel still clones it until V2 replaces both In Parallel figures. |
| U6 | Pattern Synthesis order: HOW THIS MAP IS MADE at the top under LOOKING OUT. WHAT THE GROUND SAYS sits above the map. PATTERNS THAT RUN THROUGH IT (renamed from PHRASES THAT RUN THROUGH) sits directly under the map, open. |
| B1 | Ticking a pattern now draws its loop on the 3D map. Before this, the relief ignored the ticks. Loops are dark brown with a white edge, and the legend explains them. |
| U3 | Defiance is a deeper ultramarine, to match the Starratt painting (`#1b2a8f` in 2D; the 3D shade is kept dark). The present flag is green and labeled PRESENT. The goal is a checkered flag. |
| V3 (early) | 3D full screen shows the legend in a collapsible, blurred side drawer and "THE BEAR CANYON METHOD · BY OPERATIONAL COHERENCE". |
| C4 | "Like a cell turning toward what feeds it (Thompson, 2007)". |
| R1 | Kurtz & Snowden (2003) added to the Taking Action sources. A full REFERENCES list (his nine entries, exactly as given) sits at the end of the workbook, on Taking Action. |
| I1 | The footer carries his website statement, plus an "Intellectual property statement" fold with his formal statement. The PDF ends with his exported-files statement, and its page footer reads "free to use; attribution required". Saved workbook files carry the statement in a `notice` field. |
| — | Fixed a page error ("Cannot read properties of null (reading 'clientWidth')") that the new layout exposed in the canvas fallback's resize handler. |

## Checked

- `tests/matrix.py` on his 11-13 workbook and all 13 synthetic workbooks (clinic, hostile,
  200 notes, legacy, both maps…): no page errors, no script injection.
- `tests/dump2.py`: every tab read in full.
- Screenshots of Pattern Synthesis and Taking Action with the 3D module loaded
  (SwiftShader WebGL): loops draw, flags and colors show.
- No Esri key in any built file.

## For Gregory's pass

1. Every sentence listed under C2, C3, C5 and B6 above (Claude's wording).
2. Reference list: Juarrero (2023)'s subtitle is "How Constraints Create Coherence" (that is
   how your paper cites it); the review has "How constraints create change". Waldrop
   (1992)'s title begins "Complexity:". Both are used as you wrote them until you say.
3. "Old versions behind Taking Action": the old flat route chart only shows when 3D
   cannot load. Is that what you saw, or something else?
