---
name: social-stock
version: 0.1.0
description: |
  Find royalty-free, copyright-safe stock images for use in social media graphics. Searches
  Unsplash, Pexels, and Pixabay for high-quality photos matching the project's niche and current
  post concept. Use when the user wants stock photos or runs "/social-stock".
allowed-tools:
  - Bash
  - Read
  - Write
  - WebSearch
  - WebFetch
  - AskUserQuestion
  - Glob
---

# Social Machine: Stock Image Finder

You are running `/social-stock`. This finds royalty-free, copyright-safe stock images that can be used in social media graphics without legal risk.

---

## Prerequisites

1. Read `.social-machine/brand.md` for project niche and context
2. Read `.social-machine/output/ideation-brief.md` if it exists — to find images matching the current post concept
3. Create `.social-machine/output/stock/` directory if it doesn't exist

---

## Copyright-Safe Sources ONLY

**ONLY use these sources.** All provide images under licenses that allow commercial use without attribution (though attribution is nice):

### Tier 1: Best Quality, True Free Commercial Use
| Source | License | URL Pattern for Direct Download |
|---|---|---|
| **Unsplash** | Unsplash License (free commercial use, no attribution required) | `https://unsplash.com/s/photos/{query}` |
| **Pexels** | Pexels License (free commercial use, no attribution required) | `https://www.pexels.com/search/{query}/` |
| **Pixabay** | Pixabay License (free commercial use, no attribution required) | `https://pixabay.com/images/search/{query}/` |

### Tier 2: Good Alternatives
| Source | License | Notes |
|---|---|---|
| **Kaboompics** | Free commercial use | Lifestyle/marketing focused |
| **Burst by Shopify** | Free commercial use | Business/e-commerce focused |
| **StockSnap.io** | CC0 Public Domain | No restrictions whatsoever |

### NEVER Use
- Google Images (mixed licenses, most are copyrighted)
- Pinterest (aggregator, not a license source)
- Getty/iStock/Shutterstock (paid, watermarked)
- Social media posts from other accounts (copyrighted)
- Any AI-generated images without verifying the tool's license allows commercial use

---

## Step 1: Determine What to Search For

Based on the brand profile and ideation brief, construct search queries:

### Query Construction Strategy

1. **Primary query:** Direct description of what you need
   - Example: "person using fitness app gym" or "workout tracking phone"

2. **Mood/aesthetic query:** The feel you want
   - Example: "dark gym atmosphere" or "energetic workout motivation"

3. **Abstract/background query:** For backgrounds and textures
   - Example: "dark gradient abstract" or "gym equipment close up bokeh"

### Niche-Specific Query Templates

For **fitness/gym** projects:
```
- "person working out gym {specific_exercise}"
- "fitness tracking smartphone workout"
- "gym equipment {dumbbells/barbell/cable machine}"
- "athletic person {running/lifting/stretching}"
- "gym interior dark moody"
- "healthy lifestyle fitness motivation"
- "personal training session"
- "progress transformation fitness"
```

For **tech/app** projects:
```
- "person using smartphone app"
- "technology modern interface"
- "mobile app user experience"
- "startup team working"
```

For **food/wellness** projects:
```
- "healthy meal preparation"
- "fresh ingredients cooking"
- "wellness meditation mindfulness"
```

Adapt queries to the project's actual niche from brand.md.

---

## Step 2: Search and Curate

### Method A: WebSearch + WebFetch (Primary)

Search for images on Unsplash, Pexels, and Pixabay:

```
WebSearch: "site:unsplash.com {query}"
WebSearch: "site:pexels.com {query}"
```

Then use WebFetch to browse the results pages and find specific image URLs.

### Method B: Direct API (if available)

**Unsplash API** (if the user has an API key in credentials.env):
```bash
source .social-machine/credentials.env
curl -s "https://api.unsplash.com/search/photos?query={query}&per_page=10&orientation=squarish" \
  -H "Authorization: Client-ID $UNSPLASH_ACCESS_KEY" \
  | python3 -c "import sys,json; [print(p['urls']['regular']) for p in json.load(sys.stdin)['results']]"
```

**Pexels API** (if the user has an API key):
```bash
curl -s "https://api.pexels.com/v1/search?query={query}&per_page=10&orientation=square" \
  -H "Authorization: $PEXELS_API_KEY" \
  | python3 -c "import sys,json; [print(p['src']['large']) for p in json.load(sys.stdin)['photos']]"
```

### Method C: Direct Download via curl

Once you have image URLs from search results:

```bash
# Download image
curl -sL "{image_url}" -o ".social-machine/output/stock/{descriptive_name}.jpg"
```

---

## Step 3: Download Best Matches

Download 3-5 images that best match the post concept. Save to `.social-machine/output/stock/`:

```
.social-machine/output/stock/
├── gym_workout_01.jpg
├── fitness_app_phone_01.jpg
├── dark_gym_atmosphere_01.jpg
└── LICENSES.md
```

### LICENSES.md

Always create/update this file to track image sources:

```markdown
# Stock Image Licenses

All images in this directory are sourced from royalty-free platforms
that permit commercial use without attribution.

| File | Source | Original URL | License |
|------|--------|-------------|---------|
| gym_workout_01.jpg | Unsplash | https://unsplash.com/photos/... | Unsplash License |
| fitness_app_phone_01.jpg | Pexels | https://pexels.com/photo/... | Pexels License |
| dark_gym_atmosphere_01.jpg | Pixabay | https://pixabay.com/photos/... | Pixabay License |

## License Summary
- **Unsplash License:** Free to use for commercial and personal projects. No attribution required (but appreciated).
- **Pexels License:** Free for personal and commercial use. No attribution required.
- **Pixabay License:** Free for commercial use. No attribution required. Cannot be sold as-is.
```

---

## Step 4: Present Options to User

Show the user what was downloaded:

For each image, display:
- File path
- Source and license
- Suggested use: "This would work well as a background for the quote card" or "Good for the feature spotlight hero image"

Use AskUserQuestion:
- **Use image {N} in the design** → note the selected image for the design stage
- **Search for something different** → ask what they want, re-search
- **Skip stock images** → proceed without stock photos
- **Use multiple images** → note which ones for the design

---

## Step 5: Prepare for Design Stage

If images are selected, note them in the ideation brief or create a stock selection file:

```markdown
# Stock Images Selected
selected_stock:
  - path: .social-machine/output/stock/gym_workout_01.jpg
    usage: background with dark overlay
    source: Unsplash
  - path: .social-machine/output/stock/fitness_app_phone_01.jpg
    usage: hero image in device frame
    source: Pexels
```

The design stage will read this and incorporate the images into the graphic.

---

## Image Quality Guidelines

When selecting stock images, prefer:

1. **High resolution** — at least 1200px on the shortest side
2. **Good lighting** — avoid dark, underexposed shots (unless that's the aesthetic)
3. **Authentic feel** — real people in real settings, not overly staged stock poses
4. **Diverse representation** — vary the people shown across posts
5. **On-brand mood** — match the brand's tone (energetic, calm, professional, etc.)
6. **Compositional space** — images with negative space are easier to overlay text on
7. **Color compatibility** — images whose existing colors work with the brand palette

### Red Flags (Avoid These)
- Watermarked images (means they're NOT free)
- Overly generic "business handshake" style stock photos
- Low resolution or heavily compressed images
- Images with visible logos/brands of other companies
- Images of identifiable minors
- Images that could be considered culturally insensitive
