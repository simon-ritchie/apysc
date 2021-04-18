"""Expression exporting interface implementation.
"""

import os
import re
from logging import Logger
from typing import List
from typing import Match
from typing import Optional
from typing import Pattern

from html_minifier.minify import Minifier

from apysc.console import loggers

info_logger: Logger = loggers.get_info_logger()


def save_expressions_overall_html(
        dest_dir_path: str, minify: bool = True) -> None:
    """
    Save each expressions html under the specified directory path.

    Notes
    -----
    Specified directory will be emptied before saving.

    Parameters
    ----------
    dest_dir_path : str
        Destination directory path to save each html and js files.
    minify : bool, default True
        Boolean value whether minify HTML and js or not.
        False setting is useful when debugging.
    """
    from apysc.file import file_util
    from apysc.html import html_util
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
    html_str = _append_expression_to_html_str(html_str=html_str)
    html_str = html_util.append_html_to_str(
        to_append_html='</body>', dest_html=html_str, indent_num=0)
    html_str = _append_entry_point_function_call(html_str=html_str)
    html_str = html_util.append_html_to_str(
        to_append_html='</html>', dest_html=html_str, indent_num=0)
    html_str = _minify_html(html_str=html_str, minify=minify)
    info_logger.info(msg='HTML saving started...')
    _save_html(
        html_str=html_str, dir_path=dest_dir_path, file_name='index.html')
    file_path: str = os.path.join(dest_dir_path, 'index.html')
    info_logger.info(
        msg=f'All files were exported! \nFile path is : {file_path}')


def _minify_html(html_str: str, minify: bool) -> str:
    """
    Minify HTML and js string.

    Parameters
    ----------
    html_str : str
        HTML string to minify.
    minify : bool
        Boolean value whether minify HTML and js or not.
        If False, then minifying will be skipped.

    Returns
    -------
    html_str : str
        Result html string.
    """
    if not minify:
        return html_str
    minifier = Minifier(html=html_str)
    html_str = minifier.minify()
    return html_str


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
    from apysc.display.stage import get_stage_elem_id
    from apysc.html import html_const
    from apysc.html import html_util
    html_str = html_util.append_html_to_str(
        to_append_html=html_const.SCRIPT_START_TAG,
        dest_html=html_str, indent_num=0)
    html_str = html_util.append_html_to_str(
        to_append_html=f'var {get_stage_elem_id()};',
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
    from apysc.display.stage import get_stage_variable_name
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
    from apysc.file import file_util
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
    from apysc.expression import expression_file_util
    from apysc.file import file_util
    from apysc.html import html_const
    from apysc.html import html_util
    info_logger.info(msg='Reading basic expression file...')
    expression: str = file_util.read_txt(
        file_path=expression_file_util.EXPRESSION_FILE_PATH)
    info_logger.info(msg='Appending common js functions...')
    expression = _append_common_js_functions(expression=expression)
    info_logger.info(msg='Appending event handler expressions...')
    expression = _append_event_handler_expressions(expression=expression)
    info_logger.info(msg='Removing unused variables...')
    expression = _remove_unused_js_vars(expression=expression)
    info_logger.info(msg='Removing blank lines...')
    expression = _remove_blank_lines(expression=expression)
    expression = html_util.wrap_expression_by_script_tag(
        expression=expression)
    info_logger.info(msg='Appending indentations...')
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


def _append_event_handler_expressions(expression: str) -> str:
    """
    Append event handler's expressions to a specified string.

    Parameters
    ----------
    expression : str
        Expression string to append event handler's one.

    Returns
    -------
    expression : str
        Result expression string.
    """
    from apysc.expression import expression_file_util
    event_handler_scope_expression: str = \
        expression_file_util.get_current_event_handler_scope_expression()
    expression = f'{expression}\n{event_handler_scope_expression}'
    return expression


def _remove_blank_lines(expression: str) -> str:
    """
    Remove blank (break or spaces only) lines from expression string.

    Parameters
    ----------
    expression : str
        Target expression string.

    Returns
    -------
    expression : str
        Expression string that removed blank lines.
    """
    lines: List[str] = expression.splitlines()
    result_lines: List[str] = []
    pattern: Pattern = re.compile(pattern=r'^\s*$')
    for line in lines:
        match: Optional[Match] = pattern.match(string=line)
        if match is not None:
            continue
        result_lines.append(line)
    expression = '\n'.join(result_lines)
    return expression


def _append_common_js_functions(expression: str) -> str:
    """
    Append common JavaScript functions (e.g., helper function)
    to a expression string.

    Parameters
    ----------
    expression : str
        Target expression string.

    Returns
    -------
    expression : str
        Expression string that common functions are appended.
    """
    from apysc.expression import js_functions
    js_function_strs: List[str] = js_functions.get_js_functions()
    js_function_strs.reverse()
    for js_function in js_function_strs:
        expression = f'{js_function}\n{expression}'
    return expression


def _remove_unused_js_vars(expression: str) -> str:
    """
    Remove unused js variables from expression string.

    Parameters
    ----------
    expression : str
        Target js expression string.

    Returns
    -------
    expression : str
        After removing expression string.
    """
    lines: List[str] = expression.splitlines()
    lines.reverse()
    current_line_idx: int = 0
    while True:
        if current_line_idx >= len(lines):
            break
        var_name: str = _get_var_name_from_line(line=lines[current_line_idx])
        if var_name == '':
            current_line_idx += 1
            continue
        target_js_variable_is_used: bool = _target_js_variable_is_used(
            var_name=var_name, exp_lines=lines)
        if not target_js_variable_is_used:
            del lines[current_line_idx]
            continue
        current_line_idx += 1
    lines.reverse()
    expression = '\n'.join(lines)
    return expression


def _target_js_variable_is_used(
        var_name: str, exp_lines: List[str]) -> bool:
    """
    Get a boolean value whether target variable is used in
    js expression or not.

    Parameters
    ----------
    var_name : str
        Target variable name.
    exp_lines : list of str
        js expression lines.

    Returns
    -------
    result : bool
        If target variable is used in js expression, True will be
        returned.
    """
    var_pattern: Pattern = re.compile(pattern=rf'var ({var_name}) = ')
    used_pattern: Pattern = re.compile(pattern=rf'{var_name}[ ;\)\.}},\]]')
    for line in exp_lines:
        match: Optional[Match] = var_pattern.search(string=line)
        if match is not None:
            continue
        match = used_pattern.search(string=line)
        if match is not None:
            return True
    return False


_VAR_PATTERN: Pattern = re.compile(pattern=r'^var (.+?) = ')


def _get_var_name_from_line(line: str) -> str:
    """
    Get a js variable name from specified line string.

    Parameters
    ----------
    line : str
        Target line string.

    Returns
    -------
    var_name : str
        Result variable name. If line contains `var <any_name> = ...;`
        pattern, then `any_name` will be returned. Or if there is no
        var expression, blank string will be returned.
    """
    line = line.strip()
    match: Optional[Match] = _VAR_PATTERN.search(string=line)
    if match is None:
        return ''
    var_name: str = match.group(1)
    return var_name


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
    from apysc.html import html_util
    from apysc.jslib import jslib_util
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
    from apysc.jslib import jslib_util
    jslib_file_names: List[str] = jslib_util.get_jslib_file_names()
    saved_js_file_paths: List[str] = []
    for jslib_file_name in jslib_file_names:
        saved_js_file_path: str = jslib_util.export_jslib_to_specified_dir(
            dest_dir_path=dest_dir_path, jslib_name=jslib_file_name)
        saved_js_file_paths.append(saved_js_file_path)
    return saved_js_file_paths
