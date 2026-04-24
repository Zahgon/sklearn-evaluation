from sklearn.metrics import accuracy_score
from sklearn.metrics import auc
import re
from sklearn_evaluation import plot
from sklearn_evaluation.report.util import Range, run_if_args_are_not_none, gen_ax, check_model
from sklearn_evaluation.report import ModelHeuristics, ReportSection
import time
import numpy as np
COMMUNITY_LINK = 'https://ploomber.io/community'
COMMUNITY = 'If you need help understanding these stats, ' + f"send us a message on <a href='{COMMUNITY_LINK}'" + "target='_blank'>slack</a>"

class ModelEvaluator(ModelHeuristics):
    """
    Model evaluation report

    This is a utility class that simplifies the evaluation of various model
    aspects, including balance, AUC, and accuracy. Use this evaluator
    to assess different models like RandomForestClassifier, DecisionTreeClassifier,
    LogisticRegression, and LinearRegression.

    The results of each step can be accessed using the `key` that corresponds
    to the step name. Use a custom ReportSection to use your own keys and
    a different report structure.

    For example
    ``mh.evaluation_state['auc']``

    The steps are : 'balance', 'accuracy', 'auc', 'general_stats',
    'calibration', and 'precision_recall'
    """

    def __init__(self, model):
        self.model = model
        super().__init__()

    @run_if_args_are_not_none
    def evaluate_balance(self, y_true, custom_section=None):
        """
        Checks if model is balanced

        If minority class is < 5%, then a plot and class imbalance warning is displayed
        """
        pass

    @run_if_args_are_not_none
    def evaluate_accuracy(self, y_true, y_pred_test, custom_section=None):
        """
        Measures how many labels the model got right out of the
        total number of predictions

        If accuracy score is < 80%, then a plot and class accuracy warning are displayed
        If accuracy score is > 80% and class is imbalanced, then a plot and class
        accuracy warning are displayed
        """
        pass

    @run_if_args_are_not_none
    def evaluate_auc(self, y_true, y_score, custom_section=None):
        """
        Checks if roc auc is in acceptable range

        If auc is < 70%, then plot and low auc warning are displayed
        """
        pass

    def generate_general_stats(self, y_true, y_pred, y_score, X_test=None, custom_section=None):
        """
        Add confusion matrix and roc curve to the report
        """
        pass

    @run_if_args_are_not_none
    def evaluate_precision_and_recall(self, X_test, y_true, custom_section=None):
        """
        Returns a precision and recall plot
        """
        pass

    @run_if_args_are_not_none
    def evaluate_calibration(self, X_test, y_true, custom_section=None):
        """
        Returns a calibration plot
        """
        pass

    @run_if_args_are_not_none
    def get_roc_auc(self, y_test, y_score) -> list:
        """
        Returns list of roc auc
        """
        pass

    @run_if_args_are_not_none
    def get_model_prediction_time(self, X) -> float:
        """
        Returns model.predict(X) time in seconds
        """
        pass

    @run_if_args_are_not_none
    def check_array_balance(self, array) -> bool:
        """
        Checks if array is balanced.

        Balance threshold is 0.05
        """
        pass

def evaluate_model(model, y_true, y_pred, X_test=None, y_score=None, report_title=None):
    """
    Evaluates a given model and generates an HTML report

    Parameters
    -----------
    model : estimator
        An estimator to evaluate.

    y_true : array-like
        Correct target values (ground truth).

    y_pred : array-like
        Target predicted classes (estimator predictions).

    y_score : array-like, default None
        Target scores (estimator predictions).

    report_title : str, default "Model evaluation - {model_name}"

    Examples
    --------

    .. seealso:: :ref:`Report: Evaluation`

    Generate evaluation report for RandomForestClassifier

    .. plot:: ../examples/report_evaluation.py

    Notes
    -----
    .. versionadded:: 0.11.4
    """
    pass
