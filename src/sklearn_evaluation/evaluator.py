import matplotlib.pyplot as plt
from sklearn_evaluation.plot.util import requires_properties
from sklearn_evaluation.report.serialize import EvaluatorHTMLSerializer
from sklearn_evaluation.report.report import Report
from sklearn_evaluation.util import estimator_type, class_name
from sklearn_evaluation import plot

class ClassifierEvaluator(object):
    """
    Encapsulates results from an estimator on a testing set to provide a
    simplified API from other modules. All parameters are optional, just
    fill the ones you need for your analysis.

    Parameters
    ----------
    estimator : sklearn estimator
        Must have a ``feature_importances_`` attribute.
    y_true : array-like
        Target predicted classes (estimator predictions).
    y_pred : array-like
        Correct target values (ground truth).
    y_score : array-like
        Target scores (estimator predictions).
    feature_names : array-like
        Feature names.
    target_names : list
        List containing the names of the target classes
    estimator_name : str
        Identifier for the model. This can be later used to identify the
        estimator when generating reports.
    """
    TEMPLATE_NAME = 'classifier.md'

    def __init__(self, estimator=None, y_true=None, y_pred=None, y_score=None, feature_names=None, target_names=None, estimator_name=None, X=None):
        self._estimator = estimator
        self._y_true = y_true
        self._y_pred = y_pred
        self._y_score = y_score
        self._feature_names = feature_names
        self._target_names = target_names
        self._estimator_name = estimator_name
        self._X = X

    @property
    def estimator_type(self):
        """Estimator name (e.g. RandomForestClassifier)"""
        return estimator_type(self.estimator)

    @property
    def estimator_class(self):
        """Estimator class (e.g. sklearn.ensemble.RandomForestClassifier)"""
        pass

    @property
    def estimator(self):
        pass

    @property
    def X(self):
        return self._X

    @property
    def y_true(self):
        pass

    @property
    def y_pred(self):
        pass

    @property
    def y_score(self):
        pass

    @property
    def feature_names(self):
        pass

    @property
    def target_names(self):
        pass

    @property
    def estimator_name(self):
        pass

    def confusion_matrix(self):
        """Confusion matrix plot"""
        pass

    def roc(self):
        """ROC plot"""
        pass

    def precision_recall(self):
        """Precision-recall plot"""
        pass

    def feature_importances(self):
        """Feature importances plot"""
        pass

    def feature_importances_table(self):
        """Feature importances table"""
        pass

    def precision_at_proportions(self):
        """Precision at proportions plot"""
        pass

    def html_serializable(self):
        """
        Returns a EvaluatorHTMLSerializer instance, which is an object with the
        same methods and properties than a ClassifierEvaluator, but it returns
        HTML serialized versions of each
        (i.e. evaluator.feature_importances_table() returns a string with the
        table in HTML format, evaluator.confusion_matrix() returns a HTML image
        element with the image content encoded in base64), useful for
        generating reports using some template system
        """
        pass

    def make_report(self, template=None):
        """
        Make HTML report

        Parameters
        ----------
        template: str, or pathlib.Path, optional
            HTML or Markdown template with jinja2 format. If a pathlib.Path
            object is passed, the content of the file is read. Within the
            template, the evaluator is passed as "e", so you can use things
            like {{e.confusion_matrix()}} or any other attribute/method. If
            None, a default template is used

        style: str
            Path to a css file to apply style to the report. If None, no
            style will be applied

        Returns
        -------
        Report
            Returns the contents of the report if path is None.

        """
        pass

def _gen_ax():
    pass
