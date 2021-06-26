"""Common JavaScript library utility implementations.

Mainly the following interfaces are defined:

- get_jslib_file_names
    Get the JavaScript libraries file names.
- get_jslib_abs_dir_path
    Get the Javascript library's absolute directory path.
- export_jslib_to_specified_dir
    Export a JavaScript library to specified directory.
- read_jslib_str
    Read a JavaScript library file str.
"""

import os
import shutil
import sys
from types import ModuleType
from typing import List


def get_jslib_file_names() -> List[str]:
    """
    Get the JavaScript libraries file names.

    Returns
    -------
    jslib_file_names : list of str
        JavaScript libraries file names existing in this module's
        directory.
        e.g., ['jquery.min.js', 'svg.min.js']
    """
    this_modules_dir_path: str = get_jslib_abs_dir_path()
    jslib_file_names: List[str] = []
    file_names: List[str] = os.listdir(this_modules_dir_path)
    for file_name in file_names:
        if not file_name.endswith('.js'):
            continue
        jslib_file_names.append(file_name)
    return jslib_file_names


def get_jslib_abs_dir_path() -> str:
    """
    Get the Javascript library's absolute directory path.

    Returns
    -------
    jslib_abs_dir_path : str
        Javascript library's absolute directory path.
        This module's directory will be set.
    """
    this_module: ModuleType = sys.modules[__name__]
    jslib_abs_dir_path: str = os.path.dirname(this_module.__file__)
    return jslib_abs_dir_path


def export_jslib_to_specified_dir(
        dest_dir_path: str, jslib_name: str) -> str:
    """
    Export a JavaScript library to specified directory.

    Parameters
    ----------
    dest_dir_path : str
        Directory path to export JavaScript library file.
    jslib_name : str
        JavaScript file name to export.

    Returns
    -------
    dest_file_path : str
        Exported Javascript library's file path.

    Raises
    ------
    FileNotFoundError
        If specified JavaScript file is not found.
    """
    os.makedirs(dest_dir_path, exist_ok=True)
    dir_path: str = get_jslib_abs_dir_path()
    src_file_path: str = os.path.join(dir_path, jslib_name)
    if not os.path.isfile(src_file_path):
        raise FileNotFoundError(
            'Specified JavaScript library file is not found: '
            f'{src_file_path}')
    dest_file_path: str = os.path.join(dest_dir_path, jslib_name)
    shutil.copyfile(src_file_path, dest_file_path)
    return dest_file_path


def read_jslib_str(jslib_name: str) -> str:
    """
    Read a JavaScript library file str.

    Parameters
    ----------
    jslib_name : str
        JavaScript file name to read.

    Returns
    -------
    jslib_str : str
        Read JavaScript library string.
    """
    from apysc._file import file_util
    dir_path: str = get_jslib_abs_dir_path()
    file_path: str = os.path.join(dir_path, jslib_name)
    jslib_str: str = file_util.read_txt(file_path=file_path)
    return jslib_str
