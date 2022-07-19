"""This module is for each language enum definition.
"""

from enum import Enum


class Lang(Enum):
    """Translation target languages definitions."""

    EN = "en"
    JP = "jp"


class _UndefinedStrValue(Exception):
    pass


def get_lang_from_str_value(*, str_value: str) -> Lang:
    """
    Get a language enum value from a specified string value.

    Parameters
    ----------
    str_value : str
        A target language string value.

    Returns
    -------
    lang : Lang
        A target language enum value.

    Raises
    ------
    _UndefinedStrValue
        If a specified string value is undefined.
    """
    for lang in Lang:
        if lang.value == str_value:
            return lang
    raise _UndefinedStrValue(
        f"A specified language string value is undefined: {str_value}"
    )
