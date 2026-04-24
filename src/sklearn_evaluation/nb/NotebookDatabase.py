import json
import sqlite3
from glob import iglob
from sklearn_evaluation.nb.NotebookIntrospector import NotebookIntrospector

class NotebookDatabase:
    """
    Construct a SQLite database with a folder of notebooks
    """

    def __init__(self, path_to_db, pattern):
        self._path_to_db = path_to_db
        self._pattern = pattern
        self._conn = sqlite3.connect(self._path_to_db)
        cur = self._conn.cursor()
        cur.execute('\n        CREATE TABLE IF NOT EXISTS nbs (\n            created TIMESTAMP default current_timestamp,\n            path TEXT NOT NULL PRIMARY KEY,\n            c TEXT\n        )\n        ')
        cur.close()

    def index(self, verbose=True, update=False):
        """Index notebooks

        Parameters
        ----------
        verbose : bool, default=True
            If True, it prints one message per notebook

        update : bool, default=False
            If True, it updates the entry in the database if the path already
            exists
        """
        pass

    def query(self, query):
        pass

    def _get_paths(self):
        """Returns a set with all paths to the indexed notebooks"""
        pass
