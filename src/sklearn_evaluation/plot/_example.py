"""
Example implemention of ``AbstractPlot``, and ``ComposedAbstractPlot``. This is
intended to guide developers add new plots, and not intended for new users.

Useful links:

.. plot:: documentation https://matplotlib.org/3.1.3/devel/plot_directive.html
"""
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from sklearn_evaluation import __version__
from sklearn_evaluation.plot.plot import AbstractComposedPlot, AbstractPlot

class MyBar(AbstractPlot):
    """
    Bar plot. This is an internal plot targeted for developers, not intended for
    end-users.

    Parameters
    ----------
    count : dict
        A dictionary whose keys are labels and values are counts

    color : string, default=None
        Color for the bars, must be a valid matplotlib color

    name : string, default=None
        A value to identify this plot

    Notes
    -----
    .. versionadded:: 0.9


    Examples
    --------

    Create plot:

    .. plot::

        from sklearn_evaluation.plot._example import MyBar
        MyBar.from_raw_data(["banana", "banana", "apple", "pineapple", "apple"],
                                color="lightblue")

    Compare plots:


    .. plot::

        from sklearn_evaluation.plot._example import MyBar
        one = MyBar.from_raw_data(["banana", "banana", "apple", "pineapple", "apple"])
        another = MyBar.from_raw_data(["banana", "apple",  "pineapple"])
        one + another

    """

    def __init__(self, count, *, color=None, name=None):
        self.count = count
        self.color = color
        self.name = name

    def plot(self, ax=None):
        """Create the plot

        Parameters
        -----------
        ax : matplotlib.Axes
            An Axes object to add the plot to
        """
        pass

    @classmethod
    def from_raw_data(cls, things_to_count, *, color=None, name=None):
        """
        check typical naming: such as y_pred, y_score, y_true

        Parameters
        ----------
        things_to_count : list
            The list of elements to count

        color : string, default=None
            Color for the bars, must be a valid matplotlib color

        name : string, default=None
            A value to identify this plot
        """
        pass

    def __add__(self, another):
        return MyBarAdd(counts=[self.count, another.count], names=[self.name, another.name]).plot()

    def __sub__(self, another):
        return MyBarSub(counts=[self.count, another.count]).plot()

    @classmethod
    def _from_data(cls):
        pass

    def _get_data(self):
        pass

class MyBarSub(AbstractComposedPlot):

    def __init__(self, counts, color=None) -> None:
        self.counts = counts
        self.color = color

    def plot(self, ax=None):
        pass

class MyBarAdd(AbstractComposedPlot):

    def __init__(self, counts, names) -> None:
        self.counts = counts
        self.names = names

    def plot(self, ax=None):
        pass

def my_bar(things_to_count, ax=None, color=None):
    """
    Parameters
    ----------
    things_to_count : list
        The list of elements to count

    color : string, default=None
        Color for the bars, must be a valid matplotlib color

    Examples
    --------
    .. plot::

        from sklearn_evaluation.plot._example import my_bar
        my_bar(["banana", "banana", "apple", "pineapple", "apple"],
               color="lightblue")
    """
    pass
