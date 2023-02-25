"""Class implementation for the SVG text's bold mix-in.
"""

from typing import Dict

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos
from apysc._type.boolean import Boolean


class SVGTextBoldMixIn(
    VariableNameMixIn,
):

    _bold: bool = False

    @property
    @add_debug_info_setting(module_name=__name__)
    def bold(self) -> Boolean:
        """
        Get a boolean whether this text is bold style or not.

        Returns
        -------
        bold_ : Boolean
            A boolean whether this text is bold style or not.
        """
        import apysc as ap
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="bold",
        )
        bold_: Boolean = Boolean(self._bold, variable_name_suffix=suffix)
        expression: str = (
            f'{bold_.variable_name} = {self.variable_name}.font("weight") === "bold";'
        )
        ap.append_js_expression(expression=expression)
        return bold_
