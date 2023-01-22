"""Class implementtion for the min-related mix-in.
"""

from typing import List, Union, TypeVar

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.array import Array
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
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
        """
        import apysc as ap

        min_value = Number(0)
        min_float_value: float = _get_min_float_value(values=values)
        min_value._value = min_float_value
        expression: str = (
            f"{min_value.variable_name} = {values.variable_name}.reduce("
            "function (a, b) {return Math.min(a, b)});"
        )
        ap.append_js_expression(expression=expression)
        return min_value


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