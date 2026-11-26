# v298: YOUR STORY SO FAR for place maps

His go-ahead (25 Nov 2026 22:50, "In the engine first"). Patch: tools/patches/v298_place_story.py, which inserts tools/patches/v298_place_story.js.

The line-map story reads hollows in the emotion ground. A place map's hills are real land, so this story reads the notes and answers instead, with no terrain words. It runs when the line map holds no stories and the place map has at least 8 notes, 3 of them holding back (Q.1 or Q.2, an emotion other than acceptance), and at least one reason found in two places.

Reasons it reads (each needs two places, as in v294): how the place would look, a danger people do not feel, what it costs, doubt that the work is worth it, plus tradition, fear of blame, and what others expect. Qualifiers: people away in the season it matters (seasonal, secluded), and no one yet offering to do the work. The unit is "household" when the goal or answers talk about homes or homeowners, otherwise "person".

It measures how far the people already doing the work (Q.3 notes with acceptance) are from those who hold back, and says "a few minutes' walk" (under 400 m), "a short walk" (under 1.5 km) or "a short drive" (under 5 km).

Same layout as the line story: four summary paragraphs, then "Your story in greater detail" with one chapter (STORY 1 · ON THE PLACE MAP) in the seven moves, and its notes. AT A GLANCE gets WHAT THE SYSTEM IS DOING, and BIGGEST GAP goes, as on line maps.

Checks: Broadview reads as one story; a made-up Main Street storefront workbook reads without fire or house words; 11-13, 11-18, 11-20 stories unchanged; matrix.py on every test workbook plus the real ones: no errors. Known, from before this version: Broadview's two Taking Action titles are vague ("Change what holds the situation in place", "Scale the alternative that already exists").
