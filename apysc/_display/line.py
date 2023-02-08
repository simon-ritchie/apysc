"""Implementations of the Line class.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._display import graphics
from apysc._display.child_mixin import ChildMixIn
from apysc._display.flip_x_mixin import FlipXMixIn
from apysc._display.flip_y_mixin import FlipYMixIn
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
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._geom import point2d
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class Line(
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
    LineColorMixIn,
    LineAlphaMixIn,
    LineDotSettingMixIn,
    LineDashSettingMixIn,
    LineRoundDotSettingMixIn,
    LineDashDotSettingMixIn,
    VariableNameSuffixMixIn,
):
    """
    The line vector graphics class.

    References
    ----------
    - Line class
        - https://simon-ritchie.github.io/apysc/en/line.html
    - Graphics draw_line interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_line.html  # noqa
    - Graphics draw_dotted_line interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_dotted_line.html  # noqa
    - Graphics draw_dashed_line interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_dashed_line.html  # noqa
    - Graphics draw_round_dotted_line interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_round_dotted_line.html  # noqa
    - Graphics draw_dash_dotted_line interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_dash_dotted_line.html # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color="#fff", thickness=5)
    >>> line: ap.Line = sprite.graphics.draw_line(
    ...     x_start=50, y_start=50, x_end=150, y_end=50
    ... )
    >>> line.line_color
    String('#ffffff')

    >>> line.line_thickness
    Int(5)
    """

    _start_point: "point2d.Point2D"
    _end_point: "point2d.Point2D"

    # self
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    # start_point
    @arg_validation_decos.is_point_2d(arg_position_index=1)
    # end_point
    @arg_validation_decos.is_point_2d(arg_position_index=2)
    # line_color
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=3)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=4)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=5)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=5)
    # line_cap
    @arg_validation_decos.is_line_cap(arg_position_index=6, optional=True)
    # line_dot_setting
    @arg_validation_decos.is_line_dot_setting(arg_position_index=7)
    # line_dash_setting
    @arg_validation_decos.is_line_dash_setting(arg_position_index=8)
    # line_round_dot_setting
    @arg_validation_decos.is_line_round_dot_setting(arg_position_index=9)
    # line_dash_dot_setting
    @arg_validation_decos.is_line_dash_dot_setting(arg_position_index=10)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=11, optional=True
    )
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=12, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        start_point: "point2d.Point2D",
        end_point: "point2d.Point2D",
        line_color: Union[str, String] = "",
        line_alpha: Union[float, Number] = 1.0,
        line_thickness: Union[int, Int] = 1,
        line_cap: Optional[Union[String, LineCaps]] = None,
        line_dot_setting: Optional[LineDotSetting] = None,
        line_dash_setting: Optional[LineDashSetting] = None,
        line_round_dot_setting: Optional[LineRoundDotSetting] = None,
        line_dash_dot_setting: Optional[LineDashDotSetting] = None,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Create a line vector graphic.

        Parameters
        ----------
        start_point : Points2D
            Line start point.
        end_point : Points2D
            Line end point.
        line_color : str or String, default ''
            A line-color to set.
        line_alpha : float or Number, default 1.0
            A line-alpha to set.
        line_thickness : int or Int, default 1
            A line-thickness (line-width) to set.
        line_cap : String or LineCaps or None, default None
            A line-cap setting to set.
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
        - Line class
            - https://simon-ritchie.github.io/apysc/en/line.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> line: ap.Line = ap.Line(
        ...     start_point=ap.Point2D(x=50, y=50),
        ...     end_point=ap.Point2D(x=150, y=50),
        ...     line_color="#ffffff",
        ...     line_thickness=3,
        ... )
        >>> line.line_color
        String('#ffffff')
        >>> line.line_thickness
        Int(3)
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.LINE
        )
        self.variable_name = variable_name
        self._set_initial_basic_values(
            fill_color="",
            fill_alpha=1,
            line_color=line_color,
            line_thickness=line_thickness,
            line_alpha=line_alpha,
            line_cap=line_cap,
            line_joints=None,
        )
        self._start_point = start_point
        self._end_point = end_point
        self._append_constructor_expression()
        self._set_line_setting_if_not_none_value_exists(
            line_dot_setting=line_dot_setting,
            line_dash_setting=line_dash_setting,
            line_round_dot_setting=line_round_dot_setting,
            line_dash_dot_setting=line_dash_dot_setting,
        )
        self._set_initial_x_and_y_with_minimum_point()
        super(Line, self).__init__(parent=parent, variable_name=variable_name)

    @final
    def _set_initial_x_and_y_with_minimum_point(self) -> None:
        """
        Set initial x and y properties coordinate with
        a minimum point.
        """
        min_x: float = min(self._start_point._x._value, self._end_point._x._value)
        min_y: float = min(self._start_point._y._value, self._end_point._y._value)
        self._x = Number(min_x)
        self._y = Number(min_y)

    @classmethod
    @final
    def _create_with_graphics(
        cls,
        *,
        graphics: "graphics.Graphics",
        start_point: "point2d.Point2D",
        end_point: "point2d.Point2D",
        variable_name_suffix: str = "",
    ) -> "Line":
        """
        Create a line instance with the instance of
        specified graphics.

        Parameters
        ----------
        graphics : Graphics
            Graphics instance to link this instance.
        start_point : Points2D
            Line start point.
        end_point : Points2D
            Line end point.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        line : Line
            A created line instance.
        """
        line: Line = Line(
            start_point=start_point,
            end_point=end_point,
            line_color=graphics._line_color,
            line_alpha=graphics._line_alpha,
            line_thickness=graphics._line_thickness,
            line_cap=graphics._line_cap,
            line_dot_setting=graphics._line_dot_setting,
            line_dash_setting=graphics._line_dash_setting,
            line_round_dot_setting=graphics._line_round_dot_setting,
            line_dash_dot_setting=graphics._line_dash_dot_setting,
            parent=graphics,
            variable_name_suffix=variable_name_suffix,
        )
        return line

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        import apysc as ap

        stage: ap.Stage = ap.get_stage()
        points_str: str = self._make_points_expression()
        expression: str = (
            f"var {self.variable_name} = {stage.variable_name}"
            f"\n  .line({points_str})"
            "\n  .attr({"
        )
        expression = self._append_basic_vals_expression(
            expression=expression, indent_num=2
        )
        expression += "\n  });"
        ap.append_js_expression(expression=expression)

    @final
    def _make_points_expression(self) -> str:
        """
        Make line start and end expression str.

        Returns
        -------
        expression : str
            Each point expression.
        """
        import apysc as ap

        start_point: ap.Point2D = self._start_point
        end_point: ap.Point2D = self._end_point
        expression: str = (
            f"{start_point.x.variable_name}, "
            f"{start_point.y.variable_name}, "
            f"{end_point.x.variable_name}, "
            f"{end_point.y.variable_name}"
        )
        return expression

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Line('<variable_name>')`).
        """
        repr_str: str = f"Line('{self.variable_name}')"
        return repr_str
