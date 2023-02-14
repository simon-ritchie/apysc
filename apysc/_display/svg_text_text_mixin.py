"""Class implementation for the SVG text's text mix-in.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class SVGTextTextMixIn(
    VariableNameMixIn,
):

    _text: str = ""

    @property
    @add_debug_info_setting(module_name=__name__)
    def text(self) -> String:
        """
        Get a current text's string.

        Returns
        -------
        text : String
            A current text's string.
        """
        from apysc._type.variable_name_suffix_attr_or_var_mixin import (
            VariableNameSuffixAttrOrVarMixIn,
        )

        suffix: str = ""
        if isinstance(self, VariableNameSuffixAttrOrVarMixIn):
            suffix = self._get_attr_or_variable_name_suffix(value_identifier="text")
        text: String = String(self._text, variable_name_suffix=suffix)
        self._append_text_getter_expression(text=text)
        return text

    @text.setter
    @arg_validation_decos.is_apysc_string(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def text(self, value: String) -> None:
        """
        Set a current text's string.

        Parameters
        ----------
        value : String
            A text to set.
        """
        self._text = value._value
        self._append_text_setter_expression(text=value)

    @final
    @arg_validation_decos.is_apysc_string(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
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

    @final
    @arg_validation_decos.is_apysc_string(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_text_setter_expression(self, *, text: String) -> None:
        """
        Append a text's setter expression string.

        Parameters
        ----------
        text : String
            A target text string.
        """
        import apysc as ap

        expression: str = f"{self.variable_name}.text({text.variable_name});"
        ap.append_js_expression(expression=expression)
