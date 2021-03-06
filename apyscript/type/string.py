"""Class implementation for string.
"""

from typing import Any, Union
from apyscript.expression import expression_file_util
from apyscript.expression import expression_variables_util
from apyscript.type.copy_interface import CopyInterface
from apyscript.validation import string_validation
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.type.value_util import get_value_str_for_expression
from apyscript.validation import number_validation


class String(CopyInterface):

    _initial_value: Union[str, Any]
    _value: str

    def __init__(self, value: Union[str, Any]) -> None:
        """
        String class for apyscript library.

        Parameters
        ----------
        value : str or String
            Initial string value.
        """
        TYPE_NAME: str = 'string'
        string_validation.validate_string_type(string=value)
        self._initial_value = value
        self._type_name = TYPE_NAME
        self._value = self._get_str_value(value=value)
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=TYPE_NAME)
        self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        expression: str = f'var {self.variable_name} = '
        if isinstance(self._initial_value, String):
            expression += f'{self._initial_value.variable_name};'
        else:
            expression += f'"{self._value}";'
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def _get_str_value(self, value: Union[str, Any]) -> str:
        """
        Get a (Python's) str value from specified value.

        Parameters
        ----------
        value : str or String
            Target string value.

        Returns
        -------
        value : str
            Python's builtin str value.
        """
        if isinstance(value, String):
            return value._value
        return value

    @property
    def value(self) -> Union[str, Any]:
        """
        Get current string value.

        Returns
        -------
        value : str
            Current string value.
        """
        return self._value

    @value.setter
    def value(self, value: Union[str, Any]) -> None:
        """
        Set string value.

        Parameters
        ----------
        value : str or String
            Any string value to set.
        """
        string_validation.validate_string_type(string=value)
        self._value = self._get_str_value(value=value)
        self._append_value_setter_expression(value=value)

    def _append_value_setter_expression(
            self, value: Union[str, Any]) -> None:
        """
        Append value's setter expression to file.

        Parameters
        ----------
        value : str or String
            Any string value to set.
        """
        expression: str = f'{self.variable_name} = '
        if isinstance(value, String):
            expression += f'{value.variable_name};'
        else:
            expression += f'"{value}";'
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def __add__(self, other: Union[str, Any]) -> Any:
        """
        Method for addition (string concatenation).

        Parameters
        ----------
        other : str or String
            Other string value to concatenate.

        Returns
        -------
        result : String
            Concatenated result string.
        """
        string_validation.validate_string_type(string=other)
        if isinstance(other, String):
            value: str = self._value + other.value
        else:
            value = self._value + other
        result: String = self._copy()
        result._value = value
        self._append_addition_expression(result=result, other=other)
        return result

    def _append_addition_expression(
            self, result: VariableNameInterface,
            other: Union[str, Any]) -> None:
        """
        Append addition (string concatenation) expression to file.

        Parameters
        ----------
        result : String
            Addition result value.
        other : str or String
            Other string value to concatenate.
        """
        right_value: str = get_value_str_for_expression(value=other)
        expression: str = (
            f'var {result.variable_name} = '
            f'{self.variable_name} + {right_value};'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def __mul__(self, other: Union[int, Any]) -> Any:
        """
        Method for multiplication (string repetition).

        Parameters
        ----------
        other : int or Int
            String repetition number.

        Returns
        -------
        result : String
            Repeated result string.
        """
        from apyscript.type import Int
        number_validation.validate_integer(integer=other)
        if isinstance(other, Int):
            value: int = other.value  # type: ignore
        else:
            value = other
        result: String = self._copy()
        result._value = result._value * value
        self._append_multiplication_expression(result=result, other=other)
        return result

    def _append_multiplication_expression(
            self, result: VariableNameInterface,
            other: Union[int, Any]) -> None:
        """
        Append multiplication (string repetition) expression to file.

        Parameters
        ----------
        result : String
            Multiplication result value.
        other : int or Int
            String repetition number.
        """
        from apyscript.type import Int
        expression: str = f'var {result.variable_name} = "";'
        expression += '\nfor (var i = 0; i < '
        if isinstance(other, Int):
            expression += f'{other.variable_name}'
        else:
            expression += f'{other}'
        expression += '; i++) {'
        expression += f'\n  {result.variable_name} += {self.variable_name};'
        expression += '\n}'
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
