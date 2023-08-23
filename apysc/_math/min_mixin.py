"""Class implementation for the min-related mix-in.
"""

from typing import Any
from typing import List
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class MinMixIn:
    @classmethod
    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_nums_array(arg_position_index=1)
    def min(
        cls,
        values: Array,
    ) -> Number:
        """
        Get a minimum number from a specified array's values.

        Parameters
        ----------
        values : Array[Union[Int, Number, int, float]]
            An array of numbers.

        Returns
        -------
        min_value : Number
            Minimum number in an array.

        References
        ----------
        - Math min interface
            - https://simon-ritchie.github.io/apysc/en/math_min.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])
        >>> min_value: ap.Number = ap.Math.min(values=arr)
        >>> min_value
        Number(8.0)
        """
        from apysc._expression import expression_data_util

        min_value_variable_name_suffix: str = (
            _get_min_value_variable_name_suffix_from_arr(arr=values)
        )
        min_value: Number = Number(
            0,
            variable_name_suffix=min_value_variable_name_suffix,
        )
        min_float_value: float = _get_min_float_value(values=values)
        min_value._value = min_float_value
        expression: str = (
            f"{min_value.variable_name} = {values.variable_name}.reduce("
            "function (a, b) {return Math.min(a, b)});"
        )
        expression_data_util.append_js_expression(expression=expression)
        return min_value


def _get_min_value_variable_name_suffix_from_arr(*, arr: Array) -> str:
    """
    Get a minimum value's variable name suffix from a specified array.

    Parameters
    ----------
    arr : Array
        An array of numbers.

    Returns
    -------
    suffix : str
        An extracted variable name suffix.
    """
    from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn

    values: List[float] = [float(value) for value in arr._value]
    min_value: float = min(values)
    min_value_index: int = values.index(min_value)
    min_value_: Any = arr._value[min_value_index]
    if isinstance(min_value_, VariableNameSuffixMixIn):
        return min_value_._variable_name_suffix
    return ""


def _get_min_float_value(*, values: Array[Union[Int, Number, int, float]]) -> float:
    """
    Get a minimum float value from a specified array.

    Parameters
    ----------
    values : Array[Union[Int, Number, int, float]]
        An array of numbers.

    Returns
    -------
    min_value : float
        A minimum float value.
    """
    values_: List[float] = []
    for value in values._value:
        if isinstance(value, (Int, Number)):
            values_.append(float(value._value))
            continue
        values_.append(float(value))
    min_value: float = min(values_)
    return min_value
