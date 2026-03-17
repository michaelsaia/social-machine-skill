# Graphics Provider: Figma MCP

This provider uses the Figma MCP server to create designs directly in Figma, then exports screenshots.

---

## Prerequisites

- Figma MCP server must be configured and running
- User must have a Figma account with appropriate permissions
- The following MCP tools must be available:
  - `mcp__figma__generate_figma_design`
  - `mcp__figma__get_screenshot`
  - `mcp__figma__get_design_context`

If these tools are not available, warn the user and suggest switching to `html-screenshot` provider via `/social-config`.

---

## Step 1: Create the Design

Use the Figma MCP `generate_figma_design` tool to create the social media graphic.

Provide a detailed prompt that includes:
- The content type and visual direction from the ideation brief
- Brand colors (exact hex values from brand.md)
- Dimensions for the target platform
- Text content (headline, body, CTA)
- Layout preferences based on content type guidelines

Example prompt structure:
```
Create a social media graphic for Instagram (1080x1080px).

Brand colors: Primary #F59E0B, Secondary #F97316, Accent #EAB308
Background: gradient from #F59E0B to #F97316

Content type: Feature Spotlight
Headline: "Your AI Workout Partner"
Body text: "Get personalized programs in seconds"
CTA: "Try Yoked Free"

Layout: centered, app screenshot in a phone mockup frame,
headline above, body text and CTA below.
Modern, clean design with rounded corners and subtle shadows.
```

---

## Step 2: Export Screenshot

Use `mcp__figma__get_screenshot` to capture the design as an image.

Save to: `.social-machine/output/{date}_{content_type}_{platform}_{WIDTH}x{HEIGHT}.png`

---

## Step 3: Multi-Platform Adaptation

For each target platform, either:
- Create a separate Figma frame at the target dimensions
- Or duplicate and resize the original frame

Export a screenshot for each.

---

## Step 4: Save Figma Link

Save the Figma file URL to the output so the user can access and edit the design:

```
.social-machine/output/{date}_{content_type}_figma_link.txt
```

---

## Notes

- Figma MCP's `generate_figma_design` is optimized for converting live web UI to Figma layers. For social media graphics, provide very specific design instructions since this is not its primary use case.
- For best results, consider creating a Figma template file first and using the MCP to populate it with content.
- The Figma provider produces editable designs, which is its main advantage over HTML screenshots.
