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

from apysc._console import loggers

info_logger: Logger = loggers.get_info_logger()


def save_overall_html(
        dest_dir_path: str,
        html_file_name: str = 'index.html',
        minify: bool = True,
        js_lib_dir_path: str = './',
        skip_js_lib_exporting: bool = False,
        embed_js_libs: bool = False,
        verbose: int = 1) -> None:
    """
    Save the overall HTML and js files under the specified
    directory path.

    Notes
    -----
    Specified directory will be emptied before saving.

    Parameters
    ----------
    dest_dir_path : str
        Destination directory path to save each HTML and js files.
    html_file_name : str, default 'index.html'
        The output HTML file name.
    minify : bool, default True
        Boolean value whether minify HTML and js or not.
        False setting is useful when debugging.
    js_lib_dir_path : str, default './'
        JavaScript libraries directory path. This setting will be
        applied to JavaScript source path in HTML.
        If not specified, then the same directory with HTML will be set.
        This setting is maybe useful to set common js lib directory,
        such as Django's static (static_collected) directory.
        It is recommended to set True value to `skip_js_lib_exporting`
        argument if this argument is set.
    skip_js_lib_exporting : bool, default False
        If True is set, then JavaScript libraries will not be exported.
    embed_js_libs: bool, default False
        Option to embed the JavaScript libraries script to the
        output HTML or not.
        If True, the output HTML will be bigger but only one HTML
        file will be exported. This option will occasionally be useful
        when you share the exported file, or use the output file with
        iframe tag and avoid the CORS error.
    verbose : int, default 1
        The Logging setting. If 0 is specified, then logging message
        will not be displayed. If 1 or the other value is specified,
        message will be displayed normally.
    """
    from apysc._file import file_util
    from apysc._html import html_util
    _display_info(msg='Overall exporting started...', verbose=verbose)
    file_util.empty_directory(directory_path=dest_dir_path)
    _display_info(msg='JavaScript libraries exporting...', verbose=verbose)
    _ = _export_js_libs(
        dest_dir_path=dest_dir_path,
        skip_js_lib_exporting=skip_js_lib_exporting)
    html_str: str = html_util.append_html_to_str(
        to_append_html='<html>', dest_html='', indent_num=0)
    html_str = _append_head_to_html_str(
        html_str=html_str, js_lib_dir_path=js_lib_dir_path,
        embed_js_libs=embed_js_libs)
    html_str = html_util.append_html_to_str(
        to_append_html='<body style="margin: 0;">',
        dest_html=html_str,
        indent_num=0)
    html_str = _append_stage_global_variable_to_html(html_str=html_str)
    html_str = _append_expression_to_html_str(
        html_str=html_str, verbose=verbose)
    html_str = html_util.append_html_to_str(
        to_append_html='</body>', dest_html=html_str, indent_num=0)
    html_str = _append_entry_point_function_call(html_str=html_str)
    html_str = html_util.append_html_to_str(
        to_append_html='</html>', dest_html=html_str, indent_num=0)
    html_str = _minify_html(html_str=html_str, minify=minify)
    _display_info(msg='HTML saving started...', verbose=verbose)
    _save_html(
        html_str=html_str, dir_path=dest_dir_path, file_name=html_file_name)
    file_path: str = os.path.join(dest_dir_path, html_file_name)
    _display_info(
        msg=f'All files were exported! \nFile path is : {file_path}',
        verbose=verbose)


def _display_info(msg: str, verbose: int) -> str:
    """
    Display a info log message.

    Parameters
    ----------
    msg : str
        A message to display.
    verbose : int
        If 0 is specified, message will not be displayed.
        1 or the other value will display the message.

    Returns
    -------
    msg : str
        Displayed message.
    """
    if verbose == 0:
        return ''
    info_logger.info(msg=msg)
    return msg


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
    from apysc._display.stage import get_stage_elem_id
    from apysc._html import html_const
    from apysc._html import html_util
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
    from apysc._display.stage import get_stage_variable_name
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
    from apysc import document
    html_str += (
        '\n<script type="text/javascript">'
        f'\n$({document.variable_name}).ready(function() {{'
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
    from apysc._file import file_util
    os.makedirs(dir_path, exist_ok=True)
    file_path: str = os.path.join(dir_path, file_name)
    file_util.save_plain_txt(txt=html_str, file_path=file_path)


def _append_expression_to_html_str(html_str: str, verbose: int) -> str:
    """
    Append expression strings to a specified HTML string.

    Parameters
    ----------
    html_str : str
        Target HTML string.
    verbose : int, default 1
        The Logging setting.

    Returns
    -------
    html_str : str
        HTML string after appended expressions.
    """
    from apysc._expression import expression_file_util
    from apysc._file import file_util
    from apysc._html import html_const
    from apysc._html import html_util
    _display_info(msg='Reading basic expression file...', verbose=verbose)
    expression: str = file_util.read_txt(
        file_path=expression_file_util.EXPRESSION_FILE_PATH)
    _display_info(msg='Appending common js functions...', verbose=verbose)
    expression = _append_common_js_functions(expression=expression)
    _display_info(
        msg='Appending event handler expressions...', verbose=verbose)
    expression = _append_event_handler_expressions(expression=expression)
    _display_info(msg='Removing unused variables...', verbose=verbose)
    expression = _remove_unused_js_vars(expression=expression)
    _display_info(msg='Removing blank lines...', verbose=verbose)
    expression = _remove_blank_lines(expression=expression)
    expression = html_util.wrap_expression_by_script_tag(
        expression=expression)
    _display_info(msg='Appending indentations...', verbose=verbose)
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
    from apysc._expression import expression_file_util
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
    from apysc._expression import js_functions
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
    used_pattern: Pattern = re.compile(pattern=rf'{var_name}[ ;\)\.}},\]\[]')
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


def _append_head_to_html_str(
        html_str: str, js_lib_dir_path: str,
        embed_js_libs: bool) -> str:
    """
    Append head tag section to specified html string.

    Parameters
    ----------
    html_str : str
        Target HTML string.
    js_lib_dir_path : str
        JavaScript libraries directory path.
    embed_js_libs: bool, default False
        Option to embed the JavaScript libraries script to the
        output HTML or not.

    Returns
    -------
    html_str : str
        HTML string after appended.
    """
    from apysc._html import html_util
    from apysc._jslib import jslib_util
    html_str = html_util.append_html_to_str(
        to_append_html='<head>', dest_html=html_str, indent_num=0)
    html_str = html_util.append_html_to_str(
        to_append_html='<meta charset="utf-8">',
        dest_html=html_str, indent_num=1)
    jslib_file_names: List[str] = jslib_util.get_jslib_file_names()
    for jslib_file_name in jslib_file_names:
        html_str = _append_jslib_str_to_html(
            html_str=html_str,
            js_lib_dir_path=js_lib_dir_path,
            jslib_file_name=jslib_file_name,
            embed_js_libs=embed_js_libs)
    html_str = html_util.append_html_to_str(
        to_append_html='</head>', dest_html=html_str, indent_num=0)
    return html_str


def _append_jslib_str_to_html(
        html_str: str, js_lib_dir_path: str,
        jslib_file_name: str,
        embed_js_libs: bool) -> str:
    """
    Append JavaScript libraries script string to HTML.

    Parameters
    ----------
    html_str : str
        A HTML string to be appended.
    js_lib_dir_path : str
        Target libraries directory path.
        If the `embed_js_libs` option is True, then this setting
        will be ignored.
    jslib_file_name : str
        Target JavaScript library file name.
    embed_js_libs: bool, default False
        Option to embed the JavaScript libraries script to the
        output HTML or not.

    Returns
    -------
    html_str : str
        Result HTML string.
    """
    from apysc._html import html_util
    from apysc._jslib import jslib_util
    if not embed_js_libs:
        html_str = html_util.append_html_to_str(
            to_append_html=(
                '<script type="text/javascript" '
                f'src="{js_lib_dir_path}{jslib_file_name}"></script>'),
            dest_html=html_str, indent_num=1)
        return html_str

    js_script: str = (
        '<script type="text/javascript">'
        f'\n  {jslib_util.read_jslib_str(jslib_name=jslib_file_name)}'
        '\n  </script>'
    )
    html_str = html_util.append_html_to_str(
        to_append_html=js_script, dest_html=html_str, indent_num=1)
    return html_str


def _export_js_libs(
        dest_dir_path: str, skip_js_lib_exporting: bool) -> List[str]:
    """
    Export JavaScript libraries to a specified directory.

    Parameters
    ----------
    dest_dir_path : str
        Directory path to export JavaScript libraries.
    skip_js_lib_exporting : bool
        If True is set, then JavaScript libraries will not be exported.

    Returns
    -------
    saved_js_file_paths : str
        Saved JavaScript file paths.
    """
    if skip_js_lib_exporting:
        return []

    from apysc._jslib import jslib_util
    jslib_file_names: List[str] = jslib_util.get_jslib_file_names()
    saved_js_file_paths: List[str] = []
    for jslib_file_name in jslib_file_names:
        saved_js_file_path: str = jslib_util.export_jslib_to_specified_dir(
            dest_dir_path=dest_dir_path, jslib_name=jslib_file_name)
        saved_js_file_paths.append(saved_js_file_path)
    return saved_js_file_paths
