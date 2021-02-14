"""Implementations for Graphics class.
"""

from typing import Any
from typing import List

from apyscript.display.begin_fill_interface import BiginFillInterface
from apyscript.display.line_style_interface import LineStyleInterface
from apyscript.display.graphic_base import GraphicBase
from apyscript.display.rectangle import Rectangle
from apyscript.display.rectangle import append_draw_rect_expression
from apyscript.validation import display_validation


class Graphics(BiginFillInterface, LineStyleInterface):

    _graphics: List[GraphicBase]

    def __init__(self, parent: Any) -> None:
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
            parent=self, x=x, y=y, width=width, height=height)
        self._graphics.append(rectangle)
        append_draw_rect_expression(rectangle=rectangle)
        return rectangle
