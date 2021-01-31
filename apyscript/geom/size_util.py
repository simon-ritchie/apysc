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
