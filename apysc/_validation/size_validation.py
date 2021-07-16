"""Size's (width or height) common validation implementation.
"""


from typing import Optional
from typing import Union

import apysc as ap


def validate_size_is_int(
        size: Union[int, ap.Int], err_msg: Optional[str] = None) -> None:
    """
    Check that whether size is integer or not.

    Parameters
    ----------
    size : int or Int
        Target size (width or height) value.
    err_msg : str or None, default None
        The error message that display at error raised.

    Raises
    ------
    ValueError
        If not integer value is specified.
    """
    if isinstance(size, (int, ap.Int)):
        return
    if err_msg is None:
        err_msg = (
            f'Specified size is not integer value: {size}({type(size)})'
        )
    raise ValueError(err_msg)


def validate_size_is_gt_zero(
        size: Union[int, ap.Int], err_msg: Optional[str] = None) -> None:
    """
    Check that whether size is greater than zero or not.

    Parameters
    ----------
    size : int or Int
        Target size (width or height) value.
    err_msg : str or None, default None
        The error message that display at error raised.

    Raises
    ------
    ValueError
        If size is less than or equal to zero.
    """
    if size > 0:
        return
    if err_msg is None:
        err_msg = (
            f'Specified size is not greater than zero: {size}'
        )
    raise ValueError(err_msg)


def validate_size_is_gte_zero(
        size: Union[int, ap.Int], err_msg: Optional[str] = None) -> None:
    """
    Check that whether size is greater than or equal to zero or not.

    Parameters
    ----------
    size : int or Int
        Target size (width or height) value.
    err_msg : str or None, default None
        The error message that display at error raised.

    Raises
    ------
    ValueError
        If size is less than zero.
    """
    if size >= 0:
        return
    if err_msg is None:
        err_msg = (
            f'Specified size is not greater than or equal to zero: {size}'
        )
    raise ValueError(err_msg)
