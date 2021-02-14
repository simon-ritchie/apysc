"""Implementation of common cast conversion.
"""


from typing import Union


def to_int_from_float(int_or_float: Union[int, float]) -> int:
    """
    Convert float value to int.

    Parameters
    ----------
    int_or_float : int or float
        Target float value. If integer is specified, conversion
        will be skipped.

    Returns
    -------
    int_val : int
        Converted integer value.
    """
    if not isinstance(int_or_float, float):
        return int_or_float
    return int(int_or_float)


def to_float_from_int(int_or_float: Union[int, float]) -> float:
    """
    Convert int value to float.

    Parameters
    ----------
    int_or_float : int or float
        Target integer value. If float is specified, conversion will
        be skipped.

    Returns
    -------
    float_val : float
        Converted float value.
    """
    if not isinstance(int_or_float, int):
        return int_or_float
    return float(int_or_float)
