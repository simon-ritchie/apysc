"""Implementations of Triangle class.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._color.color import Color
from apysc._color.colorless import COLORLESS
from apysc._display import graphics
from apysc._display.add_to_parent_mixin import AddToParentMixIn
from apysc._display.append_fill_alpha_attr_expression_mixin import (
    AppendFillAlphaAttrExpressionMixIn,
)
from apysc._display.append_fill_color_expression_mixin import (
    AppendFillColorAttrExpressionMixIn,
)
from apysc._display.append_line_alpha_attr_expression_mixin import (
    AppendLineAlphaAttrExpressionMixIn,
)
from apysc._display.append_line_cap_attr_expression_mixin import (
    AppendLineCapAttrExpressionMixIn,
)
from apysc._display.append_line_color_attr_expression_mixin import (
    AppendLineColorAttrExpressionMixIn,
)
from apysc._display.append_line_joints_attr_expression_mixin import (
    AppendLineJointsAttrExpressionMixIn,
)
from apysc._display.append_line_thickness_attr_expression_mixin import (
    AppendLineThicknessAttrExpressionMixIn,
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
from apysc._display.line_alpha_mixin import LineAlphaMixIn
from apysc._display.line_caps import LineCaps
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.line_dash_dot_setting_mixin import LineDashDotSettingMixIn
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_dash_setting_mixin import LineDashSettingMixIn
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_dot_setting_mixin import LineDotSettingMixIn
from apysc._display.line_joints import LineJoints
from apysc._display.line_joints_mixin import LineJointsMixIn
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._display.line_round_dot_setting_mixin import LineRoundDotSettingMixIn
from apysc._display.polygon_append_constructor_expression_mixin import (
    PolygonAppendConstructorExpressionMixIn,
)
from apysc._display.polygon_x1_mixin import PolygonX1MixIn
from apysc._display.polygon_x2_mixin import PolygonX2MixIn
from apysc._display.polygon_x3_mixin import PolygonX3MixIn
from apysc._display.polygon_y1_mixin import PolygonY1MixIn
from apysc._display.polygon_y2_mixin import PolygonY2MixIn
from apysc._display.polygon_y3_mixin import PolygonY3MixIn
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
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._geom.point2d import Point2D
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.repr_interface import ReprInterface
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class Triangle(
    ReprInterface,
    XMixIn,
    AppendXAttrExpressionMixIn,
    YMixIn,
    AppendYAttrExpressionMixIn,
    PolygonX1MixIn,
    PolygonY1MixIn,
    PolygonX2MixIn,
    PolygonY2MixIn,
    PolygonX3MixIn,
    PolygonY3MixIn,
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
    LineColorMixIn,
    AppendLineColorAttrExpressionMixIn,
    LineAlphaMixIn,
    AppendLineAlphaAttrExpressionMixIn,
    AppendLineThicknessAttrExpressionMixIn,
    AppendLineCapAttrExpressionMixIn,
    LineJointsMixIn,
    AppendLineJointsAttrExpressionMixIn,
    LineDotSettingMixIn,
    LineDashSettingMixIn,
    LineRoundDotSettingMixIn,
    LineDashDotSettingMixIn,
    PolygonAppendConstructorExpressionMixIn,
    GetBoundsMixIn,
    VariableNameSuffixMixIn,
    InitializeWithBaseValueInterface,
    AddToParentMixIn,
):
    """
    The triangle vector graphics class.

    References
    ----------
    - Triangle class
        - https://simon-ritchie.github.io/apysc/en/triangle.html

    Examples
    --------
    >>> import apysc as ap
    >>> _ = ap.Stage()
    >>> triangle: ap.Triangle = ap.Triangle(
    ...     x1=75,
    ...     y1=50,
    ...     x2=50,
    ...     y2=100,
    ...     x3=100,
    ...     y3=100,
    ...     fill_color=ap.Color("#0af"),
    ...     line_color=ap.Color("#fff"),
    ...     line_thickness=3,
    ... )
    >>> triangle.x2
    Number(50.0)
    >>> triangle.y1 = ap.Number(30)
    >>> triangle.y1
    Number(30.0)
    """

    # self
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    # x1
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    # y1
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    # x2
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    # y2
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    # x3
    @arg_validation_decos.is_num(arg_position_index=5, optional=False)
    # y3
    @arg_validation_decos.is_num(arg_position_index=6, optional=False)
    # fill_color
    @arg_validation_decos.is_color(arg_position_index=7, optional=False)
    # fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=8, optional=False)
    # line_color
    @arg_validation_decos.is_color(arg_position_index=9, optional=False)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=10, optional=False)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=11, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=11, optional=False)
    # line_cap
    @arg_validation_decos.is_line_cap(arg_position_index=12, optional=True)
    # line_joints
    @arg_validation_decos.are_line_joints(arg_position_index=13, optional=True)
    # line_dot_setting
    @arg_validation_decos.is_line_dot_setting(arg_position_index=14)
    # line_dash_setting
    @arg_validation_decos.is_line_dash_setting(arg_position_index=15)
    # line_round_dot_setting
    @arg_validation_decos.is_line_round_dot_setting(arg_position_index=16)
    # line_dash_dot_setting
    @arg_validation_decos.is_line_dash_dot_setting(arg_position_index=17)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=18, optional=True
    )
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=19, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        x1: Union[float, Number],
        y1: Union[float, Number],
        x2: Union[float, Number],
        y2: Union[float, Number],
        x3: Union[float, Number],
        y3: Union[float, Number],
        fill_color: Color = COLORLESS,
        fill_alpha: Union[float, Number] = 1.0,
        line_color: Color = COLORLESS,
        line_alpha: Union[float, Number] = 1.0,
        line_thickness: Union[int, Int] = 1,
        line_cap: Optional[Union[String, LineCaps]] = None,
        line_joints: Optional[Union[String, LineJoints]] = None,
        line_dot_setting: Optional[LineDotSetting] = None,
        line_dash_setting: Optional[LineDashSetting] = None,
        line_round_dot_setting: Optional[LineRoundDotSetting] = None,
        line_dash_dot_setting: Optional[LineDashDotSetting] = None,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Create a triangle vector graphics instance.

        Parameters
        ----------
        x1 : Union[float, Number]
            First vertex's x coordinate.
        y1 : Union[float, Number]
            First vertex's y coordinate.
        x2 : Union[float, Number]
            Second vertex's x coordinate.
        y2 : Union[float, Number]
            Second vertex's y coordinate.
        x3 : Union[float, Number]
            Third vertex's x coordinate.
        y3 : Union[float, Number]
            Third vertex's y coordinate.
        fill_color : Color, default COLORLESS
            A fill-color to set.
        fill_alpha : float or Number, default 1.0
            A fill-alpha to set.
        line_color : Color, default COLORLESS
            A line-color to set.
        line_alpha : float or Number, default 1.0
            A line-alpha to set.
        line_thickness : int or Int, default 1
            A line-thickness (line-width) to set.
        line_cap : String or LineCaps or None, default None
            A line-cap setting to set.
        line_joints : String or LineJoints or None, default None
            A line-joints setting to set.
        line_dot_setting : LineDotSetting or None, default None
            A dot setting to set.
        line_dash_setting : LineDashSetting or None, default None
            A dash setting to set.
        line_round_dot_setting : LineRoundDotSetting or None, default None
            A round-dot setting to set.
        line_dash_dot_setting : LineDashDotSetting or None, default None
            A dash-dot (1-dot chain) setting to set.
        parent : ChildMixIn or None, default None
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Triangle class
            - https://simon-ritchie.github.io/apysc/en/triangle.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> triangle: ap.Triangle = ap.Triangle(
        ...     x1=75,
        ...     y1=50,
        ...     x2=50,
        ...     y2=100,
        ...     x3=100,
        ...     y3=100,
        ...     fill_color=ap.Color("#0af"),
        ...     line_color=ap.Color("#fff"),
        ...     line_thickness=3,
        ... )
        >>> triangle.x2
        Number(50.0)
        >>> triangle.y1 = ap.Number(30.0)
        >>> triangle.y1
        Number(30.0)
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_number_from_builtin_val,
        )
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.TRIANGLE,
        )
        self.variable_name = variable_name
        self._set_initial_basic_values(
            fill_color=fill_color,
            fill_alpha=fill_alpha,
            line_color=line_color,
            line_thickness=line_thickness,
            line_alpha=line_alpha,
            line_cap=line_cap,
            line_joints=line_joints,
        )
        self._x1 = get_copied_number_from_builtin_val(float_or_num=x1)
        self._y1 = get_copied_number_from_builtin_val(float_or_num=y1)
        self._x2 = get_copied_number_from_builtin_val(float_or_num=x2)
        self._y2 = get_copied_number_from_builtin_val(float_or_num=y2)
        self._x3 = get_copied_number_from_builtin_val(float_or_num=x3)
        self._y3 = get_copied_number_from_builtin_val(float_or_num=y3)
        self._set_points_with_each_coordinate()
        self._append_constructor_expression()
        self._set_line_setting_if_not_none_value_exists(
            line_dot_setting=line_dot_setting,
            line_dash_setting=line_dash_setting,
            line_round_dot_setting=line_round_dot_setting,
            line_dash_dot_setting=line_dash_dot_setting,
        )
        self._set_x_and_y_with_minimum_point()
        super(Triangle, self).__init__(variable_name=variable_name)
        self._set_overflow_visible_setting()
        self._add_to_parent(parent=parent)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_points_with_each_coordinate(self) -> None:
        """
        Set the `_points`' attribute value with each coordinate.
        """
        self._points = Array(
            value=[
                Point2D(x=self._x1, y=self._y1),
                Point2D(x=self._x2, y=self._y2),
                Point2D(x=self._x3, y=self._y3),
            ]
        )

    @final
    def _set_x_and_y_with_minimum_point(self) -> None:
        """
        Set an x and y properties coordinate with a minimum point.
        """
        min_x: float = min(self._x1._value, self._x2._value, self._x3._value)
        min_y: float = min(self._y1._value, self._y2._value, self._y3._value)

        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="x")
        self._x = Number(min_x, variable_name_suffix=suffix)

        suffix = self._get_attr_or_variable_name_suffix(value_identifier="y")
        self._y = Number(min_y, variable_name_suffix=suffix)

    @classmethod
    @final
    def _create_with_graphics(
        cls,
        *,
        graphics: "graphics.Graphics",
        x1: Union[float, Number],
        y1: Union[float, Number],
        x2: Union[float, Number],
        y2: Union[float, Number],
        x3: Union[float, Number],
        y3: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> "Triangle":
        """
        Create a triangle instance with the instance of
        specified graphics.

        Parameters
        ----------
        graphics : graphics.Graphics
            Graphics instance to link this instance.
        x1 : Union[float, Number]
            First vertex's y coordinate.
        y1 : Union[float, Number]
            First vertex's y coordinate.
        x2 : Union[float, Number]
            Second vertex's x coordinate.
        y2 : Union[float, Number]
            Second vertex's y coordinate.
        x3 : Union[float, Number]
            Third vertex's x coordinate.
        y3 : Union[float, Number]
            Third vertex's y coordinate.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        triangle : Triangle
            A created triangle instance.
        """
        triangle: Triangle = Triangle(
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            x3=x3,
            y3=y3,
            fill_color=graphics._fill_color,
            fill_alpha=graphics._fill_alpha,
            line_color=graphics._line_color,
            line_alpha=graphics._line_alpha,
            line_thickness=graphics._line_thickness,
            line_cap=graphics._line_cap,
            line_joints=graphics._line_joints,
            line_dot_setting=graphics._line_dot_setting,
            line_dash_setting=graphics._line_dash_setting,
            line_round_dot_setting=graphics._line_round_dot_setting,
            line_dash_dot_setting=graphics._line_dash_dot_setting,
            parent=graphics,
            variable_name_suffix=variable_name_suffix,
        )
        return triangle

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Triangle("<variable_name>")`).
        """
        repr_str: str = f'{Triangle.__name__}("{self.variable_name}")'
        return repr_str

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "Triangle":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        triangle : Triangle
            An initialized triangle instance.
        """
        from apysc._type.boolean import Boolean

        triangle: Triangle = Triangle(
            x1=-2,
            y1=-2,
            x2=-1,
            y2=-2,
            x3=-1,
            y3=-1,
        )
        triangle.visible = Boolean(False)
        return triangle
