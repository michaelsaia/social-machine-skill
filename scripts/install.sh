#!/bin/bash
# Social Machine Skill Installer
# Creates symlinks from this repo into ~/.claude/skills/

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$HOME/.claude/skills"
SKILL_SOURCE="$REPO_DIR/skills/social-machine"
SKILL_TARGET="$SKILLS_DIR/social-machine"

echo "Social Machine Skill Installer"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Source: $SKILL_SOURCE"
echo "Target: $SKILL_TARGET"
echo ""

# Check source exists
if [ ! -d "$SKILL_SOURCE" ]; then
    echo "ERROR: Skill source not found at $SKILL_SOURCE"
    exit 1
fi

# Create skills directory if needed
if [ ! -d "$SKILLS_DIR" ]; then
    echo "Creating $SKILLS_DIR..."
    mkdir -p "$SKILLS_DIR"
fi

# Check for existing installation
if [ -L "$SKILL_TARGET" ]; then
    CURRENT_TARGET=$(readlink "$SKILL_TARGET")
    if [ "$CURRENT_TARGET" = "$SKILL_SOURCE" ]; then
        echo "Already installed and up to date."
        exit 0
    else
        echo "Existing symlink points to: $CURRENT_TARGET"
        echo "Updating to: $SKILL_SOURCE"
        rm "$SKILL_TARGET"
    fi
elif [ -d "$SKILL_TARGET" ]; then
    echo "WARNING: $SKILL_TARGET exists as a directory (not a symlink)."
    echo "Please remove it manually and re-run this script."
    exit 1
fi

# Create symlink
ln -s "$SKILL_SOURCE" "$SKILL_TARGET"
echo "Symlink created: $SKILL_TARGET -> $SKILL_SOURCE"

# Create sub-skill symlinks for direct access
# These allow running /social-scan, /social-research, etc. directly
SUBSKILLS=("config" "scan" "research" "ideate" "design" "capture" "post" "video")

for subskill in "${SUBSKILLS[@]}"; do
    SUB_TARGET="$SKILLS_DIR/social-$subskill"
    SUB_SOURCE="$SKILL_SOURCE/$subskill"

    if [ -d "$SUB_SOURCE" ]; then
        if [ -L "$SUB_TARGET" ]; then
            rm "$SUB_TARGET"
        fi
        ln -s "$SUB_SOURCE" "$SUB_TARGET"
        echo "  Linked: social-$subskill"
    fi
done

echo ""
echo "Installation complete!"
echo ""
echo "Available commands:"
echo "  /social         — Run the full pipeline"
echo "  /social-config  — Configure providers and platforms"
echo "  /social-scan    — Scan project for brand identity"
echo "  /social-research — Research current trends"
echo "  /social-ideate  — Generate post ideas and captions"
echo "  /social-design  — Create graphics"
echo "  /social-capture — Capture app screenshots"
echo "  /social-post    — Publish content"
echo "  /social-video   — Create video content (Phase 2)"
echo ""
echo "Get started: run /social in any project directory."
