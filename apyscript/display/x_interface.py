"""Class implementation for x position interface.
"""

from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import number_validation


class XInterface(VariableNameInterface):

    _x: int = 0

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
        Append x position updating expression.
        """
        expression: str = (
            f'{self.variable_name}.x({self.x});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)
