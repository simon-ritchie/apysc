"""Number validation implementations.

Mainly following interfaces are defined:

- validate_num
    Validate specified value is integer or float type.
- validate_integer
    Validate specified value is integer.
- validate_int_is_zero_or_one
    Validate specified integer value is zero or one.
- validate_num_is_gt_zero
    Validate specified value is greater than zero.
- validate_num_is_gte_zero
    Validate specified value is greater than or equal to zero.
- validate_nums_are_int_and_gt_zero
    Validate specified number values are greater integer and
    greater than zero.
"""

from typing import List
from typing import Union

from apysc import Int
from apysc import Number


def validate_num(
        num: Union[int, float, Int, Number]) -> None:
    """
    Validate specified value is integer or float type.

    Parameters
    ----------
    num : int or float or Int or Number
        Number value to check.

    Raises
    ------
    ValueError
        If specified value is not integer and float value.
    """
    from apysc._type.number_value_interface import NumberValueInterface
    if isinstance(
            num,
            (int, float, NumberValueInterface)):
        return
    raise ValueError(
        f'Specified value is not iteger or float type: {num}'
        f'({type(num)})')


def validate_integer(integer: Union[int, Int]) -> None:
    """
    Validate specified value is integer.

    Parameters
    ----------
    integer : int or Int
        Integer value to check.

    Raises
    ------
    ValueError
        If specified value is not integer.
    """
    from apysc import Int
    if isinstance(integer, (int, Int)):
        return
    raise ValueError(
        f'Specified value is not integer: {integer}({type(integer)})')


def validate_int_is_zero_or_one(integer: Union[int, Int]) -> None:
    """
    Validate specified integer value is zero or one.

    Notes
    -----
    If argument value is not int or Int instance, then validation
    will be skipped.

    Parameters
    ----------
    integer : int or Int
        Integer value to check.

    Raises
    ------
    ValueError
        If specified integer is not zero and one.
    """
    from apysc import Int
    if not isinstance(integer, (int, Int)):
        return
    if integer == 0 or integer == 1:
        return
    raise ValueError(
        f'Specified integer value is not zero and one: {integer}')


def validate_num_is_gt_zero(num: Union[int, float, Int, Number]) -> None:
    """
    Validate specified value is greater than zero.

    Parameters
    ----------
    num : int or float or Int or Number
        Number value to check.

    Raises
    ------
    ValueError
        If specified value is less than or equal to zero.
    """
    if num > 0:
        return
    raise ValueError(f'Specified values is less than or equal to zero: {num}')


def validate_num_is_gte_zero(num: Union[int, float, Int, Number]) -> None:
    """
    Validate specified value is greater than or equal to zero.

    Parameters
    ----------
    num : int or float or Int or Number
        Number value to check.

    Raises
    ------
    ValueError
        If specified value is less than zero.
    """
    if num >= 0:
        return
    raise ValueError(f'Specified values is less than zero: {num}')


def validate_nums_are_int_and_gt_zero(nums: List[Union[int, Int]]) -> None:
    """
    Validate specified number values are greater integer and
    greater than zero.

    Parameters
    ----------
    nums : list
        Integer values to check.

    Raises
    ------
    ValueError
        If any value is not integer type or less than one.
    """
    for num in nums:
        validate_integer(integer=num)
        validate_num_is_gt_zero(num=num)
