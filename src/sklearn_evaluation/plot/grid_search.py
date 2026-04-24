"""
Functions for visualizing grid search results
"""
import collections
import matplotlib.pyplot as plt
import numpy as np
from six import string_types
from sklearn_evaluation.plot.matplotlib.bar import BarShifter
from ploomber_core.exceptions import modify_exceptions
from sklearn_evaluation.plot.style import apply_theme
from ploomber_core import validate
from sklearn_evaluation.util import _group_by, _get_params_value, _mapping_to_tuple_pairs, _sorted_map_iter, _flatten_list

def _validate_change_input(change, valid):
    pass

def _validate_kind_input(kind, valid):
    pass

@modify_exceptions
def grid_search(cv_results_, change, subset=None, kind='line', cmap=None, ax=None, sort=True):
    """
    Plot results from a sklearn grid search by changing two parameters at most.

    Parameters
    ----------
    cv_results_ : list of named tuples
        Results from a sklearn grid search (get them using the
        `cv_results_` parameter)
    change : str or iterable with len<=2
        Parameter to change
    subset : dictionary-like
        parameter-value(s) pairs to subset from grid_scores.
        (e.g. ``{'n_estimators': [1, 10]}``), if None all combinations will be
        used.
    kind : ['line', 'bar']
        This only applies whe change is a single parameter. Changes the
        type of plot
    cmap : matplotlib Colormap
        This only applies when change are two parameters. Colormap used for
        the matrix. If None uses a modified version of matplotlib's OrRd
        colormap.
    ax: matplotlib Axes
        Axes object to draw the plot onto, otherwise uses current Axes
    sort: bool
        If True sorts the results in alphabetical order.

    Returns
    -------
    ax: matplotlib Axes
        Axes containing the plot

    Examples
    --------

    Plot the results of grid search:

    .. plot:: ../examples/grid_search.py

    """
    pass

def _grid_search_single(grid_scores, change, subset, kind, ax, sort, params):
    pass

def _grid_search_double(grid_scores, change, subset, cmap, ax, sort):
    pass
