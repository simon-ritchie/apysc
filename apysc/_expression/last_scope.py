"""This module is for interfaces and definitions for
a last expression's scope information.
"""

from enum import Enum
from typing import Optional
from typing import Tuple


class LastScope(Enum):
    NORMAL = 1
    IF = 2
    ELIF = 3
    ELSE = 4
    FOR = 5
    EVENT_HANDLER = 6
    FOR_ARRAY_INDICES = 7
    FOR_ARRAY_VALUES = 8
    FOR_ARRAY_INDICES_AND_VALUES = 9
    FOR_DICT_KEYS = 10
    FOR_DICT_VALUES = 11
    FOR_DICT_KEYS_AND_VALUES = 12


def reset() -> None:
    """
    Reset last expression's scope information.
    """
    from apysc._expression import expression_data_util

    query: str = f"DELETE FROM {expression_data_util.TableName.LAST_SCOPE.value};"
    expression_data_util.exec_query(sql=query)


def get_last_scope() -> LastScope:
    """
    Get last scope value.

    Returns
    -------
    last_scope : LastScope
        Last scope value. If there is no last scope's
        value, this interface returns LastScope.NORMAL.
    """
    from apysc._expression import expression_data_util

    query: str = (
        "SELECT last_scope FROM "
        f"{expression_data_util.TableName.LAST_SCOPE.value} "
        "LIMIT 1;"
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result is None:
        return LastScope.NORMAL
    last_scope: LastScope = LastScope(result[0])
    return last_scope


def set_last_scope(*, value: LastScope) -> None:
    """
    Set last scope value.

    Parameters
    ----------
    value : LastScope
        Last scope value to set.
    """
    from apysc._expression import expression_data_util

    reset()
    query: str = (
        "INSERT INTO "
        f"{expression_data_util.TableName.LAST_SCOPE.value}(last_scope) "
        f"VALUES({value.value});"
    )
    expression_data_util.exec_query(sql=query)
