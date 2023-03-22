"""Class implementation for the SVG text's delta-y mix-in.
"""

from typing import Dict
from typing import Optional

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class SVGTextDeltaYMixIn(
    VariableNameMixIn,
    RevertMixIn,
):

    _delta_y: float = 0.0

    @property
    @add_debug_info_setting(module_name=__name__)
    def delta_y(self) -> Number:
        """
        Get a current position's delta-y value.

        Returns
        -------
        delta_y : Number
            A current position's delta-y value.
        """
        import apysc as ap
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="delta_y",
        )
        delta_y: Number = Number(self._delta_y, variable_name_suffix=suffix)
        expression: str= f"{delta_y.variable_name} = {self.variable_name}.dy();"
        ap.append_js_expression(expression=expression)
        return delta_y
