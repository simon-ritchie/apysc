"""Handler circular calling related utilities.
"""

from typing import List, Tuple


def is_handler_circular_calling(handler_name: str) -> bool:
    """
    Get a boolean value whether a specified handler is
    a circular call or not.

    Parameters
    ----------
    handler_name : str
        Targer handler name.

    Returns
    -------
    result : bool
        If a specified handler is a circular call, True will be returned.
    """
    handler_names: List[str] = _read_handler_names()
    count: int = handler_names.count(handler_name)
    if count < 2:
        return False
    prev_handler_name: str = handler_names[-2]
    prev_handler_count: int = 0
    for i, handler_name_ in enumerate(handler_names):
        if i == 0:
            continue
        if handler_name_ != handler_name:
            continue
        prev_handler_name_: str = handler_names[i - 1]
        if prev_handler_name_ != prev_handler_name:
            continue
        prev_handler_count += 1
        if prev_handler_count == 2:
            break
    if prev_handler_count == 2:
        return True
    return False


def _read_handler_names() -> List[str]:
    """
    Read the current handler names from the calling stack.

    Returns
    -------
    handler_names : list of str
        Target handler names.
    """
    from apysc._expression import expression_data_util
    expression_data_util.initialize_sqlite_tables_if_not_initialized()
    table_name: str = expression_data_util.TableName.\
        HANDLER_CALLING_STACK.value
    query: str = (
        f'SELECT handler_name FROM {table_name} '
        f'ORDER BY scope_count'
    )
    expression_data_util.cursor.execute(query)
    result: List[Tuple[str]] = expression_data_util.cursor.fetchall()
    handler_names: List[str] = [tpl[0] for tpl in result]
    return handler_names
