import numpy as np
from sklearn.metrics import precision_score
from sklearn_evaluation.preprocessing import binarize
from sklearn_evaluation import util
from sklearn_evaluation import validate

def compute_at_thresholds(fn, y_true, y_score, n_thresholds=10, start=0.0):
    """
    Given scores, binarize them at different thresholds, then compute
    metrics

    Examples
    --------
    >>> from sklearn_evaluation.metrics import compute_at_thresholds
    >>> from sklearn.metrics import accuracy_score
    >>> from sklearn.metrics import precision_score, recall_score, f1_score
    >>> import numpy as np
    >>> y_true = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
    >>> y_score = np.array([1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1])
    >>> binarized = compute_at_thresholds([accuracy_score, precision_score,
    ...                                    recall_score, f1_score],
    ...                                    y_true, y_score)
    """
    pass

def confusion_matrix(y_true, y_pred, normalize):
    pass

def precision_at(y_true, y_score, top_proportion, ignore_nas=False):
    """
    Calculates precision at a given proportion.
    Only supports binary classification.
    """
    pass

def __precision(y_true, y_pred):
    """
    Precision metric tolerant to unlabeled data in y_true,
    NA values are ignored for the precision calculation
    """
    pass

def tp_at(y_true, y_score, top_proportion):
    pass

def fp_at(y_true, y_score, top_proportion):
    pass

def tn_at(y_true, y_score, top_proportion):
    pass

def fn_at(y_true, y_score, top_proportion):
    pass

def labels_at(y_true, y_score, top_proportion, normalize=False):
    """
    Return the number of labels encountered in the top  X proportion
    """
    pass
