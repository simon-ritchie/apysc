"""Common string utilities.

Mainly following interfaces and defined.

- escape_str
    Escape special characters (e.g. line breaks of `\n`).
- escape_double_quotation
    Escape double quotations.
- wrap_by_double_quotation_if_value_is_string
    Wrap specified by double quotation if value is a string.
- substitute_file_by_pattern
    Substitute text file by regular expression pattern.
"""

import re
from typing import Any
from typing import TypeVar


def escape_str(string: str) -> str:
    """
    Escape special characters (e.g. line breaks of `\n`).

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
    return string


def escape_double_quotation(string: str) -> str:
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


T = TypeVar('T')


def wrap_by_double_quotation_if_value_is_string(value: T) -> T:
    """
    Wrap specified by double quotation if value is a string.

    Parameters
    ----------
    value : *
        Any value to wrap.

    Returns
    -------
    value : *
        Wrapped value. If not string value is specified, return that
        value imediatelly.
    """
    if not isinstance(value, str):
        return value
    value = f'"{value}"'  # type: ignore
    return value  # type: ignore


def substitute_file_by_pattern(
        file_path: str, pattern: str, repl: str,
        flags: Any) -> None:
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
    from apysc.file import file_util
    string: str = file_util.read_txt(file_path=file_path)
    string = re.sub(
        pattern=pattern,
        repl=repl,
        string=string,
        flags=flags)
    file_util.save_plain_txt(txt=string, file_path=file_path)
