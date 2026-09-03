# Intent: Correct the memory-system figures and document where memory actually lives

- **Slug:** memory-internals
- **Author:** Kiro Agent
- **Accepted-by:**
- **Date:** 2026-09-03
- **Status:** draft

## Problem

The site's memory sections are the most technical thing it teaches, and parts of them
are now wrong. Verified against KiroCrew source on 2026-09-03:

1. **Every per-layer character budget is stale.** `context.py` derives each cap as a
   percentage of `_CONTEXT_BUDGET_BASE = 165_000`. The published figures do not match
   that derivation:

   | Layer | Published | Actual | Source |
   |---|---|---|---|
   | Preferences | 4,250 | **4,290** | `_budget(0.026)` |
   | Projects | 6,400 | **6,435** | `_budget(0.039)` |
   | Recent History | 26,600 | **26,400** | `_budget(0.16)` |
   | Semantic | 12,000 | **12,705** | `_budget(0.077)` |
   | Lessons | 37,250 | **37,290** | `_budget(0.226)` |
   | Thread history (compressed) | 45,000 | **44,550** | `_budget(0.27)` |

   The numbers appear in three places each — the layer card, the Context Assembly
   card, and an embedded quiz explanation — so a reader who cross-checks finds the
   same wrong value three times and concludes it is confirmed.

2. **The page presents the budgets as fixed.** They are the 1M-window reference
   values; `_resolve_caps(window)` re-derives the same percentages for the active
   model window, so a smaller window yields proportionally smaller caps. Stating a
   bare number without that qualifier is misleading even once corrected.

3. **"max 50 lessons" is wrong for the active store.** Two different constants exist
   (`_MAX_LESSONS_IN_CONTEXT = 50`, `_MAX_LESSONS_TOTAL = 200`) but both live in the
   legacy JSONL `LessonStore`, which newer installs never create — `learn add` writes
   only to the vector store, whose lesson path is bounded by the character budget and
   applies no count cap. Live check: 48 lessons stored, all 48 injected.

4. **Episodic memory is described as per-message. It is not.** `context.py:2993`
   states it is "injected on new sessions only ... follow-ups skip it", and the whole
   memory block is assembled under an `if is_new_session:` gate. This is the most
   consequential error on the page: it hides the fact that a running session holds a
   stale snapshot, which is why a `learn_add` mid-session does not take effect until
   the next session.

5. **`conversations/` does not exist.** Session transcripts live in `sessions/*.jsonl`.

6. **The backup card says "episodic + semantic DBs"**, implying separate files.
   Semantic, episodic and lessons all live in one `memory.db`.

7. **The "Conflict Resolution — 6-Level Priority Order" card is not implemented.**
   No layer-rank constant, precedence table, or inter-layer arbitration routine
   exists. Levels 1–3 order by source and confidence, and the code states the
   opposite intent outright: ranking "is relevance-only — neither `source` nor
   `confidence` contributes — so an unrelated user-taught rule cannot displace a
   relevant inferred one". The `≥0.8` figure is a write-time admission gate, not a
   rank. What *does* exist is per-key conflict resolution inside semantic memory at
   write time (`_write_semantic`), which the card never mentions. Quiz Q7 asks
   "which source has the highest priority", so its question text carries the same
   false premise.

## Root cause

These are not authoring errors. Every one of the above is reproduced **verbatim from
the official Kiro documentation** at `kiro.dev/docs/crew/features/memory/` (page
updated 2026-08-04): the six capacity figures, "max 50 lessons", episodic-per-message,
the 6-level priority list, and the "episodic + semantic DBs" phrasing all appear there.
The site's own claim that the limits were "verified from official documentation" was
therefore true as written — the upstream doc is what drifted from the implementation.
That reframes the fix: the page should state where it diverges from the docs and why
source is the ground truth, rather than silently disagreeing with the vendor's own
reference.

The one place the docs are more accurate than this site is the semantic conflict rule
("higher confidence wins; same confidence → newer wins"), which is real but imprecise —
the code uses a 0.1 tolerance band, not exact equality.

Separately, the site documents the six layers conceptually but never says where they
are stored or how to inspect them — so a reader cannot verify any of it, and cannot
back it up correctly. The WAL sidecar is a live data-loss trap: copying `memory.db`
alone can silently drop recent memories, and in a live check the `-wal` file was
larger than the database.

## Desired outcome

Every memory figure on the page matches source and carries the qualifier that caps
scale with the model window. The session-start-snapshot behaviour is stated plainly,
including its practical consequence for lessons. A reader can locate the store,
inspect it safely read-only, and back it up without losing WAL contents.

## Affected users / systems

Readers of the published training site. No runtime behaviour changes; this is
documentation of KiroCrew internals plus corrections to already-published claims.

## Non-goals

- No change to KiroCrew itself.
- No reproduction of any real memory or lesson content: the store is mode `0600`
  personal data, so all examples are neutral.
- Channel-Aware Memory buffer sizes/TTLs are left untouched — they were not verified
  in this pass, and correcting only what was checked is the point.
