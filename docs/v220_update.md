# v220: the meaning pass on Pattern Analysis

His note (11-18 18:05): "Analysis should tell me what the findings mean, not what exists."

Each finding card on Pattern Analysis now opens with one sentence on what the finding means for the work. What the card used to say (the words, the questions, the counts) folds under it in a closed section, **The words and notes**, with the notes that carry those words: number, emotion, side of the line, and a short quote.

- The sentences come from the draft patterns (claude/meaning_patterns_draft.md in the Claude project). They're Claude's wording and are waiting for his redlines.
- Each sentence's subject is a sentence quoted from the workbook, with its source, never a lone word (11-12 rule). A finding that is one phrase or name ("natural resource", "Fire Adapted Colorado") uses the phrase. Each quote is used once per page where possible.
- Emotion readings follow the paper: far-apart emotions take a big move; indifference is the easiest ground to move through; aggression and defiance are the slowest to change; acceptance doesn't hold on its own. Lever or risk follows the emotion of the quoted note.
- Kinds covered: opposition with no answer, support nothing builds on, words pulled two ways, words that run together, one emotion, one side only, one voice, said not seen, answered with nothing on the map, and the POSSIBLE PATTERNS items. A "nothing you would design mentions it" item reads as opposition, as support, or as "what you talk about most may be what you have planned least," depending on which side its notes sit.
- Cards that already said what they mean (CONDITION NOT IN Q.5–Q.7, FOR AND AGAINST ON THE MAP, and the rest of GSMMEAN) keep their sentence at the top, with the rest folded.
- Left as they were: ONE WORD, SEVERAL MEANINGS and WHICH WORDS, AND WHOSE VOICES, SHAPE THIS MAP.
- Only Pattern Analysis (`[data-pv="2"]`). In Parallel comes next, after his look.

Code: `gsmMeanPass()` is called from `gsmPD()`; `gsmMeanRun`, `gsmMeanData`, `gsmMeanSay`, `gsmMeanQuote`, `gsmMeanEv`. Patch: tools/patches/v220_meaning_pass_analysis.py.

Tests: matrix.py on w18, real, broadview, and every mkwb workbook. No page errors, and no injection. Read the Analysis text on w18, clinic, Broadview, and hostile. One screenshot of Analysis.
