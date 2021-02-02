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


def add_html_to_str(
        to_append_html: str, dest_html: str, indent_num: int) -> str:
    """
    Add html string to another string with line break and specified
    number's indentation.

    Parameters
    ----------
    to_append_html : str
        Html string to append.
    dest_html : str
        `to_append_html` will be appended to this string.
    indent_num : int
        Indentation's number. The spaces that multiplied this
        number by 2 will be added.

    Returns
    -------
    result : str
        Html appended string.
    """
    result: str = dest_html
    if result != '':
        result += '\n'
    result += ' ' * (indent_num * 2)
    result += to_append_html
    return result
