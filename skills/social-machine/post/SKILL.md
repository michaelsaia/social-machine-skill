---
name: social-post
version: 0.1.0
description: |
  Publish social media content using the configured provider (API, manual, or browser).
  Use when the user wants to post content, publish a graphic, or runs "/social-post".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# Social Machine: Post

You are running `/social-post`. This publishes (or prepares for manual publishing) the generated social media content.

---

## Prerequisites

Read these files:

1. **`.social-machine/config.md`** (REQUIRED) — posting provider, target platforms, auto_post
2. **`.social-machine/output/ideation-brief.md`** (REQUIRED) — captions per platform
3. **`.social-machine/output/`** — find the generated graphics (PNG files)

Verify that graphics exist for each target platform. If not, warn the user and suggest running `/social-design` first.

---

## Step 1: Pre-Post Review

### If `auto_post: false` (default)

Show the user a complete preview of what will be posted:

For each target platform, display:
```
PLATFORM: {platform name}
GRAPHIC:  {file path to PNG}
CAPTION:  {platform-adapted caption text}
HASHTAGS: {hashtags}
```

Use AskUserQuestion with options:
- **Post to all platforms** — proceed with posting
- **Post to {specific platform} only** — post to just one
- **Edit caption** — let user modify the caption text
- **Regenerate graphic** — go back to design stage
- **Save for later** — save everything but don't post
- **Cancel** — abort

### If `auto_post: true`

Skip the review and proceed directly to posting.
Still log everything for the history.

---

## Step 2: Determine Provider

Read `posting_provider` from config.md:

| Provider | Load Instructions From |
|---|---|
| `manual` | `post/providers/manual.md` |
| `api` | `post/providers/api/{platform}.md` for each platform |
| `browser` | `post/providers/browser.md` |

Read the provider file and follow its instructions.

---

## Step 3: Execute Post (per platform)

For each target platform, execute the posting provider's instructions.

**Important:** Post to platforms sequentially, not in parallel. If one fails, the user can decide whether to continue with the remaining platforms.

If a post fails:
- Show the error message
- Ask the user: Retry / Skip this platform / Switch to manual for this one / Cancel all

---

## Step 4: Log to History

After posting (or saving for manual), append to `.social-machine/history/posts.md`.

If the file doesn't exist, create it with this header:

```markdown
# Social Machine Post History

| Date | Platform | Type | Topic | Hook | Status |
|------|----------|------|-------|------|--------|
```

Append a row for each platform posted to:

```markdown
| {YYYY-MM-DD} | {platform} | {content_type} | {topic} | {hook_type} | {posted/saved} |
```

---

## Step 5: Report

Show the user a summary:

```
SOCIAL MACHINE — Post Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Instagram: Posted (or: Saved to .social-machine/output/)
✓ X:         Posted (or: Saved to .social-machine/output/)

Files:
  .social-machine/output/{graphic_files}
  .social-machine/output/ideation-brief.md

History updated: .social-machine/history/posts.md
```

### Content Variety Suggestion

After posting, analyze the updated history and suggest what to post next:

```
Based on your post history:
  Last 5 posts: 2 feature spotlights, 1 quote card, 1 tip, 1 announcement

  Suggestion for next post: A testimonial card or stat graphic
  would add variety to your content mix.
```
