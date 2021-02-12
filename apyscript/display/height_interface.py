"""Class implementation for height.
"""

from apyscript.converter import cast
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
        value = cast.to_int_from_float(int_or_float=value)
        size_validation.validate_size_is_int(size=value)
        size_validation.validate_size_is_gte_zero(size=value)
        self._height = value
