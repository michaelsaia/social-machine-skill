---
name: social-ideate
version: 0.1.0
description: |
  Generate social media post ideas with captions, visual direction, and content type selection.
  Use when the user wants post ideas, caption writing, or runs "/social-ideate".
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
---

# Social Machine: Content Ideation

You are running `/social-ideate`. This generates post concepts and caption variants based on the brand profile, research brief, and post history.

---

## Prerequisites

Read these files (in order of importance):

1. **`.social-machine/brand.md`** (REQUIRED) — brand identity, tone, audience, features
2. **`.social-machine/research-latest.md`** (if exists) — current trends and opportunities
3. **`.social-machine/history/posts.md`** (if exists) — past posts for variety analysis
4. **`.social-machine/config.md`** (REQUIRED) — target platforms and settings

---

## Step 1: Content Variety Check

If post history exists, analyze it:

```
VARIETY RULES:
- Don't repeat the same content TYPE two posts in a row
- Don't repeat the same TOPIC within 5 posts
- Don't use the same HOOK style two posts in a row
- Rotate between platforms if posting to multiple
- Balance: educational / promotional / entertaining / inspiring
```

Note any constraints for this post based on history analysis. Tell the user:
"Based on your post history, your last {N} posts were {types}. I'm recommending a {different_type} for variety."

---

## Step 2: Select Content Type

Based on the research brief, history analysis, and user input, recommend a content type:

```
PHASE 1 CONTENT TYPES:
━━━━━━━━━━━━━━━━━━━━━
1. FEATURE SPOTLIGHT
   - Showcases a specific app/product feature
   - Best for: new features, underrated features
   - Visual: app screenshot with overlay text + branded frame

2. QUOTE CARD
   - Motivational, educational, or thought-provoking quote
   - Best for: engagement, shares, brand personality
   - Visual: bold text on branded background

3. STAT / METRIC GRAPHIC
   - Highlights an impressive number or achievement
   - Best for: social proof, milestones, credibility
   - Visual: large number with supporting text

4. BEFORE / AFTER
   - Shows transformation or improvement
   - Best for: results-oriented products, testimonials
   - Visual: split-screen or side-by-side comparison

5. TIP / HOW-TO
   - Educational content teaching something useful
   - Best for: value-first content, establishing expertise
   - Visual: numbered steps or key takeaway

6. ANNOUNCEMENT
   - New feature, update, milestone, or news
   - Best for: launches, updates, company news
   - Visual: bold headline with feature imagery

7. TESTIMONIAL CARD
   - User quote or review
   - Best for: social proof, trust building
   - Visual: quote text with stars/rating + user attribution
```

Present your recommendation with rationale. If the user has a specific idea, adapt to that instead.

---

## Step 3: Generate Caption Variants

For the selected content type and topic, generate **3 caption variants** with different hooks:

### Variant 1: QUESTION HOOK
Start with a question that makes the reader stop scrolling.
- Creates curiosity
- Invites engagement (comments)
- Example: "Still spending 30 minutes planning every workout?"

### Variant 2: STAT / SOCIAL PROOF HOOK
Start with a compelling number, fact, or proof point.
- Builds credibility instantly
- Creates FOMO
- Example: "10,000+ AI-generated workout programs and counting."

### Variant 3: STORY / RELATABLE HOOK
Start with a relatable scenario or personal story angle.
- Creates emotional connection
- Feels authentic, not promotional
- Example: "I used to dread planning workout splits every Sunday night."

### For Each Variant, Include:

```
CAPTION STRUCTURE:
1. Hook (first line — this is what shows before "...more")
2. Body (2-4 lines expanding on the hook)
3. Value proposition (what the product does for them)
4. CTA (call to action — subtle or direct)
5. Hashtags (platform-appropriate, from research brief)
```

### Platform Adaptations:

**Instagram:** Full caption (up to 2,200 chars). Rich hashtags (5-15). Can use line breaks for readability. CTA: "Link in bio" or "Try it free."

**X (Twitter):** Concise (under 280 chars including image). 1-3 hashtags max. Punchy hook. CTA: link to website or app.

**TikTok:** Casual, conversational. Trend-aware language. 3-5 hashtags. CTA: "Link in bio."

**LinkedIn:** Professional but personal. Longer form OK. Minimal hashtags (3-5). CTA: direct link.

---

## Step 4: Visual Direction Brief

For the selected content type, write a brief visual direction that the design stage will follow:

```
VISUAL BRIEF:
- Content type: {type}
- Primary text: "{headline or key text for the graphic}"
- Secondary text: "{supporting text if any}"
- Visual elements: {what should appear — screenshot, icon, pattern, etc.}
- Mood: {energetic / clean / bold / minimal / etc.}
- Colors to emphasize: {which brand colors to feature}
- Logo placement: {yes/no, where}
```

---

## Step 5: Present to User

Show all 3 caption variants with the visual direction brief.

Use AskUserQuestion to let the user:
- Pick a caption variant (1, 2, or 3)
- Request edits to the selected caption
- Ask for more variants
- Change the content type entirely
- Adjust the visual direction

Once the user approves a caption and visual direction, save the ideation output to `.social-machine/output/ideation-brief.md`:

```markdown
# Post Ideation Brief
**Date:** {date}
**Content Type:** {type}
**Target Platforms:** {platforms}

## Selected Caption
### Instagram
{platform-adapted caption}

### X
{platform-adapted caption}

## Visual Direction
{visual brief}

## Hashtags
### Instagram
{hashtags}

### X
{hashtags}
```

This file is consumed by the design stage.
