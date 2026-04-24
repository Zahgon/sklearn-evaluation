"""
Plotting 2 discrete parameters in a heatmap
"""

import numpy as np
from sklearn_evaluation.plot.util import set_default_ax
from sklearn_evaluation.plot.matplotlib.data_grid import DataGrid


@set_default_ax
def heatmap(
    records,
    ax=None,
    get_value=lambda data: data,
    get_text=lambda data: data,
    kwargs_text=dict(ha="center", va="center", color="w"),
):
    """ """
    pass
