"""Class implementation for array.
"""

from apyscript.type.variable_name_interface import VariableNameInterface
from typing import Any, List, Optional, Union

from apyscript.expression import expression_file_util
from apyscript.expression import expression_variables_util
from apyscript.type.copy_interface import CopyInterface
from apyscript.type import value_util
from apyscript.validation import number_validation


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

    def insert(
            self, index: Union[int, Any], value: Any) -> None:
        """
        Insert value to this array at a specified index.
        This behaves same as insert_at method.

        Parameters
        ----------
        index : int or Int
            Index to append value to.
        value : *
            Any value to append.
        """
        number_validation.validate_integer(integer=index)
        from apyscript.type import Int
        if isinstance(index, Int):
            index_: int = int(index.value)
        else:
            index_ = index
        if isinstance(value, Int):
            value_: int = int(value.value)
        else:
            value_ = value
        self._value.insert(index_, value_)
        self._append_insert_expression(index=index, value=value)

    def insert_at(self, index: Union[int, Any], value: Any) -> None:
        """
        Insert value to this array at a specified index.
        This behaves same as insert method.

        Parameters
        ----------
        index : int or Int
            Index to append value to.
        value : *
            Any value to append.
        """
        self.insert(index=index, value=value)

    def _append_insert_expression(
            self, index: Union[int, Any], value: Any) -> None:
        """
        Append insert method expression to file.

        Parameters
        ----------
        index : int or Int
            Index to append value to.
        value : *
            Any value to append.
        """
        value_str: str = value_util.get_value_str_for_expression(value=value)
        index_str: str = value_util.get_value_str_for_expression(value=index)
        expression: str = (
            f'{self.variable_name}.splice({index_str}, 0, {value_str});'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def pop(self) -> Any:
        """
        Remove this array's last value and return it.

        Returns
        -------
        value : *
            Removed value.
        """
        value: Any = self._value.pop()
        self._append_pop_expression(value=value)
        return value

    def _append_pop_expression(self, value: Any) -> Any:
        """
        Append pop method expression to file.

        Parameters
        ----------
        value : *
            Removed value.
        """
        expression: str = f'{self.variable_name}.pop();'
        if isinstance(value, VariableNameInterface):
            expression = f'{value.variable_name} = {expression}'
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def remove(self, value: Any) -> None:
        """
        Remove specified value from this array.

        Parameters
        ----------
        value : Any
            Value to remove.
        """
        self._value.remove(value)
        self._append_remove_expression(value=value)

    def _append_remove_expression(self, value: Any) -> None:
        """
        Append remove method expression to file.

        Parameters
        ----------
        value : Any
            Value to remove.
        """
        index_var_name: str = expression_variables_util.\
            get_next_variable_name(type_name='index')
        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = (
            f'var {index_var_name} = _.indexOf'
            f'({self.variable_name}, {value_str});'
            f'\n{self.variable_name}.splice({index_var_name}, 1);')
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def remove_at(self, index: Union[int, Any]) -> None:
        """
        Remove specified index value from this array.

        Parameters
        ----------
        index : int or Int
            Index to remove value.
        """
        number_validation.validate_integer(integer=index)
        from apyscript.type import Int
        if isinstance(index, Int):
            index_: int = int(index.value)
        else:
            index_ = index
        del self._value[index_]
        self._append_remove_at_expression(index=index)

    def _append_remove_at_expression(self, index: Union[int, Any]) -> None:
        """
        Append remove_at method expression to file.

        Parameters
        ----------
        index : int or Int
            Index to remove value.
        """
        index_str: str = value_util.get_value_str_for_expression(value=index)
        expression: str = (
            f'{self.variable_name}.splice({index_str}, 1);'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def reverse(self) -> None:
        """
        Reverse this array in place.
        """
        self._value.reverse()
        self._append_reverse_expression()

    def _append_reverse_expression(self) -> None:
        """
        Append reverse method expression to file.
        """
        expression: str = (
            f'{self.variable_name}.reverse();'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def sort(self, ascending: bool = True) -> None:
        """
        Sort this array in place.

        Parameters
        ----------
        ascending : bool, default True
            Sort by ascending or not. If False is specified,
            values will be descending.
        """
        self._value.sort()
        self._append_sort_expression()
        if not ascending:
            self.reverse()

    def _append_sort_expression(self) -> None:
        """
        Append sort method expression to file.
        """
        expression: str = (
            f'{self.variable_name}.sort();'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def slice(
            self,
            start: Optional[Union[int, Any]] = None,
            end: Optional[Union[int, Any]] = None) -> Any:
        """
        Slice this array by specified start and end indexes.

        Parameters
        ----------
        start : int or Int or None, default None
            Slicing start index.
        end : int or Int or None, default None
            Slicing end index (this index will not be including).

        Returns
        -------
        sliced_arr : Array
            Sliced array.

        Examples
        --------
        >>> arr: Array = Array([1, 2, 3, 4])
        >>> arr.slice(1, 3)
        [2, 3]

        >>> arr.slice(1)
        [2, 3, 4]

        >>> arr.slice(end=2)
        [1, 2]
        """
        from apyscript.type import Int
        if isinstance(start, Int):
            start_: Optional[int] = int(start.value)
        else:
            start_ = start
        if isinstance(end, Int):
            end_: Optional[int] = int(end.value)
        else:
            end_ = end
        sliced_arr: Array = self._copy()
        sliced_arr._value = self._value[slice(start_, end_)]
        self._append_slice_expression(
            sliced_arr=sliced_arr, start=start, end=end)
        return sliced_arr

    def _append_slice_expression(
            self,
            sliced_arr: VariableNameInterface,
            start: Optional[Union[int, Any]],
            end: Optional[Union[int, Any]]) -> None:
        """
        Append slice method expression to file.

        Parameters
        ----------
        sliced_arr : Array
            Sliced array.
        start : int or Int or None
            Slicing start index.
        end : int or Int or None
            Slicing end index.
        """
        if start is None:
            start = 0
        expression: str = (
            f'var {sliced_arr.variable_name} = '
            f'{self.variable_name}.slice('
            f'{start}'
        )
        if end is not None:
            expression += f', {end}'
        expression += ');'
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def __getitem__(self, index: Union[int, Any]) -> Any:
        """
        Get a specified index single value.

        Parameters
        ----------
        index : int or Int
            Array's index to get value. Currently not supported tuple
            value (e.g., slicing).

        Returns
        -------
        value : *
            Specified index's value.

        Raises
        ------
        ValueError
            If specified index type is not int and Int.
        """
        from apyscript.type import Int
        self._validate_index_type_is_int(index=index)
        if isinstance(index, Int):
            index_: int = int(index.value)
        else:
            index_ = index
        value: Any = self._value[index_]
        self._append_getitem_expression(index=index, value=value)
        return value

    def _validate_index_type_is_int(self, index: Union[int, Any]) -> None:
        """
        Validate whether index value type is int (or Int) or not.

        Parameters
        ----------
        index : int or Int
            Index value to check.

        Raises
        ------
        ValueError
            If index type is not int or Int type.
        """
        from apyscript.type import Int
        if isinstance(index, (int, Int)):
            return
        raise ValueError(
            'Currently indexing is only supported int or Int types.'
            ' If you need to slice array please use slice method.')


    def _append_getitem_expression(
            self, index: Union[int, Any],
            value: Any) -> None:
        """
        Append __getitem__ expression to file.

        Parameters
        ----------
        index : int or Int
            Array's index to get value.
        value : *
            Specified index's value.
        """
        if not isinstance(value, VariableNameInterface):
            return
        index_str: str = value_util.get_value_str_for_expression(
            value=index)
        expression: str = (
            f'var {value.variable_name} = '
            f'{self.variable_name}[{index_str}];'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def __setitem__(self, index: Union[int, Any], value: Any) -> None:
        """
        Set value to a specified index.

        Parameters
        ----------
        index : int or Int
            Array's index to set value. Currently not supported tuple
            value (e.g., slicing).
        """
