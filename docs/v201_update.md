# v201 update (2026-11-18)

Phase 1, step 4 of the review plan, second half: the phrase-and-meaning layer (P1) on Pattern Analysis and Pattern Synthesis. Patch: `tools/patches/v201_phrases_findings.py` (engine only, for every workbook; builds on v200's helpers).

## 1. WHAT YOU WOULD DO (Analysis, review 3f)
"Causes" and the counts ("56 also turn up … and 25 do not") are gone. The section now says plainly what nothing you would do deals with yet, with the notes behind each item (each note number links to the map). On 11-13: "Nothing you would design, redesign, or reinforce deals yet with tradition (N1, N18, and N23), reduce (N9, N12, and N25), and measures (N9, N25, and N26), among other things that stand in the way in the context you've grasped."

## 2. WHAT IT MIGHT MEAN (Synthesis, 4i)
Every list (Not in Q.5–Q.7 yet, For and against, Unused support, and the rest) names the phrase the workbook repeats around each word, with up to three notes. The note numbers link back to the map. A phrase is used only when the workbook repeats it or the goal uses it; otherwise the word stays bare, with its notes. (That keeps "tradition" from turning into "traditional media.")

## 3. IN YOUR ANSWERS, NOT ON THE MAP (Synthesis, 4h)
A single word is never shown as a theme. A word the workbook repeats inside a phrase is shown and asked about as that phrase. A word with no repeated phrase around it ("allowing," "creating," "benefit") is left out.

## 4. POSSIBLE PATTERNS (Analysis, 3l)
"What you talk about most may be what you have planned least" now counts the notes written under Q.5–Q.7 as planning, not only the answers. On 11-13 "management" drops out (N16 is a Q.5 note), and "tradition" takes its place. Every finding there now names its phrase.

## 5. ONE WORD, SEVERAL MEANINGS (Analysis, 3i)
Under each saturated word there is a fold, Each meaning, in your words. It opens every meaning into its phrase and up to three of the sentences that carry it, with a few words before for context and the note or answer each comes from. "fire later" becomes "encounter fire later": "…a specific future where it will encounter fire later" (Q.4); "grows thicker and taller and supports larger fires later" (N28). The actions written around the word get a line of their own. For "fire": allowing unplanned fires (Q.4), managing unplanned fires (Q.6), enabling aggressive fire (N8), putting good fire (N27), corralling fires (Q.1), and introducing fire (Q.1).

Sentences no longer break at abbreviations such as "U.S." and "a.m."

## Wording that is Claude's (flagged)
"Nothing you would design, redesign, or reinforce deals yet with …, among other things that stand in the way in the context you've grasped."; "Each meaning, in your words"; "Written as an action: …"; "These phrases also run …"; and the 3l sentence "comes up often, but nothing you would design, redesign, or reinforce (Q.5–Q.7, answers or notes) mentions it." The last sentence after it is his line, unchanged.

## Not yet
The interactive version of ONE WORD, SEVERAL MEANINGS beyond the fold, and the review's Phase 2 reordering of these pages.

## Tests
- `tests/dump2.py` and a fold probe on 11-13, Broadview, and clinic.
- `tests/matrix.py` on 11-13, Broadview, and every mkwb workbook: no page errors, no script injection.
- `tests/relief_text.py` with the 3D on 11-13, Broadview, and clinic. (The fold only exists where a word is saturated, which takes ten or more answers and notes; Broadview and clinic have none.)
- `grep -c 'AAPK\|AIza'` = 0.
