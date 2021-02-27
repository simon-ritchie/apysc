"""Class implementation for y position interface.
"""

from apyscript.type.number_value_interface import NumberValueInterface
from apyscript.type.int import Int
from typing import Union
from apyscript.expression import expression_file_util
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import number_validation


class YInterface(VariableNameInterface):

    _y: Union[int, Int] = Int(value=0)

    @property
    def y(self) -> Union[int, Int]:
        """
        Get y position.

        Returns
        -------
        y : Int
            Y position.
        """
        return self._y

    @y.setter
    def y(self, value: Union[int, Int]) -> None:
        """
        Update y position.

        Parameters
        ----------
        value : int or Int
            Y position value.
        """
        if not isinstance(value, NumberValueInterface):
            number_validation.validate_integer(integer=value)
            value = Int(value=value)
        self._y = value
        self._append_y_update_expression()

    def _append_y_update_expression(self) -> None:
        """
        Append y position updating expression.
        """
        expression: str = (
            f'{self.variable_name}.y({self.y});'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
