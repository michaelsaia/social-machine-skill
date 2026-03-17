# Social Machine — Deferred Work

## Phase 2: Content Types
- [ ] **Carousel support** — Multi-image posts for Instagram. Need HTML template that generates multiple slides + Instagram API carousel endpoint.
- [ ] **Thread support** — X/Twitter thread posting. Chain multiple tweets with reply_to.
- [ ] **Story format** — 1080x1920 ephemeral content for Instagram/Facebook Stories.

## Phase 2: Video
- [ ] **ElevenLabs integration** — Full implementation of AI voiceover + video combining. Framework in `video/providers/elevenlabs.md`.
- [ ] **Browser screen recording** — Record scripted browser interactions as video. Framework in `video/providers/browser-record.md`.
- [ ] **Simulator capture** — Full iOS Simulator recording workflow. Framework in `video/providers/simulator-capture.md`.
- [ ] **Auto-captions** — Burn subtitles into videos (85% of social video watched on mute).

## Phase 2: Intelligence
- [ ] **Git log feature detection** — Auto-detect new features from recent commits and suggest posts about them. "You shipped AI coaching 2 days ago — want to post about it?"
- [ ] **Competitor content scanning** — Research what competitors are posting. WebSearch-based, not scraping.
- [ ] **Optimal posting times** — Research best times to post per platform/niche.
- [ ] **A/B caption testing** — Generate multiple variants, post one, suggest testing the other next time.

## Phase 2: API Posting
- [ ] **X API posting** — Full implementation with OAuth 1.0a and tweepy. Helper script in `post/providers/api/x.md`.
- [ ] **Instagram API posting** — Full implementation with image hosting. Setup guide in `post/providers/api/instagram.md`.
- [ ] **TikTok API posting** — Full implementation (requires app audit for public posts).

## Phase 3: Analytics & Learning
- [ ] **Engagement metrics pull** — Pull likes/comments/shares back from platform APIs.
- [ ] **Content performance analysis** — Track which content types/hooks perform best.
- [ ] **Auto-adjust strategy** — Learn from engagement data to improve recommendations.
- [ ] **Content calendar** — Plan a week/month of varied content in advance.

## Phase 4: Distribution
- [ ] **OpenClaw adapter** — Portable version that works outside Claude Code.
- [ ] **Multi-project support** — Run Social Machine across multiple projects from one place.
- [ ] **Team sharing** — Share brand profiles and templates across team members.
- [ ] **Marketplace distribution** — Package for Claude Code skill marketplace.

## Infrastructure
- [ ] **PowerPoint provider** — Generate PPTX files for teams that use slides.
- [ ] **Canva API provider** — Integration with Canva's design API (if available).
- [ ] **Image hosting service** — Built-in temporary image hosting for Instagram API (which requires public URLs).
- [ ] **Token refresh automation** — Auto-refresh expiring OAuth tokens (especially Instagram's 60-day tokens).
