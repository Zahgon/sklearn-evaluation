"""
Plot for target analysis

NOTE: this is based on the yellowbricks target analysis module. License below.

Copyright 2016-2020 The scikit-yb developers

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils.multiclass import unique_labels, type_of_target
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import get_color_palette, apply_theme

def _validate_target(y):
    """
    Raises a value error if the target is not a classification target.
    """
    pass

@modify_exceptions
def target_analysis(y_train, y_test=None, labels=None, colors=None, ax=None):
    """Target analysis plot for visualising class imbalance.

    There are two modes:

    1. Balance mode: if only y_train is specified
    2. Compare mode: if both train and test are specified

    In balance mode, the bar chart is displayed with each class as its own
    color. In compare mode, a side-by-side bar chart is displayed colored
    by train or test respectively.

    Parameters
    ----------
    y_train : array-like
        Array or list of shape (n,) that contains discrete data.
        Refer https://numpy.org/doc/stable/glossary.html#term-array-like
    y_test : array-like, optional
        Array or list of shape (m,) that contains discrete data. If
        specified, the bar chart will be drawn in compare mode.
        Refer https://numpy.org/doc/stable/glossary.html#term-array-like

    labels: list, optional
        A list of class names for the x-axis if the target is already encoded.
        Ensure that the labels are ordered lexicographically with respect to
        the values in the target. A common use case is to pass
        ``LabelEncoder.classes_`` as this parameter. If not specified, the labels
        in the data will be used.

    colors: list of strings
        Specify colors for the barchart.

    ax : :class:`matplotlib.axes.Axes`, optional
        The axes upon which to plot the curve. If None, the plot is drawn
        on the current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot the Target Analysis:

    .. plot:: ../examples/target_analysis.py

    Notes
    -----
    .. versionadded:: 0.8.3

    """
    pass
