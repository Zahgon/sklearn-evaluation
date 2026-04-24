from contextlib import contextmanager
from decorator import decorator
import matplotlib.pyplot as plt
from sklearn_evaluation import util

@decorator
def set_default_ax(func, *args, **kwargs):
    pass

def requires_properties(properties):
    pass

@contextmanager
def no_display_plots():
    """Turn off matplotlib interactive plotting

    Examples
    --------
    >>> from sklearn_evaluation.plot.util import no_display_plots
    >>> import matplotlib.pyplot as plt
    >>> with no_display_plots():
    ...     ax = plt.plot([1, 2, 3])

    """
    pass
