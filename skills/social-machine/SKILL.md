---
name: social
version: 0.1.0
description: |
  AI-powered social media marketing pipeline. Use when the user wants to create social media
  content, posts, graphics, or marketing materials for their project. Triggers on: "social media",
  "create a post", "marketing content", "instagram post", "tweet", "tiktok", or "/social".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebSearch
  - WebFetch
  - Agent
---

# Social Machine: AI Marketing Pipeline

You are running the `/social` orchestrator. This chains sub-skills to produce publish-ready social media content for the user's project.

## Overview

Social Machine is a modular pipeline with swappable providers. It reads project config from `.social-machine/config.md` and brand identity from `.social-machine/brand.md`.

```
PIPELINE:
  scan → research → ideate → meme (optional) → stock (optional) → design → capture (optional) → post
```

Each stage produces artifacts that the next stage consumes. The user can also run any stage independently via its own slash command (`/social-scan`, `/social-research`, etc.).

---

## First-Time Welcome

If `.social-machine/` directory does NOT exist in the current project, this is a new user.
Display this welcome message before anything else:

```
Welcome to Social Machine! I'll help you create social media content for your project.

Here's what I can do:
• Scan your codebase to understand your brand (colors, logo, features)
• Research current social media trends in your niche
• Generate post ideas with optimized captions
• Create graphics — branded designs, real meme templates (Drake, Expanding Brain, etc.), or custom layouts
• Find royalty-free stock photos
• Capture app screenshots from simulators or browsers
• Post to Instagram, X, TikTok, LinkedIn, and Facebook

Let's get you set up. This takes about 2 minutes.
```

Then proceed to Step 0 (which will trigger config + scan since neither exists).

## Returning User Quick Menu

If `.social-machine/config.md` AND `.social-machine/brand.md` already exist, this is a
returning user. Skip the welcome and ask what they want to do:

Use AskUserQuestion with these options (adjust based on config):
- **A) Create a new post** — Run the full pipeline (research → ideate → design → post)
- **B) Make memes** — Scout trending formats and generate meme content (`/social-meme`) — **ONLY show this option if `memes_enabled: true` in config**
- **C) Just make a graphic** — Skip ideation, describe what you want and I'll design it
- **D) Research trends** — See what's working in your niche right now
- **E) Change settings** — Update providers, platforms, or brand profile

If the user provides a specific request (e.g., "make a Drake meme about our new feature"),
skip the menu and go directly to the relevant step.

---

## Step 0: Load Configuration

1. Check if `.social-machine/config.md` exists in the current project root.
   - If YES: read it and parse the YAML frontmatter for provider settings.
   - If NO: run the `/social-config` setup flow first (see `config/SKILL.md`).

2. Check if `.social-machine/brand.md` exists.
   - If YES: read it for brand identity context.
   - If NO: run the `/social-scan` brand extraction first (see `scan/SKILL.md`).

3. Check if `.social-machine/history/posts.md` exists.
   - If YES: read it to understand recent post history for content variety.
   - If NO: this is the first post — no history constraints.

---

## Step 1: Research (if not skipped)

Read the `research/SKILL.md` instructions and execute them. This produces:
- Current trends relevant to the project's niche
- Best-performing content formats right now
- Relevant hashtags per platform

Save research output to `.social-machine/research-latest.md` for the ideation stage.

**Skip condition:** If the user provides a specific post idea (e.g., "make a post about our new AI coaching feature"), skip research and go directly to ideation with their idea.

---

## Step 2: Ideate

Read the `ideate/SKILL.md` instructions and execute them. This produces:
- A post concept (content type, topic, angle)
- 3 caption variants with different hooks
- Suggested visual direction

Present all 3 caption variants to the user using AskUserQuestion. Let them pick one, request edits, or ask for more options.

---

## Step 2.5: Meme Engine (Optional)

**Pre-check:** Read `memes_enabled` from config.md. If `memes_enabled: false`, skip this
step entirely and do NOT suggest meme content types during ideation.

If `memes_enabled: true` AND the ideation stage selects content type "meme" or the user
requests meme/humor content:
1. Read `meme/SKILL.md` instructions and execute them
2. Scout trending meme formats via web search
3. Apply style transfer — adapt trending formats to the brand
4. Generate 3-5 meme concepts for user selection
5. Hand off approved concept to design stage with meme-specific brief

The design stage will use meme layout patterns from `design/providers/meme-layouts.md`
for HTML/CSS meme generation, and/or the memegen API for classic templates.

**Skip conditions:**
- `memes_enabled: false` in config → always skip
- User wants standard branded content (feature spotlight, quote card, etc.) → skip

---

## Step 2.7: Stock Images (Optional)

If the visual direction calls for photography (backgrounds, lifestyle imagery, product-in-use shots):
1. Read `stock/SKILL.md` instructions and execute them
2. Search royalty-free sources (Unsplash, Pexels, Pixabay) for images matching the concept
3. Download selected images to `.social-machine/output/stock/`
4. Track licenses in `.social-machine/output/stock/LICENSES.md`

The design stage will incorporate these images into the graphic.

**Skip condition:** If the design is purely typographic (quote cards, stat graphics) or uses only app screenshots, skip this step.

---

## Step 3: Design

Read the `design/SKILL.md` instructions and execute them. This:
1. Reads `config.md` to determine the graphics provider
2. Loads the appropriate provider file from `design/providers/`
3. Creates the graphic at platform-specific dimensions for each target platform
4. Saves output images to `.social-machine/output/`

Show the user the output file paths so they can preview the graphics.

---

## Step 4: Capture (Optional)

If the post concept involves app screenshots or screen recordings:
1. Read `capture/SKILL.md` instructions
2. Capture screenshots from iOS simulator or browser
3. These may be embedded into the design, or used as standalone post images

**Skip condition:** If the design doesn't require app screenshots, skip this step.

---

## Step 5: Post

Read the `post/SKILL.md` instructions and execute them. This:
1. Reads `config.md` to determine the posting provider and target platforms
2. Checks `auto_post` setting in config
3. If `auto_post: false` (default): shows the final graphic + caption and asks for confirmation via AskUserQuestion with options: Post it / Edit caption / Regenerate graphic / Cancel
4. If `auto_post: true`: posts directly without confirmation
5. Loads the appropriate provider file from `post/providers/`
6. Executes the post (or saves files for manual posting)
7. Logs the post to `.social-machine/history/posts.md`

---

## Step 6: Log & Report

After posting (or saving for manual posting), update the history log:

Append a row to `.social-machine/history/posts.md`:
```
| {date} | {platform} | {content_type} | {topic} | {caption_hook} |
```

Then report to the user:
- What was created
- Where files are saved
- What was posted (or instructions for manual posting)
- Suggest what to post next based on content variety analysis

---

## Important Rules

- **Always read config before doing anything.** If config is missing, set it up first.
- **Always read brand profile.** The brand colors, tone, and audience must inform every decision.
- **Never post without the user's knowledge.** Even with `auto_post: true`, log everything.
- **Respect provider choices.** Don't use Figma if the user configured html-screenshot. Don't use API posting if they chose manual.
- **Respect meme preference.** If `memes_enabled: false` in config, do NOT suggest meme content types or offer the meme menu option. Some brands (B2B, enterprise, medical, legal) are not meme-appropriate.
- **Keep outputs organized.** All artifacts go in `.social-machine/output/` with date-stamped filenames.
- **Platform-specific optimization.** Captions, hashtags, dimensions, and tone should vary per platform. Instagram is visual-first with longer captions. X is punchy and concise. TikTok is casual and trend-aware.

## Fit Content to the Project

**This is critical.** Social Machine works on ANY project — fitness apps, SaaS dashboards,
developer tools, e-commerce stores, personal blogs, non-profits, restaurants, etc. You MUST
adapt your content strategy to the specific project you're working on.

After reading `brand.md`, analyze the project type and adjust:

### Content Tone Mapping
```
PROJECT TYPE          → CONTENT STYLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Consumer app (fitness,   Energetic, motivational, lifestyle-focused.
food, social, dating)    Memes work great. Casual language. Emoji OK.

SaaS / B2B product       Professional but not boring. Focus on ROI,
                          productivity, problem-solving. Memes only if
                          the audience skews young (dev tools, startups).

Developer tool /          Technical credibility matters. Code snippets
open source               in graphics. Memes about developer culture
                          land well. No corporate fluff.

E-commerce / DTC          Product-forward. Lifestyle imagery. UGC-style
                          content. Seasonal/trend-driven. Memes for
                          community building.

Creative / agency         Portfolio-style. High design standards. Show
                          process and results. Memes feel off-brand
                          unless the brand is intentionally irreverent.

Non-profit / cause        Mission-driven. Impact stories. Stat graphics
                          about the cause. Memes rarely appropriate
                          unless it's a youth-focused org.

Local business            Community-focused. Behind-the-scenes. Staff
(restaurant, gym, etc)    highlights. Local events. Memes can work
                          for casual businesses.
```

### Adaptation Checklist

When generating ANY content, verify:
1. **Does this match the brand's tone?** (from brand.md `tone` field)
2. **Would the target audience relate?** (from brand.md `audience` field)
3. **Does the visual style fit the industry?** Dark/bold for fitness ≠ light/clean for wellness ≠ code-forward for dev tools
4. **Are the references and humor niche-appropriate?** Gym memes don't work for accounting software
5. **Is the vocabulary right?** "Gains" and "PRs" for fitness. "Ship" and "deploy" for dev tools. "ROI" and "pipeline" for B2B.
6. **Does the CTA make sense?** "Link in bio" for apps. "Try it free" for SaaS. "Shop now" for e-commerce.
