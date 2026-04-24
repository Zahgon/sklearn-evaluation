import numpy as np
from sklearn_evaluation.metrics import compute_at_thresholds
from sklearn_evaluation.plot.util import set_default_ax
from ploomber_core.exceptions import modify_exceptions

@set_default_ax
@modify_exceptions
def metrics_at_thresholds(fn, y_true, y_score, n_thresholds=10, start=0.0, ax=None):
    """Plot metrics at increasing thresholds"""
    pass
