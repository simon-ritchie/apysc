"""Each interface to get an apysc value from a Python built-in one.
"""

from typing import Union

import apysc as ap


def get_copied_int_from_builtin_val(
        integer: Union[int, ap.Int]) -> ap.Int:
    """
    Get a copied Int value from a Python built-in int.

    Parameters
    ----------
    integer : int or Int
        Target integer value.

    Returns
    -------
    copied : Int
        Copied Int value.
    """
    with ap.DebugInfo(
            callable_=get_copied_int_from_builtin_val, locals_=locals(),
            module_name=__name__):
        if isinstance(integer, int):
            copied: ap.Int = ap.Int(integer)
        else:
            copied = integer._copy()
        return copied


def get_copied_number_from_builtin_val(
        float_or_num: Union[float, ap.Number]) -> ap.Number:
    """
    Get a copied number value from a Python built-in float.

    Parameters
    ----------
    float_or_num : float or Number
        Target float (or Number) value.

    Returns
    -------
    num : Number
        Copied Number value.
    """
    with ap.DebugInfo(
            callable_=get_copied_number_from_builtin_val, locals_=locals(),
            module_name=__name__):
        if isinstance(float_or_num, float):
            copied: ap.Number = ap.Number(float_or_num)
        else:
            copied = float_or_num._copy()
        return copied


def get_copied_string_from_builtin_val(
        string: Union[str, ap.String]) -> ap.String:
    """
    Get a copied String value from a Python built-in str.

    Parameters
    ----------
    string : str or String
        Target string value.

    Returns
    -------
    copied : String
        Copied String value.
    """
    with ap.DebugInfo(
            callable_=get_copied_string_from_builtin_val, locals_=locals(),
            module_name=__name__):
        if isinstance(string, str):
            copied: ap.String = ap.String(string)
        else:
            copied = string._copy()
        return copied
