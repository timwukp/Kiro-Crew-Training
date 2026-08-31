# Security Policy

## About this repository

This repository contains **educational training material** for Kiro Crew — a
static HTML website (published via GitHub Pages), a diagram, and Markdown docs.
It ships **no executable application code, no server, and no dependencies to
install**. There is therefore no runtime attack surface in what this repo
distributes.

## Scope

Security-relevant issues we care about here are limited to the content itself:

- **Factual errors** about Kiro Crew security behavior that could mislead a
  reader (e.g. an incorrect statement about sandboxing, denied commands, or
  credential handling). All security claims in the site are sourced from the
  official docs at <https://kiro.dev/docs/crew/security/>.
- **Broken or spoofed links** that point somewhere other than the official
  `kiro.dev` documentation.
- **Accidentally committed secrets** (there should be none — the material uses
  placeholders only).

For vulnerabilities in **Kiro Crew itself** (the product), report them upstream
at <https://github.com/kirodotdev/Kiro/issues> or via Kiro's official channels —
not here.

## Reporting

Open an issue on this repository, or contact the maintainer (**@timwukp**)
through GitHub. There is no formal SLA for this educational repo; issues are
addressed on a best-effort basis.

## Supported content

Only the current `main` branch is maintained. The material is verified against
the official Kiro documentation as of the date shown in the site footer.
