"""Digit validation implementations.
"""

from typing import Union


def validate_digit(digits: Union[int, float]) -> None:
    """
    Validate specified value is integer or float type.

    Parameters
    ----------
    digits : int or float
        Digits value to validate.

    Raises
    ------
    ValueError
        If specified value is not integer and float value.
    """
    if isinstance(digits, (int, float)):
        return
    raise ValueError(
        f'Specified value is not iteger or float type: {digits}'
        f'({type(digits)})')
