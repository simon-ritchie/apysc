"""Class implementation for graphic base class.
"""

from typing import Any
from typing import Union

from apysc import Int
from apysc.display.display_object import DisplayObject

_Graphics = Any


class GraphicBase(DisplayObject):

    _variable_name: str

    def __init__(
            self, parent: _Graphics,
            x: Union[int, Int],
            y: Union[int, Int],
            variable_name: str) -> None:
        """
        Vector graphic base class.

        Parameters
        ----------
        parent : Graphics
            Parent `Graphics` instance.
        x : int or Int
            X position.
        y : int or Int
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
        if isinstance(x, int):
            x = Int(x)
        self._x = x
        if isinstance(y, int):
            y = Int(y)
        self._y = y
        string_validation.validate_not_empty_string(string=variable_name)
        self._variable_name = variable_name
