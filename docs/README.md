# Documents

Design and audit documents for the Bear Canyon Method web workbook, kept
beside the code so the two travel together. All wording in these documents is
Claude's unless it quotes Gregory directly.

| File | What it is |
| --- | --- |
| `handoff_v103.md` | **Start here.** Current state at v103, the decisions of 2026-11-08, what is known about the figure clipping, and four corrections to earlier documents. Supersedes `handoff_v99.md`. |
| `handoff_v99.md` | Superseded by `handoff_v103.md`. Kept for its fuller v99 detail. Current state, every change agreed for next week with its evidence, standing rules, architecture notes, and the lessons. |
| `v99_update.md` | What v99 actually shipped on 2026-11-07. |
| `engine_audit_v98.md` | A measured audit of the engine at v98: what is sound, nine defects with evidence, and where the advancements are. |
| `v99_plan.md` | The next batch: figure clipping, the Pattern Synthesis rewrite, "feeling" to "emotion". |
| `vocabulary_architecture.md` | Why a built-in domain lexicon cannot generalize, and why the engine cannot infer synonyms by itself. The reasoning behind v98. |
| `vocabulary_funnel.md` | How the list of candidate synonyms is narrowed before the person is asked anything. |

The five-screen interface mockup for declaring synonyms is an artifact, not in
this repository: https://claude.ai/artifact/Vk5rTHDvugvbXGzZ72uG7V

The full per-version history (`groundsmith_web_vNN_update.md`, v36 onward, and
the handoffs) lives in the Claude project "Wildfire Design Industry".
