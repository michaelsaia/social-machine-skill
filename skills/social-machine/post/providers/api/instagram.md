# Posting Provider: Instagram Graph API

Posts photos to Instagram via the Instagram Graph API (through Meta/Facebook). This has more setup requirements than X.

---

## Prerequisites Check

Before posting, verify:

1. Read `.social-machine/credentials.env` and check these are non-empty:
   - `INSTAGRAM_ACCESS_TOKEN`
   - `INSTAGRAM_BUSINESS_ACCOUNT_ID`

If missing, tell the user:
"Instagram API not configured. You need a Facebook Business account connected to your Instagram Business/Creator account."

Provide setup guide:
```
INSTAGRAM API SETUP:
━━━━━━━━━━━━━━━━━━━

1. Convert Instagram to a Business or Creator account
2. Create a Facebook Page and link it to your Instagram
3. Go to developers.facebook.com → Create App → Business type
4. Add Instagram Graph API product
5. Generate a long-lived access token
6. Get your Instagram Business Account ID:

   curl -s "https://graph.facebook.com/v22.0/me/accounts?access_token={TOKEN}" \
     | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['data'][0]['id'])"

   Then get the Instagram account linked to that page:
   curl -s "https://graph.facebook.com/v22.0/{PAGE_ID}?fields=instagram_business_account&access_token={TOKEN}" \
     | python3 -c "import sys,json; print(json.load(sys.stdin)['instagram_business_account']['id'])"

7. Add both values to .social-machine/credentials.env
```

---

## Step 1: Host Image Publicly

**Instagram's API requires the image to be at a publicly accessible URL.** This is the biggest pain point.

Options for hosting:

### Option A: Temporary hosting via file.io (simplest)
```bash
UPLOAD_RESPONSE=$(curl -s -F "file=@{path_to_image}" https://file.io)
IMAGE_URL=$(echo $UPLOAD_RESPONSE | python3 -c "import sys,json; print(json.load(sys.stdin)['link'])")
```

### Option B: Upload to project's existing hosting
If the project has an R2 bucket, S3 bucket, or other hosting:
```bash
# Example for Cloudflare R2 via wrangler
wrangler r2 object put {bucket}/social-machine/{filename} --file={path_to_image}
IMAGE_URL="https://{bucket_domain}/social-machine/{filename}"
```

### Option C: GitHub raw content (if public repo)
```bash
# Commit the image and use raw.githubusercontent.com URL
# Not recommended for private repos
```

Tell the user which hosting method is being used. If none are available, suggest they set up file.io or switch to manual posting.

---

## Step 2: Create Media Container

```bash
source .social-machine/credentials.env

# Create media container
CONTAINER_RESPONSE=$(curl -s -X POST \
  "https://graph.facebook.com/v22.0/$INSTAGRAM_BUSINESS_ACCOUNT_ID/media" \
  -F "image_url=$IMAGE_URL" \
  -F "caption=$(cat .social-machine/output/captions/instagram.txt)" \
  -F "access_token=$INSTAGRAM_ACCESS_TOKEN")

CREATION_ID=$(echo $CONTAINER_RESPONSE | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")
```

---

## Step 3: Check Container Status

The container needs time to process. Poll until ready:

```bash
# Wait a few seconds for processing
sleep 5

STATUS=$(curl -s \
  "https://graph.facebook.com/v22.0/$CREATION_ID?fields=status_code&access_token=$INSTAGRAM_ACCESS_TOKEN" \
  | python3 -c "import sys,json; print(json.load(sys.stdin).get('status_code','UNKNOWN'))")

# Status should be "FINISHED"
# If "IN_PROGRESS", wait and retry (max 3 attempts)
# If "ERROR", check the error message
```

---

## Step 4: Publish

```bash
PUBLISH_RESPONSE=$(curl -s -X POST \
  "https://graph.facebook.com/v22.0/$INSTAGRAM_BUSINESS_ACCOUNT_ID/media_publish" \
  -F "creation_id=$CREATION_ID" \
  -F "access_token=$INSTAGRAM_ACCESS_TOKEN")

POST_ID=$(echo $PUBLISH_RESPONSE | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")
echo "SUCCESS: Posted to Instagram (ID: $POST_ID)"
```

---

## Error Handling

| Error | Action |
|---|---|
| Invalid access token | Token expired. Regenerate at developers.facebook.com |
| Image URL not accessible | Image hosting failed. Try a different hosting method. |
| (#9004) Media upload timed out | Image too large or hosting too slow. Compress image. |
| Permission error | App doesn't have instagram_content_publish permission |
| Container status ERROR | Check image format (JPEG recommended) and size (<8MB) |

---

## Notes

- Instagram captions support up to 2,200 characters
- Hashtags can go in the caption or first comment (caption is simpler via API)
- The API does not support Stories posting to personal accounts — only Business/Creator
- Access tokens expire. Long-lived tokens last 60 days. Set a reminder to refresh.
- Rate limit: 25 API calls per user per hour for content publishing
