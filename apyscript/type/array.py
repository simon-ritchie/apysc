"""Class implementation for array.
"""

from apyscript.expression import expression_variables_util
from typing import Any, List, Union
from apyscript.type.copy_interface import CopyInterface


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
