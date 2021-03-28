"""Interfaces and definitions for last expression's scope information.
"""

from enum import Enum


class LastScope(Enum):

    NORMAL = 1
    IF = 2
    ELIF = 3
    ELSE = 4


def reset() -> None:
    """
    Reset last expression's scope information.
    """
    from apysc.expression.expression_file_util import LAST_SCOPE_FILE_PATH
    from apysc.file import file_util
    file_util.remove_file_if_exists(file_path=LAST_SCOPE_FILE_PATH)
