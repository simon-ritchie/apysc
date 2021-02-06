"""HTML related implementations.
"""


from typing import List


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


def append_html_to_str(
        to_append_html: str, dest_html: str, indent_num: int) -> str:
    """
    Add html string to another string with line break and specified
    number's indentation.

    Parameters
    ----------
    to_append_html : str
        HTML string to append.
    dest_html : str
        `to_append_html` will be appended to this string.
    indent_num : int
        Indentation's number. The spaces that multiplied this
        number by 2 will be added.

    Returns
    -------
    result : str
        HTML appended string.
    """
    result: str = dest_html
    if result != '':
        result += '\n'
    result += ' ' * (indent_num * 2)
    result += to_append_html
    return result


def append_indent_to_each_line(html: str, indent_num: int) -> str:
    """
    Append indentation spaces to each lines of specified html.

    Parameters
    ----------
    html : str
        Target html string.
    indent_num : int
        Indentation number. e.g., if specified 1, then will be added
        two spaces.

    Returns
    -------
    result_html : str
        Indentation added html string.
    """
    space_num: int = indent_num * 2
    each_lines: List[str] = html.splitlines()
    result_html: str = ''
    for line in each_lines:
        if result_html != '':
            result_html += '\n'
        result_html += ' ' * space_num
        result_html += line
    return result_html
