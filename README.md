# Kiro Crew Training Materials

**🌐 Live site: [timwukp.github.io/Kiro-Crew-Training](https://timwukp.github.io/Kiro-Crew-Training/)** — open it in any browser, no setup needed.

60-minute comprehensive training on Kiro Crew — fully verified against the official docs at [kiro.dev/docs/crew](https://kiro.dev/docs/crew/) (verified 2026-08-31).

> The interactive HTML site (`index.html`) is published via GitHub Pages at the link above, and is also viewable locally (see below).

⚠️ **IMPORTANT**: This version corrects major errors in the original material:
- ✅ Kiro Crew uses Kiro subscription credits (NOT AWS Bedrock)
- ✅ One subscription for all Kiro surfaces (IDE, CLI, Web, Mobile, Crew)
- ✅ Crew is a surface/interface, not a separate product
- ✅ Setup through kiro-cli + Kiro account (NOT AWS CLI)

## Contents

### 1. Interactive HTML Website (`index.html`)
Self-paced learning website with:
- Introduction to Kiro Crew (corrected architecture)
- Kiro Crew's unique value in the Kiro ecosystem
- Deep dive into Crew-specific features
- Real-world enterprise use cases
- Code examples for every core feature
- Accurate architecture diagrams

**To view:**
```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory .
```
Then open: http://localhost:8000/index.html

### 2. Training Outline
The site delivers a full 60-minute lecture flow (see the outline below). A matching PowerPoint deck is produced from the same verified content but is **not distributed in this repository** — the interactive site is the canonical deliverable.

## Training Outline (60 minutes)

### Part 1: Introduction (10 min)
- What is Kiro Crew? (part of unified Kiro platform)
- Architecture: Gateway → kiro-cli → Kiro services
- How it fits with IDE/CLI/Web/Mobile

### Part 2: Kiro Crew's Unique Value (10 min)
- Persistence & 24/7 availability
- Self-learning memory system (6 layers)
- Multi-channel access (Slack, Discord, Teams)
- Autonomous operations
- When to use Crew vs IDE/CLI

### Part 3: Core Features Deep Dive (20 min)
- Memory (6-layer system with specific limits)
- Subagents (3-32 concurrent, auto-sized)
- Cron/Scheduling (3 patterns: cron, heartbeats, webhooks)
- Task Runner (autonomous execution with checkpoints)
- Artifacts (versioned output)
- Knowledge Library (curated docs)
- Feature-specific enterprise use cases and safe, repeatable live demos

### Part 4: Enterprise Use Cases & Integration (15 min)
- CI/CD integration (3 modes)
- 24/7 monitoring and alerting
- Multi-repo operations
- Team collaboration patterns
- Cost considerations

### Part 5: Getting Started & Q&A (5 min)
- Setup steps (correct process)
- First project walkthrough
- Questions

## Target Audience

Enterprise development teams who:
- Already use Kiro IDE/CLI for development
- Need persistent, autonomous agent capabilities
- Want 24/7 monitoring and automation
- Require multi-channel team access

## Prerequisites

For hands-on sections:
- ✅ Kiro subscription (Pro or higher)
- ✅ Kiro CLI installed and authenticated
- ✅ Kiro Crew installed (Mac app or CLI)
- ❌ NO AWS account required
- ❌ NO AWS CLI configuration needed
- ❌ NO Bedrock setup required

## Key Messages (Corrected)

1. **One Platform, Multiple Surfaces** - Kiro Crew is part of the unified Kiro platform
2. **Shared Subscription** - One subscription covers IDE, CLI, Web, Mobile, AND Crew
3. **Unique Capabilities** - Crew adds persistence, memory, scheduling that IDE/CLI don't have
4. **Local + Cloud** - Runs locally via Gateway, connects to Kiro's model services
5. **Credits-Based** - Uses same credit system as other Kiro surfaces

## Files

- `index.html` - Interactive training website (corrected architecture, published via GitHub Pages)
- `memory-layers.svg` - Six-memory-layers diagram used by the site
- `demo-task-spec.md` - Runnable Task Runner demo spec referenced in the site
- `demo-knowledge-source.md` - Fictional, public runbook for the Knowledge ingestion/retrieval demo
- `README.md` - This file
- `CORRECTIONS.md` - Detailed list of corrections from the original version
- `VERIFIED_OUTLINE.md` - Verified content outline
- `QUICK_START.md` - How to view and present the material
- `UPDATES.md` - Change log
- `REWRITE_SUMMARY.md` - Summary of the rewrite and its deliverables
- `SECURITY.md` - Security policy for this repository

## Verification Status

✅ **Verified from official docs** (https://kiro.dev/docs/):
- Architecture and components
- Memory system structure and limits
- Subagent concurrency (3-32, auto-sized)
- Cron/scheduling capabilities
- Feature availability

ℹ️ **Not published by Kiro** (so the materials do not state these as fact — check the usage dashboard / latest docs):
- Per-operation credit costs (subagent / cron / task)
- Real customer case studies
- Some quota limits (artifacts, cron jobs)

## License

Training material based on official Kiro documentation.
