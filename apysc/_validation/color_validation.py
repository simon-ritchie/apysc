"""Validations related to color.
"""

from string import hexdigits
from typing import Tuple
from typing import TypeVar

from apysc._type.string import String

StrOrString = TypeVar("StrOrString", str, String)


def validate_hex_color_code_format(
    *, hex_color_code: StrOrString, additional_err_msg: str = ""
) -> None:
    """
    Validate a specified hexadecimal color code format.

    Parameters
    ----------
    hex_color_code : str
        Hexadecimal color code (not including '#').
        e.g., 'ff0000', '666', '0'.
        A blank string is also acceptable.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If invalid hex color code specified.
    """
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    if not isinstance(hex_color_code, (str, String)):
        raise ValueError(
            "Hex color code only supports str type, specified: "
            f"{type(hex_color_code)}{additional_err_msg}"
        )

    if isinstance(hex_color_code, String):
        value_: str = hex_color_code._value
    else:
        value_ = hex_color_code

    char_len: int = len(value_)
    expected_char_lengths: Tuple[int, int, int, int] = (0, 1, 3, 6)
    if char_len not in expected_char_lengths:
        raise ValueError(
            "Not supported hex color code number of digits is specified."
            f"\nSupported number of digits are: {expected_char_lengths}"
            f"\nSpecified: {hex_color_code} ({char_len} digits)"
            f"{additional_err_msg}"
        )

    for char in value_:
        if char in hexdigits:
            continue
        raise ValueError(
            "Invalid hexadecimal character is specified."
            f"\nTarget character: {char}"
            f"\nSupported characters: {hexdigits}"
            f"{additional_err_msg}"
        )
