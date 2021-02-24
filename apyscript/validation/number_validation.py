"""Number validation implementations.
"""

from typing import Any
from typing import Union


def validate_num(num: Union[int, float, Any]) -> None:
    """
    Validate specified value is integer or float type.

    Parameters
    ----------
    num : int or float
        Number value to check.

    Raises
    ------
    ValueError
        If specified value is not integer and float value.
    """
    from apyscript.type.number_value_interface import NumberValueInterface
    if isinstance(num, (int, float, NumberValueInterface)):
        return
    raise ValueError(
        f'Specified value is not iteger or float type: {num}'
        f'({type(num)})')


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


def validate_num_is_gt_zero(num: Union[int, float]) -> None:
    """
    Validate specified value is greater than zero.

    Parameters
    ----------
    num : int or float
        Number value to check.

    Raises
    ------
    ValueError
        If specified value is less than or equal to zero.
    """
    if num > 0:
        return
    raise ValueError(f'Specified values is less than or equal to zero: {num}')


def validate_num_is_gte_zero(num: Union[int, float]) -> None:
    """
    Validate specified value is greater than or equal to zero.

    Parameters
    ----------
    num : int or float
        Number value to check.

    Raises
    ------
    ValueError
        If specified value is less than zero.
    """
    if num >= 0:
        return
    raise ValueError(f'Specified values is less than zero: {num}')
