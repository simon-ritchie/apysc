"""Class implementation for graphic base class.
"""

from typing import Any

from apysc import Int
from apysc.display.display_object import DisplayObject


class GraphicBase(DisplayObject):

    _variable_name: str

    def __init__(
            self, parent: Any, x: Int, y: Int, variable_name: str) -> None:
        """
        Vector graphic base class.

        Parameters
        ----------
        parent : Graphics
            Parent `Graphics` instance.
        x : int
            X position.
        y : int
            Y position.
        variable_name : str
            Variable name of this instance. This will be used to
            js expression.
        """
        from apysc.display.graphics import Graphics
        from apysc.validation import display_validation
        from apysc.validation import number_validation
        from apysc.validation import string_validation

        display_validation.validate_graphics(graphics=parent)
        self.parent_graphics: Graphics = parent
        number_validation.validate_integer(integer=x)
        number_validation.validate_integer(integer=y)
        self._x = x
        self._y = y
        string_validation.validate_not_empty_string(string=variable_name)
        self._variable_name = variable_name
