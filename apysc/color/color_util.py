"""Color related implementations.
"""

from typing import Any
from typing import TypeVar

from apysc import String

StrOrString = TypeVar('StrOrString', str, String)


def complement_hex_color(
        hex_color_code: StrOrString) -> StrOrString:
    """
    Complement hex color for convenience, for instance, add # prefix or
    three digits to six digits, upper case to lower case etc.

    Parameters
    ----------
    hex_color_code : str or String
        Hexadecimal color code. e.g., 'ff0000', '#666', '#0'

    Returns
    -------
    complemented_hex_color_code : str or String
        Result hex color code. e.g., '#ff0000', '#666666, '#000000'
    """
    from apysc.html import html_util
    from apysc.validation import color_validation
    hex_color_code = html_util.remove_first_selector_symbol_char(
        str_val=hex_color_code)

    color_validation.validate_hex_color_code_format(
        hex_color_code=hex_color_code)
    if isinstance(hex_color_code, String):
        value_: str = hex_color_code.value
    else:
        value_ = hex_color_code
    char_len = len(value_)
    if char_len == 1:
        value_ = _fill_one_digit_hex_color_code(
            hex_color_code=value_)
    elif char_len == 3:
        value_ = _fill_three_digit_hex_color_code(
            hex_color_code=value_)
    value_ = value_.lower()
    value_ = f'#{value_}'

    if isinstance(hex_color_code, String):
        hex_color_code.value = value_
        _append_complement_hex_color_expression(
            hex_color_code=hex_color_code)
    else:
        hex_color_code = value_  # type: ignore
    return hex_color_code  # type: ignore


def _append_complement_hex_color_expression(
        hex_color_code: Any) -> None:
    """
    Append complement_hex_color function's expression to file.

    Parameters
    ----------
    hex_color_code : String
        Complemented hex color code string.
    """
    from apysc.expression import expression_file_util
    hex_color_code_: String = hex_color_code
    var_name: str = hex_color_code_.variable_name
    expression: str = (
        f'var str_length = {var_name}.length;'
        '\nif (str_length === 1) {'
        f'\n  {var_name} = "00000" + {var_name};'
        '\n}else if (str_length === 3) {'
        f'\n  {var_name} = {var_name}.repeat(2);'
        '\n}'
    )
    expression_file_util.append_js_expression(expression=expression)


def _fill_three_digit_hex_color_code(hex_color_code: str) -> str:
    """
    Fill 3 digits hexadecimal color code until it becomes 6 digits.

    Parameters
    ----------
    hex_color_code : str
        One digit hexadecimal color code (not including '#').
        e.g., 'aaa', 'fff'

    Returns
    -------
    filled_color_code : str
        Result color code. e.g., 'aaaaaa', 'ffffff'
    """
    filled_color_code: str = ''
    for char in hex_color_code:
        filled_color_code += char * 2
    return filled_color_code


def _fill_one_digit_hex_color_code(hex_color_code: str) -> str:
    """
    Fill 1 digit hexadecimal color code until it becomes 6 digits.

    Parameters
    ----------
    hex_color_code : str
        One digit hexadecimal color code (not including '#').
        e.g., 'a', '0'

    Returns
    -------
    filled_color_code : str
        Result color code. e.g., '00000a', '000000'
    """
    filled_color_code: str = hex_color_code.zfill(6)
    return filled_color_code
