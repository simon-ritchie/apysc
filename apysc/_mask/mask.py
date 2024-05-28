"""Implementation for the mask class.
"""

from typing import Union
from apysc._display.css_mixin import CssMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._type.number import Number


class Mask(
    CssMixIn,
    SetOverflowVisibleSettingMixIn,
):
    """
    The class for the object masking.
    """

    def __init__(
        self,
        *,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class for the object masking.

        Parameters
        ----------
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.MASK
        )
        self.variable_name = variable_name
        self._append_constructor_expression()
        self._set_overflow_visible_setting()

    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_data_util

        stage: Stage = get_stage()
        expression: str = (
            f"var {self.variable_name} = {stage.variable_name}.mask();"
        )
        expression_data_util.append_js_expression(expression=expression)
