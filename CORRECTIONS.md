# Corrections & Verification Status

This document lists all corrections from the original training material and verification status of each claim.

## ❌ Major Errors Corrected

### 1. Billing & Infrastructure (CRITICAL ERROR)

**Original (WRONG):**
- Kiro Crew runs on AWS Bedrock
- Requires AWS CLI configuration (`aws configure`)
- Billing through AWS account
- Need to enable Bedrock model access

**Corrected (VERIFIED):**
- ✅ **Kiro Crew uses Kiro subscription credits**
  - Source: https://kiro.dev/pricing/ - "Kiro subscriptions can be used with Kiro IDE, Kiro CLI, Kiro on the web, Kiro Crew"
- ✅ **No AWS CLI needed**
  - Source: https://kiro.dev/docs/crew/installation/ - Uses kiro-cli via ACP, not AWS
- ✅ **Billing: Kiro subscription ($20-$200/month for credits)**
  - Source: https://kiro.dev/pricing/
- ✅ **Setup: Install Crew + authenticate kiro-cli**
  - Source: https://kiro.dev/docs/crew/installation/

### 2. Product Positioning (CRITICAL ERROR)

**Original (WRONG):**
- Kiro Crew is separate product from Kiro IDE/CLI
- Enterprises need "both products"
- Different billing systems

**Corrected (VERIFIED):**
- ✅ **Kiro Crew is ONE SURFACE of the unified Kiro platform**
  - Source: https://kiro.dev/docs/ - "One agent, every surface"
- ✅ **Single subscription covers all surfaces**
  - Source: https://kiro.dev/pricing/ - "Kiro subscriptions can be used with... Kiro Crew"
- ✅ **Shared .kiro/ configuration across all surfaces**
  - Source: https://kiro.dev/docs/ - "Your .kiro/ configuration is shared across all of them"

### 3. Model Access (CRITICAL ERROR)

**Original (WRONG):**
- Need to enable AWS Bedrock models
- Claude Opus 4 in private preview
- No Claude Opus 5 / Sonnet 5

**Corrected (VERIFIED):**
- ✅ **Models available through Kiro subscription**
  - Source: https://kiro.dev/docs/models/available-models/
- ✅ **Claude Opus 5 EXISTS and is Active** (launched July 24, 2026)
  - Source: https://kiro.dev/docs/models/available-models/
- ✅ **Claude Sonnet 5 EXISTS and is Active** (launched June 30, 2026)
  - Source: https://kiro.dev/docs/models/available-models/
- ✅ **Auto model router available**
  - Source: https://kiro.dev/docs/models/available-models/

---

## ✅ Verified Information (From Official Docs)

### Architecture

**Gateway → kiro-cli → Kiro Services**
- ✅ Gateway is local Python server (port 5476)
- ✅ Communicates via Agent Client Protocol (ACP)
- ✅ kiro-cli connects to Kiro's model services
- ✅ Data stored locally in `~/.kiro/crew/`
- Source: https://kiro.dev/docs/crew/installation/

### Memory System (6 Layers)

| Layer | Capacity | Source |
|-------|----------|--------|
| Preferences | 4,250 chars | https://kiro.dev/docs/crew/features/memory/ |
| Projects | 6,400 chars | https://kiro.dev/docs/crew/features/memory/ |
| History | 26,600 chars | https://kiro.dev/docs/crew/features/memory/ |
| Semantic | 12,000 chars | https://kiro.dev/docs/crew/features/memory/ |
| Episodic | 3,000 chars (top-8), max 10,000 entries | https://kiro.dev/docs/crew/features/memory/ |
| Lessons | 37,250 chars, max 50 lessons | https://kiro.dev/docs/crew/features/memory/ |

### Subagents

- ✅ Concurrency: **3-32 (auto-sized based on machine resources)**
  - Source: https://kiro.dev/docs/crew/features/subagents/ - "usually 3–32"
  - ❌ NOT 11 as originally stated
- ✅ Timeout: 30 minutes hard limit
- ✅ Stall detection: ~2 minutes of no activity
- Source: https://kiro.dev/docs/crew/features/subagents/

### Scheduling

**Three modes:**
1. ✅ Cron jobs (scheduled tasks)
2. ✅ Heartbeats (reactive monitoring, 60s tick)
3. ✅ Webhooks (external triggers, max 6 concurrent)
- Source: https://kiro.dev/docs/crew/features/cron/

### Crew-Specific Features

**Features ONLY in Crew (not in IDE/CLI):**
- ✅ Persistent memory (6-layer system)
- ✅ Subagents
- ✅ Cron/Scheduling
- ✅ Heartbeats
- ✅ Webhooks
- ✅ Task Runner
- ✅ Artifacts (versioned)
- ✅ Knowledge Library
- ✅ Multi-instance management
- ✅ Multi-channel access (Slack/Discord/Teams)
- ✅ Snapshot & restore
- Source: https://kiro.dev/docs/crew/features/

---

## ⚠️ To Be Verified (Not Found in Official Docs)

### Credit Costs

**Not documented:**
- ⚠️ How many credits does one subagent session consume?
- ⚠️ How many credits does one cron job run consume?
- ⚠️ Average cost of a Task Runner task?
- ⚠️ Real-world cost examples?

**What we know:**
- ✅ Different models have different multipliers (Opus 5 = 2.2x verbatim; Sonnet family ~1.3x; open-weight 0.05x–0.5x)
- ✅ Credits are metered to 0.01 precision
- ✅ Add-on credits cost $0.04 each
- Source: https://kiro.dev/pricing/

**Reasonable inference:**
- Subagents and cron jobs likely consume credits based on the model calls they make
- Cost scales with task complexity and model choice
- **We will state this as inference, not fact**

### Quota Limits

**Not explicitly documented:**
- ⚠️ Maximum number of cron jobs?
- ⚠️ Artifact version limit? (may exist but not found in docs reviewed)
- ⚠️ Knowledge Library size limit?
- ⚠️ Maximum MCP servers?

**What we know:**
- ✅ Subagent concurrency: 3-32 auto-sized
- ✅ Webhook concurrency: max 6
- ✅ Memory limits: documented above
- ✅ History retention: 365 days

### Real Customer Examples

**Not found:**
- ⚠️ Named customer case studies
- ⚠️ Real ROI data
- ⚠️ Specific deployment examples

**What we will do:**
- Use "typical scenarios" or "example workflows"
- Clearly label as examples, not real cases
- Base scenarios on documented capabilities

---

## 📋 How We Handle Unverified Information

### For Training Materials:

1. **Verified facts**: State directly with confidence
2. **Reasonable inferences**: Clearly label as "typical" or "estimated"
3. **Unknown information**: 
   - Option A: Omit entirely
   - Option B: State "⚠️ To be verified - check latest documentation"
   - Option C: Provide calculation method instead of specific numbers

### Examples:

**✅ GOOD (Verified):**
> "Kiro Crew can run 3-32 subagents concurrently, auto-sized based on your machine's resources."

**✅ GOOD (Sourced, no fabricated numbers):**
> "Credit consumption scales with the model's multiplier (Opus 5 = 2.2x, Sonnet family ~1.3x, open-weight 0.05x–0.5x) and the number of model calls an operation makes. Kiro does not publish a per-operation figure, so measure your own workload in the usage dashboard."

**❌ BAD (Fabricated):**
> "A typical enterprise using Kiro Crew spends $500/month on credits."

**✅ GOOD (Transparent):**
> "⚠️ Specific cost examples vary by usage. Refer to Kiro pricing documentation for your use case."

---

## 🎯 Verification Sources Used

All corrections and verified facts come from:
- https://kiro.dev/docs/
- https://kiro.dev/docs/crew/
- https://kiro.dev/docs/crew/installation/
- https://kiro.dev/docs/crew/features/
- https://kiro.dev/docs/crew/features/subagents/
- https://kiro.dev/docs/crew/features/cron/
- https://kiro.dev/docs/crew/features/memory/
- https://kiro.dev/docs/models/available-models/
- https://kiro.dev/pricing/

Reviewed: August 25, 2026

---

## 📝 Change Summary

| Topic | Original | Corrected | Confidence |
|-------|----------|-----------|------------|
| Billing | AWS Bedrock | Kiro subscription | ✅ Verified |
| Setup | AWS CLI | kiro-cli | ✅ Verified |
| Product type | Separate product | One surface | ✅ Verified |
| Opus 5 | "Doesn't exist" | Active (July 2026) | ✅ Verified |
| Sonnet 5 | "Doesn't exist" | Active (June 2026) | ✅ Verified |
| Subagent concurrency | 11 | 3-32 (auto) | ✅ Verified |
| Memory limits | Unspecified | Documented limits | ✅ Verified |
| Crew-unique features | Unclear | 11 specific features | ✅ Verified |
| Credit costs | Fabricated | To be verified | ⚠️ Unknown |
| Customer cases | Fabricated | Will use examples | ⚠️ Unknown |
