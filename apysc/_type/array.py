"""Class implementation for an array.
"""

from typing import Any
from typing import Dict
from typing import Generic
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union
from typing import cast

from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.boolean import Boolean
from apysc._type.copy_mixin import CopyMixIn
from apysc._type.initial_substitution_exp_mixin import InitialSubstitutionExpMixIn
from apysc._type.int import Int
from apysc._type.py_builtin_iter_disabling_mixin import PyBuiltInIterDisablingMixIn
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string import String
from apysc._type.to_string_mixin import ToStringMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos

_ArrValue = TypeVar("_ArrValue")


class Array(
    ToStringMixIn,
    CopyMixIn["Array"],
    RevertMixIn,
    CustomEventMixIn,
    VariableNameSuffixMixIn,
    InitialSubstitutionExpMixIn,
    PyBuiltInIterDisablingMixIn,
    InitializeWithBaseValueInterface,
    Generic[_ArrValue],
):
    """
    Array class for the apysc library.

    References
    ----------
    - Array
        - https://simon-ritchie.github.io/apysc/en/array.html
    - Array class comparison interfaces
        - https://simon-ritchie.github.io/apysc/en/array_comparison.html

    Examples
    --------
    >>> import apysc as ap
    >>> _ = ap.Stage()
    >>> arr: ap.Array = ap.Array([1, 2, 3])
    >>> arr
    Array([1, 2, 3])

    >>> arr[0]
    1

    >>> arr[1]
    2

    >>> arr = ap.Array((4, 5, 6))
    >>> arr
    Array([4, 5, 6])

    >>> arr = ap.Array(range(3))
    >>> arr
    Array([0, 1, 2])

    >>> arr = ap.Array([1, 2, 3])
    >>> arr.append(4)
    >>> arr
    Array([1, 2, 3, 4])

    >>> arr = ap.Array([1, 2, 3])
    >>> arr = arr.concat([4, 5, 6])
    >>> arr
    Array([1, 2, 3, 4, 5, 6])
    """

    _initial_value: Union[List[Any], tuple, "Array"]
    _value: List[_ArrValue]
    _fixed_value_type: Optional[Type[InitializeWithBaseValueInterface]]

    @arg_validation_decos.is_acceptable_array_value(arg_position_index=1)
    @arg_validation_decos.is_initialize_with_base_value_interface_subclass(
        arg_position_index=2, optional=True
    )
    @arg_validation_decos.is_builtin_string(arg_position_index=3, optional=False)
    @arg_validation_decos.is_builtin_boolean(arg_position_index=4)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        value: Union[List[_ArrValue], tuple, range, "Array"],
        *,
        fixed_value_type: Optional[Type[InitializeWithBaseValueInterface]] = None,
        variable_name_suffix: str = "",
        skip_init_substitution_expression_appending: bool = False,
    ) -> None:
        """
        Array class for the apysc library.

        Parameters
        ----------
        value : Array or list or tuple or range
            Initial array value.
        fixed_value_type : Optional[Type[InitializeWithBaseValueInterface]], optional
            A fixed value type of array.
            This argument only becomes an apysc type, such as the
            `ap.Int`, `ap.String`, or `ap.Rectangle`.
            If specified, the array value-related interfaces, such as
            the `__getitem__` method (array subscript interface,
            for example, `arr[5]`), becomes possibly returning
            a specified value type instance.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        skip_init_substitution_expression_appending : bool, default False
            A boolean indicates whether to skip an initial substitution
            expression or not. This class uses this option internally.

        References
        ----------
        - Array
            - https://simon-ritchie.github.io/apysc/en/array.html
        - Array class comparison interfaces
            - https://simon-ritchie.github.io/apysc/en/array_comparison.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> arr
        Array([1, 2, 3])

        >>> arr[0]
        1

        >>> arr[1]
        2

        >>> arr = ap.Array((4, 5, 6))
        >>> arr
        Array([4, 5, 6])

        >>> arr = ap.Array(range(3))
        >>> arr
        Array([0, 1, 2])
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope

        self._fixed_value_type = fixed_value_type

        with TemporaryNotHandlerScope():
            self._variable_name_suffix = variable_name_suffix
            TYPE_NAME: str = var_names.ARRAY
            value = self._convert_range_to_list(value=value)
            value_: Union[List[Any], tuple, "Array"] = value
            self._initial_value = value_
            self._type_name = TYPE_NAME
            self._value = self._get_list_value(value=value)
            self.variable_name = expression_variables_util.get_next_variable_name(
                type_name=TYPE_NAME
            )
            self._append_constructor_expression()

        self._append_initial_substitution_expression_if_in_handler_scope(
            skip_appending=skip_init_substitution_expression_appending,
        )

    @final
    def _convert_range_to_list(self, *, value: Any) -> Union[List[Any], tuple, "Array"]:
        """
        Convert argument value to list if a specified
        value is a range type.

        Parameters
        ----------
        value : Array or list or tuple or range
            Target value.

        Returns
        -------
        value : Array or list or tuple
            Converted value.
        """
        if isinstance(value, range):
            return list(value)
        return value

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        from apysc._expression import expression_data_util

        expression: str = self._create_initial_substitution_expression()
        expression = f"var {expression}"
        expression_data_util.append_js_expression(expression=expression)

    @final
    def _create_initial_substitution_expression(self) -> str:
        """
        Create an initial value's substitution expression string.

        Returns
        -------
        expression : str
            Created expression string.
        """
        from apysc._type import value_util

        expression: str = f"{self.variable_name} = "
        if isinstance(self._initial_value, Array):
            expression += f"{self._initial_value.variable_name};"
        else:
            value_str: str = value_util.get_value_str_for_expression(value=self._value)
            expression += f"{value_str};"
        return expression

    @final
    def _get_list_value(self, *, value: Union[List[Any], tuple, "Array"]) -> List[Any]:
        """
        Get a list value from a specified list, tuple, or
        Array value.

        Parameters
        ----------
        value : Array or list or tuple
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
        return list(value)  # type: ignore[arg-type]

    @property
    @add_debug_info_setting(module_name=__name__)
    def value(self) -> Union[List[Any], tuple, "Array"]:
        """
        Get a current array value.

        Returns
        -------
        value : list
            Current array value.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> arr.value = [4, 5, 6]
        >>> arr.value
        [4, 5, 6]
        """
        return self._value

    @value.setter
    @arg_validation_decos.is_acceptable_array_value(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def value(self, value: Union[List[Any], tuple, range, "Array"]) -> None:
        """
        Set array value.

        Parameters
        ----------
        value : Array or list or tuple or range
            Iterable value (list, tuple, or Array) to set.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa
        """
        value = self._convert_range_to_list(value=value)
        self._value = self._get_list_value(value=value)
        self._append_value_setter_expression(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_value_setter_expression(
        self, *, value: Union[List[Any], tuple, "Array"]
    ) -> None:
        """
        Append value's setter expression.

        Parameters
        ----------
        value : Array or list or tuple
            Iterable value (Array, list, or tuple) to set.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        expression: str = f"{self.variable_name} = "
        if isinstance(value, Array):
            expression += f"{value.variable_name};"
        else:
            value_str: str = value_util.get_value_str_for_expression(value=value)
            expression += f"{value_str};"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def append(self, value: _ArrValue) -> None:
        """
        Add any value to the end of this array.
        This method behaves the same `push` method.

        Parameters
        ----------
        value : *
            Any value to append.

        References
        ----------
        - Array class append and push interfaces
            - https://simon-ritchie.github.io/apysc/en/array_append_and_push.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> arr.append(4)
        >>> arr
        Array([1, 2, 3, 4])
        """
        self._value.append(value)
        self._append_push_and_append_expression(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def push(self, value: _ArrValue) -> None:
        """
        Add any value to the end of this array. This
        interface behaves the same as the `append` method.

        Parameters
        ----------
        value : *
            Any value to append.

        References
        ----------
        - Array class append and push interfaces
            - https://simon-ritchie.github.io/apysc/en/array_append_and_push.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> arr.push(4)
        >>> arr
        Array([1, 2, 3, 4])
        """
        self.append(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_push_and_append_expression(self, *, value: _ArrValue) -> None:
        """
        Append push and append method expression.

        Parameters
        ----------
        value : *
            Any value to append.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = f"{self.variable_name}.push({value_str});"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_acceptable_array_value(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def extend(self, other_arr: Union[List[_ArrValue], tuple, range, "Array"]) -> None:
        """
        Concatenate argument array to this one. This interface
        positions the argument array's values after this array
        values. This method is similar to the concat method.
        Still, there is a difference in whether updating the same
        variable (extend) or returning as a different variable (concat).

        Parameters
        ----------
        other_arr : Array or list or tuple or range
            Other array-like values to concatenate.

        References
        ----------
        - Array class extend and concat interfaces
            - https://simon-ritchie.github.io/apysc/en/array_extend_and_concat.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> arr.extend([4, 5, 6])
        >>> arr
        Array([1, 2, 3, 4, 5, 6])
        """
        other_arr = self._convert_range_to_list(value=other_arr)
        if isinstance(other_arr, Array):
            self._value.extend(other_arr.value)  # type: ignore
        else:
            self._value.extend(list(other_arr))  # type: ignore[arg-type]
        self._append_extend_expression(other_arr=other_arr)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_extend_expression(
        self, *, other_arr: Union[List[_ArrValue], tuple, "Array"]
    ) -> None:
        """
        Append an `extend` method expression.

        Parameters
        ----------
        other_arr : Array or list or tuple
            The other array-like value to concatenate.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        value_str: str = value_util.get_value_str_for_expression(value=other_arr)
        expression: str = (
            f"{self.variable_name} = {self.variable_name}" f".concat({value_str});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def concat(self, other_arr: Union[List[_ArrValue], tuple, "Array"]) -> "Array":
        """
        Concatenate argument array to this one. This interface
        positions the argument array's values after this array
        values. This method is similar to extend method,
        but there is a difference in whether updating
        the same variable (extend) or returning as a different
        variable (concat).

        Parameters
        ----------
        other_arr : Array or list or tuple
            Other array-like values to concatenate.

        Returns
        -------
        concatenated : Array
            Concatenated array value.

        References
        ----------
        - Array class extend and concat interfaces
            - https://simon-ritchie.github.io/apysc/en/array_extend_and_concat.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> arr = arr.concat([4, 5, 6])
        >>> arr
        Array([1, 2, 3, 4, 5, 6])
        """
        concatenated: Array = self._copy()
        concatenated.extend(other_arr)
        self._append_concat_expression(concatenated=concatenated, other_arr=other_arr)
        return concatenated

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_concat_expression(
        self,
        *,
        concatenated: VariableNameMixIn,
        other_arr: Union[List[_ArrValue], tuple, "Array"],
    ) -> None:
        """
        Append the `concat` method expression.

        Parameters
        ----------
        concatenated : Array
            Concatenated array value.
        other_arr : Array or list or tuple
            The other array-like value to concatenate.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        value_str: str = value_util.get_value_str_for_expression(value=other_arr)
        expression: str = (
            f"var {concatenated.variable_name} = "
            f"{self.variable_name}.concat({value_str});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def insert(self, index: Union[int, Int], value: _ArrValue) -> None:
        """
        Insert value to this array at a specified index.
        This interface behaves in the same `insert_at` method.

        Parameters
        ----------
        index : Int or int
            Index to append value.
        value : *
            Any value to append.

        References
        ----------
        - Array class insert and insert_at interfaces
            - https://simon-ritchie.github.io/apysc/en/array_insert_and_insert_at.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 3])
        >>> arr.insert(index=1, value=2)
        >>> arr
        Array([1, 2, 3])
        """
        if isinstance(index, Int):
            index_: int = int(index.value)
        else:
            index_ = int(index)
        value_: Any
        if isinstance(value, Int):
            value_ = int(value.value)
        else:
            value_ = value
        self._value.insert(index_, value_)
        self._append_insert_expression(index=index, value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def insert_at(self, *, index: Union[int, Int], value: _ArrValue) -> None:
        """
        Insert value to this array at a specified index.
        This interface behaves in the same `insert` method.

        Parameters
        ----------
        index : Int or int
            Index to append value.
        value : *
            Any value to append.

        References
        ----------
        - Array class insert and insert_at interfaces
            - https://simon-ritchie.github.io/apysc/en/array_insert_and_insert_at.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 3])
        >>> arr.insert_at(index=1, value=2)
        >>> arr
        Array([1, 2, 3])
        """
        self.insert(index=index, value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_insert_expression(
        self,
        *,
        index: Union[int, Int],
        value: _ArrValue,
    ) -> None:
        """
        Append insert method expression.

        Parameters
        ----------
        index : Int or int
            Index to append value.
        value : *
            Any value to append.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        value_str: str = value_util.get_value_str_for_expression(value=value)
        index_str: str = value_util.get_value_str_for_expression(value=index)
        expression: str = f"{self.variable_name}.splice({index_str}, 0, {value_str});"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def pop(self) -> _ArrValue:
        """
        Remove this array's last value and return it.

        Returns
        -------
        value : *
            Removed value.

        References
        ----------
        - Array class pop interface
            - https://simon-ritchie.github.io/apysc/en/array_pop.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> popped_val: int = arr.pop()
        >>> popped_val
        3

        >>> arr
        Array([1, 2])
        """
        value: _ArrValue = self._value.pop()
        self._append_pop_expression(value=value)
        return value

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_pop_expression(self, *, value: _ArrValue) -> None:
        """
        Append pop method expression.

        Parameters
        ----------
        value : *
            Removed value.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{self.variable_name}.pop();"
        if isinstance(value, VariableNameMixIn):
            expression = f"{value.variable_name} = {expression}"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def remove(self, value: _ArrValue) -> None:
        """
        Remove a specified value from this array.

        Parameters
        ----------
        value : Any
            Value to remove.

        References
        ----------
        - Array class remove and remove_at interfaces
            - https://simon-ritchie.github.io/apysc/en/array_remove_and_remove_at.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 3, 5])
        >>> arr.remove(3)
        >>> arr
        Array([1, 5])
        """
        self._value.remove(value)
        self._append_remove_expression(value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_remove_expression(self, *, value: _ArrValue) -> None:
        """
        Append a `remove` method expression.

        Parameters
        ----------
        value : Any
            Value to remove.
        """
        from apysc._expression import expression_data_util
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._type import value_util

        index_var_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.INDEX
        )
        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = (
            f"var {index_var_name} = _.indexOf"
            f"({self.variable_name}, {value_str});"
            f"\n{self.variable_name}.splice({index_var_name}, 1);"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def remove_at(self, index: Union[int, Int]) -> None:
        """
        Remove a specified index value from this array.

        Parameters
        ----------
        index : Int or int
            Index to remove value.

        References
        ----------
        - Array class remove and remove_at interfaces
            - https://simon-ritchie.github.io/apysc/en/array_remove_and_remove_at.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> arr.remove_at(1)
        >>> arr
        Array([1, 3])
        """
        self._validate_index_type_is_int(index=index)
        if isinstance(index, Int):
            index_: int = int(index.value)
        else:
            index_ = int(index)
        if index_ in self._value:
            del self._value[index_]
        self._append_remove_at_expression(index=index)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_remove_at_expression(self, *, index: Union[int, Int]) -> None:
        """
        Append a remove_at method expression.

        Parameters
        ----------
        index : Int or int
            Index to remove value.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        index_str: str = value_util.get_value_str_for_expression(value=index)
        expression: str = f"{self.variable_name}.splice({index_str}, 1);"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def reverse(self) -> None:
        """
        Reverse this array in place.

        References
        ----------
        - Array class reverse interface
            - https://simon-ritchie.github.io/apysc/en/array_reverse.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> arr.reverse()
        >>> arr
        Array([3, 2, 1])
        """
        self._value.reverse()
        self._append_reverse_expression()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_reverse_expression(self) -> None:
        """
        Append reverse method expression.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{self.variable_name}.reverse();"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_builtin_boolean(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def sort(self, *, ascending: bool = True) -> None:
        """
        Sort this array in place.

        Parameters
        ----------
        ascending : bool, default True
            Sort by ascending or not. If False is specified,
            this interface sorts values descending.

        References
        ----------
        - Array class sort interface
            - https://simon-ritchie.github.io/apysc/en/array_sort.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([3, 5, 1, 4, 2])
        >>> arr.sort()
        >>> arr
        Array([1, 2, 3, 4, 5])

        >>> arr.sort(ascending=False)
        >>> arr
        Array([5, 4, 3, 2, 1])
        """
        self._value.sort()  # type: ignore
        self._append_sort_expression()
        if not ascending:
            self.reverse()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_sort_expression(self) -> None:
        """
        Append sort method expression.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{self.variable_name}.sort();"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def slice(
        self,
        *,
        start: Optional[Union[int, Int]] = None,
        end: Optional[Union[int, Int]] = None,
    ) -> "Array":
        """
        Slice this array by specified start and end indexes.

        Parameters
        ----------
        start : Int or int or None, default None
            Slicing start index.
        end : Int or int or None, default None
            Slicing end index (a result array does not contain
            this index).

        Returns
        -------
        sliced_arr : Array
            Sliced array.

        References
        ----------
        - Array class slice interface
            - https://simon-ritchie.github.io/apysc/en/array_slice.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3, 4])
        >>> arr.slice(start=1, end=3)
        Array([2, 3])

        >>> arr.slice(start=1)
        Array([2, 3, 4])

        >>> arr.slice(end=2)
        Array([1, 2])
        """
        if isinstance(start, Int):
            start_: Optional[int] = int(start.value)
        else:
            start_ = start  # type: ignore[assignment]
        if isinstance(end, Int):
            end_: Optional[int] = int(end.value)
        else:
            end_ = end  # type: ignore[assignment]
        sliced_arr: Array = self._copy()
        sliced_arr._value = self._value[slice(start_, end_)]
        self._append_slice_expression(sliced_arr=sliced_arr, start=start, end=end)
        return sliced_arr

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_slice_expression(
        self,
        *,
        sliced_arr: VariableNameMixIn,
        start: Optional[Union[int, Int]],
        end: Optional[Union[int, Int]],
    ) -> None:
        """
        Append slice method expression.

        Parameters
        ----------
        sliced_arr : Array
            Sliced array value.
        start : Int or int or None
            Slicing start index.
        end : Int or int or None
            Slicing end index.
        """
        from apysc._expression import expression_data_util

        if start is None:
            start = 0
        expression: str = (
            f"var {sliced_arr.variable_name} = "
            f"{self.variable_name}.slice("
            f"{start}"
        )
        if end is not None:
            expression += f", {end}"
        expression += ");"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __getitem__(self, index: Union[int, Int]) -> _ArrValue:
        """
        Get a specified index single value.

        Parameters
        ----------
        index : Int or int
            Array's index to get value. Currently not supported tuple
            value (e.g., slicing).

        Returns
        -------
        value : *
            Specified index's value.

        Raises
        ------
        ValueError
            If a specified index type is not the `Int` or `int` type.
        """
        from apysc._type.any_value import AnyValue

        self._validate_index_type_is_int(index=index)
        index_: int = self._get_builtin_int_from_index(index=index)
        value: Any
        index_is_out_of_bounds: bool = len(self._value) <= index
        if (
            index_is_out_of_bounds
            and self._fixed_value_type is not None
            and issubclass(self._fixed_value_type, InitializeWithBaseValueInterface)
        ):
            value = self._fixed_value_type._initialize_with_base_value()
        elif index_is_out_of_bounds:
            value = AnyValue(None)
        else:
            value = self._value[index_]
        self._append_getitem_expression(index=index, value=value)
        return value

    @final
    def _get_builtin_int_from_index(self, *, index: Union[int, Int]) -> int:
        """
        Get Python built-in integer from index value.

        Parameters
        ----------
        index : Int or int
            Specified an array's index.

        Returns
        -------
        builtin_int_index : int
            Python builtin integer index value.
        """
        if isinstance(index, Int):
            return int(index.value)
        return int(index)

    @final
    def _validate_index_type_is_int(self, *, index: Union[int, Int]) -> None:
        """
        Validate whether an index value type is an int (or Int)
        type or not.

        Parameters
        ----------
        index : Int or int
            Index value to check.

        Raises
        ------
        ValueError
            If index type is not int or Int type.
        """
        if isinstance(index, (int, Int)):
            return
        raise ValueError(
            "Currently indexing is only supported int or Int types."
            " If you need to slice array please use slice method."
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_getitem_expression(
        self,
        *,
        index: Union[int, Int],
        value: _ArrValue,
    ) -> None:
        """
        Append __getitem__ expression.

        Parameters
        ----------
        index : Int or int
            Array's index to get value.
        value : *
            Specified index's value.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util
        from apysc._type.any_value import AnyValue

        value_: VariableNameMixIn
        if not isinstance(value, VariableNameMixIn):
            value_ = AnyValue(None)
        else:
            value_ = value
        index_str: str = value_util.get_value_str_for_expression(value=index)
        expression: str = (
            f"var {value_.variable_name} = " f"{self.variable_name}[{index_str}];"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __setitem__(self, index: Union[int, Int], value: _ArrValue) -> None:
        """
        Set value to a specified index.

        Parameters
        ----------
        index : Int or int
            Array's index to set value. Currently not supported tuple
            value (e.g., slicing).
        value : *
            Any value to set.

        Raises
        ------
        ValueError
            If a specified index type is not an `Int` or an
            `int` type.
        """
        self._validate_index_type_is_int(index=index)
        index_: int = self._get_builtin_int_from_index(index=index)
        self._value[index_] = value
        self._append_setitem_expression(index=index, value=value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_setitem_expression(
        self,
        *,
        index: Union[int, Int],
        value: _ArrValue,
    ) -> None:
        """
        Append __setitem__ method expression.

        Parameters
        ----------
        index : Int or int
            Array's index to set value. Currently not supported tuple
            value (e.g., slicing).
        value : *
            Any value to set.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        index_str: str = value_util.get_value_str_for_expression(value=index)
        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = f"{self.variable_name}[{index_str}] = " f"{value_str};"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __delitem__(self, index: Union[int, Int]) -> None:
        """
        Delete a specified index value from this array value.

        Parameters
        ----------
        index : Int or int
            Array's index to delete. Currently not supported tuple
            value (e.g., slicing).

        Raises
        ------
        ValueError
            - ValueError: If specified index type is not the
            `Int` or `int`.
        """
        self.remove_at(index=index)

    @property
    @add_debug_info_setting(module_name=__name__)
    def length(self) -> Int:
        """
        Get length of this array.

        Returns
        -------
        length : Int
            This array's length.

        References
        ----------
        - Array class length interface
            - https://simon-ritchie.github.io/apysc/en/array_length.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> arr.length
        Int(3)
        """
        length: Int = Int(
            len(self._value), variable_name_suffix=self._variable_name_suffix
        )
        self._append_length_expression(length=length)
        return length

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_length_expression(self, *, length: Int) -> None:
        """
        Append length method expression.

        Parameters
        ----------
        length : Int
            Created length Int variable.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{length.variable_name} = {self.variable_name}.length;"
        expression_data_util.append_js_expression(expression=expression)

    @final
    def __len__(self) -> None:
        """
        This method is disabled and can't use from an
        Array instance.
        """
        raise Exception(
            "Array instance can't apply len function."
            " Please use length property instead."
        )

    @final
    @arg_validation_decos.is_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def join(self, sep: Union[str, String]) -> String:
        """
        Join this array value with a specified separator string.

        Parameters
        ----------
        sep : String or str
            Separator string.

        Returns
        -------
        joined : String
            Joined string.

        References
        ----------
        - Array class join interface
            - https://simon-ritchie.github.io/apysc/en/array_join.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 2, 3])
        >>> arr.join(sep=", ")
        String("1, 2, 3")
        """
        if isinstance(sep, String):
            sep_: str = sep._value
        else:
            sep_ = str(sep)
        values_: List[Any] = [str(value) for value in self._value]
        joined: String = String(sep_.join(values_))
        self._append_join_expression(joined=joined, sep=sep)
        return joined

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_join_expression(
        self, *, joined: String, sep: Union[str, String]
    ) -> None:
        """
        Append a `join` method expression.

        Parameters
        ----------
        joined : String
            Joined string.
        sep : String or str
            Separator string.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        sep_str: str = value_util.get_value_str_for_expression(value=sep)
        expression: str = (
            f"{joined.variable_name} = {self.variable_name}" f".join({sep_str});"
        )
        expression_data_util.append_js_expression(expression=expression)

    def __str__(self) -> str:
        """
        String conversion method.

        Returns
        -------
        string : str
            Converted value string.
        """
        if not hasattr(self, "_value"):
            return "[]"
        return str(self._value)

    def __repr__(self) -> str:
        """
        Get a representation string of this instance.

        Returns
        -------
        repr_str : str
            Representation string of this instance.
        """
        if not hasattr(self, "_value"):
            repr_str: str = "Array([])"
        else:
            repr_str = f"Array({repr(self._value)})"
        return repr_str

    @final
    @add_debug_info_setting(module_name=__name__)
    def index_of(self, value: _ArrValue) -> Int:
        """
        Search specified value's index and return it.

        Parameters
        ----------
        value : *
            Any value to search.

        Returns
        -------
        index : Int
            Found position of index. If this array does not
            contain a value, this interface returns -1.

        References
        ----------
        - Array class index_of interface
            - https://simon-ritchie.github.io/apysc/en/array_index_of.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([1, 3, 5])
        >>> arr.index_of(3)
        Int(1)
        """
        index: Int = Int(-1, variable_name_suffix=self._variable_name_suffix)
        try:
            index_: int = self._value.index(value)
        except Exception:
            index_ = -1
        index._value = index_
        self._append_index_of_expression(index=index, value=value)
        return index

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_index_of_expression(self, *, index: Int, value: _ArrValue) -> None:
        """
        Append index_of method expression.

        Parameters
        ----------
        index : Int
            Found position of index. If an array does not
            contain a value, this interface returns -1.
        value : *
            Any value to find.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        value_str: str = value_util.get_value_str_for_expression(value=value)
        expression: str = (
            f"{index.variable_name} = {self.variable_name}" f".indexOf({value_str});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : *
            The other value to compare. A list or an Array
            type is acceptable.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        result: Boolean
        if isinstance(other, Array):
            result = Boolean(self._value == other._value)
        else:
            result = Boolean(self._value == other)
            other = self._convert_other_val_to_array(other=other)
        if isinstance(other, VariableNameMixIn):
            self._append_eq_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _convert_other_val_to_array(self, *, other: Any) -> Any:
        """
        If a comparison's other value is list value, then convert
        it to Array instance.

        Parameters
        ----------
        other : *
            The other value to compare.

        Returns
        -------
        converted_val : *
            Converted value. If the other value is a list,
            this value becomes Array type. Otherwise, this
            interface returns its value directly (skips conversion).
        """
        if isinstance(other, list):
            return Array(other)
        return other

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_eq_expression(
        self, *, result: Boolean, other: VariableNameMixIn
    ) -> None:
        """
        Append an __eq__ expression.

        Parameters
        ----------
        result : Boolean
            A result boolean value.
        other : Array
            The other value to compare.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{result.variable_name} = "
            f"_.isEqual({self.variable_name}, {other.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : *
            The other value to compare. A list or an Array
            type is acceptable.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        other = self._convert_other_val_to_array(other=other)
        result: Boolean = self == other
        result = result.not_
        if isinstance(other, VariableNameMixIn):
            self._append_ne_expression(result=result, other=other)
        return result

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ne_expression(
        self, *, result: Boolean, other: VariableNameMixIn
    ) -> None:
        """
        Append a __ne__ expression.

        Parameters
        ----------
        result : Boolean
            A result boolean value.
        other : Array
            The other value to compare.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{result.variable_name} = "
            f"!_.isEqual({self.variable_name}, {other.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

    def __bool__(self) -> bool:
        """
        Get a boolean value whether this array value is empty
        or not.

        Returns
        -------
        result : bool
            If this array value is empty, this interface returns True.
        """
        return bool(self._value)

    @final
    def clear(self) -> None:
        """
        Empty this array's value.

        References
        ----------
        - Array class clear interface
            - https://simon-ritchie.github.io/apysc/en/array_clear.md
        """
        self._value.clear()
        self._append_clear_expression()

    @final
    def _append_clear_expression(self) -> None:
        """
        Append a `clear` interface expression.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{self.variable_name}.splice(0);"
        expression_data_util.append_js_expression(expression=expression)

    _value_snapshots: Optional[Dict[str, List[_ArrValue]]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_value_snapshots",
            value=[*self._value],
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert values if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._value = self._get_snapshot_val_if_exists(
            current_value=self._value,
            snapshot_dict=self._value_snapshots,
            snapshot_name=snapshot_name,
        )

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "Array":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        arr_value : Array
            An initialized array value.
        """
        return Array([])

    @property
    @add_debug_info_setting(module_name=__name__)
    def last_value(self) -> _ArrValue:
        """
        Get an array's last index value.

        Returns
        -------
        last_value : _ArrValue
            An array's last index value.

        Notes
        -----
        - The constructor's `fixed_value_type` setting affects
            this property's value type.
        - If an array is empty, this value becomes `undefined`
            on the JavaScript runtime.

        References
        ----------
        - Array class last_value property
            - https://simon-ritchie.github.io/apysc/en/array_last_value.html

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage(
        ...     stage_width=100,
        ...     stage_height=50,
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )
        >>> arr: ap.Array[ap.Int] = ap.Array([], fixed_value_type=ap.Int)
        >>> last_value: ap.Int = arr.last_value
        >>> ap.assert_undefined(last_value)

        >>> arr.append(ap.Int(10))
        >>> last_value = arr.last_value
        >>> ap.assert_equal(last_value, 10)

        >>> arr.append(ap.Int(20))
        >>> last_value = arr.last_value
        >>> ap.assert_equal(last_value, 20)
        """
        from apysc._expression import expression_data_util
        from apysc._type.any_value import AnyValue
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        if self._fixed_value_type is not None and issubclass(
            self._fixed_value_type,
            InitializeWithBaseValueInterface,
        ):
            last_value: _ArrValue = self._fixed_value_type._initialize_with_base_value()
        elif len(self._value) > 0 and isinstance(self._value[-1], VariableNameMixIn):
            last_value = cast(_ArrValue, self._value[-1])
        else:
            last_value = cast(_ArrValue, AnyValue(None))

        last_value_variable_name: str = validate_variable_name_mixin_type(
            instance=last_value
        ).variable_name
        expression: str = (
            f"{last_value_variable_name} = "
            f"{self.variable_name}[{self.variable_name}.length - 1];"
        )
        expression_data_util.append_js_expression(expression=expression)

        return last_value
