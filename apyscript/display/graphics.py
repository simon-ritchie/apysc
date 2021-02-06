"""Implementations for Graphics class.
"""

from typing import List, Optional
from apyscript.color import color_util
from apyscript.display.display_object import DisplayObject


class _GraphicBase:

    _x: int
    _y :int

    def __init__(self, parent, x: int, y: int) -> None:
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
        """
        self.parent: Graphics = parent
        self._x = x
        self._y = y


class Graphics:

    _fill_color: Optional[str] = None
    _graphics: List[_GraphicBase]
    parent: DisplayObject

    def __init__(self, parent: DisplayObject) -> None:
        """
        Create a object that has each vector graphics interface.
        """
        self.parent = parent
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
        pass


class Rectangle(_GraphicBase):

    parent: Graphics
    width: int
    height: int

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
        super(Rectangle, self).__init__(parent=parent, x=x, y=y)
        self.width = width
        self.height = height
