"""Implementation of common geometry conversion.
"""


from typing import Union


def to_int_from_float(int_or_float: Union[int, float]) -> int:
    """
    Convert geometry float value to int.

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
