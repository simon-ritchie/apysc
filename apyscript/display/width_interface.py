"""Class implementation for witdth.
"""

from apyscript.validation import size_validation


class WidthInterface:

    _width: int

    @property
    def width(self) -> int:
        """
        Get this instance's width.

        Returns
        -------
        width : int
            This instance's width.
        """
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        """
        Update this instance's width.

        Parameters
        ----------
        value : int
            Width value to set.
        """
        size_validation.validate_size_is_gte_zero(size=value)
        self._width = value
