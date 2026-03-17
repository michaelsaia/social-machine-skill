# Graphics Provider: Pure SVG

This is the fallback provider for environments without a headless browser or Figma. It generates SVG files that can be viewed in any browser or converted to PNG.

---

## When to Use

- No headless browser available (gstack/browse not installed, no Playwright/Puppeteer)
- No Figma MCP configured
- User prefers vector output
- Simple graphics (quote cards, stat graphics, text-heavy designs)

---

## Step 1: Generate SVG

Create a self-contained SVG file at `.social-machine/output/{date}_{content_type}_source.svg`.

### SVG Template Structure

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     width="{WIDTH}" height="{HEIGHT}"
     viewBox="0 0 {WIDTH} {HEIGHT}">

  <!-- Background -->
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{PRIMARY_COLOR}" />
      <stop offset="100%" style="stop-color:{SECONDARY_COLOR}" />
    </linearGradient>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg)" rx="0" />

  <!-- Content -->
  <text x="{CENTER_X}" y="{TITLE_Y}"
        font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
        font-size="64" font-weight="800" fill="white"
        text-anchor="middle">
    {HEADLINE}
  </text>

  <!-- Body text -->
  <text x="{CENTER_X}" y="{BODY_Y}"
        font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
        font-size="28" font-weight="400" fill="rgba(255,255,255,0.9)"
        text-anchor="middle">
    {BODY_TEXT}
  </text>

</svg>
```

### SVG Design Tips

1. **Text wrapping:** SVG doesn't auto-wrap text. For multi-line text, use multiple `<text>` elements or `<tspan>` elements with adjusted `dy` values.

2. **Rounded rectangles:** Use `rx` and `ry` attributes: `<rect rx="20" ry="20" />`

3. **Shadows:** Use SVG filters:
   ```xml
   <defs>
     <filter id="shadow">
       <feDropShadow dx="0" dy="10" stdDeviation="20" flood-opacity="0.15" />
     </filter>
   </defs>
   <rect filter="url(#shadow)" ... />
   ```

4. **Embedded images:** Use `<image>` with base64 or absolute file path:
   ```xml
   <image href="file:///path/to/screenshot.png" x="100" y="200" width="400" height="300" />
   ```

5. **Brand colors:** Apply directly from brand.md hex values.

---

## Step 2: Convert to PNG (if possible)

Try to convert the SVG to PNG for posting:

```bash
# Option 1: macOS built-in (via sips)
# SVG support is limited, may not work for complex SVGs

# Option 2: If rsvg-convert is available
rsvg-convert -w {WIDTH} -h {HEIGHT} input.svg -o output.png

# Option 3: If ImageMagick is available
convert -density 300 input.svg output.png

# Option 4: If none available, leave as SVG
# User can open in browser and screenshot manually
```

---

## Limitations

- No automatic text wrapping — must manually position multi-line text
- Limited typography control compared to HTML/CSS
- Embedding raster images (screenshots) reduces the vector advantage
- Complex layouts (cards, grids) are harder to build than in HTML
- No CSS-like flexbox/grid layout — everything is absolute positioned

For complex designs, recommend the user switch to `html-screenshot` provider.
