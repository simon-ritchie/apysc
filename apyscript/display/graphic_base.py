"""Class implementation for graphic base class.
"""

from typing import Any

from apyscript.display.x_interface import XInterface
from apyscript.display.y_interface import YInterface
from apyscript.validation import display_validation
from apyscript.validation import number_validation
from apyscript.validation import string_validation
from apyscript.display.parent_interface import ParentInterface


class GraphicBase(XInterface, YInterface, ParentInterface):

    _variable_name: str

    def __init__(
            self, parent: Any, x: int, y: int, variable_name: str) -> None:
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
        from apyscript.display.graphics import Graphics
        display_validation.validate_graphics(graphics=parent)
        self.parent: Graphics = parent
        number_validation.validate_integer(integer=x)
        number_validation.validate_integer(integer=y)
        self._x = x
        self._y = y
        string_validation.validate_not_empty_string(string=variable_name)
        self._variable_name = variable_name
