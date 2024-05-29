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
        expression: str = f"var {self.variable_name} = {stage.variable_name}.mask();"
        expression_data_util.append_js_expression(expression=expression)

    def add_masking_object(
        self,
        *,
        masking_object: FillColorMixIn,
        alpha: Union[float, Number] = 1.0,
    ) -> None:
        """
        Add a masking object to this mask. This instance uses its masking object
        to mask other display objects.

        It is possble to add multiple masking objects to a mask.

        Notes
        -----
        This method updates the `masking_object` argument's fill color.

        Parameters
        ----------
        masking_object : FillColorMixIn
            The masking object to add.
        alpha : float or Number, default 1.0
            The alpha value for masking.
            1.0 means fully visible, and 0.0 means fully invisible.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._math.math import Math
        from apysc._color.color import Color
        from apysc._type.int import Int
        from apysc._expression import expression_data_util

        alpha_: Number = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
            float_or_num=alpha
        )
        alpha_ = Math.clamp(value=alpha_, min_=Number(0.0), max_=Number(1.0))
        color_value: Int = Math.trunc(alpha_ * 255)
        mask_color: Color = Color.from_rgb(
            red=color_value, green=color_value, blue=color_value
        )
        masking_object.fill_color = mask_color
        expression: str = f"{self.variable_name}.add({masking_object.variable_name});"
        expression_data_util.append_js_expression(expression=expression)
