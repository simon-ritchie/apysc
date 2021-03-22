"""Class implementation for x position interface.
"""

from apyscript.type import Int
from apyscript.type.number_value_interface import NumberValueInterface
from apyscript.type.variable_name_interface import VariableNameInterface


class XInterface(VariableNameInterface):

    _x: Int

    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize _x attribute if it is not initialized yet.
        """
        if hasattr(self, '_x'):
            return
        self._x = Int(0)

    @property
    def x(self) -> Int:
        """
        Get x position.

        Returns
        -------
        x : Int
            X position.
        """
        from apyscript.type import value_util
        self._initialize_x_if_not_initialized()
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
        from apyscript.validation import number_validation
        if not isinstance(value, NumberValueInterface):
            number_validation.validate_integer(integer=value)
            value = Int(value=value)
        self._x = value
        self._append_x_update_expression()

    def _append_x_update_expression(self) -> None:
        """
        Append x position updating expression.
        """
        from apyscript.expression import expression_file_util
        from apyscript.type import value_util
        self._initialize_x_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._x)
        expression: str = (
            f'{self.variable_name}.x({value_str});'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
