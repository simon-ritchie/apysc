"""String's validation implementations.
"""

from typing import Union

import apysc as ap


def validate_string_type(string: Union[str, ap.String]) -> None:
    """
    Validate specified string's type is str.

    Parameters
    ----------
    string : str or String
        String to check.

    Raises
    ------
    ValueError
        - If not string value is specified.
    """
    if isinstance(string, str):
        return
    if isinstance(string, ap.String):
        return
    raise ValueError(f'Specified value is not str type: {type(string)}')


def validate_not_empty_string(string: Union[str, ap.String]) -> None:
    """
    Validate specified string is not empty.

    Parameters
    ----------
    string : str or String
        String to check.

    Raises
    ------
    ValueError
        - If empty string ('' or "") is specified.
        - If specified value is not str type.
    """
    validate_string_type(string=string)
    if string != '':
        return
    raise ValueError('Empty string is not acceptable.')
