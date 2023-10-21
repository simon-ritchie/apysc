"""Implementations of Polygon class.
"""

from typing import List
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
from apysc._display.append_line_point_mixin import AppendLinePointMixIn
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
from apysc._display.rotation_around_center_mixin import RotationAroundCenterMixIn
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._display.scale_x_from_center_mixin import ScaleXFromCenterMixIn
from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
from apysc._display.scale_y_from_center_mixin import ScaleYFromCenterMixIn
from apysc._display.scale_y_from_point_mixin import ScaleYFromPointMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.set_x_and_y_with_minimum_point_interface_base import (
    SetXAndYWithMinimumPointInterfaceBase,
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


class Polygon(
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
    AppendLinePointMixIn,
    SetXAndYWithMinimumPointInterfaceBase,
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
    The polygon vector graphics class.

    References
    ----------
    - Polygon class
        - https://simon-ritchie.github.io/apysc/en/polygon.html
    - Graphics draw_polygon interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_polygon.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
    >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
    ...     points=[
    ...         ap.Point2D(x=50, y=50),
    ...         ap.Point2D(x=50, y=100),
    ...         ap.Point2D(x=100, y=75),
    ...     ]
    ... )
    >>> polygon.fill_color
    Color("#00aaff")
    """

    # self
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    # points
    @arg_validation_decos.are_point_2ds(arg_position_index=1)
    # fill_color
    @arg_validation_decos.is_color(arg_position_index=2, optional=False)
    # fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=3, optional=False)
    # line_color
    @arg_validation_decos.is_color(arg_position_index=4, optional=False)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=5, optional=False)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=6, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=6, optional=False)
    # line_cap
    @arg_validation_decos.is_line_cap(arg_position_index=7, optional=True)
    # line_joints
    @arg_validation_decos.are_line_joints(arg_position_index=8, optional=True)
    # line_dot_setting
    @arg_validation_decos.is_line_dot_setting(arg_position_index=9)
    # line_dash_setting
    @arg_validation_decos.is_line_dash_setting(arg_position_index=10)
    # line_round_dot_setting
    @arg_validation_decos.is_line_round_dot_setting(arg_position_index=11)
    # line_dash_dot_setting
    @arg_validation_decos.is_line_dash_dot_setting(arg_position_index=12)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=13, optional=True
    )
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=14, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        points: Union[List[Point2D], Array[Point2D]],
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
        Create a polygon vector graphic. This class is
        similar to the Polyline class, but unlike that,
        this class connects an end-point and start-point.

        Parameters
        ----------
        points : Array of Point2D or list of Point2D
            List of polygon vertex points.
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
        - Polygon class
            - https://simon-ritchie.github.io/apysc/en/polygon.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> polygon: ap.Polygon = ap.Polygon(
        ...     points=[
        ...         ap.Point2D(x=50, y=50),
        ...         ap.Point2D(x=50, y=100),
        ...         ap.Point2D(x=100, y=75),
        ...     ],
        ...     fill_color=ap.Color("#00aaff"),
        ... )
        >>> polygon.fill_color
        Color("#00aaff")
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        if isinstance(points, list):
            points = Array(points)
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.POLYGON
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
        self.points = points
        self._append_constructor_expression()
        self._set_line_setting_if_not_none_value_exists(
            line_dot_setting=line_dot_setting,
            line_dash_setting=line_dash_setting,
            line_round_dot_setting=line_round_dot_setting,
            line_dash_dot_setting=line_dash_dot_setting,
        )
        self._set_x_and_y_with_minimum_point()
        super(Polygon, self).__init__(variable_name=variable_name)
        self._set_overflow_visible_setting()
        self._add_to_parent(parent=parent)

    @final
    def _set_x_and_y_with_minimum_point(self) -> None:
        """
        Set an x and y properties coordinate with a minimum point.
        """
        min_x: float = min([point._x._value for point in self._points._value])
        min_y: float = min([point._y._value for point in self._points._value])

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
        points: Union[List[Point2D], Array[Point2D]],
        variable_name_suffix: str = "",
    ) -> "Polygon":
        """
        Create a polygon instance with the instance of
        specified graphics.

        Parameters
        ----------
        graphics : Graphics
            Graphics instance to link this instance.
        points : Array[Point2D]
            List of polygon vertex points.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        polygon : Polygon
            A created polygon instance.
        """
        polygon: Polygon = Polygon(
            points=points,
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
        return polygon

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Polygon("<variable_name>")`).
        """
        repr_str: str = f'{Polygon.__name__}("{self.variable_name}")'
        return repr_str

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "Polygon":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        polygon : Polygon
            An initialized polygon instance.
        """
        from apysc._type.boolean import Boolean

        polygon: Polygon = Polygon(
            points=[
                Point2D(x=-2, y=-2),
                Point2D(x=-1, y=-2),
                Point2D(x=-1, y=-1),
            ]
        )
        polygon.visible = Boolean(False)
        return polygon
