# Kiro Crew Training Materials - Rewrite Summary

**Date:** August 25, 2026  
**Status:** ✅ COMPLETED  
**Verification Level:** All factual claims sourced from official docs (verified 2026-08-31)

---

## 🎯 What Was Done

Complete rewrite of all training materials based on verified official documentation from kiro.dev.

> **Distribution note:** `generate_pptx.py`, `kiro-crew-training.pptx` and
> `presentation-brief.md` are listed below for historical accuracy but are **not
> distributed in this repository** (the first two are git-ignored). The interactive
> site (`index.html`) is the canonical deliverable.

### Files Updated

1. **index.html** (63 KB, 1,552 lines)
   - ✅ Fully rewritten with verified content
   - ✅ Modern, interactive design
   - ✅ All sections include verification badges
   - ✅ Direct links to official documentation

2. **kiro-crew-training.pptx** (62 KB, 29 slides)
   - ✅ Completely regenerated from verified content
   - ✅ Clean, professional design
   - ✅ Verification status on each slide
   - ✅ ~60 minutes of content

3. **generate_pptx.py** (21 KB, 627 lines)
   - ✅ Rewritten with verified content
   - ✅ Includes verification badges
   - ✅ Proper source attribution

4. **Supporting Documentation**
   - ✅ CORRECTIONS.md (7.7 KB) - All errors documented
   - ✅ VERIFIED_OUTLINE.md (11 KB) - Content blueprint
   - ✅ README.md (3.9 KB) - Updated instructions

---

## 🔥 Critical Errors Corrected

### 1. Billing & Infrastructure (MOST CRITICAL)

| Original (WRONG) | Corrected (VERIFIED) |
|------------------|----------------------|
| ❌ Runs on AWS Bedrock | ✅ Uses Kiro subscription credits via Kiro services |
| ❌ Requires AWS CLI setup | ✅ No AWS CLI needed (uses kiro-cli via ACP) |
| ❌ Billing through AWS | ✅ Kiro subscription ($20-$200/month) |
| ❌ Need Bedrock model approval | ✅ Models available through Kiro subscription |

**Impact:** This was presenting Kiro Crew as an AWS product, which is completely incorrect.

### 2. Product Positioning (CRITICAL)

| Original (WRONG) | Corrected (VERIFIED) |
|------------------|----------------------|
| ❌ Separate product from IDE/CLI | ✅ One surface of unified Kiro platform |
| ❌ Different billing systems | ✅ Single subscription for all surfaces |
| ❌ Need "both products" | ✅ One subscription includes all |

**Impact:** This was confusing the product positioning and customer value proposition.

### 3. Model Availability (CRITICAL)

| Original (WRONG) | Corrected (VERIFIED) |
|------------------|----------------------|
| ❌ Claude Opus 4 in private preview | ✅ Claude Opus 5 Active (July 24, 2026) |
| ❌ No Opus 5 / Sonnet 5 | ✅ Claude Sonnet 5 Active (June 30, 2026) |
| ❌ Need to enable models | ✅ Available through subscription |

**Impact:** Training materials were referencing outdated/non-existent models.

### 4. Technical Specifications

| Original (WRONG) | Corrected (VERIFIED) |
|------------------|----------------------|
| ❌ Up to 11 concurrent subagents | ✅ 3-32 concurrent (auto-sized) |
| ❌ Memory limits unspecified | ✅ All 6 layers with specific limits documented |
| ❌ Architecture unclear | ✅ Gateway → kiro-cli → Kiro services |

---

## ✅ Verified Content (all facts sourced)

### Architecture
- ✅ Gateway (local Python server, port 5476)
- ✅ kiro-cli (Agent Client Protocol)
- ✅ Kiro Model Services (cloud)
- ✅ Local storage: `~/.kiro/crew/`
- ✅ Authentication: device-code sign-in on first launch (account via AWS Builder ID or social login)

### Memory System (6 Layers)
- ✅ Layer 1: Preferences (4,250 chars)
- ✅ Layer 2: Projects (6,400 chars)
- ✅ Layer 3: Recent History (26,600 chars)
- ✅ Layer 4: Semantic Memory (12,000 chars)
- ✅ Layer 5: Episodic Memory (3,000 chars, top-8)
- ✅ Layer 6: Lessons (37,250 chars, max 50)

### Subagents
- ✅ Concurrency: 3-32 (auto-sized)
- ✅ Timeout: 30 minutes
- ✅ Stall detection: ~2 minutes
- ✅ Context: Isolated with memory injection

### Scheduling (3 Modes)
- ✅ Cron jobs (standard expressions)
- ✅ Heartbeats (reactive, 60s tick)
- ✅ Webhooks (max 6 concurrent)

### Features
- ✅ Task Runner (decompose → execute → test → retry)
- ✅ Artifacts (versioned outputs, optional AWS deploy)
- ✅ Knowledge Library (document ingestion, search)

### Subscription
- ✅ Single subscription for all surfaces
- ✅ Credits: $20-$200/month (1K-10K credits)
- ✅ Model multipliers documented
- ✅ Add-on: $0.04/credit

---

## ℹ️ Not Published by Kiro (NOT stated as fact in the materials)

### Specific Credit Consumption
- ⚠️ How many credits per subagent session?
- ⚠️ How many credits per cron job run?
- ⚠️ Average Task Runner costs?

### Quotas
- ⚠️ Maximum number of cron jobs?
- ⚠️ Artifact version limits?
- ⚠️ Knowledge Library size limits?

### Customer Examples
- ⚠️ Real customer case studies
- ⚠️ Real ROI data
- ⚠️ Named deployments

**Approach:** Clearly labeled as "⚠️ To Be Verified" throughout materials. Used "example scenarios" and "typical" language instead of claiming facts.

---

## 📚 Sources Used

All verified content sourced from:

- https://kiro.dev/docs/
- https://kiro.dev/docs/crew/
- https://kiro.dev/docs/crew/installation/
- https://kiro.dev/docs/crew/features/
- https://kiro.dev/docs/crew/features/memory/
- https://kiro.dev/docs/crew/features/subagents/
- https://kiro.dev/docs/crew/features/cron/
- https://kiro.dev/docs/crew/features/task-runner/
- https://kiro.dev/docs/crew/features/knowledge/
- https://kiro.dev/docs/models/available-models/
- https://kiro.dev/pricing/

**Date reviewed:** August 25, 2026

---

## 📦 Deliverables

### Interactive HTML Website (63 KB)
- **Path:** `index.html`
- **Features:**
  - Responsive design
  - Tab navigation for features
  - Verification badges on each section
  - Direct links to official docs
  - Modern gradient design
  - Smooth animations
- **Duration:** Self-paced browsing

### PowerPoint Presentation (62 KB)
- **Path:** `kiro-crew-training.pptx`
- **Slides:** 29 slides
- **Duration:** ~60 minutes
- **Features:**
  - Professional dark theme
  - Verification badges
  - Clear section dividers
  - Tables and two-column layouts
  - Source attribution

### Documentation
- **CORRECTIONS.md** - Detailed error corrections
- **VERIFIED_OUTLINE.md** - Content blueprint
- **README.md** - Quick start guide
- **REWRITE_SUMMARY.md** - This file

---

## 🎓 Training Content Structure

### Part 1: Introduction (10 min)
- What is Kiro Crew?
- Kiro ecosystem ("One agent, every surface")
- Architecture (Gateway → kiro-cli → Kiro services)

### Part 2: Why Crew? (10 min)
- IDE/CLI vs Crew comparison
- When to use what
- Complementary, not replacement

### Part 3: Features Deep Dive (20 min)
- 6-layer memory system
- Subagents (3-32 concurrent)
- Scheduling (cron/heartbeats/webhooks)
- Task Runner
- Artifacts & Knowledge

### Part 4: Use Cases (15 min)
- 24/7 PR monitoring
- Nightly security audits
- Incident response
- Multi-repo migrations
- CI/CD integration (3 modes)

### Part 5: Getting Started (5 min)
- Installation (Desktop app or CLI)
- First steps
- Resources

---

## ✅ Quality Assurance

### Verification Process
1. ✅ Read all relevant official documentation
2. ✅ Cross-referenced multiple sources
3. ✅ Documented verification status for each claim
4. ✅ Marked uncertain information explicitly
5. ✅ Provided source links for all verified facts

### Honesty Standards
- ✅ No fabricated statistics
- ✅ No invented customer cases
- ✅ No guessed technical limits
- ✅ Clear distinction between verified facts and examples
- ✅ "To be verified" clearly marked

### Design Quality
- ✅ Professional visual design
- ✅ Consistent branding
- ✅ Accessible color contrast
- ✅ Responsive layout (HTML)
- ✅ Clear information hierarchy

---

## 🔄 How to Update Materials

When new information becomes available:

1. **Update CORRECTIONS.md** - Move items from "To Be Verified" to "Verified"
2. **Update VERIFIED_OUTLINE.md** - Add new verified information
3. **Update index.html** - Add content, change badges from ⚠️ to ✓
4. **Update generate_pptx.py** - Modify slide content
5. **Regenerate PPTX** - Run `python3 generate_pptx.py`
6. **Update this file** - Document changes made

---

## 📝 Key Takeaways for Trainers

### Core Messages (100% Verified)
1. Kiro Crew is ONE SURFACE of the Kiro platform, not a separate product
2. Single subscription covers IDE, CLI, Web, Mobile, AND Crew
3. Architecture: Gateway → kiro-cli → Kiro services (NOT AWS Bedrock)
4. No AWS configuration needed (unless deploying artifacts)
5. Crew adds persistence, autonomy, and memory to the Kiro agent

### Common Misconceptions to Correct
1. ❌ "Kiro Crew runs on AWS Bedrock" → ✅ Uses Kiro subscription services
2. ❌ "Need AWS CLI setup" → ✅ Only need kiro-cli (included)
3. ❌ "Separate billing from IDE" → ✅ Single subscription
4. ❌ "11 concurrent subagents" → ✅ 3-32 (auto-sized)
5. ❌ "Opus 4" → ✅ Opus 5 (launched July 2026)

### When Asked About Unverified Items
Use this language:
- "Specific credit consumption varies by usage. Monitor your dashboard."
- "Based on documented capabilities, typical scenarios would..."
- "For current limits, please refer to the latest documentation at kiro.dev"

---

## 🎯 Success Metrics

### Content Quality
- ✅ All factual claims verified from official sources
- ✅ Items Kiro does not publish are excluded, not guessed
- ✅ Zero fabricated facts or statistics
- ✅ All sources documented and linked

### Deliverable Completeness
- ✅ Interactive HTML website
- ✅ 60-minute PowerPoint presentation
- ✅ Supporting documentation
- ✅ Generation scripts for reproducibility

### Accuracy
- ✅ All critical errors corrected
- ✅ Architecture diagrams accurate
- ✅ Technical specifications verified
- ✅ Model information current (August 2026)

---

## 📞 Support & Feedback

For questions or updates to these materials:

1. **Official Documentation:** https://kiro.dev/docs/crew/
2. **Pricing:** https://kiro.dev/pricing/
3. **Installation Guide:** https://kiro.dev/docs/crew/installation/

For feedback on training materials, contact training content team.

---

**Last Updated:** August 25, 2026, 21:33 (GMT+7)  
**Status:** ✅ Production Ready  
**Next Review:** When official documentation updates
