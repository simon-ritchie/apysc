"""2-dimensional geometry point class implementation.
"""

from typing import Union
from apysc import Int

_int = Union[int, Int]


class Point2D:

    _x: Int
    _y: Int

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
        if isinstance(x, int):
            x = Int(x)
        if isinstance(y, int):
            y = Int(y)
        self._x = x
        self._y = y

    @property
    def x(self) -> Int:
        """
        X-coordinate property.

        Returns
        -------
        x : Int
            X-coordinate.
        """
        return self._x

    @property
    def y(self) -> Int:
        """
        Y-coordinate property.

        Parameters
        ----------
        y : Int
            Y-coordinate.
        """
        return self._y
