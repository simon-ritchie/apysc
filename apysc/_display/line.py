"""Implementations of the Line class.
"""

from typing import Optional as Op, Union

from apysc._display import graphics
from apysc._display.graphics_base import GraphicsBase
from apysc._display.x_interface import XInterface
from apysc._display.y_interface import YInterface
from apysc._geom import point2d
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos
from apysc._type.int import Int
from apysc._type.string import String
from apysc._type.number import Number
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.line_caps import LineCaps
from apysc._display.line_joints import LineJoints
from apysc._display.child_interface import ChildInterface


class Line(
        XInterface,
        YInterface,
        GraphicsBase):
    """
    The line vector graphics class.

    References
    ----------
    - Graphics draw_line interface document
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_line.html  # noqa
    - Graphics draw_dotted_line interface document
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_dotted_line.html  # noqa
    - Graphics draw_dashed_line interface document
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_dashed_line.html  # noqa
    - Graphics draw_round_dotted_line interface document
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_round_dotted_line.html  # noqa
    - Graphics draw_dash_dotted_line interface document
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_dash_dotted_line.html # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color='#fff', thickness=5)
    >>> line: ap.Line = sprite.graphics.draw_line(
    ...     x_start=50, y_start=50, x_end=150, y_end=50)
    >>> line.line_color
    String('#ffffff')

    >>> line.line_thickness
    Int(5)
    """

    _start_point: 'point2d.Point2D'
    _end_point: 'point2d.Point2D'

    # self
    @arg_validation_decos.multiple_line_settings_are_not_set(
        arg_position_index=0)

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
    @arg_validation_decos.is_line_cap(
        arg_position_index=6, optional=True)

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
        arg_position_index=11, optional=True)

    @add_debug_info_setting(
        module_name=__name__, class_name='Line')
    def __init__(
            self,
            *,
            start_point: 'point2d.Point2D',
            end_point: 'point2d.Point2D',
            line_color: Union[str, String] = '',
            line_alpha: Union[float, Number] = 1.0,
            line_thickness: Union[int, Int] = 1,
            line_cap: Op[Union[String, LineCaps]] = None,
            line_dot_setting: Op[LineDotSetting] = None,
            line_dash_setting: Op[LineDashSetting] = None,
            line_round_dot_setting: Op[LineRoundDotSetting] = None,
            line_dash_dot_setting: Op[LineDashDotSetting] = None,
            parent: Op[ChildInterface] = None) -> None:
        """
        Create a line vector graphic.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        start_point : Points2D
            Line start point.
        end_point : Points2D
            Line end point.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        variable_name: str = expression_variables_util.\
            get_next_variable_name(type_name=var_names.LINE)
        self.variable_name = variable_name
        self._set_initial_basic_values(
            fill_color='', fill_alpha=1,
            line_color=line_color, line_thickness=line_thickness,
            line_alpha=line_alpha, line_cap=line_cap, line_joints=None)
        self._start_point = start_point
        self._end_point = end_point
        self._append_constructor_expression()
        self._set_line_setting_if_not_none_value_exists(
            line_dot_setting=line_dot_setting,
            line_dash_setting=line_dash_setting,
            line_round_dot_setting=line_round_dot_setting,
            line_dash_dot_setting=line_dash_dot_setting)
        super(Line, self).__init__(
            parent=parent, variable_name=variable_name)

    @classmethod
    def _create_with_graphics(
            cls,
            *,
            graphics: 'graphics.Graphics',
            start_point: 'point2d.Point2D',
            end_point: 'point2d.Point2D') -> 'Line':
        """
        Create a line instance with a specified `graphics`
        instance.

        Parameters
        ----------
        graphics : Graphics
            Graphics instance to link this instance.
        start_point : Points2D
            Line start point.
        end_point : Points2D
            Line end point.

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
            parent=graphics)
        return line

    @add_debug_info_setting(
        module_name=__name__, class_name='Line')
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        import apysc as ap
        from apysc._display.stage import get_stage_variable_name
        stage_variable_name: str = get_stage_variable_name()
        points_str: str = self._make_points_expression()
        expression: str = (
            f'var {self.variable_name} = {stage_variable_name}'
            f'\n  .line({points_str})'
            '\n  .attr({'
        )
        expression = self._append_basic_vals_expression(
            expression=expression,
            indent_num=2)
        expression += '\n  });'
        ap.append_js_expression(expression=expression)

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
            f'{start_point.x.variable_name}, '
            f'{start_point.y.variable_name}, '
            f'{end_point.x.variable_name}, '
            f'{end_point.y.variable_name}'
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
