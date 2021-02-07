"""HTML and js expression's scope implementation.
"""

from apyscript.html import html_util
import os
import re
from typing import List

from apyscript.expression import expression_file_util
from apyscript.file import file_util


def update_current_scope(scope_name: str) -> None:
    """
    Update expression's current scope name.

    Parameters
    ----------
    scope_name : str
        Scope name value to set.
    """
    _reset_scope_history_if_scope_is_main_entry_point(
        scope_name=scope_name)
    file_util.save_plain_txt(
        txt=scope_name,
        file_path=expression_file_util.CURRENT_SCOPE_FILE_PATH)
    _save_scope_history(scope_name=scope_name)


def _reset_scope_history_if_scope_is_main_entry_point(
        scope_name: str) -> None:
    """
    Reset (remove) scope history file if specified scope is main
    entry point (The case of module name is `__main__` and function
    name is `main`).

    Parameters
    ----------
    scope_name : str
        Specified scope name.
    """
    if scope_name != '__main_____main':
        return
    file_util.remove_file_if_exists(
        file_path=expression_file_util.SCOPE_HISTORY_FILE_PATH)


def _save_scope_history(scope_name: str) -> None:
    """
    Save scope updating history to file.

    Parameters
    ----------
    scope_name : str
        Scope name value to bo specified updating function.
    """
    with open(expression_file_util.SCOPE_HISTORY_FILE_PATH, 'a') as f:
        f.write(f'{scope_name},')


def get_current_scope() -> str:
    """
    Get expression's current scope name.

    Returns
    -------
    scope_name : str
        Current scope name.
    """
    if not os.path.isfile(expression_file_util.CURRENT_SCOPE_FILE_PATH):
        return expression_file_util.ROOT_SCOPE
    scope_name: str = file_util.read_txt(
        file_path=expression_file_util.CURRENT_SCOPE_FILE_PATH)
    scope_name = scope_name.strip()
    return scope_name


def get_scope_name_from_file_path(expression_file_path: str) -> str:
    """
    Get a scope name from expression's file path.

    Parameters
    ----------
    expression_file_path : str
        Target expression's file path or file name.

    Returns
    -------
    scope_name : str
        Target scope name.
    """
    scope_name: str = os.path.basename(expression_file_path)
    scope_name = scope_name.replace('.html', '')
    return scope_name


def _get_scope_wrapper_function_head(scope_name: str) -> str:
    """
    Get a scope wrapper function's head.

    Parameters
    ----------
    scope_name : str
        Target scope name.

    Returns
    -------
    scope_wrapper_function_head : str
        Scope wrapper function's head. e.g., `function <scope_name>() {`
    """
    scope_wrapper_function_head: str = f'function {scope_name}() {{'
    return scope_wrapper_function_head


def append_scope_wrapper_func_to_expression(
        expression: str, scope_name: str) -> str:
    """
    Append js function wrapper to expression's each <script> tag section.

    Parameters
    ----------
    expression : str
        Target HTML and js expression.
    scope_name : str
        Expression's scope name. Same as extension excluded file name.

    Returns
    -------
    result_expression : str
        HTML string After appended wrapper function.
    """
    each_lines: List[str] = expression.splitlines()
    result_expression: str = ''
    for each_line in each_lines:
        if result_expression != '':
            result_expression += '\n'
        if html_util.is_script_end_tag_line(line=each_line):
            result_expression += '}\n'
        result_expression += each_line
        if html_util.is_script_start_tag_line(line=each_line):
            function_head: str = _get_scope_wrapper_function_head(
                scope_name=scope_name)
            result_expression += f'\n{function_head}'
    return result_expression
