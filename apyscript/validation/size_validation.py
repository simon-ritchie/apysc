"""Size's (width or height) common utility implementation.
"""


def validate_size_is_int(size: int, err_msg: str) -> None:
    """
    Check that whether size is integer or not.

    Parameters
    ----------
    size : int
        Target size (width or height) value.
    err_msg : str
        The error message that display at error raised.

    Raises
    ------
    ValueError
        If not integer value is specified.
    """
    if isinstance(size, int):
        return
    raise ValueError(err_msg)


def validate_size_is_greater_than_zero(size: int, err_msg: str) -> None:
    """
    Check that whether size is greater than zero or not.

    Parameters
    ----------
    size : int
        Target size (width or height) value.
    err_msg : str
        The error message that display at error raised.

    Raises
    ------
    ValueError
        If size is less than or equal to zero.
    """
    if size > 0:
        return
    raise ValueError(err_msg)
