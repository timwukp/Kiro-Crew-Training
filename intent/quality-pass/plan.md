# Plan: Quality pass on the training site and its docs

- **Spec:** ./spec.md
- **Author:** Kiro Agent
- **Accepted-by:** Tim WU
- **Status:** accepted

## Files changed (in order of work)
1. `evals/check_quality_pass.py` — the verification target, written FIRST.
2. `demo-task-spec.md` — absolute `/Users/tmwu/...` path → `./index.html`.
3. `index.html` — `<head>` metadata block; `.skip-link` CSS; skip-link anchor and
   `#main-content`; `<img>` dimensions; tab ARIA and the `showTab` signature.
4. `README.md`, `QUICK_START.md` — drop the copy-button claim, list `SECURITY.md`
   and `REWRITE_SUMMARY.md`.
5. `REWRITE_SUMMARY.md`, `UPDATES.md` — mark the non-distributed deliverables.

## Work order
1. Write the eval; run it against the unchanged tree — it MUST fail.
2. Apply the fixes in the order above, re-running the eval after each group.
3. Verify independently of the eval: HTML tag balance, no duplicate ids, no dead
   anchors, `node --check` on the inline JS, and a real browser check of the tab
   switch and the skip-link.
4. Commit with the artifacts.

## Tests that prove it
`python3 evals/check_quality_pass.py` — exit 0 only when every criterion holds.
Browser verification is required for the tab and skip-link behaviour: static checks
cannot see that a panel is actually visible or that the skip-link renders on focus.

## Risks
- **Riskiest step: the tab edits.** Touching the script could break the tab or quiz.
  Mitigation: the eval asserts the quiz ids and all six panels survive, and that
  exactly one tab starts selected.
- Wrong ARIA is worse than none. Mitigation: `showTab` updates `aria-selected`
  alongside the `.active` class so DOM state and ARIA cannot diverge.
- **Rejected approach:** adding `#memory`/`#subagents`/… to the header nav. Those
  panels are `display:none` unless active, so a fragment link scrolls to an
  invisible element. An earlier attempt did this and passed a weaker eval that only
  checked whether the id existed. Recorded in `REVIEW.md` as a trap.
