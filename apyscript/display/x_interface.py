"""Class implementation for x position.
"""

from apyscript.validation import number_validation


class XInterface:

    _x: int

    @property
    def x(self) -> int:
        """
        Get x position.

        Returns
        -------
        x : int
            X position.
        """
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        """
        Update x position.

        Parameters
        ----------
        value : int
            X potision value.
        """
        number_validation.validate_integer(integer=value)
        self._x = value
