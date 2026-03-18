#!/usr/bin/env python3
"""
Watermark a meme image with a brand logo.

Usage:
    python watermark.py <input_image> <logo_image> <output_image> [--position BR] [--size 60] [--padding 20] [--opacity 0.7]

Positions: BR (bottom-right), BL (bottom-left), TR (top-right), TL (top-left), BC (bottom-center)
"""

import argparse
import sys
from PIL import Image, ImageDraw, ImageFont


def add_watermark(input_path, logo_path, output_path, position="BR", size=60, padding=20, opacity=0.7, add_handle=None):
    """Add a logo watermark to an image with optional @handle text."""
    img = Image.open(input_path).convert("RGBA")
    logo = Image.open(logo_path).convert("RGBA")

    # Resize logo maintaining aspect ratio
    logo_ratio = logo.width / logo.height
    new_height = size
    new_width = int(new_height * logo_ratio)
    logo = logo.resize((new_width, new_height), Image.LANCZOS)

    # Apply opacity to logo
    if opacity < 1.0:
        alpha = logo.split()[3]
        alpha = alpha.point(lambda p: int(p * opacity))
        logo.putalpha(alpha)

    # Create a transparent overlay for compositing
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))

    # Calculate position
    positions = {
        "BR": (img.width - new_width - padding, img.height - new_height - padding),
        "BL": (padding, img.height - new_height - padding),
        "TR": (img.width - new_width - padding, padding),
        "TL": (padding, padding),
        "BC": ((img.width - new_width) // 2, img.height - new_height - padding),
    }

    pos = positions.get(position.upper(), positions["BR"])

    # If we have a handle, shift logo left to make room for text
    if add_handle:
        # Approximate text width
        handle_width = len(add_handle) * 10  # rough estimate
        total_width = new_width + 8 + handle_width
        if position.upper() == "BR":
            pos = (img.width - total_width - padding, pos[1])
        elif position.upper() == "BC":
            pos = ((img.width - total_width) // 2, pos[1])

    overlay.paste(logo, pos, logo)

    # Add handle text if provided
    if add_handle:
        draw = ImageDraw.Draw(overlay)
        text_x = pos[0] + new_width + 8
        text_y = pos[1] + (new_height // 2) - 8
        # Semi-transparent white text
        text_color = (255, 255, 255, int(255 * opacity * 0.6))
        try:
            font = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 16)
        except (OSError, IOError):
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
            except (OSError, IOError):
                font = ImageFont.load_default()
        draw.text((text_x, text_y), add_handle, fill=text_color, font=font)

    # Composite
    result = Image.alpha_composite(img, overlay)

    # Convert to RGB for PNG/JPG output
    if output_path.lower().endswith(".jpg") or output_path.lower().endswith(".jpeg"):
        result = result.convert("RGB")

    result.save(output_path, quality=95)
    print(f"Watermarked: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Add logo watermark to meme images")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("logo", help="Logo image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("--position", default="BR", choices=["BR", "BL", "TR", "TL", "BC"],
                        help="Watermark position (default: BR)")
    parser.add_argument("--size", type=int, default=60, help="Logo height in pixels (default: 60)")
    parser.add_argument("--padding", type=int, default=20, help="Padding from edge (default: 20)")
    parser.add_argument("--opacity", type=float, default=0.7, help="Logo opacity 0-1 (default: 0.7)")
    parser.add_argument("--handle", type=str, default=None, help="Add @handle text next to logo")

    args = parser.parse_args()
    add_watermark(args.input, args.logo, args.output, args.position, args.size, args.padding, args.opacity, args.handle)


if __name__ == "__main__":
    main()
