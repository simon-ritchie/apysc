"""The conversion utility to convert a built-in list of str to
an apysc's Array of String.
"""

from typing import List, Optional, Union
from apysc._type.array import Array
from apysc._type.string import String


def list_of_strs_to_array_of_string(
    *,
    optional_list_or_arr: Optional[Union[List[str], Array[String]]],
    variable_name_suffix: str = "",
) -> Optional[Array[String]]:
    """
    Convert a built-in list of str to an apysc's `Array` of `String`.

    Parameters
    ----------
    optional_list_or_arr : Optional[Union[List[str], Array[String]]]
        An optional list of str or array of `String` to convert.
    variable_name_suffix : str, optional
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript debugging.

    Returns
    -------
    converted_value : Optional[Array[String]]
        A converted array of `String` value.
        If the `optional_list_or_arr` is None, this function returns None.
    """
    if optional_list_or_arr is None:
        return None
    if isinstance(optional_list_or_arr, list):
        converted_value: Array[String] = Array(
            [
                String(str_value, variable_name_suffix=variable_name_suffix)
                for str_value in optional_list_or_arr
            ],
            variable_name_suffix=variable_name_suffix,
        )
        return converted_value
    return optional_list_or_arr
