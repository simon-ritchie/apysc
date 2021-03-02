"""Class implementation for y position interface.
"""

from apyscript.expression import expression_file_util
from apyscript.type import Int
from apyscript.type import value_util
from apyscript.type.number_value_interface import NumberValueInterface
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import number_validation


class YInterface(VariableNameInterface):

    _y: Int

    @property
    def y(self) -> Int:
        """
        Get y position.

        Returns
        -------
        y : Int
            Y position.
        """
        return value_util.get_copy(value=self._y)

    @y.setter
    def y(self, value: Int) -> None:
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
        value_str: str = value_util.get_value_str_for_expression(
            value=self._y)
        expression: str = (
            f'{self.variable_name}.y({value_str});'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
