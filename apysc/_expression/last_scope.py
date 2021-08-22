"""Interfaces and definitions for last expression's scope information.
"""

from enum import Enum
from typing import Optional, Tuple


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
    from apysc._expression import expression_file_util
    expression_file_util.initialize_sqlite_tables_if_not_initialized()
    query: str = (
        f'DELETE FROM {expression_file_util.TableName.LAST_SCOPE.value};'
    )
    expression_file_util.cursor.execute(query)
    expression_file_util.connection.commit()



def get_last_scope() -> LastScope:
    """
    Get last scope value.

    Returns
    -------
    last_scope : LastScope
        Last scope value. If there is no last scope's value, then
        LastScope.NORMAL will be returned.
    """
    from apysc._expression import expression_file_util
    expression_file_util.initialize_sqlite_tables_if_not_initialized()
    query: str = (
        'SELECT last_scope FROM '
        f'{expression_file_util.TableName.LAST_SCOPE.value} '
        'LIMIT 1;'
    )
    expression_file_util.cursor.execute(query)
    result: Optional[Tuple[int]] = expression_file_util.cursor.fetchone()
    if result is None:
        return LastScope.NORMAL
    last_scope: LastScope = LastScope(result[0])
    return last_scope


def set_last_scope(value: LastScope) -> None:
    """
    Set last scope value.

    Parameters
    ----------
    value : LastScope
        Last scope value to set.
    """
    from apysc._expression import expression_file_util
    reset()
    query: str = (
        'INSERT INTO '
        f'{expression_file_util.TableName.LAST_SCOPE.value}(last_scope) '
        f'VALUES({value.value});'
    )
    expression_file_util.cursor.execute(query)
    expression_file_util.connection.commit()
