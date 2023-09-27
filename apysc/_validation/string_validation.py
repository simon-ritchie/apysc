"""String's validation implementations.
"""

from typing import Any
from typing import Union

from apysc._type.string import String


def validate_string_type(
    *, string: Union[str, String], additional_err_msg: str = ""
) -> None:
    """
    Validate a specified string's type is str.

    Parameters
    ----------
    string : String or str
        A string to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        - If a non-string value is specified.
    """
    from apysc._validation import validation_common_utils

    if isinstance(string, str):
        return
    if isinstance(string, String):
        return
    err_msg: str = f"A specified value is not str type: {type(string)}"
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)


def validate_builtin_string_type(*, string: str, additional_err_msg: str = "") -> None:
    """
    Validate a specified string's type is Python built-in's str.

    Parameters
    ----------
    string : str
        A string to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        - If a non-string value is specified.
    """
    from apysc._validation import validation_common_utils

    if isinstance(string, str):
        return
    err_msg: str = f"A specified value is not str type: {type(string)}"
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)


def validate_apysc_string_type(*, string: Any) -> String:
    """
    Validate whether the specified argument is the apysc's `String`
    type or not.

    Parameters
    ----------
    string : Any
        The target string to check.

    Returns
    -------
    string : String
        An apysc's string.

    Raises
    ------
    TypeError
        If the specified argument is not the apysc's `String` type.
    """
    if isinstance(string, String):
        return string
    raise TypeError(
        "The specified argument is not the apysc's `String` type: "
        f"{type(string).__name__}"
    )


def validate_not_empty_string(
    *, string: Union[str, String], additional_err_msg: str = ""
) -> None:
    """
    Validate whether a specified string is not empty.

    Parameters
    ----------
    string : String or str
        String to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        - If empty string ('' or "") is specified.
        - If specified value is not str type.
    """
    from apysc._validation import validation_common_utils

    validate_string_type(string=string)
    if isinstance(string, str):
        if string != "":
            return
    elif isinstance(string, String):
        if string._value != "":
            return
    err_msg: str = "Empty string is not acceptable."
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)
