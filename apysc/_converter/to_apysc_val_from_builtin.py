"""Each interface to get an apysc value from a Python built-in one.
"""

from typing import Union

from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String


def get_copied_int_from_builtin_val(
        *, integer: Union[int, Int]) -> Int:
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
    import apysc as ap
    with ap.DebugInfo(
            callable_=get_copied_int_from_builtin_val, locals_=locals(),
            module_name=__name__):
        if isinstance(integer, int):
            copied: ap.Int = ap.Int(integer)
        else:
            copied = integer._copy()
        return copied


def get_copied_number_from_builtin_val(
        *, float_or_num: Union[float, Number]) -> Number:
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
    import apysc as ap
    with ap.DebugInfo(
            callable_=get_copied_number_from_builtin_val, locals_=locals(),
            module_name=__name__):
        if isinstance(float_or_num, float):
            copied: ap.Number = ap.Number(float_or_num)
        else:
            copied = float_or_num._copy()
        return copied


def get_copied_string_from_builtin_val(
        *, string: Union[str, String]) -> String:
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
    import apysc as ap
    with ap.DebugInfo(
            callable_=get_copied_string_from_builtin_val, locals_=locals(),
            module_name=__name__):
        if isinstance(string, str):
            copied: ap.String = ap.String(string)
        else:
            copied = string._copy()
        return copied


def get_copied_boolean_from_builtin_val(
        *, bool_val: Union[bool, Boolean]) -> Boolean:
    """
    Get a copied Boolean value from a Python built-in bool.

    Parameters
    ----------
    bool_val : bool
        Target bool value.

    Returns
    -------
    copied : Boolean
        Copied Boolean value.
    """
    import apysc as ap
    with ap.DebugInfo(
            callable_=get_copied_boolean_from_builtin_val, locals_=locals(),
            module_name=__name__):
        if isinstance(bool_val, bool):
            copied: ap.Boolean = ap.Boolean(bool_val)
        else:
            copied = bool_val._copy()
        return copied
