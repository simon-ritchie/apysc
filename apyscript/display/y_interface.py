"""Class implementation for y position.
"""

from apyscript.validation import digit_validation


class YInterface:

    _y: int

    @property
    def y(self) -> int:
        """
        Get y position.

        Returns
        -------
        y : int
            Y position.
        """
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        """
        Update y position.

        Parameters
        ----------
        value : int
            Y position value.
        """
        digit_validation.validate_integer(integer=value)
        self._y = value
