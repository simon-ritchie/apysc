"""Class implementation for height.
"""

from apyscript.validation import size_validation


class HeightInterface:

    _height: int

    @property
    def height(self) -> int:
        """
        Get this instance's height.

        Parameters
        ----------
        height : int
            This instance's height.
        """
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        size_validation.validate_size_is_gte_zero(size=value)
        self._height = value
