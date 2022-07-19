"""Color-related implementations.
"""

from typing import Any
from typing import TypeVar

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String

StrOrString = TypeVar("StrOrString", str, String)


@add_debug_info_setting(module_name=__name__)
def complement_hex_color(*, hex_color_code: StrOrString) -> StrOrString:
    """
    Complement hex color for convenience; for instance,
    add # prefix or three digits to become six digits,
    upper case to lower case.

    Parameters
    ----------
    hex_color_code : str or String
        Hexadecimal color code. e.g., 'ff0000', '#666', '#0'

    Returns
    -------
    complemented_hex_color_code : str or String
        Result hex color code. e.g., '#ff0000', '#666666, '#000000'
    """
    import apysc as ap
    from apysc._validation import color_validation

    hex_color_code = remove_color_code_sharp_symbol(hex_color_code=hex_color_code)

    color_validation.validate_hex_color_code_format(hex_color_code=hex_color_code)
    if isinstance(hex_color_code, ap.String):
        value_: str = hex_color_code._value
    else:
        value_ = str(hex_color_code)
    char_len = len(value_)
    if char_len == 1:
        value_ = _fill_one_digit_hex_color_code(hex_color_code=value_)
    elif char_len == 3:
        value_ = _fill_three_digit_hex_color_code(hex_color_code=value_)
    value_ = value_.lower()
    value_ = f"#{value_}"

    if isinstance(hex_color_code, ap.String):
        hex_color_code._value = value_
        _append_complement_hex_color_expression(hex_color_code=hex_color_code)
    else:
        hex_color_code = value_  # type: ignore
    return hex_color_code  # type: ignore


def remove_color_code_sharp_symbol(*, hex_color_code: StrOrString) -> StrOrString:
    """
    Remove a sharp symbol from a specified hexadecimal color code
    string.

    Parameters
    ----------
    hex_color_code : StrOrString
        A targert hexadecimal color code string.

    Returns
    -------
    hex_color_code : StrOrString
        A result string.
    """
    from apysc._type import value_util

    if isinstance(hex_color_code, str):
        hex_color_code_: str = hex_color_code  # type: ignore
        if hex_color_code_.startswith("#"):
            hex_color_code_ = hex_color_code_[1:]
        return hex_color_code_  # type: ignore

    if isinstance(hex_color_code, String):
        hex_color_code__: String = value_util.get_copy(value=hex_color_code)
        if hex_color_code__._value.startswith("#"):
            hex_color_code__._value = hex_color_code__._value[1:]
        _append_remove_color_code_sharp_symbol_expression(
            hex_color_code=hex_color_code__
        )
        return hex_color_code__  # type: ignore

    raise TypeError(
        "Other than str or String type value is specified: " f"{type(hex_color_code)}"
    )


def _append_remove_color_code_sharp_symbol_expression(
    *, hex_color_code: String
) -> None:
    """
    Append the remove_color_code_sharp_symbol function's
    expression.

    Parameters
    ----------
    hex_color_code : String
        A sharp symbol removed string instance.
    """
    import apysc as ap

    var_name: str = hex_color_code.variable_name
    expression: str = (
        f"var first_char = {var_name}.slice(0, 1);"
        '\nif (first_char === "#") {'
        f"\n  {var_name} = {var_name}.slice(1);"
        "\n}"
    )
    ap.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def _append_complement_hex_color_expression(*, hex_color_code: Any) -> None:
    """
    Append complement_hex_color function's expression.

    Parameters
    ----------
    hex_color_code : String
        Complemented hex color code string.
    """
    import apysc as ap
    from apysc._expression import expression_variables_util
    from apysc._expression import var_names

    index_name: str = expression_variables_util.get_next_variable_name(
        type_name=var_names.INDEX
    )
    hex_color_code_: ap.String = hex_color_code
    var_name: str = hex_color_code_.variable_name
    expression: str = (
        f"var str_length = {var_name}.length;"
        "\nif (str_length === 1) {"
        f'\n  {var_name} = "00000" + {var_name};'
        "\n}else if (str_length === 3) {"
        f'\n  var {var_name}_ = "";'
        f"\n  for (var {index_name} = 0; {index_name} < "
        f"{var_name}.length; "
        f"{index_name}++) {{"
        f"\n    {var_name}_ += {var_name}[{index_name}].repeat(2);"
        "\n  }"
        f"\n  {var_name} = {var_name}_;"
        "\n}"
        f'\n{var_name} = "#" + {var_name};'
    )
    ap.append_js_expression(expression=expression)


def _fill_three_digit_hex_color_code(*, hex_color_code: str) -> str:
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
    filled_color_code: str = ""
    for char in hex_color_code:
        filled_color_code += char * 2
    return filled_color_code


def _fill_one_digit_hex_color_code(*, hex_color_code: str) -> str:
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
