"""Each interface to get a Python built-in value from an apysc one.
"""

from typing import Union

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String


@add_debug_info_setting(module_name=__name__)
def get_builtin_str_from_apysc_val(*, string: Union[str, String]) -> str:
    """
    Get a Python built-in string from an apysc one.

    Parameters
    ----------
    string : str or ap.String
        Target string value.

    Returns
    -------
    builtin_val : str
        A Python built-in string.
    """
    if isinstance(string, str):
        return string
    builtin_val: str = string._value
    return builtin_val
