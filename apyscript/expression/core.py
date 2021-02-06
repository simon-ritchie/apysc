"""HTML and js expression's core implementation.
"""

from apyscript.expression import expression_file_util
from apyscript.file import file_util


def update_current_scope(scope_name: str) -> None:
    """
    Update expression's current scope.

    Parameters
    ----------
    scope_name : str
        Scope name value to set.
    """
    file_util.save_plain_txt(
        txt=scope_name,
        file_path=expression_file_util.CURRENT_SCOPE_FILE_PATH)
