"""Class implementation for y position interface.
"""

from apyscript.type import Int
from apyscript.type.variable_name_interface import VariableNameInterface


class YInterface(VariableNameInterface):

    _y: Int

    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize _y attribute if it is not initialized yet.
        """
        if hasattr(self, '_y'):
            return
        self._y = Int(0)

    @property
    def y(self) -> Int:
        """
        Get y position.

        Returns
        -------
        y : Int
            Y position.
        """
        from apyscript.type import value_util
        self._initialize_y_if_not_initialized()
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
        from apyscript.type.number_value_interface import NumberValueInterface
        from apyscript.validation import number_validation
        if not isinstance(value, NumberValueInterface):
            number_validation.validate_integer(integer=value)
            value = Int(value=value)
        self._y = value
        self._append_y_update_expression()

    def _append_y_update_expression(self) -> None:
        """
        Append y position updating expression.
        """
        from apyscript.expression import expression_file_util
        from apyscript.type import value_util
        self._initialize_y_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._y)
        expression: str = (
            f'{self.variable_name}.y({value_str});'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
