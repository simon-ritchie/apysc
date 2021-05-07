"""Implementations of Rectangle class.
"""

from typing import Any
from typing import Union

from apysc import Int
from apysc.display.fill_alpha_interface import FillAlphaInterface
from apysc.display.fill_color_interface import FillColorInterface
from apysc.display.graphic_base import GraphicBase
from apysc.display.height_interface import HeightInterface
from apysc.display.line_alpha_interface import LineAlphaInterface
from apysc.display.line_color_interface import LineColorInterface
from apysc.display.line_thickness_interface import LineThicknessInterface
from apysc.display.width_interface import WidthInterface

_Graphics = Any


class Rectangle(
        GraphicBase, WidthInterface, HeightInterface, FillColorInterface,
        FillAlphaInterface, LineColorInterface, LineThicknessInterface,
        LineAlphaInterface):

    def __init__(
            self, parent: _Graphics,
            x: Union[int, Int],
            y: Union[int, Int],
            width: Union[int, Int],
            height: Union[int, Int]) -> None:
        """
        Create a rectangle vector graphic.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        x : int or Int
            X position to start drawing.
        y : int or Int
            Y position to start drawing.
        width : int or Int
            Rectangle width.
        height : int or Int
            Rectangle height.
        """
        from apysc.display.graphics import Graphics
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        from apysc.validation import size_validation
        parent_graphics: Graphics = parent
        variable_name: str = expression_variables_util.\
            get_next_variable_name(type_name=var_names.RECTANGLE)
        super(Rectangle, self).__init__(
            parent=parent, x=x, y=y, variable_name=variable_name)
        size_validation.validate_size_is_gte_zero(size=width)
        size_validation.validate_size_is_gte_zero(size=height)
        self._update_width_and_skip_appending_exp(value=width)
        self._update_height_and_skip_appending_exp(value=height)
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
        self._append_constructor_expression()

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

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        from apysc.display.stage import get_stage_variable_name
        from apysc.expression import expression_file_util
        variable_name: str = self.variable_name
        stage_variable_name: str = get_stage_variable_name()
        expression: str = (
            f'var {variable_name} = {stage_variable_name}'
            f'\n  .rect({self.width.variable_name}, '
            f'{self.height.variable_name})'
        )
        attrs_str: str = self._make_rect_attrs_expression()
        expression += f'{attrs_str};'
        expression_file_util.append_js_expression(expression=expression)

    def _make_rect_attrs_expression(self) -> str:
        """
        Make rectangle attributes expression string.

        Returns
        -------
        rect_attrs_expression : str
            Rectangle attributes expression string.
        """
        from apysc.display import graphics_expression
        from apysc.display.graphics import Graphics
        graphics: Graphics = self.parent_graphics
        INDENT_NUM: int = 2
        rect_attrs_expression: str = '\n  .attr({'
        rect_attrs_expression = graphics_expression.append_fill_expression(
            graphics=graphics, expression=rect_attrs_expression,
            indent_num=INDENT_NUM)
        rect_attrs_expression = \
            graphics_expression.append_fill_opacity_expression(
                graphics=graphics, expression=rect_attrs_expression,
                indent_num=INDENT_NUM)
        rect_attrs_expression = graphics_expression.append_stroke_expression(
            graphics=graphics, expression=rect_attrs_expression,
            indent_num=INDENT_NUM)
        rect_attrs_expression = \
            graphics_expression.append_stroke_width_expression(
                graphics=graphics, expression=rect_attrs_expression,
                indent_num=INDENT_NUM)
        rect_attrs_expression = \
            graphics_expression.append_stroke_opacity_expression(
                graphics=graphics, expression=rect_attrs_expression,
                indent_num=INDENT_NUM)
        rect_attrs_expression = graphics_expression.append_x_expression(
            graphic=self, expression=rect_attrs_expression,
            indent_num=INDENT_NUM)
        rect_attrs_expression = graphics_expression.append_y_expression(
            graphic=self, expression=rect_attrs_expression,
            indent_num=INDENT_NUM)

        rect_attrs_expression += '\n  })'
        return rect_attrs_expression
