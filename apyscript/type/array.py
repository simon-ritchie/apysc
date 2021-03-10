"""Class implementation for array.
"""

from typing import Any, List, Union

from apyscript.expression import expression_file_util
from apyscript.expression import expression_variables_util
from apyscript.type.copy_interface import CopyInterface
from apyscript.type import value_util


class Array(CopyInterface):

    _initial_value: Union[List[Any], tuple, Any]
    _value: List[Any]

    def __init__(self, value: Union[List[Any], tuple, Any]) -> None:
        """
        Array class for apyscript library.

        Parameters
        ----------
        value : list or tuple or Array
            Initial array value.
        """
        TYPE_NAME: str = 'array'
        self._validate_acceptable_value_type(value=value)
        self._initial_value = value
        self._type_name = TYPE_NAME
        self._value = self._get_list_value(value=value)
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=TYPE_NAME)
        self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        expression: str = f'var {self.variable_name} = '
        if isinstance(self._initial_value, Array):
            expression += f'{self._initial_value.variable_name};'
        else:
            value_str: str = value_util.get_value_str_for_expression(
                value=self._value)
            expression += f'{value_str};'
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def _get_list_value(
            self, value: Union[List[Any], tuple, Any]) -> List[Any]:
        """
        Get a list value from specified list, tuple, or Array value.

        Parameters
        ----------
        value : list or tuple or Array
            Specified list, tuple, or Array value.

        Returns
        -------
        list_val : list
            Converted list value.
        """
        if isinstance(value, tuple):
            return list(value)
        if isinstance(value, Array):
            return value._value
        return value

    def _validate_acceptable_value_type(
            self, value: Union[List[Any], tuple, Any]) -> None:
        """
        Validate that specified value is acceptable type or not.

        Parameters
        ----------
        value : list or tuple or Array
            Iterable value to check.

        Raises
        ------
        ValueError
            If specified value's type is not list, tuple, or Array.
        """
        if isinstance(value, (list, tuple, Array)):
            return
        raise ValueError(
            'Not acceptable value\'s type is specified.'
            f'\nSpecified value type: {type(value)}'
            '\nAcceptable types: list, tuple, and Array')

    @property
    def value(self) -> Union[List[Any], tuple, Any]:
        """
        Get a current array value.

        Returns
        -------
        value : list
            Current array value.
        """
        return self._value

    @value.setter
    def value(self, value: Union[List[Any], tuple, Any]) -> None:
        """
        Set array value.

        Parameters
        ----------
        value : list or tuple or Array
            Iterable value (list, tuple, or Array) to set.
        """
        self._validate_acceptable_value_type(value=value)
        self._value = self._get_list_value(value=value)
        self._append_value_setter_expression(value=value)

    def _append_value_setter_expression(
            self, value: Union[List[Any], tuple, Any]) -> None:
        """
        Append value's setter expression to file.

        Parameters
        ----------
        value : list or tuple or Array
            Iterable value (list, tuple, or Array) to set.
        """
        expression: str = f'{self.variable_name} = '
        if isinstance(value, Array):
            expression += f'{value.variable_name};'
        else:
            value_str: str = value_util.get_value_str_for_expression(
                value=value)
            expression += f'{value_str};'
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
