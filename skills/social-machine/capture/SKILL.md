---
name: social-capture
version: 0.1.0
description: |
  Capture app screenshots and screen recordings from iOS Simulator, browser, or running
  applications. Use when the user needs screenshots for social media content or runs
  "/social-capture".
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - AskUserQuestion
---

# Social Machine: Capture

You are running `/social-capture`. This captures screenshots and recordings from the user's running app for use in social media graphics.

---

## Prerequisites

1. Read `.social-machine/brand.md` for project context
2. Read `.social-machine/config.md` for settings

---

## Step 1: Detect Available Capture Sources

Check what's available to capture from:

### iOS Simulator
```bash
# Check if simulator is running
xcrun simctl list devices booted 2>/dev/null
```

If a simulator is booted:
- Can capture screenshots: `xcrun simctl io booted screenshot {output_path}`
- Can capture video: `xcrun simctl io booted recordVideo {output_path}`

### Running Web App
Check if there's a dev server running:
```bash
# Common dev server ports
lsof -i :3000 -i :8080 -i :8000 -i :5173 -i :4200 2>/dev/null | grep LISTEN
```

If a dev server is running, capture via headless browser:
```bash
$B goto http://localhost:{port}
$B screenshot {output_path}
```

### Browser (gstack/browse)
If the project has a live website (from brand.md), can screenshot that:
```bash
$B goto {website_url}
$B screenshot {output_path}
```

---

## Step 2: Ask What to Capture

Use AskUserQuestion to ask the user what they want to capture:

Options should be based on what's available:
- **iOS Simulator screenshot** (if simulator is booted)
- **Web app screenshot** (if dev server is running)
- **Live website screenshot** (if website URL exists in brand.md)
- **Specific screen/page** — ask the user which screen they want

---

## Step 3: Capture

### iOS Simulator Screenshot
```bash
# Take screenshot
xcrun simctl io booted screenshot /tmp/social-machine-capture.png

# Copy to output directory
cp /tmp/social-machine-capture.png .social-machine/output/capture_{date}_{description}.png
```

**Tips for better simulator captures:**
- The user should navigate to the desired screen before capture
- Ask the user: "Navigate your simulator to the screen you want to capture, then tell me when ready"
- Capture at the simulator's native resolution for best quality

### iOS Simulator Video Recording
```bash
# Start recording (runs in background)
xcrun simctl io booted recordVideo .social-machine/output/capture_{date}.mp4 &
RECORD_PID=$!

# Tell user recording has started
# Wait for user to say "stop"

# Stop recording
kill -INT $RECORD_PID
```

### Web App / Website Screenshot
```bash
# Navigate to the page
$B goto {url}

# Wait for content to load
$B wait --networkidle

# Optional: set specific viewport for mobile look
$B viewport 390x844  # iPhone 14 Pro dimensions

# Take screenshot
$B screenshot .social-machine/output/capture_{date}_{description}.png
```

### Multiple Screens
If the user wants screenshots of multiple screens:
1. Capture each one sequentially
2. Name them descriptively: `capture_{date}_home.png`, `capture_{date}_workout.png`, etc.
3. List all captured files when done

---

## Step 4: Post-Processing (Optional)

After capture, optionally enhance the screenshots:

### Device Mockup Frame
Wrapping a screenshot in a device frame makes it look more professional for social media.
This is best handled by the design stage — the HTML/CSS provider can embed the raw screenshot in a CSS-styled device frame.

Save the raw screenshot and note its path for the design stage to use.

### Cropping
If the screenshot includes unnecessary status bar or navigation elements:
```bash
# If ImageMagick is available
convert {input} -crop {width}x{height}+{x}+{y} {output}
```

---

## Step 5: Output

Save all captures to `.social-machine/output/` and report:
- File paths of all captured images/videos
- Resolution of each capture
- Suggestion: "These captures are ready for the design stage. Run `/social-design` to create a graphic using them, or run `/social` to continue the full pipeline."
