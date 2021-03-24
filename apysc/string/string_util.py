"""Common string utilities.

Mainly following interfaces and defined.

- escape_str
    Escape special characters (e.g. line breaks of `\n`).
- wrap_by_double_quotation_if_value_is_string
    Wrap specified by double quotation if value is a string.
"""


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
