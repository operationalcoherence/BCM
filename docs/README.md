# Documents

Design and audit documents for the Bear Canyon Method web workbook, kept beside
the code so the two travel together. All wording in these documents is Claude's
unless it quotes Gregory directly. Gregory edits his own text.

**Latest shipped: v109 (preview only). The live page `/gsmlive` is still on the
old pasted v92 file and must not be touched without his say-so.**

| File | What it is |
| --- | --- |
| `handoff_v104.md` | **Start here.** Current state at v104, the decisions of 2026-11-08, the PDF uncoupling, four corrections to earlier documents, architecture notes, the word pipeline, and the lessons. Supersedes `handoff_v99.md`. |
| `week_of_11_09_plan.md` | **The current plan.** What to build next, in order, with estimates. The build started 2026-11-10; the safe cuts are next. Supersedes `v99_plan.md`'s ordering. |
| `keep_or_cut_table.md` | Per-section verdict on every part of Pattern Analysis and Pattern Synthesis: keep, or look at for deletion. The checklist to work from for the safe cuts. |
| `elegance_screening.md` | The reasoning behind that table, with confidence marked: which calls are safe because the content is duplicated, and which are judgment. |
| `asking_questions.md` | Eight classes of question the engine could ask from structure it already computes, and the rule that governs which findings become questions. Designed, not scheduled. |
| `vocabulary_architecture.md` | Why a built-in domain lexicon cannot generalize, and why the engine cannot infer synonyms by itself. The reasoning behind v98. |
| `vocabulary_funnel.md` | How the list of candidate synonyms is narrowed before the person is asked anything. |
| `engine_audit_v98.md` | A measured audit of the engine at v98: what is sound, nine defects with evidence, and where the advancements are. |
| `v109_update.md` | "Where to look first" removed from Synthesis; "Where to start" on In Parallel kept. |
| `v108_update.md` | The big swing: three noise lists hidden, EACH QUESTION, the repeated PRESSING NOW and "The meaning of that meaning" removed. About 1,000 words off since v104. |
| `v107_update.md` | Six more sections cut; two more checked and kept because other findings depend on them. |
| `v106_update.md` | Three word-spotting findings cut from Pattern Analysis. |
| `v105_update.md` | Two duplicated findings cut. Three others were checked and kept; see the file. |
| `v104_update.md` | The hang figure is no longer cut off at the bottom: the frame is sized from the measured drawing. |
| `v103_update.md` | "Where to start" no longer names the same word twice. |
| `v102_update.md` | The stopword list cleaned, with no change in behavior. |
| `v101_update.md` | The place map's note hover appears at all. Corrects a claim in `v100_update.md`. |
| `v100_update.md` | The map hover names the note's author. |
| `v99_update.md` | What v99 shipped on 2026-11-07. |
| `v99_plan.md` | The batch agreed at v98. Its ordering is superseded; the item detail still stands. |
| `handoff_v99.md` | Superseded by `handoff_v104.md`. Kept for its fuller detail on the v99 batch. |

The repository is public and clones anonymously:

    git clone --depth 1 https://github.com/operationalcoherence/bcm

An attach is only needed to push. His two saved workbooks are not in the
repository — they are in the Claude project "Bear Canyon Method", which also
holds the full per-version history (`groundsmith_web_vNN_update.md`, v13
onward, and the earlier handoffs).

The five-screen interface mockup for declaring synonyms is an artifact:
https://claude.ai/artifact/Vk5rTHDvugvbXGzZ72uG7V
