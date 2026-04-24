"""
Plots for clustering models

NOTE: this is largely based in the scikit-plot cluster module. License below.

MIT License

Copyright (c) [2018] [Reiichiro Nakano]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn.base import clone
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.preprocessing import LabelEncoder
from joblib import Parallel, delayed
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import apply_theme

def _generate_axes(cluster, figsize, ax):
    pass

@modify_exceptions
def elbow_curve(X, clf, range_n_clusters=None, n_jobs=1, show_cluster_time=True, ax=None):
    """Plots elbow curve of different values of K of a clustering algorithm.

    Parameters
    ----------
    X : array-like, shape = [n_samples, n_features]:
        Data to cluster, where n_samples is the number of samples and
        n_features is the number of features.
        Refer https://numpy.org/doc/stable/glossary.html#term-array-like

    clf
        Clusterer instance that implements ``fit``,``fit_predict``, and
        ``score`` methods, and an ``range_n_clusters`` hyperparameter.
        e.g. :class:`sklearn.cluster.KMeans` instance

    range_n_clusters : None or :obj:`list` of int, optional
        List of n_clusters for which to plot the explained variances.
        Defaults to ``[1, 3, 5, 7, 9, 11]``.

    n_jobs : int, optional
        Number of jobs to run in parallel. Defaults to 1.

    show_cluster_time : bool, optional
        Include plot of time it took to cluster for a particular K.

    ax : :class:`matplotlib.axes.Axes`, optional
        The axes upon which to plot the curve. If None, the plot is drawn
        on the current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot the Elbow Curve:

    .. plot:: ../examples/elbow_curve.py

    """
    pass

@modify_exceptions
def elbow_curve_from_results(n_clusters, sum_of_squares, times, ax=None):
    """
    Same as `elbow_curve`, but it takes the number of clusters and sum of
    squares as inputs. Useful if you want to train the models yourself.

    Examples
    --------

    Plot the Elbow Curve from the results:

    .. plot:: ../examples/elbow_curve_from_results.py

    """
    pass

def _clone_and_score_clusterer(clf, X, n_clusters):
    """Clones and scores a clustering model"""
    pass

@modify_exceptions
def silhouette_analysis(X, clf, range_n_clusters=None, metric='euclidean', figsize=None, cmap=None, text_fontsize='medium', ax=None):
    """Plots silhouette analysis of clusters provided.

    Parameters
    -----------

    X : array-like, shape = [n_samples, n_features]:
        Cluster data, where n_samples is the number of samples and
        n_features is the number of features.
        Refer https://numpy.org/doc/stable/glossary.html#term-array-like

    clf
        Clusterer instance that implements ``fit``,``fit_predict``, and
        ``score`` methods, and an ``n_clusters`` hyperparameter.
        e.g. :class:`sklearn.cluster.KMeans` instance

    range_n_clusters : None or :obj:`list` of int, optional
        List of n_clusters for which to plot the silhouette scores.
        Defaults to ``[2, 3, 4, 5, 6]``.

    metric : string or callable, optional:
        The metric to use when calculating distance between instances in
        a feature array. If metric is a string, it must be one of the
        options allowed by sklearn.metrics.pairwise.pairwise_distances.
        If X is the distance array itself, use "precomputed" as the metric.

    figsize : 2-tuple, optional:
        Tuple denoting figure size of the plot
        e.g. (6, 6). Defaults to ``None``.

    cmap : string or :class:`matplotlib.colors.Colormap` instance, optional:
        Colormap used for plotting the projection. View Matplotlib Colormap
        documentation for available options.
        https://matplotlib.org/users/colormaps.html

    text_fontsize : string or int, optional:
        Matplotlib-style fontsizes.
        Use e.g. "small", "medium", "large" or integer-values. Defaults to
        "medium".

    ax : :class:`matplotlib.axes.Axes`, optional:
        The axes upon which to plot the curve. If None, the plot is drawn on
        a new set of axes.

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot


    Examples
    --------

    Plot the Silhouette Analysis:

    .. plot:: ../examples/silhouette_plot_basic.py

    Notes
    -----
    .. versionadded:: 0.8.3

    """
    pass

@modify_exceptions
def _silhouette_analysis_one_model(X, cluster_labels, metric='euclidean', figsize=None, cmap=None, text_fontsize='medium', ax=None):
    """
    Generate silhouette plot for one value of n_cluster.
    """
    pass

@modify_exceptions
def silhouette_analysis_from_results(X, cluster_labels, metric='euclidean', figsize=None, cmap=None, text_fontsize='medium', ax=None):
    """
    Same as `silhouette_plot` but takes list of cluster_labels as input.
    Useful if you want to train the model yourself

    Examples
    --------

    Plot the Silhouette Analysis from the results:

    .. plot:: ../examples/silhouette_plot_from_results.py

    """
    pass
