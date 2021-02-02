"""Expression exporting interface implementation.
"""

from typing import List
from apyscript.file import file_util
from apyscript.jslib import jslib_util


def save_expressions_overall_html(dest_dir_path: str) -> None:
    """
    Save each expressions html under the specified directory path.

    Notes
    -----
    Specified directory will be emptied before saving.

    Parameters
    ----------
    dest_dir_path : str
        Destination directory path to save each html and js files.
    """
    file_util.empty_directory(directory_path=dest_dir_path)
    _ = _export_js_libs(dest_dir_path=dest_dir_path)
    pass


def _export_js_libs(dest_dir_path: str) -> List[str]:
    """
    Export JavaScript libraries to a specified directory.

    Parameters
    ----------
    dest_dir_path : str
        Directory path to export JavaScript libraries.

    Returns
    -------
    saved_js_file_paths : str
        Saved JavaScript file paths.
    """
    jslib_file_names: List[str] = jslib_util.get_jslib_file_names()
    saved_js_file_paths: List[str] = []
    for jslib_file_name in jslib_file_names:
        saved_js_file_path: str = jslib_util.export_jslib_to_specified_dir(
            dest_dir_path=dest_dir_path, jslib_name=jslib_file_name)
        saved_js_file_paths.append(saved_js_file_path)
    return saved_js_file_paths
