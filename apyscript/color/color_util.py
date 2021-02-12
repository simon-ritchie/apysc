"""Color related implementations.
"""


from apyscript.html import html_util
from apyscript.validation import color_validation


def complement_hex_color(hex_color_code: str) -> str:
    """
    Complement hex color for convenience, for instance, add # prefix or
    three digits to six digits, upper case to lower case etc.

    Parameters
    ----------
    hex_color_code : str
        Hexadecimal color code. e.g., 'ff0000', '#666', '#0'

    Returns
    -------
    complemented_hex_color_code : str
        Result hex color code. e.g., '#ff0000', '#666666, '#000000'
    """
    hex_color_code = html_util.remove_first_selector_symbol_char(
        str_val=hex_color_code)
    color_validation.validate_hex_color_code_format(
        hex_color_code=hex_color_code)
    char_len: int = len(hex_color_code)
    if char_len == 1:
        hex_color_code = _fill_one_digit_hex_color_code(
            hex_color_code=hex_color_code)
    elif char_len == 3:
        hex_color_code = _fill_three_digit_hex_color_code(
            hex_color_code=hex_color_code)
    hex_color_code = hex_color_code.lower()
    hex_color_code = f'#{hex_color_code}'
    return hex_color_code


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
