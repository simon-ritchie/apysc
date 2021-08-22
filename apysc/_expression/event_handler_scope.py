"""Implementations for the event handler's expression scope
interfaces.
"""

from typing import Any, Optional, Tuple


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
    from apysc._expression import expression_file_util
    expression_file_util.initialize_sqlite_tables_if_not_initialized()
    query: str = (
        'DELETE FROM '
        f'{expression_file_util.TableName.EVENT_HANDLER_SCOPE_COUNT.value};'
    )
    expression_file_util.cursor.execute(query)
    query = (
        'INSERT INTO '
        f'{expression_file_util.TableName.EVENT_HANDLER_SCOPE_COUNT.value}'
        f'(count) VALUES({count});'
    )
    expression_file_util.cursor.execute(query)
    expression_file_util.connection.commit()


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
    expression_file_util.initialize_sqlite_tables_if_not_initialized()
    query: str = (
        'SELECT count FROM '
        f'{expression_file_util.TableName.EVENT_HANDLER_SCOPE_COUNT.value} '
        'LIMIT 1;'
    )
    expression_file_util.cursor.execute(query)
    result: Optional[Tuple] = expression_file_util.cursor.fetchone()
    expression_file_util.connection.commit()
    if result is None:
        return 0
    scope_count: int = int(result[0])
    return scope_count
