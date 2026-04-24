from contextlib import contextmanager
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
from sklearn_evaluation.util import truncate_colormap
from ploomber_core import validate

@contextmanager
def tmp_theme(ax_style, cmap_style):
    """
    Adds a scheme coloring and styling to matplotlib plots.

    Parameters
    ----------
    ax_style : str, default 'no_frame'
        Define which ax style to apply.

        Availble styles:
        'no_frame' no top and right boundaries

        'frame' ax with border

    cmap_style : str, default 'monochromatic'
        Define which cmap style to apply.

        Availble styles:

        'monochromatic' a palette in which a single color tint is used

        'gradient' a palette of two colors gradually shift from one to another
    """
    pass

def _validate_inputs(ax_style, cmap_style):
    pass

def _set_default_rc_params(ax_style):
    """
    Set default rcParams
    """
    pass

def get_color_palette(n_colors=None):
    """
    Returns default color palette
    """
    pass

def apply_theme(ax_style='no_frame', cmap_style='monochromatic'):
    """
    Decorates plotting function and applies a visual theme to matplotlib plots.

    Parameters
    ----------
    ax_style : str, default 'no_frame'
        Define which ax style to apply.

        Availble styles:
        'no_frame' wihout top and right boundaries

        'frame' ax with border

    cmap_style : str, default 'monochromatic'
        Define which cmap style to apply.

        Availble styles:

        'monochromatic' a palette in which a single color tint is used

        'gradient' a palette of two colors gradually shift from one to another
    """
    pass

def _set_default_plot_colors(cmap_style):
    pass

def default_cmap():
    """
    Returns palette in which a single color tint is used.
    """
    pass

def gradient_cmap():
    """
    Returns a palette of two colors gradually shift from one to another
    """
    pass

def default_heatmap():
    pass
