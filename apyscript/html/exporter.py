"""Expression exporting interface implementation.
"""

from logging import Logger

from typing import List
import os

from apyscript.file import file_util
from apyscript.jslib import jslib_util
from apyscript.html import html_util
from apyscript.expression import expression_file_util, expression_scope
from apyscript.logging import loggers

user_info_logger: Logger = loggers.get_user_info_logger()


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
    user_info_logger.info(msg='Overall exporting started...')
    file_util.empty_directory(directory_path=dest_dir_path)
    user_info_logger.info(msg='JavaScript libraries exporting...')
    _ = _export_js_libs(dest_dir_path=dest_dir_path)
    html_str: str = html_util.append_html_to_str(
        to_append_html='<html>', dest_html='', indent_num=0)
    html_str = _append_head_to_html_str(html_str=html_str)
    html_str = html_util.append_html_to_str(
        to_append_html='<body>', dest_html=html_str, indent_num=0)
    user_info_logger.info(msg='Reading each expression files...')
    html_str = _append_each_expression_to_html_str(html_str=html_str)
    html_str = html_util.append_html_to_str(
        to_append_html='</body>', dest_html=html_str, indent_num=0)
    html_str = html_util.append_html_to_str(
        to_append_html='</html>', dest_html=html_str, indent_num=0)
    user_info_logger.info(msg='HTML saving started...')
    _save_html(
        html_str=html_str, dir_path=dest_dir_path, file_name='index.html')
    file_path: str = os.path.join(dest_dir_path, 'index.html')
    user_info_logger.info(
        msg=f'All files were exported! \nFile path is : {file_path}')


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


def _append_each_expression_to_html_str(html_str: str) -> str:
    """
    Append each expression strings to a specified HTML string.

    Parameters
    ----------
    html_str : str
        Target HTML string.

    Returns
    -------
    html_str : str
        HTML string after appended each expressions.
    """
    expression_file_paths: List[str] = \
        expression_file_util.get_expression_file_paths()
    for expression_file_path in expression_file_paths:
        expression: str = file_util.read_txt(file_path=expression_file_path)
        expression = html_util.append_indent_to_each_line(
            html=expression, indent_num=1)
        # expression = expression_scope.append_scope_wrapper_func_to_expression(
        #     expression=expression,
        #     expression_file_name=os.path.basename(expression_file_path))
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
