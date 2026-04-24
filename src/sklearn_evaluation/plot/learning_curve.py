import numpy as np
import matplotlib.pyplot as plt
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import apply_theme

@modify_exceptions
def learning_curve(train_scores, test_scores, train_sizes, ax=None):
    """Plot a learning curve

    Plot a metric vs number of examples for the training and test set

    Parameters
    ----------
    train_scores : array-like
        Scores for the training set
    test_scores : array-like
        Scores for the test set
    train_sizes : array-like
        Relative or absolute numbers of training examples used to generate
        the learning curve
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot a Learning Curve:

    .. plot:: ../examples/learning_curve.py

    """
    pass
