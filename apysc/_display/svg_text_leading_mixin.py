"""Class implementation for the SVG text's leading mix-in.
"""

from typing import Dict

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos
from apysc._type.number import Number


class SVGTextLeadingMixIn(
    VariableNameMixIn,
):

    _leading: float = 1.5

    @property
    @add_debug_info_setting(module_name=__name__)
    def leading(self) -> Number:
        """
        Get a current leading setting.

        Returns
        -------
        leading : Number
            A current leading setting.
        """
        import apysc as ap
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="leading",
        )
        leading: Number = Number(self._leading, variable_name_suffix=suffix)
        expression: str = (
            f'{leading.variable_name} = {self.variable_name}.font("leading");'
        )
        ap.append_js_expression(expression=expression)
        return leading
