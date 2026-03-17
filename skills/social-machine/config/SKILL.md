---
name: social-config
version: 0.1.0
description: |
  Configure Social Machine providers and settings. Use when the user wants to set up or change
  their social media posting workflow, switch graphics tools, change posting method, or run
  "/social-config".
allowed-tools:
  - Read
  - Write
  - Edit
  - AskUserQuestion
  - Glob
---

# Social Machine: Configuration

You are running `/social-config`. This sets up or modifies the Social Machine configuration for the current project.

---

## Step 1: Check Existing Config

Read `.social-machine/config.md` if it exists. If it does, show the current settings and ask what the user wants to change. If it doesn't exist, run the full setup flow.

---

## Step 2: Graphics Provider

Ask the user which tool they want to use for creating graphics:

Options:
- **html-screenshot** (Recommended) — Claude generates HTML/CSS, headless browser screenshots it. Best brand precision, most portable. Works everywhere with a browser.
- **figma** — Uses Figma MCP to create designs. Professional tool, requires Figma account + MCP configured.
- **svg** — Pure SVG code generation. Zero dependencies but limited for complex layouts.
- **powerpoint** — Generate PPTX files. Good for teams that use PowerPoint/Google Slides.

Default: `html-screenshot`

---

## Step 3: Video Provider

Ask the user if they want video content support:

Options:
- **none** (Default) — No video generation. Focus on static images.
- **elevenlabs** — AI voiceover for UGC-style content. Requires ElevenLabs API key.
- **browser-recording** — Screen recordings via headless browser. Good for app demos.
- **simulator-capture** — iOS Simulator screen recordings. Good for mobile app demos.

Default: `none`

---

## Step 4: Posting Provider

Ask the user how they want to publish content:

Options:
- **manual** (Default) — Saves graphic + caption to output folder. User posts manually. Zero setup required.
- **api** — Posts directly via platform APIs. Requires API keys per platform. Most automated.
- **browser** — Uses browser automation to post via platform UIs. No API keys but fragile.

Default: `manual`

---

## Step 5: Target Platforms

Ask the user which platforms they want to post to (multi-select):

Options:
- **instagram** — 1080x1080 feed, 1080x1920 stories
- **x** — 1200x675 posts
- **tiktok** — 1080x1920 videos/images
- **linkedin** — 1200x627 posts
- **facebook** — 1200x630 posts

Default: `[x, instagram]`

---

## Step 6: Auto-Post Setting

Ask the user if they want automatic posting or confirmation before each post:

Options:
- **Confirm before posting** (Default) — Shows preview + asks for approval. Safer.
- **Auto-post** — Posts immediately after generation. For power users.

Default: `auto_post: false`

---

## Step 7: Write Config File

Create `.social-machine/` directory if it doesn't exist.

Write `.social-machine/config.md` with this format:

```markdown
---
graphics_provider: {choice}
video_provider: {choice}
posting_provider: {choice}
posting_platforms:
  - {platform1}
  - {platform2}
auto_post: {true/false}
---

# Social Machine Configuration
# Edit this file directly or run /social-config to update.
# Provider options: see skills/social-machine/README.md
```

---

## Step 8: Credentials Setup (if API posting selected)

If the user chose `api` as their posting provider:

1. Create `.social-machine/credentials.env` with placeholder values:
```
# X (Twitter) API - https://developer.x.com/
X_API_KEY=
X_API_SECRET=
X_ACCESS_TOKEN=
X_ACCESS_TOKEN_SECRET=

# Instagram Graph API - https://developers.facebook.com/
INSTAGRAM_ACCESS_TOKEN=
INSTAGRAM_BUSINESS_ACCOUNT_ID=

# TikTok Content Posting API - https://developers.tiktok.com/
TIKTOK_ACCESS_TOKEN=
```

2. **CRITICAL:** Check if `.gitignore` exists in the project root.
   - If YES: check if `.social-machine/credentials.env` is already in it. If not, append it.
   - If NO: create `.gitignore` with `.social-machine/credentials.env`.

3. Warn the user: "I've created `.social-machine/credentials.env` with placeholder values. Fill in your API keys before using API posting. This file is gitignored to protect your credentials."

---

## Step 9: Confirm

Show the user a summary of their configuration and confirm it looks correct.
If they want changes, loop back to the relevant step.
