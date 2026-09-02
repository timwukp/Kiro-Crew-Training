#!/usr/bin/env python3
"""check_quality_pass.py — verification target for the quality-pass change.

Stdlib only, so CI needs no install step. Exit 0 = every criterion holds.
Each check asserts a REACHABLE/observable property, not merely that an
identifier exists somewhere — an earlier version of this eval passed while the
change was wrong because it only checked "does the id exist".
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read(name: str) -> str:
    p = ROOT / name
    return p.read_text(encoding="utf-8", errors="replace") if p.is_file() else ""


HTML = read("index.html")
README = read("README.md")
QUICK = read("QUICK_START.md")

TAB_PANELS = ["memory", "subagents", "scheduling", "tasks", "artifacts", "knowledge"]
NOT_DISTRIBUTED = ["generate_pptx.py", "kiro-crew-training.pptx", "presentation-brief.md"]

fails: list[str] = []
ids = set(re.findall(r'id="([^"]+)"', HTML))

# c1 — no machine-specific absolute path anywhere (also a username leak).
for p in sorted(ROOT.glob("*.md")) + sorted(ROOT.glob("*.html")):
    if re.search(r"/Users/[A-Za-z0-9._-]+/", p.read_text(encoding="utf-8", errors="replace")):
        fails.append(f"c1: machine-specific /Users/<name>/ path in {p.name}")

# c2 — canonical + Open Graph + Twitter + inline favicon.
head = HTML.split("</head>")[0]
if not re.search(r'<link[^>]+rel="canonical"', head, re.I):
    fails.append('c2: missing <link rel="canonical">')
for prop in ("og:title", "og:description", "og:type", "og:url", "og:image"):
    if f'"{prop}"' not in head:
        fails.append(f"c2: missing {prop}")
if "twitter:card" not in head:
    fails.append("c2: missing twitter:card")
if not re.search(r'rel="icon"[^>]*href="data:', head, re.I):
    fails.append("c2: favicon must be an inline data: URI (no external asset)")

# c3 — the diagram declares intrinsic dimensions (layout shift).
img = re.search(r"<img[^>]*memory-layers\.svg[^>]*>", HTML, re.I)
if not img:
    fails.append("c3: memory-layers.svg <img> not found")
else:
    if not re.search(r"\bwidth=", img.group(0)):
        fails.append("c3: <img> missing width")
    if not re.search(r"\bheight=", img.group(0)):
        fails.append("c3: <img> missing height")

# c4 — skip-link is the FIRST anchor in body, has a CSS rule, and resolves.
body = HTML.split("<body>", 1)[1] if "<body>" in HTML else HTML
m = re.search(r'<a\b[^>]*class="[^"]*skip-link[^"]*"[^>]*href="#([^"]+)"', body, re.I)
if not m:
    fails.append("c4: no skip-link anchor in <body>")
else:
    if m.group(1) not in ids:
        fails.append(f"c4: skip-link target #{m.group(1)} does not exist")
    first = re.search(r"<a\b", body, re.I)
    if first and first.start() != m.start():
        fails.append("c4: skip-link is not the first anchor in <body>")
    if not re.search(r"\.skip-link\b", HTML):
        fails.append("c4: no .skip-link CSS rule (must be hidden until focused)")

# c5 — tab ARIA is complete AND consistent, and the handler takes the element.
if not re.search(r'role="tablist"', HTML):
    fails.append('c5: missing role="tablist"')
if re.search(r"\bevent\.target\b", HTML):
    fails.append("c5: showTab still reads the implicit global event.target")
for t in TAB_PANELS:
    if len(re.findall(r"showTab\('%s',\s*this\)" % t, HTML)) != 1:
        fails.append(f"c5: expected exactly one showTab('{t}', this) call site")
    if len(re.findall(r'<button[^>]*aria-controls="%s"' % t, HTML)) != 1:
        fails.append(f"c5: expected exactly one tab button controlling '{t}'")
    if len(re.findall(r'<div id="%s" class="tab-content[^"]*" role="tabpanel"' % t, HTML)) != 1:
        fails.append(f"c5: panel '{t}' is not marked role=tabpanel")
    if f"tab-{t}" not in ids:
        fails.append(f"c5: button id 'tab-{t}' missing (aria-labelledby would dangle)")
if len(re.findall(r'aria-selected="true"', HTML)) != 1:
    fails.append('c5: exactly one tab must start aria-selected="true"')
if len(re.findall(r'class="tab-content active"', HTML)) != 1:
    fails.append("c5: exactly one panel must start active")

# c6 — no doc claims copy buttons while the site has none.
site_has_copy = bool(re.search(r"copyCode|copy-btn", HTML, re.I))
for name, txt in (("README.md", README), ("QUICK_START.md", QUICK)):
    if re.search(r"copy button", txt, re.I) and not site_has_copy:
        fails.append(f"c6: {name} claims copy buttons but index.html has none")

# c7 — docs citing non-distributed files say so.
for doc in ("REWRITE_SUMMARY.md", "UPDATES.md"):
    txt = read(doc)
    if any(f in txt for f in NOT_DISTRIBUTED) and not re.search(
        r"not distributed|git-ignored", txt, re.I
    ):
        fails.append(f"c7: {doc} cites non-distributed files without saying so")

# c8 — SECURITY.md appears in both manifests.
for name, txt in (("README.md", README), ("QUICK_START.md", QUICK)):
    if "SECURITY.md" not in txt:
        fails.append(f"c8: {name} does not list SECURITY.md")

# c9 — regression: no dead in-page anchors, no duplicate ids, quiz intact.
dead = [h for h in re.findall(r'href="#([^"]+)"', HTML) if h not in ids]
if dead:
    fails.append(f"c9: dead anchors {dead}")
all_ids = re.findall(r'id="([^"]+)"', HTML)
dupes = {i for i in all_ids if all_ids.count(i) > 1}
if dupes:
    fails.append(f"c9: duplicate ids {sorted(dupes)}")
for qid in ("quiz-form", "quiz-results"):
    if qid not in ids:
        fails.append(f"c9: quiz element '{qid}' missing")

if fails:
    print(f"FAIL ({len(fails)}):")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("PASS: all quality-pass criteria hold")
