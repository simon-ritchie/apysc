"""Validations related to color.
"""

from string import hexdigits
from typing import Tuple


def validate_hex_color_code_format(hex_color_code: str) -> None:
    """
    Validate a specified hexadecimal color code's format.

    Parameters
    ----------
    hex_color_code : str
        Hexadecimal color code (not including '#').
        e.g., 'ff0000', '666', '0'

    Raises
    ------
    ValueError
        If invalid hex color code specified.
    """
    if not isinstance(hex_color_code, str):
        raise ValueError(
            'Hex color code only supports str type, specified: '
            f'{type(hex_color_code)}')

    char_len: int = len(hex_color_code)
    expected_char_lengths: Tuple[int, int, int] = (1, 3, 6)
    if char_len not in expected_char_lengths:
        raise ValueError(
            'Not supported hex color code number of digits is specified.'
            f'\nSupported number of digits are: {expected_char_lengths}'
            f'\nSpecified: {hex_color_code} ({char_len} digits)')

    for char in hex_color_code:
        if char in hexdigits:
            continue
        raise ValueError(
            'Invalid hexadecimal character is specified.'
            f'\nTarget character: {char}'
            f'\nSupported characters: {hexdigits}')
