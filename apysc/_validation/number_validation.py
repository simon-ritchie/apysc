"""Number validation implementations.

Mainly following interfaces are defined:

- validate_num
    - Validate a specified value as an integer or float type.
- validate_integer
    - Validate whether a specified value is an integer or not.
- validate_int_is_zero_or_one
    - Validate specified integer value is zero or one.
- validate_num_is_gt_zero
    - Validate specified value is greater than zero.
- validate_num_is_gte_zero
    - Validate whether a specified value is greater than or
    equal to zero.
- validate_nums_are_int_and_gt_zero
    - Validate specified number values are greater integer and
    greater than zero.
- validate_num_is_0_to_1_range
    - Validate whether a specified number is from 0.0 to 1.0.
"""

from typing import List
from typing import Union

from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.number_value_interface import NumberValueInterface


def validate_num(
        *, num: Union[int, float, Int, Number],
        additional_err_msg: str = '') -> None:
    """
    Validate a specified value as an integer or float type.

    Parameters
    ----------
    num : int or float or Int or Number
        Number value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value is not an integer and float value.
    """
    if isinstance(
            num,
            (int, float, NumberValueInterface)):
        return
    if additional_err_msg != '':
        additional_err_msg = f'\n{additional_err_msg}'
    raise ValueError(
        f'Specified value is not iteger or float type: {num}'
        f'({type(num)}){additional_err_msg}')


def validate_integer(
        *, integer: Union[int, Int],
        additional_err_msg: str = '') -> None:
    """
    Validate whether a specified value is an integer or not.

    Parameters
    ----------
    integer : Int or int
        Integer value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value is not an integer.
    """
    if isinstance(integer, (int, Int)):
        return
    if additional_err_msg != '':
        additional_err_msg = f'\n{additional_err_msg}'
    raise ValueError(
        f'A specified value is not integer: {integer}({type(integer)})'
        f'{additional_err_msg}')


def validate_int_is_zero_or_one(*, integer: Union[int, Int]) -> None:
    """
    Validate specified integer value is zero or one.

    Notes
    -----
    This interface skips validation if an argument
    value is not an Int or int instance.

    Parameters
    ----------
    integer : Int or int
        Integer value to check.

    Raises
    ------
    ValueError
        If a specified integer is not zero and one.
    """
    if not isinstance(integer, (int, Int)):
        return
    if integer == 0 or integer == 1:
        return
    raise ValueError(
        f'Specified integer value is not zero and one: {integer}')


def validate_num_is_gt_zero(
        *, num: Union[int, float, Int, Number],
        additional_err_msg: str = '') -> None:
    """
    Validate specified value is greater than zero.

    Parameters
    ----------
    num : int or float or Int or Number
        Number value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value is less than or equal to zero.
    """
    if isinstance(num, NumberValueInterface):
        if num._value > 0:
            return
    elif num > 0:
        return
    if additional_err_msg != '':
        additional_err_msg = f'\n{additional_err_msg}'
    raise ValueError(
        f'Specified values is less than or equal to zero: {num}'
        f'{additional_err_msg}')


def validate_num_is_gte_zero(
        *, num: Union[int, float, Int, Number],
        additional_err_msg: str = '') -> None:
    """
    Validate whether a specified value is greater than or equal to zero.

    Parameters
    ----------
    num : int or float or Int or Number
        Number value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value is less than zero.
    """
    if isinstance(num, NumberValueInterface):
        if num._value >= 0:
            return
    elif num >= 0:
        return
    if additional_err_msg != '':
        additional_err_msg = f'\n{additional_err_msg}'
    raise ValueError(
        f'Specified values is less than zero: {num}{additional_err_msg}')


def validate_nums_are_int_and_gt_zero(*, nums: List[Union[int, Int]]) -> None:
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


def validate_num_is_0_to_1_range(
        *, alpha: Union[float, NumberValueInterface]) -> None:
    """
    Validate whether a specified number is from 0.0 to 1.0.

    Parameters
    ----------
    alpha : float or Number
        Opacity value to check.

    Raises
    ------
    ValueError
        If a specified opacity is out of the 0.0 to 1.0 range.
    """
    lt_err_msg: str = 'Can\'t specify alpha value less than 0.0: '
    gt_err_msg: str = 'Can\'t specify alpha value greater than 1.0: '
    if isinstance(alpha, NumberValueInterface):
        if alpha._value < 0.0:
            raise ValueError(f'{lt_err_msg}{alpha}')
        if alpha._value > 1.0:
            raise ValueError(f'{gt_err_msg}{alpha}')
    else:
        if alpha < 0.0:
            raise ValueError(f'{lt_err_msg}{alpha}')
        if alpha > 1.0:
            raise ValueError(f'{gt_err_msg}{alpha}')
