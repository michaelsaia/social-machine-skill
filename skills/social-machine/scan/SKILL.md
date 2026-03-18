---
name: social-scan
version: 0.1.0
description: |
  Scan a project's codebase to extract brand identity — colors, icons, logos, website, app name,
  features, and target audience. Use when setting up Social Machine for a new project or when
  the user runs "/social-scan".
allowed-tools:
  - Read
  - Grep
  - Glob
  - Write
  - Edit
  - AskUserQuestion
  - WebSearch
  - WebFetch
  - Agent
---

# Social Machine: Brand Scan

You are running `/social-scan`. This analyzes the current project's codebase to build a brand profile that informs all content creation.

---

## Step 1: Detect Project Type

Look for indicators of what kind of project this is:

```
SEARCH ORDER:
1. app.json / app.config.js     → Expo / React Native mobile app
2. package.json                  → Node.js / React / Next.js web app
3. Podfile / *.xcodeproj         → Native iOS app
4. build.gradle                  → Android app
5. pyproject.toml / setup.py     → Python project
6. Cargo.toml                    → Rust project
7. go.mod                        → Go project
8. Any other indicators
```

Read the main config file to get:
- **App/project name**
- **Description/tagline** (from package.json description, app.json description, README.md first paragraph)
- **Bundle ID / package name** (for app store links)

---

## Step 2: Extract Brand Colors

Search for color definitions in this order:

```
SEARCH LOCATIONS:
1. tailwind.config.{js,ts}       → theme.extend.colors
2. */constants/Colors.{js,ts}    → Color constant exports
3. */theme/*.{js,ts}             → Theme configuration
4. */styles/variables.{css,scss}  → CSS custom properties
5. *.css with :root              → CSS variables
6. */brand/*.{js,ts,json}        → Brand configuration
7. Info.plist / AndroidManifest   → Accent colors
```

For each color found, note:
- The color name/role (primary, secondary, accent, background, text)
- The hex value
- Where it was defined (file path)

If multiple color systems exist (e.g., light/dark themes), prefer the primary/light theme colors for social media content since most social feeds use light backgrounds.

---

## Step 3: Find Logos & Icons

Search for visual assets:

```
SEARCH PATTERNS:
- **/icon.png, **/logo.png, **/favicon.png
- **/adaptive-icon.png
- **/icon-*.png, **/logo-*.{png,svg}
- **/assets/images/icon*, **/assets/images/logo*
- **/public/images/*, **/public/favicon*
- **/assets/brand/*
```

Note the file paths for:
- Primary app icon / logo
- Any transparent-background variants
- Favicon (for web projects)

---

## Step 4: Detect Website & Social Links

Search for URLs in the codebase:

```
SEARCH PATTERNS:
- grep for "https://" in constants, config, and package files
- Look for social media URLs (instagram.com, twitter.com, tiktok.com, etc.)
- Look for app store URLs (apps.apple.com, play.google.com, testflight.apple.com)
- Look for website/homepage URLs in package.json, app.json, README
```

---

## Step 5: Identify Key Features

Read the project to understand what it does:

1. Read README.md for feature descriptions
2. Look at route/navigation files to understand the app's screens/pages
3. Look at key service files or API endpoints
4. Check for any feature flags or feature lists in constants

Summarize the top 5-7 user-facing features.

---

## Step 6: Ask the User

Some things can't be extracted from code. Use AskUserQuestion for each:

1. **Target audience:** "Who is the target audience for this product? (e.g., 'fitness enthusiasts aged 18-35', 'small business owners', 'developers')"

2. **Brand tone:** "How should the brand voice sound on social media?"
   Options: Professional / Casual & friendly / Motivating & energetic / Witty & humorous / Educational & authoritative

3. **Competitors:** "Who are 2-3 direct competitors? (This helps with trend research and differentiation)"

4. **Current social handles:** If not found in code, ask: "What are your social media handles? (e.g., @myapp on Instagram, X, TikTok)"

---

## Step 7: Write Brand Profile

Create `.social-machine/brand.md` using the template from `templates/brand-profile.md`.

Fill in all discovered and user-provided information. Use this format:

```markdown
---
name: {project name}
tagline: {tagline or description}
website: {URL}
audience: {target audience}
tone: {brand voice}
colors:
  primary: "{hex}"
  secondary: "{hex}"
  accent: "{hex}"
  background: "{hex}"
  text: "{hex}"
logo: {relative path to logo file}
platforms:
  instagram: {handle}
  x: {handle}
  tiktok: {handle}
key_features:
  - {feature 1}
  - {feature 2}
  - {feature 3}
competitors:
  - {competitor 1}
  - {competitor 2}
  - {competitor 3}
app_store_links:
  ios: {URL or "pending"}
  android: {URL or "pending"}
  web: {URL or "N/A"}
---
```

---

## Step 8: Verify with User

Show the completed brand profile to the user and ask if anything needs correction.
If they want changes, update the file accordingly.

Report: "Brand profile saved to `.social-machine/brand.md`. You can edit this file directly anytime, or run `/social-scan` again to regenerate it."
