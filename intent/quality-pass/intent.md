# Intent: Quality pass on the training site and its docs

- **Slug:** quality-pass
- **Author:** ai-native-sdlc loop
- **Date:** 2026-09-02
- **Status:** accepted

## Problem
A read-only audit of the repo at `38b5453` found defects that are individually small
but all user-visible or misleading. Each was verified against the actual files:

1. `demo-task-spec.md` told the runner to read
   `/Users/tmwu/.kiro/crew/workspace/kiro-crew-training/index.html` — a machine-specific
   absolute path. The site advertises this spec as runnable, so the advertised demo
   failed on any other checkout. It also leaked a username.
2. No canonical URL, no Open Graph / Twitter tags, no favicon — the portal previewed
   as a bare URL when shared and requested a 404 favicon.
3. The only `<img>` declared no `width`/`height`, so the page shifted layout as it loaded.
4. No skip-link: a sticky header with an 8-item nav meant keyboard users tabbed
   through the whole nav on every section.
5. `showTab` mutated `event.target` from the implicit global `event`, and the tab
   buttons/panels carried no ARIA, so screen-reader users got no active-tab state.
6. `README.md` and `QUICK_START.md` advertised "code examples with copy buttons".
   Verified: `copy` appears in `index.html` only as `&copy;`. The feature did not exist.
7. `REWRITE_SUMMARY.md` and `UPDATES.md` presented `generate_pptx.py`,
   `kiro-crew-training.pptx` and `presentation-brief.md` as repo deliverables with
   sizes and line counts. None are in the tree.
8. `SECURITY.md` existed but was absent from both file manifests.

Explicitly NOT a problem (checked and cleared): the published site matches the repo,
and `memory-layers.svg` / `demo-task-spec.md` both resolve on the
`/Kiro-Crew-Training/` subpath because the HTML references them relatively.

## Desired outcome
The advertised demo runs from a fresh clone; the portal previews correctly when
shared and is navigable by keyboard with accurate screen-reader state; the docs
describe only features and files that actually exist.

## Affected users / systems
Site visitors; anyone running the demo spec from a clone; anyone reading the repo
docs. No backend. GitHub Pages deployment unchanged.

## Constraints
- `index.html` stays a single self-contained file — no build step, no external assets.
- No new network dependencies (the favicon must be inline).
- The existing quiz and tab behaviour must keep working.

## Success criteria
See `evals/check_quality_pass.py`, which is the executable form of this list.
Every criterion asserts an observable property, not merely that an identifier exists.

## Open questions
None. Adding real copy buttons rather than dropping the false claim is out of scope.
