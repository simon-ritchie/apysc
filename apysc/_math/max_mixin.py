"""Class implementation for the max-related mix-in.
"""

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
        """
        import apysc as ap

        max_value: Number = Number(0)
        max_float_value: float = _get_max_float_value(values=values)
        max_value._value = max_float_value
        expression: str = (
            f"{max_value.variable_name} = {values.variable_name}.reduce("
            "function (a, b) {return Math.max(a, b)});"
        )
        ap.append_js_expression(expression=expression)
        return max_value


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
