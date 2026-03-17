# Posting Provider: X (Twitter) API v2

Posts tweets with images via the X API v2. Requires API keys in `.social-machine/credentials.env`.

---

## Prerequisites Check

Before posting, verify:

1. Read `.social-machine/credentials.env` and check these are non-empty:
   - `X_API_KEY`
   - `X_API_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

If any are missing, tell the user:
"X API keys not configured. Fill in `.social-machine/credentials.env` or switch to manual posting with `/social-config`."

Provide setup link: https://developer.x.com/en/portal/dashboard

---

## Step 1: Upload Media

Upload the image first using the media upload endpoint.

```bash
# Source credentials
source .social-machine/credentials.env

# Upload media using v2 endpoint
# The image must be uploaded first, then referenced in the tweet

MEDIA_RESPONSE=$(curl -s -X POST "https://api.x.com/2/media/upload" \
  -H "Authorization: OAuth \
    oauth_consumer_key=\"$X_API_KEY\", \
    oauth_token=\"$X_ACCESS_TOKEN\", \
    oauth_signature_method=\"HMAC-SHA256\"" \
  -F "file=@{path_to_image}" \
  -F "media_category=tweet_image")

MEDIA_ID=$(echo $MEDIA_RESPONSE | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['id'])")
```

**Note:** The X API v2 media upload uses OAuth 1.0a User Context. The curl command above is simplified — in practice, generating the OAuth signature requires computing HMAC-SHA1 with the consumer secret and token secret. Use a helper script for this.

### Recommended: Python Helper Script

Create `.social-machine/scripts/post_x.py` if it doesn't exist:

```python
#!/usr/bin/env python3
"""Post a tweet with an image to X/Twitter via API v2."""
import os
import sys
import json
from pathlib import Path

try:
    import tweepy
except ImportError:
    print("ERROR: tweepy not installed. Run: pip install tweepy")
    sys.exit(1)

def post_tweet(image_path: str, caption: str):
    # Load credentials
    env_path = Path(".social-machine/credentials.env")
    creds = {}
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            creds[key.strip()] = val.strip()

    # Authenticate
    auth = tweepy.OAuth1UserHandler(
        creds["X_API_KEY"],
        creds["X_API_SECRET"],
        creds["X_ACCESS_TOKEN"],
        creds["X_ACCESS_TOKEN_SECRET"]
    )

    # Upload media (v1.1 endpoint, still required for media)
    api_v1 = tweepy.API(auth)
    media = api_v1.media_upload(filename=image_path)

    # Post tweet (v2 endpoint)
    client = tweepy.Client(
        consumer_key=creds["X_API_KEY"],
        consumer_secret=creds["X_API_SECRET"],
        access_token=creds["X_ACCESS_TOKEN"],
        access_token_secret=creds["X_ACCESS_TOKEN_SECRET"]
    )

    response = client.create_tweet(
        text=caption,
        media_ids=[media.media_id]
    )

    tweet_id = response.data["id"]
    handle = "yokedapp"  # Read from brand.md
    print(f"SUCCESS: https://x.com/{handle}/status/{tweet_id}")
    return response

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: post_x.py <image_path> <caption>")
        sys.exit(1)
    post_tweet(sys.argv[1], sys.argv[2])
```

---

## Step 2: Post Tweet

```bash
# Read the caption
CAPTION=$(cat .social-machine/output/captions/x.txt)

# Post using helper script
python3 .social-machine/scripts/post_x.py \
  ".social-machine/output/{graphic_file}" \
  "$CAPTION"
```

---

## Rate Limits

- Free tier: 1,500 tweets/month, 85 media uploads/24 hours
- If rate limited: tell the user and suggest waiting or switching to manual posting

---

## Error Handling

| Error | Action |
|---|---|
| 401 Unauthorized | API keys invalid or expired. Regenerate at developer.x.com |
| 403 Forbidden | App doesn't have write permissions. Check app settings. |
| 429 Rate Limited | Hit rate limit. Wait or switch to manual. |
| Media upload fails | Check file size (<5MB for images) and format (PNG, JPG, GIF) |
