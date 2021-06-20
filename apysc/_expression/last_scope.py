"""Interfaces and definitions for last expression's scope information.
"""

import os
from enum import Enum


class LastScope(Enum):

    NORMAL = 1
    IF = 2
    ELIF = 3
    ELSE = 4
    FOR = 5
    EVENT_HANDLER = 6


def reset() -> None:
    """
    Reset last expression's scope information.
    """
    from apysc._expression.expression_file_util import LAST_SCOPE_FILE_PATH
    from apysc._file import file_util
    file_util.remove_file_if_exists(file_path=LAST_SCOPE_FILE_PATH)


def get_last_scope() -> LastScope:
    """
    Get last scope value.

    Returns
    -------
    last_scope : LastScope
        Last scope value. If there is no last scope's value, then
        LastScope.NORMAL will be returned.
    """
    from apysc._expression.expression_file_util import LAST_SCOPE_FILE_PATH
    from apysc._file import file_util
    if not os.path.isfile(LAST_SCOPE_FILE_PATH):
        return LastScope.NORMAL
    last_scope_str: str = file_util.read_txt(file_path=LAST_SCOPE_FILE_PATH)
    if last_scope_str == '':
        return LastScope.NORMAL
    last_scope: LastScope = LastScope(int(last_scope_str))
    return last_scope


def set_last_scope(value: LastScope) -> None:
    """
    Set last scope value.

    Parameters
    ----------
    value : LastScope
        Last scope value to set.
    """
    from apysc._expression.expression_file_util import LAST_SCOPE_FILE_PATH
    from apysc._file import file_util
    file_util.save_plain_txt(
        txt=str(value.value),
        file_path=LAST_SCOPE_FILE_PATH)
