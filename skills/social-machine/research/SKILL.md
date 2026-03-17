---
name: social-research
version: 0.1.0
description: |
  Research current social media trends, best practices, and optimal content strategies for a
  project's niche. Use when the user wants trend insights, content inspiration, or runs
  "/social-research".
allowed-tools:
  - Read
  - Write
  - WebSearch
  - WebFetch
  - AskUserQuestion
---

# Social Machine: Trend Research

You are running `/social-research`. This researches current social media trends and best practices relevant to the project's niche to inform content creation.

---

## Prerequisites

1. Read `.social-machine/brand.md` to understand:
   - The project's niche/industry
   - Target audience
   - Competitors
   - Active platforms

2. Read `.social-machine/history/posts.md` if it exists, to understand what's already been posted.

---

## Step 1: Niche Trend Research

Use WebSearch to research current trends. Run these searches (adapt keywords to the project's niche):

```
SEARCHES TO RUN:
1. "{niche} social media trends {current_month} {current_year}"
   Example: "fitness app social media trends March 2026"

2. "{niche} instagram content ideas {current_year}"
   Example: "fitness instagram content ideas 2026"

3. "best performing {niche} social media posts {current_year}"
   Example: "best performing fitness social media posts 2026"

4. "{niche} hashtags trending {current_month} {current_year}"
   Example: "fitness hashtags trending March 2026"
```

From the results, extract:
- **Trending content formats** (e.g., carousel tips, before/after, day-in-the-life)
- **Trending topics** in the niche
- **Viral hooks** that are getting engagement
- **Trending hashtags** (separate into: high-volume general, medium niche-specific, low-volume targeted)

---

## Step 2: Platform-Specific Best Practices

For each platform in the user's config, research current best practices:

### Instagram
- Optimal caption length (currently: 125-150 chars for feed, longer for carousels)
- Best posting times for the niche
- Reel vs. feed post performance
- Hashtag strategy (number, placement, mix)
- Current algorithm preferences

### X (Twitter)
- Optimal tweet length (short punchy vs. thread starters)
- Image tweet vs. text-only performance
- Best times to post
- Engagement tactics (questions, polls, hot takes)
- Thread format best practices

### TikTok
- Trending sounds/formats relevant to niche
- Optimal video length
- Caption strategy
- Hashtag strategy
- Hook timing (first 1-3 seconds)

### LinkedIn (if applicable)
- Content types performing well
- Optimal post length
- Best posting times
- Professional vs. personal tone balance

---

## Step 3: Competitor Quick Scan

If competitors are listed in brand.md, do a quick web search for each:

```
"{competitor_name} instagram" OR "{competitor_name} social media"
```

Note:
- What content types they're posting
- Their posting frequency
- Any standout posts or campaigns
- Gaps in their content that we could fill

---

## Step 4: Content Opportunity Analysis

Based on research, identify the top 5 content opportunities ranked by:
1. **Relevance** to the project's features and audience
2. **Timeliness** — trending NOW, not last month
3. **Differentiation** — what competitors aren't doing
4. **Effort** — achievable with current tools (static image + caption for Phase 1)

---

## Step 5: Write Research Brief

Save findings to `.social-machine/research-latest.md`:

```markdown
# Social Media Research Brief
**Generated:** {date}
**Project:** {project name}
**Niche:** {niche}

## Trending Content Formats
- {format 1}: {why it's trending, example}
- {format 2}: {why it's trending, example}
- {format 3}: {why it's trending, example}

## Trending Topics in {niche}
- {topic 1}
- {topic 2}
- {topic 3}

## Viral Hooks Working Right Now
- {hook type}: "{example hook}"
- {hook type}: "{example hook}"
- {hook type}: "{example hook}"

## Hashtag Strategy
### High-Volume (reach)
{list of 5-10 hashtags}

### Niche-Specific (targeting)
{list of 5-10 hashtags}

### Low-Competition (discoverability)
{list of 5-10 hashtags}

## Platform-Specific Notes
### Instagram
{key findings}

### X
{key findings}

## Competitor Observations
{brief notes}

## Top 5 Content Opportunities
1. {opportunity}: {rationale}
2. {opportunity}: {rationale}
3. {opportunity}: {rationale}
4. {opportunity}: {rationale}
5. {opportunity}: {rationale}
```

---

## Step 6: Present to User

Show a brief summary of the top findings and content opportunities.
Ask if they want to proceed to ideation with any of these opportunities, or if they have their own idea.

---

## Marketing Best Practices (Always Apply)

These are baked-in best practices that should inform all research and recommendations:

1. **80/20 Rule:** 80% value content (educational, entertaining, inspiring), 20% promotional
2. **Consistency > Perfection:** Regular posting beats occasional perfect posts
3. **Platform-Native:** Don't cross-post identical content. Adapt per platform.
4. **Hook First:** The first line/3 seconds determines if someone engages
5. **CTA Always:** Every post should have a clear next step (even if subtle)
6. **Social Proof:** User testimonials, numbers, and community content build trust
7. **Storytelling:** Personal stories and behind-the-scenes outperform polished corporate content
8. **Engagement Bait (good kind):** Ask questions, create polls, invite opinions
9. **Hashtag Hygiene:** Mix sizes (big reach + small niche), refresh regularly, 5-15 per IG post
10. **Timing Matters:** Post when your audience is active, not when you finish creating
