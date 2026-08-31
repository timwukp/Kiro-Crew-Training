# Kiro Crew Training Presentation Brief (Verified)

> Rewritten 2026-08-31. All facts verified against live kiro.dev docs.
> Uncertain items are marked ⚠️ To be verified. This brief matches the
> 29-slide deck produced by `generate_pptx.py`.

## Presentation Details
- **Duration**: 60 minutes
- **Audience**: Enterprise customers with an existing Kiro subscription (IDE/CLI/Web/Mobile)
- **Goal**: Explain what Kiro Crew is, its unique value vs the other surfaces, and how to use it
- **Format**: Lecture + Demo + Q&A

## Core Correct Framing (do NOT drift from this)
- Kiro Crew is **one surface of the unified Kiro platform**, not a separate product.
- **One subscription** covers IDE, CLI, Web, Mobile, and Crew (+ ACP IDEs, CI/CD).
  Source: https://kiro.dev/pricing/
- Billing is **Kiro subscription credits** — NOT AWS Bedrock, NOT AWS billing.
- Architecture: **Gateway (local :5476) → kiro-cli (ACP) → Kiro model services (cloud)**.
  Source: https://kiro.dev/docs/crew/installation/
- Auth on first launch: **device-code sign-in** (account can be created via AWS Builder ID
  or social login per the pricing page).
- **No AWS CLI, no Bedrock model approval** needed.

## Slide Outline (29 slides ≈ 2 min each)

### Opening
1. **Title** — "Kiro Crew: Persistent, Self-Learning AI Agent"
2. **Agenda** — 60-min breakdown
3. **What You'll Learn** — key takeaways

### Part 1: Introduction
4. **What is Kiro Crew?** — persistent, self-learning, self-evolving local/remote agent
5. **The Kiro Ecosystem** — one agent, every surface; shared `.kiro/` config
6. **Architecture** — Gateway → kiro-cli (ACP) → Kiro services; data in `~/.kiro/crew/`
7. **⚠️ CRITICAL: NO AWS Bedrock** — correct billing/infra framing

### Part 2: Positioning (Crew vs IDE/CLI)
8. **Why Crew When You Have IDE/CLI** — persistence, autonomy, multi-channel
9. **Crew-Unique Features** — memory, subagents, cron, heartbeats, webhooks, task runner, artifacts, knowledge, multi-channel, multi-instance, snapshot
10. **When to Use What** — decision table
11. **Subscription & Credits** — $20/$40/$100/$200 = 1k/2k/5k/10k credits; add-on $0.04/credit;
    Opus 5 = 2.2x, Sonnet family ~1.3x, open-weight 0.05x–0.5x

### Part 3: Features Deep Dive
12. **Memory System (6 layers)** — Preferences 4,250 / Projects 6,400 / History 26,600 /
    Semantic 12,000 / Episodic 3,000 (top-8, max 10,000) / Lessons 37,250 (max 50)
13. **Memory decay & retention** — episodic decay formula; 365-day history retention
14. **Subagents** — 3–32 auto-sized, 30-min timeout, ~2-min stall detection
15. **Scheduling: Cron** — cron expr / `--every`; default timeout 1800s; jitter
16. **Scheduling: Heartbeats** — reactive, 60s tick, HEARTBEAT.md
17. **Scheduling: Webhooks** — `/api/hooks/agent`, max 6 concurrent, 10-min default timeout
18. **Task Runner** — spec → steps → execute → test → retry; checkpoints; Projects panel
19. **Artifacts** — versioned output; widget/HTML/markdown/SVG/JSON; ⚠️ version limit TBV
20. **Knowledge Library** — curated store; `local_knowledge_search`; ⚠️ size limits TBV

### Part 4: Enterprise Use Cases & Integration
21. **CI/CD Integration (3 patterns)** — CLI headless (`kiro-cli chat --no-interactive`,
    engine `--engine v3`), Crew webhooks, Crew cron
22. **Use Case: 24/7 PR monitoring** (heartbeat + Slack) — example scenario
23. **Use Case: Nightly security audit** (cron + subagents) — example scenario
24. **Use Case: Incident response** (webhook + memory + knowledge) — example scenario
25. **Use Case: Multi-repo migration** (task runner + subagents) — example scenario

### Part 5: Getting Started
26. **Installation** — Desktop app or CLI (`kirocrew setup/doctor/gateway`); device-code sign-in
27. **First Steps** — chat, schedule a job, teach a preference, run a task, delegate parallel work
28. **Resources** — docs links

### Closing
29. **Key Takeaways + Q&A**

## Visual Style
- Dark theme matching `index.html` (slate background, indigo/purple accents)
- Dark terminal-style code blocks
- Verification badges (✅ verified / ⚠️ to be verified) on factual slides
- Source URLs on slides carrying specific numbers

## Honesty Rules (mandatory)
- Verified facts stated directly; every specific number carries its source.
- Inferences labeled "typical"/"example"; never presented as real customer data.
- Unknowns marked "⚠️ To be verified — check latest docs".
- No fabricated costs, no fabricated customer names, no guessed quotas.

## ⚠️ To Be Verified (not in official docs as of 2026-08-31)
- Specific credit consumption per subagent session / cron run / task
- Real named customer case studies and ROI figures
- Some quota limits (max cron jobs, artifact version cap, knowledge library size)

## Verification Sources (fetched 2026-08-31)
- https://kiro.dev/docs/crew/ , /installation/ , /features/{memory,subagents,cron}/
- https://kiro.dev/docs/models/available-models/
- https://kiro.dev/docs/cli/headless/
- https://kiro.dev/pricing/
