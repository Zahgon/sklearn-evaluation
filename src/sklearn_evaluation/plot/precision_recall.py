import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import auc
from sklearn.metrics import precision_recall_curve
from sklearn.preprocessing import label_binarize
from sklearn_evaluation.util import is_column_vector, is_row_vector
from sklearn_evaluation.plot.plot import AbstractComposedPlot, AbstractPlot
from sklearn_evaluation import __version__
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import apply_theme
from warnings import warn
_default_label = 'Precision Recall Curve'

def _set_ax_settings(ax, name):
    pass

@modify_exceptions
def _validate_raw_input(y_true, y_score):
    pass

@modify_exceptions
def _validate_metrics_input(precision, recall):
    pass

def _precision_recall_metrics(y_true, y_score):
    pass

def _precision_recall_metrics_multiclass(y_true, y_score):
    pass

def _multiclass_metrics_from_raw(y_true, y_score, n_classes, label):
    pass

def _plot_metrics_multiclass(precision, recall, labels, ax):
    pass

def _plot_metrics_binary(precision, recall, label, ax):
    pass

def _generate_labels(n_classes):
    pass

class PrecisionRecall(AbstractPlot):
    """
    Plot precision recall curve.

    Parameters
    ----------
    precision : array-like, shape = [n_samples], when task is binary classification,
                or shape = [n_classes, n_samples], when task is multiclass
                classification.

    recall : array-like, shape = [n_samples], when task is binary classification.
             or shape = [n_classes, n_samples], when task is multiclass classification.

    label : string when task is binary classification, optional
            list of strings when task is multiclass classification
            this is used for labelling the curves. Defaults to precision recall.
            Make sure that the order of the labels corresponds to the order in
            which recall/precision arrays are passed to the constructor.

    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes

    Examples
    --------

    Plot a Precision-Recall Curve:

    .. plot:: ../examples/precision_recall_oop.py

    Compare Precision-Recall Curves of two classifiers:

    .. plot:: ../examples/precision_recall_add.py

    Notes
    -----
    .. versionadded:: 0.10.1
    """

    @modify_exceptions
    def __init__(self, precision, recall, label=None):
        self.precision = precision
        self.recall = recall
        self.label = label
        _validate_metrics_input(self.precision, self.recall)

    def plot(self, ax=None):
        """Create the plot
        Parameters
        -----------
        ax : matplotlib.Axes
            An Axes object to add the plot to
        """
        pass

    @classmethod
    def _from_data(cls):
        pass

    def __add__(self, another):
        return PrecisionRecallAdd(precisions=[self.precision, another.precision], recalls=[self.recall, another.recall], labels=[self.label, another.label]).plot()

    @classmethod
    @modify_exceptions
    def from_raw_data(cls, y_true, y_score, *, label=None):
        """
        Plot precision-recall curve from raw data.

        Parameters
        ----------
        y_true : array-like, shape = [n_samples]
            Correct target values (ground truth).
        y_score : array-like, shape = [n_samples] or [n_samples, 2] for binary
                  classification or [n_samples, n_classes] for multiclass
            Target scores (estimator predictions).
        label : string or list, optional
            labels for the curves

        Notes
        -----
        It is assumed that the y_score parameter columns are in order. For example,
        if ``y_true = [2, 2, 1, 0, 0, 1, 2]``, then the first column in y_score
        must contain the scores for class 0, second column for class 1 and so on.

        """
        pass

    def _get_data(self):
        pass

class PrecisionRecallAdd(AbstractComposedPlot):

    def __init__(self, precisions, recalls, labels) -> None:
        self.precisions = precisions
        self.recalls = recalls
        self.labels = labels

    def plot(self, ax=None):
        """
        Create the plot

        Parameters
        -----------
        ax : matplotlib.Axes
            An Axes object to add the plot to
        """
        pass

@modify_exceptions
def precision_recall(y_true, y_score, ax=None):
    """
    Plot precision-recall curve.

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Correct target values (ground truth).
    y_score : array-like, shape = [n_samples] or [n_samples, 2] for binary
              classification or [n_samples, n_classes] for multiclass
              Target scores (estimator predictions).
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes

    Notes
    -----
    It is assumed that the y_score parameter columns are in order. For example,
    if ``y_true = [2, 2, 1, 0, 0, 1, 2]``, then the first column in y_score
    must contain the scores for class 0, second column for class 1 and so on.

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot a Precision-Recall Curve for binary classification:

    .. plot:: ../examples/precision_recall.py

    Plot a Precision-Recall Curve for multi-class classification:

    .. plot:: ../examples/precision_recall_multiclass.py

    """
    pass
