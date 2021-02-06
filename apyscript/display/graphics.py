"""Implementations for Graphics class.
"""

from typing import Optional
from apyscript.color import color_util
from apyscript.display.display_object import DisplayObject


class Graphics:

    _fill_color: Optional[str]
    parent: DisplayObject

    def __init__(self, parent: DisplayObject) -> None:
        """
        Create a object that has each vector graphics interface.
        """
        self.parent = parent

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
