# v235: YOUR OWN WORDS as a strip (plan item 3g)

"Your own words, in the order the method asks for them," under YOUR STORY SO FAR on Pattern Analysis, now opens with a strip. The fold stays closed, so the page's word count is unchanged.

- One line, RUNS THROUGH NEARLY EVERY ANSWER, names the phrases that almost every question uses (on 11-18: "good fire" and "fire back"). They leave the columns so that each column can say something of its own.
- **Q.1 to Q.7, left to right,** under THE CONTEXT YOU HAVE GRASPED (Q.1–Q.4, black) and WHAT YOU WOULD DESIGN (Q.5–Q.7, teal). Each column holds up to three phrases from that answer and its notes, as written: the ones used most there, with phrases shared with only a few other questions ranked higher. Under each phrase, in small gray text, is where else it appears ("also the goal, Q.6"), so nothing depends on hover. A phrase that overlaps one already shown is skipped.
- Phrases only, two or three words, never a lone word (his rule). Very long words are cut.
- An unanswered question says "Not answered yet."
- The full text that was there before moves into a fold below, Read them in full.
- On a phone, the two groups stack.

All wording is Claude's. Checked: tests/ownwords.py on 11-18 (desktop and 390 px), clinic, and hostile; matrix.py on everything, no errors; step9.py, ta_flow.py, and qhover.py pass. Patch: tools/patches/v235_own_words_strip.py (`gsmOwnStrip()`).
