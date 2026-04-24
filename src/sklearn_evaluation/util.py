from copy import copy
from inspect import signature, _empty
import re
from collections.abc import Iterable
from collections import defaultdict
from itertools import product
from six import string_types
import numpy as np

def isiter(obj):
    pass

def isiterofiter(obj):
    pass

def estimator_type(model):
    pass

def class_name(obj):
    pass

def _can_iterate(obj):
    pass

def check_elements_in_range(array, min, max, include_min=True, inclue_max=True):
    """
    Checks if values in an array are within a range
    """
    pass

def is_column_vector(x):
    pass

def convert_array_to_string(array, max_length=100):
    pass

def is_row_vector(x):
    pass

def is_binary(array):
    pass

def _group_by(data, criteria):
    """
    Group objects in data using a function or a key
    """
    pass

def _get_params_value(params):
    """
    Given an iterator (k1, k2), returns a function that when called
    with an object obj returns a tuple of the form:
    ((k1, obj.parameters[k1]), (k2, obj.parameters[k2]))
    """
    pass

def _sorted_map_iter(d, sort=True):
    pass

def _product(k, v):
    """
    Perform the product between two objects
    even if they don't support iteration
    """
    pass

def _mapping_to_tuple_pairs(d):
    """
    Convert a mapping object (such as a dictionary) to tuple pairs,
    using its keys and values to generate the pairs and then generating
    all possible combinations between those
    e.g. {1: (1,2,3)} -> (((1, 1),), ((1, 2),), ((1, 3),))
    """
    pass

def _flatten_list(elements):
    pass

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    """
    http://stackoverflow.com/questions/18926031/how-to-extract-a-subset-of-a-colormap-as-a-new-colormap-in-matplotlib
    """
    pass

def map_parameters_in_fn_call(args, kwargs, func):
    """
    Based on function signature, parse args to to convert them to key-value
    pairs and merge them with kwargs
    Any parameter found in args that does not match the function signature
    is still passed.
    Missing parameters are filled with their default values
    """
    pass
