"""Class implementation for array.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._event.custom_event_interface import CustomEventInterface
from apysc._type.copy_interface import CopyInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface

T = TypeVar('T')


class Array(
        CopyInterface, RevertInterface, CustomEventInterface, Generic[T]):
    """
    Array class for the apysc library.
    """

    _initial_value: Union[List[Any], tuple, 'Array']
    _value: List[Any]

    def __init__(
            self,
            value: Union[List[T], tuple, range, 'Array']) -> None:
        """
        Array class for the apysc library.

        Parameters
        ----------
        value : list or tuple or range or Array
            Initial array value.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            from apysc._expression.event_handler_scope import \
                TemporaryNotHandlerScope
            with TemporaryNotHandlerScope():
                TYPE_NAME: str = var_names.ARRAY
                self._validate_acceptable_value_type(value=value)
                value = self._convert_range_to_list(value=value)
                value_: Union[List[Any], tuple, 'Array'] = value
                self._initial_value = value_
                self._type_name = TYPE_NAME
                self._value = self._get_list_value(value=value)
                self.variable_name = expression_variables_util.\
                    get_next_variable_name(type_name=TYPE_NAME)
                self._append_constructor_expression()

    def _convert_range_to_list(
            self,
            value: Any) -> Union[List[Any], tuple, 'Array']:
        """
        Convert argument value to list that if specified
        value is range type.

        Parameters
        ----------
        value : list or tuple or range or Array
            Target value.

        Returns
        -------
        value : list or tuple or Array
            Converted value.
        """
        if isinstance(value, range):
            return list(value)
        return value

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            expression: str = f'var {self.variable_name} = '
            if isinstance(self._initial_value, Array):
                expression += f'{self._initial_value.variable_name};'
            else:
                value_str: str = value_util.get_value_str_for_expression(
                    value=self._value)
                expression += f'{value_str};'
            ap.append_js_expression(expression=expression)

    def _get_list_value(
            self, value: Union[List[Any], tuple, 'Array']) -> List[Any]:
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
            self,
            value: Union[List[Any], tuple, range, 'Array']) -> None:
        """
        Validate that specified value is acceptable type or not.

        Parameters
        ----------
        value : list or tuple or range or Array
            Iterable value to check.

        Raises
        ------
        ValueError
            If specified value's type is not list, tuple, or Array.
        """
        if isinstance(value, (list, tuple, range, Array)):
            return
        raise ValueError(
            'Not acceptable value type is specified.'
            f'\nSpecified value type: {type(value)}'
            '\nAcceptable types: list, tuple, range, and Array')

    @property
    def value(self) -> Union[List[Any], tuple, 'Array']:
        """
        Get a current array value.

        Returns
        -------
        value : list
            Current array value.

        References
        ----------
        - apysc basic data classes common value interface
            - https://bit.ly/3Be1aij
        """
        return self._value

    @value.setter
    def value(self, value: Union[List[Any], tuple, 'Array']) -> None:
        """
        Set array value.

        Parameters
        ----------
        value : list or tuple or Array
            Iterable value (list, tuple, or Array) to set.

        References
        ----------
        apysc basic data classes common value interface
            https://bit.ly/3Be1aij
        """
        with ap.DebugInfo(
                callable_='value', locals_=locals(),
                module_name=__name__, class_=Array):
            self._validate_acceptable_value_type(value=value)
            self._value = self._get_list_value(value=value)
            self._append_value_setter_expression(value=value)

    def _append_value_setter_expression(
            self, value: Union[List[Any], tuple, 'Array']) -> None:
        """
        Append value's setter expression.

        Parameters
        ----------
        value : list or tuple or Array
            Iterable value (list, tuple, or Array) to set.
        """
        with ap.DebugInfo(
                callable_=self._append_value_setter_expression,
                locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            expression: str = f'{self.variable_name} = '
            if isinstance(value, Array):
                expression += f'{value.variable_name};'
            else:
                value_str: str = value_util.get_value_str_for_expression(
                    value=value)
                expression += f'{value_str};'
            ap.append_js_expression(expression=expression)

    def append(self, value: T) -> None:
        """
        Add any value to the end of this array.
        This behaves same as push method.

        Parameters
        ----------
        value : *
            Any value to append.
        """
        with ap.DebugInfo(
                callable_=self.append, locals_=locals(),
                module_name=__name__, class_=Array):
            self._value.append(value)
            self._append_push_and_append_expression(value=value)

    def push(self, value: T) -> None:
        """
        Add any value to the end of this array.
        This behaves same as append method.

        Parameters
        ----------
        value : *
            Any value to append.
        """
        with ap.DebugInfo(
                callable_=self.push, locals_=locals(),
                module_name=__name__, class_=Array):
            self.append(value=value)

    def _append_push_and_append_expression(self, value: T) -> None:
        """
        Append push and append method expression.

        Parameters
        ----------
        value : *
            Any value to append.
        """
        with ap.DebugInfo(
                callable_=self._append_push_and_append_expression,
                locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            value_str: str = value_util.get_value_str_for_expression(
                value=value)
            expression: str = (
                f'{self.variable_name}.push({value_str});'
            )
            ap.append_js_expression(expression=expression)

    def extend(self, other_arr: Union[List[T], tuple, 'Array']) -> None:
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
        with ap.DebugInfo(
                callable_=self.extend, locals_=locals(),
                module_name=__name__, class_=Array):
            self._validate_acceptable_value_type(value=other_arr)
            if isinstance(other_arr, Array):
                self._value.extend(other_arr.value)  # type: ignore
            else:
                self._value.extend(other_arr)
            self._append_extend_expression(other_arr=other_arr)

    def _append_extend_expression(
            self, other_arr: Union[List[T], tuple, 'Array']) -> None:
        """
        Append extend method expression.

        Parameters
        ----------
        other_arr : list or tuple or Array
            Other array-like value to concatenate.
        """
        with ap.DebugInfo(
                callable_=self._append_extend_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            value_str: str = value_util.get_value_str_for_expression(
                value=other_arr)
            expression: str = (
                f'{self.variable_name} = {self.variable_name}'
                f'.concat({value_str});')
            ap.append_js_expression(expression=expression)

    def concat(
            self, other_arr: Union[List[T], tuple, 'Array']) -> 'Array':
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
        with ap.DebugInfo(
                callable_=self.concat, locals_=locals(),
                module_name=__name__, class_=Array):
            concatenated: Array = self._copy()
            concatenated.extend(other_arr)
            self._append_concat_expression(
                concatenated=concatenated, other_arr=other_arr)
            return concatenated

    def _append_concat_expression(
            self, concatenated: VariableNameInterface,
            other_arr: Union[List[T], tuple, 'Array']) -> None:
        """
        Append concat method expression.

        Parameters
        ----------
        concatenated : Array
            Concatenated array value.
        other_arr : list or tuple or Array
            Other array-like value to concatenate.
        """
        with ap.DebugInfo(
                callable_=self._append_concat_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            value_str: str = value_util.get_value_str_for_expression(
                value=other_arr)
            expression: str = (
                f'var {concatenated.variable_name} = '
                f'{self.variable_name}.concat({value_str});'
            )
            ap.append_js_expression(expression=expression)

    def insert(
            self, index: Union[int, ap.Int], value: T) -> None:
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
        with ap.DebugInfo(
                callable_=self.insert, locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=index)
            if isinstance(index, ap.Int):
                index_: int = int(index.value)
            else:
                index_ = index
            value_: Any
            if isinstance(value, ap.Int):
                value_ = int(value.value)
            else:
                value_ = value
            self._value.insert(index_, value_)
            self._append_insert_expression(index=index, value=value)

    def insert_at(self, index: Union[int, ap.Int], value: T) -> None:
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
        with ap.DebugInfo(
                callable_=self.insert_at, locals_=locals(),
                module_name=__name__, class_=Array):
            self.insert(index=index, value=value)

    def _append_insert_expression(
            self, index: Union[int, ap.Int], value: T) -> None:
        """
        Append insert method expression.

        Parameters
        ----------
        index : int or Int
            Index to append value to.
        value : *
            Any value to append.
        """
        with ap.DebugInfo(
                callable_=self._append_insert_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            value_str: str = value_util.get_value_str_for_expression(
                value=value)
            index_str: str = value_util.get_value_str_for_expression(
                value=index)
            expression: str = (
                f'{self.variable_name}.splice({index_str}, 0, {value_str});'
            )
            ap.append_js_expression(expression=expression)

    def pop(self) -> T:
        """
        Remove this array's last value and return it.

        Returns
        -------
        value : *
            Removed value.
        """
        with ap.DebugInfo(
                callable_=self.pop, locals_=locals(),
                module_name=__name__, class_=Array):
            value: T = self._value.pop()
            self._append_pop_expression(value=value)
            return value

    def _append_pop_expression(self, value: T) -> None:
        """
        Append pop method expression.

        Parameters
        ----------
        value : *
            Removed value.
        """
        with ap.DebugInfo(
                callable_=self._append_pop_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            expression: str = f'{self.variable_name}.pop();'
            if isinstance(value, VariableNameInterface):
                expression = f'{value.variable_name} = {expression}'
            ap.append_js_expression(expression=expression)

    def remove(self, value: T) -> None:
        """
        Remove specified value from this array.

        Parameters
        ----------
        value : Any
            Value to remove.
        """
        with ap.DebugInfo(
                callable_=self.remove, locals_=locals(),
                module_name=__name__, class_=Array):
            self._value.remove(value)
            self._append_remove_expression(value=value)

    def _append_remove_expression(self, value: T) -> None:
        """
        Append remove method expression.

        Parameters
        ----------
        value : Any
            Value to remove.
        """
        with ap.DebugInfo(
                callable_=self._append_remove_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            from apysc._type import value_util
            index_var_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.INDEX)
            value_str: str = value_util.get_value_str_for_expression(
                value=value)
            expression: str = (
                f'var {index_var_name} = _.indexOf'
                f'({self.variable_name}, {value_str});'
                f'\n{self.variable_name}.splice({index_var_name}, 1);')
            ap.append_js_expression(expression=expression)

    def remove_at(self, index: Union[int, ap.Int]) -> None:
        """
        Remove specified index value from this array.

        Parameters
        ----------
        index : int or Int
            Index to remove value.
        """
        with ap.DebugInfo(
                callable_=self.remove_at, locals_=locals(),
                module_name=__name__, class_=Array):
            self._validate_index_type_is_int(index=index)
            if isinstance(index, ap.Int):
                index_: int = int(index.value)
            else:
                index_ = index
            if index_ in self._value:
                del self._value[index_]
            self._append_remove_at_expression(index=index)

    def _append_remove_at_expression(
            self, index: Union[int, ap.Int]) -> None:
        """
        Append remove_at method expression.

        Parameters
        ----------
        index : int or Int
            Index to remove value.
        """
        with ap.DebugInfo(
                callable_=self._append_remove_at_expression,
                locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            index_str: str = value_util.get_value_str_for_expression(
                value=index)
            expression: str = (
                f'{self.variable_name}.splice({index_str}, 1);'
            )
            ap.append_js_expression(expression=expression)

    def reverse(self) -> None:
        """
        Reverse this array in place.
        """
        with ap.DebugInfo(
                callable_=self.reverse, locals_=locals(),
                module_name=__name__, class_=Array):
            self._value.reverse()
            self._append_reverse_expression()

    def _append_reverse_expression(self) -> None:
        """
        Append reverse method expression.
        """
        with ap.DebugInfo(
                callable_=self._append_reverse_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            expression: str = (
                f'{self.variable_name}.reverse();'
            )
            ap.append_js_expression(expression=expression)

    def sort(self, ascending: bool = True) -> None:
        """
        Sort this array in place.

        Parameters
        ----------
        ascending : bool, default True
            Sort by ascending or not. If False is specified,
            values will be descending.
        """
        with ap.DebugInfo(
                callable_=self.sort, locals_=locals(),
                module_name=__name__, class_=Array):
            self._value.sort()
            self._append_sort_expression()
            if not ascending:
                self.reverse()

    def _append_sort_expression(self) -> None:
        """
        Append sort method expression.
        """
        with ap.DebugInfo(
                callable_=self._append_sort_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            expression: str = (
                f'{self.variable_name}.sort();'
            )
            ap.append_js_expression(expression=expression)

    def slice(
            self,
            start: Optional[Union[int, ap.Int]] = None,
            end: Optional[Union[int, ap.Int]] = None) -> 'Array':
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
        with ap.DebugInfo(
                callable_=self.slice, locals_=locals(),
                module_name=__name__, class_=Array):
            if isinstance(start, ap.Int):
                start_: Optional[int] = int(start.value)
            else:
                start_ = start
            if isinstance(end, ap.Int):
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
            start: Optional[Union[int, ap.Int]],
            end: Optional[Union[int, ap.Int]]) -> None:
        """
        Append slice method expression.

        Parameters
        ----------
        sliced_arr : Array
            Sliced array.
        start : int or Int or None
            Slicing start index.
        end : int or Int or None
            Slicing end index.
        """
        with ap.DebugInfo(
                callable_=self._append_slice_expression, locals_=locals(),
                module_name=__name__, class_=Array):
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
            ap.append_js_expression(expression=expression)

    def __getitem__(self, index: Union[int, ap.Int]) -> T:
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
        with ap.DebugInfo(
                callable_='__getitem__', locals_=locals(),
                module_name=__name__, class_=Array):
            self._validate_index_type_is_int(index=index)
            index_: int = self._get_builtin_int_from_index(index=index)
            value: Any
            if len(self._value) <= index:
                value = ap.AnyValue(None)
            else:
                value = self._value[index_]
            self._append_getitem_expression(index=index, value=value)
            return value

    def _get_builtin_int_from_index(self, index: Union[int, ap.Int]) -> int:
        """
        Get Python builtin integer from index value.

        Parameters
        ----------
        index : int or Int
            Specified array's index.

        Returns
        -------
        builtin_int_index : int
            Python builtin integer index value.
        """
        if isinstance(index, ap.Int):
            return int(index.value)
        return index

    def _validate_index_type_is_int(self, index: Union[int, ap.Int]) -> None:
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
        if isinstance(index, (int, ap.Int)):
            return
        raise ValueError(
            'Currently indexing is only supported int or Int types.'
            ' If you need to slice array please use slice method.')

    def _append_getitem_expression(
            self, index: Union[int, ap.Int],
            value: T) -> None:
        """
        Append __getitem__ expression.

        Parameters
        ----------
        index : int or Int
            Array's index to get value.
        value : *
            Specified index's value.
        """
        with ap.DebugInfo(
                callable_=self._append_getitem_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            value_: VariableNameInterface
            if not isinstance(value, VariableNameInterface):
                value_ = ap.AnyValue(None)
            else:
                value_ = value
            index_str: str = value_util.get_value_str_for_expression(
                value=index)
            expression: str = (
                f'var {value_.variable_name} = '
                f'{self.variable_name}[{index_str}];'
            )
            ap.append_js_expression(expression=expression)

    def __setitem__(self, index: Union[int, ap.Int], value: T) -> None:
        """
        Set value to a specified index.

        Parameters
        ----------
        index : int or Int
            Array's index to set value. Currently not supported tuple
            value (e.g., slicing).
        value : *
            Any value to set.

        Raises
        ------
        ValueError
            If specified index type is not int and Int.
        """
        with ap.DebugInfo(
                callable_='__setitem__', locals_=locals(),
                module_name=__name__, class_=Array):
            self._validate_index_type_is_int(index=index)
            index_: int = self._get_builtin_int_from_index(index=index)
            self._value[index_] = value
            self._append_setitem_expression(index=index, value=value)

    def _append_setitem_expression(
            self, index: Union[int, ap.Int], value: T) -> None:
        """
        Append __setitem__ method expression.

        Parameters
        ----------
        index : int or Int
            Array's index to set value. Currently not supported tuple
            value (e.g., slicing).
        value : *
            Any value to set.
        """
        with ap.DebugInfo(
                callable_=self._append_setitem_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            index_str: str = value_util.get_value_str_for_expression(
                value=index)
            value_str: str = value_util.get_value_str_for_expression(
                value=value)
            expression: str = (
                f'{self.variable_name}[{index_str}] = '
                f'{value_str};'
            )
            ap.append_js_expression(expression=expression)

    def __delitem__(self, index: Union[int, ap.Int]) -> None:
        """
        Delete specified index value from this array.

        Parameters
        ----------
        index : int or Int
            Array's index to delete. Currently not supported tuple
            value (e.g., slicing).

        Raises
        ------
        ValueError
            If specified index type is not int and Int.
        """
        with ap.DebugInfo(
                callable_='__delitem__', locals_=locals(),
                module_name=__name__, class_=Array):
            self.remove_at(index=index)

    @property
    def length(self) -> ap.Int:
        """
        Get length of this array.

        Returns
        -------
        length : Int
            This array's length.
        """
        with ap.DebugInfo(
                callable_='length', locals_=locals(),
                module_name=__name__, class_=Array):
            length: ap.Int = ap.Int(len(self._value))
            self._append_length_expression(length=length)
            return length

    def _append_length_expression(self, length: ap.Int) -> None:
        """
        Append length method expression.

        Parameters
        ----------
        length : Int
            Created length Int variable.
        """
        with ap.DebugInfo(
                callable_=self._append_length_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            expression: str = (
                f'{length.variable_name} = {self.variable_name}.length;'
            )
            ap.append_js_expression(expression=expression)

    def __len__(self) -> None:
        """
        This method is disabled and can't use from Array instance.
        """
        raise Exception(
            'Array instance can\'t apply len function.'
            ' Please use length property instead.')

    def join(self, sep: Union[str, ap.String]) -> ap.String:
        """
        Join this array values with specified separator string.

        Parameters
        ----------
        sep : str or String
            Separator string.

        Returns
        -------
        joined : String
            Joined string.

        Examples
        --------
        >>> arr: Array = Array([1, 2', 3])
        >>> arr.join(sep=', ')
        '1, 2, 3'
        """
        with ap.DebugInfo(
                callable_=self.join, locals_=locals(),
                module_name=__name__, class_=Array):
            if isinstance(sep, ap.String):
                sep_: str = sep._value
            else:
                sep_ = sep
            values_: List[Any] = [str(value) for value in self._value]
            joined: ap.String = ap.String(sep_.join(values_))
            self._append_join_expression(joined=joined, sep=sep)
            return joined

    def _append_join_expression(
            self, joined: ap.String, sep: Union[str, ap.String]) -> None:
        """
        Append join method expression.

        Parameters
        ----------
        joined : String
            Joined string.
        sep : str or String
            Separator string.
        """
        with ap.DebugInfo(
                callable_=self._append_join_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            sep_str: str = value_util.get_value_str_for_expression(value=sep)
            expression: str = (
                f'{joined.variable_name} = {self.variable_name}'
                f'.join({sep_str});'
            )
            ap.append_js_expression(expression=expression)

    def __str__(self) -> str:
        """
        String conversion method.

        Returns
        -------
        string : str
            Converted value string.
        """
        if not hasattr(self, '_value'):
            return '[]'
        return str(self._value)

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        if not hasattr(self, '_value'):
            repr_str: str = 'Array([])'
        else:
            repr_str = f'Array({self._value})'
        return repr_str

    def index_of(self, value: T) -> ap.Int:
        """
        Search specified value's index and return it.

        Parameters
        ----------
        value : *
            Any value to search.

        Returns
        -------
        index : Int
            Found position of index. If value is not contains,
            -1 will be returned.
        """
        with ap.DebugInfo(
                callable_=self.index_of, locals_=locals(),
                module_name=__name__, class_=Array):
            index: ap.Int = ap.Int(-1)
            try:
                index_: int = self._value.index(value)
            except Exception:
                index_ = -1
            index._value = index_
            self._append_index_of_expression(index=index, value=value)
            return index

    def _append_index_of_expression(
            self, index: ap.Int, value: T) -> None:
        """
        Append index_of method expression.

        Parameters
        ----------
        index : Int
            Found position of index. If value is not contains,
            -1 will be set.
        value : *
            Any value to search.
        """
        with ap.DebugInfo(
                callable_=self._append_index_of_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            from apysc._type import value_util
            value_str: str = value_util.get_value_str_for_expression(
                value=value)
            expression: str = (
                f'{index.variable_name} = {self.variable_name}'
                f'.indexOf({value_str});'
            )
            ap.append_js_expression(expression=expression)

    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : *
            Other value to compare. list or Array types are acceptable.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        with ap.DebugInfo(
                callable_='__eq__', locals_=locals(),
                module_name=__name__, class_=Array):
            result: ap.Boolean
            if isinstance(other, Array):
                result = ap.Boolean(self._value == other._value)
            else:
                result = ap.Boolean(self._value == other)
                other = self._convert_other_val_to_array(other=other)
            if isinstance(other, VariableNameInterface):
                self._append_eq_expression(result=result, other=other)
            return result

    def _convert_other_val_to_array(self, other: Any) -> Any:
        """
        If comparison's other value is list value, then convert it to
        Array instance.

        Parameters
        ----------
        other : *
            Other value to compare.

        Returns
        -------
        converted_val : *
            Converted value. If other value is list, then this will
            be Array type. Otherwise this will be returned directly
            (not to be converted).
        """
        with ap.DebugInfo(
                callable_=self._convert_other_val_to_array, locals_=locals(),
                module_name=__name__, class_=Array):
            if isinstance(other, list):
                return Array(other)
            return other

    def _append_eq_expression(
            self, result: ap.Boolean, other: VariableNameInterface) -> None:
        """
        Append an __eq__ expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : Array
            Array other value to compare.
        """
        with ap.DebugInfo(
                callable_=self._append_eq_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            expression: str = (
                f'{result.variable_name} = '
                f'_.isEqual({self.variable_name}, {other.variable_name});'
            )
            ap.append_js_expression(expression=expression)

    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : *
            Other value to compare. list or Array types are acceptable.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        with ap.DebugInfo(
                callable_='__ne__', locals_=locals(),
                module_name=__name__, class_=Array):
            other = self._convert_other_val_to_array(other=other)
            result: ap.Boolean = self == other
            result = result.not_
            if isinstance(other, VariableNameInterface):
                self._append_ne_expression(result=result, other=other)
            return result

    def _append_ne_expression(
            self, result: ap.Boolean, other: VariableNameInterface) -> None:
        """
        Append a __ne__ expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        other : Array
            Array other value to compare.
        """
        with ap.DebugInfo(
                callable_=self._append_ne_expression, locals_=locals(),
                module_name=__name__, class_=Array):
            expression: str = (
                f'{result.variable_name} = '
                f'!_.isEqual({self.variable_name}, {other.variable_name});'
            )
            ap.append_js_expression(expression=expression)

    def __bool__(self) -> bool:
        """
        Get a boolean value whether this array is empty or not.

        Returns
        -------
        result : bool
            If this array is empty, True will be returned.
        """
        return bool(self._value)

    _value_snapshots: Dict[str, List[T]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_value_snapshots'):
            self._value_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._value_snapshots[snapshot_name] = [*self._value]

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._value = self._value_snapshots[snapshot_name]
