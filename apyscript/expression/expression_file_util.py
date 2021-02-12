"""The implementation of manipulating HTL and js expression files.

Mainly following interfaces are defined:

- empty_expression_dir : Remove expression directory
    (EXPRESSION_ROOT_DIR) to initialize.
- append_expression : Append html and js expression to specified
    scope's file.
- append_expression_to_current_scope : Append html and js
    expression to current scope's file.
- get_scope_file_path_from_scope : Get scope file path from
    specified scope string.
- get_expression_file_paths : Get existing expression file paths.
- get_current_scope_expression_file_path : Get current scope's
    expression file path.
- get_current_scope_expression : Get current scope's expression string.
- remove_current_scope_expression_file : Remove current scope's
    expression file.
"""

import os
from typing import Dict, List, Optional

from apyscript.file import file_util
from apyscript.expression import expression_scope
from apyscript.html.html_util import ScriptLineUtil
from apyscript.html import html_const

EXPRESSION_ROOT_DIR: str = '../.apyscript_expression/'
CURRENT_SCOPE_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'current_scope.txt')
SCOPE_HISTORY_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'scope_history.txt')

MAINTAINING_FILE_PATHS: List[str] = [
    CURRENT_SCOPE_FILE_PATH,
    SCOPE_HISTORY_FILE_PATH,
]


def empty_expression_dir() -> None:
    """
    Remove expression directory (EXPRESSION_ROOT_DIR) to initialize.

    Notes
    -----
    Files that contained in MAINTAINING_FILE_PATHS will not be removed.
    """
    maintaining_files_txt: Dict[str, str] = _get_maintaining_files_txt()
    file_util.empty_directory(directory_path=EXPRESSION_ROOT_DIR)
    _restore_maintaining_files(maintaining_files_txt=maintaining_files_txt)


def _restore_maintaining_files(
        maintaining_files_txt: Dict[str, str]) -> None:
    """
    Restore txt files that contained in MAINTAINING_FILE_PATHS.

    Parameters
    ----------
    maintaining_files_txt : dict
        Dict value that has file paths in key and files's text in value.
    """
    for file_path, text in maintaining_files_txt.items():
        file_util.save_plain_txt(txt=text, file_path=file_path)


def _get_maintaining_files_txt() -> Dict[str, str]:
    """
    Get maintaining files (not remove at empty function) text.

    Returns
    -------
    maintaining_files_txt : dict
        Dict value that has file paths in key and files's text in value.
    """
    maintaining_files_txt: Dict[str, str] = {}
    for file_path in MAINTAINING_FILE_PATHS:
        if not os.path.isfile(file_path):
            continue
        txt: str = file_util.read_txt(file_path=file_path)
        maintaining_files_txt[file_path] = txt
    return maintaining_files_txt


ROOT_SCOPE: str = 'root'


def append_expression(expression: str, scope: Optional[str] = None) -> None:
    """
    Append html and js expression to specified scope's file.

    Parameters
    ----------
    expression : str
        HTML and js Expression string.
    scope : str, optional
        Target scope name. If skipped, this will be root scope.
    """
    scope_file_path: str = get_scope_file_path_from_scope(scope=scope)
    dir_path: str = file_util.get_abs_directory_path_from_file_path(
        file_path=scope_file_path)
    os.makedirs(dir_path, exist_ok=True)
    file_util.append_plain_txt(
        txt=f'{expression}\n', file_path=scope_file_path)
    _merge_script_section(scope_file_path=scope_file_path)


def _merge_script_section(scope_file_path: str) -> None:
    """
    Merge specified scope expression's script section (If there are
    multiple script tag in same scope file, then they will be merged).

    Parameters
    ----------
    scope_file_path : str
        Target scope's file path.
    """
    result_expression: str = ''
    current_expression: str = file_util.read_txt(file_path=scope_file_path)
    current_exp_lines: List[str] = current_expression.splitlines()
    script_line_util: ScriptLineUtil = ScriptLineUtil(
        html=current_expression)
    script_strings: str = ''
    for i, current_exp_line in enumerate(current_exp_lines):
        if current_exp_line == html_const.SCRIPT_START_TAG:
            continue
        if current_exp_line == html_const.SCRIPT_END_TAG:
            continue
        line_num: int = i + 1
        if script_line_util.is_script_line(line_number=line_num):
            if current_exp_line == '':
                continue
            script_strings += f'{current_exp_line}\n'
            continue
        result_expression += f'{current_exp_line}\n'
    if script_strings != '':
        result_expression += (
            f'{html_const.SCRIPT_START_TAG}\n'
            f'{script_strings}'
            f'{html_const.SCRIPT_END_TAG}\n'
        )
    file_util.save_plain_txt(
        txt=result_expression, file_path=scope_file_path)


def append_expression_to_current_scope(expression: str) -> None:
    """
    Append html and js expression to current scope's file.

    Parameters
    ----------
    expression : str
        HTML and js Expression string.
    """
    scope: str = expression_scope.get_current_scope()
    append_expression(expression=expression, scope=scope)


def get_scope_file_path_from_scope(scope: Optional[str] = None) -> str:
    """
    Get scope file path from specified scope string.

    Parameters
    ----------
    scope : str, optional
        Target scope name. If None is specified, this will be root scope.

    Returns
    -------
    scope_file_path : str
        Result scope file path string (include html extension).
    """
    if scope is None:
        scope = ROOT_SCOPE
    if not scope.endswith('.html'):
        scope += '.html'
    scope_file_path: str = os.path.join(EXPRESSION_ROOT_DIR, scope)
    return scope_file_path


def get_expression_file_paths() -> List[str]:
    """
    Get existing expression file paths.

    Returns
    -------
    expression_file_paths : list of str
        Existing expression file paths.
    """
    expression_file_paths: List[str] = []
    file_names: List[str] = os.listdir(EXPRESSION_ROOT_DIR)
    for file_name in file_names:
        if not file_name.endswith('.html'):
            continue
        file_path: str = os.path.join(EXPRESSION_ROOT_DIR, file_name)
        expression_file_paths.append(file_path)
    return expression_file_paths


def get_current_scope_expression_file_path() -> str:
    """
    Get current scope's expression file path.

    Returns
    -------
    file_path : str
        Current scope's expression file path.
    """
    current_scope: str = expression_scope.get_current_scope()
    file_path: str = get_scope_file_path_from_scope(scope=current_scope)
    return file_path


def get_current_scope_expression() -> str:
    """
    Get current scope's expression string from file.

    Returns
    -------
    current_scope_expression : str
        Current scope's expression string.
    """
    file_path: str = get_current_scope_expression_file_path()
    if not os.path.isfile(file_path):
        return ''
    current_scope_expression: str = file_util.read_txt(
        file_path=file_path)
    current_scope_expression = current_scope_expression.strip()
    return current_scope_expression


def remove_current_scope_expression_file() -> None:
    """
    Remove current scope's expression file.
    """
    file_path: str = get_current_scope_expression_file_path()
    file_util.remove_file_if_exists(file_path=file_path)
