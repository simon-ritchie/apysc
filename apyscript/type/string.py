"""Class implementation for string.
"""

from typing import Any, Union
from apyscript.expression import expression_file_util
from apyscript.expression import expression_variables_util
from apyscript.type.copy_interface import CopyInterface
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import string_validation


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
