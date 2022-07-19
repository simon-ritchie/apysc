"""String's validation implementations.
"""

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
    if isinstance(string, str):
        return
    if isinstance(string, String):
        return
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    raise ValueError(
        f"A specified value is not str type: {type(string)}" f"{additional_err_msg}"
    )


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
    if isinstance(string, str):
        return
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    raise ValueError(
        f"A specified value is not str type: {type(string)}" f"{additional_err_msg}"
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
    validate_string_type(string=string)
    if isinstance(string, str):
        if string != "":
            return
    elif isinstance(string, String):
        if string._value != "":
            return
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    raise ValueError(f"Empty string is not acceptable.{additional_err_msg}")
