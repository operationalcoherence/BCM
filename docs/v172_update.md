# v172 (preview only) — 2026-11-17

Priority 1 batch 2: the word engine. All new wording is Claude's and is marked for his pass.

| Task | Change |
|---|---|
| E1 | **Saturation filter.** A word in 40% or more of the answers and notes (with at least 10 of them) that the person also splits into two or more recurring two-word phrases is the medium, not a finding ("water in the fishbowl"). It stops counting as a recurring word, so every finding, card and reading names its phrases instead. On his workbook: fire (22 of 39), wildfire (19) and suppression (17). The top course of action is now **good fire**, not "fire". The clinic workbook has no such word and is unchanged. |
| E2 | **ONE WORD, SEVERAL MEANINGS** (Pattern Analysis, IN THE WORDS). For each medium word, the phrases it takes, sorted by which side of the line they sit on. For "fire": good fire, fire back and putting fire where things help; prescribed fire, fire suppression and fire later where things hinder; unplanned fire on both sides. Domain-free: built from his own phrases, with no word list. |
| E4 | "involved" and "necessary" join the stopwords. They were surfacing as findings ("tradition and involved", "necessary") without meaning anything. |

Checked: matrix on his workbook and all 13 synthetic workbooks, no page errors. The clinic workbook gets no medium word.

Not done, needs a decision (D2): **fire ≡ wildfire.** The engine's standing rule (`vocabulary_architecture.md`) is *split by default; merge only where the person says to*. A built-in merge broke other workbooks at v97. So "they mean the same thing" has to be his declaration, not the engine's guess. Proposed: when two medium words contain one another (fire / wildfire), Patterns asks once, "Do these mean the same thing to you?", and merges only on Yes. This uses the same one-tap question pattern as "Is it a theme?".
