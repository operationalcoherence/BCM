# v221: the structure pass on Pattern Analysis

His note (11-18 18:34): Analysis should interpret the structures the observations form, not report the observations, and use emotions as terrain that explains. "Go ahead" 18:48.

A new section opens Pattern Analysis, **WHY IT BEHAVES THIS WAY**, open by default. Each reading has one meaning sentence, with its notes folded under **The notes behind it**. A reading is silent when the workbook doesn't meet its test. The section shows when at least one reading does. All wording is Claude's, for his redlines (claude/structure_pass_plan.md in the Claude project).

1. **THE SYSTEM THAT HOLDS.** The largest group of hindering notes tied by shared words. Each part is named by its note's opening words; parts that say they reinforce, feed, drive, entrench, or freeze come first. It's called self-supporting when two or more of its notes say so; otherwise the parts "hang together." Its ground (top emotions) explains why it holds.
2. **THE KEY TENSION.** The goal clause that asks for more of something, against the hindering notes that share its words and carry fear words (fear, liability, escape, vilify, eradicate, deadly, …). It shows only when help-side notes share those words too. The fearing note's emotion gives the ground.
3. **THE LOOP.** A word (not a medium word in over half the workbook) found in two or more sentences that say it feeds itself (reinforce, accumulate, itself, feedback, need for more, …). It's read with now and later when those sentences carry both, and the quote is centered on the word.
4. **THE OPPORTUNITY.** Support and reinforce notes on the help side, on acceptance or indifference (what already exists), against help-side design and redesign notes (what's new). "Most" when existing ≥ new.
5. **WHERE IT CAN CROSS.** Indifference notes, as the ridge between the system that holds and the high ground. Shown only with reading 1.

Code: `gsmStruct()` (window.gsmStruct), `gsmStructBuild`, `gsmStName`, `gsmStQ`, `gsmStList`, `gsmStSent`, `gsmStEm`, all inside `phKeep` so word tallies don't move. It's inserted before WHAT IT PRODUCED. Patch: tools/patches/v221_structure_pass.py.

Tests: matrix.py on w18, real, broadview, and every mkwb workbook, with no page errors and no injection. Read the section on w18, real, Broadview, clinic, hostile, one, and same. One screenshot.

Known limits: part names come from opening words, so long notes can get clumsy names (Broadview: "has heard many stories of homes"). The clinic workbook shows only THE OPPORTUNITY: its three hindering notes share no words, so no system.
