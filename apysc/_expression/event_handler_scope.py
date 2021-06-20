"""Implementations for event handler's expression scope
interfaces.
"""

import os
from typing import Any


class HandlerScope:
    """
    Class for a handler scope. This is used at a with statement.
    """

    def __init__(self) -> None:
        """
        Class for a handler scope. This is used at a with statement.
        """

    def __enter__(self) -> None:
        """
        Enter and set an event handler scope setting.
        """
        _increment_scope_count()

    def __exit__(self, *args: Any) -> None:
        """
        Exit and remove an event handler scope setting.

        Parameters
        ----------
        *args : list
            Positional arguments.
        """
        _decrement_scope_count()


class TemporaryNotHandlerScope:
    """
    Class temporarily sets up a scope that is not a handler.
    This is used at a with statement.
    """

    _original_scope_count: int

    def __init__(self) -> None:
        """
        Class temporarily sets up a scope that is not a handler.
        This is used at a with statement.
        """
        self._original_scope_count = get_current_event_handler_scope_count()

    def __enter__(self) -> None:
        """
        Enter and set the scope count to zero.
        """
        _save_current_scope_count(count=0)

    def __exit__(self, *args: Any) -> None:
        """
        Exit and revert the scope count.

        Parameters
        ----------
        *args : list
            Positional arguments.
        """
        _save_current_scope_count(count=self._original_scope_count)


def _increment_scope_count() -> None:
    """
    Increment current scope count.
    """
    scope_count: int = get_current_event_handler_scope_count()
    scope_count += 1
    _save_current_scope_count(count=scope_count)


def _decrement_scope_count() -> None:
    """
    Decrement current scope count.
    """
    scope_count: int = get_current_event_handler_scope_count()
    scope_count -= 1
    scope_count = max(scope_count, 0)
    _save_current_scope_count(count=scope_count)


def _save_current_scope_count(count: int) -> None:
    """
    Save current scope count.

    Parameters
    ----------
    count : int
        Scope count ot save.
    """
    from apysc._expression.expression_file_util import \
        EVENT_HANDLER_SCOPE_COUNT_FILE_PATH
    from apysc._file import file_util
    file_util.save_plain_txt(
        txt=str(count),
        file_path=EVENT_HANDLER_SCOPE_COUNT_FILE_PATH)


def get_current_event_handler_scope_count() -> int:
    """
    Get a current event handler's scope count.

    Returns
    -------
    scope_count : int
        Current event handler's scope count.
        If normal handler's call, then 1 will be returned,
        or call other handler in handler's function, then
        2 or more count will be returned.
    """
    from apysc._expression import expression_file_util
    from apysc._file import file_util
    file_path: str = expression_file_util.EVENT_HANDLER_SCOPE_COUNT_FILE_PATH
    if not os.path.isfile(file_path):
        return 0
    txt: str = file_util.read_txt(file_path=file_path)
    txt = txt.strip()
    if not txt.isdigit():
        return 0
    scope_count: int = int(txt)
    return scope_count
