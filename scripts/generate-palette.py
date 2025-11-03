from ischemist.colors import ColorPalette
from ischemist.dev.generate_palette import generate_pastel_palette, print_palette_for_registry
from ischemist.dev.visualize import plot_palettes

if __name__ == "__main__":
    generated_palettes = {}

    for lightness in [0.8, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.95]:
        for chroma in [0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.15]:
            soft_pastels_12 = generate_pastel_palette(12, lightness=lightness, chroma=chroma)
            generated_palettes[f"soft_pastels_{lightness}_{chroma}"] = ColorPalette.from_hex_codes(soft_pastels_12)

    if generated_palettes:
        print("\n--- 2. Visualizing NEWLY Generated Palettes ---")
        new_fig = plot_palettes(
            generated_palettes,
            cols=min(4, len(generated_palettes)),
            title="Preview of Newly Generated Palettes",
        )
        new_fig.show()
    else:
        print("\n--- No new palettes generated. ---")

    print_palette_for_registry("pastel", generate_pastel_palette(8, lightness=0.7879, chroma=0.1121))
