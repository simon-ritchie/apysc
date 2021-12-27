"""The utilities module for each lint's hash file (used to check whether
the files are updated or not).

Mainly following interfaces are defined:

- get_lint_hash_dir_path
    - Get a specified lint type's hash directory path.
- get_target_module_hash_file_path
    - Get a specified module's hash file path.
- read_target_module_hash
    - Read a specified module's hashed string.
- read_saved_hash
    - Read an already-saved module's hashed string.
- save_target_module_hash
    - Save a target module's current hash.
- save_target_modules_hash
    - Save target modules' current hash.
- is_module_updated
    - Get a boolean value whether a specified module has been updated
        after the last lint execution.
- remove_not_updated_module_paths
    - Remove not updated modules from specified module paths.
"""

import hashlib
import os
from concurrent import futures
from enum import Enum
from multiprocessing import Pool
from multiprocessing import cpu_count
from typing import List

from typing_extensions import TypedDict


class LintType(Enum):

    AUTOFLAKE = 'autoflake'
    ISORT = 'isort'
    AUTOPEP8 = 'autopep8'


_LINT_PACKAGE_ROOT_PATH: str = './.lint_hash/'


def get_lint_hash_dir_path(*, lint_type: LintType) -> str:
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
        *, module_path: str, lint_type: LintType) -> str:
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
    file_path = file_path.replace('.py', '', 1)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    return file_path


def read_target_module_hash(*, module_path: str) -> str:
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


def read_saved_hash(*, module_path: str, lint_type: LintType) -> str:
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
        module_path=module_path, lint_type=lint_type)
    if not os.path.isfile(file_path):
        return ''
    saved_hash: str = file_util.read_txt(file_path=file_path)
    saved_hash = saved_hash.strip()
    return saved_hash


def save_target_module_hash(*, module_path: str, lint_type: LintType) -> None:
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
        module_path=module_path, lint_type=lint_type)
    file_util.save_plain_txt(txt=hash, file_path=file_path)


def save_target_modules_hash(
        *, module_paths: List[str], lint_type: LintType) -> None:
    """
    Save target modules' current hash.

    Parameters
    ----------
    module_paths : list of str
        Target module paths.
    lint_type : LintType
        Target lint type.
    """
    workers: int = max(cpu_count() - 1, 1)
    with futures.ProcessPoolExecutor(max_workers=workers) as executor:
        future_list: List[futures.Future] = []
        for module_path in module_paths:
            future = executor.submit(
                save_target_module_hash,
                module_path=module_path,
                lint_type=lint_type)
            future_list.append(future)
        _ = futures.as_completed(fs=future_list)


def is_module_updated(*, module_path: str, lint_type: LintType) -> bool:
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
        module_path=module_path, lint_type=lint_type)
    current_hash: str = read_target_module_hash(module_path=module_path)
    if saved_hash == current_hash:
        return False
    return True


class _IsModuleUpdatedArgs(TypedDict):
    module_path: str
    lint_type: LintType


def _is_module_updated_func_for_multiprocessing(
        args: _IsModuleUpdatedArgs) -> bool:
    """
    Wrapper function of the `is_module_updated` function
    for the multiprocessing.

    Parameters
    ----------
    args : _IsModuleUpdatedArgs
        Arguments dictionary to pass to the `is_module_updated`
        function.

    Returns
    -------
    result : bool
        If a specified module has been updated then True will
        be returned.
    """
    result: bool = is_module_updated(
        module_path=args['module_path'],
        lint_type=args['lint_type'])
    return result


def _create_args_list_for_multiprocessing(
        *, module_paths: List[str],
        lint_type: LintType) -> List[_IsModuleUpdatedArgs]:
    """
    Create an arguments list for the multiprocessing.

    Parameters
    ----------
    module_paths : list of str
        Target Python module paths.
    lint_type : LintType
        Target lint type.

    Returns
    -------
    args_list : list of _IsModuleUpdatedArgs
        Created arguments list for the multiprocessing.
    """
    args_list: List[_IsModuleUpdatedArgs] = []
    for module_path in module_paths:
        args_list.append({
            'module_path': module_path,
            'lint_type': lint_type,
        })
    return args_list


def remove_not_updated_module_paths(
        *, module_paths: List[str],
        lint_type: LintType) -> List[str]:
    """
    Remove not updated modules from specified module paths.

    Parameters
    ----------
    module_paths : list of str
        Target Python module paths.
    lint_type : LintType
        Target lint type.

    Returns
    -------
    sliced_module_paths : list of str
        After the slicing module paths.
    """
    workers: int = max(cpu_count() - 1, 1)
    args_list: List[_IsModuleUpdatedArgs] = \
        _create_args_list_for_multiprocessing(
            module_paths=module_paths, lint_type=lint_type)
    sliced_module_paths: List[str] = []
    with Pool(processes=workers) as p:
        module_updated_bool_list: List[bool] = p.map(
            func=_is_module_updated_func_for_multiprocessing,
            iterable=args_list,
        )
    module_updated: bool
    for i, module_updated in enumerate(module_updated_bool_list):
        if not module_updated:
            continue
        sliced_module_paths.append(module_paths[i])
    return sliced_module_paths
