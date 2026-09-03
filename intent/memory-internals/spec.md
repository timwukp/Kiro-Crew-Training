# Spec: Correct the memory-system figures and document where memory actually lives

- **Intent:** ./intent.md
- **Author:** Kiro Agent
- **Accepted-by:**
- **Status:** draft

## Requirements

1. Every published per-layer capacity equals `int(165000 × fraction)` for its
   `context.py` fraction: Preferences 4,290 · Projects 6,435 · Recent History 26,400 ·
   Semantic 12,705 · Lessons 37,290 · compressed thread history 44,550. Corrected in
   all three locations (layer card, Context Assembly card, quiz explanation).

2. The capacity preamble states that the figures are 1M-window reference values
   derived from `_CONTEXT_BUDGET_BASE = 165,000` and re-derived per model window by
   `_resolve_caps(window)`, and names the verification date. It no longer claims
   "verified from official documentation" — the values were verified against source.

3. The Lessons layer no longer claims a count cap. It states the character budget and
   that the active store applies no lesson-count cap, noting the 50/200 constants
   belong to the legacy JSONL store.

4. The Context Assembly card places all six memory layers, episodic included, under
   session-start-only injection, and lists per-message injection accurately (project
   line, runtime line, channel history, triggered skills, hook context, post-compaction
   skills re-injection).

5. The card states the consequence: a running session holds a stale snapshot, and a
   `learn_add` mid-session takes effect in the next session, not the current one, with
   the mitigation of querying the live set.

6. The Local Data Storage card lists `sessions/` (`*.jsonl`) instead of
   `conversations/`.

7. The backup line names `memory.db` and `memory_index.db` and states that semantic,
   episodic and lessons all live in them.

8. A new "Where Memory Actually Lives" section exists, marked as observed
   implementation detail with a date and schema version, covering: the single SQLite
   WAL database vs the markdown layers; the five tables and their purpose; lessons as
   `lesson.<md5>` semantic rows with soft delete and confidence 1.0/0.9; the two dedup
   passes and the five write outcomes; hybrid `0.6 × cosine + 0.4 × keyword` with
   NULL-embedding handling; Qwen3-Embedding-0.6B at 1,024 dims; the deferred-embedding
   window and what it degrades; the WAL backup trap; and a read-only inspection recipe.

9. No real lesson or memory text appears anywhere in the change.

10. Attribution: the new section states KiroCrew is Apache-2.0 and that the names are
    internal and may change. The capacity preamble states that where the figures differ
    from the official Kiro docs, the docs are stale, so a reader who cross-checks the
    vendor page is not left thinking this page is wrong.

11. The "Conflict Resolution — 6-Level Priority Order" card is replaced by one that
    describes only mechanisms present in source, in this order: per-key conflict
    resolution at write time (`user_explicit` always wins; automated-over-user_explicit
    refused; higher confidence wins; within 0.1 the newer wins; otherwise refused and
    logged as `conflict_skip`), the `≥0.8` admission gate, per-layer instruction
    strength quoted from the wrappers, and relevance-only retrieval ranking. It states
    plainly that no inter-layer priority ordering exists, that the official docs publish
    one, and that assembly order is not a ranking (lessons are assembled last yet carry
    the most binding language).

12. Quiz Q7's question text no longer presumes a priority ordering. It asks which layer
    carries the most binding instruction language; answer C (Lessons) stays correct, and
    the explanation is rewritten to the verified mechanism.

## Non-functional

- Valid HTML: tags balanced, no duplicate `id`, no dead internal anchors.
- No new external assets and no new fetches.
- Existing quality-pass criteria continue to hold (`evals/check_quality_pass.py`).

## Out of scope

Channel-Aware Memory figures and the `~500 chars` critical-rules estimate (neither was
verified in this pass). Filing the upstream documentation drift with Kiro — worth doing,
but a separate action outside this repo. The vendored gate's missing
`Author:`/`Accepted-by:` duties check and its argparse prefix-matching fail-open, both
tracked separately.
