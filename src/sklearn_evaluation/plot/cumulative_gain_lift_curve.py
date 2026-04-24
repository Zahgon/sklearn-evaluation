"""
Plots for cumulative gain and lift curve

NOTE: this is largely based in the scikit-plot metrics module. License below.

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
import numpy as np
import matplotlib.pyplot as plt
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import apply_theme

def _cumulative_gain_curve(y_true, y_score, pos_label=None):
    """This function generates the points necessary to plot the Cumulative Gain
    Note: This implementation is restricted to the binary classification task.
    Parameters
    ----------
    y_true (array-like, shape (n_samples)): True labels of the data.

    y_score (array-like, shape (n_samples)): Target scores, can either be
            probability estimates of the positive class, confidence values, or
            non-thresholded measure of decisions (as returned by
            decision_function on some classifiers).

    pos_label (int or str, default=None): Label considered as positive and
            others are considered negative

    Returns
    ----------
    percentages (numpy.ndarray): An array containing the X-axis values for
        plotting the Cumulative Gains chart.
    gains (numpy.ndarray): An array containing the Y-axis values for one
        curve of the Cumulative Gains chart.

    Raises
    ----------
    ValueError: If `y_true` is not composed of 2 classes. The Cumulative
        Gain Chart is only relevant in binary classification.
    """
    pass

@modify_exceptions
def cumulative_gain(y_true, y_score, figsize=None, title_fontsize='large', text_fontsize='medium', ax=None):
    """
    Generates the Cumulative Gains Plot from labels and scores/probabilities
    The cumulative gains chart is used to determine the effectiveness of a
    binary classifier. The implementation here works only for binary classification.

    Parameters
    ----------
    y_true : array-like, shape=[n_samples,]
        Ground truth (correct) target values.
        Refer: https://numpy.org/doc/stable/glossary.html#term-array-like

    y_score : array-like, shape=[n_samples, n_classes]
        Prediction probabilities for each class returned by a classifier.
        Refer: https://numpy.org/doc/stable/glossary.html#term-array-like

    figsize :2-tuple, optional
        Tuple denoting figure size of the plot e.g. (6, 6). Defaults to ``None``.

    title_fontsize : string or int, optional
        Matplotlib-style fontsizes. Use e.g. "small", "medium", "large" or
        integer-values. Defaults to "large".

    text_fontsize : string or int, optional
        Matplotlib-style fontsizes. Use e.g. "small", "medium",
        "large" or integer-values. Defaults to "medium".

    ax : matplotlib Axes, optional
        Axes object to draw the plot onto, otherwise uses current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot the Cumulative Gains of a binary classifier:

    .. plot:: ../examples/cumulative_gain.py

    Notes
    -----
    .. versionadded:: 0.8.4
    """
    pass

@modify_exceptions
def lift_curve(y_true, y_score, ax=None, figsize=None, title_fontsize='large', text_fontsize='medium'):
    """Generates the Lift Curve from labels and scores/probabilities
    The lift curve is used to determine the effectiveness of a
    binary classifier. A detailed explanation can be found at
    http://www2.cs.uregina.ca/~dbd/cs831/notes/lift_chart/lift_chart.html.
    The implementation here works only for binary classification.

    Parameters
    ----------
    y_true : array-like, shape=[n_samples,]
        Ground truth (correct) target values.
        Refer: https://numpy.org/doc/stable/glossary.html#term-array-like

    y_score : array-like, shape=[n_samples, n_classes]
        Prediction probabilities for each class returned by a classifier.
        Refer: https://numpy.org/doc/stable/glossary.html#term-array-like

    figsize :2-tuple, optional
        Tuple denoting figure size of the plot e.g. (6, 6). Defaults to ``None``.

    title_fontsize : string or int, optional
        Matplotlib-style fontsizes. Use e.g. "small", "medium", "large" or
        integer-values. Defaults to "large".

    text_fontsize : string or int, optional
        Matplotlib-style fontsizes. Use e.g. "small", "medium",
        "large" or integer-values. Defaults to "medium".

    ax : matplotlib Axes, optional
        Axes object to draw the plot onto, otherwise uses current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot the Lift Curve for a binary classifier:

    .. plot:: ../examples/lift_curve.py

    Notes
    -----
    .. versionadded:: 0.8.4

    """
    pass
