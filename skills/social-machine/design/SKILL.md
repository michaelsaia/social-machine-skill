---
name: social-design
version: 0.1.0
description: |
  Create social media graphics using the configured provider (HTML/CSS screenshot, Figma, SVG, etc.).
  Use when the user wants to generate a graphic for social media or runs "/social-design".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# Social Machine: Design

You are running `/social-design`. This creates publish-ready graphics using the configured graphics provider.

---

## Prerequisites

Read these files:

1. **`.social-machine/config.md`** (REQUIRED) — which graphics provider to use, target platforms
2. **`.social-machine/brand.md`** (REQUIRED) — colors, logo, tone
3. **`.social-machine/output/ideation-brief.md`** (REQUIRED) — what to create

---

## Step 1: Determine Provider

Read `graphics_provider` from config.md:

| Provider | Load Instructions From |
|---|---|
| `html-screenshot` | `design/providers/html-screenshot.md` |
| `figma` | `design/providers/figma.md` |
| `svg` | `design/providers/svg.md` |
| `powerpoint` | `design/providers/powerpoint.md` |

Read the provider file and follow its instructions for the creation step.

---

## Step 2: Determine Target Dimensions

For each platform in `posting_platforms` from config.md, use these dimensions:

```
PLATFORM DIMENSIONS (pixels):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Instagram Feed:     1080 x 1080
Instagram Story:    1080 x 1920
X / Twitter:        1200 x 675
TikTok:             1080 x 1920
LinkedIn:           1200 x 627
Facebook:           1200 x 630
```

Create ONE design that adapts to each target dimension. The core content stays the same but layout adjusts:
- **Square (IG feed):** centered, balanced layout
- **Landscape (X, LinkedIn, FB):** wider layout, text can sit beside visuals
- **Portrait (Stories, TikTok):** vertical stack, more space for text below visuals

---

## Step 3: Create the Graphic

Follow the loaded provider's instructions to create the graphic.

Regardless of provider, the graphic MUST:

1. **Use brand colors** from brand.md as the primary palette
2. **Include the headline/key text** from the ideation brief's visual direction
3. **Match the content type's visual style** (see content type guidelines below)
4. **Be high quality** — clean, modern, professional
5. **Be readable** — text must be large enough to read on mobile
6. **Include branding** — logo or app name, subtly placed (bottom corner or small watermark)

### Content Type Visual Guidelines

**Feature Spotlight:**
- App screenshot as hero visual (centered or offset)
- Overlay headline text on a semi-transparent branded banner
- Subtle gradient or branded background behind screenshot
- Optional: device mockup frame around screenshot

**Quote Card:**
- Bold, large text centered on branded background
- Quote marks or decorative elements in brand accent color
- Author attribution if applicable
- Clean, minimal design — let the words breathe

**Stat / Metric Graphic:**
- HUGE number as the focal point (largest text element)
- Supporting context text below in smaller size
- Brand accent color for the number
- Optional: simple chart or icon related to the metric

**Before / After:**
- Split design: left side "before", right side "after"
- Clear labels for each side
- Divider line or diagonal split in brand color
- Consistent framing for both sides

**Tip / How-To:**
- Numbered steps or bullet points, clearly formatted
- Each step gets its own visual row/section
- Icons or small illustrations per step if possible
- Header with the tip topic

**Announcement:**
- Bold headline — the news
- Supporting details in smaller text
- Energetic/celebratory feel (gradients, accent colors)
- CTA button visual (e.g., "Try it now" badge)

**Testimonial Card:**
- Large quote text
- Star rating (if applicable)
- User name/attribution
- App icon or logo
- Warm, trustworthy colors

---

## Step 4: Output Files

Save all generated graphics to `.social-machine/output/` with descriptive filenames:

```
.social-machine/output/
├── {date}_{content_type}_instagram_1080x1080.png
├── {date}_{content_type}_x_1200x675.png
├── {date}_{content_type}_linkedin_1200x627.png
└── {date}_{content_type}_source.html  (if html-screenshot provider)
```

The source file (HTML, SVG, or Figma link) should also be saved so the user can manually edit it later.

---

## Step 5: Preview & Iterate

Show the user the file paths for all generated graphics.
Tell them to open the files to preview.

Use AskUserQuestion:
- **Looks good — proceed to posting** → continue pipeline
- **Adjust colors/layout** → describe what to change, regenerate
- **Try a different content type** → go back to ideation
- **Edit the source file manually** → show source file path, wait for user to finish editing, then re-screenshot
