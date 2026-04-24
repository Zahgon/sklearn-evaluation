"""
Tools for binarizing scores
"""
import numpy as np
from sklearn_evaluation import validate

def cutoff_score_at_top_proportion(y_score, top_proportion):
    """
    Sort scores and get the score at
    """
    pass

def cutoff_score_at_top_n(y_score, top_n):
    pass

def cutoff_score_at_quantile(y_score, quantile):
    pass

def scores_at_top_proportion(y_score, top_proportion):
    """Binary scores by sorting them and grabbing a proportion from the top"""
    pass

def at_top_n(y_score, top_n):
    pass

def scores_at_quantile(y_score, quantile):
    """Binary scores at certain quantile"""
    pass

def scores_at_thresholds(y_score, n_thresholds=10, start=0.0):
    """
    Binarize scores at increasing thresholds, outputs a binary
    matrix where each row corresponds to the binary labels
    obtained from thresholding. n thresholds are generated
    uniformly from [start, 1.0]
    """
    pass
