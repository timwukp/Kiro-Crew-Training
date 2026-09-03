# Plan: Correct the memory-system figures and document where memory actually lives

- **Spec:** ./spec.md
- **Author:** Tim WU
- **Accepted-by:** Tim WU
- **Status:** accepted

## Files changed

1. `index.html` — the only product source file touched:
   - capacity preamble rewritten (source-verified, date, window-scaling qualifier)
   - six capacity figures corrected across the layer card, Context Assembly card and
     the quiz explanation
   - Lessons layer count-cap claim removed
   - Context Assembly card restructured to session-start vs per-message, plus the
     stale-snapshot consequence
   - Local Data Storage: `conversations/` → `sessions/`
   - backup line names both DB files
   - "Conflict Resolution — 6-Level Priority Order" card replaced by "How Conflicts Are
     Actually Resolved" (per-key write-time rule, admission gate, instruction strength,
     relevance-only ranking, assembly-order caveat)
   - quiz Q7 question text and explanation de-premised
   - new "Where Memory Actually Lives" section inserted before Channel-Aware Memory
2. `intent/memory-internals/{intent,spec,plan}.md` — this chain (meta, no coverage needed)
3. `.sdlc/active` — points at this slug

## Work order

1. Verify every figure against source before editing; record the constant and its
   file:line. Do not carry a number forward that was not re-derived.
2. Apply the numeric corrections, then assert no stale token remains anywhere in the
   file (a figure repeated in three places must change in all three).
3. Restructure the Context Assembly card.
4. Insert the new section.
5. Structural checks, then the existing eval.

## Tests that prove it

- `grep` asserts zero occurrences of every stale figure (`4,250`, `6,400` as a
  standalone capacity, `26,600`, `12,000`, `37,250`, `45,000`, `max 50`,
  `conversations/`) — the failure mode being guarded is a figure fixed in one place
  and left wrong in the other two.
- `python3 evals/check_quality_pass.py` exits 0 (no regression of the prior pass).
- HTML structural check: tag balance, no duplicate `id`, no dead internal anchors.
- `python3 .sdlc/scripts/sdlc_ci_gate.py` exits 0 once the chain is signed.

## Risks

- **Documenting internals invites drift.** Table and column names are the fastest-
  rotting layer. Mitigated by scoping them into one dated, explicitly-provisional
  section rather than spreading them through the page.
- **A wrong correction is worse than a stale value.** Three candidate "corrections" were
  rejected during verification: "max 50 → 200" (conflated two constants, both belonging
  to an inactive store); treating the episodic per-message claim as correct; and a first
  draft of the conflict-resolution rewrite that asserted no conflict resolution exists at
  all — `_write_semantic` does implement a real per-key rule, which that draft would have
  deleted from the page. All three were caught by re-deriving from source rather than
  trusting a first-pass report.
- **Two sub-agents disagreed on the priority order** (one judged it confirmed, one said no
  such ordering exists in code). That contradiction was adjudicated by reading source
  directly, not by taking the majority or the more confident report.
- **Privacy.** The store is personal data at mode `0600`; every example is neutral and
  no live content is reproduced.
