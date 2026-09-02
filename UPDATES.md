# Training Materials Updates Log

## Update: 2026-08-31 — Accuracy pass (verified against live kiro.dev docs)

### Change 1: CI/CD headless command corrected

Earlier drafts used `kiro-cli --v3` in the CI/CD examples. Verification against the
official docs (https://kiro.dev/docs/cli/headless/) found that `--v3` is **not a
documented flag**. Corrected to the documented headless form:

**Before (undocumented):**
```bash
kiro-cli --v3 ask "Generate test fixtures"
```

**After (documented):**
```bash
kiro-cli chat --no-interactive --trust-tools=read,grep "Generate test fixtures"
```

- Engine version is selected with `--engine v3` (two tokens), not `--v3`.
- `--v3` works on some local binaries as a shorthand but is not the documented CI form.
- Auth in headless mode is via the `KIRO_API_KEY` env var.

### Change 2: Model multiplier claim corrected

`Sonnet 5 = 1.3x` was overstated. The docs state **1.3x for the Sonnet family**
(vs 2.2x for Opus), not a per-model figure for Sonnet 5. Also removed an unsourced
`Haiku 4.5 = 0.6x` figure. Opus 5 = 2.2x remains verbatim-confirmed.

### Change 3: Authentication wording corrected

Installation page states first-launch auth is **device-code sign-in**. "AWS Builder
ID / social login" is an account-creation option on the pricing page, not the
Gateway auth method — reworded accordingly.

### Files Updated
- `index.html` (CI block, model multipliers, two auth references)
- `VERIFIED_OUTLINE.md` (CI, multipliers, two auth references)
- `generate_pptx.py` (CI slide, multipliers, two auth references) — *not distributed in this repository*
- `QUICK_START.md` (stale setup line + stale size/slide numbers)
- `CORRECTIONS.md`, `REWRITE_SUMMARY.md` (multiplier + auth statements)
- `presentation-brief.md` (fully rewritten — was still the old Bedrock version) — *not distributed in this repository*
- `kiro-crew-training.pptx` (regenerated) — *not distributed in this repository*

### Verification sources (fetched 2026-08-31)
- https://kiro.dev/docs/cli/headless/
- https://kiro.dev/docs/models/available-models/
- https://kiro.dev/docs/crew/installation/
- https://kiro.dev/pricing/

---

## Previous Updates

### 2026-08-25 (21:33 GMT+7) - Complete Rewrite

- Complete rewrite of all training materials
- All factual claims verified from official documentation
- All AWS Bedrock references removed
- Architecture corrected (Gateway → kiro-cli → Kiro services)
- Memory system limits documented
- Subagent concurrency corrected (3-32, not 11)

See `REWRITE_SUMMARY.md` for full details.
