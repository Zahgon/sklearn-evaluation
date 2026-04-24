from sklearn_evaluation import plot
from sklearn_evaluation.report.util import run_if_args_are_not_none, check_model
from sklearn_evaluation.report import ModelHeuristics, ReportSection, ModelEvaluator

class ModelsComparer(ModelHeuristics):
    """
    Model comparison helper

    This is a utility class that simplifies the comparison of multiple models
    in one place. You can utilize this comparator to compare different models, e.g
    RandomForestClassifier against DecisionTreeClassifier, or LogisticRegression
    agains LinearRegression.

    The results of each step can be accessed using the `key` that corresponds
    to the step name.

    For example
    ``mh.evaluation_state['precision_recall']``

    The steps are : 'precision_recall', 'auc', 'prediction_time',
    'calibration', and 'combined_confusion_matrix'

    If model calculation failed an error is displayed
    """

    def __init__(self, model_a, model_b):
        self.model_a = model_a
        self.model_b = model_b
        self.evaluator_a = ModelEvaluator(model_a)
        self.evaluator_b = ModelEvaluator(model_b)
        super().__init__()

    @run_if_args_are_not_none
    def precision_and_recall(self, X_test, y_true):
        """
        Calculates precision and recall for each of the models
        """
        pass

    @run_if_args_are_not_none
    def auc(self, X_test, y_true):
        """
        Compares models roc auc and adds a report section
        """
        pass

    @run_if_args_are_not_none
    def computation(self, X_test):
        """
        Compares models prediction compute time in seconds and
        adds a report section

        If time differences > 60 sec, warning is displayed
        """
        pass

    @run_if_args_are_not_none
    def calibration(self, X_test, y_true):
        """
        Compares models calibration and adds a report section
        """
        pass

    @run_if_args_are_not_none
    def add_combined_cm(self, X_test, y_true):
        """
        Adds a report guideline with a confusion matrix of model a and model b
        """
        pass

    @run_if_args_are_not_none
    def add_combined_pr(self, X_test, y_true):
        """
        Adds a report guideline with a precision and recall of model a and model b
        """
        pass

def compare_models(model_a, model_b, X_test, y_true, report_title=None):
    """
    Compares two models and generates an HTML report

    Parameters
    -----------
    model_a : estimator
        An estimator to compare.

    model_b : estimator
        An estimator to compare.

    X_test : array-like of shape (n_samples, n_features)
        Training data, where `n_samples` is the number of samples
        and `n_features` is the number of features.

    y_true : array-like
        Correct target values (ground truth).

    report_title : str, default "Compare models - {model_a} vs {model_b}"

    Examples
    --------
    .. seealso:: :ref:`Report: Comparison`

    Compare DecisionTreeClassifier and RandomForestClassifier

    .. plot:: ../examples/report_comparison.py

    Notes
    -----
    .. versionadded:: 0.11.4
    """
    pass
