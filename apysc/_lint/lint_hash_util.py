"""The utilities module for each lint's hash file (used to check whether
the files are updated or not).
"""

import os
from enum import Enum


class LintType(Enum):

    AUTOPEP8 = 'autopep8'


_LINT_PACKAGE_ROOT_PATH: str = './apysc/_lint/'


def get_lint_hash_dir_path(lint_type: LintType) -> str:
    """
    Get a specified lint type's hash directory path.

    Parameters
    ----------
    lint_type : LintType
        Target lint type.

    Returns
    -------
    dir_path : str
        Target lint type's hash directory path.

    Notes
    -----
    Returned directory path will create automatically if it does
    not exist.
    """
    dir_path: str = os.path.join(
        _LINT_PACKAGE_ROOT_PATH,
        f'.{lint_type.value}/'
    )
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def get_target_module_hash_file_path(
        module_path: str, lint_type: LintType) -> str:
    """
    Get a specified module's hash file path.

    Parameters
    ----------
    module_path : str
        Target module path.
    lint_type : LintType
        Target lint type.

    Returns
    -------
    file_path : str
        Target hash file path.

    Notes
    -----
    Returned file's directory path will create automatically if it
    does not exist.
    """
    if module_path.startswith('./'):
        module_path = module_path.replace('./', '', 1)
    dir_path: str = get_lint_hash_dir_path(lint_type=lint_type)
    file_path: str = os.path.join(dir_path, module_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    return file_path
