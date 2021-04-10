"""Class implementation of any value.
"""

from typing import Any

from apysc.type.variable_name_interface import VariableNameInterface


class AnyValue(VariableNameInterface):

    _value: Any

    def __init__(self, value: Any) -> None:
        """
        Class implementation of any value (value that can't determine
        type).

        Parameters
        ----------
        value : *
            Initial any value.
        """
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        self._value = value
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=var_names.ANY)
        self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        from apysc.expression import expression_file_util
        expression: str = f'var {self.variable_name} = '
        if isinstance(self._value, VariableNameInterface):
            expression += f'{self._value.variable_name};'
        else:
            expression += f'{self._value};'
        expression_file_util.append_js_expression(expression=expression)

    @property
    def value(self) -> Any:
        """
        Get a current value.

        Returns
        -------
        value : *
            Any value.
        """
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        """
        Set a any value.

        Parameters
        ----------
        value : *
            Any value to set.
        """
        self._value = value
        self._append_value_setter_expression(value=value)

    def _append_value_setter_expression(self, value: Any) -> None:
        """
        Append value's setter expression to file.

        Parameters
        ----------
        value : *
            Any value to set.
        """
        from apysc.expression import expression_file_util
        expression: str = f'{self.variable_name} = '
        if isinstance(value, VariableNameInterface):
            expression += f'{value.variable_name};'
        else:
            expression += f'{value};'
        expression_file_util.append_js_expression(expression=expression)
