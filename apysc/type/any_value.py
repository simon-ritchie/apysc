"""Class implementation of any value.
"""

from typing import Any

from apysc.type.variable_name_interface import VariableNameInterface
from apysc.type.copy_interface import CopyInterface


class AnyValue(CopyInterface):

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
        TYPE_NAME: str = var_names.ANY
        self._value = value
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=TYPE_NAME)
        self._type_name = TYPE_NAME
        self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        from apysc.expression import expression_file_util
        from apysc.type import value_util
        expression: str = f'var {self.variable_name} = '
        if isinstance(self._value, VariableNameInterface):
            expression += f'{self._value.variable_name};'
        else:
            value_str: str = value_util.get_value_str_for_expression(
                value=self._value)
            expression += f'{value_str};'
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

    def _append_arithmetic_operation_expression(
            self, other: Any, operator: str) -> VariableNameInterface:
        """
        Append arithmetic operation (e.g., addition) expression
        to file.

        Parameters
        ----------
        other : Any
            Other value to use.
        operator : str
            JavaScript arithmetic operator, like '+', '*', and so on.

        Returns
        -------
        result : AnyValue
            Calculated result value.
        """
        from apysc.expression import expression_file_util
        from apysc.type.value_util import get_value_str_for_expression
        value_str: str = get_value_str_for_expression(value=other)
        result: AnyValue = self._copy()
        expression: str = (
            f'var {result.variable_name} = '
            f'{self.variable_name} {operator} {value_str};'
        )
        expression_file_util.append_js_expression(expression=expression)
        return result

    def __add__(self, other: Any) -> VariableNameInterface:
        """
        Method for addition.

        Parameters
        ----------
        other : Any
            Other value to add.

        Returns
        -------
        result : AnyValue
            Addition result value.
        """
        result: VariableNameInterface = \
            self._append_arithmetic_operation_expression(
                other=other, operator='+')
        return result

    def __sub__(self, other: Any) -> VariableNameInterface:
        """
        Method for subtraction.

        Parameters
        ----------
        other : Any
            Other value to subtract.

        Returns
        -------
        result : AnyValue
            Subtraction result value.
        """
        result: VariableNameInterface = \
            self._append_arithmetic_operation_expression(
                other=other, operator='-')
        return result
