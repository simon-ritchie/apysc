"""
The class implementation for the material icon's base class.
"""

from typing import Union
from apysc._type.string import String
from apysc._color.color import Color
from apysc._type.number import Number
from apysc._type.int import Int
from apysc._validation import arg_validation_decos
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._type.repr_interface import ReprInterface
from apysc._display.append_x_attr_expression_mixin import AppendXAttrExpressionMixIn
from apysc._display.append_y_attr_expression_mixin import AppendYAttrExpressionMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.css_mixin import CssMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.rotation_around_center_mixin import RotationAroundCenterMixIn
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._display.scale_x_from_center_mixin import ScaleXFromCenterMixIn
from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
from apysc._display.scale_y_from_center_mixin import ScaleYFromCenterMixIn
from apysc._display.scale_y_from_point_mixin import ScaleYFromPointMixIn
from apysc._display.flip_x_mixin import FlipXMixIn
from apysc._display.flip_y_mixin import FlipYMixIn
from apysc._display.skew_x_mixin import SkewXMixIn
from apysc._display.skew_y_mixin import SkewYMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.append_fill_color_expression_mixin import (
    AppendFillColorAttrExpressionMixIn,
)
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.append_fill_alpha_attr_expression_mixin import (
    AppendFillAlphaAttrExpressionMixIn,
)
from apysc._display.get_bounds_mixin import GetBoundsMixIn
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._display.add_to_parent_mixin import AddToParentMixIn


class MaterialIconBase(
    ReprInterface,
    XMixIn,
    AppendXAttrExpressionMixIn,
    YMixIn,
    AppendYAttrExpressionMixIn,
    SetOverflowVisibleSettingMixIn,
    CssMixIn,
    GraphicsBase,
    RotationAroundCenterMixIn,
    RotationAroundPointMixIn,
    ScaleXFromCenterMixIn,
    ScaleYFromCenterMixIn,
    ScaleXFromPointMixIn,
    ScaleYFromPointMixIn,
    FlipXMixIn,
    FlipYMixIn,
    SkewXMixIn,
    SkewYMixIn,
    FillColorMixIn,
    AppendFillColorAttrExpressionMixIn,
    FillAlphaMixIn,
    AppendFillAlphaAttrExpressionMixIn,
    GetBoundsMixIn,
    VariableNameSuffixMixIn,
    # InitializeWithBaseValueInterface,
    AddToParentMixIn,
):

    # svg_path_value
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    # fill_color
    @arg_validation_decos.is_color(arg_position_index=2, optional=False)
    # fill_alpha
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    # width
    @arg_validation_decos.num_is_gte_zero(arg_position_index=4, optional=False)
    # height
    @arg_validation_decos.num_is_gte_zero(arg_position_index=5, optional=False)
    # variable_name
    @arg_validation_decos.is_builtin_string(arg_position_index=6, optional=False)
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=7, optional=False)
    def __init__(
        self,
        *,
        svg_path_value: Union[str, String],
        fill_color: Color,
        fill_alpha: Union[float, Number] = 1.0,
        width: Union[int, Int] = 24,
        height: Union[int, Int] = 24,
        variable_name: str = "",
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class implementation for the material icon's base class.

        Parameters
        ----------
        svg_path_value : Union[str, String]
            SVG path value string.
            This value requires the `d` attribute of the SVG `path` tag.
            E.g., "M15.5 14h-.79l-.28-.27C15.41 12.59 ..."
        fill_color : Color
            An icon fill color.
        fill_alpha : Union[float, Number], optional
            An icon fill alpha (opacity).
        width : Union[int, Int], optional
            An icon width.
        height : Union[int, Int], optional
            An icon height.
        variable_name : str, optional
            A Variable name of JavaScript.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self.variable_name = self._make_variable_name_if_empty(
            variable_name=variable_name
        )
        pass

    def _make_variable_name_if_empty(self, *, variable_name: str) -> str:
        """
        Make a variable name if it is empty.

        Parameters
        ----------
        variable_name : str
            A variable name of JavaScript.

        Returns
        -------
        variable_name : str
            A variable name of JavaScript.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        if variable_name != "":
            return variable_name
        variable_name = expression_variables_util.get_next_variable_name(
            type_name=var_names.MATERIAL_ICON,
        )
        return variable_name
    
    def __repr__(self) -> str:
        pass
