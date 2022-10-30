"""Document (overall window) class implementation.
"""

from typing_extensions import final

from apysc._type.variable_name_mixin import VariableNameMixIn


class Document(VariableNameMixIn):
    """
    Document (overall HTML document) class.
    """

    @final
    def __init__(self) -> None:
        """
        Document (overall HTML document) class.
        """
        from apysc._expression import var_names

        self.variable_name = var_names.DOCUMENT


document: Document = Document()
