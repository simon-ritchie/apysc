"""Each interface to get a Python built-in value from an apysc one.
"""

from typing import Union

import apysc as ap


def get_builtin_str_from_apysc_val(string: Union[str, ap.String]) -> str:
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
    with ap.DebugInfo(
            callable_=get_builtin_str_from_apysc_val, locals_=locals(),
            module_name=__name__):
        if isinstance(string, str):
            return string
        builtin_val: str = string._value
        return builtin_val
