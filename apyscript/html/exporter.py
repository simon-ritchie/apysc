"""Expression exporting interface implementation.
"""

from typing import List
from apyscript.file import file_util
from apyscript.jslib import jslib_util
from apyscript.html import html_util
from apyscript.expression import expression_file_util


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
    html_str: str = html_util.append_html_to_str(
        to_append_html='<html>', dest_html='', indent_num=0)
    html_str = _append_head_to_html_str(html_str=html_str)
    pass


def _append_head_to_html_str(html_str: str) -> str:
    """
    Append head tab section to specified html string.

    Parameters
    ----------
    html_str : str
        Target HTML string.

    Returns
    -------
    html_str : str
        HTML string after appended.
    """
    # html_str = html_util.append_html_to_str(to_append_html='')
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
