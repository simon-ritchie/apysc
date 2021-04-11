"""Implementations of expression's indent number related interfaces.

Mainly following interfaces are defined:

- get_current_indent_num: Get a current indent number.
- increment: Increment current indent number.
- decrement: Decrement current indent number.
- reset: Reset current indent number.
"""

import os


def get_current_indent_num() -> int:
    """
    Get a current indent number.

    Returns
    -------
    current_indent_num : int
        Current indent number.
    """
    from apysc.file import file_util
    file_path: str = _get_indent_num_file_path()
    if not os.path.isfile(file_path):
        return 0
    indent_num_txt: str = file_util.read_txt(file_path=file_path)
    indent_num_txt = indent_num_txt.strip()
    if indent_num_txt == '':
        return 0
    current_indent_num: int = int(indent_num_txt)
    return current_indent_num


def _get_indent_num_file_path() -> str:
    """
    Get a indent number file path. This value will switch by
    scope condition (e.g., event handler's scope or not).

    Returns
    -------
    file_path : str
        Indent number file path.
    """
    from apysc.expression import event_handler_scope
    from apysc.expression import expression_file_util
    event_handler_scope_count: int = \
        event_handler_scope.get_current_event_handler_scope_count()
    if event_handler_scope_count == 0:
        return expression_file_util.INDENT_NUM_FILE_PATH
    return expression_file_util.EVENT_HANDLER_INDENT_NUM_FILE_PATH


def increment() -> None:
    """
    Increment current indent number.
    """
    from apysc.file import file_util
    file_path: str = _get_indent_num_file_path()
    current_indent_num: int = get_current_indent_num()
    current_indent_num += 1
    file_util.save_plain_txt(
        txt=str(current_indent_num), file_path=file_path)


def decrement() -> None:
    """
    Decrement current indent number.
    """
    from apysc.file import file_util
    file_path: str = _get_indent_num_file_path()
    current_indent_num: int = get_current_indent_num()
    current_indent_num -= 1
    if current_indent_num < 0:
        current_indent_num = 0
    file_util.save_plain_txt(
        txt=str(current_indent_num), file_path=file_path)


def reset() -> None:
    """
    Reset current indent number.
    """
    from apysc.expression import expression_file_util
    from apysc.file import file_util
    file_util.remove_file_if_exists(
        file_path=expression_file_util.INDENT_NUM_FILE_PATH)
    file_util.remove_file_if_exists(
        file_path=expression_file_util.EVENT_HANDLER_INDENT_NUM_FILE_PATH)
