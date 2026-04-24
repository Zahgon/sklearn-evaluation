from functools import reduce
import base64
from six import BytesIO
import matplotlib

class EvaluatorHTMLSerializer:
    """
    Wraps ClassifierEvaluator so attributes and methods return an HTML
    serializable version of them
    """

    def __init__(self, evaluator):
        self.evaluator = evaluator

    def __getattr__(self, key):
        attr = getattr(self.evaluator, key)
        if callable(attr):
            return HTMLSerializableCallable(attr)
        else:
            return attr

class HTMLSerializableCallable:
    """Wraps a method so that the results is serialized after it is run"""

    def __init__(self, attr):
        self.attr = attr

    def __call__(self, *args, **kwargs):
        obj = self.attr(*args, **kwargs)
        if isinstance(obj, matplotlib.axes.Axes):
            return figure2html(obj.get_figure())
        elif isinstance(obj, matplotlib.figure.Figure):
            return figure2html(obj)
        elif hasattr(obj, 'to_html'):
            return obj.to_html()
        else:
            raise TypeError('Unsupported type {}'.format(type(obj)))

def figure2html(fig):
    pass

def base64_2_html(img):
    pass

def figure2base64(fig):
    pass

def prettify_list(elements):
    pass

def prettify_dict(d):
    pass

def try_figure2html(obj):
    pass

def try_serialize_figures(d):
    pass
