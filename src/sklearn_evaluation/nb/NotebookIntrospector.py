import base64
from collections.abc import Mapping
import ast
import parso
import pandas as pd
import nbformat
from IPython.display import Image, HTML

def _safe_literal_eval(source, to_df=False, none_if_error=False):
    """
    Evaluates a literal, if the code cannot be parsed, it returns the original
    source as a string unless non_if_error is True, in such case it returns
    None
    """
    pass

def _do_nothing(source):
    pass

def _process_cell(cell):
    pass

def _process_output(output):
    pass

def _allowed_output(output):
    pass

def _filter_and_process_outputs(outputs):
    pass

def _parse_output(output, literal_eval, to_df, text_only):
    pass

def find_cell_with_tag(cells, tag):
    pass

def parse_injected_parameters_cell(cells):
    pass

def _process_stmt(stmt):
    pass

class NotebookIntrospector(Mapping):
    """Retrieve output from a notebook file with tagged cells.

    For instructions on tagging cells,
    `see this <https://papermill.readthedocs.io/en/latest/usage-parameterize.html>`_.

    Notes
    -----
    Ignores untagged cells, if a cell has more than one tag, it uses the first
    one as identifier. If a cell has more than one output, it uses the last
    one and discards the rest.
    """

    def __init__(self, path, literal_eval=True, to_df=False):
        self.nb = nbformat.read(path, nbformat.NO_CONVERT)
        self.tag2output_raw = self._tag2output()
        self.literal_eval = literal_eval
        self.tag2output = {k: _parse_output(v, literal_eval=literal_eval, to_df=to_df, text_only=False) for k, v in self.tag2output_raw.items()}

    def _tag2output(self):
        pass

    def __getitem__(self, key):
        return self.tag2output[key]

    def __iter__(self):
        for k in self.tag2output:
            yield k

    def __len__(self):
        return len(self.tag2output)

    def __repr__(self):
        return '{} with {}'.format(type(self).__name__, set(self.tag2output))

    def _ipython_key_completions_(self):
        pass

    def to_json_serializable(self):
        pass

    def get_injected_parameters(self):
        pass
