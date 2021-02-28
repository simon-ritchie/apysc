"""Expression exporting interface implementation.
"""

import os
from logging import Logger
from typing import List

from apyscript.console import loggers
from apyscript.display.stage import get_stage_element_id
from apyscript.display.stage import get_stage_variable_name
from apyscript.expression import expression_file_util
from apyscript.file import file_util
from apyscript.html import html_const
from apyscript.html import html_util
from apyscript.jslib import jslib_util

info_logger: Logger = loggers.get_info_logger()


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
    info_logger.info(msg='Overall exporting started...')
    file_util.empty_directory(directory_path=dest_dir_path)
    info_logger.info(msg='JavaScript libraries exporting...')
    _ = _export_js_libs(dest_dir_path=dest_dir_path)
    html_str: str = html_util.append_html_to_str(
        to_append_html='<html>', dest_html='', indent_num=0)
    html_str = _append_head_to_html_str(html_str=html_str)
    html_str = html_util.append_html_to_str(
        to_append_html='<body>', dest_html=html_str, indent_num=0)
    html_str = _append_stage_global_variable_to_html(html_str=html_str)
    info_logger.info(msg='Reading each expression files...')
    html_str = _append_expression_to_html_str(html_str=html_str)
    html_str = html_util.append_html_to_str(
        to_append_html='</body>', dest_html=html_str, indent_num=0)
    html_str = _append_entry_point_function_call(html_str=html_str)
    html_str = html_util.append_html_to_str(
        to_append_html='</html>', dest_html=html_str, indent_num=0)
    info_logger.info(msg='HTML saving started...')
    _save_html(
        html_str=html_str, dir_path=dest_dir_path, file_name='index.html')
    file_path: str = os.path.join(dest_dir_path, 'index.html')
    info_logger.info(
        msg=f'All files were exported! \nFile path is : {file_path}')


def _append_stage_global_variable_to_html(html_str: str) -> str:
    """
    Append stage's global variable to html string.

    Parameters
    ----------
    html_str : str
        Target HTML string.

    Returns
    -------
    html_str : str
        After appended HTML string.
    """
    html_str = html_util.append_html_to_str(
        to_append_html=html_const.SCRIPT_START_TAG,
        dest_html=html_str, indent_num=0)
    html_str = html_util.append_html_to_str(
        to_append_html=f'var {get_stage_element_id()};',
        dest_html=html_str, indent_num=0)
    html_str = html_util.append_html_to_str(
        to_append_html=html_const.SCRIPT_END_TAG,
        dest_html=html_str, indent_num=0)
    return html_str


def get_entry_point_func_name() -> str:
    """
    Get an entry point function name.

    Returns
    -------
    entry_point_func_name : str
        An entry point function name.
    """
    stage_variable_name: str = get_stage_variable_name()
    entry_point_func_name: str = f'main_{stage_variable_name}'
    return entry_point_func_name


def _append_entry_point_function_call(html_str: str) -> str:
    """
    Append entry point function call script to html string.

    Parameters
    ----------
    html_str : str
        Target HTML string.

    Returns
    -------
    html_str : str
        After appended html string.
    """
    html_str += (
        '\n<script type="text/javascript">'
        '\n$(document).ready(function() {'
    )
    entry_point_func_name: str = get_entry_point_func_name()
    html_str += f'\n  {entry_point_func_name}();'
    html_str += (
        '\n});'
        '\n</script>'
    )
    return html_str


def _save_html(
        html_str: str, dir_path: str, file_name: str) -> None:
    """
    Save HTML string to file.

    Parameters
    ----------
    html_str : str
        HTML String to save.
    dir_path : str
        Destination directory path to save html.
    file_name : str
        HTML file name. e.g., 'index.html'
    """
    os.makedirs(dir_path, exist_ok=True)
    file_path: str = os.path.join(dir_path, file_name)
    file_util.save_plain_txt(txt=html_str, file_path=file_path)


def _append_expression_to_html_str(html_str: str) -> str:
    """
    Append expression strings to a specified HTML string.

    Parameters
    ----------
    html_str : str
        Target HTML string.

    Returns
    -------
    html_str : str
        HTML string after appended expressions.
    """
    expression: str = file_util.read_txt(
        file_path=expression_file_util.EXPRESSION_FILE_PATH)
    expression = html_util.append_indent_to_each_script_line(
        html=expression, indent_num=1)
    entry_point_func_name: str = get_entry_point_func_name()
    expression = expression.replace(
        f'{html_const.SCRIPT_START_TAG}',
        f'{html_const.SCRIPT_START_TAG}'
        f'\nfunction {entry_point_func_name}() {{',
        1)
    expression = expression.replace(
        f'{html_const.SCRIPT_END_TAG}',
        f'}}\n{html_const.SCRIPT_END_TAG}')

    html_str += f'\n{expression}'
    return html_str


def _append_head_to_html_str(html_str: str) -> str:
    """
    Append head tag section to specified html string.

    Parameters
    ----------
    html_str : str
        Target HTML string.

    Returns
    -------
    html_str : str
        HTML string after appended.
    """
    html_str = html_util.append_html_to_str(
        to_append_html='<head>', dest_html=html_str, indent_num=0)
    html_str = html_util.append_html_to_str(
        to_append_html='<meta charset="utf-8">',
        dest_html=html_str, indent_num=1)
    jslib_file_names: List[str] = jslib_util.get_jslib_file_names()
    for jslib_file_name in jslib_file_names:
        html_str = html_util.append_html_to_str(
            to_append_html=(
                '<script type="text/javascript" '
                f'src="./{jslib_file_name}"></script>'),
            dest_html=html_str, indent_num=1)
    html_str = html_util.append_html_to_str(
        to_append_html='</head>', dest_html=html_str, indent_num=0)
    return html_str


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
