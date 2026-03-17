# Posting Provider: Browser Automation

Posts content by automating the platform's web UI via headless browser. No API keys needed but more fragile than API posting.

---

## WARNING

Browser automation for social media posting carries risks:
- Platforms actively detect and may ban accounts using automation
- UI changes break the automation without notice
- Login sessions may require 2FA which can't be automated
- This approach is **less reliable** than API or manual posting

**Recommendation:** Use this only as a convenience layer, not for high-volume posting. For reliable automated posting, use the API provider.

---

## Prerequisites

- gstack/browse (headless browser) must be available
- User must be logged into the target platforms in their browser
- Cookies should be imported via `/setup-browser-cookies` if available

---

## X (Twitter) Posting

```bash
# Navigate to compose
$B goto https://x.com/compose/tweet

# Wait for compose box
$B wait --networkidle
$B snapshot -i

# Find the text input area and fill caption
$B fill "[data-testid='tweetTextarea_0']" "{caption_text}"

# Upload image - find the media upload button
$B snapshot -i
# Click the image upload icon
$B click "[data-testid='fileInput']"
$B upload "[data-testid='fileInput']" {path_to_image}

# Wait for upload to complete
$B wait --networkidle

# Click the post button
$B click "[data-testid='tweetButton']"

# Verify success
$B wait --networkidle
$B snapshot -D
```

**Note:** Selectors may change. If the above selectors fail, use `$B snapshot -i` to find the current interactive elements and adapt.

---

## Instagram Posting

Instagram web has limited posting support. The workflow:

```bash
# Navigate to Instagram
$B goto https://instagram.com

# Instagram web does support creating posts
# Click the "Create" button (+ icon)
$B snapshot -i
# Find and click the create post button

# This is fragile and may require 2FA or login
# Recommend manual posting for Instagram
```

**Recommendation:** Instagram's web UI for posting is limited and fragile. Suggest the user use manual posting for Instagram.

---

## LinkedIn Posting

```bash
$B goto https://linkedin.com/feed/
$B wait --networkidle
$B snapshot -i

# Click "Start a post"
# Upload image
# Add caption
# Click Post
```

---

## General Approach

For any platform:

1. `$B goto {platform_url}` — navigate to the platform
2. `$B snapshot -i` — find interactive elements
3. Find the compose/create button and click it
4. Upload the image via file input
5. Fill the caption text
6. Click the post/publish button
7. `$B snapshot -D` — verify the post was created

---

## Error Handling

| Issue | Action |
|---|---|
| Not logged in | Ask user to log in manually first, or use `/setup-browser-cookies` |
| 2FA required | Cannot automate. Switch to manual posting. |
| Selectors changed | Use `$B snapshot -i` to find new selectors. Inform user. |
| Upload fails | Check file size and format. Try JPEG if PNG fails. |
| Platform blocks automation | Switch to manual or API posting. |

---

## Notes

- Always screenshot before and after posting for verification
- Save screenshots to `.social-machine/output/` as evidence of posting
- If browser posting fails, automatically fall back to manual posting instructions
- Never store login credentials — rely on existing browser sessions
