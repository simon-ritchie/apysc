"""Common utilities for each validation interface.
"""


def append_additional_err_msg(
    *,
    err_msg: str,
    additional_err_msg: str,
) -> str:
    """
    Append an additional error message to a specified error message.

    Parameters
    ----------
    err_msg : str
        An error message.
    additional_err_msg : str
        An additional error message.

    Returns
    -------
    err_msg : str
        A result error message.
    """
    if not additional_err_msg:
        return err_msg
    err_msg += f"\n{additional_err_msg}"
    return err_msg
