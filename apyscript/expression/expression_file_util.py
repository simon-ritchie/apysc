"""The implementation of manipulating HTL and js expression files.

Mainly following interfaces are defined:

- empty_expression_dir : Remove expression directory
    (EXPRESSION_ROOT_DIR) to initialize.
- append_expression : Append html and js expression to file.
- wrap_by_script_tag_and_append_expression : Wrap an expression
    string by script tags and append it's expression to file.
- get_current_expression : Get current expression string.
- remove_expression_file : Remove expression file.
"""

import os
from typing import List

from apyscript.file import file_util
from apyscript.html import html_const
from apyscript.html import html_util
from apyscript.html.html_util import ScriptLineUtil

EXPRESSION_ROOT_DIR: str = '../.apyscript_expression/'
EXPRESSION_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'expression.txt')


def empty_expression_dir() -> None:
    """
    Remove expression directory (EXPRESSION_ROOT_DIR) to initialize.
    """
    file_util.empty_directory(directory_path=EXPRESSION_ROOT_DIR)


def append_expression(expression: str) -> None:
    """
    Append html and js expression to file.

    Parameters
    ----------
    expression : str
        HTML and js Expression string.
    """
    dir_path: str = file_util.get_abs_directory_path_from_file_path(
        file_path=EXPRESSION_FILE_PATH)
    os.makedirs(dir_path, exist_ok=True)
    file_util.append_plain_txt(
        txt=f'{expression}\n', file_path=EXPRESSION_FILE_PATH)
    _merge_script_section()


def wrap_by_script_tag_and_append_expression(expression: str) -> None:
    """
    Wrap an expression string by script tags and append it's
    expression to file (helper function of `append_expression`).

    Parameters
    ----------
    expression : str
        HTML and js Expression string.
    """
    expression = html_util.wrap_expression_by_script_tag(
        expression=expression)
    append_expression(expression=expression)


def _merge_script_section() -> None:
    """
    Merge expression's script section (If there are multiple
    script tag in expression file, then they will be merged).
    """
    result_expression: str = ''
    current_expression: str = file_util.read_txt(
        file_path=EXPRESSION_FILE_PATH)
    current_exp_lines: List[str] = current_expression.splitlines()
    script_line_util: ScriptLineUtil = ScriptLineUtil(
        html=current_expression)
    script_strings: str = ''
    for i, current_exp_line in enumerate(current_exp_lines):
        if current_exp_line == html_const.SCRIPT_START_TAG:
            continue
        if current_exp_line == html_const.SCRIPT_END_TAG:
            continue
        line_num: int = i + 1
        if script_line_util.is_script_line(line_number=line_num):
            if current_exp_line == '':
                continue
            script_strings += f'{current_exp_line}\n'
            continue
        result_expression += f'{current_exp_line}\n'
    if script_strings != '':
        result_expression += (
            f'{html_const.SCRIPT_START_TAG}\n'
            f'{script_strings}'
            f'{html_const.SCRIPT_END_TAG}\n'
        )
    file_util.save_plain_txt(
        txt=result_expression,
        file_path=EXPRESSION_FILE_PATH)


def get_current_expression() -> str:
    """
    Get current expression's string from file.

    Returns
    -------
    current_expression : str
        Current expression's string.
    """
    if not os.path.isfile(EXPRESSION_FILE_PATH):
        return ''
    current_expression: str = file_util.read_txt(
        file_path=EXPRESSION_FILE_PATH)
    current_expression = current_expression.strip()
    return current_expression


def remove_expression_file() -> None:
    """
    Remove expression file.
    """
    file_util.remove_file_if_exists(file_path=EXPRESSION_FILE_PATH)
