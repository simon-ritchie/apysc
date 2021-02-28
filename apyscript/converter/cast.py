"""Implementation of common cast conversion.
"""


from typing import Any
from typing import Union


def to_int_from_float(
        int_or_float: Union[int, float, Any]) -> Any:
    """
    Convert float value to int.

    Parameters
    ----------
    int_or_float : int or float or NumberValueInterface
        Target float value. If integer is specified, conversion
        will be skipped.

    Returns
    -------
    int_val : int or Int
        Converted integer value.
    """
    from apyscript.type.number import Number
    if isinstance(int_or_float, Number):
        from apyscript.type.int import Int
        return Int(int_or_float)
    if not isinstance(int_or_float, float):
        return int_or_float
    return int(int_or_float)


def to_float_from_int(int_or_float: Union[int, float, Any]) -> Any:
    """
    Convert int value to float.

    Parameters
    ----------
    int_or_float : int or float or NumberValueInterface
        Target integer value. If float is specified, conversion will
        be skipped.

    Returns
    -------
    float_val : float or Number
        Converted float value.
    """
    from apyscript.type.int import Int
    if isinstance(int_or_float, Int):
        from apyscript.type.number import Number
        return Number(int_or_float)
    if not isinstance(int_or_float, int):
        return int_or_float
    return float(int_or_float)
