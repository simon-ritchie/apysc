"""Class implementation for the SVG text's text mix-in.
"""

from apysc._type.string import String
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn
)


class SvgTextTextMixIn(
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):

    _text: str = ""

    @property
    def text(self) -> String:
        """
        Get a current text's string.

        Returns
        -------
        text : String
            A current text's string.
        """
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="text")
        text: String = String(self._text, variable_name_suffix=suffix)
        self._append_text_getter_expression(text=text)
        pass

    def _append_text_getter_expression(self, *, text: String) -> None:
        """
        Append a text's getter expression string.

        Parameters
        ----------
        text : String
            A target text string.
        """
        import apysc as ap
        expression: str = f"{text.variable_name} = {self.variable_name}.text();"
        ap.append_js_expression(expression=expression)

