"""2-dimensional geometry point class implementation.
"""

from typing import Union
from apysc import Int

_int = Union[int, Int]


class Point2D:

    _x: _int
    _y: _int

    def __init__(self, x: _int, y: _int) -> None:
        """
        2-dimensional geometry point.

        Parameters
        ----------
        x : int or Int
            X-coordinate.
        y : int or Int
            Y-coordinate.
        """
        from apysc.validation.number_validation import validate_integer
        validate_integer(integer=x)
        validate_integer(integer=y)
        self._x = x
        self._y = y
