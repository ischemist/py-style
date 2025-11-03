import numpy as np
import plotly.graph_objects as go

from ischemist.colors import PALETTES, ColorPalette
from ischemist.dev.visualize import plot_palettes
from ischemist.plotly import Styler


def visualize_line_differentiability(palette: ColorPalette, n_lines: int = 8, dark_mode: bool = False):
    """generates a dummy plot of training-like curves to test color differentiability."""
    fig = go.Figure()
    styler = Styler(dark=dark_mode, title_size=18)

    x = np.linspace(0, 10, 100)
    colors = palette.sample(n_lines, as_hex=True)

    for i in range(n_lines):
        # generate slightly different curves
        offset = 1 - (i * 0.05)
        decay = 0.5 + (i * 0.1)
        noise = np.random.normal(0, 0.01, size=x.shape)
        y = (1 - offset * np.exp(-decay * x)) + noise

        fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name=f"curve_{i + 1}", line=dict(color=colors[i], width=2.5)))

    styler.apply_style(fig)
    fig.update_layout(
        title=f"Line Differentiability Test: ({'dark' if dark_mode else 'light'})",
        xaxis_title="Epochs",
        yaxis_title="Metric",
    )
    return fig


if __name__ == "__main__":
    all_fig = plot_palettes(PALETTES, cols=5, title="All Registered Palettes")
    all_fig.show()

    # 2. test a specific palette for line plots
    # using 'blue_red_20' bc it's a good candidate for this kind of thing
    test_palette = PALETTES["blue_red_20"]

    light_lines_fig = visualize_line_differentiability(test_palette, n_lines=10, dark_mode=False)
    light_lines_fig.show()

    dark_lines_fig = visualize_line_differentiability(test_palette, n_lines=10, dark_mode=True)
    dark_lines_fig.show()
