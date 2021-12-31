"""Files' common utilities implementation.

Mainly following interfaces are defined:

- empty_directory
    - Empty specified directory.
- read_txt
    - Read specified file's text.
- save_plain_txt
    - Save plain text string to file.
- append_plain_txt
    - Append plain text string to file.
- remove_file_if_exists
    - Remove specified file if exists.
- get_abs_directory_path_from_file_path
    - Get an absolute directory path of specified file.
- get_abs_module_dir_path
    - Get a specified module's abosulute directory path.
- get_specified_ext_file_paths_recursively
    - Get specified extension file paths recursively.
- count_files_recursively
    - Count the existing files number in a specified directory.
"""

import os
import shutil
import traceback
from types import ModuleType
from typing import List
from typing import Optional


def empty_directory(*, directory_path: str) -> None:
    """
    Empty specified directory.

    Parameters
    ----------
    directory_path : str
        Directory path to empty. This folder itself will not be
        removed.
    """
    if os.path.isdir(directory_path):
        shutil.rmtree(directory_path, ignore_errors=True)
    os.makedirs(directory_path, exist_ok=True)


def read_txt(*, file_path: str) -> str:
    """
    Read specified file's text.

    Parameters
    ----------
    file_path : str
        File path to read.

    Returns
    -------
    txt : str
        Target file's text.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            txt: str = f.read()
        except Exception:
            err_msg: str = (
                f'{traceback.format_exc()}'
                f'\nFailed the file reading: {file_path}'
            )
            raise Exception(err_msg)
    return txt


def save_plain_txt(*, txt: str, file_path: str) -> None:
    """
    Save plain text string to file.

    Parameters
    ----------
    txt : str
        Plain text string to save.
    file_path : str
        Destination file path.
    """
    dir_path: str = get_abs_directory_path_from_file_path(
        file_path=file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(txt)


def append_plain_txt(*, txt: str, file_path: str) -> None:
    """
    Append plain text string to file.

    Parameters
    ----------
    txt : str
        Plain text string to append.
    file_path : str
        Destination file path.
    """
    dir_path: str = get_abs_directory_path_from_file_path(
        file_path=file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(txt)


def remove_file_if_exists(*, file_path: str) -> None:
    """
    Remove specified file if exists.

    Parameters
    ----------
    file_path : str
        File path to remove.
    """
    if not os.path.isfile(file_path):
        return
    os.remove(file_path)


def get_abs_directory_path_from_file_path(*, file_path: str) -> str:
    """
    Get an absolute directory path of specified file.

    Parameters
    ----------
    file_path : str
        Target file path.

    Returns
    -------
    dir_path : str
        An absolute directory path.
    """
    dir_path: str = os.path.dirname(file_path)
    dir_path += '/'
    return dir_path


def get_abs_module_dir_path(*, module: ModuleType) -> str:
    """
    Get a specified module's abosulute directory path.

    Parameters
    ----------
    module : ModuleType
        Target module.

    Returns
    -------
    abs_module_dir_path : str
        Specified module's abosulute directory path.
    """
    abs_module_dir_path: str = os.path.dirname(str(module.__file__))
    abs_module_dir_path += '/'
    return abs_module_dir_path


def get_specified_ext_file_paths_recursively(
        *, extension: str, dir_path: str = './',
        file_paths: Optional[List[str]] = None) -> List[str]:
    """
    Get specified extension file paths recursively.

    Parameters
    ----------
    extension : str
        Target file extension (e.g., '.md', 'md', and so on).
    dir_path : str
        Directory path to search files recursively.
    file_paths : list of str or None
        Current file paths (only used for recursive function calls).

    Returns
    -------
    file_paths : list of str
        File paths that end with target extension.
    """
    if file_paths is None:
        file_paths = []
    if not extension.startswith('.'):
        extension = f'.{extension}'
    file_or_dir_names: List[str] = os.listdir(dir_path)
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if os.path.isdir(file_or_dir_path):
            file_paths = get_specified_ext_file_paths_recursively(
                extension=extension,
                dir_path=file_or_dir_path,
                file_paths=file_paths)
            continue
        if not file_or_dir_path.endswith(extension):
            continue
        file_paths.append(file_or_dir_path)
    return file_paths


def count_files_recursively(dir_path: str) -> int:
    """
    Count the existing files number in a specified directory
    recursively.

    Parameters
    ----------
    dir_path : str
        Target directory path.

    Returns
    -------
    count : int
        Existing files count.
    """
    if not os.path.isdir(dir_path):
        return 0
    file_or_dir_names: List[str] = os.listdir(dir_path)
    count: int = 0
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if os.path.isdir(file_or_dir_path):
            count += count_files_recursively(file_or_dir_path)
            continue
        if os.path.isfile(file_or_dir_path):
            count += 1
    return count
