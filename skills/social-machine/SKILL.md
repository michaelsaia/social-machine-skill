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
  scan → research → ideate → design → capture (optional) → post
```

Each stage produces artifacts that the next stage consumes. The user can also run any stage independently via its own slash command (`/social-scan`, `/social-research`, etc.).

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
- **Keep outputs organized.** All artifacts go in `.social-machine/output/` with date-stamped filenames.
- **Platform-specific optimization.** Captions, hashtags, dimensions, and tone should vary per platform. Instagram is visual-first with longer captions. X is punchy and concise. TikTok is casual and trend-aware.
