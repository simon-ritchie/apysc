"""The implementation of manipulating HTL and js expression files.

Mainly following interfaces are defined:

- empty_expression_dir : Remove expression directory
    (EXPRESSION_ROOT_DIR) to initialize.
- append_js_expression : Append js expression to the file.
- get_current_expression : Get current expression string.
- get_current_event_handler_scope_expression : Get a current
    event handler scope's expression string from a file.
- remove_expression_file : Remove the expression file.
"""

import os

EXPRESSION_ROOT_DIR: str = '../.apysc_expression/'
EXPRESSION_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'expression.txt')
EVENT_HANDLER_EXPRESSION_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'event_handler_expression.txt')
INDENT_NUM_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'indent_num.txt')
EVENT_HANDLER_INDENT_NUM_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'event_handler_indent_num.txt')
LAST_SCOPE_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'last_scope.txt')
EVENT_HANDLER_SCOPE_COUNT_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'event_handler_scope_count.txt')


def empty_expression_dir() -> None:
    """
    Remove expression directory (EXPRESSION_ROOT_DIR) to initialize.
    """
    from apysc._file import file_util
    file_util.empty_directory(directory_path=EXPRESSION_ROOT_DIR)


def append_js_expression(expression: str) -> None:
    """
    Append js expression to the file.

    Parameters
    ----------
    expression : str
        JavaScript Expression string.
    """
    from apysc._expression import indent_num
    from apysc._expression import last_scope
    from apysc._file import file_util
    from apysc._string import indent_util
    current_indent_num: int = indent_num.get_current_indent_num()
    expression = indent_util.append_spaces_to_expression(
        expression=expression, indent_num=current_indent_num)
    file_path: str = _get_expression_file_path()
    dir_path: str = file_util.get_abs_directory_path_from_file_path(
        file_path=file_path)
    os.makedirs(dir_path, exist_ok=True)
    file_util.append_plain_txt(
        txt=f'{expression}\n', file_path=file_path)
    last_scope.set_last_scope(value=last_scope.LastScope.NORMAL)


def _get_expression_file_path() -> str:
    """
    Get a expression file path. It will switch that current scope
    is event handler's one or not.

    Returns
    -------
    file_path : str
        Expression file path.
    """
    from apysc._expression import event_handler_scope
    event_handler_scope_count: int = \
        event_handler_scope.get_current_event_handler_scope_count()
    if event_handler_scope_count == 0:
        return EXPRESSION_FILE_PATH
    return EVENT_HANDLER_EXPRESSION_FILE_PATH


def get_current_expression() -> str:
    """
    Get a current expression's string from a file.

    Notes
    -----
    If it is necessary to get event handler scope's expression,
    then use get_current_event_handler_scope_expression function
    instead.

    Returns
    -------
    current_expression : str
        Current expression's string.
    """
    current_expression: str = _get_current_expression(
        file_path=EXPRESSION_FILE_PATH)
    return current_expression


def get_current_event_handler_scope_expression() -> str:
    """
    Get a current event handler scope's expression string from a file.

    Notes
    -----
    If it is necessary to get normal scope's expression, then use
    get_current_expression function instead.

    Returns
    -------
    current_expression : str
        Current expression's string.
    """
    current_expression: str = _get_current_expression(
        file_path=EVENT_HANDLER_EXPRESSION_FILE_PATH)
    return current_expression


def _get_current_expression(file_path: str) -> str:
    """
    Get a current expression's string from specified file path.

    Parameters
    ----------
    file_path : str
        Target file path.

    Returns
    -------
    current_expression : str
        Current expression's string.
    """
    from apysc._file import file_util
    if not os.path.isfile(file_path):
        return ''
    current_expression: str = file_util.read_txt(
        file_path=file_path)
    current_expression = current_expression.strip()
    return current_expression


def remove_expression_file() -> None:
    """
    Remove expression file.
    """
    from apysc._file import file_util
    file_util.remove_file_if_exists(file_path=EXPRESSION_FILE_PATH)
    file_util.remove_file_if_exists(
        file_path=EVENT_HANDLER_SCOPE_COUNT_FILE_PATH)
    file_util.remove_file_if_exists(
        file_path=EVENT_HANDLER_EXPRESSION_FILE_PATH)
