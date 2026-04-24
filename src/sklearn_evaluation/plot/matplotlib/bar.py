import numpy as np
import matplotlib.pyplot as plt
from sklearn_evaluation.plot.matplotlib.data_grid import DataGrid
from sklearn_evaluation.plot.util import set_default_ax
from sklearn_evaluation.plot.style import gradient_cmap
from sklearn_evaluation.plot.style import apply_theme

def plot(values, orientation, labels=None, sort=True, error=None, ax=None):
    pass

def horizontal(values, labels=None, sort=True, error=None, ax=None):
    """Plots a horizontal bar given a list of values

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> from sklearn_evaluation.plot.matplotlib import bar
    >>> values = np.arange(10)
    >>> ax = bar.horizontal(values)

    Notes
    -----
    https://matplotlib.org/gallery/lines_bars_and_markers/barh.html

    """
    pass

def vertical(values, labels=None, sort=True, error=None, ax=None):
    """Plots vertical bars given a list of values

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> from sklearn_evaluation.plot.matplotlib import bar
    >>> values = np.arange(10)
    >>> ax = bar.vertical(values)

    """
    pass

class BarShifter:
    """
    bar shifter is just a wrapper for matplotlib bar chart
    which automatically computes the position of the bars
    you need to specify how many groups of bars are gonna be
    and the size of such groups. The frst time you call it,
    will plot the first element for every group, then the second one
    and so on
    """

    def __init__(self, g_number, g_size, ax, scale=0.8):
        self.g_number = g_number
        self.g_size = g_size
        self.ax = ax
        self.i = 0
        self.width = 1.0 / g_size * scale
        self.colors = gradient_cmap()(np.linspace(0, 1, self.g_size))

    def __call__(self, height, **kwargs):
        left = [x + self.i * self.width for x in range(self.g_number)]
        self.ax.bar(left, height, self.width, color=self.colors[self.i], ecolor=self.colors[self.i], **kwargs)
        self.i += 1
        if self.i == self.g_size:
            n = range(self.g_number)
            ticks_pos = [x + self.width * self.g_size / 2.0 for x in n]
            self.ax.set_xticks(ticks_pos)

@set_default_ax
def bar_groups(records, ax=None, group_by=None, get_value=lambda data: data, get_error=None):
    pass
