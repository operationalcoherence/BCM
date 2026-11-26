# v287 — tidy, second pass

His call, 25 Nov 2026 18:59: "Want to keep searching?" Engine fixes; no text of his changed. Patch: `tools/patches/v287_more_tidy.py`.

## Fixed (every workbook)
1. **FOR AND AGAINST, ROOT CONDITION, READY TO REINFORCE, REDESIGN THE RESISTANCE, BUILD OR REBUILD** state shared phrases only, never shared single words (11-20: "emergent, organization, leadership"). Emotion names still count.
2. **WHERE THESE MEET** drops its "The word …" entries (single words).
3. **POSSIBLE PATTERNS** drops "“command” sits behind two findings…" when it rests on a single word.
4. **WHERE THE CARDS MEET** says a name once when it is a piece of another on the same line (11-20: "complex adaptive" under "complex adaptive system"; 4 names became 3).
5. **DOES THIS SERVE THE GOAL?** Since v269 its heading sat on Taking Action with nothing under it, and its questions sat inside IN YOUR ANSWERS, NOT ON THE MAP on Pattern Analysis. The questions and YOU SAID THESE DO NOT SERVE THE GOAL now sit under their own heading on Taking Action, and stay there after a Yes or No (`gsmGoalQ`).

## Effect worth his eye
- Findings that rested only on single words are gone. On the clinic test, WHERE THESE MEET no longer appears at all ("lease" and "referrals" were single words).

## Tests
matrix.py on 11-20 and the eleven mkwb workbooks (no errors), vague_titles.py, ta_flow.py, switch.py pass; a click test confirms the goal questions stay on Taking Action after an answer.
