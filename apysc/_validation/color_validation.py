"""Validations related to color.
"""

from string import hexdigits
from typing import Tuple
from typing import TypeVar
from typing import Union

from apysc._type.number_value_interface import NumberValueInterface
from apysc._type.string import String

StrOrString = TypeVar('StrOrString', str, String)


def validate_hex_color_code_format(hex_color_code: StrOrString) -> None:
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
    if not isinstance(hex_color_code, (str, String)):
        raise ValueError(
            'Hex color code only supports str type, specified: '
            f'{type(hex_color_code)}')

    if isinstance(hex_color_code, String):
        value_: str = hex_color_code._value
    else:
        value_ = hex_color_code

    char_len: int = len(value_)
    expected_char_lengths: Tuple[int, int, int] = (1, 3, 6)
    if char_len not in expected_char_lengths:
        raise ValueError(
            'Not supported hex color code number of digits is specified.'
            f'\nSupported number of digits are: {expected_char_lengths}'
            f'\nSpecified: {hex_color_code} ({char_len} digits)')

    for char in value_:
        if char in hexdigits:
            continue
        raise ValueError(
            'Invalid hexadecimal character is specified.'
            f'\nTarget character: {char}'
            f'\nSupported characters: {hexdigits}')


def validate_alpha_range(
        alpha: Union[float, NumberValueInterface]) -> None:
    """
    Validate specified alpha (opacity) value's range.

    Parameters
    ----------
    alpha : float or Number
        Opacity value to check.

    Raises
    ------
    ValueError
        If specified opacity is out of 0.0 to 1.0 range.
    """
    if alpha < 0.0:
        raise ValueError(
            f'Can\'t specify alpha value less than 0.0: {alpha}')
    if alpha > 1.0:
        raise ValueError(
            f'Can\'t specify alpha value greater than 1.0: {alpha}')
