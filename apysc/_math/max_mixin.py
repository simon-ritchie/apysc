"""Class implementation for the max-related mix-in.
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


class MaxMixIn:
    @classmethod
    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_nums_array(arg_position_index=1)
    def max(
        cls,
        values: Array,
    ) -> Number:
        """
        Get a maximum number from a specified array's values.

        Parameters
        ----------
        values : Array[Union[Int, Number, int, float]]
            An array of numbers.

        Returns
        -------
        max_value : Number
            Maximum number in an array.

        References
        ----------
        - Math max interface
            - https://simon-ritchie.github.io/apysc/en/math_max.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> arr: ap.Array = ap.Array([10, 9.5, ap.Int(8), ap.Number(8.5)])
        >>> max_value: ap.Number = ap.Math.max(values=arr)
        >>> max_value
        Number(10.0)
        """
        from apysc._expression import expression_data_util

        max_value_variable_name_suffix: str = (
            _get_max_value_variable_name_suffix_from_arr(arr=values)
        )
        max_value: Number = Number(
            0, variable_name_suffix=max_value_variable_name_suffix
        )
        max_float_value: float = _get_max_float_value(values=values)
        max_value._value = max_float_value
        expression: str = (
            f"{max_value.variable_name} = {values.variable_name}.reduce("
            "function (a, b) {return Math.max(a, b)});"
        )
        expression_data_util.append_js_expression(expression=expression)
        return max_value


def _get_max_value_variable_name_suffix_from_arr(*, arr: Array) -> str:
    """
    Get a maximum value's variable name suffix from a specified array.

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
    max_value: float = max(values)
    max_value_index: int = values.index(max_value)
    max_value_: Any = arr._value[max_value_index]
    if isinstance(max_value_, VariableNameSuffixMixIn):
        return max_value_._variable_name_suffix
    return ""


def _get_max_float_value(*, values: Array[Union[Int, Number, int, float]]) -> float:
    """
    Get a maximum float value from a specified array.

    Parameters
    ----------
    values : Array[Union[Int, Number, int, float]]
        An array of numbers.

    Returns
    -------
    max_value : float
        A maximum float value.
    """
    values_: List[float] = []
    for value in values._value:
        if isinstance(value, (Int, Number)):
            values_.append(float(value._value))
            continue
        values_.append(float(value))
    max_value: float = max(values_)
    return max_value
