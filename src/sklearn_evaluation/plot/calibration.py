"""
Calibration curve

NOTE: this is largely based in the scikit-plot implementation. License below.

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
from sklearn.calibration import calibration_curve as sk_calibration_curve
from sklearn.utils import column_or_1d
from sklearn_evaluation import __version__
from sklearn_evaluation.util import isiterofiter
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.plot import AbstractComposedPlot, AbstractPlot
from sklearn_evaluation.plot.style import apply_theme, get_color_palette

def _set_ax_settings(ax, name):
    pass

@modify_exceptions
def _validate_metrics_input(mean_predicted_value, fraction_of_positives):
    pass

@modify_exceptions
def _validate_raw_data(probabilities, y_true, label):
    pass

def _plot_from_metrics(mpv, fop, label, color, ax):
    pass

def _generate_colors(cmap, n_color):
    pass

class CalibrationCurve(AbstractPlot):
    """
    Parameters
    ----------
    mean_predicted_value : ndarray of shape (n_bins,) or smaller
        The mean predicted probability in each bin.

    fraction_of_positives : ndarray of shape (n_bins,) or smaller
        The proportion of samples whose class is the positive class, in each
        bin.

    label : list of str, optional
            A list of strings, where each string refers to the name of the
            classifier that produced the corresponding probability estimates in
            `probabilities`. If ``None``, the names "Classifier 1", "Classifier 2",
            etc. will be used.

    cmap : string or :class:`matplotlib.colors.Colormap` instance, optional
            Colormap used for plotting the projection. View Matplotlib Colormap
            documentation for available options.
            https://matplotlib.org/users/colormaps.html

    Examples
    --------
    .. plot:: ../examples/calibration_curve_oop.py

    .. plot:: ../examples/calibration_curve_diff_sample_size.py

    .. plot:: ../examples/calibration_curve_add.py

    Notes
    -----
    .. versionadded:: 0.11.1
    """

    @modify_exceptions
    def __init__(self, mean_predicted_value, fraction_of_positives, label=None, cmap=None):
        self.mean_predicted_value = mean_predicted_value
        self.fraction_of_positives = fraction_of_positives
        self.label = label
        self.cmap = cmap

    def plot(self, ax=None):
        """Create the plot
        Parameters
        -----------
        ax : matplotlib.Axes
            An Axes object to add the plot to
        """
        pass

    @classmethod
    @modify_exceptions
    def from_raw_data(cls, y_true, probabilities, *, label=None, n_bins=10, cmap=None):
        """
        Plots calibration curves for a set of classifier probability estimates.
        Calibration curves help determining whether you can interpret predicted
        probabilities as confidence level. For example, if we take a
        well-calibrated and take the instances where the score is 0.8, 80% of those
        instanes should be from the positive class. This function only works for
        binary classifiers.

        Parameters
        ----------
        y_true : array-like, shape = [n_samples] or list with array-like:
            Ground truth (correct) target values. If passed a single array-
            object, it assumes all the `probabilities` have the same shape as
            `y_true`. If passed a list, it expects `y_true[i]` to have the same
            size as `probabilities[i]`
        probabilities : list of array-like, shape (n_samples, 2) or (n_samples,)
            A list containing the outputs of binary classifiers'
            :func:`predict_proba` method or :func:`decision_function` method.
        label : list of str, optional)
            A list of strings, where each string refers to the name of the
            classifier that produced the corresponding probability estimates in
            `probabilities`. If ``None``, the names "Classifier 1", "Classifier 2",
            etc. will be used.
        n_bins : int, optional, default=10
            Number of bins. A bigger number requires more data.
        cmap : string or :class:`matplotlib.colors.Colormap` instance, optional
            Colormap used for plotting the projection. View Matplotlib Colormap
            documentation for available options.
            https://matplotlib.org/users/colormaps.html
        """
        pass

    def __add__(self, another):
        return CalibrationCurveAdd(mean_predicted_value_list=[self.mean_predicted_value, another.mean_predicted_value], fraction_of_positives_list=[self.fraction_of_positives, another.fraction_of_positives], label_list=[self.label, another.label], cmaps=[self.cmap, another.cmap]).plot()

    @classmethod
    def _from_data(cls):
        pass

    def _get_data(self):
        pass

class CalibrationCurveAdd(AbstractComposedPlot):

    @modify_exceptions
    def __init__(self, mean_predicted_value_list, fraction_of_positives_list, label_list, cmaps=None):
        self.mean_predicted_value_list = mean_predicted_value_list
        self.fraction_of_positives_list = fraction_of_positives_list
        self.label_list = label_list
        self.cmaps = cmaps

    def plot(self, ax=None):
        """Generate a new plot with overlapping Calibration curves
        Parameters
        -----------
        ax : matplotlib.Axes
            An Axes object to add the plot to

        """
        pass

@modify_exceptions
def calibration_curve(y_true, probabilities, clf_names=None, n_bins=10, cmap='nipy_spectral', ax=None):
    """
    Plots calibration curves for a set of classifier probability estimates.
    Calibration curves help determining whether you can interpret predicted
    probabilities as confidence level. For example, if we take a
    well-calibrated and take the instances where the score is 0.8, 80% of those
    instanes should be from the positive class. This function only works for
    binary classifiers.

    Parameters
    ----------

    y_true : array-like, shape = [n_samples] or list with array-like:
        Ground truth (correct) target values. If passed a single array-
        object, it assumes all the `probabilities` have the same shape as
        `y_true`. If passed a list, it expects `y_true[i]` to have the same
        size as `probabilities[i]`
    probabilities : list of array-like, shape (n_samples, 2) or (n_samples,)
        A list containing the outputs of binary classifiers'
        :func:`predict_proba` method or :func:`decision_function` method.
    clf_names : list of str, optional)
        A list of strings, where each string refers to the name of the
        classifier that produced the corresponding probability estimates in
        `probabilities`. If ``None``, the names "Classifier 1", "Classifier 2",
        etc. will be used.
    n_bins : int, optional, default=10
        Number of bins. A bigger number requires more data.
    cmap : string or :class:`matplotlib.colors.Colormap` instance, optional
        Colormap used for plotting the projection. View Matplotlib Colormap
        documentation for available options.
        https://matplotlib.org/users/colormaps.html
    ax: matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------
    .. plot:: ../examples/calibration_curve.py
    """
    pass

@modify_exceptions
def scores_distribution(y_scores, n_bins=5, title='Predictions distribution', color=None, ax=None):
    """Generate a histogram from model's predictions

    Parameters
    ----------
    y_scores : array-like, shape=(n_samples, )
        Scores produced by a trained model for a single class
    n_bins : int, default=5
        Number of histogram bins
    title : title of the plot. Defaults to Predictions Distribution
    color : color of the histogram. Defaults to blue.
    ax: matplotlib Axes, default=None
        Axes object to draw the plot onto, otherwise uses current Axes
    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot
    Examples
    --------
    .. plot:: ../examples/scores_distribution.py
    """
    pass
