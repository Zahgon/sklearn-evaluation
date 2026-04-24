import numpy as np
import matplotlib.pyplot as plt
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import apply_theme

@modify_exceptions
def validation_curve(train_scores, test_scores, param_range, param_name=None, semilogx=False, ax=None):
    """Plot a validation curve

    Plot a metric vs hyperparameter values for the training and test set

    Parameters
    ----------
    train_scores : array-like
        Scores for the training set
    test_scores : array-like
        Scores for the test set
    param_range : array-like
        Hyperparameter values used to generate the curve
    param_range : str
        Hyperparameter name
    semilgo : bool
        Sets a log scale on the x axis
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot a Validation Curve:

    .. plot:: ../examples/validation_curve.py

    """
    pass
