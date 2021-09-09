"""Implementations of the Rectangle class.
"""

from typing import Union

import apysc as ap
from apysc._display.ellipse_height_interface import EllipseHeightInterface
from apysc._display.ellipse_width_interface import EllipseWidthInterface
from apysc._display.height_interface import HeightInterface
from apysc._display.line_base import LineBase
from apysc._display.width_interface import WidthInterface


class Rectangle(
        LineBase, WidthInterface, HeightInterface,
        EllipseWidthInterface, EllipseHeightInterface):
    """
    The rectangle vector graphics class.

    References
    ----------
    - Graphics draw_rect interface document
        - https://simon-ritchie.github.io/apysc/graphics_draw_rect.html
    """

    def __init__(
            self, parent: 'ap.Graphics',
            x: Union[int, ap.Int],
            y: Union[int, ap.Int],
            width: Union[int, ap.Int],
            height: Union[int, ap.Int]) -> None:
        """
        Create a rectangle vector graphics.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphics.
        x : int or Int
            X-coordinate to start drawing.
        y : int or Int
            Y-coordinate to start drawing.
        width : int or Int
            Rectangle width.
        height : int or Int
            Rectangle height.

        References
        ----------
        - Graphics draw_rect interface document
            - https://simon-ritchie.github.io/apysc/graphics_draw_rect.html
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Rectangle):
            from apysc._display.graphics import Graphics
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            from apysc._validation import size_validation
            parent_graphics: Graphics = parent
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.RECTANGLE)
            super(Rectangle, self).__init__(
                parent=parent, x=x, y=y, variable_name=variable_name)
            size_validation.validate_size_is_gte_zero(size=width)
            size_validation.validate_size_is_gte_zero(size=height)
            self._update_width_and_skip_appending_exp(value=width)
            self._update_height_and_skip_appending_exp(value=height)
            self._set_initial_basic_values(parent=parent)
            self._append_constructor_expression()
            self._set_line_setting_if_not_none_value_exists(
                parent_graphics=parent_graphics)
            self._set_overflow_visible_setting()

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
        Append constructor expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=Rectangle):
            from apysc._display.stage import get_stage_variable_name
            variable_name: str = self.variable_name
            stage_variable_name: str = get_stage_variable_name()
            expression: str = (
                f'var {variable_name} = {stage_variable_name}'
                f'\n  .rect({self.width.variable_name}, '
                f'{self.height.variable_name})'
            )
            attrs_str: str = self._make_rect_attrs_expression()
            expression += f'{attrs_str};'
            ap.append_js_expression(expression=expression)

    def _make_rect_attrs_expression(self) -> str:
        """
        Make rectangle attributes expression string.

        Returns
        -------
        rect_attrs_expression : str
            Rectangle attributes expression string.
        """
        from apysc._display import graphics_expression
        from apysc._display.graphics import Graphics
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
