# Social Machine Skill

AI-powered social media marketing pipeline for Claude Code.

## Project Structure

```
social-machine-skill/
├── skills/social-machine/       # All skill definitions
│   ├── SKILL.md                 # Orchestrator (/social)
│   ├── config/SKILL.md          # /social-config
│   ├── scan/SKILL.md            # /social-scan (brand extraction)
│   ├── research/SKILL.md        # /social-research (trend research)
│   ├── ideate/SKILL.md          # /social-ideate (content ideas + captions)
│   ├── design/                  # /social-design (graphics creation)
│   │   ├── SKILL.md
│   │   └── providers/           # Swappable graphics providers
│   ├── capture/SKILL.md         # /social-capture (screenshots)
│   ├── post/                    # /social-post (publishing)
│   │   ├── SKILL.md
│   │   └── providers/           # Swappable posting providers
│   ├── video/                   # /social-video (Phase 2)
│   │   ├── SKILL.md
│   │   └── providers/
│   └── templates/               # Template files
├── scripts/install.sh           # Installs symlinks to ~/.claude/skills/
├── CLAUDE.md                    # This file
├── TODOS.md                     # Deferred work
└── README.md                    # Public README
```

## Architecture

- **Provider pattern:** Graphics, video, and posting each have swappable providers. Config stored in per-project `.social-machine/config.md`.
- **Modular pipeline:** Each stage is an independent sub-skill that works alone or chained via the orchestrator.
- **Per-project state:** Brand profile, config, history, and output all live in `.social-machine/` in the target project directory.

## Development Guidelines

- Keep each SKILL.md under 500 lines
- Provider files are pure instructions — no code, just markdown that tells the LLM what to do
- New providers: add a .md file in the appropriate providers/ directory
- Test changes by running the skill against the Yoked project (../Yoked/)
- The install script creates symlinks — changes to this repo are immediately reflected

## Key Files for Each Provider

### Graphics Providers
- `design/providers/html-screenshot.md` — PRIMARY: HTML/CSS → headless browser screenshot
- `design/providers/figma.md` — Figma MCP integration
- `design/providers/svg.md` — Pure SVG fallback

### Posting Providers
- `post/providers/manual.md` — DEFAULT: save files for manual posting
- `post/providers/api/x.md` — X/Twitter API v2
- `post/providers/api/instagram.md` — Instagram Graph API
- `post/providers/api/tiktok.md` — TikTok Content Posting API
- `post/providers/browser.md` — Browser automation posting
