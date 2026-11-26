# v302: targets named in context; no false "most"; no nested quotes

His asks, 26 Nov 2026 07:55. Patch: tools/patches/v302_targets_in_context.py.

1. **What an emotion is aimed at (Pattern Analysis).** "Aggression here is not one thing" named each target by a
   trimmed keyword ("supporters", "the complex adaptive system"), which lost what it was about. Each target is now the
   note's own phrase, quoted, up to the end of its clause (a list like "defiant, aggressive, or distrustful of ..."
   is kept whole; at most 12 words), plus who holds it when the note says ("among supporters"). Grouping is unchanged.
   11-20 now reads: aimed at “the idea of change” N9, “those who are defiant, aggressive, or distrustful of the
   organizational transformation” (among supporters) N16, “the complex adaptive system idea” N26, and “supporters of
   the transition” N38. The distrust line on 11-20 gets the same treatment ("the concept of a complex adaptive
   system", "what the transformation will change to").
2. **WHAT HOLDS THE SITUATION IN PLACE.** "Most of it sits on X" now only when X really has the most notes. A tie is
   named as a tie. Broadview: "It carries indifference and defiance in equal measure: the defiance holds it in place,
   while the indifference could tip either way." wb_cause had the same false "most" (a three-way tie). On a
   place-only workbook these lines name no ground.
3. **Nested quotes.** A card title quoted in THE CHEAPEST FIRST MOVE (and the story's "On Taking Action" line) uses
   single quotes inside: “Change what keeps ‘plainly uninterested’ (N1) in place”.

Checks: 11-20, Broadview, w20, wb_cause, wb_clinic, wb_places_names, wb_big against v301: only the lines above
change. vague_titles.py: ALL PASS. No page errors at 1200 or 420 wide.
