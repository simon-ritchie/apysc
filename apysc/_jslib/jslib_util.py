"""Common JavaScript library utility implementations.

Mainly the following interfaces are defined:

- get_jslib_file_names
    Get the JavaScript libraries file's names.
- get_jslib_abs_dir_path
    Get the Javascript library's absolute directory path.
    This interface returns this module's directory.
- export_jslib_to_specified_dir
    Export a JavaScript library to a specified directory.
- read_jslib_str
    Read a JavaScript library file str.
"""

import os
import re
import shutil
import sys
from types import ModuleType
from typing import List
from typing import Match
from typing import Optional


def get_jslib_file_names() -> List[str]:
    """
    Get the JavaScript libraries file's names.

    Returns
    -------
    jslib_file_names : list of str
        JavaScript libraries file names existing in this module's
        directory.
        e.g., ['jquery-3.5.1.min.js', 'svg-3.1.2.min.js']
    """
    this_modules_dir_path: str = get_jslib_abs_dir_path()
    jslib_file_names: List[str] = []
    file_names: List[str] = os.listdir(this_modules_dir_path)
    for file_name in file_names:
        if not file_name.endswith(".js"):
            continue
        jslib_file_names.append(file_name)
    jslib_file_names = _sort_js_file_names_with_priority_setting(
        jslib_file_names=jslib_file_names
    )
    return jslib_file_names


def _sort_js_file_names_with_priority_setting(
    *, jslib_file_names: List[str]
) -> List[str]:
    """
    Sort a JavaScript libraries' file names list
    with the priority setting.

    Parameters
    ----------
    jslib_file_names : List[str]
        A target list to sort.

    Returns
    -------
    sorted_jslib_file_names : List[str]
        A sorted list.
    """
    jslib_file_names.sort()
    sorted_jslib_file_names: List[str] = _HIGH_PRIORITY_FILE_ORDERS.copy()
    for jslib_file_name in jslib_file_names:
        if jslib_file_name in _HIGH_PRIORITY_FILE_ORDERS:
            continue
        sorted_jslib_file_names.append(jslib_file_name)
    return sorted_jslib_file_names


def get_jslib_abs_dir_path() -> str:
    """
    Get the Javascript library's absolute directory path.
    This interface returns this module's directory.

    Returns
    -------
    jslib_abs_dir_path : str
        Javascript library's absolute directory path.
        This module's directory will be set.
    """
    this_module: ModuleType = sys.modules[__name__]
    jslib_abs_dir_path: str = os.path.dirname(str(this_module.__file__))
    return jslib_abs_dir_path


def get_jquery_file_name() -> str:
    """
    Get the jQuery file name.

    Returns
    -------
    file_name : str
        The jQuery file name.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    """
    this_modules_dir_path: str = get_jslib_abs_dir_path()
    jslib_file_names: List[str] = []
    file_names: List[str] = os.listdir(this_modules_dir_path)
    for file_name in file_names:
        if not file_name.endswith(".js"):
            continue
        jslib_file_names.append(file_name)
    for jslib_name in jslib_file_names:
        match: Optional[Match] = re.search(
            pattern=r"jquery-\d+?\.\d+?\.\d+?\.min\.js", string=jslib_name
        )
        if match is None:
            continue
        return jslib_name
    raise FileNotFoundError("The jQuery file does not exist in the _jslib package.")


_HIGH_PRIORITY_FILE_ORDERS: List[str] = [
    get_jquery_file_name(),
]


def export_jslib_to_specified_dir(*, dest_dir_path: str, jslib_name: str) -> str:
    """
    Export a JavaScript library to a specified directory.

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
        If there is no specified JavaScript file.
    """
    os.makedirs(dest_dir_path, exist_ok=True)
    dir_path: str = get_jslib_abs_dir_path()
    src_file_path: str = os.path.join(dir_path, jslib_name)
    if not os.path.isfile(src_file_path):
        raise FileNotFoundError(
            "Specified JavaScript library file is not found: " f"{src_file_path}"
        )
    dest_file_path: str = os.path.join(dest_dir_path, jslib_name)
    shutil.copyfile(src_file_path, dest_file_path)
    return dest_file_path


def read_jslib_str(*, jslib_name: str) -> str:
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
