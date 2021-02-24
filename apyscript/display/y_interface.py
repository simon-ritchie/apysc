"""Class implementation for y position interface.
"""

from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import number_validation


class YInterface(VariableNameInterface):

    _y: int = 0

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
        self._append_y_update_expression()

    def _append_y_update_expression(self) -> None:
        """
        Append y position updating expression.
        """
        expression: str = (
            f'{self.variable_name}.y({self.y});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)
