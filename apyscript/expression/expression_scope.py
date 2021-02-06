"""HTML and js expression's scope implementation.
"""

import os

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
    file_util.save_plain_txt(
        txt=scope_name,
        file_path=expression_file_util.CURRENT_SCOPE_FILE_PATH)


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
    expression : str
        HTML string After appended wrapper function.
    """
    pass
