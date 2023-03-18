"""Class implementation for the SVG text's delta-x mix-in.
"""

from typing import Dict

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos
from apysc._type.number import Number


class SVGTextDeltaXMixIn(
    VariableNameMixIn,
    RevertMixIn,
):

    _delta_x: float = 0.0

    @property
    @add_debug_info_setting(module_name=__name__)
    def delta_x(self) -> Number:
        """
        Get a current position's delta-x value.

        Returns
        -------
        delta_x : Number
            A current position's delta-x value.
        """
        import apysc as ap
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="delta_x",
        )
        delta_x: Number = Number(self._delta_x, variable_name_suffix=suffix)
        expression: str = f"{delta_x.variable_name} = {self.variable_name}.dx();"
        ap.append_js_expression(expression=expression)
        return delta_x
