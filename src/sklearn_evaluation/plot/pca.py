from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import apply_theme, get_color_palette
import numpy as np
import matplotlib.pyplot as plt

def _set_ax_settings(ax, ind1, ind2, targets=None):
    pass

def _validate_inputs(X, n_components, target_names, colors, ax):
    pass

@modify_exceptions
def pca(X, y=None, target_names=None, n_components=2, colors=None, ax=None):
    """
    Plot principle component analysis curve.

    Parameters
    ----------

    X : array-like, shape = [n_samples, n_features]
        Training data, where n_samples is the number of samples and
        n_features is the number of features

    y : array-like or list or None
        set None if ignored otherwise, pass the targets here

    target_names: list, optional
        list of target variable names

    n_components : int, float or 'mle', default=2
        Number of components to keep. If 2, it generates
        the plot of first component vs second component.
        If >=3, all pairwise comparisons are generated.

    colors: list, optional
        colors to be used for the scatter plots for each target.
        If not passed random colors are generated.

    ax : list of matplotlib Axes, optional
        Axes object to draw the plot onto, otherwise uses current Axes.
        If passed the list should have (n_components * n_components-1)/2
        Axes objects

    Notes
    -----
    .. versionadded:: 0.10.1

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot PCA of 3 components:

    .. plot:: ../examples/pca.py

    """
    pass

def _generate_axes(n_components):
    pass

def _plot_generic(n_components, principal_components, ax):
    pass

def _plot_with_target(n_components, target_indices, principal_components, targets, ax):
    pass

def _pca(X, y=None, target_names=None, n_components=2, colors=None, ax=None):
    pass
