# Graphics Provider: HTML/CSS → Browser Screenshot

This is the primary graphics provider for Social Machine. It generates an HTML page styled with the project's brand colors, then screenshots it using a headless browser.

---

## How It Works

1. Generate a single self-contained HTML file with inline CSS
2. Open it in a headless browser at the target dimensions
3. Screenshot at 2x resolution for crisp output
4. Save the PNG

---

## Step 1: Generate HTML

Create a self-contained HTML file at `.social-machine/output/{date}_{content_type}_source.html`.

### HTML Template Structure

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    /* Reset */
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      width: {WIDTH}px;
      height: {HEIGHT}px;
      overflow: hidden;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: {BACKGROUND_COLOR or GRADIENT};
      color: {TEXT_COLOR};
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 60px;
    }

    /* Brand-specific styles below */
  </style>
</head>
<body>
  <!-- Content here -->
</body>
</html>
```

### CRITICAL: This Is a Graphic, NOT a Website

You are designing a **static image for social media** — like a poster, flyer, or magazine ad. This will be screenshotted and posted as a PNG. Nobody will click on it, hover over it, or interact with it.

**NEVER include:**
- Buttons or CTAs that look clickable (no "Try it free →" buttons with hover states)
- Navigation bars, menus, or header/footer UI
- Input fields, forms, or any interactive-looking elements
- Underlined text that looks like hyperlinks
- Drop-down menus or toggles
- Anything that makes the viewer think "why can't I click this?"

**Instead, use these graphic design conventions:**
- Text-based CTAs as simple lines of text: "Available on the App Store" or "yoked.fitness" — NOT styled as a button
- Hashtags or handles as plain text at the bottom
- QR codes if you want a scannable action (but only if the user requests it)
- The website URL as subtle branding text, not a clickable-looking element

Think **Instagram graphic / poster / billboard** — not landing page.

---

### Design Principles for Social Media Graphics

1. **Use CSS gradients liberally** — they make flat designs pop
   ```css
   background: linear-gradient(135deg, {primary} 0%, {secondary} 100%);
   ```

2. **Large, bold typography** — social media is viewed on phones
   - Headlines: 48-72px, font-weight 800
   - Body text: 24-32px, font-weight 400-600
   - Use `text-shadow` for text on busy backgrounds

3. **Generous whitespace** — don't fill every pixel. Let the design breathe.
   - Minimum 60px padding on all sides
   - Space between elements: 24-40px

4. **Brand color usage:**
   - Background: primary or gradient of primary → secondary
   - Headlines: white on dark backgrounds, primary on light backgrounds
   - Accents: accent color for highlights, borders, decorative elements
   - Never use more than 3-4 colors total

5. **Modern graphic design patterns:**
   - Rounded corners (`border-radius: 16-24px`) on cards and containers
   - Subtle shadows (`box-shadow: 0 20px 60px rgba(0,0,0,0.15)`)
   - Glass morphism for overlays (`backdrop-filter: blur(20px); background: rgba(255,255,255,0.1)`)
   - Gradient text for headlines (`background-clip: text; -webkit-text-fill-color: transparent`)
   - Decorative shapes (circles, lines, abstract blobs) for visual interest
   - Layered elements with depth (overlapping text on images, offset cards)

6. **Logo/branding placement:**
   - Small logo in bottom-right or bottom-center
   - Size: ~40-60px height
   - Can use the app icon image: `<img src="{absolute_path_to_icon}">`
   - If no logo image: use text logo with brand font styling
   - Website URL as small, subtle text near the logo — NOT as a button

7. **Stock photography integration:**
   - If stock images are available in `.social-machine/output/stock/`, embed them
   - Use as full background with text overlay (add dark overlay for readability)
   - Use as contained element within the design (in a circle cutout, phone frame, etc.)
   - Always apply brand color overlays or tints to keep images on-brand
   - Use `object-fit: cover` and `object-position` for proper cropping

8. **For app screenshots:**
   - Embed as `<img>` with absolute file path
   - Add device mockup frame via CSS (rounded corners, shadow, status bar)
   - Scale to fit within the design (max 60% of canvas width)
   - Screenshots are visual evidence of the product — they should feel like a peek inside the app, not a UI demo

9. **Visual hierarchy for graphics (not websites):**
   - One dominant element (big headline OR hero image — not both competing)
   - Supporting text is secondary — smaller, lighter weight
   - Brand mark is tertiary — small, unobtrusive
   - The viewer should "get it" in under 2 seconds

### Responsive Layout Strategy

For different platform dimensions, adjust the layout:

**Square (1080x1080 — Instagram Feed):**
```css
body {
  flex-direction: column;
  text-align: center;
}
```

**Landscape (1200x675 — X/Twitter):**
```css
body {
  flex-direction: row;
  /* text on left, visual on right (or vice versa) */
}
```

**Portrait (1080x1920 — Stories/TikTok):**
```css
body {
  flex-direction: column;
  justify-content: space-between;
  /* visual on top, text on bottom */
}
```

---

## Step 2: Screenshot with Headless Browser

Use the gstack/browse headless browser if available:

```bash
# Start browser if needed (first call auto-starts)
$B goto "file://{absolute_path_to_html_file}"

# Set viewport to target dimensions (2x for retina)
$B viewport {WIDTH}x{HEIGHT}

# Take screenshot
$B screenshot .social-machine/output/{date}_{content_type}_{platform}_{WIDTH}x{HEIGHT}.png
```

**If gstack/browse is not available**, fall back to a direct puppeteer/playwright command:

```bash
# Check if npx is available
npx --yes playwright screenshot \
  --viewport-size="{WIDTH},{HEIGHT}" \
  --device-scale-factor=2 \
  "file://{absolute_path_to_html_file}" \
  ".social-machine/output/{date}_{content_type}_{platform}_{WIDTH}x{HEIGHT}.png"
```

**If neither is available**, try:
```bash
# macOS built-in WebKit via swift
# Or suggest the user install playwright: npm install -g playwright
```

---

## Step 3: Multi-Platform Export

For each target platform in the config, repeat:
1. Adjust the HTML body dimensions (width/height in CSS)
2. Adjust the layout (see responsive strategy above)
3. Screenshot at the target dimensions

Output one PNG per platform, plus the source HTML.

---

## Troubleshooting

- **Blank screenshot:** Check that all file paths in `<img>` tags are absolute paths
- **Wrong dimensions:** Ensure the HTML body is set to exact pixel dimensions, not percentages
- **Fonts look wrong:** Stick to system fonts (-apple-system, Segoe UI, Roboto) for reliability
- **Logo not showing:** Use absolute path: `file:///Users/.../icon.png`
- **Colors look off:** Ensure hex values include the # prefix
