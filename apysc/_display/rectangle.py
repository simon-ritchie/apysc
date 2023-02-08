"""Implementations of the Rectangle class.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._display import graphics
from apysc._display.child_mixin import ChildMixIn
from apysc._display.ellipse_height_mixin import EllipseHeightMixIn
from apysc._display.ellipse_width_mixin import EllipseWidthMixIn
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.flip_x_mixin import FlipXMixIn
from apysc._display.flip_y_mixin import FlipYMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.height_mixin import HeightMixIn
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
from apysc._display.rotation_around_center_mixin import RotationAroundCenterMixIn
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._display.scale_x_from_center_mixin import ScaleXFromCenterMixIn
from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
from apysc._display.scale_y_from_center_mixin import ScaleYFromCenterMixIn
from apysc._display.scale_y_from_point_mixin import ScaleYFromPointMixIn
from apysc._display.skew_x_mixin import SkewXMixIn
from apysc._display.skew_y_mixin import SkewYMixIn
from apysc._display.width_mixin import WidthMixIn
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class Rectangle(
    XMixIn,
    YMixIn,
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
    WidthMixIn,
    HeightMixIn,
    EllipseWidthMixIn,
    EllipseHeightMixIn,
    FillColorMixIn,
    FillAlphaMixIn,
    LineColorMixIn,
    LineAlphaMixIn,
    LineJointsMixIn,
    LineDotSettingMixIn,
    LineDashSettingMixIn,
    LineRoundDotSettingMixIn,
    LineDashDotSettingMixIn,
    VariableNameSuffixMixIn,
):
    """
    The rectangle vector graphics class.

    References
    ----------
    - Rectangle class
        - https://simon-ritchie.github.io/apysc/en/rectangle.html
    - Graphics draw_rect interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_rect.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color="#0af")
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=100, height=75
    ... )
    >>> rectangle.x
    Number(50.0)

    >>> rectangle.y
    Number(50.0)

    >>> rectangle.width
    Int(100)

    >>> rectangle.height
    Int(75)

    >>> rectangle.fill_color
    String('#00aaff')
    """

    # self
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    # x
    @arg_validation_decos.is_num(arg_position_index=1)
    # y
    @arg_validation_decos.is_num(arg_position_index=2)
    # width
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=3)
    # height
    @arg_validation_decos.is_integer(arg_position_index=4)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=4)
    # ellipse_width
    @arg_validation_decos.is_integer(arg_position_index=5)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=5)
    # ellipse_height
    @arg_validation_decos.is_integer(arg_position_index=6)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=6)
    # fill_color
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=7)
    # fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=8)
    # line_color
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=9)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=10)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=11)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=11)
    # line_cap
    @arg_validation_decos.is_line_cap(arg_position_index=12, optional=True)
    # line_joints
    @arg_validation_decos.is_line_joints(arg_position_index=13, optional=True)
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
        x: Union[float, Number],
        y: Union[float, Number],
        width: Union[int, Int],
        height: Union[int, Int],
        ellipse_width: Union[int, Int] = 0,
        ellipse_height: Union[int, Int] = 0,
        fill_color: Union[str, String] = "",
        fill_alpha: Union[float, Number] = 1.0,
        line_color: Union[str, String] = "",
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
        Create a rectangle vector graphic.

        Parameters
        ----------
        x : float or Number
            X-coordinate to start drawing.
        y : float or Number
            Y-coordinate to start drawing.
        width : Int or int
            Rectangle width.
        height : Int or int
            Rectangle height.
        ellipse_width : int or Int
            Ellipse width.
        ellipse_height : int or Int
            Ellipse height.
        fill_color : str or String, default ''
            A fill-color to set.
        fill_alpha : float or Number, default 1.0
            A fill-alpha to set.
        line_color : str or String, default ''
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
            If a specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Rectangle class
            - https://simon-ritchie.github.io/apysc/en/rectangle.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> rectangle: ap.Rectangle = ap.Rectangle(
        ...     x=50, y=50, width=100, height=100, fill_color="#00aaff"
        ... )
        >>> rectangle.x
        Number(50.0)
        >>> rectangle.y
        Number(50.0)
        >>> rectangle.width
        Int(100)
        >>> rectangle.height
        Int(100)
        >>> rectangle.fill_color
        String('#00aaff')
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.RECTANGLE
        )
        self.variable_name = variable_name
        self._update_x_and_skip_appending_exp(x=x)
        self._update_y_and_skip_appending_exp(y=y)
        self._update_width_and_skip_appending_exp(value=width)
        self._update_height_and_skip_appending_exp(value=height)
        self._set_initial_basic_values(
            fill_color=fill_color,
            fill_alpha=fill_alpha,
            line_color=line_color,
            line_thickness=line_thickness,
            line_alpha=line_alpha,
            line_cap=line_cap,
            line_joints=line_joints,
        )
        self._append_constructor_expression()
        self._set_line_setting_if_not_none_value_exists(
            line_dot_setting=line_dot_setting,
            line_dash_setting=line_dash_setting,
            line_round_dot_setting=line_round_dot_setting,
            line_dash_dot_setting=line_dash_dot_setting,
        )
        self._set_ellipse_settings_if_values_are_not_zero(
            ellipse_width=ellipse_width, ellipse_height=ellipse_height
        )
        super(Rectangle, self).__init__(parent=parent, variable_name=variable_name)

    @final
    def _set_ellipse_settings_if_values_are_not_zero(
        self, *, ellipse_width: Union[int, Int], ellipse_height: Union[int, Int]
    ) -> None:
        """
        Set ellipse-related settings if values are not zero.

        Parameters
        ----------
        ellipse_width : Union[int, Int]
            Ellipse width to set.
        ellipse_height : Union[int, Int]
            Ellipse height to set.
        """
        if isinstance(ellipse_width, int) and ellipse_width == 0:
            return
        if isinstance(ellipse_height, int) and ellipse_height == 0:
            return
        if isinstance(ellipse_width, Int) and ellipse_width._value == 0:
            return
        if isinstance(ellipse_height, Int) and ellipse_height._value == 0:
            return
        if isinstance(ellipse_width, int):
            ellipse_width = Int(ellipse_width)
        if isinstance(ellipse_height, int):
            ellipse_height = Int(ellipse_height)
        self.ellipse_width = ellipse_width
        self.ellipse_height = ellipse_height

    @classmethod
    @final
    def _create_with_graphics(
        cls,
        *,
        graphics: "graphics.Graphics",
        x: Union[float, Number],
        y: Union[float, Number],
        width: Union[int, Int],
        height: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> "Rectangle":
        """
        Create a rectangle instance with the instance of
        specified graphics..

        Parameters
        ----------
        graphics : Graphics
            Graphics instance to link this instance.
        x : float or Number
            X-coordinate to start drawing.
        y : float or Number
            Y-coordinate to start drawing.
        width : Int or int
            Rectangle width.
        height : Int or int
            Rectangle height.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        rectangle : Rectangle
            A created rectangle instance.
        """
        rectangle: Rectangle = Rectangle(
            x=x,
            y=y,
            width=width,
            height=height,
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
        return rectangle

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Rectangle('<variable_name>')`).
        """
        repr_str: str = f"Rectangle('{self.variable_name}')"
        return repr_str

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        import apysc as ap

        variable_name: str = self.variable_name
        stage: ap.Stage = ap.get_stage()
        expression: str = (
            f"var {variable_name} = {stage.variable_name}"
            f"\n  .rect({self.width.variable_name}, "
            f"{self.height.variable_name})"
            "\n  .attr({"
        )
        expression = self._append_basic_vals_expression(
            expression=expression, indent_num=2
        )
        expression += "\n  });"
        ap.append_js_expression(expression=expression)
