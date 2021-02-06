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
