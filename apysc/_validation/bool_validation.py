"""Boolean value's validation implementations.
"""

from typing import Union

from apysc._type.boolean import Boolean


def validate_bool(*, value: Union[bool, Boolean], additional_err_msg: str = "") -> None:
    """
    Validate whether a specified value is `bool` or `Boolean` type.

    Parameters
    ----------
    value : bool or Boolean
        A boolean value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value isn't the `bool` or `Boolean` type.
    """
    from apysc._type import type_util
    from apysc._validation import validation_common_utils

    is_bool: bool = type_util.is_bool(value=value)
    if is_bool:
        return
    err_msg: str = f"A specified value is not the bool or Boolean type: {type(value)}"
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)


def validate_builtin_bool(*, value: bool, additional_err_msg: str = "") -> None:
    """
    Validate whether a specified value is the built-in's
    `bool` type.

    Parameters
    ----------
    value : bool
        A boolean value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value isn't the `bool` type.
    """
    from apysc._validation import validation_common_utils

    if isinstance(value, bool):
        return
    err_msg: str = f"A specified value is not the bool type: {type(value)}"
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)
