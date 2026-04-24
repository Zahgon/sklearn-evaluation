"""
When training models, it is common to try out different
subsets of features or subpopulations. ``DataSelector`` allows you to define
a series of transformations on your data so you can succinctly define a
subsetting pipeline as a series of dictionaries.
"""
from copy import copy, deepcopy
import abc
import inspect
import importlib
import itertools
from collections.abc import Mapping
import pandas as pd
from decorator import decorator
from sklearn_evaluation.exceptions import DataSelectorError
from sklearn_evaluation.util import map_parameters_in_fn_call
from sklearn_evaluation.table import Table

def import_from_dotted_path(dotted_path):
    pass

def expand_value(value):
    """
    If value is a str with at least one dot ("."), try to import it and call
    it, if anything fails, return the value
    """
    pass

@decorator
def expand_arguments(func, *args, **kwargs):
    """
    Fnctions decorated with expand_argument call "expand_value" on each
    passed argument, which will interpred as a "dotted path" any string with
    dots on it and replace the value by the value returned by a function
    imported from that location (no arguments passed), if no function
    is found in such location, the original value is returned
    """
    pass

def concatenate_over(argname):
    """Decorator to "vectorize" functions and concatenate outputs"""
    pass

class Step(abc.ABC):

    @abc.abstractmethod
    def transform(self, df):
        pass

    def get_args(self):
        pass

    def get_params(self):
        pass

def _with_prefix(df, prefix):
    pass

def _with_suffix(df, suffix):
    pass

def _contains(df, substr):
    pass

def _with_max_na_prop(df, max_prop):
    pass

class ColumnDrop(Step):
    """Drop columns

    Parameters
    ----------
    names
        List of columns to drop
    prefix
        Drop columns with this prefix (or list of)
    suffix
        Drop columns with this suffix (or list of)
    contains
        Drop columns if they contains this substring
    max_na_prop
        Drop columns whose proportion of NAs [0, 1] is larger than this

    """

    @expand_arguments
    def __init__(self, names: list=None, prefix: str=None, suffix: str=None, contains: str=None, max_na_prop: float=None):
        self.names = names or []
        self.prefix = prefix
        self.suffix = suffix
        self.contains = contains
        self.max_na_prop = max_na_prop
        self.to_delete_ = None

    def transform(self, df, return_summary=False):
        pass

    def transform_summary(self, df):
        pass

def _incomplete_cases(df):
    pass

def _query(df, query):
    pass

class RowDrop(Step):
    """Drop rows

    Parameters
    ----------
    if_nas
        If True, deletes all rows where there is at leat one NA
    query
        Drops all rows matching the query (passed via pandas.query)
    """

    @expand_arguments
    def __init__(self, if_nas: bool=False, query: str=None):
        self.if_nas = if_nas
        self.query = query

    def transform(self, df, return_summary=False):
        pass

    def transform_summary(self, df, to_delete):
        pass

class ColumnKeep(Step):
    """Subset columns

    Parameters
    ----------
    names
        List of columns to keep
    """

    def __init__(self, names: list=None, dotted_path: str=None):
        self.names = names or []
        self.dotted_path = dotted_path

    def transform(self, df, return_summary=False):
        pass

    def transform_summary(self, to_keep):
        pass

class DataSelector:
    """Subset a pandas.DataFrame by passing a series of steps

    Parameters
    ----------
    *steps
        Steps to apply to the data sequentially (order matters). Each step
        must be a dictionary with a key "kind" whose value must be one of
        "column_drop", "row_drop" or "column_keep". The rest of the key-value
        pairs must match the signature for the corresponding Step objects

    """

    def __init__(self, *steps):
        steps = deepcopy(steps)
        self.steps = [_instantiate_step(step) for step in steps]

    def transform(self, df, return_summary: bool=False):
        """Apply steps

        Parameters
        ----------
        df
            Data frame to transform
        return_summary
            If False, the function only returns the output data frame,
            if True, it also returns a summary table
        """
        pass

    def _get_table(self):
        pass

    def __repr__(self):
        table = str(self._get_table())
        table = '{} with steps:\n'.format(type(self).__name__) + table
        return table

    def _repr_html_(self):
        pass

def _instantiate_step(step):
    pass
_mapping = {'column_drop': ColumnDrop, 'row_drop': RowDrop, 'column_keep': ColumnKeep}
