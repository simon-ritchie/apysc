"""Size's (width or height) common validation implementation.
"""


from typing import Optional
from typing import Union

from apysc._type.int import Int


def validate_size_is_int(
        size: Union[int, Int], err_msg: Optional[str] = None) -> None:
    """
    Check whether a specified size is an integer or not.

    Parameters
    ----------
    size : Int or int
        Target size (width or height) value.
    err_msg : str or None, default None
        The error message that display at error raised.

    Raises
    ------
    ValueError
        The error message which displays at error raised.
    """
    if isinstance(size, (int, Int)):
        return
    if err_msg is None:
        err_msg = (
            f'Specified size is not integer value: {size}({type(size)})'
        )
    raise ValueError(err_msg)


def validate_size_is_gt_zero(
        size: Union[int, Int], err_msg: Optional[str] = None) -> None:
    """
    Check whether a specified size is greater than zero or not.

    Parameters
    ----------
    size : Int or int
        Target size (width or height) value.
    err_msg : str or None, default None
        The error message which displays at error raised.

    Raises
    ------
    ValueError
        If a specified size is less than or equal to zero.
    """
    if size > 0:
        return
    if err_msg is None:
        err_msg = (
            f'Specified size is not greater than zero: {size}'
        )
    raise ValueError(err_msg)


def validate_size_is_gte_zero(
        size: Union[int, Int], err_msg: Optional[str] = None) -> None:
    """
    Check whether a specified size is greater than or equal
    to zero or not.

    Parameters
    ----------
    size : Int or int
        Target size (width or height) value.
    err_msg : str or None, default None
        The error message which displays at error raised.

    Raises
    ------
    ValueError
        If a specified size is less than zero.
    """
    if size >= 0:
        return
    if err_msg is None:
        err_msg = (
            f'Specified size is not greater than or equal to zero: {size}'
        )
    raise ValueError(err_msg)
