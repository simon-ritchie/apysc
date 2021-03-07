"""String's validation implementations.
"""

from typing import Any
from typing import Union


def validate_string_type(string: Union[str, Any]) -> None:
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
    from apyscript.type import String
    if isinstance(string, String):
        return
    raise ValueError(f'Specified value is not str type: {type(string)}')


def validate_not_empty_string(string: str) -> None:
    """
    Validate specified string is not empty.

    Parameters
    ----------
    string : str
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
