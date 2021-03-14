"""HTML related implementations.

Mainly following interfaces are defined:

- remove_first_selector_symbol_char : Remove first selector
    symbol (`.` or `#`) from string.
- append_html_to_str : Add html string to another string with line
    break and specified number's indentation.
- append_indent_to_each_script_line : Append indentation spaces to
    each script lines of specified html.
- ScriptLineUtil : The class for HTML's script line utility.
- is_script_start_tag_line : Get a boolean whether the specified
    line contains script start tag (`<script ...>`).
- is_script_end_tag_line : Get a boolean whether the specified line
    contains script end tag (`</script>`).
- wrap_expression_by_script_tag : Wrap an expression string by
    script start and end tag.
"""

import re
from typing import List
from typing import Match
from typing import Optional
from typing import Tuple

from apyscript.html import html_const
from apyscript.string import indent_util


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
    result += indent_util.make_spaces_for_html(indent_num=indent_num)
    result += to_append_html
    return result


def append_indent_to_each_script_line(html: str, indent_num: int) -> str:
    """
    Append indentation spaces to each script lines of specified html.

    e.g., if the html is following string, then only `console.log` line
    will be added indentation.
    <html>
    <script type="text/javascript">
    console.log('Hello!');
    </script>
    </html>

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
    each_lines: List[str] = html.splitlines()
    result_html: str = ''
    script_line_util: ScriptLineUtil = ScriptLineUtil(html=html)
    for i, line in enumerate(each_lines):
        if result_html != '':
            result_html += '\n'
        if script_line_util.is_script_line(line_number=i + 1):
            result_html += indent_util.make_spaces_for_html(
                indent_num=indent_num)
        result_html += line
    return result_html


class ScriptLineUtil:

    html: str
    script_line_ranges: List[Tuple[int, int]]

    def __init__(self, html: str) -> None:
        """
        The class for HTML's script line utility.

        Parameters
        ----------
        html : str
            Target HTML string.
        """
        self.html = html
        self._set_script_line_ranges()

    def _set_script_line_ranges(self) -> None:
        """
        Set each script start and end line numbers.
        """
        self.script_line_ranges = []
        each_lines: List[str] = self.html.splitlines()
        start_line_num: int = 0
        for i, line in enumerate(each_lines):
            line_number: int = i + 1
            if is_script_start_tag_line(line=line):
                start_line_num = line_number + 1
                continue
            if is_script_end_tag_line(line=line):
                end_line_num: int = line_number - 1
                self.script_line_ranges.append(
                    (start_line_num, end_line_num))

    def is_script_line(self, line_number: int) -> bool:
        """
        Get a boolean value whether specified line number is script line
        or not.

        Parameters
        ----------
        line_number : int
            Target line number (start at 1, not 0).

        Returns
        -------
        result : bool
            If the target line is script line, then True will be set.
        """
        for script_line_start, script_line_end in self.script_line_ranges:
            if (script_line_start <= line_number
                    and line_number <= script_line_end):
                return True
        return False


def is_script_start_tag_line(line: str) -> bool:
    """
    Get a boolean whether the specified line contains script start
    tag (`<script ...>`).

    Notes
    -----
    External js script tag will not be target.
    e.g., `<script type="text/javascript" src="any_script.js"></script>`

    Parameters
    ----------
    line : str
        Target line string.

    Returns
    -------
    result : bool
        If specified line contains script start tag, then True
        will be set.
    """
    match: Optional[Match] = re.search(
        pattern=r'<script ', string=line)
    if match is None:
        return False
    if 'src=' in line:
        return False
    return True


def is_script_end_tag_line(line: str) -> bool:
    """
    Get a boolean whether the specified line contains script end
    tag (`</script>`).

    Notes
    -----
    External js script tag will not be target.
    e.g., `<script type="text/javascript" src="any_script.js"></script>`

    Parameters
    ----------
    line : str
        Target line string.

    Returns
    -------
    result : bool
        If specified line contains script end tag, then True
        will be set.
    """
    match: Optional[Match] = re.search(
        pattern=r'</script>', string=line)
    if match is None:
        return False
    if 'src=' in line:
        return False
    return True


def wrap_expression_by_script_tag(expression: str) -> str:
    """
    Wrap an expression string by script start and end tag.

    Parameters
    ----------
    expression : str
        An expression to wrap.

    Returns
    -------
    expression : str
        Wrapped expression string.
    """
    expression = (
        f'{html_const.SCRIPT_START_TAG}'
        f'\n{expression}'
        f'\n{html_const.SCRIPT_END_TAG}'
    )
    return expression
