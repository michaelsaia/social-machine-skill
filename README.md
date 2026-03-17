# Social Machine

AI-powered social media marketing pipeline for Claude Code.

Social Machine turns your project into a content machine. It scans your codebase for brand identity, researches current trends, generates post ideas with multiple caption variants, creates publish-ready graphics, and posts to your social platforms — all from a single `/social` command.

## Quick Start

```bash
# Install the skill
chmod +x scripts/install.sh
./scripts/install.sh

# In any project directory, run:
/social          # Full pipeline
/social-config   # Set up providers and platforms
/social-scan     # Extract brand identity from your codebase
```

## Features

- **Brand-aware**: Automatically extracts colors, logos, features, and tone from your codebase
- **Trend-informed**: Researches current social media trends before creating content
- **Multi-platform**: Creates optimized content for Instagram, X, TikTok, LinkedIn, Facebook
- **Auto-adapting dimensions**: One design → multiple platform-specific exports
- **3 caption variants**: Question hook, stat hook, and story hook for every post
- **Content variety**: Tracks post history and recommends diverse content types
- **Swappable providers**: Choose your tools for graphics (HTML/CSS, Figma, SVG) and posting (API, manual, browser)
- **Configurable**: Per-project settings, persistent brand profiles, provider switching

## Architecture

```
/social (orchestrator)
  ├── /social-scan      → Brand extraction
  ├── /social-research  → Trend research
  ├── /social-ideate    → Content ideas + captions
  ├── /social-design    → Graphics creation
  ├── /social-capture   → App screenshots
  └── /social-post      → Publishing
```

Each stage works independently or chains together. Providers are swappable:

| Capability | Providers |
|---|---|
| Graphics | html-screenshot (default), figma, svg, powerpoint |
| Video | elevenlabs, browser-recording, simulator-capture |
| Posting | manual (default), api, browser |

## Per-Project State

Social Machine stores per-project data in `.social-machine/`:

```
.social-machine/
├── brand.md          # Brand identity (auto-generated)
├── config.md         # Provider settings
├── credentials.env   # API keys (gitignored)
├── research-latest.md # Latest trend research
├── history/
│   └── posts.md      # Post history for variety tracking
└── output/           # Generated graphics and captions
```

## Requirements

- Claude Code with skill support
- For HTML/CSS graphics: headless browser (gstack/browse or Playwright)
- For Figma graphics: Figma MCP server configured
- For API posting: Platform API keys (see `/social-config`)
