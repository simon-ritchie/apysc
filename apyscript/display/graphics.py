"""Implementations for Graphics class.
"""

from typing import Any
from typing import List
from typing import Optional

from apyscript.display.begin_fill_interface import BiginFillInterface
from apyscript.display.line_style_interface import LineStyleInterface
from apyscript.display.rectangle import Rectangle
from apyscript.display.rectangle import append_draw_rect_expression
from apyscript.display.variable_name_interface import VariableNameInterface
from apyscript.expression import expression_variables_util
from apyscript.validation import display_validation
from apyscript.display.graphics_clear_interface import GraphicsClearInterface


class Graphics(
        BiginFillInterface, LineStyleInterface, VariableNameInterface,
        GraphicsClearInterface):

    def __init__(
            self, parent: Any, variable_name: Optional[str] = None) -> None:
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
        if variable_name is None:
            variable_name = expression_variables_util.get_next_variable_name(
                type_name='graphics')
        self.variable_name = variable_name

    def draw_rect(
            self, x: int, y: int, width: int, height: int) -> Rectangle:
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

        Returns
        -------
        rectangle : Rectangle
            Created rectangle.
        """
        rectangle: Rectangle = Rectangle(
            parent=self, x=x, y=y, width=width, height=height,
            fill_color=self.fill_color, fill_alpha=self.fill_alpha,
            line_color=self.line_color, line_thickness=self.line_thickness,
            line_alpha=self.line_alpha)
        self._graphics.append(rectangle)
        append_draw_rect_expression(rectangle=rectangle)
        return rectangle
