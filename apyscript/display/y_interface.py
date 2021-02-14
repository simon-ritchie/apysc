"""Class implementation for y position.
"""

from apyscript.validation import number_validation
from apyscript.display.variable_name_interface import VariableNameInterface


class YInterface(VariableNameInterface):

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
        number_validation.validate_integer(integer=value)
        self._y = value
