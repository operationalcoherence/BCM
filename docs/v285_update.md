# v285 — tidy for market, first pass

His call, 25 Nov 2026 18:31: "start preparing the pages for market. Delete repeats, consolidate where possible, tidy up, make engine fixes, focus on UI." Engine fixes only; none of his own text changed. Patch: `tools/patches/v285_market_tidy.py`.

## Fixed (every workbook)
1. **IN YOUR ANSWERS, NOT ON THE MAP** never asks the same phrase twice (11-20 asked "emergent situations" twice).
2. **The Q.5–Q.7 lists** (Not in Q.5–Q.7 yet, For and against, Unused support, Q.5–Q.7 only): each phrase once; a piece of a longer phrase in the same list goes ("complex adaptive" under "complex adaptive system"); a single word is not stated (his rule), except the five emotion names. 11-20's For and against went from 39 (with repeats) to 8; "yet", "strong", "context" are gone.
3. **RUNS TOGETHER** no longer quotes the goal back to the user when a note or answer carries the same words.
4. **Card maps** say "once", not "1 times" / "1 time".
5. **EMERGING** and **MORE INFORMATION NEEDED** drop contraction fragments ("dont fix").
6. **DOES THIS ANSWER THE GOAL?** never pairs a hindrance with a response through a preposition ("among") or a generic verb ("continue", "make", "take", and similar).

## Tests
matrix.py on 11-20 (full text, `tests/w20full.json`, local only) and all eleven mkwb workbooks: no page errors, no injection. vague_titles.py, ta_flow.py, switch.py pass. Not run this pass: 11-13 and Broadview (no local copies).

## Effect worth his eye
- Clinic: "clinic" and "residents" no longer show under Not in Q.5–Q.7 yet (single words). Real topics that only appear as single words now go unstated; that is his single-word rule applied to these lists.

## Repeats found, left for his call (wording is his or already approved)
- AT A GLANCE (WHAT THE SYSTEM IS DOING) and the first paragraph of YOUR STORY SO FAR say the same thing.
- THE OPPORTUNITY and the story both say support answers resistance in kind, each side hardening the other.
- On Taking Action, WHAT STILL STANDS IN THE WAY on the Build on what already helps card repeats THE TEST's "What already helps" line word for word.
- Start Here says THE FIVE PAGES and lists four.
