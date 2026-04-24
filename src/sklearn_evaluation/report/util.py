from jinja2 import Environment, PackageLoader
import matplotlib.pyplot as plt

def jinja_env():
    pass

class Range(object):
    """
    Set float range
    """

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def in_range(self, n) -> bool:
        """
        Checks if n in range
        """
        pass

def run_if_args_are_not_none(func):
    """
    Runs a function only if given args are not none.
    Doesn't raise an error.
    """
    pass

def gen_ax():
    pass

def check_model(model) -> None:
    """
    Validate model

    Raises
    ~~~~~~
    ValueError is model is None

    # TODO: Should we add ModuleNotSupportedError?
    """
    pass
