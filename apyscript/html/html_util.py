"""HTML related implementations.
"""


def remove_first_selector_symbol_char(str_val: str) -> str:
    """
    Remove first selector symbol (`.` or `#`) from string.

    Parameters
    ----------
    str_val : str
        Target string value. e.g., '#container'

    Returns
    -------
    str_val : str
        The string that removed first selector symbol character.
    """
    if str_val.startswith('.') or str_val.startswith('#'):
        str_val = str_val[1:]
    return str_val
