"""The utilities module for each lint's hash file (used to check whether
the files are updated or not).
"""

import os
import hashlib
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


def read_target_module_hash(module_path: str) -> str:
    """
    Read a specified module's hashed string.

    Parameters
    ----------
    module_path : str
        Target module path.

    Returns
    -------
    hashed_string : str
        Hashed module string. If there is no module at the specified
        path, then a blank string will be returned.
    """
    from apysc._file import file_util
    if not os.path.isfile(module_path):
        return ''
    module_txt: str = file_util.read_txt(file_path=module_path)
    hashed_string: str = hashlib.sha1(module_txt.encode()).hexdigest()
    return hashed_string


def read_saved_hash(module_path: str, lint_type: LintType) -> str:
    """
    Read an already-saved module's hashed string.

    Parameters
    ----------
    module_path : str
        Target module path.
    lint_type : LintType
        Target lint type.

    Returns
    -------
    saved_hash : str
        An already-saved module's hash string. If there is no saved
        hash file then a blank string will be returned.
    """
    from apysc._file import file_util
    file_path: str = get_target_module_hash_file_path(
        module_path= module_path, lint_type=lint_type)
    if not os.path.isfile(file_path):
        return ''
    saved_hash: str = file_util.read_txt(file_path=file_path)
    saved_hash = saved_hash.strip()
    return saved_hash


def save_target_module_hash(module_path: str, lint_type: LintType) -> None:
    """
    Save a target module's current hash.

    Parameters
    ----------
    module_path : str
        Target module path.
    lint_type : LintType
        Target lint type.
    """
    from apysc._file import file_util
    hash: str = read_target_module_hash(module_path=module_path)
    if hash == '':
        return
    file_path: str = get_target_module_hash_file_path(
        module_path= module_path, lint_type=lint_type)
    file_util.save_plain_txt(txt=hash, file_path=file_path)


def is_module_updated(module_path: str, lint_type: LintType) -> bool:
    """
    Get a boolean value whether a specified module has been updated
    after the last lint execution.

    Parameters
    ----------
    module_path : str
        Target module path.
    lint_type : LintType
        Target lint type.

    Returns
    -------
    result : bool
        If a specified module has been updated then True will
        be returned.
    """
    saved_hash: str = read_saved_hash(
        module_path= module_path, lint_type=lint_type)
    current_hash: str = read_target_module_hash(module_path= module_path)
    if saved_hash == current_hash:
        return False
    return True
