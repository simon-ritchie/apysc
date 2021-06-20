"""Common JavaScript library utility implementations.
"""

import os
import shutil
import sys
from types import ModuleType
from typing import List


def get_jslib_file_names() -> List[str]:
    """
    Get JavaScript libraries file names.

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
    Get a Javascript library's absolute directory path.

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
    Export JavaScript library to specified directory.

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
