"""Class implementation for array.
"""

from apyscript.type.variable_name_interface import VariableNameInterface
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

    def append(self, value: Any) -> None:
        """
        Add any value to the end of this array.
        This behaves same as push method.

        Parameters
        ----------
        value : *
            Any value to append.
        """
        self._value.append(value)
        self._append_push_and_append_expression(value=value)

    def push(self, value: Any) -> None:
        """
        Add any value to the end of this array.
        This behaves same as append method.

        Parameters
        ----------
        value : *
            Any value to append.
        """
        self.append(value=value)

    def _append_push_and_append_expression(self, value: Any) -> None:
        """
        Append push and append method expression to file.

        Parameters
        ----------
        value : *
            Any value to append.
        """
        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = (
            f'{self.variable_name}.push({value_str});'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def extend(self, other_arr: Union[List[Any], tuple, Any]) -> None:
        """
        Concatenate argument array to this one. Argument array's
        values will positioned after this array's values.
        This method is similar to concat method, but there is a
        difference in whether the same variable will be
        updated (extend) or returned as a different variable (concat).

        Parameters
        ----------
        other_arr : list or tuple or Array
            Other array-like value to concatenate.
        """
        self._validate_acceptable_value_type(value=other_arr)
        if isinstance(other_arr, Array):
            self._value.extend(other_arr.value)
        else:
            self._value.extend(other_arr)
        self._append_extend_expression(other_arr=other_arr)

    def _append_extend_expression(
            self, other_arr: Union[List[Any], tuple, Any]) -> None:
        """
        Append extend method expression to file.

        Parameters
        ----------
        other_arr : list or tuple or Array
            Other array-like value to concatenate.
        """
        value_str: str = value_util.get_value_str_for_expression(
            value=other_arr)
        expression: str = (
            f'{self.variable_name} = {self.variable_name}'
            f'.concat({value_str});')
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def concat(self, other_arr: Union[List[Any], tuple, Any]) -> Any:
        """
        Concatenate arugment array to this one. Argument array's
        values will positioned after this array's values.
        This method is similar to extend method, but there is a
        difference in whether the same variable will be
        updated (extend) or returned as a different variable (concat).

        Parameters
        ----------
        other_arr : list or tuple or Array
            Other array-like value to concatenate.

        Returns
        -------
        concatenated : Array
            Concatenated array value.
        """
        concatenated: Array = self._copy()
        concatenated.extend(other_arr)
        self._append_concat_expression(
            concatenated=concatenated, other_arr=other_arr)
        return concatenated

    def _append_concat_expression(
            self, concatenated: VariableNameInterface,
            other_arr: Union[List[Any], tuple, Any]) -> None:
        """
        Append concat method expression to file.

        Parameters
        ----------
        concatenated : Array
            Concatenated array value.
        other_arr : list or tuple or Array
            Other array-like value to concatenate.
        """
        value_str: str = value_util.get_value_str_for_expression(
            value=other_arr)
        expression: str = (
            f'var {concatenated.variable_name} = '
            f'{self.variable_name}.concat({value_str});'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
