from ischemist.dev.generate_palette import generate_palette, print_palette_for_registry

if __name__ == "__main__":
    print("--- Generating Palettes for `ischemist.style.colors.py` ---")
    print("Copy the output below into the `PALETTES` dictionary.\n")

    # --- Example 1: A better sequential blue palette ---
    # Interpolating from a deep blue to a light cyan in Oklab space
    soft_blue_20 = generate_palette(["#0d0887", "#6eceb1", "#f0f921"], 20)
    print_palette_for_registry("soft_blue_20", soft_blue_20)

    # --- Example 2: A "magma"-like diverging palette ---
    # This shows a multi-point gradient
    magma_20 = generate_palette(["#000004", "#51127c", "#f89540", "#fcfdbf"], 20)
    print_palette_for_registry("magma_20", magma_20)

    # --- Example 3: A Cubehelix palette for scientific visualization ---
    # This is excellent for line plots as it has a monotonic lightness gradient
    # which also works in grayscale.
    # science_helix_20 = generate_cubehelix_palette(
    #     n_points=20,
    #     start_hue=260, # Start at a purplish color
    #     rotations=-0.8, # Rotate towards yellow/green
    #     hue_gamma=0.8,
    #     lightness_gamma=1.2,
    # )
    # print_palette_for_registry("science_helix_20", science_helix_20)

    # --- Example 4: A qualitative palette using spline interpolation ---
    # This creates smooth, non-linear paths between colors.
    # We use `oklch` to keep lightness and chroma more consistent.
    # Note: coloraide uses `natural` for natural splines
    qual_spline_12 = generate_palette(
        ["#5e2a73", "#00558d", "#00767b", "#438a5b", "#a1932f", "#d29241"],
        n_points=12,
        space="oklch",  # LCh is good for this
    )
    print_palette_for_registry("qual_spline_12", qual_spline_12)
