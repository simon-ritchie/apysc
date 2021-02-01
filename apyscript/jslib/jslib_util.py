"""Common JavaScript library utility implementations.
"""

import os
import sys
from typing import List
from types import ModuleType


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
    this_module: ModuleType = sys.modules[__name__]
    this_modules_dir_path: str = os.path.dirname(this_module.__file__)
    jslib_file_names: List[str] = []
    file_names: List[str] = os.listdir(this_modules_dir_path)
    for file_name in file_names:
        if not file_name.endswith('.js'):
            continue
        jslib_file_names.append(file_name)
    return jslib_file_names
