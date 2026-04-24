from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn_evaluation import plot
from sklearn_evaluation.plot.roc import is_array_like_scores
from sklearn_evaluation.grid.classifier_grid import AbstractClassifierGrid, GridTypes
from sklearn.utils.validation import check_consistent_length
import warnings

class RandomForestClassifierGrid(AbstractClassifierGrid):
    param_grids = dict({GridTypes.TINY: {'n_estimators': [50, 100, 500], 'criterion': ['gini', 'entropy'], 'min_samples_split': [2, 4], 'min_samples_leaf': [1, 2], 'max_features': [1.0]}, GridTypes.SMALL: {'n_estimators': [50, 100, 150, 500], 'criterion': ['gini', 'entropy'], 'min_samples_split': [2, 4, 8], 'min_samples_leaf': [1, 2, 4], 'max_features': [1.0, 'sqrt', 'log2']}, GridTypes.MEDIUM: {'n_estimators': [50, 100, 150, 200, 500], 'criterion': ['gini', 'entropy'], 'min_samples_split': [2, 4, 8, 16], 'min_samples_leaf': [1, 2, 4, 8], 'max_features': [1.0, 'sqrt', 'log2']}, GridTypes.LARGE: {'n_estimators': [50, 100, 150, 200, 300, 500], 'criterion': ['gini', 'entropy', 'log_loss'], 'min_samples_split': [2, 4, 8, 16, 24], 'min_samples_leaf': [1, 2, 4, 8, 16], 'max_features': [1.0, 'sqrt', 'log2']}, GridTypes.X_LARGE: {'n_estimators': [50, 100, 150, 200, 300, 400, 500], 'criterion': ['gini', 'entropy', 'log_loss'], 'min_samples_split': [2, 4, 8, 16, 24, 40], 'min_samples_leaf': [1, 2, 4, 8, 16, 20], 'max_features': [1.0, 'sqrt', 'log2']}})

    def __init__(self, grid, cv=3, verbose=0):
        """
        A random forest classifier grid.

        Parameters
        ----------
        grid : str, default="tiny"
            The grid size to initialize

        cv : int, cross-validation generator or an iterable, default=3
            Determines the cross-validation splitting strategy.
            Possible inputs for cv are:

            - None, to use the default 5-fold cross validation,
            - integer, to specify the number of folds in a `(Stratified)KFold`,
            - :term:`CV splitter`,
            - An iterable yielding (train, test) splits as arrays of indices.

            For integer/None inputs, if the estimator is a classifier and ``y`` is
            either binary or multiclass, :class:`StratifiedKFold` is used. In all
            other cases, :class:`KFold` is used. These splitters are instantiated
            with `shuffle=False` so the splits will be the same across calls.

            Refer :ref:`User Guide <cross_validation>` for the various
            cross-validation strategies that can be used here.

        verbose : int
            Controls the verbosity: the higher, the more messages.

            - >1 : the computation time for each fold and parameter candidate is
            displayed;
            - >2 : the score is also displayed;
            - >3 : the fold and candidate parameter indexes are also displayed
            together with the starting time of the computation.

        """
        super().__init__(grid)
        self.param_grid_ = self.param_grids[self.grid]
        self.estimator_ = RandomForestClassifier()
        self.grid_search_cv_ = GridSearchCV(estimator=self.estimator_, param_grid=self.param_grid_, cv=cv, verbose=verbose)

    def fit(self, X, y):
        """
        Fit estimator.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The input samples. Use ``dtype=np.float32`` for maximum
            efficiency. Sparse matrices are also supported, use sparse
            ``csc_matrix`` for maximum efficiency.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Returns the instance itself.
        """
        pass

    def set_test_data(self, X_test, y_test) -> None:
        """
        Set the test data

        Parameters
        ----------
        X_test : array-like of shape (n_samples, n_features)
            Training data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y_test : array-like of shape (n_samples,)
            The target variable for supervised learning problems.
        """
        pass

    def confusion_matrix(self):
        """
        Plots a confusion matrix based on `GridSearchCV.best_estimator_`.

        Returns
        -------
        ax: matplotlib Axes
            Axes containing the plot

        Examples
        --------
        .. plot:: ../examples/rf_grid_cm.py

        """
        pass

    def roc(self):
        """
        Plots an ROC based on `GridSearchCV.best_estimator_`.

        Returns
        -------
        ax: matplotlib Axes
            Axes containing the plot

        Examples
        --------
        .. plot:: ../examples/rf_grid_roc.py
        """
        pass

    def feature_importances(self):
        """
        Plots feature importances based on `GridSearchCV.best_estimator_`.

        Returns
        -------
        ax: matplotlib Axes
            Axes containing the plot

        Examples
        --------
        .. plot:: ../examples/rf_grid_feature_importances.py

        """
        pass

    def grid_search_results(self, change='n_estimators', kind='line'):
        """
        Plots grid search results based on `GridSearchCV.best_estimator_`.

        Parameters
        ----------
        change : str or iterable with len<=2
            Parameter to change

        kind : ['line', 'bar']
            This only applies whe change is a single parameter. Changes the
            type of plot

        Returns
        -------
        ax: matplotlib Axes
            Axes containing the plot
        """
        pass

    def _show_no_test_data_provided_warning(self) -> None:
        """
        Warn the user if no test data was provided.
        """
        pass

    def _prepare_test_data_for_plotting(self):
        """
        Get the data to draw the plots.

        If no test data was given use the training data.

        Returns
        -------
        X_test : array-like of shape (n_samples, n_features)
            Training data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y_test : array-like of shape (n_samples,)
            The target variable for supervised learning problems.
        """
        pass

    def _is_test_data_given(self):
        pass

    def _validate_test_data(self, X_test, y_test) -> None:
        """
        Check if given test data is valid.
        """
        pass
