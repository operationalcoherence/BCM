# v222: YOUR STORY SO FAR leads Pattern Analysis

His note (11-18 19:08): elevate YOUR STORY SO FAR as the primary synthesis of Pattern Analysis, and prefer explanations, tensions, reinforcing dynamics, opportunities, obstacles, and implications over counts, frequencies, and inventories.

1. **The story leads the page.** It moves to the top of Pattern Analysis, under THE SAME THING? prompt and above WHY IT BEHAVES THIS WAY. It sits in its own panel (2 px border, warm background), with larger type for the opening and a subtitle: "What Pattern Analysis makes of your workbook: the story first, the evidence after." This is a DOM move after render (`gsmStoryLead`, called from `gsmMeanPass`, retried until the story is built).
2. **WHERE THIS LEAVES THE WORK** follows the story's opening paragraph. It ties the v221 readings into one implication: what holds the work in place (and from which ground), the loop, what it fears, what already stands, where people can cross, and so what the work is. It's built from `window.gsmStructSum`, set by `gsmStructBuild`, and shows when at least three of its sentences apply.
3. **Meaning before counts in the story.** "You name 14 things…", "5 notes name support…", "That is 14 things against the goal to 5 for it", "4 notes say…", "12 notes say…", and the "(10 of 14)"-style counts are gone. Each section opens with what it means; the note numbers follow in small gray type.

Wording is Claude's, for his redlines. Patch: tools/patches/v222_story_lead.py.

Tests: matrix.py on w18, real, Broadview, and every mkwb workbook (no errors); read the story on w18, Broadview, and clinic; one screenshot.
