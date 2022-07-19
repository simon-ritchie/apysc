"""Each interface to get an apysc value from a Python built-in one.
"""

from typing import Union

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String


@add_debug_info_setting(module_name=__name__)
def get_copied_int_from_builtin_val(
    *, integer: Union[int, Int], variable_name_suffix: str = ""
) -> Int:
    """
    Get a copied Int value from a Python built-in int.

    Parameters
    ----------
    integer : int or Int
        Target integer value.
    variable_name_suffix : str, default ''
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript's debugging.

    Returns
    -------
    copied : Int
        Copied Int value.
    """
    import apysc as ap

    if isinstance(integer, int):
        copied: ap.Int = ap.Int(integer, variable_name_suffix=variable_name_suffix)
    else:
        copied = integer._copy()
    return copied


@add_debug_info_setting(module_name=__name__)
def get_copied_number_from_builtin_val(
    *, float_or_num: Union[float, Number], variable_name_suffix: str = ""
) -> Number:
    """
    Get a copied number value from a Python built-in float.

    Parameters
    ----------
    float_or_num : float or Number
        Target float (or Number) value.
    variable_name_suffix : str, default ''
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript's debugging.

    Returns
    -------
    copied : Number
        Copied Number value.
    """
    import apysc as ap

    if isinstance(float_or_num, float):
        copied: ap.Number = ap.Number(
            float_or_num, variable_name_suffix=variable_name_suffix
        )
    else:
        copied = float_or_num._copy()
    return copied


@add_debug_info_setting(module_name=__name__)
def get_copied_string_from_builtin_val(
    *, string: Union[str, String], variable_name_suffix: str = ""
) -> String:
    """
    Get a copied String value from a Python built-in str.

    Parameters
    ----------
    string : str or String
        Target string value.
    variable_name_suffix : str, default ''
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript's debugging.

    Returns
    -------
    copied : String
        Copied String value.
    """
    import apysc as ap

    if isinstance(string, str):
        copied: ap.String = ap.String(string, variable_name_suffix=variable_name_suffix)
    else:
        copied = string._copy()
    return copied


@add_debug_info_setting(module_name=__name__)
def get_copied_boolean_from_builtin_val(
    *, bool_val: Union[bool, Boolean], variable_name_suffix: str = ""
) -> Boolean:
    """
    Get a copied Boolean value from a Python built-in bool.

    Parameters
    ----------
    bool_val : bool or Boolean
        Target bool value.
    variable_name_suffix : str, default ''
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript's debugging.

    Returns
    -------
    copied : Boolean
        Copied Boolean value.
    """
    import apysc as ap

    if isinstance(bool_val, bool):
        copied: ap.Boolean = ap.Boolean(
            bool_val, variable_name_suffix=variable_name_suffix
        )
    else:
        copied = bool_val._copy()
    return copied
