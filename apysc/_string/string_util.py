"""Common string utilities.

Mainly following interfaces and defined.

- escape_str
    - Escape special characters (e.g., line breaks).
- escape_double_quotation
    - Escape double quotations.
- wrap_by_double_quotation_if_value_is_string
    - Wrap specified value by double quotation if a value
    is a string.
- substitute_file_by_pattern
    - Substitute text file by regular expression pattern.
- replace_double_spaces_to_single_space
    - Replace double spaces with a single space.
- get_tails_lines_str
    - Get a tail's lines string from a specified string.
"""

import re
from typing import Any
from typing import List
from typing import TypeVar


def escape_str(*, string: str) -> str:
    """
    Escape special characters (e.g., line breaks of `\\n`).

    Parameters
    ----------
    string : str
        String to escape.

    Returns
    -------
    string : str
        Escaped string.
    """
    string = repr(string)[1:-1]
    string = string.replace("\\\\", "\\")
    return string


def escape_double_quotation(*, string: str) -> str:
    """
    Escape double quotations.

    Parameters
    ----------
    string : str
        String to escape.

    Returns
    -------
    string : str
        Escaped string.
    """
    string = string.replace('"', '\\"')
    return string


_Value = TypeVar("_Value")


def wrap_by_double_quotation_if_value_is_string(*, value: _Value) -> _Value:
    """
    Wrap specified value by double quotation if a
    value is a string.

    Parameters
    ----------
    value : *
        Any value to wrap.

    Returns
    -------
    value : *
        Wrapped value. If a not-string value is specified,
        return that value immediately.
    """
    if not isinstance(value, str):
        return value
    value = f'"{value}"'  # type: ignore
    return value  # type: ignore


def substitute_file_by_pattern(
    *, file_path: str, pattern: str, repl: str, flags: Any
) -> None:
    """
    Substitute text file by regular expression pattern.

    Parameters
    ----------
    file_path : str
        Target file path.
    pattern : str
        Regular expression pattern.
    repl : str
        String that replace matched pattern one.
    flags : Any
        Regular expression flags.
    """
    from apysc._file import file_util

    string: str = file_util.read_txt(file_path=file_path)
    string = re.sub(pattern=pattern, repl=repl, string=string, flags=flags)
    file_util.save_plain_txt(txt=string, file_path=file_path)


def replace_double_spaces_to_single_space(*, string: str) -> str:
    """
    Replace double spaces with a single space.

    Parameters
    ----------
    string : str
        Target string to replace.

    Returns
    -------
    string : str
        Replaced string.
    """
    while "  " in string:
        string = string.replace("  ", " ")
    return string


def get_tails_lines_str(*, string: str, n: int) -> str:
    """
    Get a tail's lines string from a specified string.

    Parameters
    ----------
    string : str
        A target string.
    n : int
        A Lines number.

    Returns
    -------
    tails_lines_str : str
        A tail's lines string
    """
    lines: List[str] = string.splitlines()
    tails_lines_str: str = "\n".join(lines[-n:])
    return tails_lines_str
