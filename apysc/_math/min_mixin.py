"""Class implementtion for the min-related mix-in.
"""

from typing import List, Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.array import Array
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class MinMixIn:
    @classmethod
    @final
    @add_debug_info_setting(module_name=__name__)
    def min(
        cls,
        values: Array[Union[Int, Number, int, float]],
    ) -> Union[Int, Number]:
        """
        Get a minimum number from a specified array's values.

        Parameters
        ----------
        values : Array[Union[Int, Number, int, float]]
            An array of numbers.

        Returns
        -------
        min_value : Union[Int, Number]
            Minimum number in an array.
        """
        all_values_are_int: bool = _all_values_are_int(values=values)
        pass


def _all_values_are_int(*, values: Array[Union[Int, Number, int, float]]) -> bool:
    """
    Get a boolean value indicating whether all values in an array are int.

    Parameters
    ----------
    values : Array[Union[Int, Number, int, float]]
        An array of numbers.

    Returns
    -------
    result : bool
        If values are all int, this interface returns True.
    """
    for value in values._value:
        if not isinstance(value, (int, Int)):
            return False
    return True
