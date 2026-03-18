# Meme Layout Patterns for HTML/CSS Screenshot Provider

These are CSS/HTML layout patterns for generating meme-format graphics. Memes have
a DIFFERENT visual language than brand graphics. Some are polished, some are intentionally rough.

## Critical: Meme Visual Rules

1. **Typography:** Bold, high-contrast, readable at thumbnail size. Impact font is a cliche
   but sometimes the right call. Modern memes use bold sans-serif (Inter Black, system bold).
2. **Lo-fi is a feature:** Not every meme needs to look designed. Sometimes a white background
   with black text IS the format.
3. **Don't over-brand:** Logo in a corner at most. If the meme is funny, people will find
   your account. If it's too branded, they won't share it.
4. **Mobile-first:** 90% of meme consumption is on phones. Text must be readable at
   phone-screen sizes without zooming.
5. **Memes are NOT infographics.** Keep text minimal. If it takes more than 5 seconds
   to read, it's too long.

---

## Layout: Drake Comparison (Reject/Prefer)

```html
<!-- Two stacked rows: reject on top, prefer on bottom -->
<style>
  body {
    width: 1080px; height: 1080px;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif;
    background: #09090B; color: #FAFAFA;
    margin: 0; display: flex; flex-direction: column;
  }
  .row {
    flex: 1; display: flex; align-items: center;
    padding: 40px 60px; gap: 40px;
    border-bottom: 2px solid #1a1a1f;
  }
  .row:last-child { border-bottom: none; }
  .row.reject { background: #0c0c0e; }
  .row.prefer { background: #111113; }
  .icon {
    width: 120px; height: 120px; border-radius: 24px;
    display: flex; align-items: center; justify-content: center;
    font-size: 64px; flex-shrink: 0;
  }
  .reject .icon { background: rgba(239,68,68,0.15); }
  .prefer .icon { background: rgba(34,197,94,0.15); }
  .text {
    font-size: 36px; font-weight: 700; line-height: 1.3;
  }
  .reject .text { color: #71717A; }
  .prefer .text { color: #FAFAFA; }
  /* Subtle brand accent on the "prefer" row */
  .prefer { border-left: 4px solid {{brand_primary}}; }
</style>

<div class="row reject">
  <div class="icon">😤</div>
  <div class="text">{{reject_text}}</div>
</div>
<div class="row prefer">
  <div class="icon">😏</div>
  <div class="text">{{prefer_text}}</div>
</div>
```

**Variations:**
- Use ❌/✅ instead of emoji faces
- Add a small product screenshot in the "prefer" row
- Use three rows for a "good / better / best" progression

---

## Layout: Starter Pack

```html
<style>
  body {
    width: 1080px; height: 1080px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background: #FAFAFA; color: #09090B;
    margin: 0; padding: 40px;
    display: flex; flex-direction: column;
  }
  .title {
    font-size: 42px; font-weight: 800; text-align: center;
    margin-bottom: 40px; line-height: 1.2;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px; flex: 1;
  }
  .item {
    background: #F4F4F5;
    border-radius: 20px;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 24px; gap: 12px;
    font-size: 18px; font-weight: 600; color: #52525B;
    text-align: center;
  }
  .item img {
    max-width: 80%; max-height: 65%;
    object-fit: contain; border-radius: 12px;
  }
  .item .emoji { font-size: 72px; }
</style>

<h1 class="title">The "{{pack_title}}" Starter Pack</h1>
<div class="grid">
  <div class="item"><span class="emoji">{{emoji1}}</span>{{label1}}</div>
  <div class="item"><span class="emoji">{{emoji2}}</span>{{label2}}</div>
  <div class="item"><span class="emoji">{{emoji3}}</span>{{label3}}</div>
  <div class="item"><span class="emoji">{{emoji4}}</span>{{label4}}</div>
</div>
```

**Notes:**
- Can use actual images (stock photos, screenshots) instead of emoji
- Light background is traditional for starter packs
- 2x2 grid is standard, 2x3 for more items
- Keep labels SHORT — 3-5 words max

---

## Layout: Expanding Brain

```html
<style>
  body {
    width: 1080px; height: 1350px; /* Taller for 4-5 rows */
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background: #09090B; color: #FAFAFA;
    margin: 0; display: flex; flex-direction: column;
  }
  .level {
    flex: 1; display: flex; align-items: center;
    padding: 24px 48px; gap: 32px;
    border-bottom: 1px solid #1a1a1f;
  }
  .level:last-child { border-bottom: none; }
  .brain {
    width: 140px; height: 140px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 64px; flex-shrink: 0;
  }
  .level:nth-child(1) .brain { background: #27272A; }
  .level:nth-child(2) .brain { background: #3F3F46; }
  .level:nth-child(3) .brain { background: rgba(245,158,11,0.2); }
  .level:nth-child(4) .brain {
    background: radial-gradient(circle, rgba(245,158,11,0.4), rgba(168,85,247,0.3));
    box-shadow: 0 0 40px rgba(245,158,11,0.3);
  }
  .text { font-size: 28px; font-weight: 600; line-height: 1.3; }
  .level:nth-child(1) .text { color: #71717A; }
  .level:nth-child(2) .text { color: #A1A1AA; }
  .level:nth-child(3) .text { color: #E4E4E7; }
  .level:nth-child(4) .text { color: #FAFAFA; }
</style>

<div class="level">
  <div class="brain">🧠</div>
  <div class="text">{{level1_text}}</div>
</div>
<div class="level">
  <div class="brain">🧠</div>
  <div class="text">{{level2_text}}</div>
</div>
<div class="level">
  <div class="brain">✨</div>
  <div class="text">{{level3_text}}</div>
</div>
<div class="level">
  <div class="brain">🌌</div>
  <div class="text">{{level4_text}}</div>
</div>
```

---

## Layout: Nobody: / Me:

```html
<style>
  body {
    width: 1080px; height: 1080px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background: #09090B; color: #FAFAFA;
    margin: 0;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 80px;
    text-align: center;
  }
  .nobody {
    font-size: 32px; color: #52525B; font-weight: 500;
    margin-bottom: 48px;
  }
  .me-label {
    font-size: 32px; color: #A1A1AA; font-weight: 500;
    margin-bottom: 24px;
  }
  .punchline {
    font-size: 44px; font-weight: 800; line-height: 1.3;
    max-width: 800px;
  }
</style>

<div class="nobody">Nobody:</div>
<div class="me-label">Me:</div>
<div class="punchline">{{punchline_text}}</div>
```

**Notes:**
- Extremely simple layout. The simplicity IS the format.
- Can add a relevant image/screenshot below the punchline
- Dark background is standard for this format

---

## Layout: POV:

```html
<style>
  body {
    width: 1080px; height: 1080px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    color: #FAFAFA; margin: 0; position: relative;
  }
  .bg-image {
    position: absolute; top: 0; left: 0;
    width: 100%; height: 100%;
    object-fit: cover; z-index: 0;
  }
  .overlay {
    position: absolute; top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(
      180deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.1) 30%,
      rgba(0,0,0,0.1) 70%, rgba(0,0,0,0.5) 100%
    );
    z-index: 1;
  }
  .pov-label {
    position: absolute; top: 48px; left: 0; right: 0;
    z-index: 2; text-align: center;
    font-size: 48px; font-weight: 800;
    text-shadow: 0 2px 20px rgba(0,0,0,0.8);
    padding: 0 60px; line-height: 1.3;
  }
  .pov-prefix {
    font-size: 24px; font-weight: 600;
    color: rgba(255,255,255,0.7);
    letter-spacing: 4px; text-transform: uppercase;
    display: block; margin-bottom: 12px;
  }
</style>

<img src="{{background_image}}" class="bg-image" alt="">
<div class="overlay"></div>
<div class="pov-label">
  <span class="pov-prefix">POV:</span>
  {{pov_text}}
</div>
```

---

## Layout: Tweet Screenshot / Relatable Text Post

```html
<style>
  body {
    width: 1080px; height: 1080px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background: #09090B;
    margin: 0;
    display: flex; align-items: center; justify-content: center;
  }
  .tweet-card {
    background: #18181B;
    border-radius: 24px;
    border: 1px solid #27272A;
    padding: 48px;
    max-width: 820px;
    width: 100%;
  }
  .tweet-header {
    display: flex; align-items: center; gap: 16px;
    margin-bottom: 24px;
  }
  .avatar {
    width: 56px; height: 56px; border-radius: 50%;
  }
  .handle-info {
    display: flex; flex-direction: column; gap: 2px;
  }
  .display-name {
    font-size: 20px; font-weight: 700; color: #FAFAFA;
  }
  .handle {
    font-size: 16px; color: #52525B;
  }
  .tweet-text {
    font-size: 36px; font-weight: 500; line-height: 1.5;
    color: #E4E4E7;
  }
  .tweet-meta {
    margin-top: 32px; padding-top: 20px;
    border-top: 1px solid #27272A;
    font-size: 15px; color: #52525B;
  }
  .engagement {
    display: flex; gap: 32px; margin-top: 16px;
    font-size: 15px; color: #71717A;
  }
  .engagement span { font-weight: 600; color: #A1A1AA; }
</style>

<div class="tweet-card">
  <div class="tweet-header">
    <img src="{{brand_logo}}" class="avatar" alt="">
    <div class="handle-info">
      <div class="display-name">{{brand_name}}</div>
      <div class="handle">@{{brand_handle}}</div>
    </div>
  </div>
  <div class="tweet-text">{{tweet_text}}</div>
  <div class="tweet-meta">
    {{time}} · {{date}}
    <div class="engagement">
      <div><span>{{retweets}}</span> Reposts</div>
      <div><span>{{likes}}</span> Likes</div>
    </div>
  </div>
</div>
```

**Notes:**
- Fake engagement numbers add social proof (use believable numbers, not millions)
- The tweet text IS the joke. Keep it under 280 characters.
- Can omit the engagement section for a cleaner look

---

## Layout: This or That (Split Screen)

```html
<style>
  body {
    width: 1080px; height: 1080px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    margin: 0; display: flex; flex-direction: column;
  }
  .title {
    background: #09090B; color: #FAFAFA;
    text-align: center; padding: 40px;
    font-size: 28px; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase;
  }
  .split {
    flex: 1; display: flex;
  }
  .side {
    flex: 1; display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 40px; gap: 20px;
  }
  .side.left { background: {{brand_primary}}; }
  .side.right { background: #18181B; }
  .vs {
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 72px; height: 72px;
    background: #09090B; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 28px; font-weight: 800; color: #FAFAFA;
    border: 3px solid #27272A;
    z-index: 1;
  }
  .side .emoji { font-size: 80px; }
  .side .label {
    font-size: 32px; font-weight: 700; color: #FAFAFA;
    text-align: center;
  }
</style>

<div class="title">This or That?</div>
<div class="split" style="position: relative;">
  <div class="side left">
    <div class="emoji">{{emoji_left}}</div>
    <div class="label">{{option_left}}</div>
  </div>
  <div class="vs">VS</div>
  <div class="side right">
    <div class="emoji">{{emoji_right}}</div>
    <div class="label">{{option_right}}</div>
  </div>
</div>
```

---

## Layout: Expectation vs Reality

```html
<style>
  body {
    width: 1080px; height: 1080px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    margin: 0; display: flex;
  }
  .panel {
    flex: 1; display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 48px; gap: 24px; position: relative;
  }
  .panel.expect {
    background: linear-gradient(180deg, #09090B, #18181B);
  }
  .panel.reality {
    background: #09090B;
  }
  .panel-label {
    position: absolute; top: 32px;
    font-size: 16px; font-weight: 700;
    letter-spacing: 3px; text-transform: uppercase;
  }
  .expect .panel-label { color: {{brand_primary}}; }
  .reality .panel-label { color: #52525B; }
  .panel-text {
    font-size: 28px; font-weight: 600;
    text-align: center; line-height: 1.4;
    color: #FAFAFA; max-width: 400px;
  }
  .panel .emoji { font-size: 80px; }
  .divider {
    width: 2px; background: #27272A;
  }
</style>

<div class="panel expect">
  <div class="panel-label">Expectation</div>
  <div class="emoji">{{emoji_expect}}</div>
  <div class="panel-text">{{expect_text}}</div>
</div>
<div class="divider"></div>
<div class="panel reality">
  <div class="panel-label">Reality</div>
  <div class="emoji">{{emoji_reality}}</div>
  <div class="panel-text">{{reality_text}}</div>
</div>
```

---

## Layout: Hot Take / Unpopular Opinion

```html
<style>
  body {
    width: 1080px; height: 1080px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background: #09090B;
    margin: 0;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 100px;
    text-align: center;
  }
  .label {
    font-size: 16px; font-weight: 700;
    letter-spacing: 4px; text-transform: uppercase;
    color: {{brand_primary}};
    margin-bottom: 40px;
  }
  .take {
    font-size: 52px; font-weight: 800;
    line-height: 1.25; letter-spacing: -1px;
    color: #FAFAFA;
    max-width: 800px;
  }
  .prompt {
    margin-top: 48px;
    font-size: 18px; color: #52525B;
    font-weight: 500;
  }
</style>

<div class="label">🔥 Hot Take</div>
<div class="take">{{hot_take_text}}</div>
<div class="prompt">Agree or disagree? 👇</div>
```

---

## Layout: Alignment Chart

```html
<style>
  body {
    width: 1080px; height: 1080px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background: #09090B; color: #FAFAFA;
    margin: 0; padding: 32px;
    display: flex; flex-direction: column;
  }
  .title {
    text-align: center; font-size: 28px;
    font-weight: 800; margin-bottom: 24px;
  }
  .chart-wrapper {
    flex: 1; display: flex; flex-direction: column;
    position: relative;
  }
  .axis-label-x {
    display: flex; justify-content: space-between;
    padding: 0 60px; margin-bottom: 8px;
    font-size: 14px; color: #71717A; font-weight: 600;
    letter-spacing: 1px; text-transform: uppercase;
  }
  .axis-label-y {
    position: absolute; left: 0; top: 50%;
    transform: translateY(-50%) rotate(-90deg);
    font-size: 14px; color: #71717A; font-weight: 600;
    letter-spacing: 1px; text-transform: uppercase;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 1fr);
    gap: 8px; flex: 1;
    margin-left: 40px;
  }
  .cell {
    background: #18181B;
    border-radius: 16px;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 16px; gap: 8px;
    text-align: center;
  }
  .cell .emoji { font-size: 40px; }
  .cell .label { font-size: 15px; font-weight: 600; color: #A1A1AA; }
</style>

<div class="title">{{chart_title}}</div>
<div class="chart-wrapper">
  <div class="axis-label-x">
    <span>{{x_axis_left}}</span>
    <span>{{x_axis_right}}</span>
  </div>
  <div class="grid">
    <!-- Fill 9 cells with emoji + label combos -->
    <div class="cell"><span class="emoji">{{c1_emoji}}</span><span class="label">{{c1_label}}</span></div>
    <!-- ... repeat for all 9 cells ... -->
  </div>
</div>
```

---

## Lo-Fi Scaling Guide

| Lo-Fi Level | Typography | Background | Layout | Branding |
|-------------|-----------|------------|--------|----------|
| 1 (Polished) | Brand fonts, clean | Brand gradients | Pixel-perfect | Logo + handle |
| 2 | Bold sans-serif | Solid dark/light | Clean but simple | Small logo |
| 3 (Sweet spot) | System bold | Simple solid | Intentionally basic | Handle only |
| 4 | Impact or basic bold | White or black | Rough, quick feel | None or watermark |
| 5 (Raw) | Default system font | Pure white/black | Minimal effort look | None |

**When to use each:**
- Level 1-2: "Brand meme" — looks like a brand made it intentionally
- Level 3: Best of both worlds — funny AND on-brand
- Level 4-5: "Organic" feel — looks like a user made it, higher share potential

Most brand memes should be Level 2-3. Only go to 4-5 if the format demands it
(like a tweet screenshot or text-only post).
