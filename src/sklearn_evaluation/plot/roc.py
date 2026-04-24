import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize, LabelBinarizer
from sklearn_evaluation.util import is_column_vector, is_row_vector, check_elements_in_range, is_binary, convert_array_to_string
from sklearn_evaluation import __version__
import json
from pathlib import Path
from sklearn_evaluation.plot.plot import AbstractPlot, AbstractComposedPlot
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import apply_theme

def _check_data_inputs(y_true, y_score) -> None:
    """
    Checks if data inputs are valid and supported for generating ROC with sklearn

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Correct target values (ground truth).

        e.g

        "classes" format : [0, 1, 2, 0, 1, ...]
        or ['virginica', 'versicolor', 'virginica', 'setosa', ...]

        one-hot encoded classes : [[0, 0, 1],
                                   [1, 0, 0]]

    y_score : array-like, shape = [n_samples] or [n_samples, 2] for binary
        classification or [n_samples, n_classes] for multiclass
        Target scores (estimator predictions).

        e.g

        "scores" format : [[0.1, 0.1, 0.8],
                           [0.7, 0.15, 0.15]]

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If any of the inputs is invalid

    """
    pass

def is_array_like_scores(array, min_allowed_length=None) -> bool:
    """
    Checks if array is in "scores" format

    Parameters
    ----------
    array : array-like, shape = [n_samples] or [n_samples, 2] for binary
        classification or [n_samples, n_classes] for multiclass
        Target scores (estimator predictions).

        e.g

        "scores" format : [[0.1, 0.1, 0.8],
                           [0.7, 0.15, 0.15]]

    min_allowed_length : int defaul=None
        define the minimum length of the array.
        If None accept any length.

    Returns
    -------
    is_scores_format bool

    """
    pass

def _get_number_of_elements(array):
    """
    Get the number of elements in array
    """
    pass

@modify_exceptions
def roc(y_true, y_score, ax=None):
    """Plot ROC curve

    Parameters
    ----------
    y_true : array-like, shape = [n_samples]
        Correct target values (ground truth).

        e.g

        "classes" format : [0, 1, 2, 0, 1, ...]
        or ['virginica', 'versicolor', 'virginica', 'setosa', ...]

        one-hot encoded classes : [[0, 0, 1],
                                   [1, 0, 0]]

    y_score : array-like, shape = [n_samples] or [n_samples, 2] for binary
        classification or [n_samples, n_classes] for multiclass
        Target scores (estimator predictions).

        e.g

        "scores" format : [[0.1, 0.1, 0.8],
                           [0.7, 0.15, 0.15]]

    ax: matplotlib Axes, default: None
        Axes object to draw the plot onto, otherwise uses current Axes

    Notes
    -----
    It is assumed that the y_score parameter columns are in order.
    For example, if ``y_true = [2, 2, 1, 0, 0, 1, 2]``, then the
    first column in y_score must contain the scores for class 0,
    second column for class 1 and so on.

    .. seealso:: :class:`ROC`

    Examples
    --------

    Plot a ROC Curve for binary classification:

    .. plot:: ../examples/roc.py

    """
    pass

def _set_custom_ax_settings(ax):
    pass

def _roc_curve_multi(y_true, y_score):
    """Compute micro-average ROC curve"""
    pass

def _plot_roc(fpr, tpr, ax, label=None, linestyle=None):
    """
    Plot ROC curve

    Parameters
    ----------
    fpr : ndarray of shape (>2,)
        Increasing false positive rates such that element i is the false
        positive rate of predictions with score >= `thresholds[i]`

    tpr : ndarray of shape (>2,)
        Increasing true positive rates such that element `i` is the true
        positive rate of predictions with score >= `thresholds[i]`

    ax: matplotlib Axes
        Axes object to draw the plot onto

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Notes
    -----
    .. versionadded:: 0.8.4
    """
    pass

def _generate_plot_from_fpr_tpr_lists(fpr, tpr, ax, label=None, linestyle=None):
    """
    Draws a plot for every list of values i.e tpr[i] and fpr[i].
    """
    pass

class ROCAdd(AbstractComposedPlot):
    """Generate a new plot with overlapping ROC curves (roc1 + roc2)

    Parameters
    ----------
    a : ROC
        ROC plot

    b : ROC
        ROC plot

    Examples
    --------

    .. plot:: ../../examples/roc_add.py

    Notes
    -----
    .. versionadded:: 0.8.4

    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plot(self, ax=None):
        pass

class ROC(AbstractPlot):
    """
    Plot ROC curve

    Parameters
    ----------
    fpr : ndarray of shape (>2,), list of lists or list of numbers
        Increasing false positive rates such that element i is the false
        positive rate of predictions with score >= `thresholds[i]`.

    tpr : ndarray of shape (>2,), list of lists or list of numbers
        Increasing true positive rates such that element `i` is the true
        positive rate of predictions with score >= `thresholds[i]`.

    label : list of str, default: None
        Set curve labels

    ax: matplotlib Axes, default: None
        Axes object to draw the plot onto, otherwise uses current Axes

    .. seealso:: :func:`roc`

    Examples
    --------

    Plot a ROC Curve for binary classification:

    .. plot:: ../examples/roc_binary_classification.py

    Compare ROC Curves of two binary classifiers:

    .. plot:: ../examples/roc_comparison.py

    Plot a ROC Curve for multi-class classification:

    .. plot:: ../examples/roc_multi_classification.py

    Notes
    -----
    .. versionadded:: 0.8.4
    """

    @modify_exceptions
    def __init__(self, fpr, tpr, label=None):
        if fpr is None or tpr is None:
            raise TypeError('fpr and tpr must be defined.')
        if type(fpr) is not type(tpr):
            raise TypeError(f'fpr and tpr must be the same type. Recevied: fpr {type(fpr)} != tpr {type(tpr)}')
        if len(fpr) == 0 or len(tpr) == 0:
            raise ValueError('fpr and tpr must not be empty')
        if not isinstance(fpr[0], (list, np.ndarray)):
            fpr = [fpr]
            tpr = [tpr]
        if len(fpr) != len(tpr):
            raise ValueError(f'fpr and tpr lengths should correspond. Recevied: fpr {len(fpr)} != tpr {len(tpr)}')
        for i in range(len(fpr)):
            fpr_ = fpr[i]
            tpr_ = tpr[i]
            if len(fpr_) != len(tpr_):
                raise ValueError(f'fpr and tpr lengths should correspond. Recevied: fpr {len(fpr_)} != tpr {len(tpr_)} at index {i}')
        self.fpr = fpr
        self.tpr = tpr
        self.label = label

    def __add__(self, other):
        roc_add_result = ROCAdd(self, other)
        roc_add_result.plot()
        return roc_add_result

    def _get_data(self):
        pass

    def plot(self, ax=None):
        pass

    @classmethod
    def from_dump(cls, path):
        pass

    @classmethod
    @modify_exceptions
    def from_raw_data(cls, y_true, y_score, ax=None):
        pass

    @staticmethod
    @modify_exceptions
    def _calculate_plotting_data(y_true, y_score):
        """
        Plot ROC curve
        Parameters
        ----------
        y_true : array-like, shape = [n_samples]
            Correct target values (ground truth).

        y_score : array-like, shape = [n_samples] or [n_samples, 2] for binary
            classification or [n_samples, n_classes] for multiclass
            Target scores (estimator predictions).

        Returns
        -------
        fpr : list of lists with fpr values

        tpr : list of lists with tpr values

        label : list of str for curves label
        """
        pass

def _preprocess_array_for_roc(array):
    """
    Binarize the array to use as valid input for plotting a
    single or a multi-class roc curve

    Note : This method in not in use but can be used in other plots
    where we don't require scores, but predictions (y_pred) i.e confusion_matrix,
    so if the user passes data in any of the three formats, we can convert it.

    Parameters
    ----------
    array : array-like, shape = [n_samples] or [n_samples, 2]
        The input array for the roc function
        array([0, 1, 2, 1, 0])
        array([[0, 0, 1],
               [1, 0, 0]])
        array([[0.1, 0.1, 0.8],
               [0.7, 0.15, 0.15]])
    Returns
    -------
    binarized_array : ndarray of shape (n_classes,)
        An input array that is valid for roc
    """
    pass
