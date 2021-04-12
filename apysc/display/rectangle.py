"""Implementations of Rectangle class and other interfaces.
"""

from typing import Any
from typing import Union

from apysc import Int
from apysc import Number
from apysc import String
from apysc.display.fill_alpha_interface import FillAlphaInterface
from apysc.display.fill_color_interface import FillColorInterface
from apysc.display.graphic_base import GraphicBase
from apysc.display.height_interface import HeightInterface
from apysc.display.line_alpha_interface import LineAlphaInterface
from apysc.display.line_color_interface import LineColorInterface
from apysc.display.line_thickness_interface import LineThicknessInterface
from apysc.display.width_interface import WidthInterface
from apysc.event.click_interface import ClickInterface


class Rectangle(
        GraphicBase, WidthInterface, HeightInterface, FillColorInterface,
        FillAlphaInterface, LineColorInterface, LineThicknessInterface,
        LineAlphaInterface, ClickInterface):

    def __init__(
            self, parent: Any,
            x: Union[int, Int],
            y: Union[int, Int],
            width: Union[int, Int],
            height: Union[int, Int],
            fill_color: Union[String, str] = '',
            fill_alpha: Union[float, Number] = 1.0,
            line_color: Union[str, String] = '',
            line_thickness: Union[int, Int] = 1,
            line_alpha: Union[float, Number] = 1.0) -> None:
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
        fill_color : str or None, default None
            Fill color (hexadecimal string, e.g., '#00aaff').
        fill_alpha : float or Number, default 1.0
            Fill opacity (0.0 to 1.0).
        line_color : str or None, default None
            Line color (hexadecimal string, e.g., '#00aaff').
        line_thickness : int or Int, default 1
            Line thickness (width).
        line_alpha : float or Number, default 1.0
            Line opacity (0.0 to 1.0).
        """
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        from apysc.validation import size_validation
        variable_name: str = expression_variables_util.\
            get_next_variable_name(type_name=var_names.RECTANGLE)
        super(Rectangle, self).__init__(
            parent=parent,
            x=Int(x),
            y=Int(y),
            variable_name=variable_name)
        size_validation.validate_size_is_gte_zero(size=width)
        size_validation.validate_size_is_gte_zero(size=height)
        self.update_width_and_skip_appending_exp(value=Int(width))
        self.update_height_and_skip_appending_exp(value=Int(height))
        if fill_color != '':
            if isinstance(fill_color, str):
                fill_color = String(fill_color)
            self.update_fill_color_and_skip_appending_exp(
                value=fill_color)
        self.update_fill_alpha_and_skip_appending_exp(value=fill_alpha)
        if line_color != '':
            if isinstance(line_color, str):
                line_color = String(line_color)
            self.update_line_color_and_skip_appending_exp(value=line_color)
        self.update_line_thickness_and_skip_appending_exp(
            value=Int(line_thickness))
        self.update_line_alpha_and_skip_appending_exp(
            value=Number(line_alpha))


def append_draw_rect_expression(rectangle: Rectangle) -> None:
    """
    Append Graphics's draw_rect interface expression to the file.

    Parameters
    ----------
    rectangle : Rectanble
        Created rectangle instance.
    """
    from apysc.display.stage import get_stage_variable_name
    from apysc.expression import expression_file_util
    variable_name: str = rectangle.variable_name
    stage_variable_name: str = get_stage_variable_name()
    expression: str = (
        f'\nvar {variable_name} = {stage_variable_name}'
        f'\n  .rect({rectangle.width.variable_name}, '
        f'{rectangle.height.variable_name})'
    )
    attrs_str: str = _make_rect_attrs_expression(rectangle=rectangle)
    expression += f'{attrs_str};'
    expression_file_util.append_js_expression(expression=expression)


def _make_rect_attrs_expression(rectangle: Rectangle) -> str:
    """
    Make rectangle attributes expression string.

    Parameters
    ----------
    rectangle : Rectangle
        Target rectangle instance.

    Returns
    -------
    rect_attrs_expression : str
        Rectangle attributes expression string.
    """
    from apysc.display import graphics_expression
    from apysc.display.graphics import Graphics
    graphics: Graphics = rectangle.parent_graphics
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
        graphic=rectangle, expression=rect_attrs_expression,
        indent_num=INDENT_NUM)
    rect_attrs_expression = graphics_expression.append_y_expression(
        graphic=rectangle, expression=rect_attrs_expression,
        indent_num=INDENT_NUM)

    rect_attrs_expression += '\n  })'
    return rect_attrs_expression
