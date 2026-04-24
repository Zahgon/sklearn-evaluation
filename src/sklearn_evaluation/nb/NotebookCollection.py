from functools import partial
from difflib import HtmlDiff
import random
import string
import base64
import copy
from pathlib import Path
from collections.abc import Mapping
import black
import pandas as pd
from IPython.display import HTML, Image
from jinja2 import Environment, PackageLoader
from sklearn_evaluation.nb.NotebookIntrospector import NotebookIntrospector
from sklearn_evaluation.nb.sets import differences
from sklearn_evaluation.table import Table
_env = Environment(loader=PackageLoader('sklearn_evaluation', 'assets/nb'))
_fm = black.FileMode(string_normalization=False, line_length=40)
_htmldiff = HtmlDiff()

class NotebookCollection(Mapping):
    """Compare output from a collection of notebooks

    To access output, notebooks must tag the cells (one tag per cell). For
    instructions on tagging cells, `see this <https://papermill.readthedocs.io/en/latest/usage-parameterize.html>`_

    :doc:`Click here <../comparison/NotebookCollection>` to see the user guide.

    Parameters
    ----------
    paths : list
        Paths to notebooks to load

    ids : list or 'filenames', default=None
        List of ids (one per notebook), if None, paths are used as identifiers,
        if 'filenames', the file name is extracted from each path and used
        as identifier (ignores extension)
    """

    def __init__(self, paths, ids=None, scores=False):
        if ids is None:
            ids = paths
        elif ids == 'filenames':
            ids = [_get_filename(path) for path in paths]
        self.nbs = {id_: NotebookIntrospector(path, to_df=False) for id_, path in zip(ids, paths)}
        nb = list(self.nbs.values())[0]
        self._keys = list(nb.tag2output.keys())
        self._scores = scores

    def __getitem__(self, key):
        raw = [nb[key] for nb in self.nbs.values()]
        e, ids_out = add_compare_tab(raw, list(self.nbs.keys()), self._scores)
        mapping = {k: v for k, v in zip(ids_out, e)}
        html = tabs_html_from_content(ids_out, e)
        return HTMLMapping(mapping, html)

    def __iter__(self):
        for k in self._keys:
            yield k

    def _ipython_key_completions_(self):
        pass

    def __len__(self):
        return len(self._keys)

class HTMLMapping(Mapping):
    """A mapping that has an HTML representation

    Parameters
    ----------
    mapping : dict
        The mapping with the data

    HTML : str
        The HTML representation of the mapping
    """

    def __init__(self, mapping, html):
        self._mapping = mapping
        self._html = html

    def __getitem__(self, key):
        return self._mapping[key]

    def _ipython_key_completions_(self):
        pass

    def __iter__(self):
        for k in self._mapping:
            yield k

    def __len__(self):
        return len(self._mapping)

    def _repr_html_(self):
        pass

def _get_filename(path):
    pass

def add_compare_tab(elements, ids, scores_arg):
    """
    Processes tab contents and ids, adding a "Compare" tab if possible

    Parameters
    ----------
    elements
        The elements to compare

    ids : list
        The IDs for each element

    Returns
    -------
    out
        A new set of element to display. It might contain one new element in
        index 0 if we can provide a comparison view

    out_ids
        A new set of IDs. It might contain a new ID in index 0 if we can
        provide a comparison view
    """
    pass

def tabs_html_from_content(names, contents):
    """
    Generate the tabs and content to display as an HTML string
    """
    pass

def to_df(obj):
    """
    Converts pandas.DataFrame, if the object is already one, returns it.
    Otherwise it tried to convert it from a HTML table. Raises an error
    if more than one table is detected
    """
    pass

def process_columns(columns):
    """
    Helper function to parse column names from pandas.DataFrame objects
    parsed from HTML tables
    """
    pass

def process_multi_index_col(col):
    """
    Helper function to parse column names from pandas.DataFrame objects
    with  multi indexes parsed from HTML tables
    """
    pass

def color_neg_green(s):
    pass

def color_neg_red(s):
    pass

def color(s, which, color):
    """
    pandas.DataFrame function to add color to cell's text
    """
    pass
_color_map = {'error': {'max': partial(color, which='max', color='red'), 'min': partial(color, which='min', color='green')}, 'score': {'max': partial(color, which='max', color='green'), 'min': partial(color, which='min', color='red')}}

def is_in(elements, value):
    """
    Determines if a value is in a list. It also handles degenerate cases
    when instead of a list, elements is True, False  or None
    """
    pass

def split_errors_and_scores(axis, scores_arg, axis_second, transpose=False):
    """
    Determines which metrics are scores and which ones are metrics based on
    the "scores_arg". Returns a pd.IndexSlice object that can be used in
    pandas.DataFrame styling functions
    """
    pass

def compare_diff(mappings):
    """
    Generates an HTML object with a diff view of two mappings
    """
    pass

def compare_sets(sets, ids):
    """
    Generates a Table object with three columns comparing two sets: 1) elements
    in both sets, 2) elements in the first set and 3) elements in the second
    set. Raises an error if sets does not have two elements
    """
    pass

def compare_df(tables, ids, scores_arg):
    """
    Generates a comparison from a list of tables. Taables can be either a
    pandas.DataFrame or a str with an HTML table. The output depends
    on the number of tables and rows. Returns a pandas.DataFrame with style
    added (colors)
    """
    pass

def data2html_img(data):
    """Converts a png image (bytes) to HTML str with the image in base64"""
    pass

def to_html_str(content):
    """Returns an HTML string representation of the content"""
    pass
