from collections.abc import Mapping
from uuid import uuid4
import sqlite3
import json
import importlib
import pandas as pd
from jinja2 import Template
from sklearn_evaluation.table import Table
from sklearn_evaluation.report.serialize import try_serialize_figures, figure2html
from sklearn_evaluation.nb.NotebookCollection import add_compare_tab, tabs_html_from_content, HTMLMapping
from sklearn_evaluation import plot
from sklearn_evaluation.plot.util import no_display_plots
minor = sqlite3.sqlite_version.split('.')[1]
ARROW_OPERATOR_SUPPORTED = int(minor) >= 38
TEMPLATE_ARROW = "SELECT\n    uuid,\n    {% for p, alias in keys -%}\n    parameters ->> '{{p}}' as {{alias}}{% if not loop.last %},{% endif %}\n    {% endfor -%}\nFROM experiments\nLIMIT 10\n"
TEMPLATE_JSON_EXTRACT = "SELECT\n    uuid,\n    {% for p, alias in keys -%}\n    json_extract(parameters, '$.{{p}}') as {{alias}}{% if not loop.last %},{% endif %}\n    {% endfor -%}\nFROM experiments\nLIMIT 10\n"

class Experiment:
    """An experiment instance used to log values"""

    def __init__(self, tracker, uuid, data) -> None:
        self._tracker = tracker
        self._uuid = uuid
        self._data = data

    @classmethod
    def new(cls, tracker):
        pass

    @property
    def uuid(self):
        pass

    def log_confusion_matrix(self, y_true, y_pred, target_names=None, normalize=False):
        """Log a confusion matrix

        Examples
        --------
        >>> from sklearn_evaluation import SQLiteTracker
        >>> tracker = SQLiteTracker("experiments.db")
        >>> exp = tracker.new_experiment()
        >>> exp.log_confusion_matrix([1, 1, 0, 0], [1, 0, 1, 0]) # doctest: +SKIP
        >>> data = tracker.get(exp.uuid)
        >>> data['confusion_matrix'] # doctest: +SKIP
        """
        pass

    def log_classification_report(self, y_true, y_pred, *, target_names=None, sample_weight=None, zero_division=0):
        """Log classification report

        Examples
        --------
        >>> from sklearn_evaluation import SQLiteTracker
        >>> tracker = SQLiteTracker("experiments.db")
        >>> exp = tracker.new_experiment()
        >>> exp.log_classification_report([1, 1, 0, 0], [1, 0, 1, 0]) # doctest: +SKIP
        >>> data = tracker.get(exp.uuid)
        >>> data['classification_report'] # doctest: +SKIP
        """
        pass

    def log(self, key, obj):
        """Log a value. Any JSON-serializable object works

        Examples
        --------
        >>> from sklearn_evaluation import SQLiteTracker
        >>> tracker = SQLiteTracker("experiments.db")
        >>> exp = tracker.new_experiment()
        >>> exp.log("accuracy", 0.8)
        0.8
        >>> data = tracker.get(exp.uuid)
        >>> data['accuracy']
        0.8
        """
        pass

    def log_dict(self, obj):
        """Log a dictionary with values

        Examples
        --------
        >>> from sklearn_evaluation import SQLiteTracker
        >>> tracker = SQLiteTracker("experiments.db")
        >>> exp = tracker.new_experiment()
        >>> exp.log_dict({"precision": 0.9, "recall": 0.7})
        {'precision': 0.9, 'recall': 0.7}
        >>> data = tracker.get(exp.uuid)
        >>> data['precision']
        0.9
        >>> data['recall']
        0.7
        """
        pass

    def log_figure(self, key, fig):
        """Log a matplotlib figure

        >>> import matplotlib.pyplot as plt
        >>> from sklearn_evaluation import SQLiteTracker
        >>> tracker = SQLiteTracker("experiments.db")
        >>> fig, ax = plt.subplots()
        >>> ax.scatter([1, 2, 3], [1, 2, 3]) # doctest: +SKIP
        >>> exp = tracker.new_experiment()
        >>> exp.log_figure("scatter", fig)
        >>> data = tracker.get(exp.uuid)
        >>> data['scatter'] # doctest: +SKIP
        """
        pass

    def comment(self, comment):
        """Add a comment to an experiment

        Examples
        --------
        >>> from sklearn_evaluation import SQLiteTracker
        >>> tracker = SQLiteTracker("experiments.db")
        >>> exp = tracker.new_experiment()
        >>> exp.comment("some comment") # add comment at runtime
        >>> retrieved = tracker.get(exp.uuid)
        >>> retrieved.comment("another commment")
        """
        pass

    def __repr__(self) -> str:
        class_ = type(self).__name__
        data = self._data
        return f'{class_}({data!r})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, type(self)):
            other = other._data
        return self._data == other

    def __getitem__(self, key):
        return self._data[key]

class SQLiteTracker:
    """A experiment tracker backed by a SQLite database

    :doc:`Click here <../comparison/SQLiteTracker>` to see the user guide.

    Parameters
    ----------
    path
        Database location

    Examples
    --------
    >>> from sklearn_evaluation import SQLiteTracker
    >>> tracker = SQLiteTracker("experiments.db")
    >>> experiment = tracker.new_experiment() # new experiment
    >>> experiment.log("accuracy", 0.8) # log metric
    0.8
    >>> tracker.get(experiment.uuid) # retrieve it later with the uuid
    Experiment({'accuracy': 0.8})
    >>> experiment.log_confusion_matrix([1, 1, 0, 0], [1, 0, 1, 0]) # doctest: +SKIP
    >>> data = tracker.get(experiment.uuid)
    >>> data['confusion_matrix'] # doctest: +SKIP

    """

    def __init__(self, path: str):
        self.conn = sqlite3.connect(path)
        cur = self.conn.cursor()
        cur.execute('\n        CREATE TABLE IF NOT EXISTS experiments (\n            uuid TEXT NOT NULL UNIQUE,\n            created TIMESTAMP default current_timestamp,\n            parameters TEXT,\n            comment TEXT\n        )\n        ')
        cur.close()

    def __getitem__(self, uuid):
        """Get experiment with a given uuid"""
        return pd.read_sql('SELECT * FROM experiments WHERE uuid = ?', self.conn, params=[uuid], index_col='uuid')

    def recent(self, n=5, normalize=False):
        """Get most recent experiments as a pandas.DataFrame"""
        pass

    def query(self, code, as_frame=True, render_plots=False):
        """Query the database

        Parameters
        ----------
        code : str
            The SQL query to execute

        as_frame : bool, default=True
            If True, it'll return the results of your query in a
            pandas.DataFrame, otherwise it'll return a Results object.
            The Results object can render HTML stored in the database but
            cannot be filtered or manipulated like a pandas.DataFrame

        render_plots: bool, default=False
            Whether to render plots in the results or not. Only valid when
            as_frame=False

        Examples
        --------
        >>> from sklearn_evaluation import SQLiteTracker
        >>> tracker = SQLiteTracker('experiments.db')
        >>> exp1 = tracker.new_experiment()
        >>> exp1.log("accuracy", 0.8) # doctest: +SKIP
        >>> exp1.log_confusion_matrix([1, 1, 0, 0], [1, 0, 1, 0]) # doctest: +SKIP
        >>> exp2 = tracker.new_experiment()
        >>> exp2.log("accuracy", 1.0) # doctest: +SKIP
        >>> exp2.log_confusion_matrix([1, 1, 0, 0], [1, 1, 0, 0]) # doctest: +SKIP

        >>> df = tracker.query('''
        ... SELECT uuid,
        ...        json_extract(parameters, '$.accuracy') AS accuracy,
        ...        json_extract(parameters, '$.confusion_matrix') AS cm
        ... FROM experiments
        ... ''', as_frame=True)


        >>> results = tracker.query('''
        ... SELECT uuid,
        ...        json_extract(parameters, '$.accuracy') AS accuracy,
        ...        json_extract(parameters, '$.confusion_matrix') AS cm
        ... FROM experiments
        ... ''', as_frame=False, render_plots=True)
        """
        pass

    def new(self):
        """Create a new experiment, returns a uuid"""
        pass

    def new_experiment(self):
        """Returns an experiment instance"""
        pass

    def update(self, uuid, parameters, allow_overwrite=False):
        """Update the parameters of a experiment given its uuid"""
        pass

    def upsert(self, uuid, parameters):
        """Modify the stored parameters of an existing experiment"""
        pass

    def upsert_append(self, uuid, parameters):
        """Append the parameters to an existing experiment

        Examples
        --------
        >>> from sklearn_evaluation import SQLiteTracker
        >>> tracker = SQLiteTracker('experiments.db')
        >>> exp = tracker.new_experiment()

        >>> #Log initial metric_a values for the experiment
        >>> exp.log("metric_a", [0.8, 0.85]) # doctest: +SKIP
        metric_a: [0.8, 0.85]

        >>> #Append new "metric_a" values and adding "metric_b" values
        >>> tracker.upsert_append(
        ...        exp.uuid,
        ...        dict(
        ...            metric_a=0.9,
        ...            metric_b=[0.4, 0.2],)
        ... )

        metric_a: [0.8, 0.85, 0.9]
        metric_b: [0.4, 0.2]
        """
        pass

    def insert(self, uuid, parameters):
        """Insert a new experiment"""
        pass

    def insert_many(self, parameters_all):
        """Insert many experiments at once"""
        pass

    def comment(self, uuid, comment):
        """Add a comment to an experiment given its uuid"""
        pass

    def _recent(self, n=5, fmt='html'):
        pass

    def _can_update(self, uuid):
        """Check if an experiment with a given uuid can be updated"""
        pass

    def get_parameters_keys(self, limit=100):
        """
        Return the keys in the parameters column by randomly sampling records
        and obtaining the keys of the JSON objects
        """
        pass

    def get_sample_query(self, compatibility_mode=True):
        pass

    def get(self, uuid, unserialize_plots=True):
        """Get an experiment given its UUID

        Examples
        --------
        >>> from sklearn_evaluation import SQLiteTracker
        >>> tracker = SQLiteTracker("experiments.db")
        >>> experiment = tracker.new_experiment() # new experiment
        >>> experiment.log("accuracy", 0.8) # log metric
        0.8
        >>> experiment = tracker.get(experiment.uuid) # retrieve it with the uuid
        >>> experiment
        Experiment({'accuracy': 0.8})
        >>> experiment.comment("best model")
        """
        pass

    def __repr__(self):
        return self._recent(fmt='plain')

    def _repr_html_(self):
        pass

    def __del__(self):
        self.conn.close()

    def __len__(self):
        cur = self.conn.execute('\n        SELECT COUNT(*)\n        FROM experiments\n        ')
        return cur.fetchone()[0]

def is_str(obj):
    pass

def is_float(obj):
    pass

def json_loads(obj):
    pass

def is_plot(obj):
    pass

def unserialize_plot(obj, return_instance=False):
    pass

def _to_html(instance):
    pass

class GenericPlot:

    def __init__(self, html):
        self._html = html

    def _repr_html_(self):
        pass

def unserialize_if_plot(obj, return_instance=False):
    pass

class Results:
    """An object to generate an HTML table from a SQLite result"""

    def __init__(self, columns, rows, render_plots):
        self.columns = columns
        self.rows = rows
        self.render_plots = render_plots

    def _repr_html_(self):
        pass

    def __getitem__(self, key):
        if key not in self.columns:
            raise KeyError(f'{key} does not appear in the results')
        idx = self.columns.index(key)
        rows = [[row[idx]] for row in self.rows]
        return Results(columns=[key], rows=rows, render_plots=self.render_plots)

    def get(self, key, index_by=None):
        """Get a single column of the results

        Examples
        --------
        >>> from sklearn_evaluation import SQLiteTracker
        >>> tracker = SQLiteTracker("experiments.db")
        >>> exp1 = tracker.new_experiment()
        >>> exp1.log("accuracy", 0.8) # doctest: +SKIP
        >>> exp1.log_confusion_matrix([1, 1, 0, 0], [1, 0, 1, 0]) # doctest: +SKIP
        >>> exp2 = tracker.new_experiment()
        >>> exp2.log("accuracy", 1.0) # doctest: +SKIP
        >>> exp2.log_confusion_matrix([1, 1, 0, 0], [1, 1, 0, 0]) # doctest: +SKIP
        >>> results = tracker.query('''
        ... SELECT uuid,
        ...        json_extract(parameters, '$.accuracy') AS accuracy,
        ...        json_extract(parameters, '$.confusion_matrix') AS confusion_matrix
        ... FROM experiments
        ... ''', as_frame=False, render_plots=False)
        >>> results.get("confusion_matrix") # doctest: +SKIP
        """
        pass

def format_id(value):
    pass

def extract_keys(d):
    pass

def _extract_keys(d):
    """ """
    pass

def extract_if_length_one(elements):
    pass

def collapse(elements):
    pass
