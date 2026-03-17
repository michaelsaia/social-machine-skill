# Posting Provider: Manual

The simplest posting method. Saves all content to the output directory and provides clear instructions for the user to post manually.

---

## Step 1: Organize Output

Ensure all files are in `.social-machine/output/`:

```
.social-machine/output/
├── {date}_{type}_instagram_1080x1080.png
├── {date}_{type}_x_1200x675.png
├── {date}_{type}_source.html
├── ideation-brief.md
└── captions/
    ├── instagram.txt
    └── x.txt
```

Create the `captions/` directory and write platform-specific caption files:

**instagram.txt:**
```
{Full caption text}

{Hashtags on a new line}
```

**x.txt:**
```
{Concise tweet text with hashtags}
```

---

## Step 2: Copy Caption to Clipboard

For the first/primary platform, copy the caption to the system clipboard:

```bash
# macOS
cat .social-machine/output/captions/{platform}.txt | pbcopy
```

Tell the user: "Caption copied to clipboard."

---

## Step 3: Open Platform (Optional)

Ask the user if they want to open the platform in their browser:

```bash
# macOS
open "https://instagram.com"   # or twitter.com, tiktok.com, etc.
```

---

## Step 4: Provide Instructions

Give the user clear steps:

```
MANUAL POSTING INSTRUCTIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Open the graphic file:
   open .social-machine/output/{graphic_filename}

2. The caption has been copied to your clipboard (Cmd+V to paste)

3. On Instagram:
   - Open Instagram app or instagram.com
   - Create new post → upload the graphic
   - Paste the caption
   - Post!

4. On X/Twitter:
   - The caption is in: .social-machine/output/captions/x.txt
   - Open x.com → compose tweet
   - Upload the graphic + paste caption

All files saved in: .social-machine/output/
```

---

## Notes

- This provider has zero external dependencies
- Works immediately with no API setup
- The user has full control over when and how they post
- Caption files can be edited before posting
- Graphics can be previewed and adjusted before uploading
