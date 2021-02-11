"""Implementations for Graphics class.
"""

from typing import List, Optional
from apyscript.color import color_util
from apyscript.display.display_object import DisplayObject
from apyscript.expression import scope_variables_util
from apyscript.expression import expression_file_util
from apyscript.validation import digit_validation
from apyscript.validation import string_validation
from apyscript.validation import size_validation
from apyscript.validation import display_validation
from apyscript.display.variable_name_interface import VariableNameInterface
from apyscript.display.x_interface import XInterface
from apyscript.display.y_interface import YInterface
from apyscript.display.width_interface import WidthInterface
from apyscript.display.height_interface import HeightInterface
from apyscript.display.stage import get_stage_variable_name
from apyscript.html import html_const


class _GraphicBase(VariableNameInterface, XInterface, YInterface):

    _variable_name: str

    def __init__(
            self, parent, x: int, y: int, variable_name: str) -> None:
        """
        Vector graphic base class.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        x : int
            X position.
        y : int
            Y position.
        variable_name : str
            Variable name of this instance. This will be used to
            js expression.
        """
        display_validation.validate_graphics(graphics=parent)
        self.parent: Graphics = parent
        digit_validation.validate_integer(integer=x)
        digit_validation.validate_integer(integer=y)
        self._x = x
        self._y = y
        string_validation.validate_not_empty_string(string=variable_name)
        self._variable_name = variable_name


class Graphics:

    _fill_color: Optional[str] = None
    _graphics: List[_GraphicBase]

    def __init__(self, parent) -> None:
        """
        Create a object that has each vector graphics interface.

        Parameters
        ----------
        parent : Sprite
            This instance's parent instance.
        """
        from apyscript.display.sprite import Sprite
        display_validation.validate_sprite(sprite=parent)
        self.parent: Sprite = parent
        self._graphics = []

    def begin_fill(self, color: str) -> None:
        """
        Set single color value for fill.

        Parameters
        ----------
        color : str
            Hexadecimal color string. e.g., '#00aaff'
        """
        color = color_util.complement_hex_color(hex_color_code=color)
        self._fill_color = color

    def draw_rect(self, x: int, y: int, width: int, height: int) -> None:
        """
        Draw rectangle vector graphics.

        Parameters
        ----------
        x : int
            X position to start drawing.
        y : int
            Y position to start drawing.
        width : int
            Rectangle width.
        height : int
            Rectangle height.
        """
        rectangle: Rectangle = Rectangle(
            parent=self, x=x, y=y, width=width, height=height)
        self._graphics.append(rectangle)
        _append_draw_rect_expression(rectangle=rectangle)


class Rectangle(_GraphicBase, WidthInterface, HeightInterface):

    parent: Graphics

    def __init__(
            self, parent: Graphics,
            x: int, y: int, width: int, height: int) -> None:
        """
        Create a rectangle vector graphic.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        x : int
            X position to start drawing.
        y : int
            Y position to start drawing.
        width : int
            Rectangle width.
        height : int
            Rectangle height.
        """
        variable_name: str = scope_variables_util.\
            get_current_scope_next_variable_name(type_name='rectangle')
        super(Rectangle, self).__init__(
            parent=parent, x=x, y=y, variable_name=variable_name)
        size_validation.validate_size_is_gte_zero(size=width)
        size_validation.validate_size_is_gte_zero(size=height)
        self.width = width
        self.height = height


def _append_draw_rect_expression(rectangle: Rectangle) -> None:
    """
    Append Graphics's draw_rect interface expression to the file
    of current scope.

    Parameters
    ----------
    rectangle : Rectanble
        Created rectangle instance.
    """
    variable_name: str = rectangle.variable_name
    stage_variable_name: str = get_stage_variable_name()
    expression: str = (
        f'{html_const.SCRIPT_START_TAG}'
        f'\nvar {variable_name} = {stage_variable_name}'
        f'\n  .rect({rectangle.width}, {rectangle.height})'
    )
    attrs_str: str = _make_rect_attrs_expression(rectangle=rectangle)
    expression += f'{attrs_str};'
    expression += f'\n{html_const.SCRIPT_END_TAG}'
    expression_file_util.append_expression_to_current_scope(
        expression=expression)


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
    graphics: Graphics = rectangle.parent
    rect_attrs_expression: str = '\n  .attr({'
    if graphics._fill_color is not None:
        rect_attrs_expression += (
            f'\n    fill: "{graphics._fill_color}",'
        )
    rect_attrs_expression += '\n  })'
    return rect_attrs_expression
