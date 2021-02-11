"""Digit validation implementations.
"""

from typing import Union


def validate_digit(digits: Union[int, float]) -> None:
    """
    Validate specified value is integer or float type.

    Parameters
    ----------
    digits : int or float
        Digits value to check.

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


def validate_integer(integer: int) -> None:
    """
    Validate specified value is integer.

    Parameters
    ----------
    integer : int
        Integer value to check.

    Raises
    ------
    ValueError
        If specified value is not integer.
    """
    if isinstance(integer, int):
        return
    raise ValueError(
        f'Specified value is not integer: {integer}({type(integer)})')
