# Memegen API Provider — Real Meme Template Graphics

This provider generates memes using REAL meme templates (Drake, Expanding Brain,
Distracted Boyfriend, etc.) via the free memegen.link API, then watermarks them
with the brand logo.

**When to use this:** When the ideation brief specifies a well-known meme FORMAT
that has a real template (Drake, Expanding Brain, etc.). For custom/original meme
layouts (alignment charts, tweet screenshots, hot takes), use html-screenshot instead.

## How It Works

```
1. Pick template from memegen.link (208+ templates, free, no auth)
2. Construct URL with meme text
3. Download the generated image
4. Watermark with brand logo + handle using watermark.py
5. Save to output directory
```

## Step 1: Select Template

Match the meme format from the ideation brief to a memegen template ID.

### Common Template IDs

| Format | Template ID | Lines | Notes |
|--------|------------|-------|-------|
| Drake (Reject/Prefer) | `drake` | 2 | Top = reject, Bottom = prefer |
| Expanding Brain | `gb` | 4 | 4 levels of brain |
| Distracted Boyfriend | `db` | 3 | Girl, Guy, Girlfriend |
| Change My Mind | `cmm` | 1 | Single text line |
| Always Has Been | `astronaut` | 4 | Wait/Always has been/Flat/Round |
| Woman Yelling at Cat | `woman-cat` | 2 | Left = yelling, Right = cat |
| Hide the Pain Harold | `harold` | 2 | Top/bottom text |
| Roll Safe | `rollsafe` | 2 | "Can't X if you Y" format |
| Disaster Girl | `disastergirl` | 2 | Top/bottom text |
| Is This a Pigeon | `pigeon` | 2 | Top/bottom text |
| Running Away Balloon | `balloon` | 3 | Opportunities running away |
| Two Buttons | `buttons` | 3 | Left/Right/Person |
| Expectation vs Reality | `dbg` | 2 | Left = expect, Right = reality |
| Honest Work | `bihw` | 2 | "It ain't much" format |
| Why Not Both | `both` | 2 | Top/bottom |
| American Chopper | `chair` | 6 | 5-panel argument |
| This Is Fine | `fine` | 2 | Dog in fire |
| One Does Not Simply | `mordor` | 2 | Boromir meme |
| Buzz Lightyear | `buzz` | 2 | "X, X everywhere" |
| Confession Bear | `cb` | 2 | Top/bottom confession |

### Browse All Templates

To see all available templates, fetch:
```
curl -s "https://api.memegen.link/templates" | python3 -c "
import json, sys
for t in json.load(sys.stdin):
    print(f\"{t['id']:30s} | {t['name']} ({t['lines']} lines)\")
"
```

Or search for a specific one:
```
curl -s "https://api.memegen.link/templates?filter=drake"
```

## Step 2: Construct the URL

### URL Format
```
https://api.memegen.link/images/{template_id}/{line1}/{line2}/.../{lineN}.png
```

### Text Encoding Rules

The memegen API uses a custom URL encoding scheme. **Getting this wrong is the #1 source
of broken memes.** The tilde (`~`) codes are memegen-specific — they are NOT standard
URL encoding.

| Character | Encoding | Example | Notes |
|-----------|----------|---------|-------|
| Space | `_` (underscore) | `hello_world` | Most common — every space becomes underscore |
| `"` (quotes) | `''` (two single quotes) | `he_said_''hello''` | NOT escaped quotes — literally two apostrophes |
| `?` | `~q` | `why~q` | Tilde-q, NOT %3F |
| `#` | `~h` | `~h1_trending` | Tilde-h |
| `/` | `~s` | `24~s7` | Tilde-s — critical since / is the line separator |
| `$` | `%24` | `%24200` | **USE URL ENCODING, NOT ~d.** `~d` renders literally as "~d" on the image. Use `%24` for dollar signs. |
| `-` (hyphen) | `--` (double dash) | `well--known` | Single `-` works in most cases but `--` is safer for literal hyphens |
| `_` (literal underscore) | `__` (double underscore) | `my__var` | Since single `_` = space |
| Blank/empty line | `_` | Just underscore | Renders as empty text for that line |
| Newline within a line | `~n` | `line_one~nline_two` | Forces a line break inside one text box |
| `'` (apostrophe) | `'` | `buddy's` | Apostrophes work as-is — no encoding needed |
| `(` `)` (parens) | `(` `)` | `(optional)` | Work as-is |
| `!` | `!` | `let's_go!` | Works as-is |
| `&` | `%26` | `you_%26_me` | Use URL encoding |
| `+` | `%2B` | `1_%2B_1` | Use URL encoding |
| `%` | `%25` | `100%25` | Use URL encoding |
| `:` | `:` | `POV:_something` | Works as-is |
| `@` | `@` | `@yokedapp` | Works as-is |
| Emoji | Paste directly | `😭` | Unicode emoji work in URLs |

### CRITICAL GOTCHAS (learned the hard way)

1. **`~d` does NOT mean dollar sign.** It renders literally as "~d" in the meme text.
   Use `%24` (standard URL encoding) for `$` instead. Example: `%24200` → "$200"

2. **Always use `-sL` with curl.** The API returns 301 redirects for some URL patterns.
   Without `-L` (follow redirects), you get an empty/broken file.

3. **Line separators are forward slashes `/`.** If your meme text contains a literal
   slash, you MUST encode it as `~s` or the API will interpret it as a new text line.
   Example: "24/7" → `24~s7`

4. **Quotes need two single quotes, not backslash-quote.** `"hello"` → `''hello''`
   This looks weird in the URL but renders correctly as quotation marks on the image.

5. **Apostrophes just work.** `buddy's` → `buddy's` — no encoding needed. Don't
   over-encode them.

6. **Keep lines SHORT.** The API auto-wraps text but it gets ugly fast on narrow
   templates. Aim for under 40 characters per line. If you need more words, use `~n`
   to control where line breaks happen instead of letting the API decide.

7. **The `.png` extension matters.** Always end the URL path with `.png` (or `.jpg`).
   Without it, you may get a JSON response instead of an image.

8. **Test your URL in a browser first** if you're unsure about encoding. Just paste
   the full URL into a browser tab — you'll see the meme instantly and can verify
   the text renders correctly before downloading.

### Query Parameters

| Param | Description | Example |
|-------|-------------|---------|
| `width` | Image width in pixels | `?width=1080` |
| `height` | Image height in pixels | `?height=1080` |
| `style` | Template style variant | `?style=default` |
| `font` | Font override | `?font=impact` |

**IMPORTANT:** Always use `?width=1080` minimum for social media quality.
If both width and height are provided, the image will be padded to exact dimensions.

### Example URLs (tested, working)

**Drake (2 lines — reject / prefer):**
```
https://api.memegen.link/images/drake/The_old_way_of_doing_things/The_better_way_your_product_enables.png?width=1080&height=1080
```

**Expanding Brain (4 lines — note %24 for dollar sign):**
```
https://api.memegen.link/images/gb/Basic_approach/Slightly_better/Paying_%24200~smo_for_the_''premium''_version/Your_product's_approach.png?width=1080
```

**Distracted Boyfriend (3 lines = other woman, boyfriend, girlfriend):**
```
https://api.memegen.link/images/db/Shiny_new_thing/Me/What_I_should_be_doing.png?width=1080&height=1080
```

**Change My Mind (1 line):**
```
https://api.memegen.link/images/cmm/Your_hot_take_goes_here.png?width=1080
```

## Step 3: Download the Image

Use curl with `-sL` (follow redirects, silent):

```bash
curl -sL -o "{output_path}" "{memegen_url}"
```

Verify the download succeeded:
```bash
file "{output_path}"  # Should show PNG/JPEG image data
```

## Step 4: Watermark with Brand Logo

Use the watermark script to add the brand logo + handle:

```bash
/tmp/meme-tools/bin/python3 /path/to/social-machine-skill/scripts/watermark.py \
  "{downloaded_meme}" \
  "{brand_logo_path}" \
  "{final_output_path}" \
  --position BR \
  --size 48 \
  --padding 15 \
  --opacity 0.8 \
  --handle "@{brand_handle}"
```

### Watermark Setup (first time only)

The watermark script needs Pillow. Create a venv if it doesn't exist:

```bash
if [ ! -d /tmp/meme-tools ]; then
  python3 -m venv /tmp/meme-tools
  /tmp/meme-tools/bin/pip install Pillow
fi
```

### Watermark Options

| Option | Default | Description |
|--------|---------|-------------|
| `--position` | BR | BR, BL, TR, TL, BC (bottom-right recommended) |
| `--size` | 60 | Logo height in pixels (48-60 for memes) |
| `--padding` | 20 | Distance from edge (15-20 for memes) |
| `--opacity` | 0.7 | Logo transparency (0.7-0.8 for subtle branding) |
| `--handle` | None | Add @handle text next to logo |

## Step 5: Save Output

Save files following the standard naming convention:
```
.social-machine/output/
├── {date}_meme_{format}_raw.png         # Raw from memegen API
├── {date}_meme_{format}_instagram_1080x1080.png  # Branded final
└── {date}_meme_{format}_x_1200x675.png  # Branded, platform-sized
```

## Platform Sizing

For different platforms, use width/height query params:
- **Instagram:** `?width=1080&height=1080` (will pad to square)
- **X/Twitter:** `?width=1200&height=675`
- **Stories/TikTok:** `?width=1080&height=1920` (most meme formats don't work portrait)

**Note:** Most classic meme formats look best at their native aspect ratio. For Instagram
square, it's often better to download at native ratio and let the padding fill in. For
X landscape, some formats work (drake, change my mind) but multi-panel ones may get too small.

## When NOT to Use This Provider

Use `html-screenshot` instead when:
- The meme format is a **custom layout** (alignment chart, tweet screenshot, hot take card)
- The content needs **brand colors** as the primary design element
- The meme is a **text-only format** (nobody:/me:, unpopular opinion)
- You need **pixel-perfect control** over typography and layout
- The concept is **original** and doesn't map to a classic template

Use `memegen-api` when:
- The meme uses a **well-known template** with recognizable imagery (Drake, Brain, Distracted BF)
- The humor relies on the **familiar template visuals** being present
- Speed matters — API memes are generated in seconds vs building HTML
- The brand identity comes from the **text/humor**, not the visual design

## Combining Providers

You can use BOTH providers in one session:
1. Use memegen-api for the classic template memes
2. Use html-screenshot for custom-designed memes (alignment chart, tweet card, hot take)
3. Watermark everything with the brand logo for consistency

This gives you the best of both worlds — authentic meme energy from real templates
AND polished custom designs for original formats.
