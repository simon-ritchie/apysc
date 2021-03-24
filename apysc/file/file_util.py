"""Files' common utilities implementation.
"""

import os
import shutil
from types import ModuleType


def empty_directory(directory_path: str) -> None:
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


def read_txt(file_path: str) -> str:
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
    with open(file_path, 'r') as f:
        txt: str = f.read()
    return txt


def save_plain_txt(txt: str, file_path: str) -> None:
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
    with open(file_path, 'w') as f:
        f.write(txt)


def append_plain_txt(txt: str, file_path: str) -> None:
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
    with open(file_path, 'a') as f:
        f.write(txt)


def remove_file_if_exists(file_path: str) -> None:
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


def get_abs_directory_path_from_file_path(file_path: str) -> str:
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


def get_abs_module_dir_path(module: ModuleType) -> str:
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
    abs_module_dir_path: str = os.path.dirname(module.__file__)
    abs_module_dir_path += '/'
    return abs_module_dir_path
