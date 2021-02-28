"""Class implementation for x position interface.
"""

from apyscript.expression import expression_file_util
from apyscript.type import value_util
from apyscript.type.int import Int
from apyscript.type.number_value_interface import NumberValueInterface
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import number_validation


class XInterface(VariableNameInterface):

    _x: Int

    @property
    def x(self) -> Int:
        """
        Get x position.

        Returns
        -------
        x : Int
            X position.
        """
        return value_util.get_copy(value=self._x)

    @x.setter
    def x(self, value: Int) -> None:
        """
        Update x position.

        Parameters
        ----------
        value : int or Int
            X potision value.
        """
        if not isinstance(value, NumberValueInterface):
            number_validation.validate_integer(integer=value)
            value = Int(value=value)
        self._x = value
        self._append_x_update_expression()

    def _append_x_update_expression(self) -> None:
        """
        Append x position updating expression.
        """
        value_str: str = value_util.get_value_str_for_expression(
            value=self._x)
        expression: str = (
            f'{self.variable_name}.x({value_str});'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
