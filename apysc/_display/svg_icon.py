"""The SVG icon class implementation.
"""

from typing import Optional
from typing import Union

from apysc._color.color import Color
from apysc._color.colors import Colors
from apysc._display.add_to_parent_mixin import AddToParentMixIn
from apysc._display.append_fill_alpha_attr_expression_mixin import (
    AppendFillAlphaAttrExpressionMixIn,
)
from apysc._display.append_fill_color_expression_mixin import (
    AppendFillColorAttrExpressionMixIn,
)
from apysc._display.append_x_attr_expression_mixin import AppendXAttrExpressionMixIn
from apysc._display.append_y_attr_expression_mixin import AppendYAttrExpressionMixIn
from apysc._display.child_mixin import ChildMixIn
from apysc._display.css_mixin import CssMixIn
from apysc._display.display_object import DisplayObject
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.get_bounds_mixin import GetBoundsMixIn
from apysc._display.scale_x_from_center_mixin import ScaleXFromCenterMixIn
from apysc._display.scale_y_from_center_mixin import ScaleYFromCenterMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._type.number import Number
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class SvgIcon(
    XMixIn,
    AppendXAttrExpressionMixIn,
    YMixIn,
    AppendYAttrExpressionMixIn,
    ScaleXFromCenterMixIn,
    ScaleYFromCenterMixIn,
    FillColorMixIn,
    AppendFillColorAttrExpressionMixIn,
    FillAlphaMixIn,
    AppendFillAlphaAttrExpressionMixIn,
    CssMixIn,
    DisplayObject,
    AddToParentMixIn,
    SetOverflowVisibleSettingMixIn,
    GetBoundsMixIn,
    VariableNameSuffixMixIn,
):
    _svg_icon_html: str

    def __init__(
        self,
        *,
        svg_icon_html: str,
        x: Union[float, Number] = 0.0,
        y: Union[float, Number] = 0.0,
        fill_color: Color = Colors.GRAY_666666,
        fill_alpha: Union[float, Number] = 1.0,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The SVG icon class implementation.

        Parameters
        ----------
        svg_icon_html : str
            An SVG icon html string.
            For example, "<svg xmlns="http://www.w3.org/2000/svg" ...>...</svg>"
        x : float or Number, optional
            X-coordinate of the icon.
        y : float or Number, optional
            Y-coordinate of the icon.
        fill_color : Color, default Colors.GRAY_666666
            Fill-color of the icon.
        fill_alpha : float or Number, default 1.0
            Fill-alpha of the icon.
        parent : ChildMixIn or None, default None
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_number_from_builtin_val,
        )
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.SVG_ICON
        )
        self.variable_name = variable_name
        self._svg_icon_html = svg_icon_html
        self._append_constructor_expression()
        super(SvgIcon, self).__init__(variable_name=variable_name)
        self.x = get_copied_number_from_builtin_val(float_or_num=x)
        self.y = get_copied_number_from_builtin_val(float_or_num=y)
        self.fill_color = fill_color
        self.fill_alpha = get_copied_number_from_builtin_val(float_or_num=fill_alpha)
        self._set_overflow_visible_setting()
        self._add_to_parent(parent=parent)

    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"var {self.variable_name} = " f"SVG('{self._svg_icon_html}');"
        )
        expression_data_util.append_js_expression(expression=expression)
