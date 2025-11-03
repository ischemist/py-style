"""
A developer script for generating high-quality, perceptually uniform color palettes.

This is not part of the installable package but a tool for development.
It uses the `coloraide` library to perform interpolations in the Oklab colorspace,
which is designed for perceptual uniformity.

Why Oklab?
  - Linear interpolation in RGB space creates "muddy" mid-tones and uneven
    perceptual steps.
  - Oklab is a modern colorspace where geometric distance between colors
    corresponds closely to perceived difference, making gradients smooth
    and aesthetically pleasing.

Usage:
  - Run this script directly: `python -m ischemist.dev.palette_generator`
  - Modify the `if __name__ == "__main__"` block to generate new palettes.
  - Copy the printed output into the `PALETTES` dictionary in `ischemist/style/colors.py`.
"""

from coloraide import Color

# --- Core Generator Functions ---


def generate_palette(
    colors: list[str],
    n_points: int,
    space: str = "oklab",
) -> list[str]:
    """
    Generates a palette by interpolating between a series of colors.

    Args:
        colors: A list of two or more hex color strings to define the gradient segments.
        n_points: The total number of colors in the final palette.
        space: The colorspace to perform interpolation in. "oklab" is recommended.

    Returns:
        A list of hex color codes.
    """
    palette = Color.interpolate(colors, space=space)
    return [palette(i / (n_points - 1)).to_string(hex=True) for i in range(n_points)]


def print_palette_for_registry(name: str, colors: list[str]):
    """Formats the output for easy copy-pasting."""
    print(f'    "{name}": ColorPalette.from_hex_codes([')

    # Print in rows of 8 for readability
    for i in range(0, len(colors), 8):
        chunk = colors[i : i + 8]
        formatted_chunk = ", ".join(f'"{c}"' for c in chunk)
        print(f"        {formatted_chunk},")
    print("    ]),")
