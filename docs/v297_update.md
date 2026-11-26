# v297: story checks from the four real workbooks

His ask (25 Nov 2026 22:38): load the workbooks through YOUR STORY SO FAR and make sure each story is coherent, like 11-20. Patch: tools/patches/v297_story_checks.py.

Found and fixed (11-13, 11-18):
1. "Each side reads the other's response as proof of its own fears" fired on any aggression on the side that helps. In 11-18 that aggression was aimed at full suppression, a practice, not at people who resist. It now needs help-side aggression aimed at people (those who, supporters, opponents, the opposition, defiant, ...). 11-20's note about supporters' aggression toward the defiant still qualifies.
2. "Jobs, money, and standing" for the close-to-the-goal story rested on homeowners protecting "their livelihoods" from wildfire, which is safety, not jobs. A protected livelihood no longer counts.
3. "Fear of blame" rested on "catastrophic" (media coverage of catastrophic wildfires). Catastrophic no longer counts as fear; that story now reads as public and political expectation, which the note is about.

11-20 reads word for word as before. Broadview (place map only) still gets no story: the story engine reads line-map ground only.

Checks: matrix.py on clinic, empty, Broadview, 11-18: no errors; vague_titles.py on 11-13, 11-18, 11-20: all pass.
