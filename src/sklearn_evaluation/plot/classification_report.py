from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report as sk_classification_report
from sklearn_evaluation.plot.classification import _add_values_to_matrix
from sklearn_evaluation.plot.plot import AbstractPlot, AbstractComposedPlot
from sklearn_evaluation.plot import _matrix
from sklearn_evaluation import __version__
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import apply_theme

def _classification_report_add(first, second, keys, target_names, ax):
    pass

class ClassificationReportSub(AbstractComposedPlot):

    def __init__(self, matrix, matrix_another, keys, target_names) -> None:
        self.matrix = matrix
        self.matrix_another = matrix_another
        self.keys = keys
        self.target_names = target_names

    def plot(self, ax=None):
        pass

class ClassificationReportAdd(AbstractComposedPlot):

    def __init__(self, matrix, matrix_another, keys, target_names) -> None:
        self.matrix = matrix
        self.matrix_another = matrix_another
        self.keys = keys
        self.target_names = target_names

    def plot(self, ax=None):
        pass

class ClassificationReport(AbstractPlot):
    """
    .. seealso:: :func:`classification_report`

    Examples
    --------

    Plot a Classification Report:

    .. plot:: ../examples/ClassificationReport.py

    """

    def __init__(self, matrix, keys, *, target_names=None):
        self.matrix = matrix
        self.keys = keys
        self.target_names = target_names

    def plot(self, ax=None):
        pass

    def __sub__(self, other):
        return ClassificationReportSub(self.matrix, other.matrix, self.keys, target_names=self.target_names).plot()

    def __add__(self, other):
        return ClassificationReportAdd(self.matrix, other.matrix, keys=self.keys, target_names=self.target_names).plot()

    def _get_data(self):
        pass

    @classmethod
    def from_dump(cls, path):
        pass

    @classmethod
    @modify_exceptions
    def from_raw_data(cls, y_true, y_pred, *, target_names=None, sample_weight=None, zero_division=0):
        pass

    @classmethod
    def _from_data(cls, target_names, matrix, keys):
        pass

def _classification_report(y_true, y_pred, *, target_names=None, sample_weight=None, zero_division=0):
    pass

def _classification_report_plot(matrix, keys, target_names, ax):
    pass

@modify_exceptions
def classification_report(y_true, y_pred, *, target_names=None, sample_weight=None, zero_division=0, ax=None):
    """Classification report

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Correct target values (ground truth)

    y_pred : array-like, shape = [n_samples]
        Target predicted classes (estimator predictions)

    target_names : list
        List containing the names of the target classes. List must be in order
        e.g. ``['Label for class 0', 'Label for class 1']``. If ``None``,
        generic labels will be generated e.g. ``['Class 0', 'Class 1']``

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    zero_division : bool,  0 or 1
        Sets the value to return when there is a zero division.

    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot


    .. seealso:: :class:`ClassificationReport`


    Examples
    --------

    Plot a Classification Report for binary classification:

    .. plot:: ../examples/classification_report.py

    Plot a Classification Report for multi-class classification:

    .. plot:: ../examples/classification_report_multiclass.py

    """
    pass
