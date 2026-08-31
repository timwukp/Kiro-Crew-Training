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

### 2. PowerPoint Presentation
**File:** `kiro-crew-training.pptx` (~64KB)

**To view:**
- Open in PowerPoint, Keynote, or Google Slides
- 29 slides for 60-minute lecture (~2min per slide)

**Slide breakdown:**
- Opening: 3 slides (title, agenda, what you'll learn)
- Part 1 Introduction: 5 slides
- Part 2 Positioning: 7 slides (comparison, decision framework)
- Part 3 Features: 9 slides (6 features + 3 code examples)
- Part 4 Use Cases: 4 slides (real-world examples)
- Part 5 Getting Started: 3 slides (setup, best practices)
- Closing: 3 slides (takeaways, Q&A, thank you)

**Presentation style:**
- Dark theme (matches HTML website)
- Code blocks with syntax highlighting
- Comparison tables
- Feature deep-dives with examples

---

## 📋 Training Agenda (60 minutes)

**0:00-0:10** - Introduction
- What is Kiro Crew? (slides 4-8)
- Live demo: show HTML website

**0:10-0:20** - Positioning
- Kiro Crew vs Kiro IDE/CLI (slides 9-15)
- Why enterprises need both
- Decision framework

**0:20-0:40** - Features Deep Dive
- 6 core features (slides 16-21)
- 3 code examples (slides 22-24)
- Interactive walkthrough in HTML site

**0:40-0:55** - Use Cases & Demo
- 4 real-world examples (slides 25-28)
- Live demo in Kiro Crew dashboard
- Show actual subagent spawning, cron setup

**0:55-1:00** - Q&A
- Questions and next steps (slides 33-35)

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
- Open PPTX and review speaker notes
- Have Kiro Crew dashboard ready
- Prepare 2-3 PRs in a test repo for demo

### During the session:
- Start with HTML site (visual overview)
- Switch to PPTX for structured walkthrough
- Use HTML site for code example deep-dives
- Live demo in dashboard for "wow" moments
- Share HTML site link for self-paced learning

### After the session:
- Share both files (HTML + PPTX)
- Send setup guide (install Crew + kiro-cli device-code sign-in; no AWS CLI)
- Offer 1:1 setup help if needed

---

## 📦 Files Included

```
kiro-crew-training/
├── index.html                    # Interactive learning website (41KB)
├── kiro-crew-training.pptx      # 60-min presentation (68KB, 33 slides)
├── README.md                     # Overview and structure
├── presentation-brief.md         # Detailed slide outline
├── generate_pptx.py              # Script to regenerate PPTX
├── QUICK_START.md               # This file
└── venv/                         # Python virtual environment (for regeneration)
```

---

## 🔧 Regenerating the PPTX

If you need to modify the presentation:

```bash
cd kiro-crew-training
source venv/bin/activate
python generate_pptx.py
```

This regenerates `kiro-crew-training.pptx` with any changes you made to the script.

---

## ✅ Ready to Go!

You have everything needed for a complete 60-minute Kiro Crew training:
- ✅ Interactive HTML website with 6 sections, code examples, diagrams
- ✅ Professional PowerPoint with 33 slides, dark theme, code blocks
- ✅ Detailed README and quick start guide
- ✅ Demo suggestions and teaching tips

**Next step:** Open `index.html` in a browser to preview the full training content!
