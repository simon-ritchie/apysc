"""The implementation of manipulating HTL and js expression files.
"""

import os
import shutil
from typing import List, Optional

from apyscript.file import file_util
from apyscript.expression import expression_scope

EXPRESSION_ROOT_DIR: str = '../.apyscript_expression/'
CURRENT_SCOPE_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'current_scope.txt')


def empty_expression_dir() -> None:
    """Remove expression directory (EXPRESSION_ROOT_DIR) to initialize.
    """
    file_util.empty_directory(directory_path=EXPRESSION_ROOT_DIR)


ROOT_SCOPE: str = 'root'


def append_expression(expression: str, scope: Optional[str] = None) -> None:
    """
    Append html and js expression to specified scope's file.

    Parameters
    ----------
    expression : str
        HTML and js Expression string.
    scope : str, optional
        Target scope name. If skipped, this will be root scope.
    """
    scope_file_path: str = get_scope_file_path_from_scope(scope=scope)
    dir_path: str = file_util.get_abs_directory_path_from_file_path(
        file_path=scope_file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(scope_file_path, 'a') as f:
        f.write(f'{expression}\n')


def append_expression_to_current_scope(expression: str) -> None:
    """
    Append html and js expression to current scope's file.

    Parameters
    ----------
    expression : str
        HTML and js Expression string.
    """
    scope: str = expression_scope.get_current_scope()
    append_expression(expression=expression, scope=scope)


def get_scope_file_path_from_scope(scope: Optional[str] = None) -> str:
    """
    Get scope file path from specified scope string.

    Parameters
    ----------
    scope : str, optional
        Target scope name. If None is specified, this will be root scope.

    Returns
    -------
    scope_file_path : str
        Result scope file path string (include html extension).
    """
    if scope is None:
        scope = ROOT_SCOPE
    if not scope.endswith('.html'):
        scope += '.html'
    scope_file_path: str = os.path.join(EXPRESSION_ROOT_DIR, scope)
    return scope_file_path


def get_expression_file_paths() -> List[str]:
    """
    Get existing expression file paths.

    Returns
    -------
    expression_file_paths : list of str
        Existing expression file paths.
    """
    expression_file_paths: List[str] = []
    file_names: List[str] = os.listdir(EXPRESSION_ROOT_DIR)
    for file_name in file_names:
        if not file_name.endswith('.html'):
            continue
        file_path: str = os.path.join(EXPRESSION_ROOT_DIR, file_name)
        expression_file_paths.append(file_path)
    return expression_file_paths
