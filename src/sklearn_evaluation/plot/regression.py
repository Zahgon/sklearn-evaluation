"""
Plotting functions for regression plots.

NOTE: Cook's distance is based on the yellowbricks regressor module. License below.

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
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import apply_theme, get_color_palette

def _set_ax_settings(ax, xlabel, ylabel, title):
    pass

def _check_parameter_validity(y_true, y_pred):
    pass

@modify_exceptions
def residuals(y_true, y_pred, ax=None):
    """
    Plot the residuals between measured and predicted values.

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Measured target values (ground truth).
    y_pred : array-like, shape = [n_samples]
        Predicted target values.
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot a Residuals Scatter plot:

    .. plot:: ../examples/residuals.py

    """
    pass

@modify_exceptions
def prediction_error(y_true, y_pred, ax=None):
    """
    Plot the scatter plot of measured values v. predicted values, with
    an identity line and a best fitted line to show the prediction
    difference.

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Measured target values (ground truth).
    y_pred : array-like, shape = [n_samples]
        Predicted target values.
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot a Prediction Error Scatter plot:

    .. plot:: ../examples/prediction_error.py

    """
    pass

@modify_exceptions
def cooks_distance(X, y, ax=None):
    """Plots cooks distance.

    Parameters
    ----------
    X : array-like, 2D
        Training data
        Refer https://numpy.org/doc/stable/glossary.html#term-array-like

    y : array-like, 1D
        Target data
        Refer https://numpy.org/doc/stable/glossary.html#term-array-like

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot a Cook's Distance Bar plot:

    .. plot:: ../examples/cooks_distance.py

    Notes
    -----
    .. versionadded:: 0.8.4
    """
    pass
