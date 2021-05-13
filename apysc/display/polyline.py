"""Implementations of Polyline class.
"""

from typing import Any
from typing import Union

from apysc import Array
from apysc import Int
from apysc.display.fill_alpha_interface import FillAlphaInterface
from apysc.display.fill_color_interface import FillColorInterface
from apysc.display.graphic_base import GraphicBase
from apysc.display.line_alpha_interface import LineAlphaInterface
from apysc.display.line_cap_interface import LineCapInterface
from apysc.display.line_color_interface import LineColorInterface
from apysc.display.line_dash_setting_interface import LineDashSettingInterface
from apysc.display.line_dot_setting_interface import LineDotSettingInterface
from apysc.display.line_joints_interface import LineJointsInterface
from apysc.display.line_thickness_interface import LineThicknessInterface
from apysc.display.points_2d_interface import Points2DInterface
from apysc.display.x_interface import XInterface
from apysc.display.y_interface import YInterface
from apysc.geom.point2d import Point2D

_Graphics = Any


class Polyline(
        GraphicBase, FillColorInterface, FillAlphaInterface,
        LineColorInterface, LineAlphaInterface, LineThicknessInterface,
        Points2DInterface, XInterface, YInterface, LineCapInterface,
        LineJointsInterface, LineDotSettingInterface,
        LineDashSettingInterface):

    _points_var_name: str

    def __init__(
            self, parent: _Graphics, points: Array[Point2D]) -> None:
        """
        Create a polyline vector graphic.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        points : Array of Point2D
            List of line points.
        """
        from apysc.display.graphics import Graphics
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        parent_graphics: Graphics = parent
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.POLYLINE)
        super(Polyline, self).__init__(
            parent=parent, x=0, y=0,
            variable_name=variable_name)
        self.points = points
        self._set_initial_fill_color_if_not_blank(
            fill_color=parent_graphics.fill_color)
        self._update_fill_alpha_and_skip_appending_exp(
            value=parent_graphics.fill_alpha)
        self._set_initial_line_color_if_not_blank(
            line_color=parent_graphics.line_color)
        self._update_line_thickness_and_skip_appending_exp(
            value=parent_graphics.line_thickness)
        self._update_line_alpha_and_skip_appending_exp(
            value=parent_graphics.line_alpha)
        self._initialize_x_if_not_initialized()
        self._initialize_y_if_not_initialized()
        self._update_line_cap_and_skip_appending_exp(
            value=parent_graphics.line_cap)
        self._update_line_joints_and_skip_appending_exp(
            value=parent_graphics.line_joints)
        self._append_constructor_expression()
        self._set_line_setting_if_not_none_value_exists(
            parent_graphics=parent_graphics)

    def _set_line_setting_if_not_none_value_exists(
            self, parent_graphics: Any) -> None:
        """
        If a line setting (dot, dash, or something else) with a value
        other than None exists, set that value to the attribute.

        Parameters
        ----------
        parent_graphics : Graphics
            Parent Graphics instance.
        """
        from apysc.display.graphics import Graphics
        parent_graphics_: Graphics = parent_graphics
        if parent_graphics_.line_dot_setting is not None:
            self.line_dot_setting = parent_graphics_.line_dot_setting
            return
        if parent_graphics_.line_dash_setting is not None:
            self.line_dash_setting = parent_graphics_.line_dash_setting
            return

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Polyline('<variable_name>')`).
        """
        repr_str: str = f"Polyline('{self.variable_name}')"
        return repr_str

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        from apysc.display import graphics_expression
        from apysc.display.graphics import Graphics
        from apysc.display.stage import get_stage_variable_name
        from apysc.expression import expression_file_util
        stage_variable_name: str = get_stage_variable_name()
        points_var_name: str
        points_expression: str
        points_var_name, points_expression = \
            self._make_2dim_points_expression()
        expression: str = (
            f'{points_expression}'
            f'\nvar {self.variable_name} = {stage_variable_name}'
            f'\n  .polyline({points_var_name})'
            '\n  .attr({'
        )
        INDENT_NUM: int = 2
        graphics: Graphics = self.parent_graphics
        expression = graphics_expression.append_fill_expression(
            graphics=graphics, expression=expression, indent_num=INDENT_NUM)
        expression = graphics_expression.append_fill_opacity_expression(
            graphics=graphics, expression=expression, indent_num=INDENT_NUM)
        expression = graphics_expression.append_stroke_expression(
            graphics=graphics, expression=expression, indent_num=INDENT_NUM)
        expression = graphics_expression.append_stroke_width_expression(
            graphics=graphics, expression=expression, indent_num=INDENT_NUM)
        expression = graphics_expression.append_stroke_opacity_expression(
            graphics=graphics, expression=expression, indent_num=INDENT_NUM)
        expression = graphics_expression.append_stroke_linecap_expression(
            graphics=graphics, expression=expression, indent_num=INDENT_NUM)
        expression = graphics_expression.append_stroke_linejoin_expression(
            graphics=graphics, expression=expression, indent_num=INDENT_NUM)
        expression = graphics_expression.append_x_expression(
            graphic=self, expression=expression, indent_num=INDENT_NUM)
        expression = graphics_expression.append_y_expression(
            graphic=self, expression=expression, indent_num=INDENT_NUM)
        expression += '\n  });'
        expression_file_util.append_js_expression(expression=expression)
        self._points_var_name = points_var_name

    def append_line_point(
            self, x: Union[int, Int], y: Union[int, Int]) -> None:
        """
        Append line point at the end.

        Parameters
        ----------
        x : int or Int
            X-coordinate.
        y : int or Int
            Y-coordinate.
        """
        from apysc.expression import expression_file_util
        from apysc.type import value_util
        self.points.append(value=Point2D(x=x, y=y))
        expression: str
        x_name: str = value_util.get_value_str_for_expression(value=x)
        y_name: str = value_util.get_value_str_for_expression(value=y)
        expression = (
            f'{self._points_var_name}.push([{x_name}, {y_name}]);'
            f'\n{self.variable_name}.plot({self._points_var_name});'
        )
        expression_file_util.append_js_expression(expression=expression)
