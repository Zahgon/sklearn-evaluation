from sklearn_evaluation.report.serialize import EvaluatorHTMLSerializer
from sklearn_evaluation.report.report import Report
from jinja2 import Template
from sklearn_evaluation.report.serialize import figure2html
import abc
import traceback

class ReportSection:
    """
    Section to include in report
    """

    def __init__(self, key, include_in_report=True):
        self.report_section = dict({'guidelines': [], 'title': key.replace('_', ' '), 'include_in_report': include_in_report, 'is_ok': False})
        self.key = key

    def append_guideline(self, guideline):
        """
        Add guideline to section

        Parameters
        ----------
        guideline : str
            The guideline to add
        """
        pass

    def get_dict(self) -> dict:
        """
        Return dict of the section
        """
        pass

    def get_guidelines(self) -> list:
        """
        Return section guidelines
        """
        pass

    def set_is_ok(self, is_ok):
        """
        Set if the reported test is valid
        """
        pass

    def set_include_in_report(self, include):
        """
        Set if should include this section in the report
        """
        pass

class ReportError(Exception):

    def __init__(self, message, exc):
        if exc:
            exc_message = getattr(exc, 'message', repr(exc))
            trace = ''.join(traceback.TracebackException.from_exception(exc).format())
            exception_message = self.parse_exec_message_to_html(exc_message)
            self.trace = self.parse_trace_message_to_html(trace)
        self.message = message
        self.exception_message = exception_message

    def parse_exec_message_to_html(self, message) -> str:
        pass

    def parse_trace_message_to_html(self, trace) -> str:
        pass

class ModelHeuristics(abc.ABC):
    """
    Base class for generating model heuristics and reports
    """
    _report_css_style = '\n    .model-evaluation-container h1 {\n        font-size: 2.25em;\n        margin-bottom: 0;\n    }\n\n    .model-evaluation-container h2 {\n        font-size: 1.25em;\n    }\n\n    .model-evaluation-container {\n        font-family: Helvetica, sans-serif, Arial;\n        text-align: left;\n        width: fit-content;\n        min-width: 100%;\n        margin: 50px auto;\n    }\n\n    .model-evaluation-container .block {\n        margin-bottom: 0px;\n        border-bottom: 1px solid #e5e4e4;\n        padding: 0.75em 0;\n    }\n\n    .model-evaluation-container .nobull {\n        list-style-type: none;\n    }\n\n    .model-evaluation-container ul li {\n        margin-bottom: 10px;\n    }\n\n    .model-evaluation-container ul {\n        padding: 0;\n    }\n\n    .model-evaluation-container ul li:not(.nobull) {\n        margin-left: 1em;\n    }\n\n    .model-evaluation-container .display-inline-block {\n        display: inline-block;\n    }\n\n    .model-evaluation-container .capitalize {\n        text-transform: capitalize;\n    }\n\n    .model-evaluation-container .hide {\n        display: none;\n    }\n\n    .model-evaluation-container .error-log {\n        margin-top: 10px;\n        max-width : 50%;\n    }\n    '

    def __init__(self):
        """
        Initialize ModelHeuristics
        """
        self.evaluation_state = dict()

    def _add_section_to_report(self, section):
        """
        Add section to report

        Parameters
        ----------
        section : ReportSection
            The section to include
        """
        pass

    def _get_calculate_failed_error(self, key, model_name, exc=None) -> str:
        """
        Include the raised error in the report

        Parameters
        ----------
        key : str
            The action key

        model_name : str
            The model name

        exc : Expection, default = None
            Include the error message

        Returns
        -------
        formatted error to display in the report str
        """
        pass

    def create_report(self, title) -> Report:
        """
        Generates html report

        Parameters
        ----------
        title : str
            Report title

        Returns
        -------
        Report instance
        """
        pass

    def _get_model_name(self, model) -> str:
        """
        Returns model name
        """
        pass
