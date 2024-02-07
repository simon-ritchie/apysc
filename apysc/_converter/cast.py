"""Implementation of common cast conversion.

Mainly following interfaces are defined.

- to_int_from_float
    Convert float value to int.
- to_float_from_int
    Convert int value to float.
- to_bool_from_int
    Convert int value to bool.
"""

from typing import Any
from typing import Union

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number_value_mixin import NumberValueMixIn


@add_debug_info_setting(module_name=__name__)
def to_int_from_float(*, int_or_float: Union[int, float, NumberValueMixIn]) -> Any:
    """
    Convert float value to int.

    Parameters
    ----------
    int_or_float : int or float or Int or Number
        Target float value. If an integer is specified,
        this interface skips the conversion.

    Returns
    -------
    int_val : Int or int
        Converted integer value.
    """
    from apysc._type.number import Number

    if isinstance(int_or_float, Number):
        return Int(int_or_float)
    if not isinstance(int_or_float, float):
        return int_or_float
    return int(int_or_float)


@add_debug_info_setting(module_name=__name__)
def to_float_from_int(*, int_or_float: Union[int, float, NumberValueMixIn]) -> Any:
    """
    Convert int value to float.

    Parameters
    ----------
    int_or_float : int or float or Int or Number
        A Target integer value. If a float is specified,
        this interface skips the conversion.

    Returns
    -------
    float_val : float or Number
        Converted float value.
    """
    from apysc._type.number import Number

    if isinstance(int_or_float, Int):
        return Number(int_or_float)
    if not isinstance(int_or_float, int):
        return int_or_float
    return float(int_or_float)


@add_debug_info_setting(module_name=__name__)
def to_bool_from_int(*, integer: Union[int, Int]) -> bool:
    """
    Convert int value to bool.

    Parameters
    ----------
    integer : Int or int
        Integer value to convert.

    Returns
    -------
    bool_val : bool
        Converted boolean value.

    Raises
    ------
    ValueError
        If an argument value isn't zero or one.
    """
    from apysc._validation import number_validation

    number_validation.validate_int_is_zero_or_one(integer=integer)
    if integer == 0:
        return False
    return True
