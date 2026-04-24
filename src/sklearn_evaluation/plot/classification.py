"""
Plotting functions for classifier models
"""
import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix as sk_confusion_matrix
from sklearn_evaluation import __version__
from sklearn_evaluation.plot.matplotlib import bar
from sklearn_evaluation.metrics import precision_at
from sklearn_evaluation import compute
from sklearn_evaluation.util import is_column_vector, is_row_vector
from sklearn_evaluation.plot.plot import AbstractPlot, AbstractComposedPlot
from sklearn_evaluation.plot import _matrix
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import default_cmap

class ConfusionMatrixSub(AbstractComposedPlot):
    """A composed plot to compare the difference between two confusion matrices"""

    def __init__(self, cm, target_names) -> None:
        self.cm = cm
        self.target_names = target_names

    def plot(self, ax=None):
        pass

class ConfusionMatrixAdd(AbstractComposedPlot):
    """A composed plot to compare two confusion matrices"""

    def __init__(self, a, b, target_names) -> None:
        self.a = a
        self.b = b
        self.target_names = target_names

    def plot(self, ax=None):
        pass

class ConfusionMatrix(AbstractPlot):
    """
    Plot confusion matrix.

    .. seealso:: :func:`confusion_matrix`

    Examples
    --------

    Plot and Compare Confusion Matrix for multiple classifiers:

    .. plot:: ../examples/confusion_matrix_oop.py

    Notes
    -----
    .. versionchanged:: 0.9
        Added ``cmap`` argument
    """

    @modify_exceptions
    def __init__(self, cm, *, target_names=None, normalize=False, cmap=None):
        self.cm = cm
        self.target_names = target_names
        self.normalize = normalize
        self.cmap = _confusion_matrix_init_defaults(cmap=cmap)

    def plot(self, ax=None):
        pass

    def __sub__(self, other):
        cm = self.cm - other.cm
        obj = ConfusionMatrixSub(cm, self.target_names)
        obj.plot()
        return obj

    def __add__(self, other):
        obj = ConfusionMatrixAdd(self.cm, other.cm, self.target_names)
        obj.plot()
        return obj

    def _get_data(self):
        pass

    @classmethod
    def from_dump(cls, path):
        pass

    @classmethod
    @modify_exceptions
    def from_raw_data(cls, y_true, y_pred, target_names=None, normalize=False, cmap=None):
        """

        Notes
        -----
        .. versionchanged:: 0.9
            Added ``cmap`` argument.
        """
        pass

    @classmethod
    def _from_data(cls, target_names, normalize, cm):
        pass

def _confusion_matrix(y_true, y_pred, normalize):
    pass

@modify_exceptions
def confusion_matrix(y_true, y_pred, target_names=None, normalize=False, cmap=None, ax=None):
    """
    Plot confusion matrix.

    .. seealso:: :class:`ConfusionMatrix`

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Correct target values (ground truth).
    y_pred : array-like, shape = [n_samples]
        Target predicted classes (estimator predictions).
    target_names : list
        List containing the names of the target classes. List must be in order
        e.g. ``['Label for class 0', 'Label for class 1']``. If ``None``,
        generic labels will be generated e.g. ``['Class 0', 'Class 1']``
    ax: matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes
    normalize : bool
        Normalize the confusion matrix
    cmap : matplotlib Colormap
        If ``None`` uses a modified version of matplotlib's OrRd colormap.


    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot a Confusion Matrix for binary classifier:

    .. plot:: ../examples/confusion_matrix.py

    """
    pass

def _confusion_matrix_validate_predictions(y_true, y_pred, target_names):
    """Validate input prediction data for a confusion matrix"""
    pass

def _confusion_matrix_init_defaults(cmap):
    """Initialize default values for confusion matrix"""
    pass

def _confusion_matrix_validate(y_true, y_pred, target_names, cmap):
    """Validate values for confusion matrix and initialize defaults"""
    pass

def _add_values_to_matrix(m, ax):
    pass

def _plot_cm(cm, cmap, ax, target_names, normalize):
    """Adds confusion matrix graphical elements to a ``matplotlib.Axes`` object"""
    pass

@modify_exceptions
def feature_importances(data, top_n=None, feature_names=None, orientation='horizontal', ax=None):
    """
    Get and order feature importances from a scikit-learn model
    or from an array-like structure. If data is a scikit-learn model with
    sub-estimators (e.g. RandomForest, AdaBoost) the function will compute the
    standard deviation of each feature.

    Parameters
    ----------
    data : sklearn model or array-like structure
        Object to get the data from.
    top_n : int
        Only get results for the top_n features.
    feature_names : array-like
        Feature names
    orientation: ('horizontal', 'vertical')
        Bar plot orientation
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot Feature Importances:

    .. plot:: ../examples/feature_importances.py

    """
    pass

@modify_exceptions
def precision_at_proportions(y_true, y_score, ax=None):
    """
    Plot precision values at different proportions.

    Parameters
    ----------
    y_true : array-like
        Correct target values (ground truth).
    y_score : array-like
        Target scores (estimator predictions).
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    """
    pass
