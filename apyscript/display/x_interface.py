"""Class implementation for x position.
"""

from apyscript.validation import number_validation
from apyscript.display.variable_name_interface import VariableNameInterface
from apyscript.expression import expression_file_util


class XInterface(VariableNameInterface):

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
        self._append_x_update_expression()

    def _append_x_update_expression(self) -> None:
        """
        Append x position updating expression to current scope.
        """
        expression: str = (
            f'{self.variable_name}.x({self.x});'
        )
        expression_file_util.append_expression_to_current_scope(
            expression=expression)
