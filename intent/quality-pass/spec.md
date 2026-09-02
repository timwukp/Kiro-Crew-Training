# Spec: Quality pass on the training site and its docs

- **Intent:** ./intent.md
- **Status:** signed-off

## Requirements
1. `demo-task-spec.md` references the site by a repo-relative path.
2. `index.html` `<head>` gains `<link rel="canonical">`, `og:title`,
   `og:description`, `og:type`, `og:url`, `og:image`, `twitter:card`, and
   `<link rel="icon">` as an inline `data:` SVG (no fetched asset).
3. The memory-diagram `<img>` declares `width`/`height` matching the SVG's intrinsic
   720×600 viewBox, keeping `max-width:100%; height:auto` so it still scales.
4. A `.skip-link` anchor is the first focusable element in `<body>`, hidden until
   focused, targeting `#main-content` on `<main>`.
5. Tab buttons get `role="tab"` + `aria-selected` + `aria-controls` and an `id`;
   panels get `role="tabpanel"` + `aria-labelledby`; the list gets `role="tablist"`.
   `showTab(name, btn)` takes the clicked element instead of the implicit global
   `event`, and keeps `aria-selected` in sync with the `.active` class.
6. The copy-button claim is removed from `README.md` and `QUICK_START.md`.
7. Docs citing `generate_pptx.py` / `kiro-crew-training.pptx` /
   `presentation-brief.md` mark them as not distributed in this repository.
8. `SECURITY.md` appears in both file manifests.
9. Regression: quiz ids and all six tab-panel ids survive; no dead anchors; no
   duplicate ids.

## Non-functional requirements
- Single-file `index.html`; no build step; no new network requests.
- Insert/replace only — no restructuring of existing section markup.

## Design
- One contiguous metadata insert after the existing `<meta name="description">`.
  The favicon is a `data:image/svg+xml` URI so it adds no request and no asset.
- Skip-link uses the standard off-screen-until-focus pattern, added to the existing
  inline `<style>` block so no new file appears.
- Passing `this` at the six call sites makes the source element explicit, which is
  also what lets the handler be invoked programmatically. Verified: the original
  throws `TypeError: Cannot read properties of undefined (reading 'target')` on a
  programmatic `showTab('knowledge')`; after the change it works.
- **Tab panels are `display:none` when inactive**, so this change does NOT add nav
  links to panel ids. Making them deep-linkable needs JS that activates the tab
  from the URL hash — out of scope.

## Flagged concerns
| Concern | Policy owner | Resolution |
|---------|--------------|------------|
| Username leak in a committed path | repo owner | fixed by requirement 1 |
| a11y regression risk from ARIA | repo owner | requirements 5 + 9 assert both new state and old ids |

## Out of scope
Adding real copy buttons; hash-based deep-linking into tabs; visual redesign;
consolidating the overlapping `REWRITE_SUMMARY.md` / `CORRECTIONS.md` tables.
