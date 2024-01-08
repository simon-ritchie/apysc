"""
The class implementation for the material icon's base class.
"""

from typing import Optional
from typing import Union

from apysc._color.color import Color
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
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.flip_x_mixin import FlipXMixIn
from apysc._display.flip_y_mixin import FlipYMixIn
from apysc._display.get_bounds_mixin import GetBoundsMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.height_mixin import HeightMixIn
from apysc._display.rotation_around_center_mixin import RotationAroundCenterMixIn
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._display.scale_x_from_center_mixin import ScaleXFromCenterMixIn
from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
from apysc._display.scale_y_from_center_mixin import ScaleYFromCenterMixIn
from apysc._display.scale_y_from_point_mixin import ScaleYFromPointMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.skew_x_mixin import SkewXMixIn
from apysc._display.skew_y_mixin import SkewYMixIn
from apysc._display.width_mixin import WidthMixIn
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.repr_interface import ReprInterface
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


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
    WidthMixIn,
    HeightMixIn,
    GetBoundsMixIn,
    VariableNameSuffixMixIn,
    InitializeWithBaseValueInterface,
    AddToParentMixIn,
):
    _svg_path_value: String

    # svg_path_value
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    # fill_color
    @arg_validation_decos.is_color(arg_position_index=2, optional=False)
    # fill_alpha
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    # x
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    # y
    @arg_validation_decos.is_num(arg_position_index=5, optional=False)
    # width
    @arg_validation_decos.num_is_gte_zero(arg_position_index=6, optional=False)
    # height
    @arg_validation_decos.num_is_gte_zero(arg_position_index=7, optional=False)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=8, optional=True
    )
    # variable_name
    @arg_validation_decos.is_builtin_string(arg_position_index=9, optional=False)
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=10, optional=False)
    def __init__(
        self,
        *,
        svg_path_value: Union[str, String],
        fill_color: Color,
        fill_alpha: Union[float, Number] = 1.0,
        x: Union[float, Number] = 0,
        y: Union[float, Number] = 0,
        width: Union[int, Int] = 24,
        height: Union[int, Int] = 24,
        parent: Optional[ChildMixIn] = None,
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
            An icon fill-color.
        fill_alpha : Union[float, Number], optional
            An icon fill-alpha (opacity).
        x : Union[float, Number], optional
            An icon x-coordinate.
        y : Union[float, Number], optional
            An icon y-coordinate.
        width : Union[int, Int], optional
            An icon width.
        height : Union[int, Int], optional
            An icon height.
        parent : ChildMixIn or None, default None
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name : str, optional
            A Variable name of JavaScript.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._converter import to_apysc_val_from_builtin

        self._variable_name_suffix = variable_name_suffix
        variable_name = self._make_variable_name_if_empty(variable_name=variable_name)
        self.variable_name = variable_name
        self._svg_path_value = (
            to_apysc_val_from_builtin.get_copied_string_from_builtin_val(
                string=svg_path_value
            )
        )
        self._append_constructor_expression()
        self.fill_color = fill_color
        self.fill_alpha = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
            float_or_num=fill_alpha
        )
        self.width = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
            integer=width
        )
        self.height = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
            integer=height
        )
        self.x = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
            float_or_num=x
        )
        self.y = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
            float_or_num=y
        )
        super(MaterialIconBase, self).__init__(variable_name=variable_name)
        self._set_overflow_visible_setting()
        self._add_to_parent(parent=parent)

    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression string.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_data_util

        stage: Stage = get_stage()
        expression: str = (
            f"{self.variable_name} = "
            f"{stage.variable_name}.path({self._svg_path_value.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @arg_validation_decos.is_builtin_string(arg_position_index=1, optional=False)
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
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        return f'MaterialIconBase("{self._svg_path_value._value}")'

    @classmethod
    def _initialize_with_base_value(cls) -> "MaterialIconBase":
        """
        Initialize this class with a base value.

        Returns
        -------
        icon : MaterialIconBase
            An initialized icon instance.
        """
        from apysc._color.colors import Colors

        icon: MaterialIconBase = cls(
            svg_path_value="",
            fill_color=Colors.GRAY_AAAAAA,
        )
        return icon
