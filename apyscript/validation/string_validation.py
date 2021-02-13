"""String's validation implementations.
"""


def validate_string_type(string: str) -> None:
    """
    Validate specified string's type is str.

    Parameters
    ----------
    string : str
        String to check.

    Raises
    ------
    ValueError
        エラー条件
    """
    if isinstance(string, str):
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
