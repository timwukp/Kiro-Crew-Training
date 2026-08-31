# Quick Start Guide

## 🎯 You now have two complete 60-minute training materials:

### 1. Interactive HTML Website
**File:** `index.html` (~65KB)

**To view:**
```bash
cd kiro-crew-training
python3 -m http.server 8000 --bind 127.0.0.1
```

Then open: http://localhost:8000/index.html

**Features:**
- Self-paced learning with navigation
- 6 major sections
- 6 interactive code examples with copy buttons
- Architecture diagrams
- Smooth scrolling, dark theme
- Works offline once loaded

**Sections:**
1. Introduction - What is Kiro Crew?
2. Positioning - vs Kiro IDE/CLI, why enterprises need both
3. Features Deep Dive - 6 core capabilities
4. Use Cases - 6 real-world examples
5. Code Examples - Copy-paste ready demos
6. Architecture & Summary

---

### 2. Presentation (not in this repo)
A matching 60-minute slide deck was produced from the same verified content, but it is **not distributed in this repository** — the interactive HTML site is the canonical deliverable and covers the full 60-minute flow on its own. If you have the deck file locally, open it in PowerPoint, Keynote, or Google Slides; otherwise present directly from the website.

---

## 📋 Training Agenda (60 minutes)

**0:00-0:10** - Introduction
- What is Kiro Crew? (Introduction section)
- Live demo: show HTML website

**0:10-0:20** - Positioning
- Kiro Crew vs Kiro IDE/CLI (Why Crew section)
- Why enterprises need both
- Decision framework

**0:20-0:40** - Features Deep Dive
- 6 core features (Features section tabs)
- Code examples on each tab
- Interactive walkthrough in HTML site

**0:40-0:55** - Use Cases & Demo
- 4 real-world examples (Enterprise Use Cases section)
- Live demo in Kiro Crew dashboard
- Show actual subagent spawning, cron setup

**0:55-1:00** - Q&A
- Questions and next steps

---

## 🎬 Demo Suggestions

### Demo 1: Persistent Memory (5 min)
Show in dashboard:
1. "Always use snake_case for Python"
2. Agent learns via learn_add
3. Open new session, ask to write Python code
4. Shows snake_case without reminder

### Demo 2: Spawn Subagents (5 min)
In dashboard:
1. "Review these 3 PRs: #123, #124, #125"
2. Show spawn_run call
3. Dashboard shows 3 subagents running
4. Wait for results, show synthesis

### Demo 3: Cron Job (3 min)
1. "Check open PRs every 30 minutes"
2. Show cron_add call
3. Dashboard → Scheduled Jobs tab
4. Show job listed, next run time

---

## 💡 Tips for Teaching

### Before the session:
- Test HTML site loads correctly
- Have Kiro Crew dashboard ready
- Prepare 2-3 PRs in a test repo for demo

### During the session:
- Present from the HTML site (visual overview + structured walkthrough)
- Use the Features tabs for code example deep-dives
- Live demo in dashboard for "wow" moments (cron trigger, task runner)
- Share HTML site link for self-paced learning

### After the session:
- Share the site link: https://timwukp.github.io/Kiro-Crew-Training/
- Send setup guide (install Crew + kiro-cli device-code sign-in; no AWS CLI)
- Offer 1:1 setup help if needed

---

## 📦 Files Included

```
kiro-crew-training/            (repo)
├── index.html                 # Interactive learning website
├── memory-layers.svg          # Six-memory-layers diagram
├── demo-task-spec.md          # Runnable Task Runner demo spec
├── README.md                  # Overview and structure
├── VERIFIED_OUTLINE.md        # Verified content outline
├── CORRECTIONS.md             # Verification status
├── UPDATES.md                 # Change log
└── QUICK_START.md             # This file
```

---

## ✅ Ready to Go!

You have everything needed for a complete 60-minute Kiro Crew training:
- ✅ Interactive HTML website with all sections, code examples, diagrams
- ✅ Detailed README and quick start guide
- ✅ Demo suggestions and teaching tips

**Next step:** Open `index.html` in a browser to preview the full training content!
