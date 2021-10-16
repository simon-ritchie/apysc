"""The utilities module for each lint's hash file (used to check whether
the files are updated or not).
"""

import os
from enum import Enum


class LintType(Enum):

    AUTOPEP8 = 'autopep8'


_LINT_PACKAGE_ROOT_PATH: str = './_lint/'


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
