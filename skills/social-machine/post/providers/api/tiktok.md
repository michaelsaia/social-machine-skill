# Posting Provider: TikTok Content Posting API

Posts photos and videos to TikTok via the Content Posting API. This has the most restrictive requirements of all platforms.

---

## Prerequisites Check

1. Read `.social-machine/credentials.env` and check:
   - `TIKTOK_ACCESS_TOKEN`

If missing, tell the user:
```
TIKTOK API SETUP:
━━━━━━━━━━━━━━━━

1. Go to developers.tiktok.com → Create App
2. Apply for the Content Posting API (requires app review)
3. Get approved for video.publish scope
4. Generate an access token via OAuth flow

WARNING: Unaudited apps can only post private (self-visible) content.
You must pass TikTok's audit to post publicly.

For most users, manual posting or browser posting is easier for TikTok.
```

---

## Step 1: Check Creator Info

Before posting, verify the user can post:

```bash
source .social-machine/credentials.env

CREATOR_INFO=$(curl -s -X POST \
  "https://open.tiktokapis.com/v2/post/publish/creator_info/query/" \
  -H "Authorization: Bearer $TIKTOK_ACCESS_TOKEN" \
  -H "Content-Type: application/json")

# Check if user can post
# Check max_video_post_duration_sec
# Check if creator has posting capability
```

If the creator cannot post, inform the user and suggest manual posting.

---

## Step 2: Post Photo

For static image posts (Phase 1):

```bash
# Initialize photo post
INIT_RESPONSE=$(curl -s -X POST \
  "https://open.tiktokapis.com/v2/post/publish/inbox/photo/init/" \
  -H "Authorization: Bearer $TIKTOK_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "post_info": {
      "title": "{caption_text}",
      "privacy_level": "MUTUAL_FOLLOW_FRIENDS",
      "disable_duet": false,
      "disable_comment": false,
      "disable_stitch": false
    },
    "source_info": {
      "source": "FILE_UPLOAD",
      "photo_count": 1
    }
  }')

PUBLISH_ID=$(echo $INIT_RESPONSE | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['publish_id'])")
UPLOAD_URL=$(echo $INIT_RESPONSE | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['upload_url'])")

# Upload the image
curl -s -X PUT "$UPLOAD_URL" \
  -H "Content-Type: image/png" \
  --data-binary @{path_to_image}
```

---

## Step 3: Check Post Status

```bash
STATUS_RESPONSE=$(curl -s -X POST \
  "https://open.tiktokapis.com/v2/post/publish/status/fetch/" \
  -H "Authorization: Bearer $TIKTOK_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"publish_id\": \"$PUBLISH_ID\"}")

# Check status: PROCESSING_UPLOAD, PROCESSING_DOWNLOAD, PUBLISH_COMPLETE, FAILED
```

---

## Rate Limits

- 6 requests per minute per user
- 15 posts per day per user
- Each user access_token: 6 requests/minute

---

## Important Restrictions

1. **Privacy level:** API clients must let users choose privacy level — no default value allowed
2. **Unaudited apps:** All content is private-only until your app passes TikTok's audit
3. **Commercial content:** Must be disclosed if promotional
4. **Duration limits:** Check `max_video_post_duration_sec` from creator_info

---

## Error Handling

| Error | Action |
|---|---|
| access_token expired | Re-authenticate via OAuth flow |
| spam_risk_too_many_posts | Hit daily limit. Wait until tomorrow. |
| unaudited_client_can_only_post_to_private | App not audited. Posts will be private. |
| photo format not supported | Convert to JPEG. TikTok prefers JPEG. |

---

## Recommendation

For most users, TikTok's API restrictions make manual posting or browser posting more practical. The API is best suited for businesses that have gone through the audit process. Consider suggesting the user switch to `manual` or `browser` provider for TikTok specifically.
