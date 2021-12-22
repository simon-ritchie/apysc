"""Implementations for the count of the current loop number
(the For or the other loop class nested number).
"""

from typing import Optional
from typing import Tuple


def get_current_loop_count() -> int:
    """
    Get the current loop count number.

    Returns
    -------
    loop_count : int
        Current loop count.
    """
    from apysc._expression import expression_data_util
    query: str = (
        'SELECT count FROM '
        f'{expression_data_util.TableName.LOOP_COUNT.value} '
        'LIMIT 1;'
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result is None:
        return 0
    return result[0]


def _save_loop_count(*, loop_count: int) -> None:
    """
    Save a loop count value.

    Parameters
    ----------
    loop_count : int
        A loop count value.
    """
    from apysc._expression import expression_data_util
    table_name: str = expression_data_util.TableName.LOOP_COUNT.value
    query: str = f'DELETE FROM {table_name};'
    expression_data_util.exec_query(sql=query, commit=False)
    query = f'INSERT INTO {table_name}(count) VALUES ({loop_count});'
    expression_data_util.exec_query(sql=query)


def increment_current_loop_count() -> None:
    """
    Increment the current loop count number.
    """
    current_loop_count: int = get_current_loop_count()
    _save_loop_count(loop_count=current_loop_count + 1)


def decrement_current_loop_count() -> None:
    """
    Decrement the current loop count number.
    """
    current_loop_count: int = get_current_loop_count()
    current_loop_count -= 1
    current_loop_count = max(0, current_loop_count)
    _save_loop_count(loop_count=current_loop_count)
