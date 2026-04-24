"""
Plotting functions for classifier models
"""
import json
import random
import warnings
import numpy as np
import pandas as pd
from pathlib import Path
from itertools import product
from collections import defaultdict
from sklearn.metrics import confusion_matrix as sk_confusion_matrix
from sklearn_evaluation import __version__
from sklearn_evaluation.plot.plot import AbstractPlot
from ploomber_core.dependencies import requires
from ploomber_core.exceptions import modify_exceptions

def _confusion_matrix_validate_predictions(y_true, y_pred, target_names):
    """Validate input prediction data for a confusion matrix"""
    pass

def _validate_test_dataset(X_test, feature_names):
    pass

def _confusion_matrix(y_true, y_pred, normalize):
    pass

def _quadrant_wise_indices(y_true, y_pred):
    pass

def _is_long_number(num):
    pass

def _convert_to_scientific(data):
    pass

def _quadrant_interactive_data(X_test, quadrants, nsample):
    pass

def _data_by_column(data, columns):
    pass

def _cm_plot_data(cm, targets):
    pass

def _plot_cm_chart(df, selection, alt):
    pass

def _plot_sample_data_chart(df, selection, columns, alt):
    pass

def _plot_data_statistics_chart(df, selection, columns, alt):
    pass

class InteractiveConfusionMatrix(AbstractPlot):
    """
    Plot interactive confusion matrix.

    Notes
    -----
    .. versionadded:: 0.11.3
    """

    @modify_exceptions
    def __init__(self, cm, *, target_names=None, interactive_data=None):
        self.cm = cm
        self.target_names = target_names
        self.interactive_data = interactive_data

    @requires(['altair'])
    def plot(self):
        pass

    def __add__(self, another):
        raise NotImplementedError(f"{type(self).__name__!r} doesn't support the add (+) operator")

    def __sub__(self, another):
        raise NotImplementedError(f"{type(self).__name__!r} doesn't support the subtract (-) operator")

    def _get_data(self):
        pass

    @classmethod
    def from_dump(cls, path):
        pass

    @classmethod
    @modify_exceptions
    def from_raw_data(cls, y_true, y_pred, X_test=None, feature_names=None, feature_subset=None, nsample=5, target_names=None, normalize=False):
        """
        Plot confusion matrix.

        .. seealso:: :class:`ConfusionMatrix`

        Parameters
        ----------
        y_true : array-like, shape = [n_samples]
            Correct target values (ground truth).
        y_pred : array-like, shape = [n_samples]
            Target predicted classes (estimator predictions).
        X_test : array-like, shape = [n_samples, n_features], optional
                Defaults to None. If X_test is passed interactive data
                is displayed upon clicking on each quadrant of the
                confusion matrix.
        feature_names : list of feature names, optional
                feature_names can be passed if X_test passed is a numpy
                array. If not passed, feature names are generated like
                [Feature 0, Feature 1, .. , Feature N]
        feature_subset: list of features, optional
                subset of features to display in the tables. If not passed
                first 5 columns are selected.
        nsample : int, optional
                Defaults to 5. Number of sample observations to display in
                the interactive table if X_test is passed.
        target_names : list
            List containing the names of the target classes. List must be in order
            e.g. ``['Label for class 0', 'Label for class 1']``. If ``None``,
            generic labels will be generated e.g. ``['Class 0', 'Class 1']``
        normalize : bool
            Normalize the confusion matrix

        Examples
        --------

        :doc:`Click here <../classification/cm_interactive>` to see the user guide.

        """
        pass

    @classmethod
    def _from_data(cls, target_names, normalize, cm):
        pass
